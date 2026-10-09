# BookBot — Analyse de livres en Python

Un livre, un script, quelques statistiques : **BookBot** est un outil en ligne de commande qui analyse un fichier texte et affiche son nombre de mots ainsi que la fréquence de ses lettres.

Ce lab a été réalisé dans le cadre du parcours [Boot.dev](https://www.boot.dev). Il permet de mettre en pratique les bases de Python à travers un projet concret, de la lecture d'un fichier à la génération d'un rapport.

## Fonctionnalitésf

- Lire un livre depuis un fichier texte fourni en argument.
- Compter les mots du document.
- Compter les caractères sans distinguer les majuscules et les minuscules.
- Afficher uniquement les caractères alphabétiques, triés par fréquence décroissante.
- Afficher une indication d'utilisation lorsqu'aucun chemin n'est fourni.

## Prérequis

- **Python 3.9 ou supérieur** : le code utilise les annotations `list[...]`, `dict[...]` et `tuple[...]`.
- **Git** pour cloner le dépôt.

Le projet utilise uniquement la bibliothèque standard de Python : aucune dépendance externe à installer.

## Installation

```bash
git clone https://github.com/LorOFab/BookBot.git
cd BookBot
python3 --version
```

## Utilisation

Depuis la racine du projet, lancer le script en indiquant le chemin du livre :

```bash
python3 main.py books/frankenstein.txt
```

Trois livres sont inclus pour essayer le programme :

```bash
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

Il est également possible d'analyser son propre fichier texte :

```bash
python3 main.py "/chemin/vers/mon livre.txt"
```

> Sous Windows, selon l'installation de Python, remplacer `python3` par `python` ou `py`.

### Exemple de rapport

Avec un fichier contenant `Hello world!`, le programme affiche :

```text
============ BOOKBOT ============
Analyzing book found at books/example.txt
----------- Word Count ----------
Found 2 total words
--------- Character Count -------
l: 3
o: 2
h: 1
e: 1
w: 1
r: 1
d: 1
============= END ===============
```

Cet exemple est illustratif : `books/example.txt` n'est pas inclus dans le dépôt.

Sans argument, le programme affiche la commande attendue et se termine avec le code de sortie `1` :

```text
Usage: python3 main.py <path_to_book>
```

## Organisation du projet

| Fichier | Rôle |
| --- | --- |
| `main.py` | Gestion de l'argument, lecture du fichier et affichage du rapport. |
| `stats.py` | Comptage des mots, comptage des caractères et tri des résultats. |
| `books/frankenstein.txt` | Livre fourni pour tester l'analyse. |
| `books/mobydick.txt` | Deuxième livre de test. |
| `books/prideandprejudice.txt` | Troisième livre de test. |

## Fonctionnement

1. Le script récupère le chemin du livre via `sys.argv`.
2. Le contenu est lu avec `open()` et un gestionnaire de contexte `with`.
3. `get_number_of_words()` compte les éléments obtenus avec `split()`.
4. `count_characters()` convertit chaque caractère en minuscule et comptabilise ses occurrences dans un dictionnaire.
5. `chars_dict_to_sorted_list()` trie les couples `(caractère, nombre)` par fréquence décroissante.
6. `print_report()` affiche le nombre de mots et les caractères retenus par `isalpha()`.

Les espaces, chiffres et signes de ponctuation sont comptés en interne, mais ne sont pas affichés dans le rapport. Le comptage des mots repose sur les espaces et autres séparateurs reconnus par `split()` : il ne s'agit pas d'une analyse linguistique.

## Notions travaillées

- Lecture de fichiers et gestionnaires de contexte.
- Fonctions, modules et séparation des responsabilités.
- Manipulation de chaînes, listes, tuples et dictionnaires.
- Tri avec `sorted()` et une fonction clé.
- Arguments en ligne de commande avec `sys.argv`.
- Annotations de types et formatage avec les f-strings.

## Limites et pistes d'amélioration

Le chemin doit désigner un fichier texte existant et lisible. Les erreurs de lecture ne sont pas encore interceptées, et l'encodage utilisé est celui par défaut de l'environnement.

Quelques évolutions possibles :

- Ajouter une gestion des fichiers introuvables et des erreurs d'encodage.
- Lire le fichier une seule fois et réutiliser son contenu pour les deux analyses.
- Ajouter des tests unitaires pour les fonctions statistiques.
- Exporter les résultats en JSON ou CSV.

## Auteur

Projet réalisé par [Samad Oceni Abiola](https://github.com/LorOFab), dans le cadre du lab BookBot de Boot.dev.
