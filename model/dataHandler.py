import pandas as pd
import io
from sqlalchemy import create_engine, text
from .settings import POSTGRES
import os
import numpy as np
import json


DATABASE_URL = (
    f"postgresql://{POSTGRES['USER']}:{POSTGRES['PASSWORD']}"
    f"@{POSTGRES['HOST']}:{POSTGRES['PORT']}/{POSTGRES['NAME']}"
)

#load csv
def validateCSV(df):
    print(f"Initial size: {df.shape[0]}")

    required_cols = set(["id", "title", "release_date", "score", "overview", "crew", "original_language", "poster_url", "genres"])
    if required_cols.issubset(df.columns):

        # Remove overviews without english translation
        df = df[~df["overview"].str.contains("We don't have an overview translated in English.", na=False)].copy()
        # Remove movies without genre
        df = df.dropna(subset=['genres'])
        # Clean white spaces
        df['date_x'] = df['date_x'].str.strip()
        # Remove duplicate rows (overview column is supposed to be unique)
        df = df.drop_duplicates(subset=['overview'])
        # Remove duplicate rows (id column is supposed to be unique)
        df = df.drop_duplicates(subset=['id'])
        # Ensure 'score' column only has values between 0-100
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df.loc[(df['score'] < 0) | (df['score'] > 100), 'score'] = pd.NA
        print(f"Final size: {df.shape[0]}")

    else:
        raise Exception("Invalid data") 

    return df

###TODO: GENRES BULLSHIT
def addMovies(df):

    tempcsv = "./tempCSV.csv"
    df.to_csv(tempcsv, index=False, header=False)  # no header

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    with engine.begin() as conn:
        conn.execute(
            f"COPY movies FROM '{os.path.abspath(tempcsv)}' WITH CSV"
        )
    if os.path.exists(tempcsv):
        os.remove(tempcsv)

def addGenres(df):

    df = df[["id", "genres"]]

    tempcsv = "./tempCSV.csv"
    df.to_csv(tempcsv, index=False, header=False)  # no header

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    with engine.begin() as conn:
        conn.execute(
            f"COPY movies_genres FROM '{os.path.abspath(tempcsv)}' WITH CSV"
        )
    if os.path.exists(tempcsv):
        os.remove(tempcsv)

def updateEmb(recommender):

    newEmb = recommender.combined_vectors

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(
            "SELECT id, overview, genres FROM movies"
        )

        rows = result.fetchall()  # returns a list of Row objects
        ids = [row.id for row in rows]
        overviews = [row.overview for row in rows]
        genres = [row.genres for row in rows]

        updatedOverviewsEmb = recommender._compute_embeddings(ids, overviews)
        updatedGenresEmb = recommender._compute_embeddings(ids, genres)

        updatedOldEmb = {}
        for movie_id in updatedOverviewsEmb:
            OvEmb = updatedOverviewsEmb[movie_id]
            GEmb = updatedGenresEmb.get(movie_id, 0)  
            updatedOldEmb[movie_id] = OvEmb + recommender.genre_scale * GEmb

    newEmb.update(updatedOldEmb)

    # --- Step 1: Prepare data for SQL ---
    emb_updates = []
    for movie_id, emb in newEmb.items():
        emb_json = json.dumps(emb.tolist())  # convert numpy array to JSON string
        emb_updates.append({"id": movie_id, "embedding": emb_json})

    # --- Step 2: Execute batch update ---
    with engine.begin() as conn:  # begin transaction
        for row in emb_updates:
            conn.execute(
                text("UPDATE movies SET embedding = :embedding WHERE id = :id"),
                {"embedding": row["embedding"], "id": row["id"]}
            )



def updateRecsTable():

    engine = create_engine(DATABASE_URL, echo=False, future=True)

    with engine.connect() as conn:
        result = conn.execute(
            "SELECT id, embedding FROM movies"
        )

        # Fetch all returned rows (at most top_k)
        rows = result.fetchall()

    with engine.begin() as conn:
        conn.execute("TRUNCATE TABLE movies_recommendation")

    # Build the list of recommendations from returned rows
    with engine.begin() as conn:  # begin transaction
        for row in rows:
            origin_id = row.id
            recs = getRecommended(row.embedding)
            for rec in recs:
                rec_id = rec.id
                similarity = rec.similarity

                conn.execute(
                    text("UPDATE movies_recommendation " \
                    "SET recommended_movie = :recommended, similarity = :similarity" \
                    "WHERE id = :id"),
                    {"recommended": rec_id, "similarity": similarity,"id": origin_id}
                )

###TODO: CHANGE GENRES BULLSHIT TABLE SHIT
def getRecommended(movie_emb):

    recs = []
    engine = create_engine(DATABASE_URL, echo=False, future=True)

    # Important: PGVector expects Python list, not numpy array
    if isinstance(movie_emb, np.ndarray):
        movie_emb = movie_emb.tolist()
    
    sql = text("""
            SELECT *, embedding <=> :vec AS distance
            FROM movies
            ORDER BY embedding <=> :vec
            LIMIT 5;
        """)

    with engine.connect() as conn:
        result = conn.execute(sql, {"vec": movie_emb})

        # Fetch all returned rows (at most top_k)
        rows = result.fetchall()

        # Build the list of recommendations from returned rows
        for row in rows:
            # `row` supports name-based access (row['distance'] or row.distance)
            dist = row.distance               # PGVector returns a distance (lower = more similar)
            similarity = 1.0 - float(dist)    # convert distance -> similarity (0..1 approx)

            recs.append({
                "id": int(row.id),
                "title": row.title,
                "release_date": row.release_date,
                "score": row.score,
                "genres": row.genres.split(",") if isinstance(row.genres, str) else row.genres,
                "overview": row.overview,
                "crew": row.crew,
                "original_language": row.original_language,
                "similarity": similarity
            })

    return recs

def getVersion():

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    sql = text("""
        SELECT version
        FROM movies_modelversion
        WHERE status = 'fine-tuning'
        ORDER BY created_at DESC
        LIMIT 1;
    """)
    with engine.connect() as conn:
        result = conn.execute(sql)
        row = result.fetchone()
        version = row.version

    return version