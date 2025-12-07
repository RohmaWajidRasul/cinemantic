import sqlite3
import pandas as pd

df = pd.read_csv("hf://datasets/ExecuteAutomation/ImdbMovieDataSet/imdb_movies.csv")

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

df.to_sql("movies", connection, if_exists="replace", index=False)

print(len(df), "Stored rows and", len(df.columns), "columns to movies.db.")
