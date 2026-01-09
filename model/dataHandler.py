# Implemented by Bimnet, Filipe, Júlia and Rohma
import io
import pandas as pd
from sqlalchemy import text
from database import engine
import os
import numpy as np

def checkDuplicates(df):
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT overview FROM movies_movie")).fetchall()

    db_overviews = {row.overview for row in rows if row.overview}

    df = df[~df["overview"].isin(db_overviews)]

    return df


#load csv
def validateCSV(df):
    print(f"Initial size: {df.shape[0]}")
    df = checkDuplicates(df)

    if df.empty:
        raise Exception("No new data") 

    else:

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

def addMovies(df):
 
    df = df.drop(columns=["genres", "genres_list"])

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, header=False)
    csv_buffer.seek(0)

    raw_conn = engine.raw_connection()
    try:
        cursor = raw_conn.cursor()
        cursor.copy_expert(
            "COPY movies_movie FROM STDIN WITH CSV",
            csv_buffer
        )
        raw_conn.commit()
        cursor.close()
    finally:
        raw_conn.close()

def addGenres(df):
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
            text("INSERT INTO movies_movie_genres (movie_id, genre_id) VALUES (:movie_id, :genre_id) ON CONFLICT DO NOTHING"),
            junction_rows
        )

    

def updateEmb(recommender, only_new=False, new_ids=None):

    if only_new:
        sql = text("""
            SELECT m.id, m.overview,
                array_agg(g.name) FILTER (WHERE g.name IS NOT NULL) AS genres
            FROM movies_movie m
            LEFT JOIN movies_movie_genres mg ON m.id = mg.movie_id
            LEFT JOIN movies_genre g ON mg.genre_id = g.id
            WHERE m.id = ANY(:ids)
            GROUP BY m.id, m.overview;
        """)
        params = {"ids": new_ids}
    else:
        sql = text("""
                SELECT 
                    m.id,
                    m.overview,
                    array_agg(g.name) FILTER (WHERE g.name IS NOT NULL) AS genres
                FROM movies_movie m
                LEFT JOIN movies_movie_genres mg ON m.id = mg.movie_id
                LEFT JOIN movies_genre g ON mg.genre_id = g.id
                GROUP BY m.id, m.overview;
            """)
    
    with engine.connect() as conn:
        result = conn.execute(sql, params) if only_new else conn.execute(sql) 
        rows = result.fetchall()  

    recommender.df = pd.DataFrame({
        "id": [row.id for row in rows],
        "overview": [row.overview for row in rows],
        "genres_list": [row.genres if row.genres is not None else [] for row in rows]
    })

    # Compute embeddings
    recommender._compute_text_embeddings()
    recommender._compute_genre_embeddings()
    recommender._build_combined_vectors()

    # Update database embeddings
    newEmb = recommender.combined_vectors
    emb_updates = [{"id": movie_id, "embedding": emb.tolist()} for movie_id, emb in newEmb.items()]

    with engine.begin() as conn:
        for row in emb_updates:
            conn.execute(
                text("UPDATE movies_movie SET embedding = :embedding WHERE id = :id"),
                {"embedding": row["embedding"], "id": row["id"]}
            )

def updateRecsTable():

    print("UPDATING RECS TABLE")
    
    with engine.connect() as conn:
        # 1. Calculate recommendations into a temporary table using a single query.
        # This uses a LATERAL JOIN to find top 5 neighbors for every movie efficiently in the DB.
        conn.execute(text("""
            CREATE TEMP TABLE temp_recs AS
            SELECT
                m.id AS movie_id,
                r.id AS recommended_movie_id,
                1 - (m.embedding <=> r.embedding) AS similarity
            FROM movies_movie m
            CROSS JOIN LATERAL (
                SELECT id, embedding
                FROM movies_movie m2
                WHERE m2.id != m.id
                ORDER BY m.embedding <=> m2.embedding
                LIMIT 5
            ) r
        """))
        conn.commit()

        print("INSERTING NEW RECS")


        # 2. Atomic swap: Truncate and Insert from Temp
        with conn.begin():
            conn.execute(text("TRUNCATE TABLE movies_recommendation"))
            conn.execute(text("""
                INSERT INTO movies_recommendation (movie_id, recommended_movie_id, similarity)
                SELECT movie_id, recommended_movie_id, similarity FROM temp_recs
            """))
            conn.execute(text("DROP TABLE temp_recs"))

        print("DONE UPDATING RECS")



###TODO: CHANGE GENRES BULLSHIT TABLE SHIT
def getRecommended(movie_emb, conn, movie_id=None):
    recs = []

    if isinstance(movie_emb, np.ndarray):
        movie_emb = movie_emb.tolist()

    if movie_id is not None:
        sql = text("""
            SELECT id, embedding <=> (:vec)::vector AS distance
            FROM movies_movie
            WHERE embedding IS NOT NULL
              AND id != :id
            ORDER BY embedding <=> (:vec)::vector
            LIMIT 5;
        """)
        params = {"vec": movie_emb, "id": movie_id}

    else:
        sql = text("""
            SELECT id, embedding <=> (:vec)::vector AS distance
            FROM movies_movie
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> (:vec)::vector
            LIMIT 5;
        """)
        params = {"vec": movie_emb}

    rows = conn.execute(sql, params).fetchall()

    for row in rows:
        similarity = 1.0 - float(row.distance)
        recs.append({
            "id": int(row.id),
            "similarity": similarity
        })

    return recs
