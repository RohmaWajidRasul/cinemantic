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

    def __init__(self, df=None, genre_scale=0.5, model_name="all-MiniLM-L6-v2",
                 output_path="./fine_tuned_model", batch_size=128, epochs=2):
        
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

        if self.df is None:
            try:
                self.model = SentenceTransformer(self.output_path)
            except Exception:
                self.model = SentenceTransformer(self.model_name)

    def _load_movies_from_dataframe(self):
        """Get data from dataframe"""

        self.df["id"] = self.df["id"].astype(int)
        self.df["title"] = self.df["title"].astype(str)
        self.df["genres"] = self.df["genres"].astype(str)
        self.df["overview"] = self.df["overview"].astype(str)

        # Filter genres
        self.df["genres_list"] = self.df["genres"].apply(lambda s: [g.strip() for g in s.split(",")])

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

    def _compute_embeddings(self, ids, texts):
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
        ids = self.df["id"].tolist()  # get the IDs
        descriptions = self.df["overview"].tolist()
        self.desc_embs = self._compute_embeddings(ids, descriptions)
        

    def _compute_genre_embeddings(self):
        """Responsible for encoding the movies' genres"""

        print("Computing genre embeddings...")
        ids = self.df["id"].tolist()  # same IDs as above
        genre_texts = [" ".join(genres) for genres in self.df["genres_list"]]
        self.genre_embs = self._compute_embeddings(ids, genre_texts)


    def _build_combined_vectors(self):
        """Combine overview and genre embeddings to get a unified vector"""

        if self.desc_embs is None or self.genre_embs is None:
            raise ValueError("Embeddings not computed or loaded.")

        combined_map = {}
        for movie_id in self.desc_embs:
            desc_emb = self.desc_embs[movie_id]
            genre_emb = self.genre_embs.get(movie_id)  # default 0 if missing
            combined_map[movie_id] = desc_emb + self.genre_scale * genre_emb

        self.combined_vectors = combined_map

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

    def encodeNewMovie(self, ids, overview, genres):
        overview_emb = self.model.encode(overview, show_progress_bar=False)
        if isinstance(genres, list):
            genre_text = " ".join(genres)
        else:
            genre_text = genres 
        genre_emb = self.model.encode(genre_text, show_progress_bar=False)
        final_emb = overview_emb + self.genre_scale * genre_emb
        return final_emb
