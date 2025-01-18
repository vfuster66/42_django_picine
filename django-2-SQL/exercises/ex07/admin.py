from django.contrib import admin
from .models import Ex07Movies


@admin.register(Ex07Movies)
class Ex07MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'episode_nb', 'director', 'producer', 'release_date'
    )
