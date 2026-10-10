#!/usr/bin/env python3
"""Static editorial structure validation: no external packages, network, model or cloud."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "volumes.json"

def validate():
    raw = json.loads(CATALOG.read_text(encoding="utf-8"))
    volumes = raw["volumes"]
    assert len(volumes) == 24, "expected 24 volumes"
    assert [v["id"] for v in volumes] == [f"{n:02d}" for n in range(1, 25)]
    assert len(set(v["slug"] for v in volumes)) == 24, "duplicate volume slugs"
    assert len(raw["parts"]) == 6
    assert [p["part"] for p in raw["parts"]] == list(range(1, 7))
    assert len([v for v in volumes if 1 <= v["part"] <= 6]) == 24
    assert all(sum(v["part"] == p for v in volumes) == 4 for p in range(1, 7))
    assert all(v["status"] in ("PLANNED", "DRAFT", "REVIEWED", "VERIFIED", "RELEASED") for v in volumes)
    total = sum(v["target_pages"] for v in volumes)
    assert total == raw["target_total_pages"] == 9530, f"unexpected page target: {total}"
    assert all(v["target_pages"] > 0 and v["title"] and v["scope"] for v in volumes)
    for v in volumes:
        path = ROOT / "volumes" / v["slug"] / "index.qmd"
        assert path.is_file(), f"missing {path}"
        data = path.read_text(encoding="utf-8")
        assert f"V{v['id']}" in data, f"wrong volume marker in {path}"
        assert "PLANNED" in data or v["status"] != "PLANNED", f"draft marker missing {path}"
    for required in ("MASTER_TOC.md", "MASTER_PLAN.md", "ROADMAP.md",
                     "sources/GOOGLE_DRIVE_INVENTORY.md",
                     "sources/INTERNAL_GITHUB_SOURCES.md",
                     "sources/PUBLIC_GITHUB_REFERENCES.md",
                     "governance/EDITORIAL_GOVERNANCE.md"):
        assert (ROOT / required).is_file(), f"missing {required}"
    print(f"MASTERBOOK_STRUCTURE_PASS volumes={len(volumes)} parts=6 page_target={total} status=EDITORIAL_BOOTSTRAP")

if __name__ == "__main__":
    validate()
