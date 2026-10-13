# Current status and reading guide

**Updated:** 12 October 2026. This is the current task and reading index. Dated meeting notes establish decisions; reviewed observations establish measured evidence; the notebooks calculate results.

## 1. Where the project stands

Define and Measure are done. Analyze is computed but not closed. **Order and confirmation checking is the leading candidate, not an approved choice.** The comparison is provisional until three human inputs arrive, none of which has moved since 7 October:

1. **The Exact test account (PC1 to PC4):** paired POs and confirmations or quotations, and a traceable approved price per line. Without them gates 2 and 3 stay open.
2. **Arno:** what a check compares, where the trusted price comes from, which support he accepts, and who takes part in the evaluation given his leave from the end of October.
3. **Zhongxin:** review of the criteria and anchors, and the weights (her own swings or a review of Yijie's).

**Johan** still has to confirm the business value with examples or figures; Dennis's 15 September explanation (outdated purchase prices led Sales to sell at a loss) is the starting example.

Recorded so far: the AS-IS workflow and task register, five observation sessions (892 observed minutes, 742 recorded, 560 in the improvement scope), the agreed stage of every record, the analysis on the original codes, the provisional selection with Yijie's weights, and Johan's permission of 7 October to use test-account data and an external AI service. No prototype, sufficiency decision, workload improvement or quality benefit is established.

## 2. What changed on 12 October

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
| 3 | Same notebook, part 4 | Codes and stages (4.1, 4.2), Zhongxin's table with Kendall's W (4.3), the leave-one-day-out check (4.4) and the 35 requests (4.5) |
| 4 | Same notebook, parts 5 to 7 | CHECK by stage, day and note, per line and the test on the rates (5.1 to 5.4); case flow (6); episode durations, Kruskal-Wallis and the three fitted curves (7.1, 7.2) |
| 5 | Same notebook, parts 8 and 9; [stage review](measurement/Stage_Review_2026-10-12.md) | The six candidate areas on the raw definitions; the conclusion and what goes to the selection; the record of how every stage was assigned |
| 6 | [Selection notebook](../Focal_Case_Selection_2026-10-07.ipynb): executive summary and sections 1 to 6 | The provisional decision and the *Where to read* table; the gates, the criteria and anchors, Yijie's provisional weights, the scores with their raw evidence, the sensitivity checks and the four conditions |
| 7 | [Supervisor update](analyze/Supervisor_Update_2026-10-15.md); [Analyze outline](analyze/Analyze_Conclusion_Outline_2026-10-07.md) | What goes to Zhongxin on 15 October and how the Analyze chapter will argue |

Before contacting Arno, read the [session guide](measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md) (priority walkthrough) and the [design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md), sections 1 to 3 and 8 to 9.

## 4. Follow-up of the 1 and 8 October meetings

**Decisions and suggestions of 1 October, and how each was closed**

| 1 October | Where | Outcome |
|---|---|---|
| Start with Arno's data; add Dennis later if needed | Analysis notebook | Done with the five Arno sessions; Dennis's notes stay separate |
| Keep former EXC in the total time, outside the AI improvement | Analysis notebook, 2 and 4.1 | Done: labelled "OTHER (outside improvement)", shown in every total, left out of the comparison |
| If the former EXC share is stable, keep it as an unchanged part of the workload | Analysis notebook, 3 | Not stable: 3.9% to 35.7% per day; reported per day, kept outside the comparison |
| Keep work outside the purchasing framework visible as "Not applicable" | Analysis notebook, 4.2 | Done: 25 in-scope minutes in 55 records |
| Organise the time by purchasing stage; a dominant stage could justify concentrating there | Analysis notebook, 4.2 | Ordering: 56.8%, largest on every day |
| Compare CHECK per order line, then reassess 18 September | Analysis notebook, 5.3, 5.4 and 4.4 | 0.90 against 0.83 minutes per line (p = 0.42); without 18 September the CHECK share falls from 16.2% to 8.3% |
| Fallback evaluation on test workloads with handling time from an observed pattern | Analysis notebook, 5.3 | The observed time per line is too imprecise for a baseline; a test needs its own timed checks |
| Compare AI task categories from the literature with what the buyers accept | [AI function comparison](methodology/AI_Function_Comparison_2026-10-02.md) | Table prepared; the buyers' acceptance is still to be asked |
| Draft the thesis alongside the work | [Analyze outline](analyze/Analyze_Conclusion_Outline_2026-10-07.md) | Drafted |

**Requests of 8 October**


| Request or finding | Where | Result |
|---|---|---|
| Activity shares by day (Zhongxin's table) | Analysis notebook, 4.3 | The daily mix varies: PO 19.5 to 41.5%, CLAR 5.7 to 39.5%, CHECK 4.2 to 38.3% of a day's in-scope minutes; given on two labelled denominators |
| Pattern across days (Kendall's W and Jensen-Shannon divergence, 13 October) | Analysis notebook, 4.3 | W = 0.42, p = 0.075: the days agree moderately on the order of the activities; 31 August, 1 and 23 September agree strongly, 8 and 18 September deviate. On the shares themselves the mean Jensen-Shannon divergence is 0.113 against 0.075 by chance (p = 0.089); 8 September is the only day that differs more than chance. Chosen with Zhongxin on 13 October instead of Kruskal-Wallis for this question ([chat record](meetings/Academic_Supervisor_Chat_2026-10-13.md)) |
| Kruskal-Wallis test | Analysis notebook, 7.1 and 5.4 | No clear rank difference in episode lengths between days (H = 2.76, p = 0.60, 182 episodes) or in CHECK minutes per line, 18 September against the other days (H = 0.66, p = 0.42). Neither establishes equal days or a stable mix |
| CHECK per line, corrected | Analysis notebook, 5.3 | 0.90 on 18 September against 0.83 on the other four days (0.87 pooled): about 4.6 seconds per line, not the 1.8 seconds discussed; mean rate per check 1.24 (95% CI 0.70 to 1.78) |
| Workload of each candidate by day | Analysis notebook, 8 | 57 of the 91 CHECK minutes fall on 18 September; without that day checking is 8.3% of the improvement minutes (workload anchor 3 instead of 5) |
| Is more observation needed? | Analysis notebook, 4.3, 4.4 and 8 | Decided on 13 October: two more observation days, 14 and 16 October, reported next to the five-day results ([chat record](meetings/Academic_Supervisor_Chat_2026-10-13.md)). 18 September changes the CHECK share but not the ranking of PO and CLAR; the second Friday shows whether that is a Friday pattern. Targeted checks with Arno remain necessary |
| Criteria: definitions and reasons | [Methodology, section 5.3](methodology/Phase_1_Current_Methodology.md#criterion-definitions-and-rationale); selection notebook, section 3; [supervisor update](analyze/Supervisor_Update_2026-10-15.md) | Definitions, rationale, 1/3/5 anchors and evidence sources; unchanged, now with raw evidence |
| Weights | Selection notebook, section 3; [swing record](analyze/Swing_Weights_Yijie_2026-10-07.md) | Yijie's provisional swings are used and labelled as such; Zhongxin is offered her own swings or a review of Yijie's |
| Dennis's role and a design draft for the focal case | [Design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md) | Conditional drafts, not approved specifications |

## 5. Questions for Zhongxin (15 October)

1. **Sufficiency.** Answered on 13 October: two more observation days, 14 and 16 October. Still open: which targeted checks are needed before Arno's leave?
2. **The tests.** Can Kendall's W be reported as moderate agreement, with the Kruskal-Wallis results as supplementary?
3. **Criteria and weights.** Are the seven criteria distinct enough? Does she set her own swings or review Yijie's?
4. **CHECK per line.** The corrected comparison is 0.90 against 0.83 minutes per line. Does the 8 October conclusion still hold?
5. **Arno.** Is a short written confirmation enough instead of a full session?
6. **Evaluation participant.** Who takes part in the evaluation, given Arno's leave from the end of October?
7. **Stage provenance.** Is layer 3 of the stage record (15 rows assigned by an assistant's context review, 5 in scope) acceptable if reported as such?

## 6. Next steps

| When | What | Where to work |
|---|---|---|
| 13 to 14 October | Exact test-account checks PC1 to PC4 | [Stage A worksheet](analyze/Stage_A_Test_Account_Check_2026-10-07.xlsx) |
| 14 and 16 October | Two more observation days with Arno (protocol v1.3, morning and afternoon block); register, stages and a rerun of both notebooks on seven days | [Measurement protocol](measurement/Measurement_Protocol_v1.3.md); [stage review](measurement/Stage_Review_2026-10-12.md) |
| From 15 October | The 15 October meeting is cancelled; Zhongxin reads the update and the notebooks when she has time, including the criteria and the weights procedure | [Supervisor update](analyze/Supervisor_Update_2026-10-15.md) |
| 19 to 20 October | Arno: written confirmation or short session; settle the evaluation participant | [Session guide](measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), priority walkthrough |
| 22 October | Focal-case alignment: Johan's business value, final weights, rerun of the totals and the Analyze conclusion | Selection notebook; [Analyze outline](analyze/Analyze_Conclusion_Outline_2026-10-07.md) |
| Before 29 October | Evaluation protocol drafted and sent for agreement | [Design draft](process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md), section 8 |

If labels or stages change again, update the CSVs, note the new commit in the loading cells of both notebooks and rerun them (the cells compare the SHA-256 of each CSV with the typed hash).

## 7. What follows selection

1. Define the selected task's requirements and TO-BE workflow: what AI contributes, what rules handle and what the buyer controls.
2. Establish the manual comparator and freeze the evaluation protocol before development and formal testing: eligible cases, workload indicators, quality requirements and reference answers, success thresholds, sampling and the separation of development and evaluation cases. The observed time per line is too imprecise for a baseline.
3. Build and demonstrate one bounded prototype and compare it with current practice, including review and correction effort; report effects on Dennis separately where relevant.
4. Write results, limitations and recommendations; prepare ownership, monitoring and manual fallback.

Firm dates in the [charter](Project_Charter.md): company placement ends **7 January 2027**; report, scientific-conduct item and end-BEP reflection **15 January 2027 at 23:59**; presentation by **29 January**; assessment by **7 February**. The next supervisor meeting date was not fixed in the 8 October notes.
