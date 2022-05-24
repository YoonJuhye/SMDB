from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_list_or_create),
    path('review/<int:review_pk>/', views.review_update_or_delete),
    path('<int:movie_pk>/review/<int:review_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/review/<int:review_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('cast/', views.cast_list),
    path('crew/', views.crew_list),
    path('search/<keyword>/', views.search_movies),
    path('sort/<value>/', views.sort_list)
]


