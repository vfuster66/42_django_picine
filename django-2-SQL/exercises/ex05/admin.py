from django.contrib import admin
from .models import Ex05Movies


@admin.register(Ex05Movies)
class Ex05MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
