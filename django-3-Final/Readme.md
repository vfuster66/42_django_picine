# Django Chat Application

## Description
Un système de chat en temps réel développé avec Django, utilisant AJAX et WebSockets pour la communication.

## Installation

1. Setup l'environnement virtuel
```
. ./setup.sh
```

2. Lancer l'application
```
python -m daphne d09.asgi:application
```

3. Accédez à l'application dans votre navigateur: [Login Page](http://127.0.0.1:8000/accounts/login/)


4. Chemins

- [Login Page](http://127.0.0.1:8000/accounts/login/)

- [Home](http://127.0.0.1:8000/account/)

- [chat](http://127.0.0.1:8000/chat/)

## Technologies utilisées

- Django
- jQuery
- Websockets (channels)
- Bootstrap 5
- Redis (pour les Websockets)

## Exercices et Implémentations

### Exercice 00 : AJAX Login System

Attendu : 
- Système de connexion/déconnexion utilisant uniquement AJAX
- Page avec deux comportements : formulaire de connexion ou "Logged as <user>" avec bouton déconnexion
- Pas de rafraîchissement de page
- Communication AJAX avec méthode POST

Implémenté avec :
- jQuery pour les requêtes AJAX
- Bootstrap pour le design
- Django AuthenticationForm
- Gestion des erreurs sans rafraîchissement
- Session persistence

### Exercice 01 : Basic Chat

Attendu :
- Page listant trois chatrooms
- Accessible uniquement aux utilisateurs connectés
- Affichage du nom de la room
- Multi-utilisateurs
- Messages visibles par tous les utilisateurs de la même room
- Affichage chronologique des messages
- Notification de connexion d'utilisateur

Implémenté avec :
- Django Channels pour les WebSockets
- Modèle ChatRoom pour la gestion des salles
- System de notification en temps réel
- Interface utilisateur responsive

### Exercice 02 : Message History

Attendu :
- Affichage des 3 derniers messages lors de la connexion
- Messages affichés du plus ancien au plus récent

Implémenté avec :
- Modèle Message pour la persistence des données
- Query optimisée pour récupérer les derniers messages
- Affichage chronologique maintenu

### Exercice 03 : User List

Attendu :
- Liste des utilisateurs connectés en temps réel
- Liste distincte des messages
- Mise à jour automatique lors des connexions/déconnexions
- Message système lors du départ d'un utilisateur

Implémenté avec :
- Gestion des utilisateurs connectés via WebSocket
- Interface séparée pour la liste des utilisateurs
- Notifications système pour les mouvements d'utilisateurs

### Exercice 04 : Scroll Management

Attendu :
- Conteneur de messages à hauteur fixe
- Barre de défilement pour les messages
- Scroll automatique vers le bas pour les nouveaux messages

Implémenté avec :
- CSS flexbox pour la mise en page
- JavaScript pour la gestion du scroll
- Design responsive
- Bootstrap pour l'interface utilisateur

## Dépendances
Voir <requirements.txt> pour la liste complète des dépendances.

Notes importantes

- L'application nécessite Redis pour les WebSockets. Assurez-vous qu'il est installé et en cours d'exécution.
- La configuration est optimisée pour le développement. Des ajustements seraient nécessaires pour la production.

## Structure du projet
```
d09/
├── account/         # Application de gestion des utilisateurs
├── chat/           # Application de chat
├── d09/           # Configuration du projet
├── templates/     # Templates globaux
├── requirements.txt
├── setup.sh
└── README.md
```
