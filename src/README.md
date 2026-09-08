# Offline tooling

The first working slice is dependency-free Python (3.9+) except for the optional
inference backend:

```powershell
python src/prepare_dataset.py data/manifests/images.csv --output data/manifests/splits --seed 42
python src/evaluate.py --labels data/labels --predictions runs/predictions --output runs/metrics.json --csv-output runs/metrics.csv
python src/infer.py path\to\image.jpg --model path\to\local-model.pt --output runs\demo
```

The manifest must contain `image_id`, `image_path`, `label_path`, `sequence_id`,
and `label_status`. Image paths and label paths are resolved relative to the
manifest. Labels use one class (`0`) and normalized YOLO coordinates. Validation
checks missing files, malformed boxes, duplicate SHA-256 image content, and
sequence IDs assigned to more than one existing split. New splits group complete
sequences and use a fixed seed.

Evaluation reads one YOLO text file per image from each directory. Prediction
rows have `class center_x center_y width height confidence`; label rows omit
confidence. It reports confusion counts, precision, recall, and AP at the
requested IoU threshold. AP is deliberately documented as a dependency-free
ranked one-to-one approximation, not a claim of equivalence to every framework's
COCO implementation.

`infer.py` is offline-only and requires a locally installed backend and local
model. It fails clearly when Ultralytics or the model is unavailable; it never
returns a fabricated result. Predictions are research aids, not instructions for
swimmers, lifeguards, or emergency response. Follow local warnings and qualified
lifeguard guidance.
