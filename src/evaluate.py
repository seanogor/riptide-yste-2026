"""Evaluate YOLO-format detections without requiring a ML framework."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_boxes(path: Path) -> list[tuple[float, float, float, float, float]]:
    boxes = []
    if not path.exists():
        raise FileNotFoundError(path)
    for line in path.read_text(encoding="utf-8").splitlines():
        fields = line.split()
        if not fields:
            continue
        if len(fields) not in (5, 6):
            raise ValueError(f"{path}: expected class + 4 coordinates, optionally confidence")
        values = [float(value) for value in fields]
        confidence = values[5] if len(values) == 6 else 1.0
        _, cx, cy, width, height = values[:5]
        boxes.append((cx - width / 2, cy - height / 2, cx + width / 2, cy + height / 2, confidence))
    return boxes


def iou(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    x1, y1 = max(left[0], right[0]), max(left[1], right[1])
    x2, y2 = min(left[2], right[2]), min(left[3], right[3])
    intersection = max(0.0, x2 - x1) * max(0.0, y2 - y1)
    area_left = max(0.0, left[2] - left[0]) * max(0.0, left[3] - left[1])
    area_right = max(0.0, right[2] - right[0]) * max(0.0, right[3] - right[1])
    union = area_left + area_right - intersection
    return intersection / union if union else 0.0


def evaluate_records(records: list[tuple[list[tuple[float, ...]], list[tuple[float, ...]]]], threshold: float = 0.5) -> dict:
    true_positive = false_positive = false_negative = 0
    scored: list[tuple[float, int]] = []
    total_truth = 0
    for predictions, truths in records:
        total_truth += len(truths)
        matched: set[int] = set()
        for prediction in sorted(predictions, key=lambda box: box[4], reverse=True):
            candidates = [(iou(prediction, truth), index) for index, truth in enumerate(truths) if index not in matched]
            best = max(candidates, default=(0.0, -1))
            is_match = best[0] >= threshold
            scored.append((prediction[4], int(is_match)))
            if is_match:
                true_positive += 1
                matched.add(best[1])
            else:
                false_positive += 1
        false_negative += len(truths) - len(matched)
    scored.sort(reverse=True)
    hits = 0
    ap_area = 0.0
    for rank, (_, is_hit) in enumerate(scored, 1):
        hits += is_hit
        precision = hits / rank
        recall = hits / total_truth if total_truth else 0.0
        if is_hit:
            ap_area += precision / total_truth if total_truth else 0.0
    return {
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "precision": true_positive / (true_positive + false_positive) if true_positive + false_positive else 0.0,
        "recall": true_positive / total_truth if total_truth else 0.0,
        "ap50": ap_area,
        "iou_threshold": threshold,
        "metric_note": "AP is the dependency-free ranked one-to-one interpolated-area approximation at the requested IoU threshold.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--labels", type=Path, required=True, help="directory of ground-truth YOLO .txt files")
    parser.add_argument("--predictions", type=Path, required=True, help="directory of prediction YOLO .txt files")
    parser.add_argument("--output", type=Path, required=True, help="JSON output path")
    parser.add_argument("--csv-output", type=Path)
    parser.add_argument("--iou", type=float, default=0.5)
    args = parser.parse_args()
    if not 0 < args.iou <= 1:
        parser.error("--iou must be in (0, 1]")
    names = sorted({path.name for path in args.labels.glob("*.txt")} | {path.name for path in args.predictions.glob("*.txt")})
    records = []
    for name in names:
        prediction_path = args.predictions / name
        label_path = args.labels / name
        predictions = read_boxes(prediction_path) if prediction_path.exists() else []
        truths = read_boxes(label_path) if label_path.exists() else []
        records.append((predictions, truths))
    metrics = evaluate_records(records, args.iou)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    if args.csv_output:
        with args.csv_output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=metrics)
            writer.writeheader()
            writer.writerow(metrics)
    print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
