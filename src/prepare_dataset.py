"""Validate a dataset manifest and create leakage-safe deterministic splits."""

from __future__ import annotations

import argparse
import csv
import hashlib
import random
from collections import defaultdict
from pathlib import Path
from typing import Iterable

REQUIRED_COLUMNS = {
    "image_id",
    "image_path",
    "label_path",
    "sequence_id",
    "label_status",
}
SPLITS = ("train", "val", "test")


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or ())
        missing = REQUIRED_COLUMNS - columns
        if missing:
            raise ValueError(f"manifest is missing required columns: {sorted(missing)}")
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    if not rows:
        raise ValueError("manifest contains no rows")
    return rows


def _resolve(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path


def validate_yolo_file(path: Path) -> None:
    if not path.exists():
        raise ValueError(f"missing label file: {path}")
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fields = line.split()
        if not fields:
            continue
        if len(fields) != 5:
            raise ValueError(f"{path}:{line_number}: expected 5 YOLO fields")
        try:
            class_id = int(fields[0])
            values = [float(value) for value in fields[1:]]
        except ValueError as exc:
            raise ValueError(f"{path}:{line_number}: fields must be numeric") from exc
        if class_id != 0 or any(value < 0 or value > 1 for value in values):
            raise ValueError(f"{path}:{line_number}: class must be 0 and coordinates in [0, 1]")
        if values[2] <= 0 or values[3] <= 0:
            raise ValueError(f"{path}:{line_number}: box width and height must be positive")


def validate_rows(rows: list[dict[str, str]], manifest_path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    hashes: dict[str, str] = {}
    sequences: dict[str, str] = {}
    base = manifest_path.parent
    for row in rows:
        image_id = row["image_id"]
        if not image_id or image_id in seen_ids:
            errors.append(f"duplicate or empty image_id: {image_id!r}")
        seen_ids.add(image_id)
        sequence = row["sequence_id"]
        if not sequence:
            errors.append(f"{image_id}: sequence_id is required")
        image = _resolve(base, row["image_path"])
        label = _resolve(base, row["label_path"])
        if not image.is_file():
            errors.append(f"{image_id}: missing image: {image}")
            continue
        try:
            validate_yolo_file(label)
        except ValueError as exc:
            errors.append(str(exc))
        digest = hashlib.sha256(image.read_bytes()).hexdigest()
        if digest in hashes:
            errors.append(f"duplicate image hash: {image_id} and {hashes[digest]}")
        hashes[digest] = image_id
        if "split" in row and row["split"] in SPLITS:
            previous = sequences.setdefault(sequence, row["split"])
            if previous != row["split"]:
                errors.append(f"sequence leakage: {sequence} appears in {previous} and {row['split']}")
    return errors


def split_rows(rows: list[dict[str, str]], seed: int = 42) -> dict[str, list[dict[str, str]]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row["sequence_id"]].append(row)
    ordered = list(groups)
    random.Random(seed).shuffle(ordered)
    targets = {"train": round(len(rows) * 0.7), "val": round(len(rows) * 0.2)}
    targets["test"] = len(rows) - targets["train"] - targets["val"]
    result = {split: [] for split in SPLITS}
    for sequence in ordered:
        destination = min(SPLITS, key=lambda split: (len(result[split]) >= targets[split], len(result[split])))
        result[destination].extend(groups[sequence])
    for split, split_rows_ in result.items():
        for row in split_rows_:
            row["split"] = split
    return result


def write_split_files(splits: dict[str, list[dict[str, str]]], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    fields = list(splits[next(iter(splits))][0])
    if "split" not in fields:
        fields.append("split")
    for split, rows in splits.items():
        with (output / f"{split}.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    rows = read_manifest(args.manifest)
    errors = validate_rows(rows, args.manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    write_split_files(split_rows(rows, args.seed), args.output)
    print(f"Validated {len(rows)} images; wrote train/val/test manifests to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
