from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserView, DeleteAllUsersView

urlpatterns = [
    path('me/', UserView.as_view()),

    path('', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('test/delete/', DeleteAllUsersView.as_view()),

]
