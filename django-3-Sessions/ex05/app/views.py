from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, TipForm
from .models import Tip
from django.core.exceptions import PermissionDenied


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
    tips = Tip.objects.order_by('-date')
    form = None
    can_downvote = (
        request.user.has_perm('app.can_downvote')
        if request.user.is_authenticated
        else False
    )
    can_delete_tip = (
        request.user.has_perm('app.delete_tip')
        if request.user.is_authenticated
        else False
    )

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.auteur = request.user
                tip.save()
                return redirect('home')
        else:
            form = TipForm()

    return render(request, 'app/home.html', {
        'tips': tips,
        'form': form,
        'can_downvote': can_downvote,
        'can_delete_tip': can_delete_tip,
    })


@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)  # Annule le downvote
    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)  # Annule l'upvote
    else:
        tip.upvotes.add(request.user)  # Ajoute un upvote
    return redirect('home')


@login_required
def downvote_tip(request, tip_id):
    """
    Vue pour gérer les downvotes.
    Seul un utilisateur ayant la permission personnalisée 'can_downvote'
    ou l'auteur de l'astuce peut effectuer un downvote.
    """
    tip = get_object_or_404(Tip, id=tip_id)

    # Vérifie si l'utilisateur a la permission ou est l'auteur
    if (not request.user.has_perm('app.can_downvote') and
            tip.auteur != request.user):
        raise PermissionDenied("Vous n'avez pas la permission de downvoter.")

    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)  # Annule l'upvote
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)  # Annule le downvote
    else:
        tip.downvotes.add(request.user)  # Ajoute un downvote
    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    """
    Vue pour supprimer une astuce.
    Seul l'auteur ou un utilisateur ayant la permission 'delete_tip'
    peut supprimer une astuce.
    """
    tip = get_object_or_404(Tip, id=tip_id)

    # Vérification des permissions : l'utilisateur doit être l'auteur
    # ou avoir la permission
    if tip.auteur == request.user or request.user.has_perm('app.delete_tip'):
        tip.delete()
        return redirect('home')

    # Si l'utilisateur n'a pas les permissions nécessaires, afficher un message
    # d'erreur
    return render(request, 'app/error.html', {
        'message': "Vous n'avez pas la permission de supprimer cette astuce."
    })
