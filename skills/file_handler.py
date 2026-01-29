"""File handling utilities."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path

__all__ = [
    "read_text",
    "write_text",
    "read_json",
    "write_json",
    "read_csv",
    "write_csv",
    "list_files",
]


def read_text(path: str | Path) -> str:
    """Read and return the full text content of a file."""
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str | Path, content: str) -> None:
    """Write text content to a file, creating parent directories if needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def read_json(path: str | Path) -> object:
    """Read and parse a JSON file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str | Path, data: object, indent: int = 2) -> None:
    """Write data to a JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)


def read_csv(path: str | Path) -> list[dict[str, str]]:
    """Read a CSV file and return a list of row dictionaries."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: str | Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
    """Write a list of dictionaries to a CSV file."""
    if not rows:
        return
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = fieldnames or list(rows[0].keys())
    with open(p, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def list_files(directory: str | Path, pattern: str = "*") -> list[Path]:
    """List files in a directory matching a glob pattern."""
    return sorted(Path(directory).glob(pattern))
