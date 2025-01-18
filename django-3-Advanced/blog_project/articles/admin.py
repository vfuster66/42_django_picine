# articles/admin.py
from django.contrib import admin
from .models import Article, UserFavouriteArticle

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'synopsis')  # Champs affichés dans la liste
    list_filter = ('author', 'created')  # Filtres sur le côté
    search_fields = ('title', 'synopsis', 'content')  # Champs recherchables
    readonly_fields = ('created',)  # Champs en lecture seule
    fieldsets = (
        (None, {
            'fields': ('title', 'author')
        }),
        ('Content', {
            'fields': ('synopsis', 'content')
        }),
        ('Metadata', {
            'fields': ('created',)
        }),
    )

@admin.register(UserFavouriteArticle)
class UserFavouriteArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')
    list_filter = ('user',)
    search_fields = ('user__username', 'article__title')