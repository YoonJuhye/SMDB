from rest_framework import serializers
from .models import Genre, Cast, Crew, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'

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
    casts = CastListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content', )