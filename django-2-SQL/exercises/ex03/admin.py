from django.contrib import admin
from .models import Ex03Movies


@admin.register(Ex03Movies)
class Ex03MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
