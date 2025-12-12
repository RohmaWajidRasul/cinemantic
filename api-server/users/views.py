from rest_framework import generics, permissions, status
from .serializers import RegisterSerializer, ProfileSerializer, UserUpdateSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from movies.serializers import MovieSerializer
from movies.models import Movie
from django.http import HttpResponse
from django.template import loader

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
