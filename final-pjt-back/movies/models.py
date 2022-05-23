from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

# class Platform(models.Model):
#     neflix = models.BooleanField()
#     watcha = models.BooleanField()
#     disney = models.BooleanField()

# class Video(models.Model):

class Movie(models.Model):
    genre_ids=models.ManyToManyField(Genre, related_name='movies')
    # casts=models.ManyToManyField(Cast, related_name='movies')
    # crews=models.ManyToManyField(Crew, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField()
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    poster_path = models.TextField()
    video = models.BooleanField()

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.TextField()
    character = models.TextField()
    # profile_path = models.TextField()


class Crew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.TextField()
    job = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()