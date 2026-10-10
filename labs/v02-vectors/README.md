# LAB V02 — Vecteurs, produit scalaire et cosinus

**Statut : DRAFT** — Python standard uniquement, pas de GPU ou de service externe.

## Exécution

Depuis la racine du Masterbook :

```bash
python -m unittest discover -s labs/v02-vectors -p 'test_*.py' -v
python labs/v02-vectors/vector_math.py
```

Le programme affiche le produit scalaire 11, la norme 5, la distance 5 et un cosinus égal à 1.

## Objectifs contrôlés

- Produit scalaire, norme euclidienne, distance et similarité cosinus.
- Refus des vecteurs vides, tailles différentes, valeurs non finies et cosinus de vecteur nul.
- Les tests ne prouvent rien sur un modèle d'embeddings, un RAG ou un GPU.

## Exercice

Calculer à la main le cosinus de (1,1) et (1,-1), puis vérifier avec la fonction : les deux directions sont orthogonales et le cosinus attendu est 0.

**Précaution :** pour des nombres très grands, une implémentation industrielle exige davantage de travail de stabilité numérique. Le laboratoire sert à comprendre, pas à remplacer NumPy.
