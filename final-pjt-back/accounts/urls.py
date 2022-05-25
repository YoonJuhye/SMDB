from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profileimg/<username>/', views.profileimg),
    path('profileimg/<int:user_pk>/save/', views.saveImg),
]

