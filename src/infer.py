"""Run optional offline inference; never fabricates predictions."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--model", required=True, help="local model path understood by the selected backend")
    parser.add_argument("--output", type=Path, required=True, help="local output path for backend-rendered predictions")
    parser.add_argument("--confidence", type=float, default=0.25)
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f"image does not exist: {args.image}")
    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise SystemExit("No inference backend is installed. Install an approved local backend (for example ultralytics) and retry.") from exc
    if not Path(args.model).is_file():
        raise SystemExit(f"Model file does not exist: {args.model}")
    model = YOLO(args.model)
    results = model.predict(source=str(args.image), conf=args.confidence, save=True, project=str(args.output.parent), name=args.output.stem, exist_ok=True)
    if not results:
        raise SystemExit("Inference backend returned no result.")
    print(f"Saved offline prediction output under {args.output.parent / args.output.stem}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
