from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Cast(models.Model):
    name = models.CharField(max_length=50)

class Crew(models.Model):
    name = models.CharField(max_length=50)

# class Platform(models.Model):
#     neflix = models.BooleanField()
#     watcha = models.BooleanField()
#     disney = models.BooleanField()

# class Video(models.Model):

class Movie(models.Model):
    genres=models.ManyToManyField(Genre, related_name='movies')
    casts=models.ManyToManyField(Cast, related_name='movies')
    crews=models.ManyToManyField(Crew, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    popularity = models.IntegerField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    video = models.BooleanField()
