from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

# class Platform(models.Model):
#     neflix = models.BooleanField()
#     watcha = models.BooleanField()
#     disney = models.BooleanField()

# class Video(models.Model):

class Movie(models.Model):
    genre_ids=models.ManyToManyField(Genre)
    # casts=models.ManyToManyField(Cast, related_name='movies')
    # crews=models.ManyToManyField(Crew, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(null=True)
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    poster_path = models.TextField()
    video = models.BooleanField()

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,null=True)
    name = models.TextField()
    character = models.TextField(null=True)
    # profile_path = models.TextField()


class Crew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    job = models.TextField(null=True)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)