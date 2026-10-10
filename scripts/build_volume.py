#!/usr/bin/env python3
"""Render an independent Quarto book from the volume catalog (drafts are previews only)."""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOLUMES = json.loads((ROOT / "catalog" / "volumes.json").read_text(encoding="utf-8"))["volumes"]

def quoted(value):
    return json.dumps(value, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", required=True, help="01..24")
    parser.add_argument("--format", choices=("html", "pdf", "epub"), default="html")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    matches = [x for x in VOLUMES if x["id"] == args.volume]
    if not matches:
        parser.error("volume not found in catalog")
    v = matches[0]
    base = ROOT / "volumes" / v["slug"]
    if not (base / "index.qmd").is_file():
        parser.error("index.qmd missing")
    chapters = sorted((base / "chapters").glob("*.qmd")) if (base / "chapters").is_dir() else []
    files = ["index.qmd"] + [p.relative_to(base).as_posix() for p in chapters]
    yaml = ("project:\n  type: book\n  output-dir: _book\n"
            "book:\n  title: " + quoted("V" + v["id"] + " — " + v["title"]) + "\n"
            "  chapters:\n" + "".join("    - " + quoted(name) + "\n" for name in files)
            + "format:\n"
              "  html:\n    toc: true\n    number-sections: true\n"
              "  pdf:\n    documentclass: scrbook\n    papersize: a4\n"
              "    toc: true\n    number-sections: true\n"
              "    geometry:\n      - margin=20mm\n"
              "  epub:\n    toc: true\n")
    print(f"VOL={v['id']} FORMAT={args.format} STATUS={v['status']} CHAPTER_FILES={len(chapters)}")
    if args.dry_run:
        print(yaml)
        return
    (base / "_quarto.yml").write_text(yaml, encoding="utf-8")
    subprocess.run(["quarto", "render", "--to", args.format], cwd=base, check=True)

if __name__ == "__main__":
    main()
