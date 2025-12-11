import pandas as pd
import io
from sqlalchemy import create_engine
from .settings import POSTGRES
import os

DATABASE_URL = (
    f"postgresql://{POSTGRES['USER']}:{POSTGRES['PASSWORD']}"
    f"@{POSTGRES['HOST']}:{POSTGRES['PORT']}/{POSTGRES['NAME']}"
)

#load csv
def validateCSV(df):
    print(f"Initial size: {df.shape[0]}")

    # Remove overviews without english translation
    df = df[~df["overview"].str.contains("We don't have an overview translated in English.", na=False)].copy()
    # Remove movies without genre
    df = df.dropna(subset=['genre'])
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
    return df

def insertCSV(df):
    tempcsv = "./tempCSV.csv"
    df.to_csv(tempcsv, index=False, header=False)  # no header

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    try:
        with engine.connect() as conn:
            conn.execute(
                f"COPY movies FROM '{os.path.abspath(tempcsv)}' WITH CSV"
            )
            conn.commit()
    finally:
        if os.path.exists(tempcsv):
            os.remove(tempcsv)
        conn.close()

def getRecommended(movie_emb):
    recs = []
    engine = create_engine(DATABASE_URL, echo=False, future=True)
    try:
        with engine.connect() as conn:
            conn.execute(
                f"SELECT * FROM movies ORDER BY embedding <=> '{movie_emb}' LIMIT 5"
            )
            conn.commit()
    finally:
        conn.close()
    return recs

def insertEmb():
    tempcsv = "./tempCSV.csv"
    df.to_csv(tempcsv, index=False, header=False)  # no header

    engine = create_engine(DATABASE_URL, echo=False, future=True)
    try:
        with engine.connect() as conn:
            conn.execute(
                f"COPY {table_name} FROM '{os.path.abspath(tempcsv)}' WITH CSV"
            )
            conn.commit()
    finally:
        if os.path.exists(tempcsv):
            os.remove(tempcsv)
        conn.close()
