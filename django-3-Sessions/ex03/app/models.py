from django.db import models
from django.contrib.auth.models import User


class Tip(models.Model):
    contenu = models.TextField()  # Contenu du tip
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)  # Auteur du tip
    date = models.DateTimeField(auto_now_add=True)  # Date et heure de création
    upvotes = models.ManyToManyField(
        User, related_name='upvoted_tips', blank=True
    )  # Utilisateurs ayant upvoté
    downvotes = models.ManyToManyField(
        User, related_name='downvoted_tips', blank=True
    )  # Utilisateurs ayant downvoté

    def __str__(self):
        return f"{self.auteur.username} - {self.date}"

    def total_upvotes(self):
        """
        Retourne le nombre total d'upvotes pour ce tip.
        """
        return self.upvotes.count()

    def total_downvotes(self):
        """
        Retourne le nombre total de downvotes pour ce tip.
        """
        return self.downvotes.count()

    def has_voted(self, user):
        """
        Vérifie si un utilisateur a déjà voté (upvote ou downvote) pour ce tip.
        """
        return user in self.upvotes.all() or user in self.downvotes.all()
