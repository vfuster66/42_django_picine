from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from articles.views import ArticleListView

# URLs non traduites
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    # Inclure toutes les URLs sauf articles/
    path('', include('articles.urls')), 
]

# Uniquement la route articles avec i18n
urlpatterns += i18n_patterns(
    path('articles/', ArticleListView.as_view(), name='article_list'),
    prefix_default_language=False  # False pour que l'anglais soit sans préfixe
)