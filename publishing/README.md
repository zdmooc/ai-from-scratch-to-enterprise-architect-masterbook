# Publication indépendante de chacun des 24 volumes

## Outils
Python 3.10+ pour la validation et la préparation de configuration. Quarto et (pour PDF) une distribution LaTeX/TinyTeX pour les rendus.

## Commandes locales
```bash
python scripts/validate_masterbook.py
python scripts/build_volume.py --volume 01 --format html --dry-run
python scripts/build_volume.py --volume 01 --format html
python scripts/build_volume.py --volume 01 --format pdf
python scripts/build_volume.py --volume 01 --format epub
```
Le script génère, à partir de `catalog/volumes.json`, le fichier local `volumes/<slug>/_quarto.yml` non versionné. Quarto écrit dans `volumes/<slug>/_book/` (ignoré par Git). Les 24 volumes possèdent un `index.qmd` **de planification** ; **ne pas publier en tant que version achevée**.

## GitHub Actions
- `masterbook-validation.yml` : validation statique du catalogue et des 24 index sur push/PR.
- `volume-preview.yml` : **déclenchement manuel uniquement** pour produire un artefact HTML/PDF/EPUB de prévisualisation du volume sélectionné.
- **Aucune release publique automatique**, aucune importation Drive ou extraction de dépôt privé par CI.

## Reprise du modèle Wero
Même discipline : chapitres Markdown/QMD, figures SVG, compilation Quarto, QA de la pagination/références, git source SHA gelé, publication contrôlée. La réalisation des contrôles avancés PDF/EPUB (figures/xrefs/chiffres exacts) constitue un jalon ultérieur.
