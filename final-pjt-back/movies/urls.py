from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movies_pk>/', views.movie_detail),
]
