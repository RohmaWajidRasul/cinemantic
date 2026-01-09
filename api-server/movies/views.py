import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Movie, Recommendation, RecommendationHistory, ModelVersion
from .serializers import MovieSerializer, RecommendationSerializer, RecommendationHistorySerializer

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "movie_id"

# ============================================
#   MOVIE LIST + SEARCH + PAGINATION
#   GET /movies/
#   GET /movies/?title=star
# ============================================

class MovieListView(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Movie.objects.all().order_by("id")

        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset


# ============================================
#   SINGLE MOVIE RECOMMENDATIONS (Top 5)
#   GET /movies/<movie_id>/recommendations/
# ============================================
# Use ListAPIView but override `list()` so we can store session AFTER
# we compute the actual top-5 recommendations that will be returned.
class MovieRecommendationsView(ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        movie_id = self.kwargs["movie_id"]

        if not Movie.objects.filter(id=movie_id).exists():
            raise Http404("Movie not found")

        # return all recommendations for that movie ordered by similarity
        return Recommendation.objects.filter(movie_id=movie_id).order_by("-similarity")

    def list(self, request, *args, **kwargs):
        movie_id = self.kwargs["movie_id"]

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "release_date": movie.release_date,
            "score": movie.score,
            "overview": movie.overview,
        }

        queryset = self.filter_queryset(self.get_queryset())

        recommendations = []
        recommended_ids = []

        for rec in queryset:
            rm = rec.recommended_movie

            recommendations.append({
                "id": rm.id,
                "title": rm.title,
                "overview": rm.overview,
                "similarity": rec.similarity,
            })

            recommended_ids.append(rm.id)


        if request.user and request.user.is_authenticated and recommendations:

            current_model_version = ModelVersion.objects.filter(status="current").order_by("-created_at").first()

            RecommendationHistory.objects.create(
                user=request.user,
                model_version=current_model_version,
                input_movies=[movie.id],
                recommended_ids=recommended_ids,
            )

        return Response(
            {
                "movie": movie_data,
                "recommendations": recommendations
            },
            status=status.HTTP_200_OK
        )



# ============================================
#   COMBINED RECOMMENDATIONS
#   GET /recommendations?movies=1,2,3
# ============================================

class CombinedRecommendationsView(APIView):

    def get(self, request):

        # ------------------------------------------
        # Read ?movies=1,2,3
        # ------------------------------------------
        movies_param = request.GET.get("movies")
        if not movies_param:
            return Response(
                {"error": "Missing query parameter: ?movies=id1,id2,..."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Parse comma-separated IDs safely
        try:
            movie_ids = [int(x) for x in movies_param.split(",")]
        except ValueError:
            return Response(
                {"error": "Movies parameter must be comma-separated integers"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Limit 1–5 movie IDs
        if not 1 <= len(movie_ids) <= 5:
            return Response(
                {"error": "You must provide between 1 and 5 movie IDs"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Ensure all movies exist
        existing = Movie.objects.filter(id__in=movie_ids)
        if existing.count() != len(movie_ids):
            return Response(
                {"error": "One or more movie IDs do not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        # ------------------------------------------
        # Aggregate recommendations
        # ------------------------------------------
        similarity_scores = {}
        recommended_movies_lookup = {}

        for mid in movie_ids:
            recs = Recommendation.objects.filter(movie_id=mid)
            for rec in recs:
                rm = rec.recommended_movie

                # Skip original movies (do not recommend input movies)
                if rm.id in movie_ids:
                    continue

                similarity_scores[rm.id] = similarity_scores.get(rm.id, 0) + rec.similarity
                recommended_movies_lookup[rm.id] = rm

        # ------------------------------------------
        # Calculate Top 5 aggregated recommendations
        # ------------------------------------------
        ranked = sorted(
            similarity_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        top5 = ranked[:5]

        # ------------------------------------------
        # Build response format
        # ------------------------------------------
        response = []
        for movie_id, score in top5:
            movie = recommended_movies_lookup[movie_id]
            response.append({
                "id": movie.id,
                "title": movie.title,
                "aggregated_similarity": score,
            })

        # ------------------------------------------
        # Persist session for authenticated users
        # ------------------------------------------
        if request.user and request.user.is_authenticated and top5:

            current_model_version = ModelVersion.objects.filter(status="current").order_by("-created_at").first()

            RecommendationHistory.objects.create(
                user=request.user,
                model_version=current_model_version or "unknown",
                input_movies = movie_ids,
                recommended_ids=[mid for mid, _ in top5],
            )


        return Response(response, status=status.HTTP_200_OK)


class RecommendationHistoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, history_id):
        session = get_object_or_404(
            RecommendationHistory,
            id=history_id,
            user=request.user
        )

        session.feedback = request.data.get("feedback")
        session.save()

        return Response({"detail": "Feedback saved."}, status=200)
    
    def get(self, request, history_id):
        session = get_object_or_404(
            RecommendationHistory,
            id=history_id,
            user=request.user
        )

        serializer = RecommendationHistorySerializer(session)

        return Response(serializer.data, status=200)


class RecommendationHistoryView(ListAPIView):
    serializer_class = RecommendationHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RecommendationHistory.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

class ExternalMovieRecommendationView(APIView):
    def get(self, request):
        title = request.data.get("title")

        if not title:
            return Response(
                {"error": "Title is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        omdb_params = {
            "t": title,
            "apikey": settings.OMDB_API_KEY
        }

        omdb_resp = requests.get(settings.OMDB_API_URL, params=omdb_params)

        if omdb_resp.status_code != 200:
            return Response(
                {"error": "Failed to reach OMDb"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        omdb_data = omdb_resp.json()

        if omdb_data.get("Response") == "False":
            return Response(
                {"error": f"OMDb could not find movie '{title}'"},
                status=status.HTTP_404_NOT_FOUND
            )

        movie_title = omdb_data.get("Title", title)
        genres = omdb_data.get("Genre", "")
        overview = omdb_data.get("Plot", "")
        year = omdb_data.get("Year", "")


        ai_url = settings.AI_SERVICE_URL + "/api/v1/movies/"

        payload = {
            "title": movie_title,
            "genres": genres,
            "overview": overview,
        }

        try:
            ai_resp = requests.get(ai_url, json=payload)
        except Exception as e:
            return Response(
                {"error": f"Could not reach AI service: {e}"},
                status=500
            )

        if ai_resp.status_code != 200:
            return Response(
                {
                    "error": "AI service returned an error",
                    "details": ai_resp.text
                },
                status=500
            )
        
        recs = ai_resp.json()
        print(recs)
        
        if request.user.is_authenticated and recs:

            input_movie_str = f"{movie_title} ({year})"

            current_model_version = ModelVersion.objects.filter(status="current").order_by("-created_at").first()

            recommended_ids = [item["id"] for item in recs.get("results", [])]

            RecommendationHistory.objects.create(
                user=request.user,
                model_version=current_model_version or "unknown",
                is_external=True,
                input_movies=[input_movie_str],
                recommended_ids=recommended_ids
            )

        return Response(ai_resp.json(), status=200)


