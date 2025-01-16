from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """
    Modèle utilisateur personnalisé avec un système de réputation basé sur 
    les votes des Tips.
    """
    reputation = models.IntegerField(default=0)

    # Résolution des conflits en définissant des `related_name` personnalisés
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def can_downvote(self):
        """
        Vérifie si l'utilisateur peut effectuer un downvote.
        """
        return self.reputation >= 15

    def can_delete_tip(self):
        """
        Vérifie si l'utilisateur peut supprimer un Tip.
        """
        return self.reputation >= 30

    def update_reputation(self):
        """
        Met à jour la réputation de l'utilisateur en fonction des votes
        reçus par ses Tips.
        """
        upvotes = sum(tip.total_upvotes() for tip in self.tips_posted.all())
        downvotes = sum(
            tip.total_downvotes() for tip in self.tips_posted.all()
        )
        self.reputation = (upvotes * 5) - (downvotes * 2)
        self.save()


class Tip(models.Model):
    """
    Modèle représentant une astuce (Tip).
    """
    contenu = models.TextField()  # Contenu du Tip
    auteur = models.ForeignKey(
        CustomUser,
        related_name="tips_posted",
        on_delete=models.CASCADE,
    )  # Auteur du Tip
    date = models.DateTimeField(auto_now_add=True)  # Date et heure de création
    upvotes = models.ManyToManyField(
        CustomUser,
        related_name="upvoted_tips",
        blank=True,
    )  # Utilisateurs ayant upvoté
    downvotes = models.ManyToManyField(
        CustomUser,
        related_name="downvoted_tips",
        blank=True,
    )  # Utilisateurs ayant downvoté

    class Meta:
        permissions = [
            ("can_downvote", "Peut effectuer un downvote"),
        ]

    def __str__(self):
        """
        Représentation textuelle de l'objet Tip.
        """
        return (
            f"Tip de {self.auteur.username} - "
            f"{self.date.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def total_upvotes(self):
        """
        Retourne le nombre total d'upvotes pour ce Tip.
        """
        return self.upvotes.count()

    def total_downvotes(self):
        """
        Retourne le nombre total de downvotes pour ce Tip.
        """
        return self.downvotes.count()

    def has_voted(self, user):
        """
        Vérifie si un utilisateur a déjà voté (upvote ou downvote) pour ce Tip.
        """
        return (
            self.upvotes.filter(pk=user.pk).exists() or
            self.downvotes.filter(pk=user.pk).exists()
        )

    def save(self, *args, **kwargs):
        """
        Enregistre le Tip et met à jour la réputation de l'auteur.
        """
        super().save(*args, **kwargs)
        if self.auteur:
            self.auteur.update_reputation()

    def delete(self, *args, **kwargs):
        """
        Supprime le Tip et annule son influence sur la réputation de l'auteur.
        """
        # Supprimer l'influence des votes avant suppression
        self.upvotes.clear()
        self.downvotes.clear()
        super().delete(*args, **kwargs)
        if self.auteur:
            self.auteur.update_reputation()
