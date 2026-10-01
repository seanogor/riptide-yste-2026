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

## After the student gives a correction

Explain what the initial assessment got right or wrong, identify the clue that
was missed or overvalued, and state a concise revised rule. Record only the
student-provided label as the student's correction. Keep the assistant's initial
prediction and confidence separate from that correction.

## Criteria recovered from the earlier training session

The conversation history preserves six corrected examples and one later
assessment awaiting student feedback:

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
- A further image received a moderate-confidence positive assessment, but no
  student correction was found. It remains unlabelled in the log and must not
  be counted as a corrected example.

These are student coaching examples, not independently verified
oceanographic ground truth. The original images for the six corrected examples
were not recovered into this repository. One later attachment remains outside
the repository, but its provenance and licence have not been verified. See
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
