# I03 — Pré-consolidation des manuscrits Drive (sans importation des originaux)

**Statut : FIRST_PASS_MAPPING / NO_SOURCE_CONTENT_COPY / RIGHTS_REVIEW_PENDING**  
**Origine :** dossier privé Google Drive `architecteAI/T1–T5`, inventorié au 10 octobre 2026.

## Résultats mesurables

- **61 fichiers physiques** répartis en 5 tomes Drive, représentant **56 unités de contenu** : 42 chapitres et 14 labs.
- **10 + 10 + 10 + 12 chapitres** dans T1 à T4 ; **14 labs** dans T5 (LAB01, LAB02, LAB04–LAB15).
- **LAB03 non trouvé** dans le dossier étudié.
- **Trois copies de labs** (T5-LAB02, LAB05, LAB15) et **une copie T3-C07** identiques à l'extraction de texte ; identité binaire/figures non vérifiée.
- **T4-C02 a deux versions différentes (DOCX et Markdown)**. Les deux doivent être examinées pour préserver les ajouts avant rédaction originale du volume V11.
- [Inventaire structuré par unité de source](historical_manuscript_mapping_2026-10-10.json), avec IDs Drive, volumes suggérés, duplications, droits et statut.

## Répartition thématique principale

| Anciens tomes | Destination nouvelle principale | Action |
|---|---|---|
| T1 — Fondements pour architecte | V01, V05–06, V09–11, V13, V16, V21 | Reprendre les concepts ; approfondir pédagogie depuis zéro, maths et exemples |
| T2 — Infrastructure physique et GPU | V15–16, V20, V22 | Revalider les versions et les dimensions; intégrer calculs et labs |
| T3 — OpenShift AI et MLOps | V13–16, V18–19, V22 | Revalider compatibilité RHOAI/OpenShift, types CRD, opérateurs et APIs |
| T4 — GenAI, RAG, agents, enterprise AI | V09, V11–22, V24 | Fusion critique des variantes, sécurité, sources primaires et coûts |
| T5 — Labs | V10–16, V18–20, V22–23 | Transformer en labs reproductibles avec prérequis, rollback et preuves réelles |

## Garde-fous avant toute conversion
1. Distinguer texte original de l'auteur, figures, tableaux ou citations provenant d'un tiers, et éléments éventuellement confidentiels.
2. Convertir **dans une branche dédiée de travail** après validation : extraction de textes, équations, tableaux, images, références et index ; ne pas modifier les fichiers Drive.
3. Établir un rapport de comparaison par fichier (nombre de sections, nombre de figures, liens, math, blocs de code, manques et corrections).
4. Ne pas publier des extraits de sources dont les droits restent indéterminés ; le statut privé GitHub n'est pas une licence de reproduction.
5. Écrire une nouvelle version pédagogique autonome dans le volume cible ; préserver le lien source/chapitre.
6. Aucune destruction, déduplication automatique ou remplacement des originaux.

## Qualification par priorité

| Priorité | Source | Raison | V cible |
|---|---|---|---|
| P0 | T1-C03/C04 | Glossaire ML/DL déjà rédigé mais orienté architecte ; refaire niveau débutant et démonstrations | V05/V06 |
| P0 | T1-C01 | Métier et responsabilités ; réutilisation conceptuelle dans cas d'introduction et dossier architecte | V01/V21 |
| P0 | T4-C02 DOCX + MD | Versions divergentes à fusionner intellectuellement, sans suppression | V11 |
| P0 | T5-LAB01/02/04/05 | Chaîne locale, Kubernetes, OpenShift, OpenShift AI ; labs qui exigent des preuves différentes selon la plateforme | V14/V16 |
| P1 | T2 complet et T3 complet | Infrastructure GPU / RHOAI, métier principal de plateforme IA | V16 |
| P1 | T4-C04/C05/C06/C11 | Sécurité, agents, évaluation et GreenOps | V12–14/V18–20 |

## Limites de cette itération

Le **mapping** est complet pour les 56 unités identifiées mais **aucun document DOCX/PDF n'a été converti** à ce stade. Les 24 volumes restent des manuscrits en rédaction et ne doivent pas être déclarés achevés.
