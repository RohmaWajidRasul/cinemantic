import sys
import random
from movie_recommender import MovieRecommender

random.randint

try:
    input_movie = sys.argv[1] if len(sys.argv) > 1 else "Shazam!"
    recommender = MovieRecommender()
    recommender.setup_recommender()
    recommendations = recommender.recommend_by_title(input_movie)

    for rec in recommendations:
        print(rec)
        
except ValueError:
    print("Movie not in database.")