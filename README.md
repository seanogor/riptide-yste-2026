# Rip Current Vision

An open, safety-focused computer-vision project for detecting visual indicators of
rip currents in elevated beach imagery.

> **Research status:** proposal and project scaffold. No model has been trained
> and no safety-critical detection claims have been made.

## Research question

Can a lightweight, open-source object-detection model identify likely rip-current
channels in real time from standard beach-camera or drone imagery, and achieve a
mean average precision (mAP@0.5) of at least 80% on an unseen test set?

Rip currents are narrow, fast-moving channels that carry water away from shore.
They may be visible as gaps in breaking waves, differences in water color,
foam/churn patterns, or sediment plumes. A public-facing model would be an aid
for research and education, not a replacement for lifeguards, warning signage, or
local emergency guidance.

## Why this matters

Rip currents are a major beach-safety hazard. They generally pull swimmers away
from shore rather than under the surface, but a swimmer who fights the current
can become exhausted quickly. Earlier visual awareness can support safer decisions
and help researchers study where conditions change.

The project focuses on software and public imagery, which is safer and more
accessible than deploying physical sensors in rough surf.

## Proposed outcome

The first milestone is a documented baseline detector that:

- accepts a still image or an extracted video frame;
- returns zero or more `rip_current` bounding boxes with confidence scores;
- reports precision, recall, mAP@0.5, and a confusion matrix on a held-out test set;
- records failure cases across lighting, weather, geography, camera angle, and
  tide/surf conditions.

The success threshold is **mAP@0.5 >= 0.80 on the untouched test split**. This
threshold is a research target, not evidence that the system is safe for
operational rescue decisions.

## Research protocol

### Data

The target dataset is approximately 1,000–1,500 static surf-zone images, including
images with and without visible rip-current indicators. Sources may include
public-domain, Creative Commons, or explicitly open-access beach cameras and
drone datasets. Every source must be recorded in a manifest with its license,
URL, capture date (when available), location/coarse region, camera type, and
permission notes.

Images must not contain unnecessarily identifiable people. Do not collect private
camera feeds, bypass access controls, or scrape a service whose terms prohibit
reuse. Store source metadata and labels in the repository, but keep large image
files in an approved external artifact store when repository size requires it.

### Labels

Annotators draw a tight bounding box around a visually supported rip-current
channel or plume. Images where no current can be supported are labeled
`negative`; uncertain images are labeled `review` and excluded from the first
training run. A second reviewer with beach-safety or oceanography experience
should audit a sample of positive labels.

The canonical YOLO label format is:

```text
class_id center_x center_y width height
```

All coordinates are normalized to `[0, 1]`. The initial class map is:

```text
0 rip_current
```

### Splits and bias controls

Use a strict 70% train / 20% validation / 10% test split. Images from the same
video sequence, camera, or near-duplicate burst must stay in the same split to
prevent leakage. The test set is locked until model selection is complete.

The split should include varied:

- weather, visibility, and time of day;
- shore geometry, geographic region, and camera elevation;
- wave height, tide, and surf density;
- positive, negative, and difficult/ambiguous examples.

Training-only augmentation may include horizontal flips where geographically
appropriate, crops, scale changes, rotation within a physically plausible range,
and brightness/contrast changes. Never augment the validation or test sets.

### Model and analysis

Start with a small YOLO-family detector or comparable PyTorch model that can run
on a consumer GPU or a free hosted notebook. Compare the baseline against at
least one simpler model or ablation so improvements are measurable.

For each run, save the dataset version, split manifest, model configuration,
random seed, training environment, and metrics. Report precision, recall,
mAP@0.5, false positives per image, and representative successes/failures.
Inspect false positives caused by ordinary wave gaps, shadows, glare, boats,
shoreline geometry, or sediment that is not a rip current.

## Project plan

1. **Source and audit data:** collect the pilot set and record provenance before
   any training.
2. **Annotate and review:** draw boxes, mark negatives and uncertain examples,
   and perform a second-person quality audit.
3. **Version the split:** generate immutable train/validation/test manifests and
   check for duplicates or sequence leakage.
4. **Train a baseline:** run a small detector with documented hyperparameters
   and data augmentation.
5. **Evaluate once:** score the locked test set and publish the complete metric
   table, not only the best examples.
6. **Investigate limitations:** stratify errors by scene conditions and document
   when the detector should not be trusted.
7. **Present results:** show raw images beside annotated predictions and explain
   that the prototype is informational only.

## Expanded scope for Young Scientist 2027

The project is designed as a complete student research study rather than only a
model-training exercise. The expanded scope includes:

- a literature review that defines the visual and oceanographic basis for a
  rip-current label;
- a documented, license-safe dataset and annotation quality process;
- a reproducible baseline detector plus one comparison or ablation;
- an error and bias analysis that tests whether the model learned beach
  appearance instead of current behavior;
- a small offline demonstration that overlays predictions on saved images;
- a research paper, poster, source list, experiment log, and disclosure of
  limitations suitable for a school or Young Scientist submission.

The student should narrow the claim if time or data is limited. A valid result
can be that the baseline does not reach 80% mAP, provided the test split was
locked, the metrics are reported honestly, and the failure modes explain what
should improve next.

## Student timeline and submission plan

This schedule follows the **Stripe Young Scientist & Technology Exhibition
2027 (YSTE)** handbook supplied with this project. The exhibition runs
**6–9 January 2027 at the RDS Dublin**. The handbook's official deadlines
override any older planning dates below.

| Dates | Student deliverable | Exit check |
|---|---|---|
| Sep 7–27, 2026 | Confirm the research question, safety boundaries, mentor/teacher, judging rubric, and permitted data sources. Build the bibliography and research log. | One-page proposal approved; every source has a citation and license note. |
| Sep 28–Oct 25 | Collect and audit the 50-image pilot. Write the manifest, remove unusable sources, define positive/negative/review labels, and practice annotation on 20 images. | At least 20 reviewed pilot labels and a written annotation guide. |
| Oct 26–Nov 22 | Expand toward 300–500 images. Annotate in batches, run duplicate/near-duplicate checks, and ask a domain reviewer to audit a sample. | Pilot quality review complete; no known train/test leakage. |
| Nov 23–Dec 20 | Reach the 1,000–1,500-image target if feasible. Freeze provenance, create the 70/20/10 split, and lock the test manifest. | Dataset version 1.0 and immutable test list recorded in the log. |
| Dec 21, 2026–Jan 17, 2027 | Prepare the environment and train the first baseline. Save configuration, seed, package versions, checkpoints, and learning curves. | A repeatable baseline run can be reproduced from the run log. |
| Jan 18–Feb 14 | Tune only against training/validation data. Run one comparison or ablation, such as augmentation on/off or small versus medium model. | Model selection rule written before opening the test results. |
| Feb 15–28 | Evaluate the selected model once on the locked test set. Produce mAP, precision, recall, confusion matrix, false-positive examples, and condition breakdowns. | Results table and representative successes/failures exported. |
| Mar 1–14 | Interpret findings, interview or consult a qualified reviewer if available, document limitations, and decide whether the 80% target was met. | Claims match evidence; no operational safety claim is made. |
| Mar 15–31 | Write the paper and build the poster: question, hypothesis, methods, ethics, results, limitations, conclusion, and references. Recreate all figures from saved outputs. | Teacher/mentor review completed; citations and image licenses checked. |
| Apr 1–deadline | Submit the required forms, paper, poster, code link, data statement, and any school approval documents. Practice a three-minute explanation and judge questions. | Submission receipt saved; final archive is read-only and reproducible. |

### Handbook deadlines and exhibition actions

Use these fixed YSTE 2027 dates instead of the generic planning rows above:

- **25 September 2026, 5:00 pm:** student entry, project details, one-page
  proposal (maximum 500 words), and entry fee due.
- **28 September, 5:00 pm:** teacher assessment due.
- **23 October:** screening result available; **5 November:** signed confirmation
  card due if qualified.
- **11 December:** three-minute video due. Keep it under three minutes, use clear
  audio and visuals, and do not add music.
- **6 January 2027, 12:00 pm:** email the report-book PDF to
  `projectbook@yste.ie` with the stand number as the subject, bring two printed
  copies, and set up the diary, report book, and landscape display at the RDS.
- **6–8 January:** judging takes place; **9 January** is the final exhibition
  day. Keep the display within the handbook's 1,189 mm x 841 mm back panel and
  1,200 mm x 600 mm worktop.

The report book should include the handbook's title page, contents, one-page
abstract, introduction, literature review, methodology, results, discussion,
conclusion, references, and appendices. Its main body must be no more than 50
pages, excluding references and appendices. The project diary should document
planning, investigation, results, problems, learning, and exhibition
preparation.

### Minimum viable path

If the full dataset or 80% target is not achievable, submit a smaller but
rigorous pilot study: 300–500 carefully audited images, a baseline model, a
locked test set, and a transparent analysis of why more data or better labels
are needed. Do not change the test split or threshold after seeing the result.

### Final submission package

Keep these artifacts together in a dated release or archive:

1. research paper and one-page abstract;
2. poster or presentation slides with raw/predicted image pairs;
3. source manifest, license notes, annotation guide, and split manifests;
4. training configuration, evaluation metrics, plots, and error gallery;
5. code and environment instructions;
6. experiment log, safety statement, limitations, and contributor/mentor notes.

## Repository layout

```text
.
├── data/
│   └── README.md                 # provenance, storage, and split rules
├── docs/
│   ├── project-proposal.md       # entry-form-ready research narrative
│   └── timeline.md               # student schedule and submission checklist
├── src/
│   └── README.md                 # planned training and inference modules
├── README.md
└── LICENSE
```

The scaffold intentionally does not include images, credentials, scraped
content, or unverified model weights.

## Work completed and next steps

The initial work is a literature review and a pilot batch of about 50
open-source beach images. That pilot confirmed that resolution and annotation
time are practical constraints, so the plan includes data augmentation and a
staged annotation review.

Next, create the source manifest, resolve image licenses, annotate the pilot
set, and establish a leakage-free split before selecting a model.

## Safety and ethics

This project must not be used to direct swimmers, lifeguards, or emergency
responses. Predictions can be wrong, especially under unfamiliar conditions.
Users should follow lifeguard instructions, posted warnings, and local emergency
guidance. The project does not use human subjects, but any image containing
people must be handled with care and in accordance with its license and school
research requirements.

## Background sources

- [NOAA: Rip currents](https://oceanservice.noaa.gov/hazards/ripcurrents/)
- [United States Lifesaving Association: Rip currents](https://www.usla.org/rip-currents/)
- [NOAA Digital Coast](https://coast.noaa.gov/digitalcoast/)
- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)

All numerical claims used in a final report should be checked against the
current source text and cited with the relevant publication date.

## License

Code and documentation are provided under the MIT License. Third-party images,
annotations, and model weights retain their original licenses and must not be
redistributed without permission.
