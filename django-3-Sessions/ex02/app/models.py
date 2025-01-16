from django.db import models
from django.contrib.auth.models import User


class Tip(models.Model):
    contenu = models.TextField()  # Contenu du tip
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)  # Auteur du tip
    date = models.DateTimeField(auto_now_add=True)  # Date et heure de création

    def __str__(self):
        return f"{self.auteur.username} - {self.date}"
