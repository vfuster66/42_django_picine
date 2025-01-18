# Piscine Django - SQL

## Prérequis

1. **Python** (3.10 ou supérieur)
2. **PostgreSQL**
3. **pip** et **virtualenv**

---

## Installation

### 1. Créer un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

# Django Exercises Readme

## Exercice 00 : SQL - Construction d’une table

- Accédez à `http://127.0.0.1:8000/ex00/init`.
- Vérifiez qu’un message **"OK"** s’affiche si la table `ex00_movies` est créée avec succès.
- En cas d’erreur, lisez le message d’erreur retourné pour corriger la configuration.

---

## Exercice 01 : ORM - Construction d’une table

- Allez dans l’interface d’administration Django : `http://127.0.0.1:8000/admin`.
- Connectez-vous avec votre **superuser**.
- Vérifiez que la table **Movies (ex01)** est présente et fonctionnelle.
- Ajoutez manuellement des entrées pour vérifier que les champs sont bien respectés.

---

## Exercice 02 : SQL - Insertion de données

- Accédez aux URLs suivantes :
  - `http://127.0.0.1:8000/ex02/init` : Crée la table.
  - `http://127.0.0.1:8000/ex02/populate` : Insère les données dans la table.
  - `http://127.0.0.1:8000/ex02/display` : Affiche les données sous forme de tableau HTML.

- Vérifiez que toutes les données sont correctement insérées et affichées.

---

## Exercice 03 : ORM - Insertion de données

- Testez les URLs suivantes :
  - `http://127.0.0.1:8000/ex03/populate` : Insère les données dans le modèle.
  - `http://127.0.0.1:8000/ex03/display` : Affiche les données.

---

## Exercice 04 : SQL - Suppression de données

- Accédez aux URLs :
  - `http://127.0.0.1:8000/ex04/init`.
  - `http://127.0.0.1:8000/ex04/populate`.
  - `http://127.0.0.1:8000/ex04/display`.
  - `http://127.0.0.1:8000/ex04/remove` : Testez le formulaire pour supprimer des films.

- Supprimez un film pour voir si la liste se met à jour correctement.

---

## Exercice 05 : ORM - Suppression de données

- Accédez aux URLs suivantes :
  - `http://127.0.0.1:8000/ex05/populate`.
  - `http://127.0.0.1:8000/ex05/display`.
  - `http://127.0.0.1:8000/ex05/remove`.

---

## Exercice 06 : SQL - Update d’une donnée

- Accédez aux URLs :
  - `http://127.0.0.1:8000/ex06/init`.
  - `http://127.0.0.1:8000/ex06/populate`.
  - `http://127.0.0.1:8000/ex06/display`.
  - `http://127.0.0.1:8000/ex06/update`.

- Testez le formulaire de modification pour changer un champ `opening_crawl`.

---

## Exercice 07 : ORM - Update d’une donnée

- Testez les URLs similaires à l’Exercice 06, mais utilisez les URLs pour `ex07` :
  - `http://127.0.0.1:8000/ex07/populate`.
  - `http://127.0.0.1:8000/ex07/display`.
  - `http://127.0.0.1:8000/ex07/update`.

---

## Exercice 08 : SQL - Foreign Key

- Testez les URLs suivantes :
  - `http://127.0.0.1:8000/ex08/init`.
  - `http://127.0.0.1:8000/ex08/populate`.
  - `http://127.0.0.1:8000/ex08/display`.

- Vérifiez que les relations **foreign key** fonctionnent correctement.

---

## Exercice 09 : ORM - Foreign Key

- Chargez les données initiales avec :
```bash
python3 manage.py loaddata ex09_initial_data.json
```

- Testez l’URL :
    - `http://127.0.0.1:8000/ex09/display`

## Exercice 10 : ORM - Many-to-Many

- Chargez les données initiales avec :
```bash
python3 manage.py loaddata ex10_initial_data.json
```

- Testez l’URL :
    - `http://127.0.0.1:8000/ex10/`

- Soumettez différentes combinaisons pour valider la logique de recherche.