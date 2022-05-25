from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')
    like_movies = MovieSerializer(many=True)



    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_movies',)


class ProfileImg(serializers.ModelSerializer):
    class UserS(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)
    user = UserS(read_only=True)
    class Meta:
        model=Profile
        fields = '__all__'