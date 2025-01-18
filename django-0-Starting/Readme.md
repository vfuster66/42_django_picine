# Module 2 : Commencement - Piscine Django

## Structure du dépôt

Ce dépôt contient les solutions aux exercices de la formation Python-Django. Chaque exercice est organisé dans un dossier dédié, nommé selon la convention exXX, où XX correspond au numéro de l'exercice.

## Pré-requis

    Python 3 : Toutes les solutions sont développées pour fonctionner avec l'interpréteur Python 3.
    Dépendances externes : Aucun module externe n'est requis sauf indication contraire dans le sujet.

## Instructions générales

- Exécution des scripts : Pour chaque exercice, exécutez le fichier principal du dossier correspondant à l'aide de la commande python3.
- Règles spécifiques : Les scripts respectent les consignes suivantes :
    - Pas de code dans le scope global.
    - Les scripts s'exécutent uniquement via la condition : `if __name__ == "__main__":`.
    - Les erreurs potentielles sont gérées lorsque requis par le sujet.
- Machine virtuelle : Tous les scripts doivent être exécutés dans une machine virtuelle configurée conformément aux consignes générales.

## Détails des exercices

### Exercice 00 : Mes premières variables

- **Objectif** : Déclarer et afficher neuf variables de types différents avec leurs types respectifs.
- **Fichier** : `var.py`
- **Commande** : `python3 var.py`

---

### Exercice 01 : Nombres

- **Objectif** : Lire un fichier numbers.txt contenant des nombres séparés par des virgules et les afficher un par ligne.
- **Fichier** : `numbers.py`
- **Commande** : `python3 numbers.py`

---

### Exercice 02 : Mon premier dictionnaire

- **Objectif** : Transformer une liste de tuples en un dictionnaire, en utilisant les années comme clés et les noms comme valeurs, avec un affichage formaté.
- **Fichier** : `var_to_dict.py`
- **Commande** : `python3 var_to_dict.py`

---

### Exercice 03 : Recherche par clé

- **Objectif** : Trouver la capitale d'un état donné en utilisant deux dictionnaires.
- **Fichier** : `capital_city.py`
- **Commande** : `python3 capital_city.py <Nom de l'état>`

---

### Exercice 04 : Recherche par valeur

- **Objectif** : Trouver l'état correspondant à une capitale donnée.
- **Fichier** : `state.py`
- **Commande** : `python3 state.py <Nom de la capitale>`

---

### Exercice 05 : Recherche par clé ou par valeur

- **Objectif** : Identifier si une chaîne d'entrée correspond à une capitale, un état ou aucun des deux, avec prise en charge de multiples entrées.
- **Fichier** : `all_in.py`
- **Commande** : `python3 all_in.py "<Liste des entrées séparées par des virgules>"`

---

### Exercice 06 : Tri d’un dictionnaire

- **Objectif** : Trier un dictionnaire par année croissante, puis par ordre alphabétique en cas d'égalité.
- **Fichier** : `my_sort.py`
- **Commande** : `python3 my_sort.py`

---

### Exercice 07 : Tableau périodique des éléments

- **Objectif** : Lire un fichier décrivant le tableau périodique, générer une page HTML avec un tableau formaté et stylisé.
- **Fichier** : `periodic_table.py`
- **Commande** : `python3 periodic_table.py <Fichier d'entrée>`