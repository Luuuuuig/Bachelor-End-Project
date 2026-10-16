# Current status and reading guide

**Updated:** 16 October 2026. This is the current task and reading index. Dated meeting notes establish decisions; reviewed observations establish measured evidence; the notebooks calculate results.

## 1. Where the project stands

Define and Measure are done. Analyze is computed but not closed. **Order and confirmation checking is the leading candidate, not an approved choice.** The comparison is provisional until three human inputs arrive; work on the first began on 13 October, and the other two have not moved since 7 October:

1. **The Exact test account (PC1 to PC4):** paired POs and confirmations or quotations, and a traceable approved price per line. Without them gates 2 and 3 stay open. *13 October, provisional:* 10 of 21 sampled October 2025 POs have a supplier confirmation attached; no quotation was seen on the 9 completed POs checked for one; invoices and PO versions give a route to the approved price in some cases ([design draft, section 6](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md#6-draft-logical-field-map)).
2. **Arno:** what a check compares, where the trusted price comes from, which support he accepts, and who takes part in the evaluation given his leave from the end of October.
3. **Zhongxin:** review of the criteria set adopted from the literature on 16 October, its anchors and the scores, and the weights (her own swings or a review of Yijie's carried-over swings).

**Johan** still has to confirm the business impact (criterion A3) with examples or figures; Dennis's 15 September explanation (outdated purchase prices led Sales to sell at a loss) is the starting example.

Recorded so far: the AS-IS workflow and task register, seven observation sessions (1,159 observed minutes, 987 recorded, 693 in the improvement scope; the first five 892, 742 and 560), the agreed stage of every record, the analysis on the original codes, the provisional selection on the criteria set adopted on 16 October with Yijie's carried-over weights, and Johan's permission of 7 October to use test-account data and an external AI service. No prototype, sufficiency decision, workload improvement or quality benefit is established.

## 2. What changed on 12 and 16 October

**16 October**

- **Two more observation days** (14 and 16 October) are recorded, staged and analysed: the [analysis notebook](../Arno_Analysis_2026_10_02.ipynb) now loads all seven daily CSVs directly, the five-day analysis of 13 October is kept as the [five-day notebook](../Arno_Analysis_Five_Days_2026_10_13.ipynb), and the conclusion of the analysis (part 9) sets the two side by side. Ordering stays the largest stage (57.3% of 693 in-scope minutes) and no code's share moves by more than 1.1 points, but the days agree less on the order of the activities (Kendall's W = 0.26, p = 0.12), mainly because of 16 October, a short morning on a day off. Checking is 16.6% of the in-scope minutes, 10.7% without 18 September; article/supplier data rose to 11.3% after three article-creation cases on 14 October.
- **The criteria set was adopted from the literature** ([literature note](analyze/Selection_Criteria_Literature_2026-10-16.md)): ten criteria in two families, value and feasibility, and two new gates (a value floor and a stable task). Yijie's swings of 7 October were carried over; every score was redrafted on seven days, checked against an independent scoring and approved by Yijie. Provisional totals: checking 71.9, article/supplier data 57.0, maximalisatie 51.1, request intake 43.8; checking is first on value and on feasibility ([selection notebook](../Focal_Case_Selection_2026-10-07.ipynb), sections 3 to 5).
- **The CSVs lost the unused column of earlier stages;** the stage review keeps the 100 earlier values of 12 October in its appendix.

**12 October**

- **The analysis was rebuilt on the original observation codes** (PO, CLAR, CHECK, SEND, OTHER, REQ, DEC) and the agreed stage of each record. The kinds-of-work layer of 30 September to 9 October (labels, codebook, framework map, causes draft, candidate matrix, label review) is archived in [docs/archive/kinds_of_work](archive/kinds_of_work/README.md) and no longer used.
- **The stages were agreed.** 100 of the 287 rows changed; the [stage review of 12 October](measurement/Stage_Review_2026-10-12.md) records the rules, nine observer confirmations and 15 rows from a context review. In scope, Ordering is 318 of 560 minutes (56.8%), Specification 121 (21.6%), Monitoring 68 (12.1%).
- **The candidate figures are raw-based:** checking 91 minutes (CHECK code), request intake 121 (Specification stage), PO work 165, maximalisatie 73, article/supplier data 43, PO supplier communication 71.
- **The selection method is unchanged;** no score changed and two uncertainty ranges widened (request intake: workload high 3 to 5, repetition high 2 to 3, because its raw definition is the whole Specification stage while the scored scenario is the narrowed retrieval of old POs and drawings). Provisional totals: checking 76.2, article/supplier data 56.8, maximalisatie 51.9, request intake 50.8; a broad-proxy scenario with request intake scored on the whole stage gives it 57.8.
- **The distribution fits stay** in the analysis (section 7.2 and Appendix A), as Yijie decided.

## 3. Reading order

Read interpretation paragraphs and tables first; inspect code when a calculation needs explaining.

| Order | File and section | What you should be able to explain |
|---|---|---|
| 1 | [Assignment](proposal/BEP_Assignment_1BEPIEX.md); [methodology](methodology/Phase_1_Current_Methodology.md), sections 2 and 3 | Arno's outcome, Dennis's role, the five sub-questions, and why handling time is one indicator rather than the definition of workload |
| 2 | [Analysis notebook](../Arno_Analysis_2026_10_02.ipynb): executive summary (with the *Where to read* table) and "How the analysis is done"; parts 1 to 3 | The main results, the data, the one exclusion, the scope rule and the coverage per day |
| 3 | Same notebook, part 4 | Codes and stages (4.1, 4.2), Zhongxin's table with Kendall's W (4.3), the leave-one-day-out check (4.4) and the 40 requests (4.5) |
| 4 | Same notebook, parts 5 to 7 | CHECK by stage, day and note, per line and the test on the rates (5.1 to 5.4); case flow (6); episode durations, Kruskal-Wallis and the three fitted curves (7.1, 7.2) |
| 5 | Same notebook, parts 8 and 9; [stage review](measurement/Stage_Review_2026-10-12.md); [five-day notebook](../Arno_Analysis_Five_Days_2026_10_13.ipynb) if needed | The six candidate areas on the raw definitions; the conclusion, with the five-day results beside the seven-day ones, and what goes to the selection; the record of how every stage was assigned |
| 6 | [Selection notebook](../Focal_Case_Selection_2026-10-07.ipynb): executive summary and sections 1 to 6 | The provisional decision and the *Where to read* table; the eight gates, the adopted criteria and anchors, Yijie's carried-over weights, the scores with their evidence and the value and feasibility subtotals, the sensitivity checks and the four conditions |
| 7 | [Supervisor update](analyze/Supervisor_Update_2026-10-15.md) | What goes to Zhongxin: the criteria, her day-share table, why checking leads, and the questions |

No separate session with Arno is planned (13 October): what is still needed is asked in passing during the observation days. The [session guide](measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md) and the [design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md), sections 1 to 3 and 8 to 9, hold the questions.

## 4. Follow-up of the 1 and 8 October meetings

**Decisions and suggestions of 1 October, and how each was closed**

| 1 October | Where | Outcome |
|---|---|---|
| Start with Arno's data; add Dennis later if needed | Analysis notebook | Done with the Arno sessions (five, then seven from 16 October); Dennis's notes stay separate |
| Keep former EXC in the total time, outside the AI improvement | Analysis notebook, 2 and 4.1 | Done: labelled "OTHER (outside improvement)", shown in every total, left out of the comparison |
| If the former EXC share is stable, keep it as an unchanged part of the workload | Analysis notebook, 3 | Not stable: 3.9% to 48.8% per day on seven days (to 35.7% on five); reported per day, kept outside the comparison |
| Keep work outside the purchasing framework visible as "Not applicable" | Analysis notebook, 4.2 | Done: 32 in-scope minutes in 63 records (25 in 55 on five days) |
| Organise the time by purchasing stage; a dominant stage could justify concentrating there | Analysis notebook, 4.2 | Ordering: 57.3% on seven days (56.8% on five), largest on every day |
| Compare CHECK per order line, then reassess 18 September | Analysis notebook, 5.3, 5.4 and 4.4 | On seven days 0.90 against 0.62 minutes per line (p = 0.28), on five 0.90 against 0.83 (p = 0.42); without 18 September the CHECK share falls from 16.6% to 10.7% (five days: 16.2% to 8.3%) |
| Fallback evaluation on test workloads with handling time from an observed pattern | Analysis notebook, 5.3; [methodology 6.1](methodology/Phase_1_Current_Methodology.md#61-workload-endpoint-and-quality-guardrail) (measurement rule); [design draft, section 8](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md#8-draft-evaluation-protocol-to-complete-after-selection) (measurement model, 14 October) | The rate per line (0.87 minutes on five days, 0.72 on seven) was recorded on other cases and is too imprecise, so Arno is timed on the test cases in both conditions; the reduction is the difference between his active processing time without and with the aid, not the gap between the aid's run time and his time (the second half of the 1 October idea was underspecified); waiting, difficulty, quality and work moved to others are reported separately |
| Compare AI task categories from the literature with what the buyers accept | [AI function comparison](methodology/AI_Function_Comparison_2026-10-02.md) | Table prepared; the buyers' acceptance is still to be asked |
| Draft the thesis alongside the work | Analysis notebook, 2, 4.3 and 9; selection notebook, executive summary | The Analyze argument and the thesis wording for the day-pattern test are kept in the notebooks; the separate outline was dropped on 13 October |

**Requests of 8 October**


| Request or finding | Where | Result |
|---|---|---|
| Activity shares by day (Zhongxin's table) | Analysis notebook, 4.3 | The daily mix varies: on seven days PO 19.5 to 41.5%, CLAR 0 to 39.5% (5.7 to 39.5% on five), CHECK 4.2 to 38.3% of a day's in-scope minutes; given on two labelled denominators |
| Pattern across days (Kendall's W and Jensen-Shannon divergence, 13 October) | Analysis notebook, 4.3 | On seven days W = 0.26, p = 0.12: the days agree only weakly on the order of the activities, mainly lowered by 16 October; 31 August, 1 and 23 September and 14 October agree strongly, 8 and 18 September and 16 October deviate. On the shares themselves the mean Jensen-Shannon divergence is 0.134 against 0.089 by chance (p = 0.053); 8 September is the only day that differs more than chance. On five days W = 0.42, p = 0.075, and the mean divergence 0.113 against 0.075 (p = 0.089). Chosen with Zhongxin on 13 October instead of Kruskal-Wallis for this question ([13 October notes](meetings/Academic_Supervisor_Meeting_Notes_2026-10-13.md)) |
| Kruskal-Wallis test | Analysis notebook, 7.1 and 5.4 | On seven days no clear rank difference in episode lengths between days (H = 3.33, p = 0.77, 225 episodes) or in CHECK minutes per line, 18 September against the other days (H = 1.17, p = 0.28); on five days p = 0.60 and p = 0.42. Neither establishes equal days or a stable mix |
| CHECK per line, corrected | Analysis notebook, 5.3 | On five days 0.90 on 18 September against 0.83 on the other four (0.87 pooled): about 4.6 seconds per line, not the 1.8 seconds discussed; mean rate per check 1.24 (95% CI 0.70 to 1.78). On seven days 0.90 against 0.62 (0.72 pooled), a gap of 17 seconds that comes from two long, fast checks on 14 and 16 October; mean rate per check 1.15 (95% CI 0.75 to 1.55) |
| Workload of each candidate by day | Analysis notebook, 8 | On seven days 57 of the 115 CHECK minutes fall on 18 September; without that day checking is 10.7% of the improvement minutes, so its workload score under the adopted criteria is 4 instead of 5 (five days: 57 of 91 and 8.3%) |
| Is more observation needed? | Analysis notebook, 3, 4.3, 4.4 and 9 | Decided on 13 October: two more observation days, 14 and 16 October, reported next to the five-day results ([13 October notes](meetings/Academic_Supervisor_Meeting_Notes_2026-10-13.md)). 18 September changes the CHECK share but not the ranking of PO and CLAR. Both days were observed; the analysis now runs on all seven days and its conclusion (part 9) compares them with the five-day results; the second Friday (16 October, a short morning on a day off, with eight e-mails about order confirmations still awaiting processing when the observation ended) does not settle whether 18 September is a Friday pattern. Targeted checks with Arno remain necessary |
| Criteria: definitions and reasons | [Methodology, section 5.3](methodology/Phase_1_Current_Methodology.md#criterion-definitions-and-rationale); selection notebook, section 3; [supervisor update](analyze/Supervisor_Update_2026-10-15.md) | Replaced on 16 October by the criteria set adopted from the literature: definitions, literature support, safeguards and 1/3/5 anchors in the selection notebook, section 3; the 9 October definitions stay in the methodology for the record |
| Criteria in the literature (Zhongxin's request of 14 October) | [Selection criteria from the literature](analyze/Selection_Criteria_Literature_2026-10-16.md) | Her four sources and 21 further criteria sets read; the recurring criteria counted; a proposed set of value criteria (workload volume, error-proneness, business impact, a value floor) and feasibility criteria (B1 to B9), with the project's seven criteria mapped onto it. Adopted by Yijie on 16 October and built into the selection notebook |
| Weights | Selection notebook, section 3; [swing record](analyze/Swing_Weights_Yijie_2026-10-07.md) | Yijie's swings of 7 October carried over to the adopted criteria (a criterion that splits shares its swing equally), confirmed by Yijie on 16 October; Zhongxin is offered her own swings or a review of these |
| Dennis's role and a design draft for the focal case | [Design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md) | Conditional drafts, not approved specifications |

## 5. Questions for Zhongxin (15 October)

1. **Sufficiency.** Answered on 13 October: two more observation days, 14 and 16 October. Still open: which targeted checks are needed before Arno's leave?
2. **The tests.** Can Kendall's W be reported as weak agreement on seven days (W = 0.26, p = 0.12; 0.42 on five), with the Kruskal-Wallis results as supplementary?
3. **Criteria and weights.** Are the ten criteria adopted from the literature on 16 October distinct enough? Does she set her own swings or review Yijie's carried-over ones?
4. **CHECK per line.** The corrected comparison is 0.90 against 0.83 minutes per line on five days and 0.90 against 0.62 on seven, with no clear difference between the rates per check (p = 0.28). Does the 8 October conclusion still hold?
5. **Arno.** Is a short written confirmation enough instead of a full session?
6. **Evaluation participant.** Who takes part in the evaluation, given Arno's leave from the end of October?
7. **Stage provenance.** Is layer 3 of the stage record (15 rows assigned by an assistant's context review, 5 in scope) acceptable if reported as such?

## 6. Next steps

| When | What | Where to work |
|---|---|---|
| 13 October, done | First Exact test-account check: a confirmation attached to 10 of 21 sampled POs, no quotation on the 9 completed POs checked, a price route through invoices and PO versions; repeat on an earlier, complete month when the evaluation set is built | [Design draft, section 6](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md#6-draft-logical-field-map) |
| 14 and 16 October, done | Two more observation days with Arno; registered, staged (stage review, sections 7 and 8) and analysed on seven days (analysis notebook; the five-day version is kept as its own notebook) | [Stage review](measurement/Stage_Review_2026-10-12.md); [analysis notebook](../Arno_Analysis_2026_10_02.ipynb) |
| 16 October, done | Criteria set adopted from the literature; scores redrafted on seven days, checked against an independent scoring and approved by Yijie; weights carried over | [Selection notebook](../Focal_Case_Selection_2026-10-07.ipynb), sections 3 to 5 |
| From 15 October | The 15 October meeting is cancelled; Zhongxin reads the update and the notebooks when she has time, including the criteria and the weights procedure | [Supervisor update](analyze/Supervisor_Update_2026-10-15.md) |
| 14 and 16 October | No separate Arno session: anything still needed (which differences count as critical; whether the documents of the live checks may be used; validation of reference answers) is asked in passing during the observation days. No buyer takes part in the assisted condition (14 October) | [Session guide](measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), part D |
| 22 October | Focal-case alignment: Johan's business impact, final weights, rerun of the totals and the Analyze conclusion | Selection notebook |
| Before 29 October | Evaluation protocol drafted and sent for agreement, planned for the case without a buyer in the assisted condition (quality measured on held-out cases, workload effect estimated) | [Design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md), section 8 |

If labels or stages change again, update the CSVs, note the new commit in the loading cells of both notebooks and rerun them (the selection notebook's loading cell compares the SHA-256 of each CSV with the typed hash; the analysis notebook's names the commit only).

## 7. What follows selection

1. Define the selected task's requirements and TO-BE workflow: what AI contributes, what rules handle and what the buyer controls.
2. Establish the manual comparator and freeze the evaluation protocol before development and formal testing: eligible cases, workload indicators, quality requirements and reference answers, success thresholds, sampling and the separation of development and evaluation cases. The observed time per line is too imprecise for a baseline.
3. Build and demonstrate one bounded prototype and compare Arno's work with and without it on the same or matched cases, including review and correction effort; report effects on Dennis separately where relevant.
4. Write results, limitations and recommendations; prepare ownership, monitoring and manual fallback.

Firm dates in the [charter](Project_Charter.md): company placement ends **7 January 2027**; report, scientific-conduct item and end-BEP reflection **15 January 2027 at 23:59**; presentation by **29 January**; assessment by **7 February**. The next supervisor meeting date was not fixed in the 8 October notes.
