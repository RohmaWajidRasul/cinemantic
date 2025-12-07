import sqlite3
import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer, InputExample, losses
from sklearn.preprocessing import normalize
from sklearn.neighbors import NearestNeighbors
import random
from torch.utils.data import DataLoader
from save_to_sqlite import init_db

class MovieRecommender:
    """
    A recommender system that fine-tunes a sentence transformer model
    and provides movie recommendations based on textual descriptions and genres.
    """

    def __init__(self, sqlite_path="./movies.db", table_name="movies", 
                 genre_scale=0.5, model_name="all-MiniLM-L6-v2",
                 output_path="./fine_tuned_model", limit=6000,
                 batch_size=64, epochs=2):
        
        if genre_scale <= 0 or limit < 1 or batch_size < 1 or epochs < 1:
            raise Exception("Integer params must be greater than 0")

        self.sqlite_path = sqlite_path
        self.table_name = table_name
        self.text_emb_path = f"{output_path}/desc_embeddings.npy"
        self.genre_emb_path = f"{output_path}/genre_embeddings.npy"
        self.genre_scale = genre_scale
        self.model_name = model_name
        self.output_path = output_path
        self.limit = limit
        self.batch_size = batch_size
        self.epochs = epochs

        self.df = None
        self.model = None
        self.desc_embs = None
        self.genre_embs = None
        self.combined_vectors = None
        self.nn_index = None

    def _load_movies_from_sqlite(self, limit):
        """Turn movies into an SQLite database"""

        try:
            conn = sqlite3.connect(self.sqlite_path)
            query = f"SELECT id, names, genre, overview FROM {self.table_name} LIMIT {limit}"
            self.df = pd.read_sql_query(query, conn)
        finally:
            conn.close()

        self.df["id"] = self.df["id"].astype(int)
        self.df["names"] = self.df["names"].astype(str)
        self.df["genre"] = self.df["genre"].fillna("").astype(str)
        self.df["overview"] = self.df["overview"].fillna("").astype(str)

        self.df["genres_list"] = self.df["genre"].apply(lambda s: [g.strip() for g in s.split(",")])

    def _build_training_pairs(self, num_pairs_per_movie=2):
        """Build training pairs from dataframe"""

        genre_map = {}
        for idx, genres in self.df["genres_list"].items():
            for g in genres:
                genre_map.setdefault(g, []).append(idx)

        examples = []
        for idx, row in self.df.iterrows():
            genres = row["genres_list"]
            candidates = set()
            for g in genres:
                candidates.update(genre_map.get(g, []))
            
            candidates.discard(idx)

            if not candidates:
                continue

            selected = random.sample(list(candidates), min(num_pairs_per_movie, len(candidates)))
            for pos_idx in selected:
                examples.append(InputExample(texts=[row["overview"], self.df.iloc[pos_idx]["overview"]]))
        
        return examples

    def _fine_tune_model(self, training_examples):
        """Fine tune model using new tuples"""

        # Clean up old embeddings for this model path if they exist
        if os.path.exists(self.text_emb_path):
            os.remove(self.text_emb_path)
        if os.path.exists(self.genre_emb_path):
            os.remove(self.genre_emb_path)

        model = SentenceTransformer(self.model_name)
        train_dataloader = DataLoader(training_examples, shuffle=True, batch_size=self.batch_size)
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

        all_embs = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            batch_emb = self.model.encode(batch, show_progress_bar=False)
            all_embs.append(batch_emb)
        return np.vstack(all_embs)

    def _compute_text_embeddings(self):
        """Responsible for encoding the movies' overviews"""

        if os.path.exists(self.text_emb_path):
            print("Loading cached text embeddings...")
            self.desc_embs = np.load(self.text_emb_path)
            return

        print("Computing text embeddings...")
        descriptions = self.df["overview"].tolist()
        self.desc_embs = self._compute_embeddings(descriptions)
        np.save(self.text_emb_path, self.desc_embs)

    def _compute_genre_embeddings(self):
        """Responsible for encoding the movies' genres"""

        if os.path.exists(self.genre_emb_path):
            print("Loading cached genre embeddings...")
            self.genre_embs = np.load(self.genre_emb_path)
            return

        print("Computing genre embeddings...")
        genre_texts = [" ".join(genres) for genres in self.df["genres_list"]]
        self.genre_embs = self._compute_embeddings(genre_texts)
        np.save(self.genre_emb_path, self.genre_embs)

    def _build_combined_vectors(self):
        """Combine overview and genre embeddings to get a unified vector"""

        if self.desc_embs is None or self.genre_embs is None:
            raise ValueError("Embeddings not computed or loaded.")
        
        combined = self.desc_embs + self.genre_scale * self.genre_embs
        self.combined_vectors = normalize(combined)

    def _fit_n_neighbours(self, n_neighbors=20):
        """Uses cosine similarity to find nearest neighbours (aka similar movies)"""

        if self.combined_vectors is None:
            raise ValueError("Combined vectors not built.")

        self.nn_index = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine", n_jobs=-1)
        self.nn_index.fit(self.combined_vectors)

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
            init_db()
            self._load_movies_from_sqlite(self.limit)
            training_examples = self._build_training_pairs()
            print(f"Found {len(training_examples)} training pairs.")
            
            print("Fine-tuning model...")
            self._fine_tune_model(training_examples)
        else:
            self._load_movies_from_sqlite(self.limit)
            # If not fine-tuning, try to load a pre fine-tuned model
            try:
                self.model = SentenceTransformer(self.output_path)
            except Exception as e:
                raise Exception(f"The specified fine-tuned model does not exist: {e}")
            
        self._compute_text_embeddings()
        self._compute_genre_embeddings()
        self._build_combined_vectors()
        self._fit_n_neighbours()