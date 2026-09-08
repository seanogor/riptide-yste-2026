# Implementation plan

The first implementation should keep training and inference reproducible:

```text
src/
├── prepare_dataset.py   # validate manifests, detect duplicates, create splits
├── train.py             # train the documented baseline
├── evaluate.py          # score the locked test set and export metrics
└── infer.py             # draw predictions for a single image or frame
```

Before adding model code, define command-line arguments for the dataset
manifest, output directory, random seed, model configuration, and confidence
threshold. Each run should write its configuration and package versions beside
the metrics. A later implementation can use a YOLO-family library, but model
choice must remain recorded in the experiment metadata rather than hidden in a
notebook.
