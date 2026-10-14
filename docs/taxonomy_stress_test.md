# Taxonomy stress test — eight SYNTHETIC posts (Milestone 2)

> **Every post in this file is made up.** They were written by an AI assistant (Claude) on 14 October 2026
> to probe the boundaries of the taxonomy in [label_taxonomy.md](label_taxonomy.md). None of them was posted
> to r/running, none quotes a real post, and none may be used as dataset rows. The races, products, times and
> people named in them are invented or used generically. Real posts live only in
> [community_review.md](community_review.md).

**Taxonomy under test**

| Label | Definition |
|---|---|
| `question` | The post exists to get something from readers — an answer, advice, a recommendation, a verdict on the writer's own situation, or others' experiences — and whatever else it contains is there to set that request up. |
| `report` | The post's substance is a firsthand account of something the writer did or went through, told with its specifics and its outcome, and it stands complete without replies. |
| `take` | The post's substance is a claim or argument about running, runners, races, methods, culture or an event, beyond the writer's own case, put forward for readers to agree or argue with. |

**Rule 1 (open/closed):** strike the asking sentences; nothing left → `question`; what is left is closed
(outcome + own conclusion, or claim + reasons) → `report`/`take`; what is left is open (unsolved, undecided,
not yet found) → `question`. Titles do not override. A single open line in a closed account is an aside.
**Rule 2 (whose case):** conclusions about the writer's own case → `report`; a claim about running beyond the
writer's case, with experience as evidence → `take`. **Tie-break:** most of its words.

**How to use this file:** the student should classify each post *before* reading the "Applying the rules"
block, write their label in the "Student's label" line, and then compare.

---

## SYNTHETIC 1 — a finished race with a feedback request at the end

*Boundary probed:* `report` vs `question` (the hardest boundary).

> **Title:** Riverbend Half race recap — where did I lose 4 minutes?
>
> Ran the Riverbend Half this morning. Goal was 1:45, finished 1:49:12. Training was 11 weeks, peaked at 38
> miles, long run of 13. Went out with the 1:45 pacer and felt great through 7 miles (7:58 average), then the
> two climbs on the river path took more out of me than I expected and I drifted to 8:40s for miles 9–11.
> Nutrition was one gel at 45 minutes, which I think was about right. Legs are fine tonight. My read is that I
> didn't do enough hill work — my long runs were all flat. Next block I'm adding a hilly long run every other
> week. If anyone has run Riverbend, did the climbs cost you the same? And would you have taken a second gel?

**Could be:** `report` or `question`.

**Applying the rules.** Strike the two asking sentences. What remains has an outcome (1:49:12), the writer's
own diagnosis (not enough hill work) and a plan (hilly long runs). That is closed → `report`. The asks are
a request to compare notes on a finished race plus one open item (second gel), neither of which makes the
situation open.

**Label: `report`.**

**Remaining ambiguity:** moderate. The title is phrased as a question. A labeller who reads the title first
will lean `question`; the rule says titles do not override. This is the same shape as real post 15 and is
decided the same way.

**Student's label:** ______

---

## SYNTHETIC 2 — long context, nothing resolved

*Boundary probed:* `question` vs `report` when the context is long and detailed.

> **Title:** Shin pain only on the left side, 6 weeks in — what am I doing wrong?
>
> 31F, started running in late August on a couch-to-10K plan, three runs a week, currently 25 minutes
> continuous. Shoes are a neutral pair fitted at a running store in September. About two weeks ago I started
> getting a dull ache on the inside of my left shin that shows up around minute 10 and fades by the time I'm
> home. No pain walking, no swelling. I've tried slowing down, running on grass instead of pavement, and
> taking an extra rest day, and it's the same. I haven't seen anyone about it. Is this the start of shin
> splints? Should I stop running entirely for a couple of weeks, or is it okay to keep going at this level?

**Could be:** `question` or `report`.

**Applying the rules.** Strike the asks. What remains is a detailed description of a problem that is still
there: the writer has tried three things and none worked, and has not decided what to do. That is open →
`question`, however much narrative precedes the ask.

**Label: `question`.**

**Remaining ambiguity:** low. The context is long but has no outcome.

**Student's label:** ______

---

## SYNTHETIC 3 — an opinion wearing a question mark

*Boundary probed:* `take` vs `question` when the title asks and the body argues.

> **Title:** Are carbon-plated shoes basically mandatory for a BQ now?
>
> I've been looking at the qualifying lists for the last few years and the shift is obvious. Everyone at the
> front is in plates, and the people I know who went from 3:10 to 3:02 did it the year they switched shoes,
> not the year they changed training. The standards haven't moved to match, which means the qualifying time
> is quietly a different test than it was in 2015. I don't think that's good for the sport. The shoes are
> legal, fine, but we should stop pretending a BQ in 2026 means the same thing. Curious whether people agree
> or think I'm overstating it.

**Could be:** `take` or `question`.

**Applying the rules.** Strike the asks (the title question and the last sentence). What remains is a stated
position ("a BQ means something different now", "not good for the sport") with reasons (who switched, the
standards not moving). Closed → `take`. Rule 2: the claim is about the sport, not the writer's own race →
`take`, not `report`.

**Label: `take`.**

**Remaining ambiguity:** low under the rules, but a labeller going by the title alone would say `question`.
Same shape as real post 23.

**Student's label:** ______

---

## SYNTHETIC 4 — curiosity with no position

*Boundary probed:* `question` vs `take` when the topic is general but the writer takes no side.

> **Title:** Why do big city marathons all start so early?
>
> Every major I've looked at starts the elite field between 7 and 8am and the last wave is usually off by
> 10. I get that heat is part of it, but Berlin in late September isn't exactly hot, and the start areas are
> chaos at that hour. Is it road-closure cost? TV windows? Something about the elite fields' routines?
> Genuinely don't know and would like to hear from anyone who's worked on the organising side.

**Could be:** `question` or `take`.

**Applying the rules.** Strike the asks. What remains is a description of what the writer has noticed and a
statement that they do not know the reason. No position is taken, so there is no claim to be closed. Open →
`question`.

**Label: `question`.**

**Remaining ambiguity:** low. Contrast with Synthetic 3: the difference is whether the writer has a position.
Real post 39 sits between the two, which is why it is marked borderline in the audit.

**Student's label:** ______

---

## SYNTHETIC 5 — a verdict on something the writer used

*Boundary probed:* `report` vs `take` for reviews.

> **Title:** Two blocks on a 5-day plan vs one on a 6-day plan, same goal race, what I found
>
> Same 10K, three years running. Years one and two I used a five-day-a-week plan from a book, peaking at 35
> miles: 44:50 and 44:10. This year I switched to a six-day plan with doubles on Tuesdays, peaking at 48
> miles, and ran 42:31. Resting HR dropped from 52 to 47 over the block. The extra easy day did more for me
> than any of the workouts, I think — the quality sessions were almost identical across the three plans. I
> wouldn't say this proves anything beyond my own legs, but for me, frequency beat intensity. Sticking with
> six days.

**Could be:** `report` or `take`.

**Applying the rules.** No asks, so rule 1 is not needed. Rule 2: every conclusion is scoped to the writer
("for me", "beyond my own legs"), about plans the writer followed. → `report`.

**Label: `report`.**

**Remaining ambiguity:** low. The post even disclaims the general version of its claim. Same shape as real
post 36.

**Student's label:** ______

---

## SYNTHETIC 6 — own experience as proof of a general claim

*Boundary probed:* `take` vs `report` when the evidence is firsthand but the claim is general.

> **Title:** 12 weeks of Norwegian singles took 90 seconds off my 10K. Everyone under 45 min should be doing this.
>
> Did the sub-threshold thing for 12 weeks: three sessions a week, all at 10K pace plus 20 seconds, nothing
> hard. Went from 44:40 to 43:10 with less fatigue than I've ever had in a block. That's the point, though —
> it's not that it worked for me, it's that it's obviously the right way to train for anyone in the 40–50
> minute range and the sub is still arguing about VO2 max sessions. The hard-interval people are training for
> a different sport. If you're a recreational runner and you're not doing this, you're leaving minutes on the
> table.

**Could be:** `take` or `report`.

**Applying the rules.** No asks. Rule 2: the writer's block is offered as evidence ("that's the point,
though") for a claim about everyone in a pace range and about how the sub trains. The claim is the point and
it goes beyond the writer's case → `take`.

**Label: `take`.**

**Remaining ambiguity:** moderate. Roughly half the words are a firsthand account with numbers, so a labeller
who weights word count before applying rule 2 will say `report`. Rule 2 comes before the tie-break for
exactly this reason. Compare Synthetic 5, which has the same shape of evidence and the opposite scoping.

**Student's label:** ______

---

## SYNTHETIC 7 — a reaction to an event, with a link and a fact

*Boundary probed:* `take` vs `report` vs out-of-scope for news reactions.

> **Title:** Sub-2 in a sanctioned race. The event is officially a different sport now.
>
> [link to a results page] 1:59:30, in a race, with pacers who had to drop out like everyone else. I watched
> the last 5K twice and I still don't believe it. People will say it's the shoes, and it is partly the
> shoes, but a 2:03 twenty years ago was a once-a-decade thing and now there are three men under 2:01 in one
> race. The distance hasn't changed; the event has. Pretty sure we'll look back on this as the line between
> two eras.

**Could be:** `take`, `report` (the writer watched it), or out of scope (news relay).

**Applying the rules.** Scope first: the body is five sentences of the poster's own words, not a copied
article → in scope. Rule 1: no asks. Rule 2: the writer did not run the race; "the event has changed",
"the line between two eras" are claims about the sport, supported by the result → `take`. Watching
something is not a firsthand account of doing it.

**Label: `take`.**

**Remaining ambiguity:** low once the scope rule is applied. Same shape as real posts 34 and 37.

**Student's label:** ______

---

## SYNTHETIC 8 — a closed story with "anyone else?" and a title that says "question"

*Boundary probed:* whether the title's framing overrides the body (`report` vs `question`).

> **Title:** Question for the fasted-running crowd
>
> For two years I ran every morning on black coffee and nothing else because that's what everyone around me
> did. Felt fine up to about 10K, fell apart on anything longer, and assumed that was just how long runs
> felt. This spring I started eating a slice of toast and a banana 40 minutes before heading out. The first
> 16-miler I did fed was the first long run I've ever finished without the last three miles being a shuffle,
> and my average pace over the block came down 15 seconds a mile with no change in training. I'm not going
> back. Anyone else make the switch and wonder why they waited so long?

**Could be:** `question` (title, closing line) or `report`.

**Applying the rules.** Strike the closing ask. What remains has its outcome (the long run finished without
the shuffle, 15 seconds a mile) and the writer's own conclusion ("I'm not going back"). Closed → `report`.
The closing line is an invitation to share, not a request for help; the title does not override.

**Label: `report`.**

**Remaining ambiguity:** low under the rules; moderate for a labeller who reads titles first. Same shape as
real posts 28 and 40.

**Student's label:** ______

---

## Summary

| # | Synthetic post | Two candidate labels | Decided by | Label | Residual ambiguity |
|---|---|---|---|---|---|
| 1 | Riverbend Half recap with feedback request | report / question | Rule 1 (closed account) | `report` | moderate |
| 2 | Shin pain, long context, unresolved | question / report | Rule 1 (open situation) | `question` | low |
| 3 | Carbon plates and the BQ | take / question | Rule 1 (position + reasons) | `take` | low |
| 4 | Why do marathons start early | question / take | Rule 1 (no position) | `question` | low |
| 5 | Two plans compared, scoped to self | report / take | Rule 2 (own case) | `report` | low |
| 6 | Norwegian singles as proof for everyone | take / report | Rule 2 (claim beyond own case) | `take` | moderate |
| 7 | Sub-2 reaction with link | take / report / out of scope | Scope rule, then rule 2 | `take` | low |
| 8 | "Question for the fasted crowd", closed story | report / question | Rule 1 (closed; title does not override) | `report` | low |

**Were any left genuinely ambiguous?** Two are moderate (1 and 6). Both resolve under the rules as written;
the ambiguity is that a labeller who reads the title first (1) or weighs word count before rule 2 (6) will
disagree. The precise improvement already made for this is the ordering in label_taxonomy.md section 3:
scope rule, then rule 1, then rule 2, then and only then the word-share tie-break. No further definition
change is proposed from this test; the one change made during Milestone 2 (rule 1 rewritten around
open/closed) is logged in label_taxonomy.md section 9 and was driven by a real post (11), not a synthetic one.

**Student's results:** ___ of 8 agree with the rule-based label. Disagreements and the student's reasoning:

-
-
