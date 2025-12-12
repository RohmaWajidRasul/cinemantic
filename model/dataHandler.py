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
        df['release_date'] = df['release_date'].str.strip()
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

    df = df.drop(columns=["genres"])
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
    engine = create_engine(DATABASE_URL, echo=False, future=True)

    df = df[["id", "genres"]].copy()
    # parse genres lists
    df['genre_list'] = df['genres'].apply(lambda s: [g.strip() for g in str(s).split(",")])

    # gather unique genres
    unique_genres = set(g for lst in df['genre_list'] for g in lst)

    with engine.connect() as conn:
        existing = conn.execute(text("SELECT id, name FROM movies_genre")).fetchall()
    existing_map = {r.name: r.id for r in existing}

    # insert missing genres and update map
    missing = [g for g in unique_genres if g not in existing_map]
    if missing:
        with engine.begin() as conn:
            for g in missing:
                res = conn.execute(text("INSERT INTO movies_genre (name) VALUES (:name) RETURNING id"), {"name": g})
                new_id = res.fetchone().id
                existing_map[g] = new_id

    # prepare rows for junction table
    junction_rows = []
    for _, row in df.iterrows():
        movie_id = row['id']
        for g in row['genre_list']:
            gid = existing_map[g]
            junction_rows.append({"movie_id": movie_id, "genre_id": gid})

    # batch insert into junction table (use ON CONFLICT to avoid duplicates if desired)
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO movies_movie_genre (movie_id, genre_id) VALUES (:movie_id, :genre_id) ON CONFLICT DO NOTHING"),
            junction_rows
        )

    

def updateEmb(recommender):

    newEmb = recommender.combined_vectors

    engine = create_engine(DATABASE_URL, echo=False, future=True)

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, overview, genres FROM movies")
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
            GEmb = updatedGenresEmb.get(movie_id)  
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
        rows = conn.execute(text("SELECT id, embedding FROM movies")).fetchall()

    # truncate table
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE movies_recommendation"))

    insert_rows = []
    for row in rows:
        origin_id = row.id
        recs = getRecommended(row.embedding)
        for rec in recs:
            insert_rows.append({
                "movie_id": origin_id,
                "recommended_movie": rec["id"],
                "similarity": rec["similarity"]
            })

    # batch insert
    with engine.begin() as conn:
        conn.execute(
            text("""
            INSERT INTO movies_recommendation (movie_id, recommended_movie, similarity)
            VALUES (:movie_id, :recommended_movie, :similarity)
            """),
            insert_rows
        )


###TODO: CHANGE GENRES BULLSHIT TABLE SHIT
def getRecommended(movie_emb):

    recs = []
    engine = create_engine(DATABASE_URL, echo=False, future=True)

    # Important: PGVector expects Python list, not numpy array
    if isinstance(movie_emb, np.ndarray):
        movie_emb = movie_emb.tolist()
    
    sql = text("""
            SELECT id, title, release_date, score, genres, overview, crew, original_language, embedding <=> :vec AS distance
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
        row = conn.execute(sql).fetchone()
        
    return row.version if row else None
