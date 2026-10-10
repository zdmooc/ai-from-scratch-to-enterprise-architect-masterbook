# V01 — Validation locale du lab symbolique (sans GitHub Actions)

**Date :** 2026-10-10. **Environnement :** environnement d'exécution isolé de l'assistant, Linux, `Python 3.13.5` ; **ce n'est PAS** le PC HP ZBook/CRC de l'utilisateur. **Statut de preuve :** `LOCAL_REPRODUCTION_PASS`, pas `GITHUB_CI_PROVEN`, pas `CRC_RUNTIME_PROVEN`.

## Procédure
Une copie locale des fichiers Python rédigés pour `labs/v01-symbolic-ai` a été exécutée (aucune connexion bancaire, réseau ou cloud) :

```bash
python -m unittest discover -s <replica-local> -p 'test_*.py' -v
python <replica-local>/rule_engine.py
```

## Résultats observés

Sept tests ont terminé **OK** en 0.001 s :

1. chemin positif lecture seule — OK ;
2. refus sans authentification — OK ;
3. aucune permission de mutation dérivée — OK ;
4. idempotence au point fixe — OK ;
5. cycle de règles borné — OK ;
6. revue manuelle par fait explicite d'indisponibilité — OK ;
7. rejet des règles invalides — OK.

La démonstration a montré les dérivations R01, R02, R03 et `PAYMENT_MUTATION_ALLOWED: False`.

## Limites
- Une **copie locale du code authored**, et non un runner GitHub exécutant directement ce SHA, a servi à cette vérification. La comparaison binaire/checksum automatique GitHub↔copie locale n'a pas été effectuée.
- Les jobs GitHub Actions sur ce dépôt privé échouent actuellement **avant les étapes**, sans runner attribué ; ce n'est pas un test du code.
- `read_events_permitted` n'est qu'un fait déduit par le moteur fictif, jamais une autorisation API réelle.
- Ne pas étendre `LOCAL_REPRODUCTION_PASS` à une validation sur OpenShift, GPU ou un système financier.

## Contrôle restant
Rejouer les tests GitHub depuis un runner autorisé après diagnostic des droits/quotas, puis conserver les logs et le commit SHA.
