# V01 — Dossier d'architecture pédagogique : recherche documentaire sécurisée

**Statut : REFERENCE_ARCHITECTURE / PROPOSED / NOT_DEPLOYED.**

Ce dossier accompagne le chapitre 12. Il décrit une organisation fictive, cent techniciens potentiels, des procédures internes et des statuts de tickets. Il n'est ni une architecture interne connue d'un client, ni un déploiement réel.

## Documents

- [Contrat de besoin et exigences](requirements.md)
- [ADR-001 — rechercher avant de générer](ADR-001-search-before-rag.md)
- [Matrice de vérification et risques](verification-matrix.md)

## Objectif et exclusion

L'application doit permettre la **recherche et la lecture** de procédures autorisées. Une génération de résumé peut être étudiée uniquement après évaluation d'une baseline de recherche.

**Hors périmètre :** mutations de production, transferts financiers, création de secrets, actions autonomes irréversibles, démonstration de conformité réglementaire.

## Architecture logique de travail

~~~text
Utilisateur identifié
       |
       v
API d'accès et politiques
       |
       v
Recherche documentaire avec ACL ---> Corpus versionné / catalogue de sources
       |
       +--> Option RAG *conditionnelle* -> Génération de synthèse
       |                                -> Contrôle de citations
       v
Réponse sourcée et journal minimisé
~~~

Les décisions effectives d'authentification et d'autorisation doivent être imposées **côté service**. Les documents indexés sont traités comme des **données de moindre confiance**, y compris lorsque leur texte demande d'appeler un outil.

## Responsabilités envisagées

- Métier : besoins et critères d'acceptation.
- Équipe documentaire : validité, version et propriétaire des sources.
- Équipe identité/sécurité : permissions et frontières.
- Architecture : alternatives, arbitrages, ADR et qualités attendues.
- Exploitation : supervision, incidents, réversibilité et capacité.
- Risque/conformité : cadre applicable au périmètre retenu.

## Gate de réalisation

**NOT_EXECUTED** : aucun des tests métier de la matrice n'a été exécuté contre une application. Les labs Python du V01 prouvent seulement des calculs ou des refus dans de **petits programmes synthétiques**, pas les propriétés opérationnelles de cette architecture.

Les objectifs chiffrés, le coût, la charge et les obligations devront être validés avec les acteurs avant toute décision réelle.
