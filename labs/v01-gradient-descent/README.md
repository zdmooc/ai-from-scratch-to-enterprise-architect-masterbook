# LAB V01 — Descente de gradient et régression linéaire

**Statut : DRAFT, tests locaux Python 3.13.5.** Aucun GPU, API, bibliothèque scientifique ou dataset client requis.

## Ce que le lecteur apprend

1. Calculer une **perte quadratique** sur un paramètre, avec une cible.
2. Établir la **dérivée analytique**, puis l'approcher par une **différence finie centrale**.
3. Observer trois itérations de descente de gradient, sans calcul caché.
4. Définir une régression linéaire à un poids et un biais, calculer l'erreur quadratique moyenne (MSE) et ses deux dérivées.
5. Comparer les gradients analytiques et numériques, puis entraîner le modèle sur quatre exemples synthétiques.
6. Provoquer des erreurs contrôlées : pas invalide, NaN, Inf, jeux vides, tailles incompatibles.

## Prérequis

- Volume 01 C05 : neurone, perte et gradient.
- Nombres, addition, multiplication et fonction du carré.
- Python 3.10 ou ultérieur, interpréteur standard uniquement.

## Première expérience à la main

La perte est L(w) = (w - 4)². Sa dérivée vaut 2(w - 4).
Au départ : w = 0, perte = 16, gradient = -8.

Avec un taux d'apprentissage égal à 0,25 :

| Étape | Poids | Gradient avant mise à jour | Perte |
|---|---:|---:|---:|
| 0 | 0 | -8 | 16 |
| 1 | 2 | -4 | 4 |
| 2 | 3 | -2 | 1 |
| 3 | 3,5 | -1 | 0,25 |

La descente utilise la formule w(suivant) = w - taux × dérivée. Pour cette fonction quadratique particulière, la plage 0 < taux < 1 permet de converger. Ce fait n'est **pas** un résultat valable pour n'importe quelle fonction de perte ni pour n'importe quel réseau.

## Deuxième expérience : ligne 2x + 1

Entrées synthétiques : x = (0, 1, 2, 3), cibles y = (1, 3, 5, 7).

Modèle : y_prédit = w×x + b.

La fonction `linear_mse_and_gradient` renvoie dans l'ordre :
- MSE, moyenne des carrés des erreurs ;
- dérivée de la MSE par rapport à w ;
- dérivée de la MSE par rapport à b.

Au point w = 0 et b = 0, les résultats attendus sont (MSE, dw, db) = (21, -17, -8). Au point w = 2 et b = 1, la perte et les deux gradients valent zéro.

## Exécuter depuis la racine du dépôt

```bash
python -m unittest discover -s labs/v01-gradient-descent -p 'test_*.py' -v
python labs/v01-gradient-descent/gradient.py
```

Les 17 tests vérifient les calculs et la validation d'entrées, y compris la comparaison des dérivées avec une différence finie. Conserver les logs et la version exacte du code pour constituer une preuve.

## Exercices corrigés

**A.** Avec L(w) = (w - 4)², w = 2 et taux = 0,25, calculer le poids suivant.

*Correction.* Gradient = 2(2 - 4) = -4. Poids suivant = 2 - 0,25×(-4) = 3.

**B.** Pourquoi la différence finie peut-elle différer légèrement de la dérivée analytique ?

*Correction.* Elle utilise des valeurs proches et une approximation numérique, sensibles à la taille du pas et à la représentation en virgule flottante.

**C.** Le modèle a trouvé w = 2 et b = 1 sur quatre points synthétiques. Est-il adapté à la prévision de dossiers réels ?

*Correction.* Non. Il n'a pas été évalué sur une population représentative, avec variables et labels réels, incertitude, drift et coûts.

**D.** Pourquoi refuser NaN et les listes de tailles différentes ?

*Correction.* Sans validation, on pourrait produire des résultats indéfinis, trompeurs ou non reproductibles.

## Limites

Cette implémentation sert à comprendre les gradients, pas à entraîner un Deep Learning industriel. Elle ne propose ni différentiation automatique générale, ni optimisation multicouche, ni garantie de stabilité pour tout taux d'apprentissage.
