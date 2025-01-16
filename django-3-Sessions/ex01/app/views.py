from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrationForm, LoginForm
import random
from django.conf import settings


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


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
