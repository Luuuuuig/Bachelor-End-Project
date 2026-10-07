# Current status and reading guide

**Updated:** 7 October 2026. This is the current task and reading index. Dated meeting notes establish decisions; reviewed observations establish measured evidence; the notebooks calculate results. Historical plans do not establish that an action happened.

## 1. Where the project stands

The exploratory Arno analysis is substantially complete. The focal-case comparison is calculated but provisional. **Purchase-price control is the current leading candidate, not a final approved choice.** The immediate goal is to finish the evidence and agreement needed to move from Analyze to one bounded Improve task.

Completed or recorded:

- AS-IS workflow, task register, seven-family observation structure, reviewed daily CSVs and row-level Van Weele assignments.
- Five official Arno sessions plus a separate pilot: 892 net observation minutes. After the nine-minute contamination exclusion, recorded activity time is 742 minutes: 182 former EXC minutes remain visible under OTHER outside improvement, and 560 minutes form the improvement profile. Activity minutes are not interchangeable with observed clock time.
- Descriptive workload profiles, stage/task analysis, CHECK per order line, duration descriptions, candidate evidence and draft explanations.
- Provisional scoring and sensitivity analysis using Yijie's weights. These do not constitute a final selection or prove feasibility.
- Johan's permission for test-account data and an external AI service, recorded on 7 October. Availability, representativeness and reference answers still need checking.
- Dennis's qualitative evidence from 15 September and enriched timed observation from 25 September. A separate synthesis and relevant handoff clarification remain useful; an automatic quota of additional days was not agreed.
- Submitted Plan of Work, initial reflections, named second assessor and signed declaration. The [1 October notes](meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md) record that approval was entered in the system.

No prototype, formal workload improvement or quality benefit is established by these records.

## 2. What must be settled to finish Analyze

These tasks can proceed in parallel. Resolve uncertainty that could change the choice, its interpretation or its feasibility; other hypotheses can remain labelled as provisional.

| Task | Evidence needed | Where to work |
|---|---|---|
| Inspect price-control data | Start with PC1–PC4: exportable PO lines, matched confirmations/quotations and a trustworthy reference price. Then check the relevant period, differences from current practice, export route, error cases and testing needs. Inspect fallback data if the proposed case fails or a close comparison depends on it. | [Exact worksheet](analyze/Stage_A_Test_Account_Check_2026-10-07.xlsx) |
| Clarify the task and accepted support | Ask Arno what a check compares, where the trusted price comes from, rough frequency/discrepancy frequency, which explanations he confirms and what the buyer must review or decide. Confirmation corroborates explanations; it does not estimate their causal contribution. | [Arno guide](measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), parts A, B questions 2–3 and D rows 5–6; other prompts when relevant |
| Review decision-relevant labels | Check ambiguous notes and labels underlying competing candidates, especially K04/K17/K18 and the broad-check versus price-explicit boundary. Record source rows, current labels, retained/corrected labels, reasons and effects on the comparison. Do not review only the favoured candidate. | [Codebook](measurement/Kinds_Of_Work_Codebook.md), [labels](measurement/Kinds_Of_Work_Rows_2026-09-30.csv), analysis notebook part 4 |
| Finalize the comparison | Obtain Zhongxin's independent swings before exposing Yijie's weights or ranking. Combine, discuss differences and freeze the weights; review gates, scores and boundaries; rerun totals and sensitivity. Johan validates business relevance and feasibility, including the missing business-value evidence. | [Evidence matrix](analyze/Candidate_Evidence_Matrix_2026-10-07.md), selection notebook |
| Write the Analyze conclusion | State the problem, supported explanations, final choice and boundary, remaining limits and conditions for Improve. Record academic/company alignment. | [Conclusion outline](analyze/Analyze_Conclusion_Outline_2026-10-07.md), especially sections 3–7 |

**Classification review status:** pending. This cleanup does not certify the labels or supply human answers. A targeted accuracy review is not an independent whole-dataset reliability study. Retain that limitation and rerun affected results if labels change. When changing notebook inputs, advance the pinned source commit deliberately; rerunning an old pin alone loads old inputs.

## 3. Optional and conditional work

| Item | Current treatment |
|---|---|
| Exactly 45 blind-coded records and Cohen's kappa | Optional additional consistency exercise. The [prepared workbook](measurement/Kinds_Coding_Check_Sample_2026-10-02.xlsx) is retained. Completing it is not an automatic Analyze exit condition; the active plan is the targeted review above. |
| More duration distributions or a formal goodness-of-fit test | No additional test is needed for the current descriptive use. The curve is not a proven law or an evaluation baseline; later results do not depend on it. |
| More general Arno observation days | No automatic additional round. Collect evidence for consequential remaining gaps. Five sessions are a coverage review point, not proof of representativeness. |
| Two more Dennis days | Conditional on the claims and gaps after he returns. Existing evidence can inform role connections; no required sample size was agreed. |
| Every cause in every fishbone | Confirm explanations used for the selected problem. Other hypotheses remain opportunities, not compulsory interview work. |
| All 31 Exact worksheet checks | A menu across candidates. Prioritize the proposed focal case and relevant common checks; assess fallbacks as needed. |
| Full Exact/Orbis integration, autonomous order preparation, all toolkit ideas | Not promised deliverables. A bounded prototype may use permitted exports and buyer review. Choose architecture after data and acceptance checks. |
| September submission reminders | Completed items are removed from the active list. Dated registers remain as history. |

## 4. What follows selection

1. Define the selected task's requirements and TO-BE workflow, including what AI contributes, what rules handle and what the buyer controls.
2. Establish the manual comparator and freeze the evaluation protocol before development and formal testing: eligible cases, justified workload indicators, quality requirements/reference answers, success thresholds, sampling/analysis and development/evaluation separation. Broad observations do not establish AI savings or a reliable task-time standard.
3. Build and demonstrate one bounded prototype, then compare it with current practice. Include review/correction effort and report effects on Dennis separately where relevant.
4. Write results, limitations and recommendations; prepare ownership, monitoring and manual fallback. Production deployment is not automatically required.
5. Verify and read the sources actually cited. The [literature register](../literature/README.md) distinguishes established use, provisional leads and unread full texts. Draft the thesis alongside the practical work.

Firm dates in the [charter](Project_Charter.md): company placement ends **7 January 2027**; report, scientific-conduct item and end-BEP reflection **15 January 2027 at 23:59**; presentation by **29 January**; assessment by **7 February**. October–December work windows are estimates. The 29 October meeting and first early-November meeting were cancelled in the 1 October notes; the next exact meeting date is not recorded there.

## 5. Reading order for Yijie

Read interpretation paragraphs and tables first. Inspect code when a calculation needs explaining.

| Order | File and section | What you should be able to explain |
|---|---|---|
| 1 | [Assignment](proposal/BEP_Assignment_1BEPIEX.md): definitions and research questions; [methodology](methodology/Phase_1_Current_Methodology.md): sections 2–3 | Arno's outcome, Dennis's role, the four questions, and why handling time is one indicator rather than the definition of workload or quality. |
| 2 | [Purchasing framework](process/Purchasing_Activity_Framework_2026-09-21.md): “Purpose and continuity”; [codebook](measurement/Kinds_Of_Work_Codebook.md): “Coding rules” and “Interpreting time and cases” | How observations led to the task register and seven live families; how stages and detailed kinds are assigned afterward; why overlapping tags cannot simply be added. |
| 3 | [Arno analysis](../Arno_Analysis_2026_10_02.ipynb): Summary, parts 1, 3 and 4 | Data coverage, clock-time/activity-time distinction, CHECK per line, and remaining interpretation checks. Read part 2's conclusion for the limited role of distribution fitting. |
| 4 | Same notebook: parts 8 and 9 | How workload supports candidates; the 98-minute broad-check versus 28-minute price-explicit distinction; observed evidence versus reported causes and hypotheses. |
| 5 | [Selection notebook](../Focal_Case_Selection_2026-10-07.ipynb): Stage A, Stage B, sensitivity and conclusion; [evidence matrix](analyze/Candidate_Evidence_Matrix_2026-10-07.md): price-control section | Why price control currently leads, which assumptions drive that result and what could change the decision. |
| 6 | [Analyze outline](analyze/Analyze_Conclusion_Outline_2026-10-07.md): sections 3–7; [methodology](methodology/Phase_1_Current_Methodology.md): section 6 | Proposed boundary, supported explanations, unresolved gates and how the eventual evaluation answers the research question. |

Your personal review should concentrate on whether interpretations match what you observed, whether the proposed price-checking boundary is accurate and whether you can explain why the evidence supports the choice. A provisional interpretation does not become confirmed by appearing in a table.

## 6. Document authority and this cleanup

Active documents use the exact main question and four sub-questions reaffirmed by Yijie on 7 October. The [submitted PDF of 22 September](proposal/Plan_of_Work_Final_2026-09-22.pdf) retains its five-question structure as the submission record. This update does not claim resubmission or new supervisor approval; flag the working/submitted difference when discussing the current plan with Zhongxin.

The cleanup removes stale active submission tasks, compulsory 45-record/kappa wording and duplicate current-status instructions. The optional workbook, original data, historical mappings/observations and submitted documents remain available. It does not complete pending interviews, test-account checks, classification review, weights or approvals.
