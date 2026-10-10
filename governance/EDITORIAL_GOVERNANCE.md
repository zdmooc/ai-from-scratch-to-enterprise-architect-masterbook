# Gouvernance éditoriale, vérité et droits

Adaptation du modèle [Wero/EPI handbook](https://github.com/zdmooc/wero-epi-reference-architecture-handbook/blob/main/governance/WORKING_MODEL.md).

## Sources de vérité
- **Ce dépôt** : original éditorial du manuscrit, bibliographie, figures, exercices, publication.
- **Google Drive** : manuscrits Word/PDF sources et archives ; ne rien supprimer sans consentement.
- **Dépôts techniques** : code, contrats, tests, preuves ; rester propriétaires de leur exécution.
- **Cadrage transverse** : ownership, statuts de programmes, priorités.

## Classes de vérité
- `PUBLIC_VERIFIED` : affirmation appuyée par référence publique primaire datée.
- `REFERENCE_ARCHITECTURE` : design proposé, ni architecture interne certifiée ni preuve runtime.
- `INFERRED` : déduction explicitement signalée.
- `STATIC_VALIDATED` : validation statique/revue, pas runtime.
- `CI_VERIFIED` : contrôles automatisés en CI, portée indiquée.
- `RUNTIME_PROVEN` : exécution observée et preuves situées (environnement, date, versions).
- `TO_BE_VERIFIED` : hypothèse ou sujet en attente de confirmation.

## Gate d'un chapitre publiable
- [ ] Texte original compréhensible au niveau cible, prérequis documentés
- [ ] Définitions, formules et hypothèses vérifiées
- [ ] Exercices et corrigés cohérents, tests du code reproductibles
- [ ] Diagrammes vectoriels sourcés et lisibles, droits maîtrisés
- [ ] Compétences visées évaluables et lab avec DoD
- [ ] Liens/versions officiels valides, citations exactes
- [ ] Limites des performances, conformité et coûts précisées
- [ ] Relecture technique, linguistique et accessibilité
- [ ] Quarto HTML + PDF + EPUB QA pass ; pas de référence cassée
- [ ] Gel du commit, version du volume, checksums, release explicitement autorisée

## Protection des sources
Ce dépôt est **privé au 10/10/2026**, mais la confidentialité GitHub ne suffit pas à autoriser toutes les données. Ne pas y pousser sans revue et nécessité :
- données de santé, personnelles ou client ;
- secrets, clés, identifiants ;
- documents privés Drive par défaut ;
- extraits longs protégés par droit d'auteur, figures externes non autorisées ;
- preuves runtime brutes susceptibles de révéler des détails confidentiels.

Les contenus des autres dépôts peuvent être **synthétisés** ; ne pas les recopier sans licence et justification.

## Publication et maintenance
Chaque volume évolue indépendamment et respecte un cycle plan → draft → peer review → build proof → freeze → publication. **Aucun déclenchement automatique d'une release publique.**
