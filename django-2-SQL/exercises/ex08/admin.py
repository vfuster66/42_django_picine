from django.contrib import admin
from .models import Ex08Planets, Ex08People


@admin.register(Ex08Planets)
class Ex08PlanetsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'climate',
        'diameter',
        'orbital_period',
        'population',
        'rotation_period',
        'surface_water',
        'terrain',
    )
    search_fields = ('name',)
    list_filter = ('climate', 'terrain')


@admin.register(Ex08People)
class Ex08PeopleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'homeworld',
    )
    search_fields = ('name',)
    list_filter = ('homeworld__name',)
