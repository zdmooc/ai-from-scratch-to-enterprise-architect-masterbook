# V01 R14 — Gradients et attention, essais locaux

**Date : 10 octobre 2026.** Statut **LOCAL_TEST_PASS / SHA_IDENTICAL / GITHUB_ACTIONS_NOT_VERIFIED**.

## Environnement

Python 3.13.5, Linux, CPU, bibliothèque standard uniquement. Tests exécutés dans un environnement isolé de l'assistant, **pas** sur le HP ZBook de l'auteur, le CRC/OpenShift ou un GPU.

## Identité des fichiers

Les SHA de blobs GitHub ont été comparées à `git hash-object` des copies exécutées :

| Fichier | SHA identique |
|---|---|
| `labs/v01-gradient-descent/gradient.py` | `fcb269ae3e7350d2b3bed06c3c8a6556f49722c3` |
| `labs/v01-gradient-descent/test_gradient.py` | `9b87d525a9ba712a6c017e2a93128e4f954de981` |
| `labs/v01-attention-qkv/attention.py` | `ba78e2eee169351e5c0e368999c0ddd76baabb28` |
| `labs/v01-attention-qkv/test_attention.py` | `877b00bfa07081c810364340e3f68a7052ad3551` |

## Résultats effectivement observés

```bash
python -m unittest discover -s labs/v01-gradient-descent -q
# Ran 17 tests — OK
python -m unittest discover -s labs/v01-attention-qkv -q
# Ran 20 tests — OK
```

**37/37 tests PASS.** Les résultats de démonstration sont :

- Descente sur L(w)=(w−4)² : (0,16), (2,4), (3,1), (3.5,0.25).
- Régression synthétique y=2x+1 : poids environ 2, biais environ 1.
- Attention sur Q=(1,0), K=((1,0),(0,1)), V=((2,0),(0,2)) : poids (0.6697615493, 0.3302384507), sortie (1.3395230987, 0.6604769013).

Les tests couvrent aussi dimensions incompatibles, matrices irrégulières, masques mal définis, NaN/Inf et paramètres numériques invalides.

## Limites

Ce sont deux laboratoires **pédagogiques**, pas un système de Deep Learning multi-couches, un vrai Transformer, une API autorisée ou un service de production. Les 37 réussites ne prouvent pas la qualité scientifique de l'ensemble du Volume 01. Les workflows GitHub Actions privés restent à vérifier ; aucun PDF/EPUB/HTML de publication n'a été généré. **R14 demeure partiel.**
