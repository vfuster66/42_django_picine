# Module 4 : Lib - Piscine Django

## Description

Ce projet a pour objectif de manipuler différentes librairies Python utiles, tout en respectant des règles strictes de structuration et d'organisation du code. Chaque exercice est indépendant et explore une fonctionnalité ou une librairie spécifique.

## Exigences Générales

- Tous les exercices doivent être réalisés dans une machine virtuelle.
- La machine virtuelle doit contenir tous les logiciels nécessaires à l’exécution du projet.
- Les fichiers doivent être conformes aux règles de nommage précisées dans chaque exercice.
- Aucun code ne doit figurer dans l’espace global : toutes les fonctionnalités doivent être encapsulées dans des fonctions.
- Le programme principal doit être exécuté dans une condition `if __name__ == "__main__"`.
- Les modules utilisés doivent être explicitement autorisés par le sujet.
- En cas d’erreur, un message pertinent doit être affiché et le programme doit se terminer proprement.

## Structure des Fichiers

Le projet est organisé en plusieurs dossiers correspondant aux exercices, chacun contenant les fichiers requis pour le bon fonctionnement et la soutenance.

- `ex00/` : Programme calculant un géohash.
- `ex01/` : Script d’installation et programme utilisant Path.py.
- `ex02/` : Script de requête à l'API Wikipédia.
- `ex03/` : Programme explorant les "roads to philosophy".
- `ex04/` : Script de configuration d’un virtualenv pour Django.
- `ex05/` : Projet Django affichant "Hello World!".

---

## Exercices

### Exercice 00 : Antigravity

**Objectif :**  
Créer un programme permettant de calculer un géohash en utilisant le module Python intégré `antigravity`.

**Détails :**  
- Prend en paramètre les données nécessaires pour le calcul.
- Affiche le géohash calculé sur la sortie standard.
- Gère les erreurs avec des messages pertinents.

---

### Exercice 01 : Pip et Path.py

**Objectif :**  
Installer une bibliothèque Python depuis un dépôt GitHub à l’aide de `pip`, puis utiliser cette bibliothèque dans un programme Python.

**Détails :**  
- Créer un script Bash pour gérer l'installation et les logs.
- Créer un programme Python qui utilise la bibliothèque installée pour effectuer des opérations sur des fichiers et dossiers.
- Générer les logs dans un fichier spécifique.

---

### Exercice 02 : Requêter l'API Wikipédia

**Objectif :**  
Requêter l'API de Wikipédia pour rechercher des informations sur un sujet donné, puis sauvegarder le résultat dans un fichier au format `.wiki`.

**Détails :**  
- Traiter les erreurs de requête et afficher des messages pertinents en cas de problème.
- Nettoyer le contenu pour supprimer les formats JSON ou Wiki Markup avant de sauvegarder.
- Gérer les noms de fichiers pour qu'ils soient compatibles avec le système.

---

### Exercice 03 : Parser HTML avec BeautifulSoup

**Objectif :**  
Créer un programme qui explore les "roads to philosophy" sur Wikipédia, en suivant le premier lien valide dans l'introduction d'un article jusqu'à atteindre l'article "Philosophy" ou une impasse.

**Détails :**  
- Identifier et gérer les redirections sur Wikipédia.
- Compter le nombre d’articles visités avant d’atteindre "Philosophy".
- Gérer les boucles infinies et les pages sans lien valide avec des messages appropriés.

---

### Exercice 04 : Virtualenv

**Objectif :**  
Configurer un environnement Python isolé pour préparer une installation Django.

**Détails :**  
- Créer un fichier `requirement.txt` contenant Django et psycopg2.
- Écrire un script Bash pour créer un environnement virtuel, installer les dépendances, et l’activer automatiquement.

---

### Exercice 05 : Hello World avec Django

**Objectif :**  
Créer une application Django affichant "Hello World!" à l’URL `/helloworld`.

**Détails :**  
- Suivre les étapes d’installation et de configuration de Django.
- Configurer les routes pour afficher le texte sur le navigateur à l’adresse spécifiée.
- Structurer le projet selon les conventions Django.

---

## Instructions pour Lancer le Projet

## Installation

1. Créez un environnement virtuel et activez-le :
```
. ./setup.sh
```

2. Démarrez le serveur de développement :
```
python manage.py runserver
```

---

