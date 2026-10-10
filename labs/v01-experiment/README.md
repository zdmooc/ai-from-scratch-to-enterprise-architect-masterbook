# LAB V01 — Prévision élémentaire et protocole mesurable

**Statut : DRAFT / aucune CI GitHub revendiquée.** Le laboratoire utilise uniquement Python standard et dix durées **synthétiques** ; aucun modèle d'IA externe, GPU ou service cloud n'est appelé.

## But

Faire la différence entre démonstration et mesure en comparant deux baselines : moyenne des six premières durées et prédiction pas à pas par dernière observation disponible.

## Protocole

- **Entraînement** : J01–J06, durées (3, 5, 4, 6, 5, 7).
- **Test** : J07–J10, durées (6, 8, 7, 9).
- **Baseline A** : moyenne du train = 5, donc prévisions (5, 5, 5, 5).
- **Baseline B** : prédiction du prochain jour d'après la dernière durée observée = (7, 6, 8, 7).
- **Mesure** : erreur absolue moyenne (MAE).
- **Valeurs attendues calculées dans le cours** : 2,5 minutes pour A, 1,5 pour B.

**Attention :** la baseline B ne peut consulter la vraie observation du jour J qu'après avoir prédit ce jour. Si l'on devait prévoir J07–J10 d'un seul coup le soir de J06, ce protocole serait inadapté.

## Reproduire

À la racine du Masterbook, avec Python 3.10+ :

```bash
python -m unittest discover -s labs/v01-experiment -p 'test_*.py' -v
python labs/v01-experiment/experiment.py
```

## Critères PASS/FAIL

- Les **12 cas unitaires** passent dans un environnement annoncé.
- Les MAE et prévisions sont cohérentes avec les corrections du chapitre C11.
- Les entrées vides, valeurs NaN/inf et séries de tailles incompatibles sont rejetées.
- Le test de non-fuite montre qu'une future observation ne modifie pas la prévision du jour courant.
- Le rapport de test distingue la validation locale des éventuelles exécutions CI.

## Limites

Les dix observations artificielles ne permettent **aucune** conclusion sur un gain métier, une qualité ML en production ou une infrastructure GPU. Un vrai protocole exigerait des données représentatives, une validation séparée, une analyse d'incertitude et un contrôle des coûts.

Le code n'implémente ni serveur bancaire ni accès à des données personnelles. Les fichiers Drive originaux ne sont pas nécessaires à son exécution.
