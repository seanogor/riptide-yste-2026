# Dataset protocol

This directory is for small manifests and documentation. Do not commit scraped
images, private camera content, credentials, or files whose license does not
permit redistribution.

## Required manifest fields

Each image record should include:

```text
image_id, source_url, license, capture_date, coarse_region,
camera_type, sequence_id, label_status, split
```

Use a stable `image_id` rather than a source filename. `sequence_id` is required
to keep adjacent video frames or burst captures in one split.

## Label status

- `positive`: a reviewer supports at least one visible rip-current box;
- `negative`: the image was reviewed and no current is supported;
- `review`: ambiguous or awaiting domain review.

Do not train on `review` records. Keep the test manifest immutable after model
selection begins.

## Suggested layout

```text
data/
├── manifests/
│   ├── images-template.csv
│   ├── images.csv
│   ├── train.txt
│   ├── val.txt
│   └── test.txt
└── labels/
    └── <image_id>.txt
```

Use `images-template.csv` as the starter template before collecting or curating
real sources. It contains only the column headings; do not treat fabricated
example URLs, licences, labels, or split assignments as data.

`training_log.csv` records the assistant's historical image assessments and
student corrections. It is a project learning record, not a verified image
dataset or ground truth. The original images were not recovered into this
repository, so these records must not be used for detector training or evaluation.

## Assistant image-training protocol

During guided image review, analyse only images supplied by the student or
already present in the project dataset. Do not search the web, open the image's
source page, reverse-search it, or consult external labels to decide whether it
shows a rip current. Follow `docs/assistant-training-protocol.md` for the
assessment format, correction loop, and uncertainty rules.

YOLO label files contain one normalized row per box:

```text
0 center_x center_y width height
```

The only initial class is `0 rip_current`. Keep original source attribution and
license evidence outside the label files so annotations remain tool-compatible.
