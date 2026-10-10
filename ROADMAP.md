# Roadmap de réalisation — Bible IA

**Point de départ : 2026-10-10.** Ce document sépare **l'infrastructure éditoriale** de l'écriture réelle des ~9 530 pages.

| Itération initiale | Objectif | Gate |
|---|---|---|
| I01 — Initialisation | Dépôt maître, registre 24 volumes, charte, source inventories, publication preview | Structure/CI vérifiées |
| I02 — Inventaire exhaustif | Drive T1–T5/Ai_OneAgent + 79 dépôts accessibles au 10/10, sélection des sources utiles | Traçabilité fichier par fichier |
| I03 — Conversion/ingestion | Convertir les DOCX autorisés en Markdown, conserver code/figures/math, analyser doublons | Comparaison avec originaux ; **aucune suppression** |
| I04 — Table des matières détaillée | Établir un chapitre-by-chapitre par volume et traiter les gaps du niveau débutant | Revue complète des prérequis |
| I05 — Prototype de publication | Finir un **vrai chapitre de V01** et une maquette de volume, tests, PDF/EPUB | QA technique et pédagogique |
| I06 — Programme long de rédaction | Rédaction progressive des 24 volumes ; revues, lab tests et éditions indépendantes | Gate individuel par volume |

**Ne pas assimiler les 6 étapes de démarrage aux 24 volumes achevés.** La rédaction complète est un programme long qui doit être suivi séparément volume par volume.

## État
- I01 : **STRUCTURE_CI_PASS / QUARTO_RENDER_NOT_YET_PROVEN** ; 24 volumes planifiés et CI statique PASS, mais aucun PDF/EPUB validé.
- I02 : **IN_PROGRESS** ; dépôt confirmé PRIVATE le 2026-10-10. Rapport archivé dans `sources/audits/`; inventaires structurés : 77 fichiers Drive (61 tomes, 14 Ai_OneAgent, 2 racine), 79 dépôts GitHub ; 34 arborescences examinées / 45 non examinées ; qualification technique, droits et conversions restant à faire.
- I03–I06 : **NOT_STARTED** ; les sources ne sont pas importées automatiquement et aucun volume n'est achevé.

## Première livraison utile
V01 : définition IA, modèles de calcul, IA symbolique vs apprentissage, premières expériences reproductibles, exercices corrigés, classification des systèmes IA selon risques et exigences.

## Maintenance
- Corrections et liens : au fil de l'eau.
- Mise à jour des technologies IA, frameworks, GPU, cloud, coûts : revue trimestrielle, sans affirmation d'automatisation déjà en place.
- Revue des architectures/laboratoires : semestrielle.
- Éditions majeures : au besoin, cible annuelle.
- EU AI Act et autres lois : vérification source primaire à la date de publication.
