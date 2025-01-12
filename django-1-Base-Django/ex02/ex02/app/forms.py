from django import forms


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Entrez votre texte',
        'class': 'form-control'
    }))