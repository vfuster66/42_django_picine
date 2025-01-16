from django.shortcuts import render
from django.conf import settings
import random


def home(request):
    # Vérifie si la session contient un nom d'utilisateur
    if not request.session.get('username'):
        # Choisit un nom aléatoire depuis la liste définie dans settings.py
        username = random.choice(settings.RANDOM_USERNAMES)
        request.session['username'] = username
        request.session.set_expiry(42)

    # Passe le nom de l'utilisateur à la page
    return render(
        request, 'app/home.html', {'username': request.session['username']}
    )
