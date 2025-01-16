from django.contrib import admin
from .models import Tip


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'contenu', 'date')
