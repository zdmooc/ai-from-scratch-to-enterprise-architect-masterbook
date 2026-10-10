# V01 — Contrôle éditorial statique des six brouillons

**Date :** 10 octobre 2026. **Portée :** inspection des fichiers `*.qmd` directement relus via le connecteur GitHub sur la branche `main` privée, puis contrôles de structure en mémoire. **Il ne s'agit ni d'une CI GitHub ni d'une compilation Quarto/PDF/EPUB.**

## Résultat : BASIC_SOURCE_STRUCTURE_PASS

| Chapitre | Mots approximatifs (espaces) | Caractères | Sections numérotées |
|---|---:|---:|---:|
| C01 — IA et frontières | 4 429 | 29 288 | 16 |
| C02 — Histoire et paradigmes | 3 077 | 20 569 | 15 |
| C03 — IA symbolique et règles | 2 320 | 15 313 | 15 |
| C04 — ML introductif | 2 516 | 16 205 | 14 |
| C05 — Deep Learning introductif | 2 341 | 15 777 | 15 |
| C06 — NLP / Transformer / LLM | 2 444 | 16 568 | 15 |
| **Total approximatif V01** | **17 127 mots** | **113 301 caractères** | **90 sections** |

Contrôles réalisés via lecture des fichiers GitHub :
- Les six chapitres contiennent explicitement la mention `DRAFT`.
- Les sections numérotées sont continues (C01 1–16, C02 1–15, C03 1–15, C04 1–14, C05 1–15, C06 1–15).
- Nombre pair de délimiteurs display-math `$$`, et équilibre des formes mathématiques `\\[` et `\\]` dans ces fichiers.
- Le catalogue `catalog/chapters.json` déclare **10 chapitres en brouillon dans le Masterbook** (V01=6, V02=2, V03=2) et **278 planifiés non rédigés** ; l'inventaire vérifié correspond.
- Exemple numérique d'attention du C06 revérifié : poids `0.66976` et `0.33024`, combinaison de valeurs environ `(1.33952, 0.66048)`.

## Non réalisé (ne pas déduire de ce PASS)

- **Aucune mesure de pagination A4 réelle** : la cible V01 reste 280 pages, non prouvée.
- Aucune compilation HTML, PDF ou EPUB.
- Aucune relecture scientifique indépendante complète ou comparaison automatique de toutes les équations avec une source primaire.
- Aucun test de contenu par un groupe de débutants.
- Aucune CI GitHub sur le dernier SHA privé : les runners ne démarrent pas et la cause n'est pas établie.
- Aucun import des originaux Google Drive, aucun changement de facturation.

Ce rapport est une **preuve limitée de cohérence statique**, et non une acceptation de publication. Le cycle editorial R07–R22 demeure ouvert.
