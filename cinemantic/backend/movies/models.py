from django.db import models

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField()
    release_date = models.CharField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    crew = models.TextField(null=True, blank=True)
    original_title = models.CharField(null=True, blank=True)
    status = models.CharField(null=True, blank=True)
    original_language = models.CharField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    country = models.CharField(null=True, blank=True)

    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommendations')
    recommended_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommended_from')
    similarity = models.FloatField()
    rank = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'recommended_movie')
        ordering = ['movie_id', 'rank']