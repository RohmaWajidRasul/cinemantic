import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer, InputExample, losses
from sklearn.preprocessing import normalize
from sklearn.neighbors import NearestNeighbors
import random
from torch.utils.data import DataLoader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split


class MovieRecommender:
    """
    A recommender system that fine-tunes a sentence transformer model
    and provides movie recommendations based on textual descriptions and genres.
    """

    def __init__(self, df=None, genre_scale=0.5, default_model="all-MiniLM-L6-v2",
                 output_path="./fine_tuned_model", batch_size=128, epochs=2):
        
        if genre_scale <= 0 or batch_size < 1 or epochs < 1:
            raise Exception("Integer params must be greater than 0")

        self.genre_scale = genre_scale
        self.output_path = output_path
        self.batch_size = batch_size
        self.epochs = epochs
        self.df = df
        self.train_df= None
        self.val_df = None
        self.desc_embs = None
        self.genre_embs = None
        self.combined_vectors = None
        self.default_model = default_model
    
        try:
            self.old_model = SentenceTransformer(self.output_path)
            self.model = SentenceTransformer(self.output_path)
        except Exception as e:
            raise Exception(f"Invalid base model: {e}")      
          
    def _reset_old_model(self):
        print("Reset to old model...")
        self.model = self.old_model

    def _load_movies_from_dataframe(self):
        """Get data from dataframe"""

        self.df["id"] = self.df["id"].astype(int)
        self.df["title"] = self.df["title"].astype(str)
        self.df["genres"] = self.df["genres"].astype(str)
        self.df["overview"] = self.df["overview"].astype(str)

        # Filter genres
        self.df["genres_list"] = self.df["genres"].apply(lambda s: [g.strip() for g in s.split(",")])

        self.train_df, self.val_df = train_test_split(
            self.df,
            train_size=0.7,
            random_state=42,
            shuffle=True
        )
        self.train_df = self.train_df.reset_index(drop=True)
        self.val_df = self.val_df.reset_index(drop=True)

    def _build_training_pairs(self, df, num_pairs_per_movie=2):
        """
        Build positive training pairs for fine-tuning the sentence transformer.
        A positive pair consists of two movie overviews that share at least one genre.
        The model will be trained to learn that these pairs are similar.
        """

        # Create a map from genre to a list of movie indices that have that genre.
        # e.g., {'Action': [0, 5, 12], 'Comedy': [1, 5, 20]}
        genre_map = {}
        for idx, genres in df["genres_list"].items():
            for g in genres:
                genre_map.setdefault(g, []).append(idx)

        examples = []
        # Iterate through each movie to create training pairs.
        for idx, row in df.iterrows():
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
                examples.append(InputExample(texts=[row["overview"], df.iloc[pos_idx]["overview"]]))
        
        return examples

    def _fine_tune_model(self, training_examples):
        """Fine tune model using new tuples"""

        train_dataloader = DataLoader(training_examples, shuffle=True, batch_size=self.batch_size, pin_memory=False)
        train_loss = losses.MultipleNegativesRankingLoss(self.model)

        self.model.fit(
            train_objectives=[(train_dataloader, train_loss)],
            epochs=self.epochs,
            warmup_steps=100,
            output_path=self.output_path
        )

    def _compute_embeddings(self, ids, texts):
        """Helper to turn strings into vector embeddings"""

        embeddings_map = {}
    
        for i in range(0, len(texts), self.batch_size):
            batch_texts = texts[i : i + self.batch_size]
            batch_ids = ids[i : i + self.batch_size]
            batch_embs = self.model.encode(batch_texts, show_progress_bar=False)
            
            # Map each ID to its embedding
            embeddings_map.update({movie_id: emb for movie_id, emb in zip(batch_ids, batch_embs)})

        
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

    def setup_recommender(self, use_default=False):
        """Loads all data and prepares the recommender"""

        precision_before = None
        precision_after = None 

        if use_default:
            print(f"Using default model to fine tune: {self.default_model}")
            self.model = SentenceTransformer(self.default_model)

        self._load_movies_from_dataframe()
        training_examples = self._build_training_pairs(self.train_df)
        print(f"Found {len(training_examples)} training pairs.")
        
        # Get TF-IDF ground truth
        val_ids, mpnet_sim = self.build_mpnet_ground_truth(self.val_df)

        print("Precision@k before finetuning")
        val_embeddings = self._compute_val_embeddings()
        val_embeddings = normalize(val_embeddings)
        precision_before = self.precision_at_k(val_ids, mpnet_sim, val_embeddings)

        print("Fine-tuning model...")
        self._fine_tune_model(training_examples)

        print("Precision@k after finetuning")
        val_embeddings = self._compute_val_embeddings()
        val_embeddings = normalize(val_embeddings)
        precision_after = self.precision_at_k(val_ids, mpnet_sim, val_embeddings)

        return precision_before, precision_after

    ###EVALUATION###
    
    def build_mpnet_ground_truth(self, df=None):
        if df is None:
            df = self.val_df  # default to validation set

        movie_ids = df["id"].tolist()
        overviews = df["overview"].tolist()

        # Load the semantic model (all-mpnet-base-v2)
        mpnet_model = SentenceTransformer("all-mpnet-base-v2")

        # Encode all overviews
        emb = mpnet_model.encode(overviews, show_progress_bar=True, normalize_embeddings=True)

        # Compute cosine similarity matrix
        similarity_matrix = cosine_similarity(emb)

        # Optional: print stats
        print("MPNet similarity min, max, mean:", similarity_matrix.min(), similarity_matrix.max(), similarity_matrix.mean())

        return movie_ids, similarity_matrix


    def precision_at_k(self, val_ids, mpnet_sim, val_embeddings, k=5):
        """
        Compute mean Precision@k using top-k overlap with MPNet as semantic ground truth.

        Args:
            val_ids: list of movie IDs (not actually used here, only for reference)
            mpnet_sim: NxN similarity matrix computed from a strong semantic model (MPNet)
            val_embeddings: NxD embeddings from your current model
            k: number of top recommendations to consider

        Returns:
            mean_precision: mean Precision@k across all movies in val_df
        """
        # 1. Build ANN index for your model's embeddings
        ann = self._build_ann_index(val_embeddings, k)
        distances, indices = ann.kneighbors(val_embeddings)

        precisions = []

        for i in range(len(val_ids)):
            # 2. Get your model's top-k recommendations (exclude self)
            top = indices[i]
            top = top[top != i][:k]

            # 3. Get MPNet's top-k recommendations (exclude self)
            top_gt = np.argsort(-mpnet_sim[i])[1:k+1]  # indices of the k most similar movies according to MPNet

            # 4. Compute overlap
            # relevant[i] = True if your model's top-k includes this MPNet top-k neighbor
            relevant = np.isin(top, top_gt)

            # 5. Precision@k for this movie = fraction of your model's top-k that are in MPNet top-k
            precisions.append(relevant.mean())

        # 6. Mean Precision@k across all movies
        mean_precision = np.mean(precisions)
        print(f"Mean Precision@{k}: {mean_precision:.4f}")
        return mean_precision

    def _compute_val_embeddings(self):
        val_overviews = self.val_df["overview"].tolist()
        val_genres = [" ".join(g) for g in self.val_df["genres_list"]]

        desc = self.model.encode(val_overviews, show_progress_bar=False, convert_to_numpy=True)
        genre = self.model.encode(val_genres, show_progress_bar=False, convert_to_numpy=True)

        val_embeddings = desc + self.genre_scale * genre
        return val_embeddings

    def _build_ann_index(self, val_embeddings, k):
        ann = NearestNeighbors(
            n_neighbors=k + 1,
            metric="cosine",
            algorithm="auto"
        )
        ann.fit(val_embeddings)
        return ann


    def encodeNewMovie(self, ids, overview, genres):
        overview_emb = self.model.encode(overview, show_progress_bar=False)
        if isinstance(genres, list):
            genre_text = " ".join(genres)
        else:
            genre_text = genres 
        genre_emb = self.model.encode(genre_text, show_progress_bar=False)
        final_emb = overview_emb + self.genre_scale * genre_emb
        return final_emb
