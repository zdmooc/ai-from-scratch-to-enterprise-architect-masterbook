# Plan détaillé préliminaire — V15: LLM Serving et ingénierie de l'inférence

**État : I04_DRAFT_TOC / NOT_PUBLISHED.** 12 chapitres proposés, cible indicative 380 pages A4 pour l'ensemble du volume.

1. **C01** — Architecture d'inférence et objectifs SLO — `PLANNED`
2. **C02** — Calculs, tokens, prefilling et decoding — `PLANNED`
3. **C03** — KV cache, context windows et concurrence — `PLANNED`
4. **C04** — Batching, scheduling et optimisations de latence — `PLANNED`
5. **C05** — Précision, quantification et qualité — `PLANNED`
6. **C06** — Ollama, runtimes locaux et API compatibles — `PLANNED`
7. **C07** — vLLM, tensor parallelism et serving distribué — `PLANNED`
8. **C08** — KServe, OpenShift AI et routing — `PLANNED`
9. **C09** — Model cache, autoscaling et warm starts — `PLANNED`
10. **C10** — Benchmarks reproductibles et capacity planning — `PLANNED`
11. **C11** — Observabilité, disponibilité et coûts par requête — `PLANNED`
12. **C12** — Lab de serving avec charge et critères d'acceptation — `PLANNED`

## Critères de validation éditoriale

- Le volume explique les prérequis utiles et introduit les concepts progressivement.
- Chaque chapitre doit comporter une théorie originale, un exemple, exercices/corrigés et références vérifiées.
- Les labs doivent être exécutables et évaluables avec un gate PASS/FAIL ; le budget CPU/GPU/cloud est explicite.
- Les sources Drive et GitHub sont à utiliser **en référence** selon le registre I02, après contrôle des droits et de l'exactitude, sans copier automatiquement leurs contenus.
- `PLANNED` **ne signifie pas texte écrit** et la cible de pages n'est pas un quota.

## Sources et correspondance

Voir [Matrice de couverture du portefeuille](../../sources/audits/I02_GITHUB_COVERAGE_MATRIX_2026-10-10.md) et [inventaire Drive structuré](../../sources/inventories/drive_files_2026-10-10.json).
