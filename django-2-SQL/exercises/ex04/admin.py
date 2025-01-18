from django.contrib import admin
from .models import Ex04Movies


@admin.register(Ex04Movies)
class Ex04MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
