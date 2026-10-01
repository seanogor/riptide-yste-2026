# Project assistant instructions

## Project purpose and safety

- Support the Young Scientist project studying whether computer vision can
  recognise likely rip-current signs in beach imagery.
- Treat the work as educational research. Never present it as a rescue,
  warning, or operational safety system, or as a replacement for lifeguards,
  beach signs, or official advice.
- Be evidence-led. Distinguish observations from confirmed labels, state
  uncertainty, and report limitations and failed results honestly.

## Image review and data

- Do not browse the web to find or inspect images in order to decide whether
  they show a rip current. Assess only images the student supplies or images
  already included in the project dataset, and describe visual evidence and
  uncertainty rather than claiming certainty from an image alone.
- Use only images whose public-domain, Creative Commons, or other open-access
  reuse terms have been verified. Record source URL, licence, capture date when
  available, coarse region, camera type, and sequence ID.
- Label examples `positive`, `negative`, or `review`. Keep ambiguous examples
  in `review`; do not force a label. Use tight bounding boxes around the
  visible channel or plume, not the entire surf zone.
- Keep related frames or burst images in the same split. Use a leakage-safe
  train/validation/test split and lock the test set before model selection.

## Conserve disk space

- Keep large image datasets, model weights, training runs, and generated
  predictions out of Git. Store only small manifests, labels when appropriate,
  source/licence notes, code, and essential research outputs in the repository.
- Do not download or duplicate datasets, pretrained weights, or other large
  artifacts unless the student explicitly requests it and the storage location
  and licence are suitable.
- Prefer scripts that process data in place and write only necessary outputs.
  Avoid unnecessary copies, caches, checkpoints, and intermediate exports.
- Keep generated artifacts in ignored data/output directories; remove only
  temporary files created for the current task when they are no longer needed.
- Check repository size and `.gitignore` before adding data or generated files.

## Changes and pull requests

- Make small, focused changes and commit completed, validated units of work
  regularly on the current project branch. Do not create a commit for every
  trivial edit.
- Before committing, inspect the diff and stage only files relevant to that
  change. Never include large datasets, model weights, secrets, or unrelated
  worktree changes.
- Use descriptive commit messages. Keep commits suitable for review in a pull
  request; do not claim a PR exists unless one has actually been created.
- Run the smallest relevant tests or checks before committing and report any
  checks that could not be run.

## Evaluation and communication

- Report precision, recall, mAP@0.5, false positives, and representative
  failure cases where applicable. Never imply a target score proves real-world
  safety.
- Follow the project's Young Scientist requirements for the report, project
  diary, video, display, citations, and deadlines. Do not invent completed
  research, image provenance, labels, or results.
