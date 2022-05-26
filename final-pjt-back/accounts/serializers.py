from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from .models import User

class ProfileSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')
    like_movies = MovieSerializer(many=True, read_only=True)



    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_movies','profile_img')