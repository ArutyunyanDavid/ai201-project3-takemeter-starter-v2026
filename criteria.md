# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

> **Reviewed and approved by me on 15 October 2026.** The five numbers were
> first drafted by an AI assistant (Claude) before any data was collected or
> any model trained; the reasoning, including why each could be too easy or
> too hard, is in [docs/criteria_proposals.md](docs/criteria_proposals.md).
> I kept criteria 1, 2, 3 and 5 as proposed. I kept criterion 4 at 16 of 20
> because it is a reasonable target for the 20 posts I label on my own.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy on the held-out split

**Target:** overall accuracy **≥ 0.70** on the 15% test split, **on every seed** (42, 7 and 2024).

**Measured by:** `results.json["accuracy"]` from notebook section 5 (unit 5), and the
same field in `results_three_seeds_before.json` for each seed (unit 6). The
test split is the stratified 15% the notebook writes to `test_split.csv`.

**Why this target:** `question` is about half the data, so a model that always
guesses it scores about 0.50; 0.70 is twenty points above that and is the
level at which a moderator could use the sorter to triage. With roughly 36 test
posts each one is worth about 2.8 points, so a seed-to-seed spread of several
points is expected and the all-three-seeds rule makes this stricter than it
looks.

**Why I kept this number:** 0.70 is well above the 0.56 you get by always guessing `question`, and it is a level I would actually trust for sorting posts.

---

## 2. Every label performs, with a looser bar for the smallest

**Target:** on every seed, F1 **≥ 0.65 for `question`**, F1 **≥ 0.65 for `report`**,
and F1 **≥ 0.50 for `take`**, each on the test split. If a label has zero
support in a test split, its F1 is 0 and the criterion is MISSED for that seed
with the cause recorded as the split.

**Measured by:** `results.json["per_label"][label]["f1"]` (support is stored
beside it).

**Why this target:** `take` was 18% of the research sample and is being
sampled up toward about 22%, which still leaves only 7–8 `take` posts in a
test split; one missed post there moves F1 by more than ten points, so its bar
is set at 0.50 rather than pretending the measurement is as precise as for the
labels with 10–19 test examples. The 0.65 bars for the other two exist so the
model cannot pass criterion 1 by learning only the question-mark cue.

**Why I kept these numbers:** the bar for `take` is lower because there are only 9 `take` posts in the test split, so one mistake moves its F1 by more than ten points.

---

## 3. Balance: no label dominates, and the smallest label is measurable

**Target:** **no label exceeds 60%** of the rows in `labels.csv`, **and the
smallest label has at least 8 posts in the test split** of every seed.

**Measured by:** label counts printed by `validate_dataset.py` and by notebook
section 2 for the 60% part; the section 3 split table (seed 42) and
`results.json["per_label"][label]["support"]` for each seed for the 8-post part.

**Why this target:** the brief's cap is 70%; 60% leaves a margin so criterion
1 cannot be met by majority guessing. Eight test examples is the notebook's own
"thin" threshold, below which per-label F1 is noise; reaching it for `take`
needs about 54 `take` posts in the file, which the natural 18% rate does not
supply at 240 posts, so this criterion is what forces the deliberate `take`
sampling documented in the README.

**Why I kept this number:** the final file has `question` at 56%, under 60%, with 9 `report` and 9 `take` posts in the seed-42 test split, so the rule is met and it keeps the small labels measurable.

---

## 4. Two labellers agree under the written rules

**Target:** on the 20 posts in `data/cold_label_queue.csv`, labelled first by
the student without any AI label in view and then, blind to those answers, by
the assistant under the rules in `docs/label_taxonomy.md`, the two label sets
agree on **at least 16 of 20 (≥ 80%)**. Until both sets exist the criterion is
**not measurable and counts as MISSED** with the reason "not yet measured";
it is never MET by default.

**Measured by:** a direct comparison of the two 20-row label lists (a small
script in unit 6 prints agreement and Cohen's kappa; kappa is reported but is
not the criterion). The unit 6 staff-set agreement uses a different taxonomy
and is reported separately, not here.

**Why this target:** the taxonomy's rules were written so that two readers
apply them the same way; the Milestone 2 audit found 7 borderline posts in 38
(about one in five), and 80% on twenty posts allows for exactly that rate. If
agreement lands at 70–75% the fix is a rule revision, not a lower number.

**Why I kept this number:** 16 of 20 allows for about one borderline post in five, which matches the borderline rate the audit found, and it is still a real test of whether the written rules can be applied the same way twice.

---

## 5. Confidence means something

**Target:** on every seed, accuracy among the **most-confident third** of test
predictions is **≥ 0.85**, **and** it exceeds accuracy among the
least-confident third by **at least 0.15**. Confidence is the softmax
probability of the predicted label. If `n_per_third` is under 5 the criterion
is MISSED with that reason.

**Measured by:** `results.json["confidence"]["accuracy_most_confident_third"]`,
`["accuracy_least_confident_third"]` and `["n_per_third"]`, written by notebook
section 5. (The notebook does not save per-post probabilities, so a
probability-threshold version such as "predictions above 0.90 are right 90% of
the time" cannot be computed from the committed files; the thirds form is used
because it can. See docs/criteria_proposals.md, area 5.)

**Why this target:** a confidence score is only useful if the sure cases can be
trusted more than the unsure ones. With about 12 posts per third, 0.85 allows
one error in the sure third, and the 0.15 gap rules out a model that is equally
right everywhere, whose confidence would carry no information. Both halves are
needed; either alone is easy to satisfy by accident.

**Why I kept these numbers:** a confidence score is only useful if the sure guesses are right more often than the unsure ones, and both parts of the rule are needed to check that.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
