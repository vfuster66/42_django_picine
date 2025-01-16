from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, TipForm
from .models import Tip


def register(request):
    """
    Vue pour l'inscription d'un utilisateur.
    """
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
    """
    Vue pour la connexion d'un utilisateur.
    """
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


@login_required
def logout_view(request):
    """
    Vue pour la déconnexion d'un utilisateur.
    """
    logout(request)
    return redirect('home')


def home(request):
    """
    Vue de la page d'accueil, affichant les astuces et permettant aux
    utilisateurs connectés de créer de nouvelles astuces.
    """
    # Liste des astuces triées par date décroissante
    tips = Tip.objects.order_by('-date')
    form = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                # Associe l'utilisateur connecté comme auteur
                tip.auteur = request.user
                tip.save()
                return redirect('home')
        else:
            form = TipForm()

    return render(request, 'app/home.html', {'tips': tips, 'form': form})
