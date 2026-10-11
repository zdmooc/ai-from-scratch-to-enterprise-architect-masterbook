"""Validate the source SVG diagrams without rendering or network access.

This gate checks XML syntax, intrinsic accessibility and disallowed embedded
content. It DOES NOT establish visual readability, factual correctness or
whether a PDF/EPUB will render.
"""
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "{http://www.w3.org/2000/svg}"
BLOCKED = {"script", "foreignObject", "iframe", "image"}
FILES = ROOT / "diagrams" / "v01"


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path):
    tree = ET.parse(path)
    root = tree.getroot()
    assert root.tag == SVG_NS + "svg", f"incorrect SVG root: {path}"
    assert root.get("role") == "img", f"missing image role: {path}"
    width = int(root.get("width", "0"))
    height = int(root.get("height", "0"))
    assert 100 <= width <= 10000 and 100 <= height <= 10000, (
        f"invalid dimensions: {path}")
    viewbox = root.get("viewBox", "").split()
    assert len(viewbox) == 4 and float(viewbox[2]) > 0 and float(viewbox[3]) > 0, (
        f"invalid viewBox: {path}")
    title, desc = root.find(SVG_NS + "title"), root.find(SVG_NS + "desc")
    assert title is not None and (title.text or "").strip(), f"missing title: {path}"
    assert desc is not None and (desc.text or "").strip(), f"missing description: {path}"
    named = set((root.get("aria-labelledby") or "").split())
    assert title.get("id") in named and desc.get("id") in named, (
        f"svg needs labelled title and description: {path}")
    for element in root.iter():
        assert local_name(element.tag) not in BLOCKED, (
            f"blocked SVG element in {path}: {local_name(element.tag)}")
        for k, value in element.attrib.items():
            attr = local_name(k).lower()
            assert not attr.startswith("on"), f"event attribute in {path}"
            if attr in ("href", "src"):
                assert not value.startswith(("http:", "https:", "data:", "//")), (
                    f"external/embedded asset in {path}")
    return path


def main():
    files = sorted(FILES.glob("*.svg"))
    assert len(files) >= 6, f"expected at least six editable SVG diagrams, got {len(files)}"
    for path in files:
        validate_svg(path)
    print(f"SVG_SOURCE_STRUCTURE_PASS diagrams={len(files)} visual_qa=NOT_DONE")


if __name__ == "__main__":
    main()
