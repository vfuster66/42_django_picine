from django.urls import path
from . import views  # Importer les vues locales

urlpatterns = [
    path('init/', views.init, name='init'),
]
