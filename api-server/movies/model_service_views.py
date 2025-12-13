from django.conf import settings
from .models import ModelVersion
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ModelVersionSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class ModelVersionUpdateView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, version):

        secret = request.headers.get("X-MODEL-SECRET")
        if secret != settings.MODEL_UPDATE_SECRET:
            return Response(
                {"error": "Unauthorized"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            mv = ModelVersion.objects.get(version=version)
        except ModelVersion.DoesNotExist:
            return Response({"error": "Version not found"}, status=status.HTTP_404_NOT_FOUND)
        
        new_status = request.data.get("status")

        if new_status is None:
            return Response(
                {"error": "Missing 'status' in request body"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        valid_statuses = dict(ModelVersion.STATUS_CHOICES).keys()
        if new_status not in valid_statuses:
            return Response(
                {"error": f"Invalid status. Must be one of {list(valid_statuses)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        mv.status = new_status
        mv.save()

        return Response({"detail": f"Model version {version} is {new_status}."}, status=status.HTTP_200_OK)
    
class ModelVersionListView(ListAPIView):
    queryset = ModelVersion.objects.all().order_by("-created_at")
    serializer_class = ModelVersionSerializer
    permission_classes = [IsAdminUser]