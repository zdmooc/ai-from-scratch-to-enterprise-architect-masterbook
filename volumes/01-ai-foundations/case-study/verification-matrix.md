# Vérifications et registre initial des risques — Case Study V01

**Tous les tests intégrés sont NOT_EXECUTED.** Ils constituent la spécification d'un futur POC et ne doivent pas être confondus avec les tests unitaires des labs Python de la collection.

## Matrice de tests

| ID | Scénario | Résultat attendu | Catégorie | Preuve |
|---|---|---|---|---|
| T01 | Utilisateur habilité, procédure courante | Source exacte et version vérifiée | Fonctionnel | NOT_EXECUTED |
| T02 | Question sans source | Abstention / clarification | Qualité | NOT_EXECUTED |
| T03 | Demandeur sans droit à un document | Aucune divulgation de contenu ou métadonnée protégée | Sécurité | NOT_EXECUTED |
| T04 | Document retiré mais présent en index | Résultat retiré ou bloqué | Données | NOT_EXECUTED |
| T05 | Deux procédures contradictoires | Conflit signalé et priorité explicite ou abstention | Gouvernance | NOT_EXECUTED |
| T06 | Instruction hostile dans un document | Aucune opération non autorisée | Injection | NOT_EXECUTED |
| T07 | LLM non disponible | Recherche seule si autorisée, sinon dégradation sûre | Résilience | NOT_EXECUTED |
| T08 | Appel d'outil de mutation demandé | Refus imposé par API et compte technique | Sécurité | NOT_EXECUTED |
| T09 | Citation fictive générée | Citation rejetée | Traçabilité | NOT_EXECUTED |
| T10 | Charge cible validée | P95 dans la limite décidée | Performance | TBD_NFR |
| T11 | Requête répétée | Aucune action indue ni effet de bord | Fiabilité | NOT_EXECUTED |
| T12 | Publication d'une nouvelle version de procédure | Source et index cohérents | Maintenabilité | NOT_EXECUTED |

## Registre initial

| Risque | Effet | Contrôle proposé | Statut |
|---|---|---|---|
| RISK01 — divulgation | Violation confidentialité | ACL côté API et index, tests inter-rôle | DESIGN_ONLY |
| RISK02 — procédure périmée | Réponse incorrecte | IDs, dates d'effet, retrait et synchronisation | DESIGN_ONLY |
| RISK03 — citation fictive | Mauvaise confiance dans le service | Validation de références par l'application | DESIGN_ONLY |
| RISK04 — injection dans document | Contournement d'outil ou politique | Données de moindre confiance, permissions minimales | DESIGN_ONLY |
| RISK05 — dépendance modèle | Indisponibilité | Dégradation vers recherche simple | DESIGN_ONLY |
| RISK06 — journaux sensibles | Exposition d'informations | Minimisation, masquage, rétention | DESIGN_ONLY |
| RISK07 — coût imprévu | Dépassement budget | Limite de charge, budget et suivi | DESIGN_ONLY |

## Leçon sur les preuves

Les laboratoires du Volume 01 montrent comment calculer une MAE et comment refuser un outil dans **une simulation Python locale**. Ils ne prouvent **aucun** des contrôles T01–T12 sur l'architecture complète.

Un futur dossier de validation devra associer pour chaque test : cas, entrées, environnement, outil, version, résultat observé, logs adaptés et verdict. Les contrôles réglementaires demanderaient une analyse séparée.
