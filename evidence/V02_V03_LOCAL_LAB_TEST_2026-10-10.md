# V02 + V03 — Reproduction locale des laboratoires Python

**Date :** 10 octobre 2026. **Environnement :** Python 3.13.5 sur machine de test isolée de l'assistant (Linux), **pas** le CRC/OpenShift de l'utilisateur. **Statut :** `LOCAL_TEST_PASS / SHA_EXACT_MATCH / GITHUB_ACTIONS_NOT_PROVEN`.

## Fichiers vérifiés

Les fichiers Python enregistrés sur GitHub ont été recopiés dans un répertoire local pour exécution. Les empreintes `git hash-object` calculées localement correspondent aux **SHA de blob GitHub** pour les quatre fichiers suivants.

| Fichier du Masterbook | SHA du blob GitHub et de la copie locale |
|---|---|
| `labs/v02-vectors/vector_math.py` | `94715688d853100bcd1e7dcd2002434e9e1560b3` |
| `labs/v02-vectors/test_vector_math.py` | `f5d15c5e63b2d07293125440b6334e963a16d26c` |
| `labs/v03-python-basics/statistics_basics.py` | `0a3d1bd7c1e848613ded0872bd1bc67d48ce7bdd` |
| `labs/v03-python-basics/test_statistics_basics.py` | `8a8353da06df2cc4cbf1a899fbb05ebbfe761e74` |

## Exécution réalisée

```bash
python -m unittest discover -s /mnt/data/masterbook_lab_check/v02 -p 'test_*.py' -v
# Ran 9 tests — OK
python -m unittest discover -s /mnt/data/masterbook_lab_check/v03 -p 'test_*.py' -v
# Ran 8 tests — OK
```

Observations pour V02 : produit scalaire `11.0`, norme `5.0`, distance `5.0`, cosinus `1.0`.  
Observations pour V03 : moyenne `5.0`, MAE `1.3333333333333333`.

La réussite des tests signifie que les implémentations pédagogiques remplissent **ces cas**, pas qu'elles sont numériquement robustes pour tous les jeux de données. Pour des calculs numériques extrêmes, comparer à des bibliothèques scientifiques éprouvées.

## Limites et prochaines validations

- Aucun matériel GPU, aucune API externe, aucun modèle d'inférence et aucun système bancaire réel n'ont été testés.
- Les workflows GitHub Actions échouent en amont de l'affectation du runner depuis la mise en privé du dépôt. Aucun succès CI n'est revendiqué pour ces versions.
- Rejouer les tests et archiver les logs dans GitHub Actions une fois le problème de runner résolu.
- Construire ensuite les PDF/EPUB via Quarto et contrôler les figures, les références et les équations.
