#!/usr/bin/env python3
"""Reject sensitive file paths before commit."""

from __future__ import annotations

import fnmatch
import sys
from pathlib import Path


DENY_PATTERNS = (
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "*.p12",
    "*.pfx",
    "id_rsa",
    "id_rsa.*",
    "id_ed25519",
    "id_ed25519.*",
    "credentials.json",
    "token.txt",
    "*.token",
    "*.secret",
    "secrets.yml",
    "secrets.yaml",
)


def is_denied(path: str) -> bool:
    normalized = path.replace("\\", "/")
    name = Path(normalized).name
    return any(
        fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(normalized, pattern)
        for pattern in DENY_PATTERNS
    )


def main(argv: list[str]) -> int:
    blocked = [path for path in argv if is_denied(path)]
    if blocked:
        print("Sensitive file paths are not allowed:")
        for path in blocked:
            print(f"  - {path}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
