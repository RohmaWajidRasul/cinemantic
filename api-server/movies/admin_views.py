import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class AdminRetrainView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "CSV file is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        ai_url = settings.AI_SERVICE_URL + "api/v1/fine-tune/"

        # Prepare multipart form-data to forward the file
        files = {
            "file": (file.name, file.read(), file.content_type)
        }

        try:
            ai_resp = requests.post(ai_url, files=files)
        except Exception as e:
            return Response(
                {"error": f"Could not reach AI service: {e}"},
                status=500
            )

        if ai_resp.status_code != 200:
            return Response(
                {
                    "error": "AI service returned an error.",
                    "ai_response": ai_resp.text
                },
                status=500
            )

        return Response(
            {
                "detail": "CSV forwarded to AI service. Retraining triggered.",

            },
            status=200
        )
