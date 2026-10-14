#!/usr/bin/env python3
"""
Validate labels.csv (and its provenance manifest) before training.

    python validate_dataset.py
    python validate_dataset.py --data labels.csv --manifest data/source_manifest.csv --min-rows 200

Checks the things the brief and the notebook care about: shape, empty text,
valid labels, duplicates (exact and normalised), the 70% cap, class sizes, and
that every row can be traced back to a source post. Prints a summary and exits
non-zero if anything that would break or quietly spoil a training run is found.
Warnings (small classes, near-duplicates) do not fail the run; they are printed.
"""
import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except (AttributeError, OSError, ValueError):
        pass

LABELS = ("question", "report", "take")
CAP = 0.70


def text_hash(text: str) -> str:
    """Stable id for a row: sha1 of the exact text. Used by the manifest."""
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


def normalise(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="labels.csv")
    ap.add_argument("--manifest", default="data/source_manifest.csv")
    ap.add_argument("--min-rows", type=int, default=200)
    ap.add_argument("--small-class", type=int, default=50,
                    help="warn when a label has fewer rows than this")
    args = ap.parse_args()

    problems, warnings = [], []

    path = Path(args.data)
    if not path.exists():
        print(f"[FAIL] {path} not found")
        return 1
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        columns = reader.fieldnames or []
        rows = list(reader)

    if columns != ["text", "label", "note"]:
        problems.append(f"columns are {columns}; the notebook expects exactly ['text', 'label', 'note']")

    n = len(rows)
    print(f"{path}: {n} rows, columns {columns}")

    if n < args.min_rows:
        problems.append(f"only {n} rows; the brief asks for at least {args.min_rows}")

    empty = [i for i, r in enumerate(rows, 2) if not (r.get("text") or "").strip()]
    if empty:
        problems.append(f"{len(empty)} rows with empty text (csv lines {empty[:5]}{'...' if len(empty) > 5 else ''})")

    missing_label = [i for i, r in enumerate(rows, 2) if not (r.get("label") or "").strip()]
    if missing_label:
        problems.append(f"{len(missing_label)} rows with no label (csv lines {missing_label[:5]})")

    bad = Counter((r.get("label") or "").strip() for r in rows if (r.get("label") or "").strip() not in LABELS)
    bad.pop("", None)
    if bad:
        problems.append(f"labels not in {LABELS}: {dict(bad)}")

    texts = [r["text"] for r in rows]
    dup_exact = n - len(set(texts))
    if dup_exact:
        problems.append(f"{dup_exact} exact duplicate texts")

    norm_counts = Counter(normalise(t) for t in texts)
    dup_norm = sum(c - 1 for c in norm_counts.values() if c > 1) - dup_exact
    if dup_norm > 0:
        warnings.append(f"{dup_norm} additional near-duplicate texts (same after lower-casing and stripping punctuation)")

    # cheap near-duplicate check: same first 200 normalised characters
    prefix_counts = Counter(normalise(t)[:200] for t in texts)
    dup_prefix = sum(c - 1 for c in prefix_counts.values() if c > 1) - dup_exact - max(dup_norm, 0)
    if dup_prefix > 0:
        warnings.append(f"{dup_prefix} pairs share their first 200 normalised characters; check for crossposts")

    counts = Counter((r.get("label") or "").strip() for r in rows)
    print("\nPer label:")
    for label in LABELS:
        c = counts.get(label, 0)
        share = c / n if n else 0
        flag = ""
        if share > CAP:
            problems.append(f"'{label}' is {share:.0%} of the data; the cap is {CAP:.0%}")
            flag = "  <-- over cap"
        elif share > 0.60:
            warnings.append(f"'{label}' is {share:.0%} of the data; getting lopsided")
            flag = "  <-- over 60%"
        if c < args.small_class:
            warnings.append(f"only {c} '{label}' rows: about {round(c * 0.15)} will land in a 15% test split")
        print(f"  {label:<10} {c:>4}  {share:6.1%}{flag}")
    print(f"  {'total':<10} {n:>4}  100.0%")

    notes = Counter()
    for r in rows:
        note = (r.get("note") or "").strip()
        notes["cold" if note == "cold" else ("ai_prelabel" if note.startswith("ai_prelabel") else "other")] += 1
    print(f"\nNotes: {dict(notes)}")

    # provenance
    mpath = Path(args.manifest)
    if not mpath.exists():
        warnings.append(f"no manifest at {mpath}; provenance not checked")
    else:
        with mpath.open(encoding="utf-8", newline="") as fh:
            man = list(csv.DictReader(fh))
        by_hash = {m["text_hash"]: m for m in man if m.get("text_hash")}
        untraced = [i for i, t in enumerate(texts, 2) if text_hash(t) not in by_hash]
        if untraced:
            problems.append(f"{len(untraced)} rows have no manifest entry matching their text hash (csv lines {untraced[:5]})")
        ids = Counter(m.get("post_id") for m in man if m.get("in_labels_csv", "yes") == "yes")
        dup_ids = {k: v for k, v in ids.items() if v > 1}
        if dup_ids:
            problems.append(f"duplicate post ids in manifest rows marked in_labels_csv: {dup_ids}")
        print(f"Manifest: {len(man)} rows; {n - len(untraced)} of {n} dataset rows traced to a post id")

    print()
    for w in warnings:
        print(f"[look at]  {w}")
    for p in problems:
        print(f"[FIX ME]   {p}")
    if problems:
        print("\nNot ready: fix the [FIX ME] lines.")
        return 1
    print("\nDataset passes every hard check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
