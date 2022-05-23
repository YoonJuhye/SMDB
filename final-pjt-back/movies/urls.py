from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movies_pk>/', views.movie_detail),
    path('cast/', views.cast_list),
    path('crew/', views.crew_list),
]


