from django.contrib import admin
from .models import Genre, Cast, Crew, Movie

# Register your models here.
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Movie)