# Implemented by Rohma
import sqlite3
import pandas as pd

def _save_csv_to_sqlite():
    conn = sqlite3.connect("movies.db")
    try:
        df = pd.read_csv("hf://datasets/ExecuteAutomation/ImdbMovieDataSet/imdb_movies.csv")
        df.to_sql("movies", conn, if_exists="replace", index=False)
        print(len(df), "Stored rows and", len(df.columns), "columns to movies.db.")
    finally:
        conn.close()

def _add_id():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
CREATE TABLE movies_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    names TEXT,
    date_x TEXT,
    score REAL,
    genre TEXT,
    overview TEXT,
    crew TEXT,
    orig_title TEXT,
    status TEXT,
    orig_lang TEXT,
    budget_x REAL,
    revenue REAL,
    country TEXT
);
    """)

        cursor.execute("""
        INSERT INTO movies_new (
            names, date_x, score, genre, overview, crew, orig_title,
            status, orig_lang, budget_x, revenue, country
        )
        SELECT
            names, date_x, score, genre, overview, crew, orig_title,
            status, orig_lang, budget_x, revenue, country
        FROM movies;
        """)

        cursor.execute("DROP TABLE movies;")
        cursor.execute("ALTER TABLE movies_new RENAME TO movies;")

        conn.commit()
    finally:
        conn.close()

def init_db():
    _save_csv_to_sqlite()
    _add_id()