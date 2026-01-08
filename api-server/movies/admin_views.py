import requests
from django.conf import settings
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

        try:
            base_model = ModelVersion.objects.get(
                version=base_model_version,
                status__in=["ready", "current"]
            )
        except ModelVersion.DoesNotExist:
            return Response(
                {
                    "error": "Base model unavailable."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        ai_url = settings.AI_SERVICE_URL + "/api/v1/admin/fine-tune/"

        data = {
            "base_model": base_model.version,
            "batch_size": batch_size,
            "epochs": epochs
        }

        files = {
            "file": (file.name, file.read(), file.content_type)
        }

        try:
            auth_header = request.headers.get("Authorization")
            headers = {}
            if auth_header:
                headers["Authorization"] = auth_header

            ai_resp = requests.post(ai_url, data=data, files=files, headers=headers)
        except Exception as e:
            return Response(
                {"error": f"Could not reach AI service: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if ai_resp.status_code != 200:
            return Response(
                {
                    "error": "AI service returned an error.",
                    "ai_response": ai_resp.text
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        new_version = ModelVersion.objects.create(
            version=self._generate_version(),
            status="fine-tuning",
            parent_model=base_model
        )

        return Response(
            {
                "detail": "Retraining triggered.",
                "model_version": new_version.version,
                "parent_model": base_model.version
            },
            status=status.HTTP_201_CREATED
        )
    
    def _generate_version(self):
        last = ModelVersion.objects.order_by("-created_at").first()
        
        if not last:
            return "v1.0"
        
        num = int(last.version.replace("v", "").split(".")[0])
        
        return f"v{num + 1}.0"
