from django.contrib import admin
from .models import Planets, People, Movies


@admin.register(Planets)
class PlanetsAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'climate', 'diameter', 'orbital_period',
        'population', 'rotation_period', 'surface_water', 'terrain',
        'created', 'updated'
    )
    list_filter = ('climate', 'terrain')
    search_fields = ('name', 'climate', 'terrain')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'birth_year', 'gender', 'eye_color',
        'hair_color', 'height', 'mass', 'homeworld',
        'created', 'updated'
    )
    list_filter = ('gender', 'eye_color', 'hair_color', 'homeworld__name')
    search_fields = ('name', 'birth_year', 'homeworld__name')


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'episode_nb', 'director', 'producer', 'release_date'
    )
    search_fields = ('title', 'director', 'producer')
    filter_horizontal = ('characters',)
