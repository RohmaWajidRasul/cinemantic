import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

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
conn.close()
