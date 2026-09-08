# Young Scientist 2027 student checklist

Use this as a working checklist alongside the [project proposal](project-proposal.md).
Dates are planning dates, not official competition deadlines.

## September 2026 — define the study

- [ ] Confirm the research question, hypothesis, and mAP@0.5 success target.
- [ ] Read and cite NOAA, USLA, and relevant computer-vision sources.
- [ ] Ask a teacher to confirm the competition rules, permitted tools, and
      whether school approval or a mentor signature is required.
- [ ] Write the safety statement: predictions are informational and never direct
      swimmers or emergency response.
- [ ] Create the research log and source/license manifest.

## October 2026 — prove the data process

- [ ] Audit the 50-image pilot and remove sources with unclear reuse rights.
- [ ] Write the annotation guide with positive, negative, and review examples.
- [ ] Annotate 20 practice images and obtain a second review of a sample.
- [ ] Record camera type, sequence ID, conditions, and coarse region.
- [ ] Decide whether the full 1,000–1,500-image target is feasible.

## November–December 2026 — build and freeze the dataset

- [ ] Collect and annotate additional images in small, reviewable batches.
- [ ] Check duplicates and keep frames from one sequence in one split.
- [ ] Generate the 70% train / 20% validation / 10% test manifests.
- [ ] Freeze the test manifest and record the dataset version.
- [ ] If the full target is not feasible, document the minimum viable pilot plan.

## January 2027 — establish a baseline

- [ ] Set up Python, the ML framework, annotation utilities, and a GPU notebook
      or approved local environment.
- [ ] Run the baseline with a fixed seed and save configuration and package
      versions.
- [ ] Export learning curves and validation metrics.
- [ ] Confirm that another person can follow the run instructions.

## February 2027 — compare and evaluate

- [ ] Run one pre-declared comparison or ablation using validation data only.
- [ ] Select the final model without opening the test labels.
- [ ] Evaluate once on the locked test set.
- [ ] Export mAP@0.5, precision, recall, false positives per image, confusion
      matrix, and examples of successes and failures.

## March 2027 — explain the evidence

- [ ] Analyze errors by weather, lighting, geography, camera angle, and surf
      state.
- [ ] Explain whether the 80% target was met and why.
- [ ] Write methods, results, limitations, ethics, and conclusion.
- [ ] Build the poster or slides with raw/predicted image pairs.
- [ ] Have a teacher or mentor review citations, licensing, and claims.

## April 2027 or official deadline — submit

- [ ] Confirm the official Young Scientist 2027 deadline and required forms.
- [ ] Submit the paper, abstract, poster/slides, code link, data statement, and
      approvals requested by the competition.
- [ ] Save the submission receipt and final archive.
- [ ] Practice a three-minute explanation and answers about false positives,
      dataset bias, safety, and limitations.

## If the model misses the target

That is a valid result. Report the measured score, preserve the locked test
evaluation, show the error gallery, and explain the next experiment. Do not
quietly remove difficult images, change the split, or describe the prototype as
operationally safe.
