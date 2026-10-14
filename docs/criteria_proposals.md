# Acceptance criteria — analysis and proposals (Milestone 3)

**Status: AI-proposed, awaiting the student's approval.** The five targets below were worked out by an AI
assistant (Claude) on 14 October 2026 from the taxonomy in [label_taxonomy.md](label_taxonomy.md) and the
label shares observed in the Milestone 1–2 sample. They are **not** the student's independent choices until
the student has read this file and either approved or changed each number in `criteria.md`. Nothing here was
derived from training results: at the time of writing no dataset had been assembled and no model trained.

The five criteria as filed are in [`criteria.md`](../criteria.md). This file holds the reasoning.

---

## What the evaluation will look like

| Fact | Value used in the reasoning |
|---|---|
| Labels | `question`, `report`, `take` |
| Shares in the 38-post research sample | 53% / 29% / 18% |
| Target dataset | 220–260 real posts; `take` deliberately sampled up toward 20–25% (documented in the dataset section of the README) |
| Split | stratified 70 / 15 / 15, seeds 42, 7 and 2024 in unit 6 |
| Test split size at N = 240 | 36 posts; at 20% `take`, about 7 of them are `take` |
| What one test post is worth | about 2.8 accuracy points overall; about 14 F1-ish points for a 7-example label |
| Chance levels | majority-class guess ≈ 0.50–0.53 accuracy; uniform guess ≈ 0.33 |
| Unit 6 rule | a target must hold on **all three** seeds to count as MET |

---

## Area 1 — Overall accuracy

- **Quantity.** Accuracy = correct predictions ÷ test posts, on the 15% held-out split.
- **How calculated.** `results.json["accuracy"]`, written by notebook section 5 (and per seed in unit 6's
  `results_three_seeds_*.json`).
- **Evaluated on.** The held-out test split written to `test_split.csv`; the baseline later scores the same
  file.
- **Defensible target: ≥ 0.70 on every seed.** A model that is right on seven posts in ten is one a moderator
  could use to triage; majority-class guessing gets about 0.50, so 0.70 is twenty points of real learning.
- **Why it might be too easy.** `question` posts have strong surface cues (question marks, "any
  recommendations"). If the classifier learns only that cue it could reach ~0.70 while being useless on
  `report` vs `take`. Criterion 2 exists to stop that.
- **Why it might be too hard.** 36 test posts, three seeds, and the rule that all three must clear the bar.
  A spread of ±8 points between seeds is normal at this size, so a model whose true accuracy is 0.74 can
  still post a 0.67 on one seed. That risk is accepted on purpose: a target that cannot be missed is not a
  target.

## Area 2 — Per-label performance

- **Quantity.** F1 per label on the test split.
- **How calculated.** `results.json["per_label"][label]["f1"]` (precision and recall are stored too).
- **Evaluated on.** The same held-out split.
- **Defensible target: F1 ≥ 0.65 for `question` and for `report`, and F1 ≥ 0.50 for `take`, on every
  seed.** The two larger labels have 10–19 test examples each; `take` has about 7, where a single missed post
  moves F1 by more than ten points, so its bar is set lower rather than pretending the measurement is as
  precise.
- **Undefined case.** If a label has zero support in a test split (the stratified split should prevent it),
  its F1 is 0 by the notebook's `zero_division=0` and the criterion is MISSED for that seed; the diagnosis
  must say the split, not the model, caused it.
- **Why it might be too easy.** 0.50 for `take` allows roughly half the takes to be missed. It is deliberately
  loose because of support size; if `take` reaches 25% of the data (about 9 in test) the student may want to
  raise it to 0.55.
- **Why it might be too hard.** `report` vs `take` is the boundary where the writer's own experience is used
  as evidence (audit posts 28, 32); if the labelling of that boundary was inconsistent, both labels' F1 will
  suffer and 0.65 for `report` will be missed. That is the intended use of the agreement report next unit.

## Area 3 — Dataset balance

- **Quantity.** (a) The largest label's share of `labels.csv`; (b) the smallest label's count in each test
  split.
- **How calculated.** (a) from `labels.csv` directly (`validate_dataset.py` prints it; the notebook's
  section 2 check flags > 60% and > 70%); (b) from the notebook's section 3 split table and `test_split.csv`
  (seed 42), and from `n_per_label support` in each seed's results in unit 6.
- **Evaluated on.** The whole dataset and each split.
- **Defensible target: no label above 60% of `labels.csv`, and the smallest label has at least 8 posts in
  the test split of every seed.** The brief's hard cap is 70%; 60% leaves a margin so the model cannot
  reach criterion 1 by guessing. Eight test examples is the notebook's own threshold for "thin"; below it
  per-label F1 is noise.
- **Why it might be too easy.** The natural `question` share (~53%) is already under 60%. The teeth are in
  the second half: 8 `take` posts in a 15% split needs about 54 `take` posts in the file, which the natural
  18% rate does not supply at N = 240. It forces the deliberate `take` sampling.
- **Why it might be too hard.** It depends on collection, not modelling: if the opinion-flavoured listings
  do not yield enough eligible `take` posts, this is missed before training starts. That would be a true
  finding about the community (takes are rare as standalone posts) and should be recorded as such.

## Area 4 — Human labelling consistency

- **Quantity.** Raw agreement between two labellers applying the written rules independently to the same
  posts.
- **How calculated.** The student labels the 20 reserved posts in `data/cold_label_queue.csv` without
  seeing any AI label. Afterwards the assistant labels the same 20 under the rules in `label_taxonomy.md`,
  blind to the student's answers (both files committed before comparison). Agreement = matching labels ÷
  20. Cohen's kappa is reported alongside for information but is not the criterion.
- **Evaluated on.** The 20 cold posts only. The unit 6 staff-set agreement (30 posts, staff taxonomy) is
  reported separately in the README and is *not* this criterion, because it measures a different taxonomy.
- **Defensible target: at least 16 of 20 agree (≥ 80%).** The rules were designed to be applied the same way
  by two readers; 80% leaves room for the one-in-five borderline rate seen in the audit (7 of 38).
- **Undefined case.** Until both label sets exist the criterion is **not measurable and counts as MISSED**,
  with the reason "not yet measured". It must not be marked MET by default.
- **Why it might be too easy.** Twenty posts is small and each one is five points; a lucky draw of clear
  posts could give 20/20 without proving much. The queue was therefore drawn at random from the eligible
  pool, not from the clear cases.
- **Why it might be too hard.** The two hardest shapes (closed account with a feedback request; experience
  as evidence for a general claim) each cost a point when they appear. If agreement comes in at 70–75%,
  the right response is a rule revision in unit 6, not a lowered target.

## Area 5 — Prediction confidence

- **Quantity.** Accuracy of the most-confident third of test predictions versus the least-confident third.
  Confidence is the softmax probability of the predicted label.
- **How calculated.** `results.json["confidence"]["accuracy_most_confident_third"]` and
  `["accuracy_least_confident_third"]`, with `n_per_third` giving the size (about 12 posts at N = 240).
- **Evaluated on.** The held-out split, per seed.
- **Defensible target: on every seed, accuracy among the most-confident third ≥ 0.85, and it exceeds the
  least-confident third by at least 0.15.** A confidence score is only useful if a moderator can trust the
  sure cases more than the unsure ones; both halves of the target are needed, because a model that is 0.85
  on both thirds has confidence that means nothing.
- **Threshold note.** The brief's wording suggests a probability cut-off such as "predictions above 0.90
  are right at least 90% of the time". The notebook does **not** store per-post probabilities, only the
  thirds summary, so a probability-threshold version cannot be computed from the committed artefacts. The
  criterion is therefore stated in thirds, which is measurable from `results.json` as it stands. If the
  student prefers the threshold form, section 5 of the notebook would need to save `confidence` per row
  into `test_split.csv`; that is a one-line change recorded in the README if made.
- **Undefined case.** If `n_per_third` < 5 the measure is not meaningful and the criterion is MISSED with
  that reason.
- **Why it might be too easy.** With 12 posts per third, 0.85 allows one wrong; the least-confident third of
  a 0.70-accuracy model will often sit near 0.50, so a 0.15 gap is the normal shape of a working softmax.
- **Why it might be too hard.** Twelve posts per third means one extra error in the sure third drops it to
  0.75. Across three seeds this is probably the most volatile of the five, which is why it is paired with a
  gap condition rather than standing alone.

---

## Feasibility against the notebook (Task 3 of the brief)

| Criterion | Needs | Available from the starter? |
|---|---|---|
| 1 accuracy | true and predicted labels on the test split | Yes: `results.json["accuracy"]`, per seed in unit 6 |
| 2 per-label F1 | same, per label | Yes: `results.json["per_label"]` |
| 3 balance | label counts in the file and in each split | Yes: `labels.csv`, section 3 split table, `per_label[label]["support"]` |
| 4 agreement | two independent label sets on the same 20 posts | **Not produced by the notebook.** Produced by `data/cold_label_queue.csv` (student) plus a blind second pass; a small script will compute agreement and kappa in unit 6 |
| 5 confidence | per-prediction probabilities | Partly: thirds summary in `results.json["confidence"]`; per-row probabilities are not saved |

No criterion was replaced by an easier one. Criterion 4 is measured outside the notebook by design, and
criterion 5 is stated in the form the notebook can actually support.

---

## Decisions the student must make

- [ ] Approve or change each of the five numbers in `criteria.md`. If a number changes, change it there and
      note the reason under it; the AI-proposed value is recorded in this file for the audit trail.
- [ ] Decide whether criterion 5 should stay in "thirds" form (measurable now) or move to a probability
      threshold (needs a one-line notebook change before training).
- [ ] Confirm criterion 4's design: the 20 cold posts labelled by you first, then blind by the assistant.
