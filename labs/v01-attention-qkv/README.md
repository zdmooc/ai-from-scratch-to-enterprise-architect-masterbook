# LAB V01 — Calcul de l'attention Q/K/V

**Statut : DRAFT, tests locaux Python 3.13.5.** Implémentation originale et pédagogique du mécanisme de **scaled dot-product attention**, sans framework et sans modèle réel.

## Objectifs

- Calculer des produits scalaires Q × K, puis les diviser par √d.
- Appliquer un **softmax stable** en soustrayant le maximum.
- Combiner les vecteurs V selon les poids calculés.
- Lire la forme des tableaux Q, K et V.
- Comprendre le masque causal, les erreurs de dimensions et la différence entre un score numérique et une vérité factuelle.

## Définition des données

Une Query, deux Keys et deux Values synthétiques :

```text
Q = ((1, 0),)
K = ((1, 0), (0, 1))
V = ((2, 0), (0, 2))
```

Chaque ligne de Q/K a dimension d = 2. Les produits Q·K valent 1 et 0. Les scores mis à l'échelle sont (1/√2, 0), soit approximativement (0,7071, 0).

Après softmax, les poids sont environ (0,66976155, 0,33023845), de somme 1. La combinaison de V donne environ (1,33952310, 0,66047690).

Ces valeurs sont une **illustration de pondération**, pas une preuve de compréhension linguistique, de fiabilité documentaire ou de qualité d'un LLM.

## Formes et masques

- Q : Nq lignes de dimension dk.
- K : Nk lignes de dimension dk.
- V : Nk lignes de dimension dv ; dv peut différer de dk.
- Sortie : Nq vecteurs de dimension dv.

Un masque facultatif indique les Keys **autorisées** par chaque Query : True signifie visible, False signifie exclue. Un masque causal pour une séquence de trois tokens admet pour le premier token uniquement le premier ; pour le deuxième, les deux premiers ; pour le troisième, les trois.

La mise en place du masque causal n'est **pas automatique** dans la fonction : on doit transmettre explicitement `mask=causal_mask(n)`.

## Exécution

À la racine du dépôt :

```bash
python -m unittest discover -s labs/v01-attention-qkv -p 'test_*.py' -v
python labs/v01-attention-qkv/attention.py
```

Les 20 tests couvrent exemples exacts et approximatifs, somme des poids, multi-requêtes, masques, causalité, softmax de scores élevés, Q/K/V vides ou irréguliers, types incorrects, valeurs non finies et dimensions incompatibles.

## Exercices corrigés

**A.** Avec deux scores identiques et sans masque, quels sont les poids ?

*Correction.* 0,5 et 0,5.

**B.** Avec des valeurs V1 = (4, 0) et V2 = (0, 8), et des poids 0,25 / 0,75, calculer la sortie.

*Correction.* (1, 6).

**C.** Pourquoi ne pas calculer directement exp(1000) dans softmax ?

*Correction.* Risque de débordement numérique ; soustraire le score maximal conserve les rapports et évite cet overflow.

**D.** Le premier token d'une séquence autorégressive doit-il voir les tokens futurs ?

*Correction.* Non, si l'architecture utilise un masque causal tel que décrit ; celui-ci doit être correctement appliqué.

**E.** Peut-on conclure qu'une forte attention sur un token prouve que l'affirmation générée est exacte ?

*Correction.* Non. Les poids d'attention ne constituent pas une preuve de vérité, et leur interprétation dépend de l'architecture.

## Limites

Il ne s'agit ni d'un Transformer complet, ni d'un mécanisme multi-head optimisé, ni d'une implémentation GPU. Les masques gèrent uniquement l'accessibilité booléenne ; ils ne représentent pas des permissions métier. Une attention numérique correcte ne prouve pas la sécurité ou la conformité d'un service LLM.
