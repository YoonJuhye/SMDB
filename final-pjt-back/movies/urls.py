from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail_or_update_or_delete),
    path('<int:movie_pk>/<int:review_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/<int:review_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('cast/', views.cast_list),
    path('crew/', views.crew_list),
]


