# Rip Current Vision: research proposal

## Research question and outcome

Rip currents are dangerous channels of water that many beachgoers do not
recognize before entering the surf. This project asks whether a lightweight,
open-source convolutional or YOLO-family object detector can identify their
visual indicators in real time from elevated beach-camera and drone imagery.

The visual targets are gaps in breaking waves, churned foam, discolored water,
and sediment plumes. The proposed outcome is a prototype that highlights likely
rip-current regions and reports confidence, precision, recall, and mAP@0.5.
The target is at least 80% mAP@0.5 on a held-out test set.

This is an educational research prototype. It is not a warning system or a
substitute for trained lifeguards.

## Background research

The project will use NOAA oceanographic and coastal-safety material, United
States Lifesaving Association guidance and statistics, and peer-reviewed
computer-vision literature on object detection and optical-flow methods.

The working hypothesis is that rip currents have recurring visual profiles that
can be learned from labeled imagery, but the model may confuse ordinary wave
gaps, glare, shadows, sediment, and shoreline structures with a current.

## Methods

The study will:

1. collect approximately 1,000–1,500 legally reusable surf-zone images;
2. record provenance, camera conditions, and coarse geography in a manifest;
3. annotate visible rip-current channels with bounding boxes;
4. label negative and uncertain examples separately;
5. split the data 70%/20%/10% into train, validation, and locked test sets;
6. train a small YOLO-family baseline using training-only augmentation;
7. evaluate on unseen images using precision, recall, mAP@0.5, false positives
   per image, and a confusion matrix;
8. stratify errors by weather, lighting, camera angle, geography, and surf state.

Images from the same sequence or camera burst must never cross split boundaries.
At least one domain reviewer should audit a sample of positive annotations.

## Resources and feasibility

The implementation uses Python, PyTorch or an equivalent ML framework, a YOLO
implementation, an annotation tool, and Google Colab or another approved
GPU-enabled environment. The planned tooling is open-source or has a free tier.
No physical sensors, boats, or field deployment are required.

## Work completed

A preliminary literature review and a pilot batch of approximately 50 open-source
beach images have been collected. The pilot showed that image resolution affects
visual clarity and that manual annotation is time-consuming. The plan therefore
includes augmentation, staged review, and a documented provenance manifest.

## Limitations and risk controls

The model may perform poorly on storm conditions, unfamiliar beaches, unusual
camera elevations, low-resolution feeds, or scenes without a visible surface
signature. A high test score cannot establish operational safety. The final
report must include failure examples, dataset composition, licensing decisions,
and an explicit non-deployment statement.

Only public-domain, Creative Commons, or explicitly open-access media should be
used. No private feeds should be accessed, and people should not be identified.
Any proposed public demonstration should use pre-recorded images rather than
live rescue decisions.

## Presentation

Results will be shown with side-by-side raw images and model predictions,
precision-recall curves, a confusion matrix, and a table of errors by condition.
Feedback from a computer-science teacher can support implementation, while a
lifeguard or coastal-safety professional can review whether annotations are
plausible.
