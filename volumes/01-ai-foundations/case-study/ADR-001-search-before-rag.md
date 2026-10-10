# ADR-001 — Évaluer la recherche documentaire avant de déployer un RAG

**Statut : PROPOSED / scénario fictif.**  
**Date : 2026-10-10.**  
**Décideur : à désigner dans le cas pratique.**

## Contexte

Une équipe de support veut répondre aux questions des techniciens à partir de procédures versionnées. Le besoin de génération en langue naturelle est envisagé, mais aucune mesure de valeur relative n'a encore été réalisée.

Les documents possèdent des classifications et des listes d'accès. Toute synthèse non vérifiée pourrait inventer une instruction ou divulguer un extrait restreint.

## Drivers architecturaux

- Ne jamais contourner les politiques documentaires.
- Montrer la provenance et la version des informations.
- Pouvoir fonctionner en mode dégradé.
- Minimiser dépendances, coûts et surface d'attaque.
- Prévoir un mécanisme de correction.
- Disposer d'un protocole d'évaluation stable entre options.

## Options

**A — Recherche traditionnelle gouvernée.** Index, filtre ACL, classement par mots-clés et métadonnées. Le système affiche les documents officiels sans synthèse générée. C'est la **baseline obligatoire**.

**B — Recherche hybride et RAG.** Ajouter représentations vectorielles, récupération et génération, avec validation d'identifiants de citation et politiques côté API. Exige de mesurer les hallucinations, les nouveaux coûts et les cas sans sources.

**C — Agent outillé.** Permettre au système d'interroger différents outils et d'orchestrer des étapes. Cette option implique davantage de limites d'actions, de tests négatifs et de maintenance. Aucun besoin confirmé ne justifie encore ces actions dans le périmètre documentaire simple.

## Décision proposée

**Commencer par l'option A, sans promettre qu'elle est définitivement retenue.** Construire le corpus synthétique de test, mesurer qualité/recherche/permissions/latence/coûts, puis proposer une extension B **uniquement si un gain métier démontré** compense les risques et le coût supplémentaire.

L'option C reste hors du périmètre initial, sauf besoin multi-outils supplémentaire explicitement accepté.

## Conséquences

### Positives

- Réduction de la surface fonctionnelle à vérifier en première phase.
- Vérification plus simple des ACL et de la provenance.
- Base comparative claire pour une future génération.
- Possibilité de rendre les sources indépendantes des modèles utilisés.

### Négatives

- Les réponses sont moins fluides ou moins synthétiques que celles d'un générateur.
- Certaines questions nécessiteront de parcourir plusieurs documents.
- Le gain d'une option RAG peut être réel mais non disponible dans la première phase.

## Risques résiduels

Une recherche non générative n'élimine pas les risques d'index erroné, de permission périmée ou de source ancienne. Les contrôles de qualité et de versionnement restent indispensables.

## Conditions de réexamen

Réexaminer l'ADR si :
- un corpus d'évaluation montre une valeur significative du RAG ;
- la nature du contenu, des permissions ou du nombre d'utilisateurs change ;
- des besoins d'interopérabilité d'outils sont formellement définis ;
- les coûts, l'hébergement ou les risques réglementaires évoluent.

## Preuves nécessaires avant acceptation

- Baseline A exécutée sur le même corpus que B.
- Tests négatifs des ACL et des documents retirés.
- Validation des citations et abstentions en B.
- Mesures de latence et coûts sous charge déclarée.
- Risques approuvés par les acteurs autorisés.

**Aucun de ces résultats de comparaison n'est revendiqué comme observé à la date de ce document.**
