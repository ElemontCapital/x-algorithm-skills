#!/usr/bin/env python3
"""Validate plugin skill packaging without external dependencies."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\((\.{1,2}/[^)#]+)(?:#[^)]+)?\)")


def repo_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_repo_link(source_file: str, target: str) -> str:
    candidate = PurePosixPath(source_file).parent.joinpath(target)
    parts: list[str] = []
    for part in candidate.parts:
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                return str(candidate)
            parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def git_tracked_paths() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return {path for path in result.stdout.split("\0") if path}


def parse_frontmatter(markdown: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(markdown)
    if not match:
        return {}

    lines = match.group(1).splitlines()
    fields: dict[str, str] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith((" ", "\t")):
            index += 1
            continue
        field = FIELD_RE.match(line)
        if not field:
            index += 1
            continue

        key, raw_value = field.group(1), field.group(2).strip()
        if raw_value in {"|", "|-", "|+", ">", ">-", ">+"}:
            index += 1
            block_lines: list[str] = []
            while index < len(lines):
                next_line = lines[index]
                if not next_line.startswith((" ", "\t")) and FIELD_RE.match(next_line):
                    break
                block_lines.append(next_line.strip())
                index += 1
            fields[key] = "\n".join(line for line in block_lines if line).strip()
            continue

        fields[key] = raw_value.strip("\"'")
        index += 1
    return fields


def main() -> int:
    errors: list[str] = []
    tracked = git_tracked_paths()
    plugin_files = sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json"))

    if not plugin_files:
        errors.append("No plugin manifests found under plugins/*/.claude-plugin/plugin.json")

    for plugin_file in plugin_files:
        plugin_rel = repo_path(plugin_file)
        plugin_root = plugin_file.parents[1]
        manifest = json.loads(plugin_file.read_text(encoding="utf-8"))
        skills = manifest.get("skills")
        if not isinstance(skills, list) or not skills:
            errors.append(f"{plugin_rel}: expected a non-empty skills array")
            continue

        for skill_entry in skills:
            if not isinstance(skill_entry, str):
                errors.append(f"{plugin_rel}: skill entry is not a string: {skill_entry!r}")
                continue

            skill_dir = (plugin_root / skill_entry).resolve()
            try:
                skill_dir_rel = skill_dir.relative_to(ROOT).as_posix()
            except ValueError:
                errors.append(f"{plugin_rel}: skill path escapes repository: {skill_entry}")
                continue

            skill_file_rel = f"{skill_dir_rel}/SKILL.md"
            if skill_file_rel not in tracked:
                errors.append(f"{plugin_rel}: missing exact tracked file {skill_file_rel}")
                continue

            lowercase_skill = f"{skill_dir_rel}/skill.md"
            if lowercase_skill in tracked:
                errors.append(f"{plugin_rel}: lowercase skill file is not portable: {lowercase_skill}")

            skill_file = ROOT / skill_file_rel
            markdown = skill_file.read_text(encoding="utf-8")
            fields = parse_frontmatter(markdown)
            for required in ("name", "description"):
                if not fields.get(required):
                    errors.append(f"{skill_file_rel}: missing non-empty frontmatter field {required!r}")

            expected_name = PurePosixPath(skill_dir_rel).name
            if fields.get("name") and fields["name"] != expected_name:
                errors.append(
                    f"{skill_file_rel}: frontmatter name {fields['name']!r} does not match directory {expected_name!r}"
                )

            for target in LOCAL_LINK_RE.findall(markdown):
                target_rel = normalize_repo_link(skill_file_rel, target)
                if target_rel not in tracked:
                    errors.append(f"{skill_file_rel}: local link target is missing: {target}")

    if errors:
        print("Skill packaging validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill packaging validation passed for {len(plugin_files)} plugin manifest(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
