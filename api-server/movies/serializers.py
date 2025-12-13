from rest_framework import serializers
from .models import Movie, Recommendation, RecommendationHistory, ModelVersion

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['id','title','release_date','score','overview','crew','original_title','status','original_language','budget','revenue','country','genres', 'poster_url']

class RecommendationSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    recommended_movie_detail = serializers.SerializerMethodField()

    class Meta:
        model = Recommendation
        fields = [
            "id",
            'movie',
            'movie_title',
            'recommended_movie',
            'recommended_movie_detail',
            'similarity',
        ]

    def get_recommended_movie_detail(self, obj):
        m = obj.recommended_movie
        return {
            "id": m.id,
            "title": m.title,
            "release_date": m.release_date,
            "score": m.score
        }

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "overview"]


class RecommendationHistorySerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = RecommendationHistory
        fields = [
            "id",
            "created_at",
            "model_version",
            "feedback",
            "movies",
        ]

    def get_movies(self, obj):
        movies = Movie.objects.filter(id__in=obj.movie_ids)
        movie_map = {m.id: m for m in movies}
        ordered = [movie_map[mid] for mid in obj.movie_ids if mid in movie_map]

        return MovieMiniSerializer(ordered, many=True).data


class RecommendationFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationHistory
        fields = ["feedback"]

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelVersion
        fields = ["id", "version", "status", "created_at"]