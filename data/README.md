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
│   ├── images.csv
│   ├── train.txt
│   ├── val.txt
│   └── test.txt
└── labels/
    └── <image_id>.txt
```

YOLO label files contain one normalized row per box:

```text
0 center_x center_y width height
```

The only initial class is `0 rip_current`. Keep original source attribution and
license evidence outside the label files so annotations remain tool-compatible.
