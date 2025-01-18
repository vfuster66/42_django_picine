# Module 8 : Blog project - Piscine Django

# Django Advanced Features Project

## Description
Ce projet explore les fonctionnalités avancées de Django en développant un site web permettant la consultation et la gestion d'articles. Il met en œuvre des concepts tels que les modèles, les vues génériques, les formulaires, les filtres et les tests, avec une attention particulière portée à la structuration et à l'extensibilité.

## Structure du Projet
Le projet est divisé en plusieurs exercices, chacun ajoutant des fonctionnalités spécifiques. Voici un aperçu des principales fonctionnalités implémentées :

- **Exercice 00** : Création des modèles `Article` et `UserFavouriteArticle`, avec une interface utilisateur minimale pour afficher les articles.
- **Exercice 01** : Ajout de vues génériques pour afficher les publications d'un utilisateur connecté, les détails d'un article, et gérer la connexion/déconnexion des utilisateurs.
- **Exercice 02** : Utilisation de `CreateView` pour permettre l'inscription des utilisateurs, la publication d'articles et l'ajout d'articles aux favoris.
- **Exercice 03** : Création de balises et filtres de templates pour personnaliser l'affichage, comme la réduction du synopsis et le tri des articles par date.
- **Exercice 04** : Intégration de Bootstrap pour améliorer l'apparence du menu principal.
- **Exercice 05** : Ajout de l'internationalisation pour basculer entre l'anglais et le français en fonction des URL.
- **Exercice 06** : Implémentation de tests unitaires pour vérifier les restrictions d'accès et les fonctionnalités principales.

## Fonctionnalités Clés
- **Affichage des Articles** : Page listant tous les articles avec leurs métadonnées, sauf le contenu complet.
- **Connexion/Déconnexion** : Gestion des utilisateurs avec un système de sessions.
- **Publications et Favoris** : Fonctionnalités pour afficher les articles publiés et enregistrés en favoris par l'utilisateur connecté.
- **Création d'Utilisateurs et d'Articles** : Formulaires pour inscrire de nouveaux utilisateurs et publier des articles.
- **Personnalisation des Templates** : Utilisation de tags et filtres pour améliorer l'affichage.
- **Internationalisation** : Basculer entre l'anglais et le français selon les préférences de l'utilisateur.
- **Tests Unitaires** : Vérification des comportements des vues et des modèles.

## Installation et Lancement
1. Clonez le dépôt Git.
2. Configurez un environnement virtuel Python.
3. Installez les dépendances depuis le fichier `requirements.txt`.
4. Effectuez les migrations de la base de données.
5. Démarrez le serveur de développement Django.

## Dépendances
Le projet utilise des outils standards de Django, notamment :
- ORM Django pour la gestion des bases de données.
- Vues génériques pour réduire la duplication de code.
- Framework de tests intégré pour valider les fonctionnalités.

## Tests
Des tests unitaires ont été implémentés pour garantir :
- L'accès restreint aux vues protégées.
- L'intégrité des données, comme la prévention des doublons dans les favoris.
- La bonne exécution des formulaires et des redirections.
