from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_list_or_create),
    path('review/<int:review_pk>/', views.review_update_or_delete),
    path('review/<int:review_pk>/comments/', views.load_comment),
    path('review/<int:review_pk>/comments/new/', views.create_comment),
    path('review/<int:review_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('search/<keyword>/', views.search_movies),
    path('sort/<value>/', views.sort_list),
    path('like/<movie_pk>/', views.like_movie),
    path('myreview/', views.my_review),
]


