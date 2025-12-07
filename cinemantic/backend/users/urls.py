from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserLikesView, RegisterView, UserView, DeleteAllUsersView

urlpatterns = [
    path('me/', UserView.as_view(), name='get-user-profile'),

    path('movies/<int:movie_id>/', UserLikesView.as_view(), name='movie-like-unlike'),
    path('movies/', UserLikesView.as_view(), name='get-liked-movies'),

    path('', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('test/delete/', DeleteAllUsersView.as_view(), name='delete-all-users'),

]
