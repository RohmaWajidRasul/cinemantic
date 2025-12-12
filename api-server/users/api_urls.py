from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserView, DeleteAllUsersView

urlpatterns = [
    path('me/', UserView.as_view(), name='get-user-profile'),                    # Get user info
    path('', RegisterView.as_view(), name='register'),                           # Post register form
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     # Post login form
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # Refresh the token (if both expire, ask user to login again)
    path('test/delete/', DeleteAllUsersView.as_view(), name='delete-all-users'), # Delete the account
]
