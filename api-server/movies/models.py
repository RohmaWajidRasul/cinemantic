from django.db import models
from django.conf import settings
from pgvector.django import VectorField
from django.contrib.postgres.fields import ArrayField


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    
class Movie(models.Model):
    title = models.CharField()
    release_date = models.CharField(null=False, blank=False)
    score = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=False, blank=False)
    crew = models.TextField(null=True, blank=True)
    original_title = models.CharField(null=True, blank=True)
    status = models.CharField(null=True, blank=True)
    original_language = models.CharField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    country = models.CharField(null=True, blank=True)

    embedding = VectorField(dimensions=384, null=True, blank=True)
    poster_url = models.CharField(null=True, blank=True)

    genres = models.ManyToManyField(Genre, related_name="movies", blank=False)


class Recommendation(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommendations')
    recommended_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommended_from')
    similarity = models.FloatField()

    class Meta:
        unique_together = ('movie', 'recommended_movie')
        ordering = ['movie_id', '-similarity']

class RecommendationHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recommendation_sessions"
    )

    movie_ids = ArrayField(
        base_field=models.IntegerField(),
        size=5
    )

    model_version = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    feedback = models.CharField(
        max_length=10,
        null=True,
        blank=True,

        choices=[
            ("positive", "Positive"),
            ("negative", "Negative"),
        ],
    )

class ModelVersion(models.Model):
    STATUS_CHOICES = [
        ("fine-tuning", "Fine-tuning"),
        ("ready", "Ready"),
        ("failed", "Failed"),
    ]

    version = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
