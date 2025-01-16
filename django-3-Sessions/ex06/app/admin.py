from django.contrib import admin
from .models import Tip, CustomUser


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Tip.
    """
    list_display = (
        'id',  # Ajout de l'ID pour une meilleure identification
        'auteur',
        'contenu_excerpt',
        'date_local',
        'total_upvotes',
        'total_downvotes'
    )
    list_filter = ('date', 'auteur')  # Filtrage par date et auteur
    search_fields = ('contenu', 'auteur__username')
    ordering = ('-date',)  # Tri par date décroissante

    def contenu_excerpt(self, obj):
        """
        Affiche un extrait du contenu (limité à 50 caractères).
        """
        return (obj.contenu[:50] + "..."
                if len(obj.contenu) > 50
                else obj.contenu)
    contenu_excerpt.short_description = "Contenu (Extrait)"

    def date_local(self, obj):
        """
        Affiche la date dans le fuseau horaire local.
        """
        from django.utils.timezone import localtime
        return localtime(obj.date).strftime('%d/%m/%Y %H:%M:%S')
    date_local.short_description = "Date (locale)"

    def total_upvotes(self, obj):
        """
        Retourne le nombre total d'upvotes.
        """
        return obj.total_upvotes()
    total_upvotes.short_description = "Upvotes"

    def total_downvotes(self, obj):
        """
        Retourne le nombre total de downvotes.
        """
        return obj.total_downvotes()
    total_downvotes.short_description = "Downvotes"


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle CustomUser.
    """
    list_display = (
        'id',
        'username',
        'email',
        'reputation',
        'is_staff',
        'is_active',
        'last_login',
    )
    list_filter = ('is_staff', 'is_active', 'reputation')
    search_fields = ('username', 'email')
    ordering = ('-reputation',)
    readonly_fields = ('reputation',)

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'reputation')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions'),
        }),
        ('Dates importantes', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
