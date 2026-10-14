# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

TakeMeter classifies standalone posts from **r/running**
(<https://www.reddit.com/r/running/>), Reddit's general running community of
over four million subscribers, where members post training questions, race
reports, gear questions and opinions about running culture. It sorts each post
by what the post is *doing*: a **`question`** asks the community for an answer,
advice, a recommendation or others' experiences; a **`report`** is a firsthand
account of something the writer did, with its outcome; a **`take`** is a claim
or argument about running, runners, races or events beyond the writer's own
case. AutoModerator threads, recurring scheduled threads, and link-only posts
with under two sentences of the poster's own words are out of scope.

*Research record:* [docs/community_review.md](docs/community_review.md) — 40
real posts with links, the sampling method, and the candidate distinctions.
*Taxonomy record:* [docs/label_taxonomy.md](docs/label_taxonomy.md) and
[docs/taxonomy_stress_test.md](docs/taxonomy_stress_test.md).



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

**Community:** r/running. Post numbers below refer to the table in
[docs/community_review.md](docs/community_review.md); every example is a real
post with its permalink. Full definitions, signals, exclusions and the audit
of all 40 posts are in [docs/label_taxonomy.md](docs/label_taxonomy.md).

### `question`

**Definition:** The post exists to get something from readers — an answer,
advice, a recommendation, a verdict on the writer's own situation, or others'
experiences — and whatever else it contains is there to set that request up.

**Example 1:** post 20 — [Should a beginner ditch speed training?](https://www.reddit.com/r/running/comments/1x3v0k6/should_a_beginner_ditch_speed_training/)
> BACKGROUND: Hello! I am a 23 y/o, 88 kg male with Stage 1 Hypertension
> (controlled) and no prior sports background. I have been running for 15 weeks
> now […] As a beginner, is it okay to ditch speed training for now and focus on
> Zone 2-3 training? […] Should I trust my HR and switch to brisk walking
> instead? Or should I trust my perceived exertion […]?

**Example 2:** post 12 — [Garmin or Strava prediction: which is more accurate?](https://www.reddit.com/r/running/comments/1wrosne/garmin_or_strava_prediction_which_is_more_accurate/)
> I have a half marathon in two weeks time and am at the end of my training
> block. There's a 7 minute difference between my Garmin estimated time and my
> Strava estimated time. They have the same input. […] Questions: Which do you
> value more? Why do you think they vary so much?

### `report`

**Definition:** The post's substance is a firsthand account of something the
writer did or went through — a race, a training block, a product or method
they used, a streak, a change of attitude — told with its specifics and its
outcome, and it stands complete without replies.

**Example 1:** post 8 — [Race Report - Loch Ness Marathon - PB, BQ, SUB 3](https://www.reddit.com/r/running/comments/1wuzdvc/race_report_loch_ness_marathon_pb_bq_sub_3/)
> Race: 2026 Loch Ness Marathon Date: September 27, 2026 Time: 2:58:34 Goals
> […] A PB (Sub 3:20) Yes B BQ (Sub 3:05) Yes C Sub 3 Yes Background I have had
> a on again/off again relationship with running over the years […]

**Example 2:** post 5 — [I successfully reverse-engineered Maurten Gel 100](https://www.reddit.com/r/running/comments/1whzccf/i_successfully_reverseengineered_maurten_gel_100/)
> TL;DR: I perfected a DIY Maurten Gel 100 clone using the exact same
> internal-gelation mechanism (Sodium Alginate + Calcium Carbonate + GDL). This
> recipe makes a 10-serving batch. Each 50g pouch delivers exactly 25g of
> carbohydrates at a 0.8:1 Fructose-to-Glucose ratio […]

### `take`

**Definition:** The post's substance is a claim or argument about running,
runners, races, training methods, running culture or an event, going beyond
the writer's own case, put forward for readers to agree or argue with rather
than to answer or to witness.

**Example 1:** post 16 — [Norwegian Singles Method. A suboptimal approach](https://www.reddit.com/r/running/comments/1wtk6v6/norwegian_singles_method_a_suboptimal_approach/)
> I've got a hot take for the Norwegian Singles Method that might ruffle some
> feathers. […] I think NSM is heading down the same road as cycling and FTP.
> […] Is it going to leave a lot of people significantly below their true
> potential. I think so.

**Example 2:** post 34 — [LA Marathon men's finish was wild-and coverage was terrible!](https://www.reddit.com/r/running/comments/1roa4ql/la_marathon_mens_finish_was_wildand_coverage_was/)
> American Nathan Martin won the LA Marathon this morning in 2:11:18, coming
> from behind in a massive sprint to the finish. At least I think that's what
> happened, because the coverage was absolutely terrible.

### The hardest boundary

**Which two labels:** `question` vs `report` — a finished account that ends by
asking for feedback. The post: post 15, [my first marathon - an immediate
reflection & seeking feedback](https://www.reddit.com/r/running/comments/1wxukty/my_first_marathon_an_immediate_reflection_seeking/)
— about 10,500 characters of race report (Higdon Novice 1, cramping from mile
18, first 17 miles in 133 minutes, last 9.2 in 108) ending with "I think it was
predominantly neuromuscular fatigue. Agree/disagree? […] Don't pull your
punches here, I am here to learn from your wisdom and experience!" The title
and the explicit request for advice argue for `question`; nine-tenths of the
words, an outcome, and the writer's own diagnosis and plan argue for `report`.
**Chosen: `report`.** *(Student confirmation pending — see
docs/label_taxonomy.md section 8.)*

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->

Strike every sentence that asks readers for something. If nothing of substance
is left, it is `question`. Otherwise: if what is left is **closed** — an
account with its outcome and the writer's own conclusion, or a claim stated
with its reasons — it is `report` or `take`; if what is left is **open** — a
problem unsolved, a choice unmade, a thing not yet found — it is `question`.
Titles such as "question" or "seeking feedback" do not override the body, and a
single open line inside an otherwise closed account is an aside. Between
`report` and `take`: conclusions about the writer's own case (their race, their
plan, the product they used) are `report`; a claim about running beyond the
writer's case, with their experience offered as evidence, is `take`. Only if
both rules leave two labels standing, label by where most of the words are.

**How AI helped test the definitions:** the assistant (Claude) applied the
rules to all 40 real posts from Milestone 1 (audit table in
docs/label_taxonomy.md, 7 of 38 eligible posts borderline, none unresolved)
and wrote eight synthetic boundary posts — clearly marked as not real, in
docs/taxonomy_stress_test.md — covering a finished race with a feedback
request, an opinion phrased as a question, own experience used as proof of a
general claim, and a closed story under a title that says "question". One
revision came out of testing: the first version of the rule said "complete
report or argument", which misfiled a gear-recommendation post whose body
complained about pricing; it was rewritten around open vs closed.

---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

> **Status (14 October 2026): PROVISIONAL.** Every label below was assigned by
> an AI assistant (Claude) under the rules in docs/label_taxonomy.md and has
> **not yet been reviewed by me**. The 20 cold posts are reserved in
> `data/cold_label_queue.csv` and are not in `labels.csv` until I label them.
> After my review the training run must be repeated on the corrected file.

**Where the posts came from:** r/running, read through Reddit's public Atom
feeds (`/r/running/<listing>/.rss`) on 14 October 2026 with 60–90 seconds
between requests; the JSON API refuses scripted access. 610 unique posts were
pulled from the top-of-year (two pages of 100), top-of-month, newest, hot and
top-of-all-time listings and from three in-subreddit searches (flair
Discussion, year and all time; "unpopular opinion / hot take / rant / PSA").
Excluded by rule before labelling: AutoModerator and recurring scheduled
threads, and posts whose body is a link or copied article with under two
sentences of the poster's own words. The **core** of the dataset is every
eligible post from the general listings (191 read, 185 kept, dated
Oct 2025–Oct 2026). Because that core came out **76% `question`**, over the
brief's 70% cap, 100 further candidates were read from the search listings and
top-of-all-time pages, and every `report` and `take` among them was added
(73 posts), plus the 10 pre-2025 `question` posts from the same pools so the
older era is not all one label. Each row's text is the post title, a blank
line, then the full body, untrimmed. Provenance for every post read, included
or not, is in `data/source_manifest.csv` (post id, permalink, date, listing,
selection group, label, reason), joined to `labels.csv` by a hash of the text.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->
Pre-labelled by AI, correction pending. The assistant read each post (title and
body; for posts over about 3,000 characters the opening and the final 700
characters in full and the race narrative in between skimmed) and applied rule
1 (open/closed), rule 2 (whose case) and the word-share tie-break from the
Label Taxonomy. Every `note` reads `ai_prelabel; human_review_pending`; the 72
rows the assistant judged borderline also name the competing label and the
reason. **I have not yet labelled anything cold.** My 20 cold posts are drawn
at random from the core (excluding the 39 posts already shown with labels in
Milestone 2) and sit in `data/cold_label_queue.csv` with no labels or hints.
`validate_dataset.py` checks the file (columns, empties, labels, duplicates,
the 70% cap, provenance coverage) and passes.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `question` | 150 | 56.0% |
| `report` | 57 | 21.3% |
| `take` | 61 | 22.8% |
| **Total** | 268 | 100% |

No label exceeds 60%. In a 15% test split about 9 `take` and 9 `report` posts
land, just above the notebook's "thin" threshold of 8.

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* `1wxukty` — "my first marathon - an immediate reflection & seeking
> feedback": 10,500 characters of race report ending "I think it was
> predominantly neuromuscular fatigue. Agree/disagree? […] Don't pull your
> punches here, I am here to learn from your wisdom and experience!"
>
> *Could have been:* `report` or `question`.
>
> *I chose, because:* `report` (AI call, awaiting my confirmation). Strike the
> asks and what is left is closed: race run, own diagnosis stated, plan made.
> The title's "seeking feedback" does not override the body, or every race
> report that ends with "thoughts?" would flip.

**2.**
> *The post:* `lvi0qd` — "PSA: Get a blood test!": a detailed account of
> sudden slowdowns, a haemoglobin of 6 and an emergency transfusion, ending
> "If you find that your performance suffers all of a sudden, please consider
> a blood test."
>
> *Could have been:* `take` or `report`.
>
> *I chose, because:* `take` (AI call). The claim is addressed to all runners
> and the story is told as evidence for it; rule 2 is applied before word
> share, even though the narrative is about 85% of the words. Six other
> "PSA + story" posts were labelled the same way for consistency; the student
> can move all seven together if they prefer the word-share reading.

**3.**
> *The post:* `1r32xpy` — "How to not let running & past race performances
> become your part of your self-identity?": 3,600 characters on burnout, a
> sold marathon bib and guilt, ending "Not sure where to go from here […] Can
> anyone relate & empathize with any of this? Any feedback, thoughts??"
>
> *Could have been:* `question` or `report`.
>
> *I chose, because:* `question` (AI call). Despite the long narrative the
> situation is unresolved and the post asks for feedback; open → `question`.
> Contrast case 1, where the account ends in a conclusion.

More cases, the full selection logic and the list of excluded posts are in
[docs/labeling_decisions.md](docs/labeling_decisions.md).

**Sampling bias and limitations:** `report` and `take` are over-represented
relative to the community (the natural standalone-post mix in 2025–26 is about
three-quarters questions). About half of the `report` rows and most of the
`take` rows come from 2011–2024 because that is where opinion posts and PSAs
were found, while nearly every `question` is from 2025–26; a model could learn
era cues as a proxy for label. Six very short thread-starter posts are labelled
`question` and marked borderline. Posts over 128 tokens are truncated by the
notebook, which hits race reports hardest.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

> **Status (14 October 2026): PROVISIONAL RUN.** This run used the AI-pre-labelled
> `labels.csv` before any of my own review and without the 20 cold posts. It
> proves the pipeline end to end and gives a first number; it must be re-run
> on the corrected file, and the numbers below will be replaced then.

**Base model:** `distilbert-base-uncased` (the notebook default), fine-tuned
for 3-way sequence classification.

**Settings:** <!-- epochs, learning rate, batch size, seed -->
epochs 3, learning rate 2e-5, batch size 16, max length 128 tokens, seed 42
(all notebook defaults). Label map by list position: `question` = 0,
`report` = 1, `take` = 2.

**Anything I changed from the defaults, and why:** Nothing in the training
configuration. Two environment facts worth recording: the run used Python
3.13.15 in the project `.venv` with torch 2.11.0+cu128 on
`cuda` (NVIDIA GeForce RTX 4060 Laptop GPU); and `pyarrow` is pinned to 20.0.0 in
that environment because Windows Application Control blocked a DLL in the
26.0.0 wheel, which stopped `datasets` from importing. Neither changes what the
model sees. The notebook was executed in place through its first five
sections only (unit 6 cells untouched) using the `.venv` kernel.

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->
train 186 / val 41 / test 41, stratified by label, seed 42.

| Label | Train | Val | Test |
|---|---|---|---|
| `question` | 104 | 23 | 23 |
| `report` | 39 | 9 | 9 |
| `take` | 43 | 9 | 9 |

No label had fewer than 8 posts in the test split, so the notebook raised no thin-label note.
The pre-training check reported no [look at] or [FIX ME] lines.

**Output artefacts:** `results.json` (accuracy, macro F1, per-label precision /
recall / F1 / support, confusion counts, confidence thirds, device, torch
version, max length) and `test_split.csv` (the 41 held-out posts, text
and label, which `baseline.py` reads next unit). Both committed. The notebook's
checkpoints go to `takemeter_out/`, which is git-ignored.

**Truncation warning:** the model reads only the first 128 tokens of each
post. Under the DistilBERT tokenizer, 87 of 150 `question`
posts (58%), 53 of 57 `report` posts
(93%) and 51 of 61 `take` posts (84%)
are longer than that (median lengths 149 / 1064 / 282
tokens). Race reports are the hardest hit: the template header and goals table
fill the window, and the outcome, lessons and any closing ask — the signals the
taxonomy's rule 1 depends on — fall outside it. The model is therefore learning
`report` largely from openings. Raising MAX_LENGTH to 256 is the obvious
unit 6 experiment; it roughly doubles time and memory.

**What the run shows:** training loss fell 1.040 → 0.981 → 0.892 over the
three epochs, but validation accuracy stayed at 0.561 after every epoch, which
is exactly the `question` share of the validation split, and the confusion
counts in `results.json` show every one of the 41 test posts predicted
`question`. With 186 training posts and batch size 16, three epochs are
about 36 optimizer steps at 2e-5, and the model never left the majority-class
solution. This is a genuine result of the default settings on this dataset,
not a bug: the label check passed, the split is stratified, and the loss moves
in the right direction. It was **not** re-run with other settings, because a
change made after reading these numbers would be tuning against the test
split. Candidates for the unit 6 improvement step, recorded now before the
three-seed runs: more epochs (8–10), a higher learning rate (5e-5), or
MAX_LENGTH 256 for the race reports.

**Numbers from this provisional run** (copied from `results.json`, unrounded
there): accuracy 0.561, macro F1 0.240; per-label F1
`question` 0.719 (n=23),
`report` 0.000 (n=9),
`take` 0.000 (n=9); most-confident
third accuracy 0.846 vs least-confident third
0.462 (n per third 13).
Not a verdict on the criteria: unit 6 does that across three seeds, on the
reviewed dataset.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

<!-- Filled in as the project goes. Milestone 1 entry below; later milestones
     add theirs. -->

**Milestone 1 — community research (14 October 2026)**

- *What I asked for:* an AI assistant (Claude) to evaluate r/running,
  r/boardgames and r/nba against the brief, fetch a varied sample of real
  posts from the chosen community, and record for each post what is
  observable in its text.
- *What came back:* r/nba's top posts turned out to be mostly clips and quote
  cards with no body text (19 of 25), r/boardgames was about a quarter image
  posts, and r/running was almost all text; 40 r/running posts with links and
  four candidate distinctions, in `docs/community_review.md`.
- *What I changed:* <!-- student: record here what you corrected after reading
  the posts yourself, e.g. a summary you disagreed with or a characteristic
  code you changed. Leave nothing here only if you changed nothing. -->

**Milestone 2 — taxonomy and boundary testing (14 October 2026)**

- *What I asked for:* labels grounded in the Milestone 1 posts, a decision
  rule for the hardest boundary with both sides argued, eight synthetic
  boundary posts, and an audit of the rules against every real post read.
- *What came back:* three labels (`question`, `report`, `take`) with real
  examples, the open/closed rule, the audit in `docs/label_taxonomy.md`, and
  the eight synthetic posts in `docs/taxonomy_stress_test.md`. The first rule
  draft failed on a real gear-question post and was rewritten (revision log
  in the taxonomy file).
- *What I changed:* <!-- student: after classifying the eight synthetic posts
  yourself and confirming the post-15 call, record here what you changed. -->

**Milestone 4 — collection and pre-labelling (14 October 2026)**

- *What I asked for:* collect 220–250 real r/running posts within Reddit's
  access rules, reserve 20 for my cold labelling, pre-label the rest under the
  written rules, keep provenance for every post, and validate the file.
- *What came back:* 610 unique posts fetched from public feeds; 291 read in
  full; `labels.csv` with 268 rows, a manifest of all 311 posts touched, a
  20-post cold queue, `validate_dataset.py`, and `docs/labeling_decisions.md`.
  The core listings were 76% questions, so `report` and `take` posts were
  added from opinion-heavy listings and that choice is documented as a bias.
- *What I changed:* <!-- student: record your corrections to the AI labels
  here (how many rows, which direction) once you have reviewed them. -->

**Milestone 5 — training run (14 October 2026)**

- *What I asked for:* build the `.venv`, run `test.py`, set the notebook's
  name, email and labels, and execute sections 1–5 on the real `labels.csv`
  with the default settings.
- *What came back:* a passing environment check (Python 3.13.15, CUDA torch
  2.11.0+cu128 on the laptop GPU), one pyarrow pin to get round an
  Application Control block, and a completed run that wrote `results.json`
  and `test_split.csv`. The assistant also measured how many posts exceed the
  128-token window, which turned out to matter most for `report`.
- *What I changed:* <!-- student: after your label review, re-run sections
  1–5 and note here whether the numbers moved. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:** All 268 rows in `labels.csv` were pre-labelled
by an AI assistant (Claude) on 14 October 2026 under the rules in
docs/label_taxonomy.md. As of this commit **none has been read and corrected
by me**; every `note` says `human_review_pending`. The 20 cold posts in
`data/cold_label_queue.csv` have not been labelled by anyone. When I finish
both, this line will say how many AI labels I changed.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
