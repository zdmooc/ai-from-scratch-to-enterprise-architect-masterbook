# Guide de style pédagogique — Bible IA 2026–2030

**Statut : DRAFT editorial policy / à confirmer avant publication.** Le même contrat de progression s'applique aux 24 volumes, tout en laissant chaque auteur justifier une exception.

## Structure recommandée d'un chapitre

1. **Objectif d'apprentissage mesurable** — expliquer ce que le lecteur doit savoir *faire*, pas seulement reconnaître.
2. **Concept introduit sans cercle de définitions** — toute abréviation utile est expliquée.
3. **Exemple minimal chiffré ou technique** — hypothèses et unités explicites.
4. **Interprétation et limitations** — dire ce que l'exemple ne prouve pas.
5. **Contexte d'architecture** — sources d'autorité, permissions, SLO, coûts quand pertinents.
6. **Un contre-exemple** — exemple où la méthode est inadéquate.
7. **Exercices progressifs et corrigés** — erreurs typiques et cas négatifs.
8. **Références et droits** — sources primaires datées, provenance, aucune copie implicite.
9. **Statut éditorial** — DRAFT, REVIEWED ou RELEASED seulement si le gate est prouvé.

## Notation et termes

- Les valeurs mesurées sont séparées des valeurs synthétiques et des sorties attendues.
- Les symboles mathématiques sont introduits avant leur usage et accompagnés d'unités si nécessaire.
- Une comparaison de modèles mentionne corpus, population, métrique, environnement et profil de charge.
- La notion de « probabilité calibrée » suppose un test ; un score ne devient pas une décision métier.
- Un prompt n'est jamais présenté comme une barrière d'accès, une autorisation ou une approbation.
- Distinguer erreur de prédiction, délai du processus métier et coût total ; ne pas transposer abusivement un gain d'une métrique à l'autre.
- Dans une banque, assurance ou administration, les exemples fictifs sont clairement marqués et ne contiennent pas de données clients réelles.

## Gouvernance des répétitions

Les concepts communs sont **définis dans le premier chapitre pertinent**, rappelés en une phrase dans les chapitres suivants et enrichis uniquement avec les détails propres à la tâche.

Exemple V01 : C01 définit RAG/agent ; C06 explique la tokenisation et l'attention ; C07 traite des modalités ; C08 des outils ; C09 décide entre options ; C12 les intègre dans un dossier.

## Échelle de preuve

- **PLANNED** : structure ou idée prévue.
- **DRAFT** : rédaction présente, révision nécessaire.
- **DESIGN_ONLY** : comportement décrit, non testé.
- **LOCAL_TEST_PASS** : code testé avec SHA et environnement identifiés.
- **CI_PASS** : pipeline exécuté avec logs et commit identifié.
- **RUNTIME_PROVEN** : comportement observé sur l'environnement explicitement cité.
- **REVIEWED** : contrôles scientifiques et éditoriaux documentés.
- **RELEASED** : publication explicitement approuvée, rendus contrôlés.

Un succès local ne devient pas automatiquement une preuve sur CRC ou un service client. Le guide exige que le statut soit toujours accompagné de son périmètre.

## Publication

PDF A4, EPUB et HTML sont prévus **en fin de rédaction du volume**, après gel du texte, contrôle scientifique, droits, accessibilité et vérification de rendu. Une compilation technique ponctuelle peut être effectuée pour diagnostiquer un problème, mais **n'est pas une édition publiée**.
