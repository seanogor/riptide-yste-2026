# Young Scientist 2027 student checklist

Use this as a working checklist alongside the [project proposal](project-proposal.md).
These dates are taken from the supplied Stripe YSTE 2027 handbook.

## Before 25 September 2026 — enter the project

- [ ] Confirm the research question, hypothesis, and mAP@0.5 target.
- [ ] Choose a precise title of no more than 100 characters.
- [ ] Read and cite NOAA, USLA, and relevant computer-vision sources.
- [ ] Ask the teacher to confirm the Technology category and age section.
- [ ] Write the safety statement: predictions are informational and never direct
      swimmers or emergency response.
- [ ] Create the research log and source/license manifest.
- [ ] Complete the student entry, project details, and one-page proposal of no
      more than 500 words.
- [ ] Submit the student application and entry fee by **25 September, 5:00 pm**.

## By 28 September — teacher assessment

- [ ] Confirm the teacher submits the separate assessment by **28 September,
      5:00 pm**.

## 29 September–22 October — prove the data process

- [ ] Audit the 50-image pilot and remove sources with unclear reuse rights.
- [ ] Write the annotation guide with positive, negative, and review examples.
- [ ] Annotate 20 practice images and obtain a second review of a sample.
- [ ] Record camera type, sequence ID, conditions, and coarse region.
- [ ] Decide whether the full 1,000–1,500-image target is feasible.

## 23 October–5 November — screening and acceptance

- [ ] Check the screening result by **23 October**.
- [ ] If qualified, complete the confirmation card and obtain student,
      parent/guardian, and teacher signatures.
- [ ] Return the confirmation card by **5 November**.

## 6 November–4 December — build and freeze the dataset

- [ ] Collect and annotate additional images in small, reviewable batches.
- [ ] Check duplicates and keep frames from one sequence in one split.
- [ ] Generate the 70% train / 20% validation / 10% test manifests.
- [ ] Freeze the test manifest and record the dataset version.
- [ ] If the full target is not feasible, document the minimum viable pilot plan.

## 5–11 December — submit the video

- [ ] Write a script covering the question, method, and current findings.
- [ ] Record a clear video under three minutes with good audio and visuals.
- [ ] Do not add music, product promotion, or unexplained technical jargon.
- [ ] Upload an accepted MP4, AVI, or MOV by **11 December**.

## 12 December–2 January — finish the study and artifacts

- [ ] Set up Python, the ML framework, annotation utilities, and a GPU notebook
      or approved local environment.
- [ ] Run the baseline with a fixed seed and save configuration and package
      versions.
- [ ] Export learning curves and validation metrics.
- [ ] Confirm that another person can follow the run instructions.
- [ ] Write the report book: title page, contents, one-page abstract,
      introduction, literature review, methodology, results, discussion,
      conclusion, references, and appendices.
- [ ] Keep the report's main body to 50 pages or fewer, excluding references
      and appendices.
- [ ] Update the project diary with planning, investigation, results, problems,
      learning, and exhibition preparation.
- [ ] Design a landscape display within 1,189 mm x 841 mm back-panel and
      1,200 mm x 600 mm worktop limits.

## 3–6 January — send the report and set up

- [ ] Run one pre-declared comparison or ablation using validation data only.
- [ ] Select the final model without opening the test labels.
- [ ] Evaluate once on the locked test set.
- [ ] Export mAP@0.5, precision, recall, false positives per image, confusion
      matrix, and examples of successes and failures.
- [ ] Email the report-book PDF to `projectbook@yste.ie` before **6 January,
      12:00 pm**, using the stand number as the subject.
- [ ] Print two report-book copies and pack the diary and display.

## 6–9 January — exhibition

- [ ] Analyze errors by weather, lighting, geography, camera angle, and surf
      state.
- [ ] Explain whether the 80% target was met and why.
- [ ] Write methods, results, limitations, ethics, and conclusion.
- [ ] Build the poster or slides with raw/predicted image pairs.
- [ ] Have a teacher or mentor review citations, licensing, and claims.
- [ ] Set up the diary, one report-book copy, and display at the RDS by **6
      January, 12:00 pm**, before Round 1 judging (3:00–6:00 pm).
- [ ] Prepare for Round 2 on **7 January, 9:00 am–1:00 pm**, Round 3 on
      **7 January, 2:00–6:00 pm**, and Round 4 if needed on **8 January,
      9:00 am–12:00 pm**.
- [ ] Save the submission receipt, final archive, and judging notes.
- [ ] Practice a three-minute explanation and answers about false positives,
      dataset bias, safety, and limitations.

## If the model misses the target

That is a valid result. Report the measured score, preserve the locked test
evaluation, show the error gallery, and explain the next experiment. Do not
quietly remove difficult images, change the split, or describe the prototype as
operationally safe.
