from rest_framework import serializers
from .models import Genre, Movie, Review, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    
    class GenreSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Genre
            fields = '__all__'

    like_users = UserSerializer(read_only=True, many=True)
    genre_ids=GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'review',)
        read_only_fields = ('review', )

class ReviewSerializer(serializers.ModelSerializer):
    class MovieS(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username','profile_img',)

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    movie = MovieS(read_only=True)
    # like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = '__all__'
