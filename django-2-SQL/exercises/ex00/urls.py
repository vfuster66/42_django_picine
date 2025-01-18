from django.urls import path
from . import views  # Import des vues de l'application ex00

urlpatterns = [
    # Exemple de route pour init
    path('init/', views.init, name='init'),
]
