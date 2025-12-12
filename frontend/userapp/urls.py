from django.urls import path
from .views import * 

urlpatterns = [
    path('homepage', HomePageView.as_view(), name='homepage'),
    path('login', LoginPageView.as_view(), name='login-page'),                
    path('register', RegisterPageView.as_view(), name='register-page'),
    path('account', AccountPageView.as_view(), name="user-page"),
    path('chat', ChatPageView.as_view(), name="chat-page"),
    path('movie', MoviePageView.as_view(), name='movie-page'),    
    path('recommendation', RecommendationPageView.as_view(), name='recommendation-page' )
]
