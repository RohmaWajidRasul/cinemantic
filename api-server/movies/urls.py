from django.urls import path
from .views import MoviePageView, RecommendationPageView
from .admin_views import AdminRetrainView


urlpatterns = [
    path('movie', MoviePageView.as_view(), name='movie-page'),    
    path('recommendation', RecommendationPageView.as_view(), name='recommendation-page' )
]
