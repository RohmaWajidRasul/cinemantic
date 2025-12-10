from django.urls import path
from .views import MovieRecommendationsView, MovieListView, CombinedRecommendationsView, RecommendationHistoryView, RecommendationFeedbackView, ExternalMovieRecommendationView
from .admin_views import AdminRetrainView


urlpatterns = [
    path("<int:movie_id>/recommendations/", MovieRecommendationsView.as_view(), name="movie-recommendations"),
    path("", MovieListView.as_view(), name="movie-list"),
    path("recommendations/", CombinedRecommendationsView.as_view(), name="combined-recommendations"),
    path("recommendationhistory/", RecommendationHistoryView.as_view(), name="recommendation-history"),
    path("recommendationhistory/<int:history_id>/", RecommendationFeedbackView.as_view(), name="recommendation-feedback"),
    path("admin/retrain/", AdminRetrainView.as_view(), name="admin-retrain"),
    path("external/", ExternalMovieRecommendationView.as_view()),

]
