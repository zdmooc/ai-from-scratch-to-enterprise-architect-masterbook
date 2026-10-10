# V01 — Matrice de couverture des laboratoires (R14)

**Révision du 10/10/2026 — R14_PARTIAL.** Les laboratoires utilisent des données synthétiques et la bibliothèque standard Python. Un laboratoire local ne prouve ni la maîtrise complète d'un chapitre ni la sécurité d'une solution réelle.

| Chapitre | Compétence observable | Ressource pratique | Preuve | Lacune ouverte |
|---|---|---|---|---|
| C01 — Fondements | Choisir des familles d'IA selon des besoins | Atelier de choix dans le chapitre | DESIGN_ONLY | Étude de cas corrigée indépendante |
| C02 — Histoire | Vérifier une source primaire et distinguer jalons | Exercice critique dans le chapitre | DRAFT_ONLY | Bibliographie vérifiée |
| C03 — Règles | Chaînage avant et contrôle de déduction | [LAB moteur de règles](../../labs/v01-symbolic-ai/README.md) | Tests locaux antérieurs, CI non prouvée | Revalidation HEAD, diagramme |
| C04 — ML | Expliquer MSE, MAE, test séparé | [LAB prévision C11](../../labs/v01-experiment/README.md) | 12/12 tests locaux PASS | Cas de classification et matrice d'erreurs |
| C05 — DL | Gradient analytique vs approximation numérique | [LAB gradient](../../labs/v01-gradient-descent/README.md) | **17/17 locaux PASS, SHA vérifiés** | Différentiation multicouche (V06) |
| C06 — Transformers | Calcul Q/K/V, softmax, masquage | [LAB attention](../../labs/v01-attention-qkv/README.md) | **20/20 locaux PASS, SHA vérifiés** | Figures et revue scientifique |
| C07 — Génération | Évaluer fidélité multimodale, droits et contenu | Atelier d'analyse du chapitre | DESIGN_ONLY | Corpus et barème de notation |
| C08 — Agents | Refuser outils non autorisés | [LAB read-only agent](../../labs/v01-agent-guardrails/README.md) | 16/16 tests locaux PASS | Tests API réelle et injection approfondie |
| C09 — Choix | Comparer baseline, options et critères éliminatoires | [ADR du mini-projet](case-study/ADR-001-search-before-rag.md) | DESIGN_ONLY | Notation simulée et corrigée |
| C10 — Risques | Relier risques, contrôles et tests | [Matrice du mini-projet](case-study/verification-matrix.md) | NOT_EXECUTED | Analyse juridique et revue des contrôles |
| C11 — POC | Évaluation chronologique sur série synthétique | [LAB expérimentation](../../labs/v01-experiment/README.md) | 12/12 tests locaux PASS | Incertitude et extrapolation |
| C12 — Projet | Produire exigences, ADR et plan de validation | [Dossier d'architecture](case-study/README.md) | DESIGN_ONLY ; 12 scénarios NOT_EXECUTED | Soutenance et contrôles d'intégration |

## Contrôle de progression

**Nouveaux tests vérifiés durant cette passe R14 : 37/37.** Ils s'ajoutent aux tests locaux antérieurs sans entraîner une preuve de CI sur le HEAD courant.

Les laboratoires ne sont pas tous indépendants : celui de prévision est partagé entre C04 et C11. Les études de cas et exercices de C01/C02/C07/C09/C10/C12 sont des travaux sur papier, non des scripts à forcer artificiellement sur CPU.

## Critères de clôture de R14

- [x] LAB gradient avec tests et corrections
- [x] LAB Q/K/V avec tests et corrections
- [x] Empreintes SHA des fichiers exécutés comparées avec GitHub
- [x] Matrice de couverture C01–C12
- [ ] Vérifier en CI les laboratoires sur un runner accessible
- [ ] Rejouer la suite complète après intégration, avec logs et SHA
- [ ] Vérifier les sorties d'exercices sur tous les chapitres
- [ ] Évaluer les travaux manuels sur une grille homogène
- [ ] Valider indépendamment équations et assertions scientifiques (R18)

**Décision : R14_PARTIAL, R15–R21 encore ouverts, aucune publication.**
