import requests
from django.conf import settings
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import ModelVersion

class AdminRetrainView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "CSV file is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        base_model_version = request.POST.get("base_model")
        batch_size = request.POST.get("batch_size")
        epochs = request.POST.get("epochs")

        if not base_model_version:
            return Response(
                {"error": "base_model is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if base_model_version.lower() != "default":
            try:
                base_model = ModelVersion.objects.get(
                    version=base_model_version,
                    status__in=["ready", "current"]
                )
            except ModelVersion.DoesNotExist:
                return Response({"error": "Base model unavailable."}, status=status.HTTP_400_BAD_REQUEST)
            parent_model = base_model

        else:
            base_model = None
            parent_model = None 

        # Reserve a new version
        new_version = self.create_new_model_version(parent_model)

        ai_url = settings.AI_SERVICE_URL + "/api/v1/fine-tune/"
        data = {
            "base_model": base_model.version if base_model else "default",
            "batch_size": batch_size,
            "epochs": epochs,
            "new_version": new_version.version
        }
        files = {"file": (file.name, file.read(), file.content_type)}

        try:
            ai_resp = requests.post(ai_url, data=data, files=files)
        except Exception as e:
            new_version.delete()  
            return Response({"error": f"Could not reach AI service: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if ai_resp.status_code != 200 and ai_resp.status_code != 202 :
            new_version.delete()  
            return Response(
                {"error": "AI service returned an error.", "ai_response": ai_resp.text},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {
                "detail": "Retraining triggered.",
                "model_version": new_version.version,
                "parent_model": base_model.version if base_model else None
            },
            status=status.HTTP_201_CREATED
        )

    def create_new_model_version(self, parent_model: ModelVersion) -> ModelVersion:
    
        with transaction.atomic():
            # Lock the last version to prevent race conditions
            last = ModelVersion.objects.select_for_update().order_by("-created_at").first()
            if not last:
                new_version_str = "v1.0"
            else:
                num = int(last.version.replace("v", "").split(".")[0])
                new_version_str = f"v{num + 1}.0"

            # Create the row immediately to reserve this version
            new_version = ModelVersion.objects.create(
                version=new_version_str,
                status="fine-tuning",
                parent_model=parent_model
            )

            return new_version

class AdminRollbackView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, _request, version):
        try:
            mv = ModelVersion.objects.get(version=version, status="ready")
        except ModelVersion.DoesNotExist:
            return Response(
                {"error": "Model must be in READY state"},
                status=status.HTTP_400_BAD_REQUEST
            )

        mv.status = "initializing"
        mv.save()

        url = f"{settings.AI_SERVICE_URL}/api/v1/model-versions/{mv.version}/rollback/"


        try:
            response = requests.post(url)
        except Exception as e:
            return Response(
                {"error": f"Could not reach AI service: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if response.status_code != 200:
            return Response(
                {
                    "error": "AI service returned an error.",
                    "ai_response": response.text
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response(
            {
                "detail": "Rollback triggered.",
                "model_version": mv.version,
            },
            status=status.HTTP_201_CREATED
        )

