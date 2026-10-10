# V01 — Preuve de test local du laboratoire C11

**Date :** 2026-10-10. **Statut : LOCAL_REPRODUCTION_PASS / GITHUB_CI_NOT_PROVEN / NO_CRC_TEST.**

## Environnement et méthode

Copie **strictement identique** des fichiers GitHub dans un environnement isolé Linux, **Python 3.13.5**, sans dépendance, accès cloud ni GPU.

Les empreintes Git des copies locales ont été comparées à celles retournées par GitHub :

| Fichier | Git blob SHA, GitHub = copie |
|---|---|
| `labs/v01-experiment/experiment.py` | `eff4cc1cf4763f384797273933608ea7ce25a5c6` |
| `labs/v01-experiment/test_experiment.py` | `4b199462b71410ce202ff292694e07c64076268f` |

## Commande et résultats observés

```bash
python -m unittest discover -s /mnt/data/v01_experiment_check -p 'test_*.py' -v
# Ran 12 tests in 0.001s — OK
python /mnt/data/v01_experiment_check/experiment.py
```

Résultats imprimés :
- `train_count: 6`, `test_count: 4`
- `mean_prediction: 5.0`
- `fixed_mean_predictions: (5.0, 5.0, 5.0, 5.0)`
- `rolling_predictions: (7, 6, 8, 7)`
- `fixed_mean_mae: 2.5`
- `rolling_mae: 1.5`
- `protocol: one_step_ahead_with_observation_after_prediction`

**12/12 tests PASS** : valeurs attendues, MAE, protocole, entrées vides, NaN, booléens, longueur incohérente, immutabilité d'entrée et absence de connaissance de la valeur du jour au moment de la prédiction.

## Limites de la preuve

- Tests exécutés dans un environnement isolé de l'assistant, **pas** sur le HP ZBook, OpenShift CRC ou un runner GitHub Actions.
- L'expérience n'utilise que dix durées fictives : aucune affirmation de gain métier, de généralisation ML ou de résultat industriel.
- Le protocole à un pas suppose que la valeur du jour précédent a été reçue avant la prédiction suivante.
- La génération HTML, PDF et EPUB reste volontairement hors périmètre de cette phase de rédaction.

## Reste à faire

Rejouer en CI après résolution du problème de runner privé, puis vérifier la cohérence manuscrit/code dans les gates R13–R21.
