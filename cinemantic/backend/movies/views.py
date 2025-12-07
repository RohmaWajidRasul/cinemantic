from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Movie, Recommendation
from .serializers import MovieSerializer, RecommendationSerializer


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

class MovieRecommendationsView(ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        movie_id = self.kwargs["movie_id"]

        if not Movie.objects.filter(id=movie_id).exists():
            raise Http404("Movie not found")

        return Recommendation.objects.filter(movie_id=movie_id).order_by("rank")



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

        return Response(response, status=status.HTTP_200_OK)
