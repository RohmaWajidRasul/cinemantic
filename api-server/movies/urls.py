from django.urls import path
from .views import MovieRecommendationsView, MovieListView, MovieDetailView, CombinedRecommendationsView, RecommendationHistoryView, RecommendationHistoryDetailView, ExternalMovieRecommendationView
from .admin_views import AdminRetrainView
from .model_service_views import ModelVersionUpdateView, ModelVersionListView



urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),

    path("movies/<int:movie_id>/recommendations/", MovieRecommendationsView.as_view()),
    path("movies/recommendations/", CombinedRecommendationsView.as_view()),
    path("movies/external/", ExternalMovieRecommendationView.as_view()),


    path("movies/recommendationhistory/", RecommendationHistoryView.as_view()),
    path("movies/recommendationhistory/<int:history_id>/", RecommendationHistoryDetailView.as_view()),

    path("admin/fine-tune/", AdminRetrainView.as_view()),
    path("admin/model-versions/", ModelVersionListView.as_view()),

    path("admin/model-versions/<str:version>/", ModelVersionUpdateView.as_view()),
]
