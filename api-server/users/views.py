# Implemented by Rohma
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, ProfileSerializer, UserUpdateSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Profile

User = get_user_model()

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile)
        return Response({"profile": serializer.data}, status=200)

    def patch(self, request):
        user_serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        profile = get_object_or_404(Profile, user=request.user)
        profile_serializer = ProfileSerializer(profile, data=request.data, partial=True)

        errors = {}
        if not user_serializer.is_valid():
            errors["user_errors"] = user_serializer.errors
        if not profile_serializer.is_valid():
            errors["profile_errors"] = profile_serializer.errors

        if errors:
            return Response(errors, status=400)

        user_serializer.save()
        profile_serializer.save()

        return Response({"detail": "Profile updated successfully"}, status=200)
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class DeleteAllUsersView(APIView):
    permission_classes = [permissions.AllowAny]
    def delete(self, request):
        count, _ = User.objects.all().delete()
        return Response({'detail': f'{count} users deleted'}, status=200)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        access = data.get("access")
        refresh = data.get("refresh")

        response = Response(
            {
                "user": data.get("user")
            },
            status=200
        )

        response.set_cookie(
            key="access",
            value=access,
            httponly=True,
            samesite="Lax",
            secure=False  # True in production
        )

        response.set_cookie(
            key="refresh",
            value=refresh,
            httponly=True,
            samesite="Lax",
            secure=False
        )

        return response
    
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh = request.COOKIES.get("refresh")

        if refresh is None:
            return Response({"detail": "No refresh token"}, status=401)

        serializer = self.get_serializer(data={"refresh": refresh})
        serializer.is_valid(raise_exception=True)

        access = serializer.validated_data["access"]

        response = Response(status=200)
        response.set_cookie(
            key="access",
            value=access,
            httponly=True,
            samesite="Lax",
            secure=False
        )

        return response
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"detail": "Logged out"}, status=200)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
