# articles/forms.py
from django import forms
from .models import Article, UserFavouriteArticle


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']


class FavouriteForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []
