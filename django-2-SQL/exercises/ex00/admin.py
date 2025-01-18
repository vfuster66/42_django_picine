from django.contrib import admin
from .models import Ex00Movies


@admin.register(Ex00Movies)
class Ex00MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'episode_nb', 
        'director', 
        'producer', 
        'release_date'
    )
