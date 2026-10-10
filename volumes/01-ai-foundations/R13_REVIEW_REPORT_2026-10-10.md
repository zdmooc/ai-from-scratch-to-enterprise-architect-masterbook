# V01 — Bilan de l'itération R13 : cohérence et densification initiales

**Date : 2026-10-10. Statut : R13_HARMONIZATION_STATIC_PASS / DEPTH_AND_REVIEW_OPEN.**  
**Portée :** analyse des douze sources Quarto du dépôt privé, modifications originales et contrôles statiques après commit. **Aucune édition publiée.**

## Ce qui a été corrigé

1. **Redondances de fonction** : une note de portée et des renvois ciblés ont été ajoutés à chacun des douze chapitres. C01 définit les concepts ; C09 compare les options ; C12 les intègre dans un dossier de conception.
2. **Six lacunes pédagogiques** : ajout d'un atelier propre à C07 (multimodal), C08 (idempotence/résultat inconnu), C09 (critères éliminatoires), C10 (registre de risques), C11 (incertitude du benchmark), C12 (traçabilité besoins/risques/tests).
3. **Vocabulaire stabilisé** : création d'un [glossaire commun de 69 notions](GLOSSARY.md) avec les renvois vers les chapitres.
4. **Prérequis et parcours** : création d'une [carte de lecture](READING_MAP.md), distinguant le parcours débutant du parcours architecte confirmé.
5. **Conventions communes** : les explications distinguent « conception », « test local », « test CI », « résultat runtime » et « publication », et rappellent les limites des données synthétiques.

## Vérifications réalisées

Contrôles menés sur le contenu courant des 12 chapitres récupérés via GitHub :

| Contrôle | Constat |
|---|---|
| Chapitres | 12/12 présents et explicitement marqués DRAFT |
| Volume approximatif | **32 101 mots** (découpage simple par espaces, non pagination) |
| Titres numérotés | 181 sections, séquences continues par chapitre |
| Liens locaux Markdown | **38 liens** résolus contre l'arbre GitHub ; **0 lien cassé** observé |
| Délimiteurs mathématiques de blocs | Aucun déséquilibre lexical détecté |
| Délimiteurs de code | Aucun bloc non fermé détecté dans l'analyse lexicale |
| Paragraphes longs identiques | Aucun doublon exact d'au moins 140 caractères observé parmi les 12 chapitres |
| Figures | SVG déjà versionnés et reliés (rendu visuel et Quarto non vérifiés) |

**Attention :** l'absence de doublons exacts n'exclut pas des répétitions de sens. Les contrôles lexicaux de formules ne garantissent pas leur vérité mathématique, et la résolution des chemins ne prouve pas la réussite d'un rendu Quarto.

## Découpage des responsabilités éditoriales

| Bloc | Chapitres | Contrôle de non-recouvrement |
|---|---|---|
| Fondamentaux et histoire | C01–C02 | Définitions vs jalons historiques |
| Calcul et apprentissage | C03–C05 | Règles vs apprentissage statistique vs réseaux |
| Langage et génération | C06–C07 | Mécanique Transformer vs production multimodale |
| Outillage et choix | C08–C09 | Action et permissions vs choix de solution |
| Risque et preuve | C10–C11 | Conséquences/biais vs méthode d'évaluation |
| Intégration | C12 | Synthèse sous forme de dossier, sans revendiquer de déploiement |

## Lacunes empêchant une clôture totale de R13

- **Densité rédactionnelle :** environ 32 100 mots pour une cible indicative de 280 pages A4. Il reste une différence importante entre une première rédaction complète et un traité approfondi. Le décompte de pages n'est **pas** mesuré à ce stade.
- **Exemples mathématiques et figures :** un contrôle indépendant des équations et illustrations reste requis (R18, R15).
- **Évaluation pédagogique :** vérifier que tous les exercices ont un corrigé fiable et permettent d'acquérir les objectifs (R17).
- **Sources et licences :** les bibliographies, dates, citations et droits sur d'éventuels matériaux externes doivent être validés (R19).
- **Publication :** aucun HTML/PDF/EPUB n'a été rendu ; choix intentionnel de fin de cycle (R22).
- **Qualité de lecture :** une relecture humaine de l'intégralité du manuscrit et un test débutant restent à faire (R20).

## Décision

**R13 — première passe d'harmonisation réussie ; clôture éditoriale complète non prononcée.**

L'objectif immédiat est de renforcer la densité *utile* et l'exactitude, pas de générer du remplissage pour atteindre un nombre de pages. Les travaux d'exécution et de finalisation R14–R21 peuvent se poursuivre en parallèle.

**Ne pas confondre** ce bilan avec la validation scientifique, la certification du contenu ou une décision de publier.
