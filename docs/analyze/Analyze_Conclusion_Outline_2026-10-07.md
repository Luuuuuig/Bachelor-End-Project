# Analyze conclusion: outline

**Drafted:** 7 October 2026; updated 9 October; rewritten 12 October on the original observation codes. **Status:** outline for the Analyze chapter and the Analyze to Improve tollgate of the [project charter](../Project_Charter.md). It names the provisional focal case; share it with Zhongxin together with the choice of weights offered in the [supervisor update](Supervisor_Update_2026-10-15.md). The 8 October meeting agreed a review of the criteria and weights, not a final weighting procedure.

Each section lists what the chapter will say, where the evidence is, and what is still open. Figures are recorded minutes without former EXC, out of 560, from five partial sessions of one buyer. Section numbers refer to the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) unless stated.

## 1. What Analyze has to answer

| Question ([methodology, section 2](../methodology/Phase_1_Current_Methodology.md#2-research-structure), charter) | Where it is answered | Status |
|---|---|---|
| Where does the recorded work go, and is the evidence enough? | Parts 3 and 4 (coverage, codes, stages, Zhongxin's table in 4.3, leave-one-day-out in 4.4) | Computed; the sufficiency decision is Zhongxin's |
| What explains the work? | Yijie's dated account of 2 October in the [session guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october); the notes behind CHECK (5.2) | Reported, not confirmed; Arno still has to confirm |
| How standard is the work? | Part 6 (case flow: stretches per case-day, returns) and 7.1 (episode durations by day) | Described; not a count of standard cases |
| Are the stages of the records supported? | [Stage review of 12 October](../measurement/Stage_Review_2026-10-12.md); analysis notebook 4.2 | Agreed on 12 October; 15 rows rest on a context review (5 in scope) |
| Is the AI support feasible with the data available? | [Selection notebook](../../Focal_Case_Selection_2026-10-07.ipynb), section 2 (gates); [test-account worksheet](Stage_A_Test_Account_Check_2026-10-07.xlsx) | Gate 1 passed on 7 October; gates 2 and 3 wait on the test account |
| Which candidate becomes the focal case? | Selection notebook, sections 4 to 6 | Provisional; Zhongxin's weights and review follow |

## 2. Where the work goes

- **Ordering is the largest stage** on every day: 318 of 560 minutes (56.8%), then Specification 121 (21.6%) and Monitoring 68 (12.1%). Its share per day runs from 42.3% (18 September) to 68.1% (23 September) (4.2). Former EXC (182 minutes) stays outside the improvement scope; its share per day is not stable (3.9% to 35.7%).
- **Per code:** PO 165 minutes, CLAR 155, CHECK 91, OTHER 77, SEND 71; REQ and DEC only as untimed tallies (4.1).
- **The daily mix varies:** within a day's improvement minutes PO ranges from 19.5% to 41.5%, CLAR from 5.7% to 39.5% and CHECK from 4.2% to 38.3%. Without 18 September the CHECK share falls from 16.2% to 8.3%; PO and CLAR stay the two largest codes with any day left out (4.3, 4.4).
- **Requests are counted, not timed:** 35 were recorded, all as untimed tallies, mostly by e-mail (21) and phone (9); 2.35 per observed hour. 21 of the 35 request case-days also contain clarification work; this is co-occurrence, not cause (4.5, 6).
- **Arno returns to 30 of 98 case-days** after other work; these hold 273 minutes (6).
- **Recorded episodes are short:** median 2 minutes, mean 3.08; no clear rank difference between days (Kruskal-Wallis H = 2.76, p = 0.60). A lognormal curve is the closest working description on average error and frequency pattern, the exponential on the tail; no formal goodness-of-fit decision is made (7.1, 7.2, Appendix A).
- **Limits of the evidence:** one buyer, five partial sessions, start and end read in whole minutes, short notes.

## 3. The focal case and its boundary

- **Provisional focal case: order and confirmation checking**, called purchase-price control until 7 October. Boundary: checking supplier quotations before ordering and order confirmations after ordering against the PO, for price, delivery date, quantity and missing or extra lines.
- **Recorded workload, raw definition:** the CHECK code, 21 records and 91 minutes (16.2%) in 19 case-days on all five days; 57 of the 91 minutes on 18 September; 37 minutes in Ordering (checks before ordering) and 54 in Monitoring (checks of confirmations) (5.1). Seven records (33 minutes) name a price or a delivery date in their note, one record (20 minutes) records a mismatch without naming the field, and the other 13 records (38 minutes) have a blank or generic note (5.2). The observer's clarification of 7 October that those checks concerned price and delivery date is reported as the observer's knowledge, not as recorded data.
- **Per order line:** 0.87 minutes pooled on 14 usable case-days; 0.90 on 18 September against 0.83 on the other days; mean rate per check 1.24 (95% CI 0.70 to 1.78); regression slope 0.62 minutes per line, 0.25 without the 29-line check; Kruskal-Wallis on the rates H = 0.66, p = 0.42 (5.3, 5.4).
- **Why this case:** 76.2 of 100 in Stage B with Yijie's provisional weights, ahead of article/supplier data (56.8), maximalisatie (51.9) and request intake and validation (50.8; 57.8 if the whole Specification stage counted for it). It stays first in every single-change sensitivity check (equal weights, each weight plus or minus 20%, each score plus or minus 1, its workload score set to 3, request intake scored on the whole stage); six combined one-point changes within the recorded ranges would put article/supplier data ahead (selection notebook, section 5).
- **Proposed AI role:** quotations and confirmations arrive on paper, as PDF, by e-mail and from websites, with item descriptions that may differ from the PO. Reading and matching those inputs could justify AI support (gate 6); inspect the actual documents to establish whether rules or structured inputs suffice. The proposed reference is an approved price per line, whose availability and trustworthiness remain to be demonstrated (gate 3).
- **Proposed support, designed in Improve:** read price, quantity and delivery date per line from the supplier's document, match the lines to the PO and flag differences and missing or extra lines. The buyer decides; nothing changes in Exact without the buyer.
- **What is not claimed:** no time saving is estimated; the 91 minutes are not divided between price, date and quantity; the price mismatch of 18 September row 3 (a CLAR row) is not counted as checking; the 33 price- or date-named minutes are not a validated minimum of the time the artifact would address.

## 4. Reported explanations of the focal-case work

Yijie's answers of 2 October, from earlier conversations with Arno and Dennis, are recorded in the [session guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october). They are reported explanations, to be confirmed or changed by Arno (guide, Appendix 1). The ones that bear on checking: lines are compared by hand; prices in Exact are not kept up to date because the buyers lack time; Exact cannot compare a confirmation with the PO; supplier prices change; prices come from paper, PDF, websites and e-mail; a change to a PO above 10,000 euros needs approval again. The causes draft of 6 October, which placed these in fishbone categories on the kinds of work, is archived.

**To write after the session:** which explanations Arno confirms, in his words; what an order check normally compares; how many confirmations he checks in a week and how often a price differs (guide, part B, questions 2 and 3). These answers describe the task and its frequency; they do not move recorded minutes.

## 5. Improvement directions for the focal case

| Direction | What it would mean here | Keep in mind |
|---|---|---|
| Support (AI, focal artifact) | Read and match prices, quantities and delivery dates from quotations and confirmations; flag differences and missing or extra lines for the buyer | Simple rules may be enough once the fields are read |
| Automate (ordinary) | Compare the extracted fields with the PO lines by fixed rules | Part of the artifact, but not its AI contribution |
| Support | Suggest price updates in Exact from accepted supplier information | The buyer approves every update and stays responsible for the data |
| Standardise | Lines without a difference follow the standard route; flagged lines go to the buyer for review (standard / review / manual frame) | What counts as a difference worth flagging is set with Arno |
| Simplify | Check whether checking before approval avoids re-approval after a change above 10,000 euros | The approval policy itself stays unchanged |
| Not addressed | Unpaid invoices and Finance aftercare | Surrounding dependencies, outside the scope |

No direction lets AI change orders on its own; the buyers raised that concern on 1 October and opposed automatic PO creation and sending (reported 8 October).

**The other candidates** become recommendations: request intake and validation (121 minutes, the Specification stage) and article/supplier data (43 minutes) are the two runners-up and conditional fallbacks; maximalisatie (73 minutes, mostly contextual evidence) stays a further opportunity in its narrowed form; PO supplier communication (71 minutes) is a quick win with ordinary automation; standard / review / manual (PO, 165 minutes) is the frame of the focal case.

## 6. Gates and conditions

| Gate | Verdict for order and confirmation checking | Settled by |
|---|---|---|
| 1. Data and tools permitted | Pass (7 October) | G1 and G2: test-account data and an external AI service permitted |
| 2. Representative data | Provisional pass | PC1 to PC3, G4, G5 |
| 3. Reference answer | Provisional pass | PC4, PC6 |
| 4. Errors detectable, human in control | Provisional pass | Arno session, walkthrough row 4; PC8 |
| 5. Fits the BEP | Provisional pass | G6, PC1, PC7 |
| 6. AI adds value beyond a rule | Provisional pass | PC2 |

**Conditions still open** (selection notebook, section 6):

1. **Test account (PC1 to PC4).** POs with their confirmations or quotations, and a traceable approved price per line. If the evidence is missing, gates 2 and 3 remain unresolved; demonstrate a suitable alternative before final selection.
2. **Arno** accepts that price and date differences are flagged for his review; the evaluation participant is settled before his leave at the end of October.
3. **Zhongxin** reviews the criteria, the boundary, gates, scores and weights; she sets her own swings or reviews Yijie's; the agreed set is recorded with the date and the totals rerun.
4. **Johan** confirms the business value of the focal case with examples or figures. Dennis's 15 September explanation, that outdated purchase prices led Sales to sell items at a loss, is the starting example. Permission to use the test account does not establish business value.

**Also needed for the tollgate:** the charter requires agreed weights for final ranking and supervisor alignment. The provisional selection used Yijie's weights only; this stays disclosed.

## 7. Into Improve

- **Problem statement and objectives** (DSRM steps 1 and 2) follow from sections 3 to 5: what the support must read, match and flag, and what stays with the buyer.
- **Evaluation design** (SQ5), to be frozen before development and formal testing: eligible matched cases, trusted reference answers, justified workload indicators, human-approved quality criteria, success thresholds and the separation of development and evaluation cases. Handling time is a possible workload indicator, not the workload or quality definition. The observed time per line is too imprecise as a task-time standard (0.87 minutes per line pooled; mean per check 1.24, 95% CI 0.70 to 1.78), so establish the selected task's manual baseline separately.
- **Fallbacks:** if order and confirmation checking fails gates 2 and 3, confirmation-against-PO checking alone (the Monitoring part) is assessed first, then article/supplier data (checks AR1 and AR2).

## 8. Limitations to report

- One buyer, five partial sessions, whole-minute records; the time per checked field is not measured.
- 57 of the 91 CHECK minutes fall on one day; a price or delivery date is recorded in the note for 33 of the 91 minutes, an unspecified mismatch for 20.
- Explanations are reported second-hand until Arno confirms them.
- The stages were agreed on 12 October from observer rules, nine observer confirmations and a context review of 15 rows (5 in scope); the review rows are reported as such.
- The workload figures were known before the weights were set; the weights were recorded before any scoring. One assessor so far; scores were drafted with AI assistance and reviewed by Yijie.
- The test account holds an older period, which may differ from current practice.

## 9. Order of the remaining work

Use the [current status and reading guide, section 6](../Current_Status_and_Reading_Guide.md#6-next-steps) as the task list: test-account checks (13 to 14 October), the criteria and weights with Zhongxin (15 October), Arno (19 to 20 October), focal-case alignment with Johan's business value and the final weights (22 October), the evaluation protocol before 29 October. Then rerun the affected results and write the conclusion.

Another general observation round, a recoding exercise with kappa and all 31 worksheet checks are not exit conditions. Workflow mapping addresses SQ1; implementation conditions support SQ2; workload profiling supports SQ3; selection supports SQ4; evaluation supports SQ5.

## 10. Draft synthesis for supervisor review, 12 October

The observations support a bounded account of Arno's recorded work and a provisional comparison of candidate areas, not an estimate of a typical complete day. The daily mix varies: within the improvement work, CHECK ranges from 4.2% to 38.3% of a day's minutes. Removing 18 September reduces checking from 91 to 34 recorded minutes, 8.3% of the remaining improvement time, which corresponds to workload anchor 3 instead of 5; with that score and everything else fixed, checking still leads by 7.6 points. This supports the recommendation of no further general observation days for the provisional selection; it is not a full reassessment after removing the day, and targeted checks still have to establish the task boundary, feasible data, reference answers and buyer acceptance. The Kruskal-Wallis calculations detect no clear rank difference in episode lengths between days (H = 2.76, p = 0.60) or in CHECK minutes per line (H = 0.66, p = 0.42); they establish neither equal days nor a stable activity mix.

The corrected CHECK comparison separates 18 September (38 minutes over 42 lines, 0.90 per line) from the other days (24 over 29, 0.83) and all days pooled (62 over 71, 0.87). It is descriptive and cannot supply a precise evaluation baseline. The distribution fits remain a description of the recorded episodes.

Order and confirmation checking remains a conditional recommendation. Dennis's explanation supports its business relevance, while usable matched documents, trusted references, case-specific buyer acceptance, Johan's confirmation and academic review still determine whether it is the defensible focal task. The [design draft](../process/Order_Confirmation_Checking_Design_Draft_2026-10-09.md) prepares the design and evaluation questions without claiming an implemented artifact or measured savings.

**To finalise this conclusion:** record Zhongxin's sufficiency and selection decisions and the agreed weights, evidence the data and reference gates, record Arno's confirmations, and freeze the evaluation design. These are open inputs, not blanks to fill with assumed answers.


## 11. To write into the thesis (Zhongxin, 13 October)

Zhongxin asked on 13 October ([chat record](../meetings/Academic_Supervisor_Chat_2026-10-13.md)) that the thesis explains two choices. Draft wording:

**Why Kendall's W, and not other tests (including Kruskal-Wallis).** The question was whether Arno's time is distributed over the activities in the same way on each observation day. The data form a table of five days by five activity codes, in which each day ranks the activities by the time spent on them. Kendall's coefficient of concordance W measures how far the days agree on that ranking (Kendall & Babington Smith, 1939); its significance test is the Friedman test on the same ranks (Friedman, 1937). Its null hypothesis is that the days rank the activities independently, so a significant W is positive evidence of a consistent pattern, whereas a non-significant result in a test of equality could not show that the days are the same. The Kruskal-Wallis test was not used for this question: it compares the distribution of one outcome across independent groups, while the activity times of one day are parts of the same day's total, not independent observations. A chi-square test of homogeneity was not used either, because recorded minutes are not independent counts. With five days the test has low power, so W is reported together with the rank correlation between each pair of days and the result with each day left out. The Kruskal-Wallis test was kept where its assumptions fit: to compare episode lengths across days (whether the work is equally fragmented) and CHECK minutes per order line between 18 September and the other days.

**Why this data table (data-preparation section).** Rows are the five timed activity codes (PO, CLAR, CHECK, SEND, OTHER); columns are the five observation days; each cell holds the in-scope recorded minutes of that activity on that day. Former EXC work is left out because it lies outside the improvement scope (decision of 1 October); REQ, DEC and REQ-Exact are untimed tallies without minutes; the single UNCLEAR minute is left out. Recorded minutes are used rather than observed clock time, because the observed time includes periods without a recorded activity. Minutes and shares of the day give identical ranks within each day, so the choice of denominator does not affect W.

**Bridge from the analysis to the selection (Zhongxin's interpretation, 13 October).** The activity mix agrees only moderately across the observation days (Kendall's W = 0.42), and no single activity is the most time-consuming on every day: CLAR leads on two days, PO on two and CHECK on one. Observed workload alone therefore does not identify one improvement target, which is why the selection combines it with feasibility gates and further criteria. Checking was not chosen because it is the largest activity (it is third, 16.2%), but because it combines recurring workload with AI fit, a possible reference answer per line and a business effect.

**Why two more observation days, and how they are reported (decided 13 October).** After the five-day analysis, Kendall's W showed moderate agreement and the Jensen-Shannon divergence singled out 8 September, with 18 September borderline. 8 September is explained from the records as a short, morning-only session (10:30 to 12:23, ended early by a company event) with several exceptions; 18 September by its checking volume. Two more days were added on 13 October, Wednesday 14 and Friday 16 October, to add an ordinary weekday and to see whether a second Friday is again check-heavy. Because the extension followed the first analysis, it was fixed in advance: exactly two days whatever their result, all seven days kept, and the five-day and seven-day results reported side by side. The data remain partial sessions of one buyer, and the conclusions are drawn within that limit.

**References to add.** Lin, J. (1991). Divergence measures based on the Shannon entropy. *IEEE Transactions on Information Theory, 37*(1), 145–151. https://doi.org/10.1109/18.61115 · Friedman, M. (1937). The use of ranks to avoid the assumption of normality implicit in the analysis of variance. *Journal of the American Statistical Association, 32*(200), 675–701. https://doi.org/10.1080/01621459.1937.10503522 · Kendall, M. G., & Babington Smith, B. (1939). The problem of m rankings. *The Annals of Mathematical Statistics, 10*(3), 275–287. https://doi.org/10.1214/aoms/1177732186
