# Contrat de besoins — Case Study V01

**PROPOSED / SYNTHETIC — paramètres à confirmer avant toute mise en œuvre.**

## Besoin métier

L'équipe fictive souhaite retrouver des procédures internes et expliquer le statut de tickets sans exposer de contenu hors autorisation, et sans automatiser d'opération de production.

### Parties prenantes

| Acteur | Responsabilité |
|---|---|
| Technicien | Recherche et consultation de documents accessibles |
| Responsable de support | Approuve les besoins, les risques et le scénario opérationnel |
| Propriétaire des documents | Version, date d'effet, classification, retrait |
| Équipe IAM | Fournit les identités et permissions de référence |
| Exploitation | Collecte la télémétrie et gère les incidents |
| Architecte | Compare les options et formalise la décision |

## Fonctions vérifiables

| ID | Besoin | Condition d'acceptation à mettre en œuvre |
|---|---|---|
| F01 | Contrôler l'identité | Une identité non attestée ne déclenche pas de recherche |
| F02 | Autoriser chaque document | L'API et l'index respectent les permissions de l'utilisateur |
| F03 | Retrouver les procédures | La réponse liste les références réellement consultables |
| F04 | Maîtriser les versions | Le document affiche ID, version et date d'effet |
| F05 | Répondre ou s'abstenir | Une question sans source ne provoque pas de fausse affirmation |
| F06 | Signaler l'erreur | Une correction peut être demandée et tracée |
| F07 | Séparer lecture et écriture | Aucun outil de mutation de production n'est disponible |
| F08 | Prévoir une dégradation sûre | La panne du générateur n'accorde aucun droit additionnel |

## Qualités non fonctionnelles — valeurs ouvertes

| ID | Qualité | Méthode de définition | Statut |
|---|---|---|---|
| NFR01 | Latence | P95 des requêtes à une charge représentative ; périmètre réseau déclaré | **TBD** |
| NFR02 | Disponibilité | Période de service, taux cible et incidents exclus | **TBD** |
| NFR03 | Sécurité | Zéro exposition d'une source non autorisée dans les tests négatifs | À implémenter |
| NFR04 | Traçabilité | Corrélation, source/version, sans secret dans les journaux | À définir |
| NFR05 | RPO/RTO | Définition selon criticité, stockage et mode dégradé | **TBD** |
| NFR06 | Coût total | Charge, horizon, hébergement et licences datés | **TBD** |
| NFR07 | GreenOps | Périmètre énergie et qualité par résultat validé | **TBD** |
| NFR08 | Réversibilité | Corpus, index et contrats indépendants du générateur | À démontrer |

**TBD** signifie que les valeurs ne sont pas décidées. Nous ne fixons pas de SLO ou prix arbitraires pour remplir un tableau.

## Données et frontières

Les sources comprennent des documents classifiés et des statuts de tickets. Toute donnée doit avoir un propriétaire et un statut de confidentialité.

La source d'autorité pour les permissions est le système IAM et la politique appliquée côté API ; celle des tickets est le SI métier ; celle des procédures est le référentiel documentaire. Une génération LLM ne crée ni état métier ni permission.

## Exclusions fortes

- Aucun transfert bancaire ou action financière.
- Aucune mutation de serveur ou cluster depuis l'assistant.
- Aucune diffusion de contenu tiers ou privé sans droits.
- Aucune publication du contenu d'incident réel.
- Aucun remplacement automatique du jugement humain pour une décision sensible.

## Définition de « prêt pour une revue de conception »

Les besoins métier et les risques sont revus, les NFR chiffrés sont validés par les acteurs, les sources d'autorité sont identifiées, un protocole de test existe, les options sont comparées et le décideur comprend les limites. Ce dossier pédagogique n'a pas encore passé ce gate.
