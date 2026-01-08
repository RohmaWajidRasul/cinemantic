from django.conf import settings
from django.db import transaction
from django.db.models import Count, Q
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
        precision_before = request.data.get("precision_before")
        precision_after = request.data.get("precision_after")

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

        with transaction.atomic():
            # Ensure only one current model
            if new_status == "current":
                ModelVersion.objects.filter(
                    status="current"
                ).exclude(
                    id=mv.id
                ).update(status="ready")

            mv.status = new_status

            if precision_before is not None:
                mv.precision_before = float(precision_before)

            if precision_after is not None:
                mv.precision_after = float(precision_after)

            mv.save()

        return Response(
            {
                "detail": f"Model version {version} is {new_status}.",
                "precision_before": mv.precision_before,
                "precision_after": mv.precision_after,
            },
            status=status.HTTP_200_OK
        )
    
class ModelVersionAdminListView(ListAPIView):
    serializer_class = ModelVersionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        
        return ModelVersion.objects.annotate(
            positive_count=Count('recommendationhistory', filter=Q(recommendationhistory__feedback="positive")),
            negative_count=Count('recommendationhistory', filter=Q(recommendationhistory__feedback="negative")),
            null_count=Count('recommendationhistory', filter=Q(recommendationhistory__feedback__isnull=True))
        ).order_by("-created_at")