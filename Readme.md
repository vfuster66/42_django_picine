# Piscine Django

## Résumé du projet
Ce projet fait partie d'une **piscine de formation** organisée autour du framework **Django**. Une piscine est un programme intensif permettant d'apprendre et de maîtriser une technologie à travers des modules quotidiens. Ce projet vise à initier et approfondir vos compétences en Django, en couvrant des concepts clés comme :

- L'installation et la configuration de base de Django.
- La manipulation des bases de données avec SQL et Django ORM.
- La gestion des sessions utilisateurs.
- Les notions avancées pour développer des applications robustes.

La piscine est conçue pour encourager un apprentissage collaboratif et continu sur une durée minimale de deux semaines.

## Un peu d'histoire sur Django

Django est un framework web open-source écrit en Python. Il a été initialement développé en 2003 par **Adrian Holovaty** et **Simon Willison** lorsqu'ils travaillaient pour le journal **Lawrence Journal-World**. Leur objectif était de créer un outil efficace pour développer rapidement des sites web dynamiques, tout en respectant des pratiques solides en matière de programmation.

En 2005, Django a été rendu public sous licence open-source, permettant à une communauté mondiale de développeurs de contribuer à son amélioration. Son nom est un hommage à Django Reinhardt, un célèbre guitariste de jazz, en clin d'œil à l'élégance et à la rapidité du framework.

Depuis, Django est devenu l'un des frameworks les plus populaires pour le développement web, apprécié pour sa simplicité, sa sécurité et son approche "batteries included" (tout-en-un). Il est utilisé par des entreprises et des organisations prestigieuses comme **Instagram**, **Pinterest**, et **Mozilla**.

### Pourquoi choisir Django ?
Django se distingue par :
- **Sa simplicité** : il permet de développer rapidement des applications web robustes.
- **Son efficacité** : il est optimisé pour gérer des bases de données, des utilisateurs et des contenus dynamiques avec un minimum de configuration.
- **Sa sécurité** : il intègre des protections contre les attaques web courantes comme l'injection SQL, les scripts intersites (XSS) ou le détournement de session (CSRF).
- **Sa communauté** : une vaste communauté de développeurs fournit des plugins, des extensions et des ressources pédagogiques.

En somme, Django est idéal pour les développeurs qui souhaitent un framework prêt à l'emploi pour créer des projets web allant des prototypes simples à des applications complexes en production.

## Structure du projet
Le projet est divisé en plusieurs modules à valider dans un ordre précis. Chaque module introduit des notions essentielles et progressives sur Django :

1. **Django - 0 - Initiation** : Introduction et configuration initiale de Django.
2. **Django - 0 - Starting** : Création d'une première application Django.
3. **Django - 0 - Oob** : Exploration des fonctionnalités "Out of the Box".
4. **Django - 1 - Lib** : Utilisation des librairies Django.
5. **Django - 1 - Base Django** : Notions fondamentales de Django.
6. **Django - 2 - SQL** : Interaction avec les bases de données via SQL et ORM.
7. **Django - 3 - Sessions** : Gestion des sessions et des utilisateurs.
8. **Django - 3 - Advanced** : Concepts avancés pour la création d'applications performantes.
9. **Django - 3 - Final** : Validation finale et consolidation des acquis.

## Règles de validation
Pour valider cette piscine, il est important de suivre les instructions suivantes :
- **Travail continu** : Il est préférable de soumettre votre travail chaque jour, même si celui-ci n'est pas finalisé.
- **Durée minimale** : Le projet nécessite au moins deux semaines d'investissement sérieux.
- **Évaluations par les pairs** : Chaque module doit être soumis et évalué dans les deux jours.
- **Ordre des modules** : Les modules doivent être complétés dans l'ordre indiqué, sans sauter d'étape.

## Comment démarrer
### Prérequis
- Python installé (version recommandée : 3.10+).
- Base de données PostgreSQL ou SQLite configurée.
- Virtualenv ou environnement virtuel Python pour isoler les dépendances.

### Installation
1. Clonez le dépôt :
```bash
   git clone <url_du_projet>
   cd <nom_du_dossier>
```

2. Installez les dépendances :
```
pip install -r requirements.txt
```
3. Lancez le serveur de développement
```
python manage.py runserver
```

### Ressources utiles
- [Documentation officielle de Django](https://docs.djangoproject.com/fr/5.1/)
