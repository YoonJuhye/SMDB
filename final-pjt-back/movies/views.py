from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Review, Comment
from .serializers import MovieSerializer, ReviewSerializer, CommentSerializer
from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        data = {
            'delete': f'{movie.title}이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET', 'POST'])
def review_list_or_create(request, movie_pk):
    def review_list():
        reviews = Review.objects.filter(movie_id=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def create_review():
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie_id=movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()

@api_view(['GET', 'PUT', 'DELETE'])
def review_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        if request.user == review.user:
            return update_review()
    elif request.method == 'DELETE':
        if request.user == review.user:
            return delete_review()

@api_view(['GET'])
def load_comment(request,review_pk):
        reviews = Comment.objects.filter(review_id=review_pk)
        serializer = CommentSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)

        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

@api_view(['GET'])
def search_movies(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-popularity')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def sort_list(request, value):
    if value == 'all':
        movies = Movie.objects.order_by('?')[0:40]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        movies = Movie.objects.filter(genre_ids = value).order_by('?')[0:20]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def my_review(request):
    user = request.user
    reviews = Review.objects.filter(user=user)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)