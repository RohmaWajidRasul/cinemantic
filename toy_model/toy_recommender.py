import sqlite3
import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
from sklearn.neighbors import NearestNeighbors

SQLITE_PATH = "ToyModel/movies.db"
TABLE_NAME = "movies"
TEXT_EMB_PATH = "ToyModel/description_embeddings.npy"
GENRE_EMB_PATH = "ToyModel/genre_embeddingss.npy"
MODEL_NAME = "all-MiniLM-L6-v2"
BATCH_SIZE = 100
GENRE_SCALE = 0.5

def load_movies_from_sqlite(sqlite_path=SQLITE_PATH, table=TABLE_NAME):
    conn = sqlite3.connect(sqlite_path)
    df = pd.read_sql_query(f"SELECT id, names, genre, overview FROM {table} LIMIT 1000", conn)
    conn.close()

    df["id"] = df["id"].astype(int)
    df["names"] = df["names"].astype(str)
    df["genre"] = df["genre"].fillna("").astype(str)
    df["overview"] = df["overview"].fillna("").astype(str)

    df["genres_list"] = df["genre"].apply(lambda s: [g.strip() for g in s.split(",")])

    return df

def compute_embeddings(model, texts, batch_size=BATCH_SIZE):
    all_embs = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        batch_emb = model.encode(batch, show_progress_bar=False)
        all_embs.append(batch_emb)
    return np.vstack(all_embs)


def compute_text_embeddings(df, model, emb_path):
    if os.path.exists(emb_path):
        print("and here")
        embeddings = np.load(emb_path) 
        return embeddings
    
    descriptions = df["overview"].tolist()
    embeddings = compute_embeddings(model, descriptions)
    np.save(emb_path, embeddings)
    return embeddings


def compute_genre_embeddings(df, model, emb_path):
    if os.path.exists(emb_path):
        print("here")
        embeddings = np.load(emb_path) 
        return embeddings
    
    genre_texts = [" ".join(genres) for genres in df["genres_list"]]
    embeddings = compute_embeddings(model, genre_texts)
    np.save(emb_path, embeddings)
    return embeddings

def build_combined_vectors(desc_embeddings, genre_embeddings, genre_scale=GENRE_SCALE):
    combined = desc_embeddings + genre_scale * genre_embeddings
    return normalize(combined)

def fit_n_neighbours(combined_vectors, n_neighbors=20):
    neighbours = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine", n_jobs=-1)
    neighbours.fit(combined_vectors)
    return neighbours

def recommend_by_title(movie, df, combined_vectors, nn_index, top_k=10):
    matches = df[df["names"].str.lower() == movie.lower()]
    print(matches)
    if matches.empty:
        raise ValueError(f"name '{movie}' not found.")
    movie_idx = matches.index[0]

    query_vector = combined_vectors[movie_idx].reshape(1, -1)

    distances, indices = nn_index.kneighbors(query_vector, n_neighbors=top_k + 1)

    distances = distances[0]
    indices = indices[0]

    results = []

    for i in range(len(distances)):
        dist = distances[i]
        idx = indices[i]
        if idx == movie_idx:
            continue

        row = df.iloc[idx]
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

if __name__ == "__main__":
    df = load_movies_from_sqlite()

    model = SentenceTransformer(MODEL_NAME)
    desc_embs = compute_text_embeddings(df, model, TEXT_EMB_PATH)
    genre_embs = compute_genre_embeddings(df, model, GENRE_EMB_PATH)

    combined_vectors = build_combined_vectors(desc_embs, genre_embs)
    neighbours = fit_n_neighbours(combined_vectors, n_neighbors=30)

    input = "Scream VI"
    recs = recommend_by_title(input, df, combined_vectors, neighbours, top_k=5)
    for rec in recs:
        print(rec)
