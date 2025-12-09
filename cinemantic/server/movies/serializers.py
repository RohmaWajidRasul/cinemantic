from rest_framework import serializers
from .models import Movie, Recommendation, RecommendationHistory

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['id','title','release_date','score','overview','crew','original_title','status','original_language','budget','revenue','country','genres']

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
            'rank',
            'created_at'
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
    movies = MovieMiniSerializer(many=True, read_only=True)

    class Meta:
        model = RecommendationHistory
        fields = [
            "id",
            "created_at",
            "model_version",
            "feedback",
            "movies",
        ]


class RecommendationFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationHistory
        fields = ["feedback"]
