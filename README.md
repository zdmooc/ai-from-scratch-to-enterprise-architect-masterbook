# AI From Scratch to Enterprise Architect — Masterbook

**Bible de l'intelligence artificielle · collection de 24 volumes · éditions évolutives 2026–2030 et au-delà**

Ce dépôt est la **source éditoriale canonique** de la collection. Il organise un parcours complet de zéro (mathématiques, Python, données, ML) à l'architecture IA d'entreprise (LLM, RAG, agents, OpenShift AI, sécurité, gouvernance, FinOps et Green AI).

## État actuel
**RÉDACTION EN COURS — aucun volume achevé ou publié.**

- 6 parties, 24 volumes
- objectif éditorial indicatif : **9 530 pages A4 cumulées**, sans obligation de pagination artificielle
- ouvrages autonomes, exemples et exercices originaux, laboratoires reproductibles
- publication cible : site HTML, PDF et EPUB **par volume**, avec versions indépendantes
- aucune importation automatique des documents Google Drive, aucune suppression des sources

## Commencer
- [Rapport d'audit I02](sources/audits/I02_2026-10-10.md)
- [Inventaires structurés Drive et GitHub](sources/inventories/README.md)
- [Sommaire des 24 volumes](MASTER_TOC.md)
- [288 chapitres planifiés](catalog/chapters.json)
- [Six brouillons du volume 01](volumes/01-ai-foundations/chapters/)
- [Deux brouillons du volume 02 (mathématiques)](volumes/02-mathematics/chapters/)
- [Deux brouillons du volume 03 (Python)](volumes/03-python/chapters/)
- [LAB V01 — moteur de règles](labs/v01-symbolic-ai/README.md)
- [LAB V02 — vecteurs](labs/v02-vectors/README.md)
- [LAB V03 — Python](labs/v03-python-basics/README.md)
- [Consolidation des 56 sources historiques](sources/consolidation/README.md)
- [Tests locaux V02/V03 : 17/17](evidence/V02_V03_LOCAL_LAB_TEST_2026-10-10.md)
- [Charte et cible éditoriale](MASTER_PLAN.md)
- [Roadmap](ROADMAP.md)
- [Sources Google Drive](sources/GOOGLE_DRIVE_INVENTORY.md)
- [Dépôts internes de référence](sources/INTERNAL_GITHUB_SOURCES.md)
- [Sources publiques comparables](sources/PUBLIC_GITHUB_REFERENCES.md)
- [Règles de vérité, de preuve et de publication](governance/EDITORIAL_GOVERNANCE.md)

## Répartition des responsabilités

| Espace | Propriétaire des faits et livrables |
| --- | --- |
| **Ce Masterbook** | manuscrits originaux, figures, sommaires, exercices, metadata, publication |
| Google Drive / `architecteAI` | originaux DOCX/PDF et références visuelles, **conservés** |
| `maya-ai-agentic-architecture-reference` | architecture IA, principes, ADR et référentiel de connaissance |
| `TradeOps-GenAI-Integration` | runtime RAG/agents/MCP/CRC et preuves d'exécution |
| Autres dépôts spécialisés | plateformes et applications, données synthétiques, Green AI, sécurité, banque/assurance |
| `cadrage_202682030` | gouvernance transverse et décisions de programme |

Les dépôts techniques ne sont **ni fusionnés ni supprimés**. Leurs concepts sont expliqués de manière autonome dans les livres; le code complexe et les preuves sont cités avec leurs limitations.

## Qualité et droits
Ne jamais assimiler `DESIGNED`, `CI_VERIFIED` et `RUNTIME_PROVEN`. Tout chapitre et toute référence doivent indiquer la provenance, la date de validité et les limites des essais. Aucun document privé, donnée de santé, secret, contenu confidentiel ou texte/figure tiers non autorisé dans ce dépôt privé sans validation des droits ou autorisation éditoriale.

**Statut :** dépôt **PRIVATE** confirmé le 10/10/2026 ; I01 structure validée, CI réussie avant passage privé ; nouvelles exécutions CI en échec avant démarrage des étapes (diagnostic en cours) ; build réel PDF/EPUB non exécuté ; I02 inventaire des arborescences terminé (77 fichiers Drive, 79 dépôts GitHub), audit de fond encore ouvert ; I04 288 titres de chapitres en brouillon ; I03 56 unités Drive cartographiées ; I04 10 chapitres en brouillon sur 288 ; I05 17 tests V02/V03 reproduits localement avec contrôle SHA ; aucun volume publié. Aucun des 24 volumes n'est terminé.

## Suivi de réalisation V01
- [Itérations R01–R22 et gates](volumes/01-ai-foundations/ITERATION_TRACKER.md) : R01–R06, rédaction en brouillon ; R07–R22 à réaliser. Aucun PDF/EPUB généré.
