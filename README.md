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
- [Douze chapitres en brouillon du volume 01](volumes/01-ai-foundations/chapters/)
- [Deux brouillons du volume 02 (mathématiques)](volumes/02-mathematics/chapters/)
- [Deux brouillons du volume 03 (Python)](volumes/03-python/chapters/)
- [LAB V01 — moteur de règles](labs/v01-symbolic-ai/README.md)
- [LAB V01 — expérimentation mesurable](labs/v01-experiment/README.md)
- [LAB V01 — agent à outils lecture seule](labs/v01-agent-guardrails/README.md)
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
Ne jamais assimiler `DESIGNED`, `CI_VERIFIED` et `RUNTIME_PROVEN`. Tout chapitre et toute référence doivent indiquer la provenance, la date de validité et les limites des essais. Aucun document privé, donnée de santé, secret, contenu confidentiel ou texte/figure tiers non autorisé dans ce dépôt public sans validation des droits ou autorisation éditoriale.

**Statut au 11/10/2026 :** dépôt **PUBLIC** confirmé sur GitHub ; structure éditoriale et tests des laboratoires réussis dans GitHub Actions ([run 38118052494](https://github.com/zdmooc/ai-from-scratch-to-enterprise-architect-masterbook/actions/runs/38118052494)), incluant gradient, Q/K/V et validation statique des six sources SVG. 24 volumes planifiés, dont 16 chapitres en brouillon (V01=12, V02=2, V03=2) ; **aucun volume achevé ni publié, aucun rendu PDF/EPUB produit**. Voir [état CI du 11 octobre](governance/CI_STATUS_2026-10-11.md).

## Suivi de réalisation V01
- [Itérations R01–R22 et gates](volumes/01-ai-foundations/ITERATION_TRACKER.md) : R01–R12, rédaction en brouillon ; R13–R22 encore ouverts. Aucun PDF/EPUB généré.

**Qualité V01 :** les douze chapitres sont au stade DRAFT, R13 audit initial en cours et R14 labs partiellement testés (C11 : 12 tests, C08 : 16 tests, tous locaux). Voir [registre R13](volumes/01-ai-foundations/R13_GAP_REGISTER.md) et [preuve C08](evidence/V01_AGENT_GUARDRAILS_LOCAL_TEST_2026-10-10.md).

- [Dossier de référence du mini-projet V01 (HLD, ADR, tests non exécutés)](volumes/01-ai-foundations/case-study/README.md)
- [Schémas vectoriels originaux V01](diagrams/v01/README.md)

### Harmonisation V01 — R13
- [Glossaire V01 — 69 termes](volumes/01-ai-foundations/GLOSSARY.md)
- [Carte des prérequis et frontières de chapitres](volumes/01-ai-foundations/READING_MAP.md)
- [Rapport R13 avec résultats et lacunes](volumes/01-ai-foundations/R13_REVIEW_REPORT_2026-10-10.md)
- [Guide de rédaction réutilisable pour les 24 volumes](governance/AI_PEDAGOGICAL_STYLE_GUIDE.md)

### R14 — Laboratoires Python complémentaires (Volume 01)

- [Gradient et vérification numérique des dérivées](labs/v01-gradient-descent/README.md) : 17 tests locaux.
- [Attention Q/K/V et masques](labs/v01-attention-qkv/README.md) : 20 tests locaux.
- [Preuve des 37 tests locaux avec empreintes Git](evidence/V01_R14_GRADIENT_ATTENTION_2026-10-10.md).

**R14 n'est pas clos.** Les laboratoires C05 et C06 passent maintenant également en GitHub Actions ; il reste à homogénéiser les exercices et les contrôles pédagogiques. La publication PDF/EPUB attend la finition du manuscrit.

**R15 — 11/10/2026 :** six schémas SVG originaux pour V01, dont nouveaux diagrammes [neurone/gradient, QKV, RAG](diagrams/v01/README.md), reliés aux chapitres C05, C06 et C12. Rendu visuel et composition restent à valider.

**Attention — exposition publique :** les inventaires historiques du dépôt contiennent des métadonnées de fichiers et références Drive créées avant le passage en public. Il faut confirmer leur périmètre de diffusion et, si besoin, traiter l'historique Git avant une édition définitive. Cette mise à jour n'efface pas les anciennes révisions.
