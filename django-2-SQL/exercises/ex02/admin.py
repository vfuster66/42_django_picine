from django.contrib import admin
from .models import Ex02Movies


@admin.register(Ex02Movies)
class Ex02MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
