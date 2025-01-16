from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, TipForm
from .models import Tip, CustomUser
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

    if request.user.is_authenticated:
        user: CustomUser = request.user
        can_downvote = user.can_downvote()
        can_delete_tip = user.can_delete_tip()

        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.auteur = user
                tip.save()
                return redirect('home')
        else:
            form = TipForm()
    else:
        can_downvote = False
        can_delete_tip = False

    return render(request, 'app/home.html', {
        'tips': tips,
        'form': form,
        'can_downvote': can_downvote,
        'can_delete_tip': can_delete_tip,
    })


@login_required
def upvote_tip(request, tip_id):
    """
    Vue pour gérer les upvotes.
    """
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)  # Annule le downvote
    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)  # Annule l'upvote
    else:
        tip.upvotes.add(request.user)  # Ajoute un upvote

    tip.auteur.update_reputation()

    return redirect('home')


@login_required
def downvote_tip(request, tip_id):
    """
    Vue pour gérer les downvotes.
    Seul un utilisateur ayant assez de réputation ou l'auteur du Tip
    peut downvoter.
    """
    tip = get_object_or_404(Tip, id=tip_id)

    if not request.user.can_downvote() and tip.auteur != request.user:
        raise PermissionDenied("Vous n'avez pas la permission de downvoter.")

    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)  # Annule l'upvote
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)  # Annule le downvote
    else:
        tip.downvotes.add(request.user)  # Ajoute un downvote

    tip.auteur.update_reputation()
    return redirect('home')


@login_required
def delete_tip(request, tip_id):
    """
    Vue pour supprimer un Tip.
    Seul l'auteur ou un utilisateur ayant assez de réputation 
    peut le supprimer.
    """
    tip = get_object_or_404(Tip, id=tip_id)

    if not request.user.can_delete_tip() and tip.auteur != request.user:
        raise PermissionDenied(
            "Vous n'avez pas la permission de supprimer cette astuce."
        )

    tip.delete()
    return redirect('home')
