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

    chapters = json.loads((ROOT / "catalog" / "chapters.json").read_text(encoding="utf-8"))
    assert chapters["chapters_total"] == 288
    assert len(chapters["volumes"]) == 24
    for v, details in zip(volumes, chapters["volumes"]):
        assert details["volume"] == v["id"]
        assert details["title"] == v["title"]
        assert len(details["chapters"]) == 12
        assert [c["id"] for c in details["chapters"]] == [f"C{i:02d}" for i in range(1, 13)]
        assert len({c["title"] for c in details["chapters"]}) == 12
        assert (ROOT / "volumes" / v["slug"] / "CHAPTER_PLAN.md").is_file()
    manuscripts = sorted((ROOT / "volumes" / "01-ai-foundations" / "chapters").glob("*.qmd"))
    assert len(manuscripts) == 6, "V01 must have exactly 6 draft chapters"
    for source in manuscripts:
        assert len(source.read_text(encoding="utf-8")) >= 2800, f"draft unexpectedly short: {source}"
        assert "DRAFT" in source.read_text(encoding="utf-8"), f"draft label missing: {source}"
    drafted = {"01": 6, "02": 2, "03": 2}
    for volume, expected in drafted.items():
        parent = next(v for v in volumes if v["id"] == volume)
        files = sorted((ROOT / "volumes" / parent["slug"] / "chapters").glob("*.qmd"))
        assert len(files) == expected, f"V{volume}: expected {expected} drafts, found {len(files)}"
        assert parent["status"] == "DRAFT"
        for i, path in enumerate(files, start=1):
            assert path.name.startswith(f"{i:02d}-"), f"V{volume}: expected C{i:02d}"
            draft = path.read_text(encoding="utf-8")
            assert "DRAFT" in draft and len(draft) >= 2800, f"draft invalid: {path}"
    for item in chapters["volumes"]:
        expected = drafted.get(item["volume"], 0)
        observed = sum(chapter["status"] == "DRAFT_REVIEW_REQUIRED" for chapter in item["chapters"])
        assert observed == expected, f"status mismatch for V{item['volume']}"
        if not expected:
            assert next(v for v in volumes if v["id"] == item["volume"])["status"] == "PLANNED"
    assert chapters["chapters_drafted"] == 10
    assert chapters["chapters_planned_not_written"] == 278

    mapping = json.loads((ROOT / "sources" / "consolidation" /
                          "historical_manuscript_mapping_2026-10-10.json").read_text(encoding="utf-8"))
    assert mapping["unique_source_units"] == 56
    assert mapping["physical_files"] == 61
    assert len(mapping["source_unit_catalog"]) == 56
    assert all(not x["publish_approval"] for x in mapping["source_unit_catalog"])

    for path in ("labs/v01-symbolic-ai/rule_engine.py",
                 "labs/v01-symbolic-ai/test_rule_engine.py",
                 "labs/v02-vectors/vector_math.py",
                 "labs/v02-vectors/test_vector_math.py",
                 "labs/v03-python-basics/statistics_basics.py",
                 "labs/v03-python-basics/test_statistics_basics.py",
                 "catalog/chapters.json"):
        assert (ROOT / path).is_file(), f"missing {path}"

    for required in ("MASTER_TOC.md", "MASTER_PLAN.md", "ROADMAP.md",
                     "sources/GOOGLE_DRIVE_INVENTORY.md",
                     "sources/INTERNAL_GITHUB_SOURCES.md",
                     "sources/PUBLIC_GITHUB_REFERENCES.md",
                     "governance/EDITORIAL_GOVERNANCE.md"):
        assert (ROOT / required).is_file(), f"missing {required}"
    print(f"MASTERBOOK_STRUCTURE_PASS volumes={len(volumes)} chapters_planned=288 v01_drafts={len(manuscripts)} parts=6 page_target={total} status=EDITORIAL_DRAFT drafted=10")

if __name__ == "__main__":
    validate()
