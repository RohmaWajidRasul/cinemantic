from django.urls import path
from .views import MovieRecommendationsView, MovieListView, CombinedRecommendationsView

urlpatterns = [
    path("<int:movie_id>/recommendations/", MovieRecommendationsView.as_view(), name="movie-recommendations"),
    path("", MovieListView.as_view(), name="movie-list"),
    path("recommendations/", CombinedRecommendationsView.as_view(), name="combined-recommendations"),

]
