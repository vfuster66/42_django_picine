from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Tip

# Utilisation du modèle utilisateur personnalisé si configuré
User = get_user_model()


class TipForm(forms.ModelForm):
    """
    Formulaire pour créer ou mettre à jour un Tip.
    Permet uniquement l'ajout de contenu.
    """
    class Meta:
        model = Tip
        fields = ['contenu']  # Champs autorisés dans le formulaire
        widgets = {
            'contenu': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Partagez votre astuce ici...',
                    'class': 'form-control',
                }
            ),
        }


class RegistrationForm(forms.ModelForm):
    """
    Formulaire d'inscription pour les nouveaux utilisateurs.
    Comprend uniquement un nom d'utilisateur et la validation des mots de passe.
    """
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Entrez un mot de passe',
                'class': 'form-control',
            }
        ),
        label="Mot de passe",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmez le mot de passe',
                'class': 'form-control',
            }
        ),
        label="Confirmez le mot de passe",
    )

    class Meta:
        model = User
        fields = ['username']  # Supprimer 'email' de la liste des champs

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
        }

    def clean(self):
        """
        Vérifie si les mots de passe correspondent.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data



class LoginForm(AuthenticationForm):
    """
    Formulaire de connexion.
    """
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nom d'utilisateur",
                'class': 'form-control',
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe',
                'class': 'form-control',
            }
        ),
        label="Mot de passe",
    )
