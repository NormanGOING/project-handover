#!/usr/bin/env python3
"""Validate the skill repository before publishing."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "SKILL.md",
    "SKILL.zh-CN.md",
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "agents/openai.yaml",
    "references/handover-template.md",
    "references/handover-template.zh-CN.md",
    "references/domain-checklists.md",
    "references/domain-checklists.zh-CN.md",
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ABSOLUTE_RE = re.compile(r"(?:[A-Za-z]:\\Users\\|/Users/|/home/|AppData[\\/])")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("\"'")
    return data


def markdown_links(text: str):
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield from LINK_RE.findall(line)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    skill = ROOT / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("name") != ROOT.name:
            errors.append(
                f"SKILL.md name must be {ROOT.name!r}, got {meta.get('name')!r}"
            )
        if not meta.get("description"):
            errors.append("SKILL.md description is missing")
        if re.search(r"\bTODO\b|\bFIXME\b|\bTBD\b", text):
            errors.append("SKILL.md still contains TODO/FIXME/TBD")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for md in markdown_files:
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for target in markdown_links(text):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (md.parent / target).resolve().exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")
        if ABSOLUTE_RE.search(text):
            errors.append(f"{md.relative_to(ROOT)}: contains an absolute local path")

    for config in sorted(ROOT.rglob("*.yaml")):
        if ".git" in config.parts:
            continue
        if ABSOLUTE_RE.search(config.read_text(encoding="utf-8")):
            errors.append(f"{config.relative_to(ROOT)}: contains an absolute local path")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {len(markdown_files)} Markdown files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
