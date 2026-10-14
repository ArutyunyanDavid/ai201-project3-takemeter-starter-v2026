# Label taxonomy — design, boundaries and audit (Milestone 2)

**Community:** r/running — <https://www.reddit.com/r/running/>
**Built from:** the 40 real posts in [community_review.md](community_review.md) (post numbers below refer to its table)
**Stress test:** [taxonomy_stress_test.md](taxonomy_stress_test.md) (eight synthetic posts, clearly marked as not real)
**Date:** 14 October 2026

> **Status.** Proposed by an AI assistant (Claude) from the Milestone 1 reading and checked against all 40
> posts. The student has not yet confirmed the labels, the hardest-boundary call, or the stress-test
> classifications. Section 8 lists what needs confirming. No dataset has been collected and no model trained.

---

## 1. Why these three labels

Milestone 1 found two distinctions that two readers would apply the same way most of the time: whether a
post **asks** the community for something or **tells** it something (distinction A), and whether what it
tells is the writer's **own experience** or a **general claim** (distinction B). Put together they give three
kinds of post, and every eligible post in the sample falls into one of them. The other two distinctions
(load-bearing facts, emotional register) are real but graded, and in r/running nearly every post contains
numbers, so they are used inside the definitions and as notes, not as labels.

A fourth label for news relays was considered and rejected: only 5 of 40 posts link out, three of those
have under two sentences written by the poster (so the classifier would be reading the BBC's prose), and the
two that do have the poster's own words fit `take`. The out-of-scope rule in section 5 handles the rest.

---

## 2. The labels

### `question`

**Definition (one sentence):** The post exists to get something from readers — an answer, advice, a
recommendation, a verdict on the writer's own situation, or others' experiences — and whatever else it
contains is there to set that request up.

**Observable signals**

- A question addressed to readers, or "any recommendations / advice / thoughts / experiences?"
- The writer's situation is still open: a decision not yet made, a problem not yet solved, a thing not yet
  found (a race in two weeks, pain on every run, a singlet they have not found).
- Context blocks (age, weekly mileage, race date, what has been tried) followed by the ask; sometimes
  literally headed BACKGROUND / QUESTIONS.
- The post would be pointless without replies.

**Real example 1** — post 20, [Should a beginner ditch speed training?](https://www.reddit.com/r/running/comments/1x3v0k6/should_a_beginner_ditch_speed_training/) (12 Oct 2026)

> BACKGROUND: Hello! I am a 23 y/o, 88 kg male with Stage 1 Hypertension (controlled) and no prior sports
> background. I have been running for 15 weeks now, with my training composed of (1) a tempo run, (2) speed
> interval training, and (3) a long run via run-walk method. […] As a beginner, is it okay to ditch speed
> training for now and focus on Zone 2-3 training? […] Should I trust my HR and switch to brisk walking
> instead? Or should I trust my perceived exertion and run at a pace that feels easy for me despite my HR?

Why `question`: strip the asking sentences and what is left is an unresolved situation (dreads intervals,
confused by heart-rate zones) written to set up the asks.

**Real example 2** — post 12, [Garmin or Strava prediction: which is more accurate?](https://www.reddit.com/r/running/comments/1wrosne/garmin_or_strava_prediction_which_is_more_accurate/) (27 Sep 2026)

> I have a half marathon in two weeks time and am at the end of my training block. There's a 7 minute
> difference between my Garmin estimated time and my Strava estimated time. They have the same input. […]
> Questions: Which do you value more? Why do you think they vary so much?

Why `question`: short, numeric, and nothing remains once the two questions are removed.

**Exclusions (when a similar post is *not* `question`)**

- A complete account that ends with an invitation to share ("anyone else?", "lend me your tales", "swap
  notes") is `report` (posts 3, 28, 40).
- A stated position with its reasons that ends with "what does everyone think?" is `take` (posts 23, 30).
- A one-line ask inside an otherwise finished account is an aside; the account's label stands (post 13).

### `report`

**Definition (one sentence):** The post's substance is a firsthand account of something the writer did or
went through — a race, a training block, a product or method they used, a streak, a change of attitude —
told with its specifics and its outcome, and it stands complete without replies.

**Observable signals**

- First person, past tense; what happened, in order; an outcome (a time, a result, a verdict on the thing
  used) and usually "what's next".
- The subreddit's race-report template: race / date / time, a goals table, splits, Training, Race, What's
  next.
- Detail density: splits, weekly mileage, gram quantities, days of a streak.
- Conclusions, where drawn, are about the writer's own case: *my* race, *my* plan, the app *I* used.

**Real example 1** — post 8, [Race Report - Loch Ness Marathon - PB, BQ, SUB 3](https://www.reddit.com/r/running/comments/1wuzdvc/race_report_loch_ness_marathon_pb_bq_sub_3/) (1 Oct 2026)

> Race: 2026 Loch Ness Marathon Date: September 27, 2026 Time: 2:58:34 Goals […] A PB (Sub 3:20) Yes B BQ
> (Sub 3:05) Yes C Sub 3 Yes Background I have had a on again/off again relationship with running over the
> years […]

Why `report`: a template race report with training, race narrative and "what's next"; no question asked.

**Real example 2** — post 5, [I successfully reverse-engineered Maurten Gel 100](https://www.reddit.com/r/running/comments/1whzccf/i_successfully_reverseengineered_maurten_gel_100/) (16 Sep 2026)

> TL;DR: I perfected a DIY Maurten Gel 100 clone using the exact same internal-gelation mechanism (Sodium
> Alginate + Calcium Carbonate + GDL). This recipe makes a 10-serving batch. Each 50g pouch delivers exactly
> 25g of carbohydrates at a 0.8:1 Fructose-to-Glucose ratio […]

Why `report`: what the writer made, how, and the result, from their own test batches; nothing is asked.
Included on purpose as a non-race report so the label is not "race report" by another name.

**Exclusions**

- If the account is unfinished and exists to set up a request (a race in twelve days, a decision between two
  marathons), it is `question` (posts 18, 19).
- If the writer's experience is offered as evidence for a claim about running or runners in general, and that
  claim is the point, it is `take` (see rule 2 below).

### `take`

**Definition (one sentence):** The post's substance is a claim or argument about running, runners, races,
training methods, running culture or an event, going beyond the writer's own case, put forward for readers to
agree or argue with rather than to answer or to witness.

**Observable signals**

- Present-tense generalisations: "NSM is heading down the same road as cycling", "races have gotten worse",
  "run clubs please use track etiquette".
- Verdicts and superlatives about things the writer did not do themselves: "greatest marathon in history",
  "coverage was absolutely terrible".
- The writer's experience, if present, is cited as evidence for the general claim rather than being the
  content.
- News relayed in the writer's own words *with* the writer's judgment attached.
- Sometimes self-labelled ("I've got a hot take", "unpopular opinion", "rant over").

**Real example 1** — post 16, [Norwegian Singles Method. A suboptimal approach](https://www.reddit.com/r/running/comments/1wtk6v6/norwegian_singles_method_a_suboptimal_approach/) (29 Sep 2026)

> I've got a hot take for the Norwegian Singles Method that might ruffle some feathers. […] I think NSM is
> heading down the same road as cycling and FTP. […] Does NSM work well for a lot of people? Yes, 100%. Is it
> going to leave a lot of people significantly below their true potential. I think so.

Why `take`: a general claim about a training method, argued by analogy, with no personal data and no
question.

**Real example 2** — post 34, [LA Marathon men's finish was wild-and coverage was terrible!](https://www.reddit.com/r/running/comments/1roa4ql/la_marathon_mens_finish_was_wildand_coverage_was/) (8 Mar 2026)

> American Nathan Martin won the LA Marathon this morning in 2:11:18, coming from behind in a massive sprint
> to the finish. At least I think that's what happened, because the coverage was absolutely terrible. […]
> There was never info about how far ahead Kimani Kamau was from anyone else […]

Why `take`: a judgment about an event (the broadcast), supported by what the writer saw on TV; the writer
did not run the race and asks nothing. Chosen as the second example because it is heated and recent, which
shows that tone and immediacy do not move a post out of `take`.

**Exclusions**

- A verdict on something the writer used themselves (an app for a year, a plan for a block) is `report`
  (post 36).
- A claim the writer asks readers to settle for them, without taking a position, is `question` (post 39:
  "why does this rule exist?").
- A link plus under two sentences of the poster's own words is out of scope (posts 4, 38).

---

## 3. The two decision rules

**Rule 1 — `question` vs `report`/`take`: the open/closed rule.**
Strike every sentence that asks readers for something. If nothing of substance is left, the post is
`question`. Otherwise ask whether what is left is *closed* or *open* for the writer. **Closed** means the
account has its outcome and the writer's own conclusion (`report`), or the claim is stated with its reasons
(`take`). **Open** means a problem unsolved, a choice unmade, or a thing not yet found, with the context
there to set up the ask: `question`. Title words such as "question" or "seeking feedback" do not override
the body. A single open line inside an otherwise closed account is an aside, and the account's label stands.

**Rule 2 — `report` vs `take`: whose case is the claim about?**
If the conclusions are about the writer's own case — their race, their plan, the product they used — it is
`report`, even if a general lesson is drawn in passing. If the claim is about running, runners, races,
methods, culture or an event beyond the writer's own case, and the writer's experience is offered as
evidence for it, it is `take`. A verdict on a product the writer used is `report`; a verdict on a method as
such, a culture, a broadcast, or a race the writer did not run is `take`.

**Tie-break (only after rules 1 and 2):** label by the part the post spends most of its words on.

---

## 4. The hardest boundary: `question` vs `report`

**The post:** post 15, [my first marathon - an immediate reflection & seeking feedback](https://www.reddit.com/r/running/comments/1wxukty/my_first_marathon_an_immediate_reflection_seeking/) (5 Oct 2026, about 10,500 characters).

A physician who finished a first marathon that morning writes a full account — Higdon Novice 1, hockey twice
a week, a hip-flexor setback seventeen days out, race-day nutrition, going out with the 3:30 pacer, total-body
cramping from mile 18, first 17 miles in 133 minutes and the last 9.2 in 108 — then writes:

> So here's where I would love confirmation versus alternative explanations, as well as advice on what I
> should do better next year […] I think it was predominantly neuromuscular fatigue. Agree/disagree? […]
> I am undecided whether electrolyte imbalance was a factor. Happy to be told either way […] Other critiques
> and thoughts are welcome. […] Don't pull your punches here, I am here to learn from your wisdom and
> experience!

**The case for `question`.** The title says "seeking feedback". The writer explicitly asks for
"confirmation versus alternative explanations, as well as advice on what I should do better next year", and
lists open items (salt tablets? interval training?). The post's stated purpose is to get answers. Under a
purpose-first reading this is the clearest kind of question there is.

**The case for `report`.** Around nine-tenths of the words are a complete race report with an outcome and
the writer's own diagnosis ("I think it was predominantly neuromuscular fatigue") and plan ("I am gonna give
this another go"). The asks are requests to critique conclusions the writer has already drawn, plus
next-year items. By rule 1, what remains after striking the asks is closed, not open. The staff taxonomy's
own tie-break (most of its words) points the same way. Labelling it `question` would also mean that any
race report with an "agree?" at the end flips label, which is exactly the inconsistency the rule exists to
prevent.

**Chosen label: `report`.** The deterministic rule for future posts of this kind is rule 1 as written:
strike the asks; if the account has its outcome and the writer's own conclusion, it stays `report`
regardless of the title. The student should confirm this call (section 8); if the student prefers
`question`, rule 1 must change to "any explicit request for advice about the writer's own next steps makes
the post `question`", and the audit in section 6 shows which other posts that would move (15 → question;
13 stays `report` only via the aside clause; 32 and 40 unaffected).

---

## 5. Scope: what gets labelled at all

Applied before any label:

1. Exclude posts by AutoModerator and the recurring scheduled threads (daily Achievements, Official Q&A,
   Shoesday, Weekly Training Thread, and the rest listed in community_review.md section 3). They are
   containers for comments.
2. Exclude posts whose body is a URL and/or quoted third-party text with fewer than two sentences written by
   the poster. In the sample: posts 4 and 38.
3. Everything else is in scope and gets exactly one label. The `text` column of the dataset will contain the
   title followed by the body, because titles carry label signal ("Race Report:", "Recommendations?") and
   are part of what readers see.

---

## 6. Consistency audit: all 40 posts labelled under the rules

Provisional labels by the AI assistant, applied with rules 1 and 2. "Clear" means both rules gave the answer
without the tie-break; "borderline" means the tie-break or an aside clause was needed, or two readers could
plausibly differ. **These are not dataset labels.** They are a dry run of the rules, for the student to check.

| # | Post (short title) | Label | Confidence | Why |
|---|---|---|---|---|
| 1 | Road Racing Etiquette Question | `question` | borderline | Anecdote is complete, but the writer's situation (was I wrong?) is open; the account exists to set up the verdict. |
| 2 | How to keep focused | `question` | clear | Nothing left once the ask is struck. |
| 3 | LA Marathon after brain surgeries | `report` | clear | Closed story; closing line is an invitation. |
| 4 | Injured Assefa… | out of scope | clear | Copied BBC text, no poster words. |
| 5 | Reverse-engineered Maurten | `report` | clear | Own method, own result. |
| 6 | How to carry gels for 2:30 | `question` | clear | Open: has not chosen a method. |
| 7 | Low HRV before race | `question` | clear | Open: race tomorrow. |
| 8 | Loch Ness race report | `report` | clear | Template report, no ask. |
| 9 | Tokyo lottery results | `question` | borderline | Nothing of substance remains; a thread starter. Fits the rule, but it is barely a post. |
| 10 | Winter Running | `question` | clear | Three asks; the PR line is context. |
| 11 | Running singlet | `question` | clear | Open: the singlet has not been found; complaint is context. |
| 12 | Garmin vs Strava | `question` | clear | |
| 13 | Berlin race report | `report` | clear (aside clause) | One-line trip ask inside 10,000 characters. |
| 14 | Picking a Marathon | `question` | clear | |
| 15 | First marathon, seeking feedback | `report` | **hardest** | Section 4. |
| 16 | Norwegian Singles Method | `take` | clear | |
| 17 | Melissa's Road Race | `report` | clear | |
| 18 | Back-to-back marathons | `question` | clear | Open decision. |
| 19 | First half taper | `question` | clear | Open decision. |
| 20 | Beginner speed training | `question` | clear | |
| 21 | Introduce gels | `question` | clear | |
| 22 | Open headphones | `question` | clear | |
| 23 | Have races gotten worse? | `take` | borderline | Position stated with reasons (prices, one memory); the asks invite agreement. Title is a question, body is not. |
| 24 | Nausea/reflux | `question` | clear | |
| 25 | Split strength training | `question` | clear | |
| 26 | Chicago race report | `report` | clear | |
| 27 | Jeff Galloway dies | `take` | borderline | Eligible by exactly two poster sentences; those sentences make a claim about Galloway's impact. Low-content case. |
| 28 | Mental gymnastics | `report` | borderline | Closed anecdote about the writer's own pattern; "every single time" is about themselves. Could be read as a general claim. |
| 29 | Started running at 39 | `question` | clear | Open: wants to know what comes next. |
| 30 | Run club phenomenon | `take` | clear | Essay with a position; closing ask is an invitation. |
| 31 | Self-destructive running | `question` | clear | |
| 32 | Stopped chasing PBs | `report` | borderline | Own shift is the substance; the research claim explains it. Rule 2 says report; a reader could see the claim as the point. |
| 33 | Slower runners mocked | `question` | clear | |
| 34 | LA Marathon coverage | `take` | clear | |
| 35 | Track etiquette | `take` | clear | Claim addressed to a group; one incident as evidence. |
| 36 | Runna review | `report` | clear (rule 2) | Verdict on a product the writer used for a year. |
| 37 | History in the Marathon | `take` | clear | "Greatest marathon in history" about a race the writer did not run. |
| 38 | London ballot record | out of scope | clear | One line plus a link. |
| 39 | Marathon course rule | `question` | borderline | Writer states a position (should be point-to-point) but the post is organised around a factual question they cannot answer; tie-break by words. |
| 40 | Streakers | `report` | clear | Long closed story; title is an invitation. |

**Counts (38 eligible):** `question` 20 (53%), `report` 11 (29%), `take` 7 (18%), out of scope 2.
Borderline: 7 of 38; no label is purely a quality judgment; similar posts got the same label (the four
template race reports are all `report`; the twelve short advice requests are all `question`).

**Two consequences for later milestones, recorded now:**

- `take` is the smallest class. At these shares a 200-post dataset would hold about 36 takes and about 5 in
  the test split, so its F1 will swing between seeds. Milestone 3's criterion for `take` should be looser
  than for `question`, and Milestone 4 should deliberately draw more posts from the top-of-year and all-time
  listings, where opinion posts concentrate, to lift `take` toward 25%.
- `question` at 53% is under the 70% cap but should be watched during collection; the newest-posts listing
  is question-heavy.

---

## 7. Audit checklist

| Check | Result |
|---|---|
| Between two and four labels | Pass — three. |
| Exactly one definition sentence per label | Pass — section 2. |
| Two authentic examples per label | Pass — six real posts, quoted from the feed text, with permalinks. |
| Example sources traceable | Pass — every example links to its r/running permalink and appears in community_review.md. |
| Labels are not subjective quality judgments | Pass — each label names what the post *does*; none says good/bad/interesting. |
| Similar posts receive similar labels | Pass on the 38 (section 6); 7 borderline cases documented with the rule that decided them. |
| Boundary rules explicit and repeatable | Pass — rules 1 and 2 plus a tie-break, in section 3; applied to all 38. |
| No obvious overlap or uncovered type | Pass with a note — news relays with the poster's own words go to `take`; link-only relays are excluded by rule, not left uncovered. |
| All eight synthetic tests reviewed | Pass by the assistant; **student review pending** (taxonomy_stress_test.md). |
| Synthetic examples separated from real ones | Pass — synthetic posts live only in taxonomy_stress_test.md, each headed "SYNTHETIC"; none appears in this file, the README, or community_review.md. |

**Readiness for labelling 200 posts (Milestone 4):** ready, subject to the student's confirmation of the
hardest-boundary call. The rules survived all 38 eligible real posts and the eight synthetic ones with one
revision (section 9). The two residual risks are the size of `take` and the handful of "closed anecdote with a
closing invitation" posts (28, 32), which the student should label with rule 2 in front of them.

---

## 8. What the student must confirm

- [ ] The three labels and their one-sentence definitions.
- [ ] The hardest-boundary call: post 15 is `report` under rule 1 (section 4). If you disagree, say which
      version of rule 1 you want, and the audit table will be re-run.
- [ ] The eight synthetic classifications in taxonomy_stress_test.md, labelled independently first.
- [ ] The scope rules in section 5 (title + body as the text; link-only posts excluded).
- [ ] The provisional labels in section 6, or the numbers you would change.

---

## 9. Revision log

| When | What changed | Why |
|---|---|---|
| 14 Oct 2026, first draft | Rule 1 was first written as "delete the asking sentences; if what remains is a complete report or argument, label by it; otherwise `question`". | Testing against post 11 (singlet) gave `take`, because the complaint about "fashion tax" read as a complete argument, although every reader would call it a gear question. |
| 14 Oct 2026, revision 1 | Rule 1 rewritten around *open vs closed*: a situation still unresolved for the writer is `question` however much argument or narrative precedes the ask. | Fixes post 11 and also settles posts 1 and 39 without a tie-break. Post 15 is unaffected (its account is closed). |
| 14 Oct 2026, revision 2 | Added the "aside" clause to rule 1. | Post 13 (Berlin report) has a one-line trip ask inside a 10,000-character report; without the clause rule 1 would have had to go to the tie-break. |
| 14 Oct 2026, revision 3 | Dropped a fourth label (`news`). | Only 2 of 5 link posts had enough poster text to classify; both fit `take`. A 10% label would have had 2–3 examples in the test split. |

*Prepared with AI assistance (Claude). Synthetic test posts are in taxonomy_stress_test.md only.*
