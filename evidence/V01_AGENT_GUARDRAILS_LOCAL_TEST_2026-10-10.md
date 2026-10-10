# V01 — Vérification locale du laboratoire d'agent en lecture seule

**Date : 2026-10-10. Statut : LOCAL_REPRODUCTION_PASS / SHA_MATCH / GITHUB_CI_NOT_PROVEN.**

## Environnement et source

Code original des fichiers GitHub recopié à l'identique dans l'environnement Linux de l'assistant ; **Python 3.13.5**, aucune dépendance externe, aucun accès réseau, cluster OpenShift ou outil bancaire.

| Fichier | SHA GitHub et copie locale identiques |
|---|---|
| `labs/v01-agent-guardrails/agent_dispatcher.py` | `e4ba63632405a859eb8894bfac75f566cbfc8a8b` |
| `labs/v01-agent-guardrails/test_agent_dispatcher.py` | `d33bd3ca85145b50072145774162be05322710f8` |

Les empreintes sont celles de `git hash-object` sur les copies locales et des blobs retournés par GitHub.

## Commandes et observation

```bash
python -m unittest discover -s /mnt/data/v01_agent_check -p 'test_*.py' -v
# Ran 16 tests in 0.002s — OK
python /mnt/data/v01_agent_check/agent_dispatcher.py
```

Résultats observés :
- Ticket synthétique A-001 consulté : `waiting_for_review`.
- Document public interne du locataire A consulté.
- Appel d'outil `delete_ticket` explicitement refusé : `DENIED: Tool not permitted by the dispatcher`.
- **16/16 tests PASS** : lecture permise, rôle autorisé, refus d'utilisateur inconnu, isolation des deux locataires, contrôle des outils autorisés, borne d'étapes, injection dans contenu **non interprétée comme outil**, absence de mutation.

## Limites à conserver

- Un programme Python de démonstration **n'est pas un agent LLM réel**, un serveur MCP, un mécanisme OIDC ni une API bancaire.
- Le test vérifie uniquement le code synthétique présent, pas la robustesse globale aux prompt injections, la sécurité réseau ou l'intégration avec un système cible.
- Dans une vraie architecture, l'autorisation doit être contrôlée par **le service cible**, avec identité authentifiée, politique traçable, validation d'arguments et gestion des secrets.
- Les tests ne couvrent ni une authentification réelle, ni la résistance au déni de service, ni la gestion de consentement ou des réglementations.
- Les workflows GitHub Actions sur dépôt privé restent à revérifier après résolution du problème de runner.

Cette preuve est limitée à la **réproduction locale des 16 cas synthétiques avec identité de fichiers établie par SHA**.
