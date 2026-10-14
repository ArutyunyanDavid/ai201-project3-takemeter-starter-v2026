# Labelling decisions — hard cases and how the rules were applied (Milestone 4)

**Taxonomy applied:** [label_taxonomy.md](label_taxonomy.md) (rule 1 open/closed, rule 2 whose case, then word share).
**Who labelled:** an AI assistant (Claude) pre-labelled every row of `labels.csv` on 14 October 2026 after
reading each post's title and body (for posts over about 3,000 characters, the opening and the closing
700 characters were read in full and the middle of the race narrative was skimmed; the closing section is
where asks and conclusions live). **No row has been reviewed by the student yet.** Every row's `note` says
so, and the 72 rows the assistant found borderline name the competing label and the reason.
**What the student must do:** read `data/source_manifest.csv` (or the `note` column) and correct any label;
label the 20 posts in `data/cold_label_queue.csv` without looking at any of this file first.

---

## 1. Where the labels came from, in numbers

| Group | Posts | How selected | Labelled by |
|---|---|---|---|
| Core | 191 read (185 kept, 6 excluded by scope rule) | every eligible post from top-of-year (200 entries), top-of-month, newest and hot listings, minus the 20 cold posts | assistant |
| Top-up | 100 read (95 labelled, 5 excluded) | the first 100 candidates, in order, from: flair:Discussion (year), opinion-keyword search (all time), flair:Discussion (all time), top-of-all-time pages 1–2 | assistant |
| Cold queue | 20 | random draw from the core, excluding the 39 posts already audited in Milestone 2; one link-only draw swapped for an unread post from the same window | **nobody yet** |

From the top-up group only `report` and `take` posts were added, plus the `question` posts dated before
the core window (October 2025) so that the older posts are not all one label. The 12 `question` posts the
Discussion-flair (year) search returned were read but not added, because the core window already supplies
questions in abundance. Every read post, included or not, is in the manifest with its label and reason.

**Why the top-up was needed.** The core listings came out at 76% `question` (140 of 185). That is the real
shape of r/running's standalone posts in 2025–26: the daily Q&A thread absorbs short questions, and the
posts that survive are long questions and race reports, with opinion posts rare. 76% is over the brief's
70% cap, so the dataset could not be the core alone. Rather than discard real questions, the assistant
added real `report` and `take` posts from listings where they concentrate. **Consequence, stated plainly:**
`take` and `report` rows are over-represented relative to the community, and about half of them come from
2013–2024 while nearly all `question` rows come from 2025–26. A model could learn era cues (COVID
references, old product names) as a proxy for label. The pre-2025 `question` rows were included to blunt
that, but it remains a limitation and is recorded in the README.

---

## 2. Hard cases

Each case names the two plausible labels, the chosen one, the exact rule that decided it, and why the
alternative lost. These are real posts; quotes are verbatim.

### Case 1 — a finished account that asks for feedback (the Milestone 2 hardest boundary, re-met)

**Post:** `1wxukty` — [my first marathon - an immediate reflection & seeking feedback](https://www.reddit.com/r/running/comments/1wxukty/my_first_marathon_an_immediate_reflection_seeking/)
> "I think it was predominantly neuromuscular fatigue. Agree/disagree? […] Other critiques and thoughts are
> welcome. […] Don't pull your punches here, I am here to learn from your wisdom and experience!"

**Plausible:** `report`, `question`. **Chosen: `report`.**
**Rule applied:** rule 1. After striking the asks, what remains is closed: the race is run, the writer has
stated a diagnosis and a plan for next year. A title that says "seeking feedback" does not override the body.
**Why `question` lost:** the asks are requests to critique conclusions the writer already drew, not an open
problem the post exists to solve. Labelling it `question` would also flip every race report that ends with
"thoughts?".
**Needs human judgment:** yes. This call is flagged in `label_taxonomy.md` section 8 for the student.

### Case 2 — a finished account with a separate open question at the end

**Post:** `1srw1u2` — [What's next after Boston?](https://www.reddit.com/r/running/comments/1srw1u2/whats_next_after_boston/)
> "Welp, I've completed my first marathon at Boston yesterday. […] Practice running down hills. That is my
> main takeaway. […] TLDR: What do you do in between marathon training blocks?"

**Plausible:** `report`, `question`. **Chosen: `report` (borderline).**
**Rule applied:** rule 1, then word share. The account is closed (3:43:20, a stated lesson, advice to other
Boston runners). The off-season question is genuinely open, but it is a separate item occupying under half
the words; the aside clause does not quite cover it, so the tie-break decided it.
**Why `question` lost:** the post would still be a complete, useful race write-up with the last paragraph
removed; the reverse is not true.
**Needs human judgment:** yes. A reader who weighs the title more will call it `question`; both are
defensible, which is why it is marked borderline.

### Case 3 — a long account of an unresolved situation

**Post:** `1r32xpy` — [How to not let running & past race performances become your part of your self-identity?](https://www.reddit.com/r/running/comments/1r32xpy/how_to_not_let_running_past_race_performances/)
> "Not sure where to go from here other than take it day-by-day. […] Can anyone relate & empathize with any
> of this? Any feedback, thoughts??"

**Plausible:** `question`, `report`. **Chosen: `question` (borderline).**
**Rule applied:** rule 1, open/closed. Despite 3,600 characters of firsthand narrative, the writer says the
situation is unresolved ("not sure where to go from here", "stuck at 55km/week", "hard to not feel guilty")
and asks for feedback. Open → `question`, however much narrative precedes the ask.
**Why `report` lost:** there is no outcome or conclusion; the narrative is context for the ask. Contrast
case 1, where the account ends in a diagnosis and a plan.

### Case 4 — personal experience used as evidence for advice to everyone ("PSA + story")

**Post:** `lvi0qd` — [PSA: Get a blood test!](https://www.reddit.com/r/running/comments/lvi0qd/psa_get_a_blood_test/)
> "My CBC was shocking - HGB of 6 […] I was called in to the emergency room for a blood transfusion. […] If
> you find that your performance suffers all of a sudden, please consider a blood test."

**Plausible:** `take`, `report`. **Chosen: `take` (borderline).**
**Rule applied:** rule 2. The claim ("if your performance drops suddenly, get a blood test") is addressed to
all runners, and the writer's anaemia story is told *as evidence for it* — the title frames the whole post as
a PSA. Rule 2 says experience offered as evidence for a claim beyond the writer's case is `take`.
**Why `report` lost:** on word count alone it would win (about 85% narrative), but rule 2 is applied before
the word-share tie-break. The same reasoning labelled `k9k0h7` (vitamin D), `wgdt0r` (old shoes), `uyghzm`
(race-series refunds), `5046of` (hot bath), `28tpff` (summer heat) and `2qbel5` (dog) as `take`.
**Consistency note:** the opposite case is `vxu07w` (a tree fell in front of the writer), labelled `report`:
the title is the event, the story is the point, and the "PSA" is one closing line. The deciding question is
whether the post is framed as advice (title or opening) with the story in service of it, or as a story with
a lesson tacked on.
**Needs human judgment:** yes. This is a whole class of posts, not one post; the student may prefer the
word-share reading, and if so all seven should move together.

### Case 5 — an opinion framed as a question

**Post:** `1x5bak4` — [Is it just me or have races gotten worse?](https://www.reddit.com/r/running/comments/1x5bak4/is_it_just_me_or_have_races_gotten_worse/)
> "I feel like races prices haven't skyrocketed in recent years, but it seems to me in terms of swag,
> nutrition, and post race goodies have gotten much worse recently. […] Anyone else think races are cutting
> the goodies you get too? Any thoughts on why?"

**Plausible:** `take`, `question`. **Chosen: `take` (borderline).**
**Rule applied:** rule 1. Strike the asks and a position remains ("races have cut the extras") with its
reasons (prices, one remembered race). Closed claim → `take`.
**Why `question` lost:** the asks invite agreement and explanation of a claim already made; nothing about
the writer's own situation is open. Compare `1q4i8fz` (course rule), labelled `question`, where the writer
cannot answer the factual question and the opinion is secondary.

### Case 6 — a rant about being judged, ending in "how do you deal with it?"

**Post:** `k9z9mt` — [Thick Girl Runner Rant](https://www.reddit.com/r/running/comments/k9z9mt/thick_girl_runner_rant/)
> "Since my body doesn't fit everyone's vision of what a runner should look like, people love to assume I'm
> slow or new to running. […] Do other runners on the thicker side experience this kind of judgement? How do
> you deal with it?"

**Plausible:** `question`, `report`. **Chosen: `question` (borderline).** Not in `labels.csv` (top-up
question from 2020, included under the pre-2025 rule — see manifest).
**Rule applied:** rule 1 and consistency with `1rdg9yc` ("Slower runners, how do you stay motivated when
people mock your pace?"), which asks the same kind of coping question after a similar account and was
labelled `question` in the Milestone 2 audit.
**Why `report` lost:** the situation is ongoing and the writer asks how to handle it; there is no outcome.
It is borderline because the account is long and the ask is partly an invitation.

### Case 7 — thread starters with almost no content

**Posts:** `1wiyhhb` (Tokyo lottery results), `1pjn8y2` (Chicago lottery), `1omigla` (NYC race-day thread),
`1urmvos` (London ballot), `1tw3f1v` (Global Running Day), `1p9okep` (December 5k challenge).
**Plausible:** `question`, or out of scope. **Chosen: `question` (borderline).**
**Rule applied:** rule 1's first clause: strike the ask and nothing of substance remains → `question`.
**Why out-of-scope lost:** they are posts by members with their own words, not AutoModerator threads or
copied articles. They are thin, and the student may prefer to drop them; they are marked borderline so they
are easy to find.

### Case 8 — excluded after reading

Six core posts and five top-up posts were excluded by the scope rule after reading: recurring threads
missed by the title filter (`1pve5us` "Weekly Complaints and Confessions", `1q0dhoq` New Year welcome
megathread, `b449a1` "Friday Spotlight" series), relayed text with under two poster sentences (`1s3n54p`
World Athletics release, `1u3v8bm` Reuters parkrun, `1wrx1i9` BBC Assefa, `1sqpazk` Boston broadcast
schedule), a moderator flair announcement (`6a54bj`), and three bare notices with no claim, account or
question (`52ec22` registration opens, `8cakrb` shoe deal, `1h74b8g` lottery results today). The notice
type is the one kind of post the taxonomy does not cover; it is rare in the current community, which
removes such posts, and it is recorded here rather than forced into a label.

---

## 3. Consistency check against the Milestone 2 audit

39 of the 40 posts provisionally labelled in `label_taxonomy.md` section 6 reappear in the core and were
labelled again during this pass without looking at the audit. All 39 received the same label (including
`1wrx1i9`, excluded both times). The fortieth, `1t4gqbz`, is not in the pool because it fell outside the
200-entry year listing. The comparison was run by script, not by eye.

---

## 4. What needs human judgment, in order of value

1. The PSA-story class (case 4): one decision moves seven rows.
2. The six thread starters (case 7): keep as `question` or drop.
3. The 72 borderline rows generally: each `note` in `labels.csv` names the alternative.
4. Then the 20 cold posts, which must be labelled before reading anything above.
