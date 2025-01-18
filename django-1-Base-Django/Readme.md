# Module 5 : Base - Piscine Django

Ce projet explore les fonctionnalités fondamentales du framework Django en suivant plusieurs exercices pratiques. Chaque exercice introduit un concept clé de Django, de la création de pages statiques à la gestion de formulaires, tout en respectant les bonnes pratiques.

## Prérequis

- Python 3
- Virtualenv
- Django (version spécifiée dans `requirements.txt`)

## Installation

1. Créez un environnement virtuel et activez-le :
```
. ./setup.sh
```

2. Démarrez le serveur de développement :
```
python manage.py runserver
```

## Structure du Projet

Le projet est divisé en plusieurs applications indépendantes, chacune correspondant à un exercice.

### Ex00 : Première Page Statique

- **URL** : `/ex00`
- **Description** : Une page statique présentant une cheatsheet Markdown. Le template utilisé est `index.html`.

### Ex01 : Quelques Pages de Plus

- **URLS disponibles** :
    - `/ex01/django` : Introduction au framework Django et son historique.
    - `/ex01/affichage` : Explication du processus d'affichage d'une page statique avec Django.
    - `/ex01/templates` : Présentation du moteur de templates de Django, y compris les blocs, les boucles, les structures conditionnelles et l'affichage de variables passées par contexte.

- **Particularité** : Toutes les pages s'appuient sur un template de base `base.html`. Une barre de navigation (`nav.html`) est incluse dans chaque page.

### Ex02 : Premier Formulaire

- **URL** : `/ex02`

- **Fonctionnalités** :
    - Un formulaire dynamique utilisant `django.forms.Form`.
    - Un historique des entrées, persisté dans un fichier de logs et affiché sur la page.

- **Particularités** :
    - Les données sont conservées même après un redémarrage du serveur.
    - Le chemin du fichier de logs est défini dans `settings.py`.

---

### Ex03 : Fifty Shades of Bic

- **URL** : `/ex03`

- **Description** : Affiche un tableau de 4 colonnes et 51 lignes, chaque colonne correspondant à une couleur (noir, rouge, bleu, vert). Les nuances des couleurs sont générées dynamiquement pour former des dégradés.

- **Contraintes respectées** :
    - Pas de couleurs codées en dur dans le template.
    - Utilisation de seulement 4 couples de balises `<td>` et `<th>` dans le template.

## Déploiement

- Utilisez collectstatic pour gérer les fichiers statiques si nécessaire :
```
python manage.py collectstatic
```

- Vérifiez les configurations pour le serveur de production.