# LAB V03 — Premiers calculs Python reproductibles

**Statut : DRAFT**. Python standard uniquement. Entrées entièrement synthétiques.

## Exécution

Depuis la racine du Masterbook :

```bash
python -m unittest discover -s labs/v03-python-basics -p 'test_*.py' -v
python labs/v03-python-basics/statistics_basics.py
```

Les valeurs attendues dans la démonstration sont `mean = 5.0` et une MAE d'environ `1.3333333333333333`.

## Ce qui est testé

Moyenne simple, observations négatives, erreur absolue moyenne et refus d'entrées vides, non finies, non numériques ou de tailles incompatibles.

## Exercice supplémentaire

Implémenter une médiane sans importer de bibliothèque externe ; écrire au moins un test pour un nombre pair d'éléments, un nombre impair et une liste vide.

**Limites :** la qualité de la donnée et l'absence de fuites temporelles ne sont pas vérifiées par ces petites fonctions ; ce sont des notions abordées dans les volumes 04 et 05.
