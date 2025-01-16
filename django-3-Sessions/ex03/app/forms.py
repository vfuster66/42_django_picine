from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Tip


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        # On ne permet que l'ajout de contenu via le formulaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Partagez votre astuce ici...'
                }
            ),
        }


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Mot de passe"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmez le mot de passe"
    )

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(
        widget=forms.PasswordInput, label="Mot de passe"
    )
