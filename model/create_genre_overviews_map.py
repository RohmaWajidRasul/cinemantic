"""
Creates a map of K=genre, V=overviews from a IMDB movie dataset and stores it in a JSON file
"""

from datasets import load_dataset
from collections import defaultdict
import json

FILE_PATH = "movie_genre_index.json"

train_dataset = load_dataset("ExecuteAutomation/ImdbMovieDataSet", split="train")

genre_to_overview = defaultdict(list)
for movie in train_dataset:
    raw_genres = movie.get("genre", None)
    overview = movie.get("overview", None)
    
    if not raw_genres or not overview:
        continue

    cleaned_genres_string = movie["genre"].replace('\xa0', ',')
    genres = [g.strip() for g in cleaned_genres_string.split(',') if g.strip()]
    for genre in genres:
        genre_to_overview[genre].append(movie["overview"])


try:
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(genre_to_overview, f, indent=4)
    print("Successfully written to json file")
except Exception as e:
    print(e)