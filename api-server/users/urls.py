from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginPageView, RegisterPageView, AccountPageView

urlpatterns = [
    path('login', LoginPageView.as_view(), name='login-page'),                
    path('register', RegisterPageView.as_view(), name='register-page'),
    path('account', AccountPageView.as_view(), name="user-page"),
]
