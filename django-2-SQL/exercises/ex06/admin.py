from django.contrib import admin
from .models import Ex06Movies


@admin.register(Ex06Movies)
class Ex06MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
