# V01 — Carte de lecture et frontières entre les 12 chapitres

**Statut : R13 — harmonisation éditoriale en cours.**

| Chapitre | Apport propre | À ne pas répéter en détail | Prépare |
|---|---|---|---|
| C01 | Définitions et frontières des approches | Matrice complète d'options métier | C09 et C12 |
| C02 | Histoire et lecture critique des jalons | Mathématiques détaillées des réseaux | C03, C05, C06 |
| C03 | Logique, faits, déductions et règles | Gestion complète des agents | C04, C08 |
| C04 | Features, labels, splits, métriques | Expérience complète pas à pas | C11 |
| C05 | Neurones, gradients et mémoire | Calcul complet des Transformers | C06 |
| C06 | Tokens, attention, architecture LLM | Multimodal, outils et sécurité approfondis | C07, C08 |
| C07 | Génération texte, image et audio | Gouvernance complète des risques | C10 |
| C08 | Orchestration, outils, limites d'action | Méthode générale de choix d'architecture | C09, C12 |
| C09 | Alternatives sans IA et ADR | Définitions générales du C01 | C11, C12 |
| C10 | Biais, droits, conséquences et risques | Cours juridique complet du volume 19 | C12 |
| C11 | Protocole expérimental et preuve bornée | Théorie complète du ML | C12 |
| C12 | Synthèse et mini-projet d'architecture | Répétition littérale des onze chapitres | V02–V24 |

## Deux parcours d'étude

**Débutant complet :** C01 → C02 → C03 → C04 → C05 → C06 → C07 → C08 → C09 → C10 → C11 → C12. Aucun prérequis GPU ou OpenShift.

**Architecte IT confirmé, nouveau dans l'IA :** C01 → C04 → C06 → C08 → C10 → C09 → C11 → C12 ; les autres chapitres complètent histoire, méthodes symboliques, réseaux et multimodalité.

La seconde trajectoire n'est pas une certification d'acquis : réaliser le [contrôle final du C12](chapters/12-capstone-and-exercises.qmd) et les exercices si des lacunes apparaissent.

## Règles de cohérence

- Un résultat de **conception** n'est pas une preuve **runtime**.
- Les exemples du volume sont synthétiques et ne donnent pas de droits de mutation réels.
- Une revue de droits ne peut pas être déduite d'un texte de prompt.
- Les tests locaux en Python ne prouvent pas la sécurité ou l'exploitabilité d'une plateforme de production.
- Les 280 pages sont un **objectif** éditorial, pas une mesure du texte actuellement disponible.

Voir aussi le [glossaire](GLOSSARY.md), le [suivi des itérations](ITERATION_TRACKER.md) et le [registre des lacunes](R13_GAP_REGISTER.md).
