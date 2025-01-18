# Module 7 : Sessions - Piscine Django

# Django Life Pro Tips

## Description
Ce projet est une application Django destinée à permettre aux utilisateurs de partager des astuces (Life Pro Tips). Il inclut des fonctionnalités telles que la gestion des utilisateurs, un système de sessions anonymes, la création et la gestion des astuces, ainsi qu'un système de votes et de permissions basées sur la réputation.

## Fonctionnalités
1. **Sessions anonymes** : 
   - Attribution automatique d'un nom d'utilisateur aléatoire avec une validité de 42 secondes.
   - Affichage du nom d'utilisateur dans la barre de navigation.

2. **Gestion des utilisateurs** :
   - Pages d'inscription et de connexion avec validation des données.
   - Gestion des sessions utilisateur et redirection en fonction de l'état de connexion.

3. **Création et gestion des astuces** :
   - Système permettant aux utilisateurs connectés de publier des astuces.
   - Liste des astuces affichées sur la page d'accueil avec auteur, date et contenu.

4. **Votes** :
   - Système d'upvotes et downvotes pour les astuces.
   - Restriction des actions aux utilisateurs connectés.
   - Gestion des incohérences telles que le vote multiple ou les votes opposés sur une même astuce.

5. **Permissions** :
   - Contrôle d'accès pour la suppression des astuces basé sur les permissions.
   - Implémentation de permissions personnalisées pour les downvotes.

6. **Réputation** :
   - Système de réputation basé sur les votes reçus par les astuces.
   - Attribution automatique de permissions en fonction de la réputation d'un utilisateur.

## Prérequis
- Python 3.x
- Django (version LTS)
- Bootstrap (pour le frontend)

## Installation
1. Créez un environnement virtuel et activez-le :
```
. ./setup.sh
```

2. Démarrez le serveur de développement :
```
python manage.py runserver
```

## Utilisation
1. Accédez à l'URL de la page d'accueil pour voir les astuces et commencer à utiliser l'application.
2. Inscrivez-vous ou connectez-vous pour accéder aux fonctionnalités avancées comme la création d'astuces et les votes.
