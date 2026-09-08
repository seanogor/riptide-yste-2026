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

## Young Scientist 2027 implementation and submission timeline

The following schedule follows the supplied **Stripe Young Scientist &
Technology Exhibition 2027 (YSTE)** handbook. The exhibition is at RDS Dublin
from **6–9 January 2027**. The handbook's official deadlines take precedence.

| Phase | Dates | Deliverables |
|---|---|---|
| Student entry | Sep 7–25, 2026 | Title (maximum 100 characters), project details, one-page proposal (maximum 500 words), online student application, and entry fee submitted by **25 Sep, 5:00 pm**. |
| Teacher assessment | Sep 26–28 | Teacher confirms category and age group and submits assessment by **28 Sep, 5:00 pm**. |
| Pilot and label design | Sep 29–Oct 22 | 50-image audit, annotation guide, label examples, provenance manifest, and 20-image practice set. |
| Screening and acceptance | Oct 23–Nov 5 | Check results by **23 Oct**; if qualified, return the signed confirmation card by **5 Nov**. |
| Dataset construction | Nov 6–Dec 4 | 1,000–1,500 images where feasible, reviewed annotations, duplicate check, licence evidence, and frozen 70/20/10 split. |
| Video submission | Dec 5–11 | Record a clear video under three minutes and upload it by **11 Dec** in an accepted format. |
| Baseline, report, and display | Dec 12–Jan 2, 2027 | Reproducible runs, locked evaluation, report book, project diary, landscape display, references, and safety disclosure. |
| Exhibition preparation | Jan 3–5 | Email the report-book PDF to `projectbook@yste.ie` with the stand number as subject before **6 Jan 2027, 12:00 pm**; print two copies and pack the diary/display. |
| Exhibition | Jan 6–9, 2027 | Set up at the RDS Dublin by **6 Jan, 12:00 pm**; judging runs 6 Jan 3–6 pm, 7 Jan 9 am–1 pm and 2–6 pm, and 8 Jan 9 am–12 pm if needed. |

### Required YSTE artifacts

The handbook requires four exhibition elements:

1. **Project report book:** title page, contents, one-page abstract,
   introduction, literature review, methodology, results, discussion,
   conclusion, references, and appendices. The main body excluding references
   and appendices must not exceed 50 pages. Email a PDF and bring two printed
   copies.
2. **Project diary:** record the idea, planning, investigation, results,
   problems solved, learning, exhibition preparation, conclusion, and
   supporting references.
3. **Three-minute video:** keep it under three minutes, explain the goal,
   methods, and findings clearly, use good audio and visuals, and submit without
   music by 11 December 2026.
4. **Visual display:** use a landscape layout and keep materials inside the
   1,189 mm x 841 mm back panel and 1,200 mm x 600 mm worktop. Include concise
   question, method, results, discussion, references, and safety wording.

### Weekly student workflow

Reserve two short sessions each week: one for research or annotation and one
for coding, analysis, or writing. End each week by recording what changed,
which data or code version was used, what failed, and the next decision. Keep
the test set inaccessible during model development. Back up the manifest,
experiment log, and final figures in two locations.

### Decision gates and submission actions

- **Before 25 September:** proofread the title and one-page proposal, submit
  the student entry by 5:00 pm, and confirm the teacher's 28 September
  assessment.
- **By 23 October:** check the screening outcome. If qualified, collect the
  required signatures and return the confirmation card by 5 November.
- **By 11 December:** finish and upload the under-three-minute video.
- **By 6 January at noon:** email the report book PDF with the stand number,
  bring two printed copies, and prepare the diary and display for setup.

- **End of October:** stop collecting a source if its licence or provenance
  cannot be verified.
- **End of December:** if fewer than 1,000 usable images are available, adopt
  the minimum viable pilot path and state that limitation.
- **Before test evaluation:** write the model-selection rule and freeze the
  test manifest.
- **After test evaluation:** report the actual result, including a miss of the
  80% target; never retune against the test set.
- **Before the exhibition:** have a teacher or mentor check citations,
  licensing, safety language, report-page count, video length, display
  dimensions, and that every conclusion is supported by a recorded metric.

The project is successful as student research if the process is reproducible and
the conclusion is honest, whether or not the model reaches the target metric.
