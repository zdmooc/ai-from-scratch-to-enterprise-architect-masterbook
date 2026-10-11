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
- I01 : **STRUCTURE_VALIDATED / PUBLIC_CI_PASS_2026_10_11 / QUARTO_RENDER_NOT_PROVEN** ; 24 volumes planifiés. La CI a repris sur runner GitHub après le passage en public le 11/10/2026 ; run `38118052494` SUCCESS avec laboratoires et contrôle SVG. Les échecs d'avant réouverture sont conservés comme historique ; leur cause exacte n'a pas été établie.
- I02 : **TREE_INVENTORY_COMPLETE / CONTENT_REVIEW_OPEN** ; visibilité PRIVATE confirmée, 77 fichiers Drive et 79 dépôts GitHub inventoriés ; **79/79 arbres examinés**, aucune ligne de code ou équation de l'ensemble des sources certifiée. Voir `sources/audits/I02_GITHUB_COVERAGE_MATRIX_2026-10-10.md`. Droits, doublons, conversions et qualification technique restent à traiter.
- I03 : **SOURCE_MAPPING_COMPLETE / CONVERSION_NOT_STARTED** ; 56 unités historiques cartographiées vers les 24 volumes (61 fichiers T1-T5). Aucun original Drive importé ni modifié.
- I04 : **FIRST_PASS_TOC_DRAFT / STATUS_SYNCED** ; 288 chapitres dont 16 en brouillon et 272 à écrire. Sommaires et catalogue synchronisés.
- I05 : **V01_V02_V03_DRAFT_IN_PROGRESS / LOCAL_LAB_TESTS_PASS / PUBLICATION_NOT_PROVEN** ; 16 chapitres : V01=12, V02=2, V03=2. Tests V02/V03 : 17/17 PASS sous Python 3.13.5, fichiers strictement identiques aux blobs GitHub. Build PDF/EPUB non réalisé par décision éditoriale ; GitHub Actions publiques maintenant validées.
- I06 : **NOT_STARTED** ; aucun des 24 volumes achevé, aucune publication.

## Première livraison utile
V01 : définition IA, modèles de calcul, IA symbolique vs apprentissage, premières expériences reproductibles, exercices corrigés, classification des systèmes IA selon risques et exigences.

## Maintenance
- Corrections et liens : au fil de l'eau.
- Mise à jour des technologies IA, frameworks, GPU, cloud, coûts : revue trimestrielle, sans affirmation d'automatisation déjà en place.
- Revue des architectures/laboratoires : semestrielle.
- Éditions majeures : au besoin, cible annuelle.
- EU AI Act et autres lois : vérification source primaire à la date de publication.

## Focus Volume 01 — séquence de 22 itérations
Voir [le tableau V01](volumes/01-ai-foundations/ITERATION_TRACKER.md). **R01–R12 : rédaction/approfondissement effectués**, mais chapitres non validés scientifiquement ni publiés. **R13–R22 : non réalisés**. Les PDF/EPUB ne seront produits qu'après clôture éditoriale du contenu, avec contrôle final des droits.

**Jalon R12 (10/10/2026) :** les 12 chapitres V01 existent désormais en premier brouillon, sans prétention à 280 pages déjà produites. Le laboratoire d'évaluation C11 a été reproduit localement : 12/12 tests PASS avec empreintes GitHub identiques ; voir `evidence/V01_EXPERIMENT_LOCAL_TEST_2026-10-10.md`. Les étapes d'harmonisation, figures, sciences, droits, QA et composition restent à réaliser.

**Avancement R13–R14 :** audit initial des lacunes enregistré, à approfondir ; simulateur pédagogique d'agent lecture seule C08 validé localement avec 16 tests PASS (blobs GitHub SHA identiques), laboratoire C11 avec 12 tests PASS. **R13 non clos, R14 partiel**. Aucun PDF, EPUB ou HTML de publication, aucun coût GPU/cloud engagé.

**R15–R16 partiels (10/10/2026) :** trois schémas SVG originaux et modifiables sont insérés dans C08/C09/C11, sans validation visuelle Quarto ; le mini-projet V01 possède un dossier de référence (exigences, ADR, matrice), avec 12 tests d'intégration **NOT_EXECUTED**. Aucun volume ni rendu PDF/EPUB n'est finalisé.

**R13 — revue de cohérence du 10/10/2026 :** première passe statique réussie sur 12 brouillons V01 (~32 101 mots, 38 liens relatifs contrôlés, 69 termes de glossaire, six ateliers ajoutés). L'approfondissement vers la qualité d'un livre complet reste ouvert ; ne pas assimiler ce PASS à une validation scientifique ou à la cible de 280 pages. Voir `volumes/01-ai-foundations/R13_REVIEW_REPORT_2026-10-10.md`.


**R14 — progrès du 10/10/2026.** Les laboratoires C05 (dérivées et gradient) et C06 (attention Q/K/V) ont été créés avec leurs guides et 37 tests locaux PASS (17 + 20). Les quatre SHA des fichiers testés correspondent aux blobs GitHub ; voir `evidence/V01_R14_GRADIENT_ATTENTION_2026-10-10.md`. Le Volume 01 reste en DRAFT. **CI GitHub et tests d'intégration non prouvés ; R14 PARTIAL.** Aucun PDF/EPUB généré.

**R14/R15 — 11/10/2026 :** validation publique [run 38118052494](https://github.com/zdmooc/ai-from-scratch-to-enterprise-architect-masterbook/actions/runs/38118052494) SUCCESS : tests V01/V02/V03, gradients, attention Q/K/V, contrôle syntaxique/accessibilité de six SVG. Trois nouvelles figures intégrées à C05/C06/C12. **R14 partiel (couverture pédagogique) ; R15 partiel (rendu visuel non contrôlé)**. Aucun PDF/EPUB/HTML de publication produit. Voir `governance/CI_STATUS_2026-10-11.md`.
