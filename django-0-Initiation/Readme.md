# Module 1 : Initiation - Piscine Django

## Résumé
Ce module introductif vise à poser les bases du **développement web** et à initier les participants à des technologies essentielles comme **HTML**, **CSS**, **JavaScript** et le protocole **HTTP**. Ces compétences serviront de fondations solides pour la suite de la piscine Django.

Au programme :
- Création d’un script shell interactif.
- Conception d’un CV structuré en HTML et CSS.
- Construction d’un formulaire dynamique avec intégration JavaScript.
- Reproduction d’une page web existante.
- Validation du code selon les standards W3C.

---

## Structure du module

### Exercice 00 : Premier script shell
- **Objectif** : Développer un script shell permettant de dévoiler l’adresse réelle d’un lien `bit.ly`.
- **Technologies utilisées** : `curl`, `grep`, `cut`.
- **Dossier de rendu** : `ex00/`
- Exemple d’utilisation :
```bash
  $ ./myawesomescript.sh bit.ly/1O72s3U
  http://42.fr/
```
- **Dossier de rendu** : `ex00/`

--- 

### Exercice 01 : Votre CV en HTML
- **Objectif** : Concevoir un CV en HTML/CSS en respectant une structure sémantique.
- **Exigences** : 
Utiliser des listes (`ul`, `ol`), des tableaux (`table`, `tr`, `td`) et appliquer des styles.
Inclure des sections obligatoires : nom, prénom, compétences, parcours.

- **Dossier de rendu** : `ex01/`

---

### Exercice 02 : Formulaire d’envoi d’emails

- **Objectif** : Construire un formulaire de contact dynamique.
- **Exigences** :
        Inclure des champs spécifiques (prénom, nom, email, téléphone, âge, etc.).
        Intégrer un fichier JavaScript fourni (sans le modifier).
        Faire apparaître une pop-up avec les données saisies.
- **Dossier de rendu** : `ex02/`

---

### Exercice 03 : Reproduction d’une page web

- **Objectif** : Reproduire une page web à partir d’un screenshot et d’un fichier CSS fourni.
- **Exigences** :
        Respecter la structure HTML et utiliser le fichier CSS sans modification.
- **Dossier de rendu** : `ex03/`

---

### Exercice 04 : Intégration de snippets JavaScript

- **Objectif** : Intégrer plusieurs fichiers JavaScript dans une page HTML.
- **Exigences** :
        Importer les scripts sans les modifier.
        Assurer que le résultat attendu (pop-up fonctionnelle) s’affiche correctement.
- **Dossier de rendu** : `ex04/``

---

### Exercice 05 : Validation W3C

- **Objectif** : Corriger une page HTML pour qu’elle respecte les normes W3C.
- **Exigences** :
        Corriger les erreurs et avertissements signalés par le validateur W3C.
- **Dossier de rendu** : `ex05/`
- **Outil recommandé** : [W3C Validator](https://validator.w3.org/)

---

## Règles générales

- Tous les projets doivent être réalisés dans une `machine virtuelle` configurée pour le développement.
- Le dépôt Git doit contenir un dossier spécifique pour chaque exercice.
- `Tests recommandés` : Bien que non évalués, des tests sont essentiels pour valider votre travail.

## Ressources utiles

- [Documentation officielle HTML](https://developer.mozilla.org/fr/docs/Web/HTML)
- [Documentation officielle CSS](https://developer.mozilla.org/fr/docs/Web/CSS)
- [Documentation officielle JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [W3C Validator](https://validator.w3.org/)