# I02 — Répartition thématique de la bibliothèque GitHub
**Date :** 10 octobre 2026. **État :** les arbres des 79 dépôts ont été inspectés. Il ne s'agit **pas** d'une certification des contenus, de leur exactitude, de leurs licences ou de leurs résultats runtime.

## Bibliothèque thématique réutilisable, par priorité
| Domaine / volumes | Dépôts propriétaires | Condition de réutilisation |
|---|---|---|
| Fondements ML/DL V01–08 | T1-C03/04 sur Drive ; ressources publiques Microsoft/D2L/ML Zoomcamp | Rédaction et labs **à créer**, mathématiques et Python de zéro absents du fonds interne |
| LLM/Transformers V09–10 | T1-C05–C09 ; `maya-ai-agentic-architecture-reference` | Révérifier attention, capacités, contexte, licences et versions |
| RAG V11 | `TradeOps-GenAI-Integration`, T4-C02/C03, T5-LAB10 | Comparer variantes DOCX/MD, ACL, reranking, datasets, sécurité |
| Agents V12 | `TradeOps-GenAI-Integration`, `maya-secure-agentic-devsecops-platform`, T4-C05, T5-LAB11/12 | MCP/HITL/evals, ne pas publier PDF tiers Mastering AI Agents |
| Évaluation V13 | TradeOps, RAI BFI, T1-C10, T3-C09, T4-C06 | Matrice claims/proofs, golden set, métriques et coûts |
| MLOps V14 | T3-C05/C07/C08/C10, T5-LAB06/07, `shared-platform-services-openshift` | Scénarios de labs isolés des déploiements runtime |
| Serving V15 | T3-C06, T4-C01/C07, T5-LAB09, `enterprise-ai-infrastructure-reference-architecture` | Performance à quantifier, benchmarks GPU non prouvés |
| GPU/RHOAI V16 | T2 complet, T3, `enterprise-ai-infrastructure-reference-architecture`, `openshift-platform-blueprints`, `k8s-openshift-cluster-factory` | Version RHOAI 3.4 datée août 2026 ; environnements locaux sans GPU dédié |
| Data/Integration V17 | `enterprise-data-lakehouse-kubernetes-openshift`, `mayabank-kafka-ddd-openshift`, `mayabank-api-management-architecture`, `kafka-socle-gouvernance-lab`, `kafka-data-engineer-kafkaops-topic-service-crc` | Source vs copie d'index, event contracts, lineage |
| Sécurité V18 | `maya-secure-agentic-devsecops-platform`, `iam-etat-de-lart-2026`, `keycloak-enterprise-roadmap-v7`, `mayabank-api-management-architecture`, T4-C04, T5-LAB14 | Trust boundary, OIDC, zero trust, prompt-injection |
| Gouvernance V19 | `maya-secure-agentic-devsecops-platform`, `dora-operational-resilience-architecture-masterbook`, `cadrage_202682030` | Sources juridiques primaires, éviter de déclarer une certification |
| FinOps/Green IT V20 | `enterprise-ai-infrastructure-reference-architecture`, `mayabank-carbon-aware-decision-architecture`, `mayabank-multicloud-migration-finops`, T4-C11, T5-LAB15, `digital-sustainability-*` | Empreinte cycle de vie + coût par résultat validé, données datées |
| Méthodes d'architecture V21 | `maya-ai-agentic-architecture-reference`, `hopex-aquila-enterprise-architecture-masterbook`, `togaf-ogea-103-combined-certification-prep`, `archimate-3-2-foundation-practitioner-masterbook`, T1-C01/C10, T4-C12 | 15 livrables d'architecture, originaux et scénarios synthétiques |
| Multicloud/résilience V22 | `mayabank-azure-cloud-ai-platform`, `mayabank-multicloud-migration-finops`, `kubernetes-the-hard-way-multicloud`, `openshift-migration-framework`, `wero-organisme-poc`, T4-C09, T5-LAB13 | PAS de coût cloud ou disponibilité GPU garanti sans mesure |
| Banque/paiements/assurance V23 | `mayabank-ibm-odm-ai-decision-architecture`, `mayabank-instant-payments-resilience-platform`, `mayabank-european-payment-processing-platform`, `payment-hub-iso20022-opf-reference`, `mayabank-pega-ai-case-management-openshift`, `wero-organisme-poc`, `mayabank-low-latency-authorization-engine` | Cas synthétiques ; droits sur documents clients et produits |
| Master Capstone V24 | `maya-ai-agentic-architecture-reference`, `TradeOps-GenAI-Integration`, `maya-freelance-mission-intelligence`, `maya-health-nutrition-intelligence`, `ysteria-ai-autonomous-business-platform`, `Maya` | Cibles produit, non preuves de commercialisation ; données de santé exclues |

## Résultat de la revue du reste des 45 dépôts
Les nouvelles arborescences confirment des sources particulièrement utiles : `keycloak-enterprise-roadmap-v7` (327 fichiers, IAM/OIDC), `kubernetes-the-hard-way-vagrant-architect-v29` (411 fichiers, composants K8s), `openshift-migration-framework` (305 fichiers, réversibilité), `cadrage_202682030` (114 fichiers, programme), `digital-sustainability-*` (3 dépôts, GreenOps, DevSecOps et gouvernance). Ces nombres sont des comptages de fichiers Git et **pas de pages**.

## Décision I02
**I02_TREE_INVENTORY_COMPLETE / SOURCE_CONTENT_VERIFICATION_OPEN.** Tous les 79 repos ont un index d'arbre ; les 77 fichiers Drive sont référencés. Le contrôle de justesse technique, droits, code, équations et figures et la cartographie fine fichier-par-chapitre restent à faire. Aucun original détruit, aucun secret transféré.
