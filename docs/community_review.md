# Community review — r/running (Milestone 1)

**Community:** r/running — <https://www.reddit.com/r/running/>
**Reviewed:** 14 October 2026
**Posts examined:** 40 genuine public posts (table in section 4)
**Sampling:** public Atom feeds of four listings (top of month, new, top of year, hot); every non-automated post from top-of-month, plus posts from the other listings chosen for variety. Details in section 3.

> **Status of the personal-reading requirement.** The research below was carried out by an AI assistant
> (Claude) working from the live public feeds on 14 October 2026. Every post in section 4 is a real r/running
> post with its original URL. The assignment asks the student to read the community personally. That reading
> is **not yet confirmed**: the checklist in section 9 is to be completed by the student after opening the
> posts. Nothing in this file should be read as a claim that the student has already done so.

---

## 1. The community and why it was chosen

r/running is Reddit's general-purpose running community ("All runners welcome"). Its own daily Q&A thread
states the subscriber count as over 4,225,000. It is public, needs no account to read, and its standalone
posts are almost entirely text written by the poster: race reports, training questions, gear questions,
opinion pieces about running culture, and a small number of news shares.

Three candidates were evaluated against the brief's requirements. The evidence is the top-of-month feed for
each (25 posts each, fetched 14 October 2026), plus the newest-25 feed for r/running.

| Requirement | r/running | r/boardgames | r/nba |
|---|---|---|---|
| Public without invitation | Yes | Yes | Yes |
| Text-based discussion | **23 of 25** top-of-month posts have a body of 200+ characters; median body 1,009 characters. 24 of 25 in the newest feed. | 16 of 25 have a body of 200+ characters; median 559. Six are image-only (shelves, tables, tier lists). | **6 of 25** have a body of 200+ characters; median body **0**. Nineteen are video highlights, quote cards or images with no text. |
| 200+ collectable real posts | Yes. One feed call (`top/.rss?t=year&limit=100`) returned 100 non-automated text posts; the month, year and all-time listings plus search give well over 200. | Likely yes, but many would be image posts with little text. | Yes in count, but most would have only a title to classify. |
| Variety of content and quality | High: two-sentence gear questions, 10,000-character race reports with split tables, argued opinion pieces, news relays. | Medium: skewed toward "look what I built / own" posts and promotions. | Low for text: dominated by quotes and clips. |
| Observable distinctions between post types | Clear (section 6). | Possible but weaker: much of the text is product description. | Weak at the post level; the discussion lives in comments. |
| Suits 2–4 labels | Yes (section 6 and Milestone 2). | Possibly. | Not from post bodies. |
| Spoiler risk | None. | Low (rules questions, not plot). | None. |

**Recommendation and choice: r/running.** It is the only one of the three where the unit of classification
(the post body) is reliably the poster's own prose, and where different kinds of post are visibly different
in form. r/nba fails the text requirement outright at the post level. r/boardgames would work but with a
quarter of posts lacking text and a narrower range of post types.

One property of r/running matters for later milestones: it is heavily moderated. About half of the newest-25
feed consists of AutoModerator or recurring threads (daily Achievements, daily Official Q&A, Tuesday
Shoesday, Weekly Training Thread, and so on). Those threads are containers for comments, not posts by a
member, and they are excluded from this review and from the eventual dataset. The standalone posts that
remain are the ones the moderators allowed to stand, which is why they skew toward substantive questions and
full race reports.

---

## 2. Access, rules and rate limits

- Reddit's JSON API (`/r/running/top.json`) answers scripted requests with HTTP 403. The public Atom feeds
  (`/r/running/top/.rss`) do answer, and they carry the full post body, title, author, timestamp and permalink.
  They do not carry score, comment count or flair, so none of those are reported here.
- Reddit rate-limits feed requests aggressively (HTTP 429 when two requests arrive within a few seconds).
  Requests were spaced 12–90 seconds apart and retried on 429. Fewer than 20 feed requests were made in total, several of which were rate-limited and retried.
- Only publicly visible submissions were read. No comments were scraped, no account was used, and no content
  beyond what the feed returns was downloaded. Posts are quoted here only in short excerpts; the full text is
  behind each link.
- Quoted excerpts keep the posters' spelling and punctuation. Reddit usernames are not reproduced in this
  document; the permalink identifies the post.

---

## 3. Sampling method

Four listings were fetched on 14 October 2026:

| Listing | Feed | Entries | Used for |
|---|---|---|---|
| Top of the past month | `top/.rss?t=month` | 25 | All 22 non-automated posts are in the sample |
| Newest | `new/.rss` | 25 (13 automated) | The 4 non-automated posts not already in the month listing |
| Top of the past year | `top/.rss?t=year` | 25 | 14 posts chosen to add types and dates the month listing lacked |
| Hot | `hot/.rss` | 25 | Structure check only (overlaps the two above; no new posts added) |
| Top of the past year, 100 entries | `top/.rss?t=year&limit=100` | 100 | Feasibility check for the 200-post dataset (section 8) |

The sample is therefore not "most popular only" and not "most recent only". It mixes a full month's top
posts (which includes short, low-key questions as well as long reports), the newest standalone posts, and a
year's worth of the posts the community valued most, which is where opinion essays and news relays appear.
Posts range from 2 December 2025 to 13 October 2026. The 14 top-of-year posts were chosen by hand to cover
kinds of post under-represented in the month listing (opinion essays, news relays, long reviews, humour,
emotional posts) rather than by rank.

Excluded by rule, not by judgment: any post authored by AutoModerator and any recurring scheduled thread
(Achievements, Official Q&A, Lurkers' Wednesday, What Are You Wearing Wednesday, Moronic Monday, Run
Nutrition Tuesday, Tuesday Shoesday, Miscellaneous Monday, Li'l Race Report Thread, The Weekly Training
Thread, Weekly Complaints & Confessions, the pinned "New to running or the sub?" post).

---

## 4. The 40 posts

Characteristic codes used in the last column, as observed in the text (not inferred):

| Code | Meaning |
|---|---|
| **ASK** | The post explicitly asks the community for something: a question addressed to readers, or a request for advice, recommendations, opinions or others' experiences. |
| **OWN** | The post narrates the writer's own firsthand experience (what they did, what happened to them). |
| **FACT** | The post states specific, checkable details: times, distances, prices, dates, quantities, named products, races or sources. |
| **CLAIM** | The post asserts something general about running, runners, races or events, beyond the writer's own case. |
| **EMO** | Overtly emotional language ("freaking out", "no words", "rant over", "so proud", emoji). |
| **LINK** | The post relays an external article or result (URL and/or quoted third-party text). |

| # | Reddit id | Posted | Listing(s) seen in | Title | Summary | Observable characteristics |
|---|---|---|---|---|---|---|
| 1 | `1x4e95g` | 2026-10-12 | new, top/month | [Road Racing Etiquette Question](https://www.reddit.com/r/running/comments/1x4e95g/road_racing_etiquette_question/) | New road racer drafted 4-5 yards behind a stranger at the Long Beach Half, was told to 'get off my ass' at mile 4, and asks whether tucking in behind someone is bad etiquette. | ASK, OWN, FACT. A narrated incident that exists to set up one question ('AITA for tucking in behind a stranger?'). |
| 2 | `1whacju` | 2026-09-15 | top/month | [How to keep focused or entertained while running](https://www.reddit.com/r/running/comments/1whacju/how_to_keep_focused_or_entertained_while_running/) | Writer gets bored after about 30 minutes despite podcasts, music and audiobooks, and asks how others stay distracted. | ASK, OWN (light). Short; no numbers beyond '30 minutes'; edited later to thank repliers. |
| 3 | `1wqpypd` | 2026-09-26 | top/month | [Training for LA Marathon 2027 after two brain surgeries and a 154 lb weight loss — sharing in case it helps anyone else who feels "too broken" to start running](https://www.reddit.com/r/running/comments/1wqpypd/training_for_la_marathon_2027_after_two_brain/) | Writer with epilepsy describes a 2017 lobectomy, 2022 deep brain stimulation and a 154 lb weight loss, and is now training for the March 2027 LA Marathon with Team CURE Epilepsy; offers to swap notes with others training around chronic conditions. | OWN, FACT. Primarily a personal story; the closing line is an open invitation, not a request for help. |
| 4 | `1wrx1i9` | 2026-09-27 | top/month | [Injured Assefa narrowly misses world record in Berlin.](https://www.reddit.com/r/running/comments/1wrx1i9/injured_assefa_narrowly_misses_world_record_in/) | Link to a BBC article: an injured Tigst Assefa won Berlin in 2:11:04 after looking set to break the women's world record. | LINK, FACT. The body is two sentences copied from the article; the poster adds no words of their own. |
| 5 | `1whzccf` | 2026-09-16 | top/month | [I successfully reverse-engineered Maurten Gel 100](https://www.reddit.com/r/running/comments/1whzccf/i_successfully_reverseengineered_maurten_gel_100/) | Writer shares a full DIY recipe that reproduces the Maurten Gel 100 hydrogel (sodium alginate + calcium carbonate + GDL), with gram quantities, steps and troubleshooting. | OWN, FACT. Instructional how-to from the writer's own test batches; precise quantities (139 g dextrose, 0.8:1 fructose:glucose); no question. |
| 6 | `1wi00iu` | 2026-09-16 | top/month | [How to carry gels for a 2:30 marathon](https://www.reddit.com/r/running/comments/1wi00iu/how_to_carry_gels_for_a_230_marathon/) | 25-year-old targeting a 2:30 Berlin Marathon (about 3:33/km) asks how fast runners carry 3-4 gels when their shorts have no pockets; considers a Salomon belt or a soft flask. | ASK, OWN, FACT. Detailed context, but the whole post is organised around 'how should I carry them?'. |
| 7 | `1wvs6xq` | 2026-10-02 | top/month | [Impact of low HRV and subpar sleep heading into a race](https://www.reddit.com/r/running/comments/1wvs6xq/impact_of_low_hrv_and_subpar_sleep_heading_into_a/) | Night before a first half marathon, writer's HRV dropped and Garmin sleep score was 67; they are 'freaking out' and ask how much stock to put in it. | ASK, OWN, EMO, FACT. Anxiety is explicit; the ask is about the writer's own race tomorrow. |
| 8 | `1wuzdvc` | 2026-10-01 | top/month | [Race Report - Loch Ness Marathon - PB, BQ, SUB 3](https://www.reddit.com/r/running/comments/1wuzdvc/race_report_loch_ness_marathon_pb_bq_sub_3/) | Structured race report for the 2026 Loch Ness Marathon: 2:58:34, PB/BQ/sub-3, 16-week Runna plan peaking at 105 km, 1:24:27 half during the block, mile-by-mile narrative, 'what's next'. | OWN, FACT. Uses the subreddit's race-report template (Goals / Training / Race / What's next). No question asked. |
| 9 | `1wiyhhb` | 2026-09-17 | top/month | [2027 tokyo marathon lottery results](https://www.reddit.com/r/running/comments/1wiyhhb/2027_tokyo_marathon_lottery_results/) | Two-line thread starter inviting people to share their 2027 Tokyo Marathon lottery results. | ASK. Almost no content of its own; exists to collect replies. |
| 10 | `1x439ym` | 2026-10-12 | new, top/month | [Winter Running](https://www.reddit.com/r/running/comments/1x439ym/winter_running/) | First-year runner finished four 5Ks and ended on a PR, then asks what changes people make to training in winter and for cold-weather tips. | ASK, OWN, EMO ('Super proud!'). Short celebration followed by three direct questions. |
| 11 | `1wi02pw` | 2026-09-16 | top/month | [High quality running singlet without the inflated price of lifestyle branding](https://www.reddit.com/r/running/comments/1wi02pw/high_quality_running_singlet_without_the_inflated/) | Writer complains that good running singlets carry a 'fashion tax' (Satisfy at EUR 140), says an EUR 80 Saysky singlet was 'absolutely dreadful', and asks for European brand recommendations. | ASK, OWN, CLAIM, FACT, EMO. Opinion about branding plus a firsthand product failure, ending in a recommendation request. |
| 12 | `1wrosne` | 2026-09-27 | top/month | [Garmin or Strava prediction: which is more accurate?](https://www.reddit.com/r/running/comments/1wrosne/garmin_or_strava_prediction_which_is_more_accurate/) | Garmin predicts 1:30 and Strava predicts 1:37 for the same half from the same data; writer asks which people trust and why they differ. | ASK, FACT. Short, numeric, two explicit questions. |
| 13 | `1wum0as` | 2026-10-01 | top/month | [First World Major, Huge PB breakthrough - 2026 Berlin Marathon Race Report](https://www.reddit.com/r/running/comments/1wum0as/first_world_major_huge_pb_breakthrough_2026/) | Long structured race report for the 2026 Berlin Marathon (3:10:33) with a 5 km split table, a 2025 injury backstory, the Hansons plan, and reflections on what to change. | OWN, FACT. Template race report. One aside near the end ('if somebody can help me out with this') about a 2027 trip, inside a 10,000-character account. |
| 14 | `1x2odxd` | 2026-10-10 | top/month | [Picking a Marathon](https://www.reddit.com/r/running/comments/1x2odxd/picking_a_marathon/) | After four half marathons the writer lists five candidate first marathons (Flying Pig, Philadelphia, Honolulu, Marine Corps, CIM) and asks for opinions and additions. | ASK, FACT (named races). Minimal personal narrative; the list exists to be voted on. |
| 15 | `1wxukty` | 2026-10-05 | top/month | [my first marathon - an immediate reflection & seeking feedback](https://www.reddit.com/r/running/comments/1wxukty/my_first_marathon_an_immediate_reflection_seeking/) | Physician who just ran a first marathon (Twin Cities) gives a very long account of Higdon Novice 1 training, a hip-flexor setback, race-day pacing and cramping, then asks 'Agree/disagree?' and invites critique; an edit summarises the consensus advice. | OWN, FACT, ASK, EMO ('I'm really beating myself up'). The clearest mixed case in the sample: a complete race report that explicitly solicits feedback. |
| 16 | `1wtk6v6` | 2026-09-29 | top/month | [Norwegian Singles Method. A suboptimal approach](https://www.reddit.com/r/running/comments/1wtk6v6/norwegian_singles_method_a_suboptimal_approach/) | Self-described 'hot take': the Norwegian Singles Method is heading the way of cycling's FTP obsession and will leave many runners below their potential; cites Pogacar changing coaches as the analogy. | CLAIM. No numbers, no personal data, no question. A general assertion argued by analogy. |
| 17 | `1wsgcw8` | 2026-09-28 | top/month | [2026 Melissa's Road Race. A PB, but also, not really a PB](https://www.reddit.com/r/running/comments/1wsgcw8/2026_melissas_road_race_a_pb_but_also_not_really/) | Structured race report for Melissa's Road Race half (1:46:53) in Banff: splits, Coach Greg Garmin plan, rain, a short course, and plans to switch to strength training. | OWN, FACT. Template race report; no question. |
| 18 | `1ww7o57` | 2026-10-02 | top/month | [Running back-to-back week of Marathon? How difficult is it?](https://www.reddit.com/r/running/comments/1ww7o57/running_backtoback_week_of_marathon_how_difficult/) | 34M, 3:10 marathoner with 2,700 km this year, has a local marathon on Feb 21 and drew Osaka on Feb 28; asks how hard two marathons in a week is and whether to drop one. | ASK, OWN, FACT. Context is specific, but the post turns on a decision the writer needs help with. |
| 19 | `1x0drqd` | 2026-10-08 | top/month | [First Half Marathon Training: Balancing Long Run Distance and Recovery During the Taper](https://www.reddit.com/r/running/comments/1x0drqd/first_half_marathon_training_balancing_long_run/) | 23F, run/walk, 12 days from a first half; longest run 8 miles; asks whether to attempt 10 miles or prioritise recovery, and for others' experiences with short peak long runs. | ASK, OWN, FACT. Several explicit questions about the writer's own taper. |
| 20 | `1x3v0k6` | 2026-10-12 | new, top/month | [Should a beginner ditch speed training?](https://www.reddit.com/r/running/comments/1x3v0k6/should_a_beginner_ditch_speed_training/) | 23-year-old beginner with controlled hypertension (sub-40 5K, sub-1:30 10K) dreads interval sessions and asks whether to drop speed work for Zone 2-3, and whether to trust heart rate or perceived exertion. | ASK, OWN, FACT. Literally sectioned into BACKGROUND / QUESTIONS / TLDR. |
| 21 | `1x3kqmk` | 2026-10-11 | new, top/month | [How to introduce gels into training?](https://www.reddit.com/r/running/comments/1x3kqmk/how_to_introduce_gels_into_training/) | Writer with a sensitive stomach, half marathon in April, has only used Honey Stinger chews (about 23 g carbs per 6); asks when and how to introduce gels and how many to take. | ASK, OWN, FACT. Direct advice request. |
| 22 | `1x4wsmj` | 2026-10-13 | new, top/month | [Open Headphone Recommendations?](https://www.reddit.com/r/running/comments/1x4wsmj/open_headphone_recommendations/) | Shokz OpenFit headphones only last about six months; writer has been through three pairs and asks for a more durable open-ear alternative. | ASK, OWN, FACT. Two sentences; a recommendation request. |
| 23 | `1x5bak4` | 2026-10-13 | new | [Is it just me or have races gotten worse?](https://www.reddit.com/r/running/comments/1x5bak4/is_it_just_me_or_have_races_gotten_worse/) | Writer feels races in Utah/Idaho (USD 90-150) now give little beyond a shirt compared with a 'buffet of goodies' at a half 15 years ago, and asks whether others agree and why. | CLAIM, OWN, ASK. Opinion framed as a question ('Is it just me...?'); evidence is one remembered race. |
| 24 | `1x57wvv` | 2026-10-13 | new | [Dealing with nausea/reflux on every run](https://www.reddit.com/r/running/comments/1x57wvv/dealing_with_nauseareflux_on_every_run/) | Returning runner gets nausea on every hard effort, runs fasted because of acid reflux, and asks whether there is a solution or whether 'running is just not my sport'. | ASK, OWN, EMO. A personal problem seeking a fix. |
| 25 | `1x57rpo` | 2026-10-13 | new | [Is splitting lower-body strength training across multiple days as effective for runners as doing dedicated leg workouts?](https://www.reddit.com/r/running/comments/1x57rpo/is_splitting_lowerbody_strength_training_across/) | Two months into a Runna return-to-running plan, writer asks whether splitting lower-body strength work across days is as effective for runners as dedicated leg days, and lists Workout A / Workout B. | ASK, OWN. A general training question with the writer's own plan as the example. |
| 26 | `1x53jc9` | 2026-10-13 | new | [Race Report: 2026 Chicago Marathon](https://www.reddit.com/r/running/comments/1x53jc9/race_report_2026_chicago_marathon/) | Race report for the 2026 Chicago Marathon: 3:55:03 for a first sub-4 after 4:18 and 4:14:35, with a list of what changed in training (strength, speed, gels every 4 miles, carb load) and a detailed race recap; ends thanking Chicago. | OWN, FACT, EMO (joy and gratitude). Template-style report; no question. |
| 27 | `1rfd5ai` | 2026-02-26 | top/year | [Jeff Galloway, who inspired people with his run-walk method, dies at 80](https://www.reddit.com/r/running/comments/1rfd5ai/jeff_galloway_who_inspired_people_with_his/) | Reports Jeff Galloway's death at 80 with quoted key details from the AP article, then adds two sentences on how the run-walk method helped the poster return from breaks. | LINK, FACT, OWN (two sentences), CLAIM ('his efforts have arguably helped more people get into the sport'). Mostly relayed text. |
| 28 | `1qo0vmv` | 2026-01-27 | top/year | [The mental gymnastics of convincing yourself to run vs actually running](https://www.reddit.com/r/running/comments/1qo0vmv/the_mental_gymnastics_of_convincing_yourself_to/) | Writer spent 45 minutes talking themselves into a 35-minute run and observes that the excuses, not the run, are the hard part; asks for everyone's favourite bogus excuse. | OWN, CLAIM, ASK. Humorous generalisation from one morning; closing question invites stories rather than advice. |
| 29 | `1w4c85u` | 2026-09-01 | top/year | [Started running at 39. For those who also started later — what happened to your fitness in years 2–4?](https://www.reddit.com/r/running/comments/1w4c85u/started_running_at_39_for_those_who_also_started/) | Started running at 39, now 41-42 miles per week before a first NYC Marathon (1:45 half, 17-miler with 8:19 finish); aerobic fitness is outpacing durability; asks late starters what changed in years 2-4. | ASK, OWN, FACT. Several explicit questions addressed to a specific group. |
| 30 | `1vnjz41` | 2026-08-13 | top/year | [What's everyone's take on the run club phenomenon?](https://www.reddit.com/r/running/comments/1vnjz41/whats_everyones_take_on_the_run_club_phenomenon/) | Runner since 2015 reflects on the 'modern run club' phenomenon: good for the sport (Philly selling out), but now a lifestyle brand and content machine; not gatekeeping; asks whether culture really changed or 'am I just getting old?'. | CLAIM, OWN, ASK (closing). An essay-length opinion with a discussion prompt at the end. |
| 31 | `1rdhyqq` | 2026-02-24 | top/year | [At what point does running become self destructive behavior?](https://www.reddit.com/r/running/comments/1rdhyqq/at_what_point_does_running_become_self/) | Four-years-sober writer running 30-40 miles a week watches an ultrarunner partner run 80-100 miles a week with a 'trashed' body, and asks when running becomes self-destructive addiction. | ASK, OWN, EMO. The comparison to substance abuse is the writer's concern; the post asks for 'all thoughts'. |
| 32 | `1t4nd59` | 2026-05-05 | top/year | [Stopped chasing PBs after my last marathon and discovered what running was actually doing for me](https://www.reddit.com/r/running/comments/1t4nd59/stopped_chasing_pbs_after_my_last_marathon_and/) | After four weeks off post-marathon, writer realised running was where they processed life problems, cites research that the prefrontal cortex quiets during aerobic exercise, and now logs feelings instead of pace; asks whether others had a similar shift. | OWN, CLAIM (research claim without a source), ASK (closing invitation). |
| 33 | `1rdg9yc` | 2026-02-24 | top/year | [Slower runners, how do you stay motivated when/if people mock your pace?](https://www.reddit.com/r/running/comments/1rdg9yc/slower_runners_how_do_you_stay_motivated_whenif/) | Slower runner (0 to half in 6-7 months, now training for a marathon) is mocked by friends, family and social media for their pace; asks how other slow runners cope. | ASK, OWN, EMO. Long edit adds examples; feelings (dread, pride) are explicit. |
| 34 | `1roa4ql` | 2026-03-08 | top/year | [LA Marathon men’s finish was wild-and coverage was terrible!](https://www.reddit.com/r/running/comments/1roa4ql/la_marathon_mens_finish_was_wildand_coverage_was/) | Nathan Martin won the LA Marathon in 2:11:18 in a sprint finish, but the writer says the TV coverage was 'absolutely terrible' and never showed the gap to Kimani Kamau. | CLAIM, FACT, EMO, LINK. A criticism of the broadcast with the result as context; no question. |
| 35 | `1u77xay` | 2026-06-16 | top/year | [Not gate keeping track but run clubs please use track etiquette](https://www.reddit.com/r/running/comments/1u77xay/not_gate_keeping_track_but_run_clubs_please_use/) | UK track athlete asks social run clubs to follow track etiquette: 30+ people warming up across lanes, headphones, joggers crossing a discus area mid-throw; links an etiquette guide; 'rant over'. | CLAIM, OWN, LINK, EMO. An argument addressed to a group, supported by one incident 'last week'. |
| 36 | `1tfyl2u` | 2026-05-17 | top/year | [In-depth review of Runna after using it for a year](https://www.reddit.com/r/running/comments/1tfyl2u/indepth_review_of_runna_after_using_it_for_a_year/) | 23,000-character review of the Runna app after two 12-week plans (a 10K and the Brooklyn Half): what it does, what it does not, who it suits, and why the writer is not renewing. | OWN, FACT, CLAIM (verdict about who benefits). Long-form review with a stated bottom line; no question. |
| 37 | `1sw5yl0` | 2026-04-26 | top/year | [History in the Marathon.](https://www.reddit.com/r/running/comments/1sw5yl0/history_in_the_marathon/) | Writer relays the 2026 London Marathon results in their own words: Sabastian Sawe 1:59:30 as the first official sub-2, Kejelcha 1:59:41 on debut, Kiplimo 2:00:28; 'this just became the greatest marathon in history'. | FACT, CLAIM, EMO ('Just no words'). Results listed with a superlative judgment; no link, no question. |
| 38 | `1t4gqbz` | 2026-05-05 | top/year | [Record 1.3m apply for 2027 London marathon ballot](https://www.reddit.com/r/running/comments/1t4gqbz/record_13m_apply_for_2027_london_marathon_ballot/) | One line plus a BBC link: a record 1.3 million applied for the 2027 London Marathon ballot; 'the odds are against us'. | LINK, FACT, EMO (emoji). Almost no original text. |
| 39 | `1q4i8fz` | 2026-01-05 | top/year | [Why do marathon courses have to follow this rule?](https://www.reddit.com/r/running/comments/1q4i8fz/why_do_marathon_courses_have_to_follow_this_rule/) | Explains two official course rules (net drop under 0.1%, start and finish within half the race distance), understands the first, and asks course designers why the second exists; argues a marathon 'should be' point-to-point. | ASK, FACT, CLAIM. A factual question wrapped around a stated opinion. |
| 40 | `1pcbzmz` | 2025-12-02 | top/year | [Streakers. Lend me your tales.](https://www.reddit.com/r/running/comments/1pcbzmz/streakers_lend_me_your_tales/) | Writer on day 2,163 of a 5 km-a-day streak tells the story: why it continued past 366 days, running through a spouse's stage 4 cancer, raising about GBP 24,000, injuries, pace and 'the number'; invites other streakers' tales. | OWN, FACT, EMO, ASK (title). A long personal narrative with an open invitation. |


Tally across the 40 posts: ASK 26, OWN 31, FACT 27, CLAIM 12, EMO 13, LINK 5. The codes overlap by design;
a single post commonly carries three of them. What separates post types is which code the post is *built
around*, which is what section 6 is about.

---

## 5. What the sample shows

1. **Most standalone posts are addressed to the community as a request.** 26 of 40 contain an explicit
   question or request. This is partly a moderation effect: simple questions are steered into the daily Q&A
   thread, so the questions that survive as posts tend to come with detailed context (age, weekly mileage,
   race date, what has been tried). Example: post 20 is literally sectioned into BACKGROUND / QUESTIONS / TLDR.
2. **Firsthand reports have a recognisable shape.** Race reports (posts 8, 13, 17, 26) follow the
   subreddit's template: a header with race, date and time, a goals table, splits, then Training / Race /
   What's next. Other reports (5, 36, 40) are long-form and detail-dense. None of these four race reports is
   organised around a question (post 13 has a one-line aside asking for trip advice); the report that does ask
   for feedback (post 15) says so in its title.
3. **Numbers are everywhere, so numbers alone do not distinguish posts.** 27 of 40 contain specific
   checkable facts, including two-sentence gear questions ("three pairs", "about 6 months"). A taxonomy built
   on "has a checkable fact" would put most of r/running in one bucket. Where facts *carry an argument*
   (post 16 has none; post 37 lists five times to justify "greatest marathon in history") is a much smaller
   set.
4. **General opinion pieces exist but are a minority.** 12 posts make a general claim; in about half of
   those the claim is the point of the post (16, 23, 30, 34, 35, 37), and in the other half it is a side
   remark inside a question or a report.
5. **Pure news relays are rare and mostly not the poster's words.** 5 of 40 link out; three of them (4, 38,
   and most of 27) have fewer than two sentences written by the poster.
6. **Emotion is present but graded.** 13 posts carry overt emotional language, from one emoji (38) to
   "freaking out" (7) and "I'm really beating myself up" (15). It is a dimension, not a category: the Chicago
   report (26) is joyful and still a structured report.

---

## 6. Candidate distinctions (four)

Each was checked against the texts above. "Consistency" is an estimate of whether two independent readers
applying the stated rule would agree, with the posts where they would most likely disagree named.

### Distinction A — Asking the community vs. telling it

**What it measures.** Whether the post exists to obtain something from readers (an answer, a recommendation,
others' experiences) or is complete as a contribution in itself.

**Why it matters here.** It is the dominant split in r/running's standalone posts (26 asking vs. 14
telling in this sample). A reader, moderator or recommender treats the two completely differently: one needs
replies, the other needs an audience.

**Posts that demonstrate it.** Asking: 1, 6, 7, 12, 18, 19, 20, 21, 22, 24, 25, 29, 31, 33. Telling: 5, 8,
13, 16, 17, 26, 34, 36, 37.

**Consistency.** High at the extremes: a question mark aimed at readers, or "any recommendations?", is
textual. The disagreements will come from posts that are both: a complete report that ends with "critiques
welcome" (15), an essay that ends with "am I just getting old?" (30), an opinion phrased as "is it just me?"
(23), and stories that end with "lend me your tales" (40) or "anyone else?" (32). A rule for those is
needed; a candidate is in section 7.

### Distinction B — Firsthand account vs. general claim

**What it measures.** Whether the substance of the post is what happened to the writer (their race, their
training block, their product, their streak) or an assertion about running, runners or events in general.

**Why it matters here.** The community treats these differently: a report is read for what it describes; a
general claim is read to be agreed or argued with. The subreddit has a template for one (race reports) and a
colloquial name for the other ("hot take", which post 16 uses of itself).

**Posts that demonstrate it.** Firsthand: 3, 5, 8, 13, 17, 26, 36, 40. General claim: 16, 23, 30, 35, 37.

**Consistency.** Moderately high. Disagreement is likely when the writer's own experience is offered as the
evidence for a general claim: 28 (one morning's procrastination → "the run is never the hard part"), 32
(own change of attitude → research claim about the prefrontal cortex), 30 (own history → verdict on run
clubs). A rule is needed for "experience as evidence": does the generalisation or the narrative get the
label?

### Distinction C — Specific, checkable facts that carry the point vs. assertion without support

**What it measures.** Whether the post's point rests on named, checkable specifics (times, distances,
prices, rules, named sources) or is asserted without them.

**Why it matters here.** It is the staff taxonomy's main axis and it clearly exists in r/running: compare
post 16 (no numbers, argument by analogy) with 37 (five finishing times) or 39 (two quoted course rules with
their numbers).

**Posts that demonstrate it.** Fact-carried: 5, 8, 13, 36, 37, 39. Assertion: 16, 23, 28, 2.

**Consistency.** Lower than A and B in this community, for the reason in section 5.3: almost every post
contains some number, so the reader must judge whether the number is *load-bearing*. Posts 23 (one price
range and one memory), 35 (one incident) and 27 (AP facts, poster's own claim unsupported) would split
readers. Useful as a secondary signal, risky as a primary label.

### Distinction D — Emotional register vs. measured register

**What it measures.** Whether the post foregrounds the writer's feelings (anxiety, pride, anger, awe) or is
written in a neutral, explanatory voice.

**Why it matters here.** Several of the most-upvoted posts of the year are emotional (31, 33, 37), and
moderators and readers respond to them differently from a Runna review.

**Posts that demonstrate it.** Emotional: 7, 31, 33, 34, 37, 38. Measured: 5, 36, 39, 12.

**Consistency.** Low to moderate. Tone is a gradient; posts 26, 15 and 10 mix elation or self-criticism
with structured content, and two readers would often disagree on the cut-off. Recommended as a note, not a
label.

**Also observed, recorded for scope rather than as a label: original text vs. relayed text.** Posts 4, 38
and 27 consist mostly of someone else's words (BBC, AP). The distinction is perfectly consistent (is there a
URL and quoted text, and how many sentences did the poster write?) but it is a question of what to classify,
not how. See section 7.

---

## 7. Implications carried forward to Milestone 2

- Distinctions **A** and **B** are the most consistent and together cover the sample. They point toward
  labels of the form *asks* / *reports own experience* / *asserts a general claim*. Milestone 2 tests that.
- Distinction **C** is real but, in r/running, is better used inside the definition of a "claim" post than as
  a label of its own.
- Distinction **D** is recorded as a secondary characteristic only.
- The hardest boundary in the sample is **A applied to posts that both narrate and ask** (15, 23, 28, 30,
  32, 40). A candidate rule, to be tested in Milestone 2: *delete every sentence that asks the reader
  something; if what remains is a complete report or a complete argument, label by what remains; if what
  remains is only context for the ask, the post is a question.*
- Eligibility rules proposed for the dataset: exclude AutoModerator and recurring threads (section 3), and
  exclude posts whose body is a URL and/or quoted third-party text with fewer than two sentences written by
  the poster (posts 4 and 38 here). Those posts would otherwise have the classifier labelling the BBC's
  prose rather than a community member's.

---

## 8. Can 200 posts be collected?

Yes, on the evidence gathered:

- `top/.rss?t=year&limit=100` returned 100 entries, all non-automated, 92 of them with a body of 150+
  characters.
- The month listing alone contributed 22 eligible posts; the year listing, the all-time listing and Reddit's
  in-subreddit search (which also serves an Atom feed) are independent pools.
- Feed pagination works (`after=t3_<last id>&count=100`): a second page of the year listing returned 100
  further entries with no overlap, and the all-time listing another 100. Three feed calls therefore yielded
  **300 unique posts** before any search was used. More than enough for 200 after exclusions.
- Collection must be spaced out: one request every 60–90 seconds is reliable; two within a few seconds is
  not.

---

## 9. Student confirmation (to be completed by the student)

The assignment requires the student to have read the community. Tick each line only once it is true.

- [ ] I opened r/running and read for at least 20 minutes, including posts not in this table.
- [ ] I opened the 40 linked posts (or a stated subset: ______ ) and agree that the summaries describe them.
- [ ] I agree with the characteristic codes, except for these post numbers, where I noted a correction: ______
- [ ] I agree that distinctions A and B are the most consistently observable; my own view on C and D: ______
- [ ] I agree with the eligibility rules in section 7, or I want to change them as follows: ______

---

*Prepared with AI assistance (Claude) on 14 October 2026. All posts are real; the summaries and codes are the
assistant's reading of the public text and are subject to the student's confirmation above.*
