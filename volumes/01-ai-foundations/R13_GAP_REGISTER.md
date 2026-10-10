# V01 — R13 : registre des lacunes après les 12 premiers brouillons

**Date : 10/10/2026. Statut : AUDIT_STATIQUE_INITIAL / RELECTURE_SCIENTIFIQUE_NON_REALISEE.**

## Périmètre

Douze manuscrits Quarto C01–C12 sont présents, **29 119 mots** approximatifs (comptage par espaces), **192 159 caractères** hors autres annexes et laboratoires. Tous sont marqués DRAFT. Les 12 ont des sections numérotées continues, des blocs de code et mathématiques délimités de manière cohérente au niveau lexical. Il ne s'agit ni d'un build Quarto, ni d'une vérification de toutes les équations, ni d'une preuve d'atteinte de la cible **280 pages A4**.

## Matrice des chapitres

| Chapitre | Mots approx. | Priorité de finition |
|---|---:|---|
| C01 Définir l'IA | 4 429 | Bibliographie, figures, éliminer doublons avec C09 |
| C02 Histoire | 3 077 | Contrôle des sources primaires et de la chronologie |
| C03 IA symbolique | 2 320 | Diagramme règles + lab V01 approfondi |
| C04 Apprentissage statistique | 2 516 | Vérifier formules, matrice de confusion et séparation des données |
| C05 Deep Learning | 2 341 | Dessin de réseau et micro-lab gradient sur CPU |
| C06 NLP/Transformers | 2 444 | Vérification de softmax, schémas Q/K/V originaux |
| C07 GenAI multimodale | 2 200 | Figures originales, cas ASR/TTS/images et droits |
| C08 Agents | 2 091 | Tests négatifs des outils et protocole MCP selon versions |
| C09 Cas d'usage | 1 849 | Enrichir la matrice comparative avec options sans IA |
| C10 Risques/éthique | 1 923 | Contrôler les références et obligations par date/version |
| C11 Expérimentation | 1 658 | Lab synthétique revérifié, expliquer incertitude statistique |
| C12 Mini-projet | 2 271 | Produire annexes ADR, threat model, checklist et corrigés étendus |
| **TOTAL** | **29 119** | **AUCUN CHAPITRE DECLARE TERMINÉ** |

## Gates transversaux P0

- **P0 — Scientifique** : revue indépendante des définitions et équations (attention, probabilités, gradients, métriques et données).
- **P0 — Droit d'auteur** : attribuer et vérifier toutes les références et figures, aucune copie aveugle des originaux Drive.
- **P0 — Coherence** : termes et exemples cohérents entre C01–C12, sans doublons importants.
- **P0 — Evaluation** : chaque chapitre doit posséder une compétence testable et des corrigés vérifiés.
- **P0 — Labs** : exécuter les laboratoires du Volume 01, contrôler les erreurs/refus et rattacher les preuves au bon SHA.
- **P0 — Figures** : diagrammes originaux pour réseau neuronal, Q/K/V, pipeline RAG, flux d'agent et choix d'architecture.
- **P0 — Publication** : pas de PDF/EPUB avant gel de contenu, relecture, validation des droits et contrôle des tests.

## Points de densification P1

- Ajouter un glossaire consolidé (débutant, définitions non circulaires).
- Élargir les exercices et corrigés, notamment C07 à C12, sans inventer des résultats de benchmark.
- Inclure des références versionnées et accessibles pour les sujets périssables (frameworks, lois, coûts).
- Ajouter un dossier d'architecture exemplaire et ses contre-exemples.
- Préparer le passage à V02 mathématiques et V03 Python avec des liens de prérequis explicites.

## Décision d'itération

**R13 reste IN_PROGRESS** : audit statique initial réalisé mais les vérifications et corrections scientifiques/éditoriales ne sont pas closes. **R14–R22 restent ouverts**. Les résultats des 12 tests du laboratoire C11 ne prouvent que leur portée déclarée.

**Aucune pagination PDF, EPUB, HTML finale ou release n'a été produite.**
