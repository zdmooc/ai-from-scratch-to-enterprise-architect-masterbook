# LAB V01 — Agent à outils en lecture seule et refus explicites

**Statut : DRAFT / démonstration synthétique, NON un serveur MCP ni une API sécurisée réelle.**

## Objectif pédagogique

Démontrer que **la sécurité d'un agent n'est pas obtenue en écrivant « ne modifie rien » dans un prompt**. Les outils autorisés sont explicitement limités en code. Le contrôle s'applique lors du dispatch des demandes.

Le laboratoire simule deux locataires (A et B), trois identités fictives, des tickets, des documents consultables et un texte non fiable contenant une fausse instruction de suppression. Aucun compte ni donnée réelle.

## Périmètre

- **Autorisé :** lecture de ticket et de document accessible.
- **Refusé :** outils non déclarés, outil de suppression, document hors rôle, ticket/document d'un autre locataire, utilisateur inconnu.
- **Borné :** maximum explicite d'étapes par plan.
- **Observation hostile :** le document demandant une suppression est traité comme **texte**, pas comme commande.

## Exécution

Depuis la racine du Masterbook, Python 3.10+ :

```bash
python -m unittest discover -s labs/v01-agent-guardrails -p 'test_*.py' -v
python labs/v01-agent-guardrails/agent_dispatcher.py
```

## Contrôles

16 tests unitaires : autorisations de lecture, refus inter-locataire, restrictions par rôle, rejet d'utilisateur inconnu, refus d'outils non permis, texte malveillant sans pouvoir d'exécution, borne d'étapes et absence de modification des données synthétiques.

## Limites fondamentales

- Le dispatcher n'est pas un système IAM réel ; il n'authentifie pas un utilisateur via un fournisseur externe.
- L'autorisation doit être **réévaluée côté API cible** dans une vraie architecture et le modèle doit recevoir le minimum de droits nécessaires.
- Ce jouet ne prouve pas qu'un agent LLM réel résisterait à toute injection de prompt ou attaque sur un serveur MCP.
- Les données sont volontairement petites et sans persistance.
- Aucun outil de paiement, de mutation de cluster ou d'accès aux secrets n'existe dans ce programme.

**Conditions pour une démonstration de production :** identité authentifiée, politiques côté service, traces protégées, limites, version de contrats, test des scénarios adversariaux et revue indépendante.
