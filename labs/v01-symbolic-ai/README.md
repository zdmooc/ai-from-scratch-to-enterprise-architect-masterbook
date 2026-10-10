# V01 — LAB : premier moteur de règles en Python (standard library)

**Statut : DRAFT / pas de preuve runtime GitHub Actions pour ce dépôt privé.**

## Intention

Comprendre l'IA symbolique sans dépendre d'un LLM ou d'un GPU. Les faits, règles et sorties sont **synthétiques**. Aucun compte bancaire, secret, action financière ou service réseau.

## Prérequis
- Python 3.10+.
- Aucune installation de paquets.
- Exécuter depuis la racine du Masterbook, ou du dossier du lab.

## Test
```bash
python -m unittest discover -s labs/v01-symbolic-ai -p "test_*.py" -v
```

## Démonstration
```bash
python labs/v01-symbolic-ai/rule_engine.py
```

Exemple de sortie attendue : `investigation_candidate`, `read_events_permitted`, `audit_required` et `PAYMENT_MUTATION_ALLOWED: False`.

## Critères d'acceptation
- [ ] Les 7 tests passent sur une version de Python annoncée et consignée.
- [ ] Sans `requester_authenticated`, aucune investigation possible n'est déduite.
- [ ] Aucune permission de mutation n'apparaît dans les faits inférés.
- [ ] Un cycle de règles se termine au point fixe.
- [ ] Les conclusions sont liées à une trace `Derivation`.

## Limites
Le programme montre **une inférence pédagogique**, non la gestion d'autorisations réelles. Une permission telle que `read_events_permitted` n'est qu'un fait déduit ; le système cible doit imposer l'autorisation au niveau de l'API et du compte de service. Le lab n'a ni négation, ni retrait de faits, ni temporalité, ni analyse de conflits. Ne pas réutiliser tel quel pour des décisions opérationnelles.
