from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil de l'application
    path('django/', views.django_page, name='django_page'),
    path('affichage/', views.affichage, name='affichage'),
    path('templates/', views.templates, name='templates'),
]
