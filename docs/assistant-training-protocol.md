# Assistant image-training protocol

This protocol records how the student coaches the project assistant to read
beach images. Here, "training" means a supervised review-and-correction process
that builds project-specific criteria and records them. It does not change the
assistant's underlying model parameters.

## Before the student gives a label

For each image supplied for review:

1. Classify it as `positive`, `negative`, or `ambiguous`.
2. Describe the suspected region using image-width and image-height percentages;
   give an approximate box only when there is a defensible region.
3. Separate visible evidence from assumptions. Consider a narrow offshore
   channel, a gap in breaking waves, foam or sediment, water colour, and the
   surrounding surf or sandbar pattern.
4. Give a confidence estimate and at least one plausible lookalike, such as
   glare, shadow, backwash, a temporary wave gap, deep water, or sediment
   movement.
5. State that a still image cannot prove water movement; video or qualified
   local review may be needed.
6. Wait for the student's correction before recording a corrected label.

Do not use the web or internet to find images or decide their labels. Do not
open the image source page, reverse-search the image, consult external
annotations, or use source metadata to infer the answer. Use only the supplied
image and the criteria taught by the student.

## Student-defined pass criterion

For this coaching exercise, the student counts an assessment as a pass when
the assistant identifies an image as positive—including "ambiguous, leaning
positive"—and the student agrees that the positive assessment is correct.
Record the assistant's uncertainty and the student's agreement separately.
This is a coaching criterion for the exercise, not a measure of model
performance or independent scientific validation. By this criterion, images
13 and 14 were passes because the assistant assessed them as ambiguous,
leaning positive, and the student confirmed them as positive. Images 16, 22,
and 23 were also passes: the assistant assessed them as positive and the
student agreed.

## After the student gives a correction

Explain what the initial assessment got right or wrong, identify the clue that
was missed or overvalued, and state a concise revised rule. Record only the
student-provided label as the student's correction. Keep the assistant's initial
prediction and confidence separate from that correction.

## Criteria recovered from the earlier training session

The conversation history preserves thirty-one student-labelled examples:

- Ordinary shoreline foam/backwash alone was corrected as negative.
- A break in a bar, discoloured water, and visible offshore flow supported a
  positive assessment.
- A visible bar break was not required in another positive example with
  discoloured, channel-like water.
- The Mauritius "Underwater Waterfall" image was corrected as negative: broad
  sediment transport from a shallow shelf into deeper water is not by itself a
  swimmer-relevant surf-zone rip current.
- Offshore-directed flow could support a positive assessment without a visible
  bar break.
- A later positive correction also noted there was no visible break in the
  bank/bar.
- A later image was assessed as a moderate-confidence positive and the student
  subsequently labelled it positive. No explanation for that correction was
  supplied, so no additional rule is inferred.
- For `rip-current 8-example.jpg`, the student supplied a positive label before
  attaching the image, then later confirmed the assistant's moderate-confidence
  positive visual assessment. The assessment noted a dark channel-like region
  interrupting breaking waves and foam along its margins. The student explained
  that discolouration and a break in the bar are visible cues. For this
  student-labelled example, those cues support the positive assessment.
  Because the label was known first, this is not a blind test or an independent
  evaluation example. The student supplied a WHOI source URL, but the image's
  reuse licence has not been verified.
- For `rip-current9-example.jpg`, the assistant first assessed the attached
  image as ambiguous, leaning positive at about 60%, based on a foamy,
  discoloured plume and a gap in the breaking-wave line. The student labelled
  it positive after seeing that assessment and explained that when those visual
  signs recur, the project criteria should label the image positive. Record
  this as the student's project heuristic: a foamy/discoloured offshore-plume
  appearance together with a gap in the breaking-wave pattern supports a
  positive image label. It is not independent proof that water is moving
  offshore. The image source and reuse licence are unverified.
- For `rip-current10-example.jpg`, the assistant assessed the image as negative
  with moderate confidence (about 75%). It showed broad breaking surf and
  turbulent whitewater without a distinct narrow offshore channel, breaker gap,
  or offshore plume. The student confirmed it was normal water activity with
  no visible signs of a rip current. This is a student coaching example, not
  independent oceanographic ground truth.
- For `rip-current11-example.jpg`, the assistant assessed the image as negative
  with about 75% confidence. It showed a shore-parallel breaking wave and foam
  around wave collapse and swash, without a distinct narrow offshore channel,
  breaker gap, or offshore plume. The student labelled it negative after seeing
  the assessment. Its source and reuse licence were not provided.
- For `rip-current12-example.jpg`, the assistant assessed the image as negative
  with about 70% confidence. The visible whitewater followed the breaker line
  along a rocky cove and beach, without a distinct narrow channel, clear
  breaker gap, or offshore plume. The student labelled it negative after seeing
  the assessment. This is a visual annotation, not proof that no current is
  present; its source and reuse licence were not provided.
- For `Rip-currents 13-example.jpg`, the assistant assessed the image as
  ambiguous, leaning positive at about 60%, based on a dark channel-like
  foreground area with lighter, foamy margins. The student labelled it positive
  and explained that there was discolouration but no visible break in the bar.
  This reinforces the student-taught criterion that discolouration can support
  a positive label even without a visible bar break. It remains an image-review
  heuristic, not proof of offshore flow from a still image.
- For `rip current 14-example.jpg`, the assistant assessed the image as
  ambiguous, leaning positive at about 58%, based on a darker channel-like
  patch between breaking-surf bands with foam around it. The student labelled
  it positive after the assessment, meeting the student's coaching pass
  criterion. The rocky coastline and oblique wave pattern are possible
  lookalikes; no additional student explanation was supplied. This is not
  independent validation.
- For `rip current-15 example.jpg`, the assistant assessed the image as
  negative at about 75% confidence. It showed shore-parallel small breakers,
  scattered rocks, and foam along the breaker line without a clear offshore
  channel, breaker gap, or plume. The student labelled it negative after seeing
  the assessment. The image has a visible Shutterstock watermark, and its reuse
  permission was not verified; it is not included in the repository.
- For `rip-current 16-example.jpg official.jpg`, the assistant assessed the
  image as positive at about 75% confidence. Several darker, narrow-looking
  channels appeared to interrupt the breaking-wave line and extend seaward,
  with discoloured water and foam around them. The student labelled it positive
  after seeing the assessment, meeting the student's coaching pass criterion.
  The source and reuse licence were not recorded, so the image is not included
  in the repository; this assessment is not independent validation.
- For `rip-current 22-example.webp`, the assistant assessed the composite as a
  positive illustration at about 70% confidence. Schematic panels a and c show
  arrows indicating offshore flow; panel b contains a turbulent, foamy patch;
  panel d shows an aerial surf line with a possible gap. The student labelled
  it positive after seeing the assessment, meeting the coaching pass
  criterion. Because this is a multi-panel graphic containing diagrams, it is
  not suitable as a single raw detector-training image or one-box annotation.
  The source and reuse licence were not recorded.
- For `rip-current-23 example.webp`, the assistant assessed the image as
  positive at about 70% confidence. A darker green channel appears to interrupt
  the breaking-wave line and extend from the beach side toward offshore, with
  foam and breaking waves on either side. The image is low resolution, so wave
  timing, depth, and glare are possible lookalikes; a still image cannot prove
  flow direction. The student labelled it positive after seeing the assessment,
  meeting the coaching pass criterion. Its source and reuse licence were not
  recorded.
- For `rip-current 20-example.jpg n official.jpg`, the assistant assessed the
  image as ambiguous, leaning negative at about 65%. It showed a sheltered
  cove with turquoise water and small waves but no clear narrow channel,
  breaker gap, or offshore plume. The student labelled it negative after seeing
  the assessment. Water colour may reflect depth, seabed, or lighting, and the
  still image cannot establish that no current is present. The source and reuse
  licence were not recorded.
- For `rip-current 21-example.jpg n official.jpg`, the assistant assessed the
  image as negative at about 80% confidence. It showed a large shore-parallel
  breaking wave and broad whitewater, without a distinct narrow offshore
  channel, breaker gap, or offshore plume. The student labelled it negative
  after seeing the assessment. A single shore-level image cannot establish
  that no current is present; its source and reuse licence were not recorded.
- For `rip current-24 example.webp`, the assistant assessed the image as
  ambiguous, leaning negative at about 60%. It showed shore-parallel wave bands
  across a cove with irregular foam near the rocky shoreline, without a clear
  offshore channel or plume. The student labelled it negative, explaining that
  there were no clear distinctive signs. Low light and the oblique view limit
  certainty; the source and reuse licence were not recorded.
- For `rip current-25 example.webp`, the assistant assessed the image as
  negative at about 80% confidence. It showed shore-parallel breakers and
  whitewater washing around exposed rocks along a shallow shoreline, without a
  distinct narrow offshore channel, breaker gap, or concentrated offshore
  plume. The student labelled it negative after seeing the assessment. This
  low shoreline view cannot establish that no current is present; its source
  and reuse licence were not recorded.
- For `rip-current 26-example.webp`, the assistant assessed the image as
  ambiguous, leaning negative at about 65%. It showed broad, mostly calm
  nearshore water with shallow-looking colour bands, but no clearly defined
  narrow channel, distinct breaker gap, or concentrated offshore plume. The
  student labelled it negative after seeing the assessment. The darker area
  could reflect depth, seabed, or lighting; the still image does not establish
  flow direction. Its source and reuse licence were not recorded.
- For `rip-current 27-example.jpg n official.jpg`, the assistant assessed the
  image as negative at about 85% confidence. It showed an exposed rocky tidal
  flat and shallow-looking water between rocks, without a distinct surf-zone
  channel, breaker gap, or offshore plume. The student labelled it negative
  after seeing the assessment. Its source and reuse licence were not verified.
- For `rip-current 31-example.jpg n official.jpg`, the assistant assessed the
  image as ambiguous, leaning positive at about 60% confidence. A gap in the
  distant breaking-wave line and a darker, relatively smooth corridor toward
  the foreground surf could be a channel-like appearance, but ordinary
  variation in breaking waves is also possible and the still image does not
  establish offshore flow. The student labelled it positive after seeing the
  assessment, meeting the project's coaching pass criterion. Its source and
  reuse licence were not verified.
- For `rip-current 33-example.jpg n official.jpg`, the assistant assessed the
  image as ambiguous, leaning positive at about 65% confidence. Apart from the
  drawn arrows, a darker, relatively smooth corridor appears to cut through
  foreground whitewater toward open water, with breaking surf on either side.
  The arrows and Surf Life Saving logo are overlays, not independent evidence,
  and the still image cannot confirm flow. The student labelled it positive
  after seeing the assessment, meeting the project's coaching pass criterion.
  Its source and reuse licence were not verified.
- For `rip current 32.jpeg`, the assistant assessed the image as ambiguous,
  leaning positive at about 60% confidence. A narrow gap in breaking foam just
  left of the rock groyne and a smoother-looking corridor extending seaward
  could be channel-like, but wave wrapping and turbulence around the structure
  are possible lookalikes. The red arrows are annotations, not evidence, and
  the still image cannot confirm flow. The student labelled it positive after
  seeing the assessment, meeting the project's coaching pass criterion. Its
  source and reuse licence were not verified.
- For `rip-current 34-example.jpg n official.jpg`, the assistant assessed the
 image as ambiguous, leaning negative at about 65% confidence. It showed a
 broad low-tide beach and shallow-looking water with diagonal wave bands, but
 no clearly defined narrow channel, distinct breaker gap, or concentrated
 offshore plume. The darker foreground area could reflect depth or seabed;
 the still image does not establish flow direction. The student labelled it
 positive after seeing the assessment. Its source and reuse licence were not
 verified.
- For `rip-current 35-example.jpg n official.jpg`, the assistant assessed the
 image as negative at about 80% confidence. It showed fairly continuous
 shore-parallel breaker bands and broad surf, without a distinct narrow
 channel, clear breaker gap, or concentrated offshore plume. The student
 labelled it negative after seeing the assessment. A still image cannot
 establish that no current is present; its source and reuse licence were not
 verified.
- For `rip current 36.png`, the assistant assessed the image as positive at
 about 85% confidence. It showed a dark, relatively smooth channel cutting
 through breaking surf toward open water, with breaking waves on either side.
 The directional arrows are annotations, but the channel-like gap is visible
 independently. A still image cannot prove flow. The student labelled it
 positive after seeing the assessment, meeting the project's coaching pass
 criterion. Its source and reuse licence were not verified.
- For `rip-current 28-example.webp`, the assistant assessed the image as
  negative at about 75% confidence. It showed a fairly continuous diagonal
  line of breaking waves and broad whitewater along the beach, with no distinct
  narrow seaward channel, clear breaker gap, or concentrated offshore plume.
  The student labelled it negative after seeing the assessment. A visible
  stock-photo watermark was present, so the image is not included in the
  repository and should not be reused without verified permission.

These are student coaching examples, not independently verified
oceanographic ground truth. The original images for these labelled examples
were not recovered into this repository. The seventh image was identified by
the student as `rip-current 7-example.jpg`, but its attachment remains outside
the repository and its provenance and licence have not been verified. Images
attached in chat are not committed because their reuse permissions have not
been verified. Image 15 also bears a visible Shutterstock watermark. See
`data/training_log.csv`; do not use it as a detector dataset, test set, or
scientific validation evidence.

## Record keeping and safety

- Preserve the first assessment, student correction, and resulting rule as
  distinct fields in the log.
- Do not invent a correction, image source, licence, annotation, or image file
  when historical information is missing.
- Do not treat this coaching log as detector training or evidence of model
  performance.
- Keep all image interpretation educational. Never use it for live swimming,
  rescue, or emergency decisions, or as a replacement for lifeguards and
  official warnings.
