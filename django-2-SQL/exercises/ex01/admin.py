from django.contrib import admin
from .models import Ex01Movies


@admin.register(Ex01Movies)
class Ex01MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'episode_nb', 'director', 'producer', 'release_date'
    )
