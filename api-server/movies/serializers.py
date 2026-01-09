# Implemented by Rohma 
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
        fields = ["id", "title", "overview", "poster_url"]


class RecommendationHistorySerializer(serializers.ModelSerializer):
    recommendations = serializers.SerializerMethodField()
    input_movies = serializers.SerializerMethodField()

    class Meta:
        model = RecommendationHistory
        fields = [
            "id",
            "created_at",
            "model_version",
            "is_external",
            "feedback",
            "input_movies",
            "recommendations",
        ]

    def get_input_movies(self, obj):
        value = obj.input_movies

        if obj.is_external:
            return [{
                "title": value[0]
            }]
        else:
            movies = Movie.objects.filter(id__in=value)
            movie_map = {m.id: m for m in movies}

            ordered = []
            for mid in value:
                if mid in movie_map:
                    movie = movie_map[mid]
                    ordered.append({
                        "id": movie.id,
                        "title": movie.title,
                        "overview": movie.overview,
                        "poster_url": movie.poster_url,
                        "genres": [g.name for g in movie.genres.all()],
                    })
                else:
                    ordered.append({"id": mid, "title": "Unknown"})

            return ordered           

    def get_recommendations(self, obj):
        movies = Movie.objects.filter(id__in=obj.recommended_ids)
        movie_map = {m.id: m for m in movies}
        ordered = [movie_map[mid] for mid in obj.recommended_ids if mid in movie_map]

        return MovieMiniSerializer(ordered, many=True).data


class RecommendationFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationHistory
        fields = ["feedback"]

class ModelVersionSerializer(serializers.ModelSerializer):
    user_feedback_summary = serializers.SerializerMethodField()
    parent_model_version = serializers.SerializerMethodField()

    class Meta:
        model = ModelVersion
        fields = [
            "id",
            "version",
            "status",
            "precision_before",
            "precision_after",
            "detail",
            "created_at",
            "user_feedback_summary",
            "parent_model_version",
        ]

    def get_user_feedback_summary(self, obj):
        # Annotated counts from queryset
        return {
            "positive": getattr(obj, "positive_count", 0),
            "negative": getattr(obj, "negative_count", 0),
            "null": getattr(obj, "null_count", 0),
        }
    
    def get_parent_model_version(self, obj):
        if obj.parent_model:
            return obj.parent_model.version
        return None