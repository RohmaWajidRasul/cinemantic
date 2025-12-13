from django.urls import path
from .views import * 

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('login', LoginPageView.as_view(), name='login-page'),                
    path('register', RegisterPageView.as_view(), name='register-page'),
    path('profile', ProfilePageView.as_view(), name="profile-page"),
    path('recommendation', RecommendationPageView.as_view(), name="recommendation-page"),
    path('movies/<int:movie_id>/', MoviePageView.as_view(), name='movie-page'),    
    path('history', HistoryPageView.as_view(), name='history-page'),
    path('admin', AdminPageView.as_view(), name="admin-page"),
]
