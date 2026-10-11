# V01 — Figures vectorielles originales (source SVG éditable)

**Statut : R15 PARTIAL_6_SVG_XML_CI_PASS / VISUAL_RENDER_QA_NOT_DONE.** Ces figures sont des sources originales créées pour le Masterbook. Elles n'ont pas été importées d'un cours externe, d'une banque d'images ou du Drive.

- `architecture-options.svg` — choix comparatif des approches, utilisé dans C09.
- `agent-trust-boundaries.svg` — contrôle des outils, ACL et données de moindre confiance, utilisé dans C08.
- `chronological-evaluation.svg` — distinction entre entraînement, test et prévision à un pas, utilisé dans C11.

Les SVG sont versionnés et modifiables en texte. Il reste à contrôler : rendu réel avec un navigateur et Quarto, contraste, lisibilité A4, flèches, orthographe, accessibilité des légendes et impression N&B. Aucune génération PDF ou EPUB n'est faite ici.

**Figures encore à dessiner :** taxonomie de risques, vue C4 du mini-projet et schémas complémentaires selon la relecture.

- `neural-network-backprop.svg` — calcul avant et gradient, intégré à C05.
- `qkv-attention-worked-example.svg` — pondération Q/K/V et softmax, intégré à C06.
- `rag-trust-boundaries.svg` — RAG documentaire : filtrage des droits et validation des sources, intégré à C12.

**R15 : 6 SVG originaux au total.** Un contrôle du rendu graphique réel reste nécessaire avant le gel du manuscrit ; statut **PARTIAL**, pas de PDF ou EPUB.

## Contrôle automatisé du 11 octobre
La CI GitHub [38118052494](https://github.com/zdmooc/ai-from-scratch-to-enterprise-architect-masterbook/actions/runs/38118052494) a exécuté avec succès `scripts/validate_svg_sources.py` sur les six SVG : XML, dimensions/viewBox, titre/description et absence de scripts embarqués. Cela ne constitue **pas** une validation visuelle ni une preuve de justesse scientifique.
