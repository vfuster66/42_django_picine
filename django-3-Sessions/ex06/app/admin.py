from django.contrib import admin
from .models import Tip, CustomUser


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Tip.
    """
    list_display = ('auteur', 'contenu_excerpt', 'date', 'total_upvotes', 'total_downvotes')
    list_filter = ('date',)  # Ajout d'un filtre par date
    search_fields = ('contenu', 'auteur__username')  # Recherche par contenu ou auteur

    def contenu_excerpt(self, obj):
        """
        Affiche un extrait du contenu (limité à 50 caractères).
        """
        return obj.contenu[:50] + "..." if len(obj.contenu) > 50 else obj.contenu
    contenu_excerpt.short_description = "Contenu (Extrait)"

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
    list_display = ('username', 'email', 'reputation', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'reputation')  # Filtres supplémentaires
    search_fields = ('username', 'email')  # Recherche par nom d'utilisateur ou email
    ordering = ('-reputation',)  # Classement par réputation décroissante
