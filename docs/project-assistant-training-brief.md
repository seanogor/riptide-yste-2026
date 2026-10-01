# Project assistant training brief

## 1. Mission and safety boundary

This is an educational Young Scientist & Technology Exhibition (YSTE) research
project: investigate whether a small, open-source computer-vision detector can
identify **visible indicators of likely rip currents** in elevated beach
imagery. The intended output is an offline prototype that draws candidate
bounding boxes and reports confidence and test metrics.

The prototype is **not** a lifeguard, warning system, rescue tool, medical or
emergency service, or substitute for official beach signs, local authorities,
or trained coastal-safety professionals. It must not be used to direct a
swimmer, initiate a rescue, or make a live safety decision. Demonstrations
should use saved images or video frames, not live operational deployment.
Never imply that a high score proves safety, generalises to every beach, or
detects every rip current. If evidence is missing, say so.

## 2. Scientific background and visual cues

A rip current is a narrow, fast-moving channel in the surf zone that carries
water away from shore. Useful visible cues can include:

- a narrow darker, foamier, calmer, or discoloured channel;
- a break in the line of breaking waves;
- foam, sand, seaweed, or debris moving offshore in a narrow plume; and
- a channel through a sandbar or nearshore region.

These cues are not proof by themselves. Ordinary wave gaps, backwash, shadows,
glare, sediment, sandbars, shoreline geometry, boats, and dark deep water can
look similar. Visibility depends on viewpoint, resolution, light, weather,
tide, surf state, and geography. The assistant must distinguish “visible visual
pattern” from “confirmed oceanographic current.”

## 3. Data collection and annotation rules

Use only public-domain, Creative Commons, or explicitly open-access sources
whose reuse is permitted. Do not access private feeds, bypass controls, scrape
prohibited services, or unnecessarily identify people. Record each image in a
manifest with a stable `image_id`, source URL, licence, capture date when
available, coarse region, camera type, `sequence_id`, label status, and split.
Keep provenance and licence evidence with the project.

Use only these label statuses:

- `positive`: a reviewer supports at least one visible rip-current channel or
  plume;
- `negative`: the image was reviewed and no rip current is supported; and
- `review`: ambiguous, obscured, too distant, too dark, or otherwise needing
  further review.

Do not train on `review` records or force uncertainty into positive/negative.
For a positive, draw one tight box around the strongest visible current feature,
not the whole beach or surf zone. YOLO labels use class `0 rip_current` and
normalised `center_x center_y width height` coordinates in `[0, 1]`. A second
reviewer should audit positives and difficult cases; record disagreements and
update the guide rather than silently resolving them.

## 4. Splitting, training, and evaluation

Use a strict 70% train / 20% validation / 10% test split. Keep every frame from
the same sequence, camera burst, video, or near-duplicate group in one split.
Check duplicates and retain varied weather, lighting, geography, camera angle,
tide, surf density, and positive/negative difficulty. Freeze and protect the
test manifest before model selection; never tune against test labels.

Augmentation is training-only. Save the dataset version, split manifests,
model/configuration, random seed, environment, and every material experiment.
Report precision, recall, mAP@0.5, false positives per image, confusion matrix,
and representative successes and failures. Stratify errors by scene conditions
and inspect lookalike false positives. The research target is mAP@0.5 >= 0.80
on the untouched test set, not a safety threshold. If the target is missed,
report the actual result and explain the limitations; do not change the split,
remove difficult examples, or select a more flattering metric.

## 5. YSTE deliverables and exhibition expectations

The project should produce a reproducible baseline, comparison or ablation,
error/bias analysis, offline demonstration, and a complete evidence trail. The
submission package includes:

1. a report book: title page, contents, one-page abstract, introduction,
   literature review, methodology, results, discussion, conclusion, references,
   and appendices; main body no more than 50 pages excluding references and
   appendices;
2. a project diary covering planning, investigation, results, problems,
   learning, and exhibition preparation;
3. a clear video under three minutes, with good audio/visuals and no music; and
4. a landscape display within the handbook dimensions, showing the question,
   method, results, discussion, references, and safety wording.

Show raw images beside predictions, metric tables, precision-recall or related
plots, the confusion matrix, failure examples, dataset composition, licensing,
bias, and limitations. Explain what was actually tested rather than presenting
selected successes as proof of performance. Follow the supplied YSTE handbook
for current deadlines, submission instructions, judging, and display limits;
the handbook overrides this summary. For the supplied 2027 schedule, the key
dates are entry by 25 September 2026, the under-three-minute video by 11
December, report-book PDF and exhibition setup before noon on 6 January 2027,
and exhibition/judging at RDS Dublin from 6–9 January. Keep the landscape
display within the stated 1,189 mm x 841 mm back panel and 1,200 mm x 600 mm
worktop limits.

## 6. Evidence and communication rules

Be honest, uncertainty-aware, and evidence-led. Separate facts from
hypotheses, planned work from completed work, model output from ground truth,
and benchmark performance from real-world usefulness. Cite reliable sources
for rip-current science and exhibition rules. Do not invent data, annotations,
experiments, citations, metrics, reviewer approval, or completed deliverables.
Use exact dataset versions and test results where available, state what is
unknown, and preserve contradictory or failed results. Prefer “the model
flagged a visual pattern consistent with the annotation” over “the model found
a rip current.” When a claim cannot be supported by the recorded evidence,
label it as unverified or decline to make it.

The project is successful when its method is reproducible and its conclusions
are accurate—even if the detector performs below the 80% research target.
