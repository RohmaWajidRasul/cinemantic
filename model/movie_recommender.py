import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer, InputExample, losses
from sklearn.preprocessing import normalize
from sklearn.neighbors import NearestNeighbors
import random
from torch.utils.data import DataLoader

class MovieRecommender:
    """
    A recommender system that fine-tunes a sentence transformer model
    and provides movie recommendations based on textual descriptions and genres.
    """

    def __init__(self, df, genre_scale=0.5, model_name="all-MiniLM-L6-v2",
                 output_path="./fine_tuned_model", batch_size=64, epochs=2):
        
        if genre_scale <= 0 or batch_size < 1 or epochs < 1:
            raise Exception("Integer params must be greater than 0")

        self.genre_scale = genre_scale
        self.model_name = model_name
        self.output_path = output_path
        self.batch_size = batch_size
        self.epochs = epochs
        self.df = df

        self.model = None
        self.desc_embs = None
        self.genre_embs = None
        self.combined_vectors = None
        self.nn_index = None

    def _load_movies_from_dataframe(self):
        """Get data from dataframe"""

        self.df["id"] = self.df["id"].astype(int)
        self.df["names"] = self.df["names"].astype(str)
        self.df["genre"] = self.df["genre"].astype(str)
        self.df["overview"] = self.df["overview"].astype(str)

        # Filter genres
        self.df["genres_list"] = self.df["genre"].apply(lambda s: [g.strip() for g in s.split(",")])

    def _build_training_pairs(self, num_pairs_per_movie=2):
        """
        Build positive training pairs for fine-tuning the sentence transformer.
        A positive pair consists of two movie overviews that share at least one genre.
        The model will be trained to learn that these pairs are similar.
        """

        # Create a map from genre to a list of movie indices that have that genre.
        # e.g., {'Action': [0, 5, 12], 'Comedy': [1, 5, 20]}
        genre_map = {}
        for idx, genres in self.df["genres_list"].items():
            for g in genres:
                genre_map.setdefault(g, []).append(idx)

        examples = []
        # Iterate through each movie to create training pairs.
        for idx, row in self.df.iterrows():
            genres = row["genres_list"]
            # Find all other movies that share at least one genre with the current movie.
            candidates = set()
            for g in genres:
                candidates.update(genre_map.get(g, []))
            
            candidates.discard(idx)

            # If no other movies share a genre, we can't create a pair.
            if not candidates:
                continue

            # Randomly select a few candidates to form pairs with the current movie.
            selected = random.sample(list(candidates), min(num_pairs_per_movie, len(candidates)))
            for pos_idx in selected:
                examples.append(InputExample(texts=[row["overview"], self.df.iloc[pos_idx]["overview"]]))
        
        return examples

    def _fine_tune_model(self, training_examples):
        """Fine tune model using new tuples"""

        model = SentenceTransformer(self.model_name)
        train_dataloader = DataLoader(training_examples, shuffle=True, batch_size=self.batch_size, pin_memory=False)
        train_loss = losses.MultipleNegativesRankingLoss(model)

        model.fit(
            train_objectives=[(train_dataloader, train_loss)],
            epochs=self.epochs,
            warmup_steps=100,
            output_path=self.output_path
        )
        self.model = SentenceTransformer(self.output_path)

    def _compute_embeddings(self, texts):
        """Helper to turn strings into vector embeddings"""

        embeddings_map = {}
    
        for i in range(0, len(texts), self.batch_size):
            batch_texts = texts[i : i + self.batch_size]
            batch_ids = ids[i : i + self.batch_size]
            batch_embs = self.model.encode(batch_texts, show_progress_bar=False)
            
            # Map each ID to its embedding
            for movie_id, emb in zip(batch_ids, batch_embs):
                embeddings_map[movie_id] = emb
        
        return embeddings_map

    def _compute_text_embeddings(self):
        """Responsible for encoding the movies' overviews"""

        print("Computing text embeddings...")
        ids = self.df["movie_id"].tolist()  # get the IDs
        descriptions = self.df["overview"].tolist()
        self.desc_embs = self._compute_embeddings(ids, descriptions)
        

    def _compute_genre_embeddings(self):
        """Responsible for encoding the movies' genres"""

        print("Computing genre embeddings...")
        ids = self.df["movie_id"].tolist()  # same IDs as above
        genre_texts = [" ".join(genres) for genres in self.df["genres_list"]]
        self.genre_embs = self._compute_embeddings(ids, genre_texts)


    def _build_combined_vectors(self):
        """Combine overview and genre embeddings to get a unified vector"""

        if self.desc_embs is None or self.genre_embs is None:
            raise ValueError("Embeddings not computed or loaded.")

        combined_map = {}
        for movie_id in self.desc_embs:
            desc_emb = self.desc_embs[movie_id]
            genre_emb = self.genre_embs.get(movie_id, 0)  # default 0 if missing
            combined_map[movie_id] = desc_emb + self.genre_scale * genre_emb

        # Convert to NumPy array (rows in same order as movie IDs)
        self.combined_vectors = normalize(np.vstack(list(combined_map.values())))
        self.combined_ids = list(combined_map.keys())  # keep IDs aligned
        
    ###TODO:REPLACE for PGvectors
    def _fit_n_neighbours(self, n_neighbors=20):
        """Uses cosine similarity to find nearest neighbours (aka similar movies)"""

        if self.combined_vectors is None:
            raise ValueError("Combined vectors not built.")

        self.nn_index = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine", n_jobs=-1)
        self.nn_index.fit(self.combined_vectors)

    ###TODO:ALTER
    def recommend_by_title(self, movie, top_k=5):
        """Get recommendations for a given movie title"""

        if self.df is None or self.combined_vectors is None or self.nn_index is None:
            raise ValueError("Recommender not set up. Call load_movies, compute embeddings, and fit_n_neighbours first.")

        matches = self.df[self.df["names"].str.lower() == movie.lower()]
        if matches.empty:
            raise ValueError(f"Movie with name '{movie}' not found.")
        
        movie_idx = matches.index[0]
        query_vector = self.combined_vectors[movie_idx].reshape(1, -1)

        distances, indices = self.nn_index.kneighbors(query_vector, n_neighbors=top_k + 1)
        distances = distances[0]
        indices = indices[0]

        results = []
        for i in range(len(distances)):
            dist = distances[i]
            idx = indices[i]
            if idx == movie_idx:
                continue

            row = self.df.iloc[idx]
            similarity = 1 - dist
            results.append({
                "id": int(row["id"]),
                "names": row["names"],
                "genre": row["genres_list"],
                "similarity": float(similarity)
            })
            if len(results) >= top_k:
                break
        return results

    def setup_recommender(self, fine_tune=False):
        """Loads all data and prepares the recommender"""

        if fine_tune:
            self._load_movies_from_dataframe()
            training_examples = self._build_training_pairs()
            print(f"Found {len(training_examples)} training pairs.")
            
            print("Fine-tuning model...")
            self._fine_tune_model(training_examples)
        else:
            self._load_movies_from_dataframe()
            # If not fine-tuning, try to load a pre fine-tuned model
            try:
                self.model = SentenceTransformer(self.output_path)
            except Exception as e:
                raise Exception(f"The specified fine-tuned model does not exist: {e}")
            
        self._compute_text_embeddings()
        self._compute_genre_embeddings()
        self._build_combined_vectors()
        self._fit_n_neighbours()