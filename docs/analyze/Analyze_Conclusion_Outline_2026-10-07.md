# Analyze conclusion: outline

**Drafted:** 7 October 2026. **Status:** outline for the Analyze chapter and the Analyze → Improve tollgate of the [project charter](../Project_Charter.md). It names the provisional focal case, so it is shared with Zhongxin only after she has sent her own swing weights ([scoring brief](https://claude.ai/artifact/P2bsL8ZfyDhdJZanQAdk6n), decision 2).

Each section lists what the chapter will say, where the evidence is, and what is still open. Figures are recorded minutes without former EXC, out of 560, from five partial sessions of one buyer.

## 1. What Analyze has to answer

| Question ([methodology §2](../methodology/Phase_1_Current_Methodology.md#2-research-structure), charter) | Where it is answered | Status |
|---|---|---|
| Where does the recorded work go, and is the evidence enough? | [Analysis notebook](../../Arno_Analysis_2026_10_02.ipynb), parts 1–3 and 5–8 | Done for description; not enough for a time standard |
| What may cause the work? | Notebook part 9; [draft causes](Arno_Causes_Draft_2026-10-06.csv) | Draft; Arno still has to confirm |
| Which work can be eliminated, simplified, standardised, automated or supported? | Notebook part 9 (directions table); section 5 below | Draft per cause |
| How standard is the work? | Notebook parts 6–8 (cases in one stretch, cases without a recorded problem) | Described; not a count of standard cases |
| Are decision-relevant classifications supported by the notes? | Notebook part 4; codebook and source rows | Pending: targeted review across competing candidates; the 45-record exercise is optional, and overall independent reliability is not established |
| Is the AI support feasible with the data available? | [Stage A gates](Stage_A_Gates_2026-10-07.csv), [test-account worksheet](Stage_A_Test_Account_Check_2026-10-07.xlsx) | Gate 1 passed on 7 October; gates 2–3 wait on the test account |
| Which candidate becomes the focal case? | [Selection notebook](../../Focal_Case_Selection_2026-10-07.ipynb) | Provisional; Zhongxin's weights and review follow |

## 2. Where the work goes

- **Ordering is the largest stage** on every day: 334 of 560 minutes (59.6%). Former EXC (182 minutes) stays outside the improvement scope.
- **Three areas carry the most time:** PO preparation and completion (111 minutes), order checks and price differences (98) and request intake & validation (94). They overlap, so they are not added up.
- **No problem was recorded in many case-days:** these contain 406 of the 560 minutes (72.5%). Absence of a recorded problem does not establish that work is routine or automatable. Arno returns to 30 of 98 case-days after other work; these hold 273 minutes.
- **Recorded episodes are short:** a lognormal curve is the working approximation for the bulk of the records (median about 2.3 minutes); no formal goodness-of-fit decision is made.
- **Limits of the evidence:** one buyer, five partial sessions, start and end read in whole minutes, kinds of work assigned by one coder.

## 3. The focal case and its boundary

- **Provisional focal case: purchase-price control.** Boundary (brief, decision 5): checking supplier quotations before ordering and order confirmations after ordering against the PO and supplier information, with price as the main reported problem.
- **Recorded workload:** 98 minutes (17.5%) in 23 records and 19 case-days, on all five days; 66 of them on 18 September. Of the 98, 28 minutes are in records whose note names price, 56 in checks whose subject is not recorded and 14 on other subjects. These describe scopes, not price-checking time.
- **Why this case:** 76.2 of 100 in Stage B, ahead of article / supplier data (56.8), maximalisatie (51.9) and request intake (50.8). It stays first in every single-change sensitivity check (equal weights, each weight ±20%, each score ±1, price-only boundary); six combined one-point changes within the recorded ranges would put article data ahead.
- **Proposed AI role:** source notes describe prices on paper, PDF, websites and email, with item descriptions that may differ from the PO. Reading and matching those inputs could justify AI support (gate 6); inspect the actual documents to establish whether rules or structured inputs suffice. The proposed reference is an approved price per line, whose availability and trustworthiness remain to be demonstrated (gate 3).
- **Proposed support, designed in Improve:** read price, quantity and delivery date per line from the supplier's document, match the lines to the PO and flag differences. The buyer decides; nothing changes in Exact without the buyer.
- **What is not claimed:** no time saving is estimated yet, and the 98 minutes are not all price work.

## 4. Causes of the focal-case work

Status after Yijie's answers of 2 October. "Supported" means consistent with those answers, which are Yijie's account of earlier conversations; Arno confirms or changes each cause in the session ([guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), part A and appendix 2).

| ID | Cause | Evidence | Status | Arno |
|---|---|---|---|---|
| PC-1 | Checks include a manual comparison of order and supplier information | Earlier notes + reported | Supported | |
| PC-5 | Prices in Exact are not kept up to date, because the buyers lack time | Earlier notes + reported | Supported | |
| PC-6 | Exact does not compare a confirmation with the PO | Reported | Supported | |
| PC-10 | Supplier prices change, for example with material costs | Earlier notes | Supported | |
| PC-3 | A change to a PO above €10,000 needs approval again | Observed + reported | Changed | |
| PC-2 | One-off and special items are checked before ordering | Earlier notes | Not yet discussed | |
| PC-4 | Prices come from paper, PDF, websites and email | Observed | Not yet discussed | |
| PC-7 | The cause of a mismatch in a long order is hard to find | Observed | Not yet discussed | |
| PC-8 | Unpaid invoices block the supplier or the check | Observed | Not yet discussed | |
| PC-11 | A price difference was attributed to a smaller order quantity | Observed | Not yet discussed | |
| PC-9 | Finance returns cases without saying what is wrong | Earlier notes | Outside the improvement scope | |

**To write after the session:** which causes Arno confirms, with his words; what an order check normally compares; how many confirmations he checks in a week and how often a price differs (guide, part B, questions 2–3). These answers describe the task and its frequency; they do not move recorded minutes between the groups in section 3.

## 5. Improvement directions for the focal case

| Direction | What it would mean here | Cause | Keep in mind |
|---|---|---|---|
| Support (AI, focal artifact) | Read and match prices from quotations and confirmations; flag differences for the buyer | PC-1, PC-4, PC-6, PC-7 | Simple rules may be enough once the fields are read |
| Automate (ordinary) | Compare the extracted fields with the PO lines by fixed rules | PC-6 | Part of the artifact, but not its AI contribution |
| Support | Suggest price updates in Exact from accepted supplier information | PC-5, PC-10 | The buyer approves every update and stays responsible for the data |
| Standardise | Lines without a difference follow the standard route; flagged lines go to the buyer for review (standard / review / manual frame) | PC-1 | What counts as a difference worth flagging is set with Arno |
| Simplify | Check whether checking before approval avoids re-approval after a change above €10,000 | PC-3 | The approval policy itself stays unchanged |
| Not addressed | Unpaid invoices and Finance aftercare | PC-8, PC-9 | Surrounding dependencies, outside the scope |

No direction lets AI change orders on its own; the buyers raised that concern on 1 October.

**The other candidates** become recommendations: article / supplier data is the first fallback; maximalisatie and request intake stay as further opportunities in their narrowed form; PO supplier communication is a quick win with ordinary automation; standard / review / manual is the frame of the focal case.

## 6. Gates and conditions

| Gate | Verdict for price control | Settled by |
|---|---|---|
| 1. Data and tools permitted | Pass (7 October) | G1–G2: test-account data and an external AI service permitted |
| 2. Representative data | Provisional pass | PC1–PC3, G4, G5 |
| 3. Reference answer | Provisional pass | PC4, PC6 |
| 4. Errors detectable, human in control | Provisional pass | Arno session, part D (rows 5–6); PC8 |
| 5. Fits the BEP | Provisional pass | G6, PC1, PC7 |
| 6. AI adds value beyond a rule | Provisional pass | PC2 |

**Conditions still open:**

1. **Test account (PC1–PC4).** POs with their confirmations or quotations, and a traceable approved price per line. Check the relevant period, export route and testing needs next. If the evidence is missing, gates 2 and 3 remain unresolved; demonstrate a suitable alternative before final selection. The current provisional comparison is not a substitute for these checks.
2. **Arno** accepts that price and date differences are flagged for his review.
3. **Zhongxin** sets her own weights, then reviews the gates, scores and focal case; the totals and sensitivity check are rerun with the combined weights.

**Also needed for the tollgate:** the charter requires agreed weights for final ranking and supervisor alignment. The provisional selection used Yijie's weights only; this remains disclosed when the combined weights are frozen and the totals rerun. Johan's view of the business value (price errors avoided, with examples or figures) is the evidence the business-value score still lacks ([evidence matrix](Candidate_Evidence_Matrix_2026-10-07.md)).

## 7. Into Improve

- **Problem statement and objectives** (DSRM steps 1–2) follow from sections 3–5: what the support must read, match and flag, and what stays with the buyer.
- **Evaluation design** (SQ5), to be frozen before development/formal testing: define eligible matched cases, trusted reference answers, justified workload indicators, final human-approved quality criteria, success thresholds and development/evaluation separation. Handling time is a possible workload indicator, not the workload or quality definition. If chosen, include all attributable human review and correction work. The observed time per line is too imprecise as a task-time standard (0.87 minutes per line pooled; mean per check 1.24, 95% interval 0.70 to 1.78), so establish the selected task's manual baseline separately. Evaluation will show whether the proposed benefit occurs.
- **Fallback:** if price control fails gates 2–3, article / supplier data is assessed next (checks AR1–AR2).

## 8. Limitations to report

- One buyer, five partial sessions, whole-minute records; price-specific time is not measured.
- Causes are reported second-hand until Arno confirms them.
- Kinds of work rest on one coding pass. The targeted classification review is pending; even when completed, it will not establish independent reliability across the whole dataset.
- The workload figures were known before the weights were set; the weights were recorded before any scoring.
- One assessor so far; verdicts and scores were drafted with AI assistance and reviewed by Yijie.
- The test account holds an older period, which may differ from current practice.

## 9. Order of the remaining work

Use [Current status and reading guide, section 2](../Current_Status_and_Reading_Guide.md#2-what-must-be-settled-to-finish-analyze) as the task list. The work can proceed in parallel: inspect focal-case data/reference answers; confirm relevant task explanations and acceptance with Arno; document a targeted classification review across competing candidates; obtain Zhongxin's independent weights and review plus Johan's business-value/feasibility input; rerun affected results and write the conclusion.

Exactly 45 records, a kappa statistic, another general observation round, every cause in all fishbones and all 31 worksheet checks are not automatic exit conditions. Keep remaining hypotheses and evidence gaps explicit. Workflow mapping addresses SQ1; implementation conditions support SQ2; workload profiling and investigation of contributing factors support SQ3; selection supports SQ4; evaluation supports SQ5. These references follow the five sub-questions in the submitted Plan of Work.
