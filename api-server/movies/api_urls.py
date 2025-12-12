from django.urls import path
from .views import MovieRecommendationsView, MovieListView, CombinedRecommendationsView, RecommendationHistoryView, RecommendationFeedbackView, ExternalMovieRecommendationView
from .admin_views import AdminRetrainView


urlpatterns = [
    path("<int:movie_id>/recommendations/", MovieRecommendationsView.as_view(), name="movie-recommendations"),             # Get the recommendations for one movie (by id)
    path("", MovieListView.as_view(), name="movie-list"),                                                                  # Get movies (can specify by title)
    path("recommendations/", CombinedRecommendationsView.as_view(), name="combined-recommendations"),                      # Get the recommendations for a list of movies
    path("recommendationhistory/", RecommendationHistoryView.as_view(), name="recommendation-history"),                    # Get the recommendation history of the user
    path("recommendationhistory/<int:history_id>/", RecommendationFeedbackView.as_view(), name="recommendation-feedback"), # Get specify recommendation 
    path("admin/retrain/", AdminRetrainView.as_view(), name="admin-retrain"),                                              # Ask to retrain the model
    path("external/", ExternalMovieRecommendationView.as_view()),                                                          # Get external recommendation (enter the title, should be sent in the body)
]
