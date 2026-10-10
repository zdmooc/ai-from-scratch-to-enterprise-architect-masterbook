# Volume 01 — Suivi des 22 itérations de réalisation

**Date de dernière mise à jour : 10 octobre 2026.** Dépôt GitHub **privé**. Cible de pagination **280 pages A4 indicative** ; aucune mesure réelle de pagination tant que le volume n'est pas composé. Le terme **RÉDACTION EFFECTUÉE** ne signifie ni `REVIEWED`, ni `VERIFIED`, ni `RELEASED`.

| Itération | Livrable principal | Statut au 10/10/2026 | Gate encore ouvert |
|---|---|---|---|
| R01 | C01 — Définition et frontières de l'IA | DRAFT_EXPANDED | Relecture scientifique, figures, bibliographie |
| R02 | C02 — Histoire et paradigmes | DRAFT_EXPANDED | Références historiques, figures originales, relecture |
| R03 | C03 — IA symbolique et règles | DRAFT_EXPANDED | Laboratoire revérifié sur le HEAD, cas limites, relecture |
| R04 | C04 — Apprentissage statistique | DRAFT_EXPANDED | Vérification formules/métriques et exemples |
| R05 | C05 — Introduction au Deep Learning | DRAFT_EXPANDED | Calculs, figures et expérimentation pédagogique |
| R06 | C06 — NLP, Transformers et LLM | DRAFT_AUTHORED | Vérification calcul d'attention, figure et bibliographie |
| R07 | C07 — IA générative texte, image, audio | DRAFT_AUTHORED | Manuscrit, exercices et sources |
| R08 | C08 — Agents IA et outils | DRAFT_AUTHORED | Manuscrit, architecture, tests négatifs |
| R09 | C09 — Choisir un cas d'usage ou alternative sans IA | DRAFT_AUTHORED | Manuscrit, grille de décision |
| R10 | C10 — Éthique, biais, erreurs et risques | DRAFT_AUTHORED | Manuscrit, sources primaires et cas |
| R11 | C11 — Première expérience mesurable | DRAFT_AUTHORED | Chapitre, dataset synthétique, protocole |
| R12 | C12 — Synthèse, exercices, mini-projet | DRAFT_AUTHORED | Manuscrit, corrections, critères PASS/FAIL |
| R13 | Consolidation de cohérence et densification C01–C12 | NOT_STARTED | Aucun prérequis manquant, aucune contradiction |
| R14 | Laboratoires reproductibles et jeux synthétiques | NOT_STARTED | Tests exécutés, aucun matériel lourd imposé |
| R15 | Schémas et illustrations originaux | NOT_STARTED | Lisibilité, licence, version, source |
| R16 | Études de cas métier et dossiers d'architecture | NOT_STARTED | Métier vs technique, ADR, options |
| R17 | Évaluations et corrigés de tous les chapitres | NOT_STARTED | Couverture des compétences mesurable |
| R18 | Relecture scientifique et vérification des formules | NOT_STARTED | Revue indépendante ou traçable |
| R19 | Bibliographie et propriété intellectuelle | NOT_STARTED | Références primaires, attribution et droits |
| R20 | Relecture intégrale, harmonisation, accessibilité | NOT_STARTED | Terminologie, glossaire, navigation |
| R21 | Gate final et gel du manuscrit | NOT_STARTED | Critères de validation éditoriale |
| R22 | Composition PDF/EPUB/HTML et release V01 | NOT_STARTED | Lancer **uniquement après** validation contenu, droits, tests et relecture |

## Bilan des premières opérations

- **12 brouillons V01 présents** sur 12 chapitres planifiés, sans relecture finale.
- C01–C05 ont été approfondis ; C06–C12 ont été rédigés depuis zéro. C11 comprend un laboratoire synthétique testé localement (12/12 PASS), mais pas en CI GitHub.
- Les nouveaux textes sont des **manuscrits originaux** ; le contenu Drive antérieur reste archivé à sa place.
- Aucun PDF, EPUB, HTML de publication ou calcul de pages n'a été généré au cours de R01–R12.
- Les laboratoires ont des contrôles locaux tracés ; le nouveau lab de C11 a 12 tests PASS avec correspondance de SHAs Git. Une validation intégrée sur GitHub Actions reste bloquée avant runner. Le problème GitHub Actions privé n'est pas résolu.
- **R13–R22 restent ouverts**. Les 22 itérations sont un plan de travail, pas une promesse que les tâches sont de taille égale ni que les chapitres en brouillon sont achevés.

## Conditions de publication

Un volume n'est déclarable `RELEASED` que lorsque ses 12 chapitres sont rédigés et relus, les références et droits sont vérifiés, les laboratoires testés, les figures sont originales, la composition Quarto est contrôlée et la décision de publication est explicitement prise.

## Liens

- [Plan C01–C12](CHAPTER_PLAN.md)
- [Brouillons C01–C06](chapters/)
- [Laboratoire V01](../../labs/v01-symbolic-ai/README.md)
- [Cadre de gouvernance](../../governance/EDITORIAL_GOVERNANCE.md)
