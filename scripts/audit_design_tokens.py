#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/audit_design_tokens.py

Audits styling migration progress across app/ and components/:
counts hardcoded hex classes ([#...]), legacy cyber-/nature-/glow/blur-3xl
classes, and raw dark: utility prefixes.
"""

import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

PATTERNS = {
    "hardcoded_hex": re.compile(r"\[#[0-9a-fA-F]{3,8}\]"),
    "cyber_or_glow": re.compile(r"cyber-|glow-cyan|glow-emerald|shadow-glow"),
    "nature_token": re.compile(r"\bnature-"),
    "blur_3xl": re.compile(r"blur-3xl"),
    "dark_prefix": re.compile(r"\bdark:"),
}


def main() -> int:
    files = sorted(
        p
        for folder in ("app", "components")
        for p in (REPO_ROOT / folder).rglob("*.tsx")
    )
    totals = {k: 0 for k in PATTERNS}

    for f in files:
        txt = f.read_text(encoding="utf-8")
        for k, pat in PATTERNS.items():
            totals[k] += len(pat.findall(txt))

    print(f"Scanned {len(files)} TSX files:")
    for k, count in totals.items():
        print(f"  - {k}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
