#!/usr/bin/env python3
"""Static editorial structure validation: no external packages, network, model or cloud."""
import json
import re
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
    # Manuscript counts follow the catalog; avoid hard-coded 5/6/7 chapter gates.
    drafted = {
        entry["volume"]: sum(ch["status"] == "DRAFT_REVIEW_REQUIRED"
                             for ch in entry["chapters"])
        for entry in chapters["volumes"]
    }
    total_drafted = sum(drafted.values())
    assert chapters["chapters_drafted"] == total_drafted
    assert chapters["chapters_planned_not_written"] == 288 - total_drafted
    for volume in volumes:
        expected = drafted[volume["id"]]
        folder = ROOT / "volumes" / volume["slug"] / "chapters"
        manuscripts = sorted(folder.glob("*.qmd")) if folder.exists() else []
        assert len(manuscripts) == expected, (
            f"V{volume['id']}: expected {expected} draft files, got {len(manuscripts)}")
        assert volume["status"] == ("DRAFT" if expected else "PLANNED"), (
            f"V{volume['id']}: status inconsistent with drafted chapters")
        for number, source in enumerate(manuscripts, start=1):
            assert source.name.startswith(f"{number:02d}-"), (
                f"V{volume['id']}: unexpected filename {source.name}")
            data = source.read_text(encoding="utf-8")
            assert "DRAFT" in data and len(data) >= 2800, f"invalid draft {source}"
            headings = [int(m.group(1)) for m in re.finditer(r"^## (\d+)\.", data, re.M)]
            assert headings == list(range(1, len(headings) + 1)), (
                f"V{volume['id']}: nonsequential numbered section in {source}")
            assert data.count("$") % 2 == 0, f"unbalanced display math in {source}"
            # Check that each local Markdown asset link resolves from its source
            # file directory. External links are reviewed separately.
            local_links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", data)
            for target in local_links:
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                relpath = target.split("#", 1)[0].strip()
                if not relpath:
                    continue
                assert (source.parent / relpath).resolve().is_file(), (
                    f"broken local source link in {source}: {target}")


    mapping = json.loads((ROOT / "sources" / "consolidation" /
                          "historical_manuscript_mapping_2026-10-10.json").read_text(encoding="utf-8"))
    assert mapping["unique_source_units"] == 56
    assert mapping["physical_files"] == 61
    assert len(mapping["source_unit_catalog"]) == 56
    assert all(not x["publish_approval"] for x in mapping["source_unit_catalog"])

    for required in ("diagrams/v01/architecture-options.svg",
                     "diagrams/v01/agent-trust-boundaries.svg",
                     "diagrams/v01/chronological-evaluation.svg",
                     "volumes/01-ai-foundations/case-study/requirements.md",
                     "volumes/01-ai-foundations/case-study/ADR-001-search-before-rag.md",
                     "volumes/01-ai-foundations/case-study/verification-matrix.md",
                     "volumes/01-ai-foundations/R13_GAP_REGISTER.md"):
        assert (ROOT / required).is_file(), f"missing V01 source asset: {required}"

    for path in ("labs/v01-symbolic-ai/rule_engine.py",
                 "labs/v01-symbolic-ai/test_rule_engine.py",
                 "labs/v01-agent-guardrails/agent_dispatcher.py",
                 "labs/v01-agent-guardrails/test_agent_dispatcher.py",
                 "labs/v01-experiment/experiment.py",
                 "labs/v01-experiment/test_experiment.py",
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
    print(f"MASTERBOOK_STRUCTURE_PASS volumes={len(volumes)} chapters_planned=288 drafted={total_drafted} parts=6 page_target={total} status=EDITORIAL_DRAFT")

if __name__ == "__main__":
    validate()
