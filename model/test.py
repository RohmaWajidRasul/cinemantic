from movie_recommender import MovieRecommender

recommender = MovieRecommender()
recommender.setup_recommender()

input_movie = "Avatar"
recommendations = recommender.recommend_by_title(input_movie)

for rec in recommendations:
    print(rec)