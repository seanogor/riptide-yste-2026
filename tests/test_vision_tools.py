import csv
import hashlib
import tempfile
import unittest
from pathlib import Path

from src.evaluate import evaluate_records
from src.prepare_dataset import split_rows, validate_rows


class VisionToolTests(unittest.TestCase):
    def test_split_is_deterministic_and_keeps_sequences_together(self):
        rows = [{"image_id": f"i{n}", "sequence_id": f"s{n // 2}"} for n in range(10)]
        first = split_rows([row.copy() for row in rows], seed=9)
        second = split_rows([row.copy() for row in rows], seed=9)
        self.assertEqual(first, second)
        locations = {row["sequence_id"]: split for split, values in first.items() for row in values}
        self.assertEqual(len(locations), 5)
        self.assertEqual(sum(len(values) for values in first.values()), 10)

    def test_validation_detects_duplicate_hash_and_sequence_leakage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "a.jpg"
            image.write_bytes(b"same")
            label = root / "a.txt"
            label.write_text("0 0.5 0.5 0.2 0.2\n", encoding="utf-8")
            rows = [
                {"image_id": "a", "image_path": "a.jpg", "label_path": "a.txt", "sequence_id": "seq", "label_status": "positive", "split": "train"},
                {"image_id": "b", "image_path": "a.jpg", "label_path": "a.txt", "sequence_id": "seq", "label_status": "positive", "split": "test"},
            ]
            errors = validate_rows(rows, root / "manifest.csv")
            self.assertTrue(any("duplicate image hash" in error for error in errors))
            self.assertTrue(any("sequence leakage" in error for error in errors))

    def test_metrics_match_boxes_and_count_misses(self):
        box = (0.4, 0.4, 0.6, 0.6, 0.9)
        result = evaluate_records([([box], [box]), ([], [box])])
        self.assertEqual(result["true_positive"], 1)
        self.assertEqual(result["false_negative"], 1)
        self.assertEqual(result["false_positive"], 0)
        self.assertEqual(result["precision"], 1.0)
        self.assertEqual(result["recall"], 0.5)


if __name__ == "__main__":
    unittest.main()
