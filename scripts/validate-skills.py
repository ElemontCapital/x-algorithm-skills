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
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


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


def normalize_repo_root_path(target: str) -> str | None:
    target = target.strip().replace("\\", "/")
    if not target or target.startswith(("/", "//")) or SCHEME_RE.match(target):
        return None

    parts: list[str] = []
    for part in PurePosixPath(target).parts:
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                return None
            parts.pop()
            continue
        parts.append(part)
    return "/".join(parts) or None


def markdown_local_link(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target:
        return None

    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split()[0]

    target = target.strip()
    if not target or target.startswith(("#", "/", "//")) or SCHEME_RE.match(target):
        return None

    target = target.split("#", 1)[0]
    return target or None


def local_links(markdown: str) -> list[str]:
    links: list[str] = []
    for raw_target in MARKDOWN_LINK_RE.findall(markdown):
        target = markdown_local_link(raw_target)
        if target:
            links.append(target)
    return links


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


def read_json_object(path: Path, errors: list[str]) -> dict[str, object] | None:
    path_rel = repo_path(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path_rel}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return None
    except OSError as exc:
        errors.append(f"{path_rel}: cannot read JSON: {exc}")
        return None

    if not isinstance(data, dict):
        errors.append(f"{path_rel}: expected a JSON object")
        return None
    return data


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


def validate_marketplace_manifest(
    tracked: set[str], plugin_files: list[Path], errors: list[str]
) -> None:
    marketplace_rel = ".claude-plugin/marketplace.json"
    marketplace_file = ROOT / marketplace_rel

    if marketplace_rel not in tracked:
        errors.append(f"Missing tracked marketplace manifest {marketplace_rel}")
        return
    if not marketplace_file.exists():
        errors.append(f"{marketplace_rel}: tracked marketplace manifest is missing on disk")
        return

    marketplace = read_json_object(marketplace_file, errors)
    if marketplace is None:
        return

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(f"{marketplace_rel}: expected a non-empty plugins array")
        return

    listed_plugin_files: set[str] = set()
    for index, entry in enumerate(plugins):
        entry_rel = f"{marketplace_rel}: plugins[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{entry_rel}: expected an object")
            continue

        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{entry_rel}: expected a non-empty name")
            name = None

        source = entry.get("source")
        if not isinstance(source, str) or not source.strip():
            errors.append(f"{entry_rel}: expected a non-empty source")
            continue

        source_rel = normalize_repo_root_path(source)
        if source_rel is None:
            errors.append(f"{entry_rel}: source must be a repository-local path: {source}")
            continue

        plugin_file_rel = f"{source_rel}/.claude-plugin/plugin.json"
        plugin_file = ROOT / plugin_file_rel
        if plugin_file_rel not in tracked:
            errors.append(f"{entry_rel}: source does not contain a tracked plugin manifest: {source}")
            continue
        if not plugin_file.exists():
            errors.append(f"{entry_rel}: source plugin manifest is missing on disk: {source}")
            continue

        listed_plugin_files.add(plugin_file_rel)
        plugin_manifest = read_json_object(plugin_file, errors)
        if plugin_manifest is not None and name is not None and plugin_manifest.get("name") != name:
            errors.append(
                f"{entry_rel}: name {name!r} does not match {plugin_file_rel} name "
                f"{plugin_manifest.get('name')!r}"
            )

    for plugin_file in sorted(repo_path(path) for path in plugin_files):
        if plugin_file not in listed_plugin_files:
            errors.append(f"{plugin_file}: plugin manifest is not listed in {marketplace_rel}")


def main() -> int:
    errors: list[str] = []
    tracked = git_tracked_paths()
    plugin_files = sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json"))

    if not plugin_files:
        errors.append("No plugin manifests found under plugins/*/.claude-plugin/plugin.json")

    validate_marketplace_manifest(tracked, plugin_files, errors)

    for plugin_file in plugin_files:
        plugin_rel = repo_path(plugin_file)
        plugin_root = plugin_file.parents[1]
        manifest = read_json_object(plugin_file, errors)
        if manifest is None:
            continue

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
            if not skill_file.exists():
                errors.append(f"{plugin_rel}: tracked skill file is missing on disk: {skill_file_rel}")
                continue

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

            markdown_file_rels = sorted(
                path
                for path in tracked
                if path == skill_file_rel or (path.startswith(f"{skill_dir_rel}/") and path.endswith(".md"))
            )
            for markdown_rel in markdown_file_rels:
                markdown_file = ROOT / markdown_rel
                if not markdown_file.exists():
                    errors.append(f"{markdown_rel}: tracked markdown file is missing on disk")
                    continue
                markdown_text = markdown_file.read_text(encoding="utf-8")
                for target in local_links(markdown_text):
                    target_rel = normalize_repo_link(markdown_rel, target)
                    target_path = (ROOT / target_rel).resolve()
                    try:
                        target_path.relative_to(ROOT)
                    except ValueError:
                        errors.append(f"{markdown_rel}: local link target escapes repository: {target}")
                        continue

                    if not target_rel.startswith(f"{skill_dir_rel}/"):
                        errors.append(f"{markdown_rel}: local link target leaves skill package: {target}")
                        continue

                    if target_rel not in tracked:
                        errors.append(f"{markdown_rel}: local link target is not tracked: {target}")
                        continue

                    if not target_path.exists():
                        errors.append(f"{markdown_rel}: local link target is missing on disk: {target}")

    if errors:
        print("Skill packaging validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill packaging validation passed for {len(plugin_files)} plugin manifest(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
