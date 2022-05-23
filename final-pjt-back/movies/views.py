from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Cast, Crew, Movie
from .serializers import CastSerializer, CrewSerializer, GenreSerializer, MovieSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.order_by('-popularity')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

def cast_list(request):
    casts = get_list_or_404(Cast)
    serializer = CastSerializer(casts, many=True)
    return Response(serializer.data)

def crew_list(request):
    crews = get_list_or_404(Crew)
    serializer = CrewSerializer(crews, many=True)
    return Response(serializer.data)