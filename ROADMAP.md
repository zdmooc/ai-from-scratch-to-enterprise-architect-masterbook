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
- I01 : **STRUCTURE_VALIDATED / CI_PRE_PRIVATE_PASS / PRIVATE_RUNNER_BLOCKED_UNDIAGNOSED / QUARTO_RENDER_NOT_PROVEN** ; 24 volumes planifiés. La CI a réussi sur le dernier commit public `65069e1`. Depuis le passage privé, les exécutions se terminent en échec sans aucune étape exécutée ni runner affecté ; raison précise à vérifier dans Actions et facturation/limites GitHub. Ne pas attribuer ces échecs au code sans logs.
- I02 : **TREE_INVENTORY_COMPLETE / CONTENT_REVIEW_OPEN** ; visibilité PRIVATE confirmée, 77 fichiers Drive et 79 dépôts GitHub inventoriés ; **79/79 arbres examinés**, aucune ligne de code ou équation de l'ensemble des sources certifiée. Voir `sources/audits/I02_GITHUB_COVERAGE_MATRIX_2026-10-10.md`. Droits, doublons, conversions et qualification technique restent à traiter.
- I03 : **SOURCE_MAPPING_COMPLETE / CONVERSION_NOT_STARTED** ; 56 unités historiques cartographiées vers les 24 volumes (61 fichiers T1-T5). Aucun original Drive importé ni modifié.
- I04 : **FIRST_PASS_TOC_DRAFT / STATUS_SYNCED** ; 288 chapitres dont 9 en brouillon et 279 à écrire. Sommaires et catalogue synchronisés.
- I05 : **V01_V02_V03_DRAFT_IN_PROGRESS / LOCAL_LAB_TESTS_PASS / PUBLICATION_NOT_PROVEN** ; 9 chapitres : V01=5, V02=2, V03=2. Tests V02/V03 : 17/17 PASS sous Python 3.13.5, fichiers strictement identiques aux blobs GitHub. Build PDF/EPUB non vérifié ; GitHub Actions privées encore bloquées avant runner.
- I06 : **NOT_STARTED** ; aucun des 24 volumes achevé, aucune publication.

## Première livraison utile
V01 : définition IA, modèles de calcul, IA symbolique vs apprentissage, premières expériences reproductibles, exercices corrigés, classification des systèmes IA selon risques et exigences.

## Maintenance
- Corrections et liens : au fil de l'eau.
- Mise à jour des technologies IA, frameworks, GPU, cloud, coûts : revue trimestrielle, sans affirmation d'automatisation déjà en place.
- Revue des architectures/laboratoires : semestrielle.
- Éditions majeures : au besoin, cible annuelle.
- EU AI Act et autres lois : vérification source primaire à la date de publication.
