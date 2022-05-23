from rest_framework import serializers
from .models import Genre, Cast, Crew, Movie, Review, Comment
from django.contrib.auth import get_user_model
User = get_user_model()



class CastListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cast
        fields = ('id', 'name', )

class CastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cast
        fields = ('id', 'name', 'character', 'movies',)
        read_only_fields = ('movies', )

class CrewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crew
        fields = ('id', 'name', )

class CrewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crew
        fields = ('id', 'name', 'job', 'movies',)
        read_only_fields = ('movies', )

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'vote_average',)

class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Genre
            fields = '__all__'

    genre_ids=GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

# class GenreDetailSerializer(GenrelistSerializer):
#     movie = MovieSerializer(many=True)
#     class Meta(GenrelistSerializer.Meta):
#         fields = GenrelistSerializer.Meta.fields + ['movie', ]


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content', )

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)
        read_only_fields = ('movie', )

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    # like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'comments',)

class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    # like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'comment_count',)
