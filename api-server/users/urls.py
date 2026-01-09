# Implemented by Rohma
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, UserView, DeleteAllUsersView, CustomTokenObtainPairView, LogoutView

urlpatterns = [
    path('me/', UserView.as_view()),

    path('', RegisterView.as_view()),
    path('token/', CustomTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view()),


    path('test/delete/', DeleteAllUsersView.as_view()),
]
