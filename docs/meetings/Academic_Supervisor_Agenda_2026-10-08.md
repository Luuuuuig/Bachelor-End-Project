# Academic Supervisor Meeting Agenda — 8 October 2026

**Time:** Thursday 15:00–16:00  
**Student:** Yijie Wang  
**Supervisor:** Zhongxin Hu  
**Project:** Reduce Operational Purchasing Workload at Hytech-Pommec using AI

This file has two parts. **Part A** is the agenda to send on Wednesday; it does not show Yijie's weights, scores or ranking, so that Zhongxin's swing weights stay independent (scoring brief, decision 2). **Part B** holds Yijie's notes for the meeting; do not send it.

---

## Part A: Agenda

### Meeting objective

Close the Analyze phase: agree the weights for the candidate comparison, review the provisional focal case and its proposed AI support, and agree what must be in place before Improve starts.

### 1. Since 1 October — 5 min

- The analysis of Arno's five sessions is complete. It follows the Plan of Work's sub-questions: SQ1 and SQ3 in the analysis, SQ4 in the selection. Former EXC is kept under OTHER, outside the improvement scope, and CHECK is compared per order line, as agreed on 1 October.
- The candidates were compared with veto gates first and weighted scores second (methodology §5.3).
- The Exact test account may be used, including processing its documents with an external AI service.

### 2. Scoring anchors and swing weights — 15 min

This item uses the [scoring brief](https://claude.ai/artifact/P2bsL8ZfyDhdJZanQAdk6n), decisions 1–4.

- Confirm or change the 1 / 3 / 5 anchors.
- Your own swing weights for the seven criteria, set without seeing mine. They can be sent before the meeting or filled in at its start.
- Buyer acceptance as a veto gate rather than a weighted criterion.
- How the figures I had already seen are handled and reported.

### 3. The provisional selection and the focal case — 10 min (after item 2)

- Gate verdicts, scores, totals and the sensitivity check.
- An updated task boundary for decision 5 of the brief, based on an observer clarification of what the recorded checks compared.

### 4. The proposed AI support — 10 min

- **Question:** is the proposed workflow an appropriate design-science artifact with a meaningful AI contribution? In it, AI reads the supplier documents and matches their lines to the PO, rules compare the values, and the buyer approves every action.

### 5. Gates before Improve — 5 min

- **Question:** does the focal case stay provisional until the test account shows representative cases with a trustworthy reference answer?
- **Question:** if it does not, does the next candidate go forward, rather than the failure being absorbed by a lower score?

### 6. Evaluation design (SQ5) — 8 min

- **Question:** is a comparison on historical cases in the Exact test environment sufficient for the BEP? The claim would be a demonstrated effect on test cases, not realised savings.
- What must be fixed before the prototype is built.

### 7. Three method checks — 5 min

- **Kinds of work:**
  - The kinds of work, coded from the notes and linked back to the task register and Van Weele's stages, are the detailed level of the analysis.
  - **Question:** is a targeted review of the labels that matter for the decision sufficient, instead of the optional 45-record recoding with kappa?
- **Arno:** is a short written confirmation enough instead of a full follow-up session? It would cover his acceptance of the proposed support, how many confirmations he checks per week and what difference is acceptable.
- **Dennis:** can broad observation stop, with Dennis involved only where the focal case changes his tasks?

### 8. Next steps — 2 min

- The planned start of Improve: requirements and the evaluation protocol.
- How to get feedback while the 29 October and early-November meetings are cancelled.

---

## Part B: Yijie's notes for the meeting (do not send)

### Item 2: swing weights

- My swings were recorded on 7 October, before any scoring ([record](../analyze/Swing_Weights_Yijie_2026-10-07.md)). Do not show them, or the ranking, until Zhongxin has given hers.
- After she gives hers: average the two sets, discuss every criterion where they differ by more than 10 points, then freeze the weights and rerun the comparison.
- **If she asks whether the weights are just opinion:** they are value judgements, as in any multi-criteria analysis (DCLG, 2009; Belton & Stewart, 2002). But each swing judges a concrete step on the written anchors, the swings were recorded before scoring, two independent sets are compared, and the result holds with equal weights.

### Item 3: the provisional selection

| Candidate | Total (my weights) |
|---|---:|
| **Order and confirmation checking** (called purchase-price control until 7 October) | **76.2** |
| Article / supplier data | 56.8 |
| Maximalisatie | 51.9 |
| Request intake & validation | 50.8 |

**Sensitivity.** It stays first in every check that changes one thing at a time:

| Check | Lead in points |
|---|---:|
| Equal weights | 17.1 |
| Each weight ±20% | 18.3 at the smallest |
| Each score ±1 | 14.1 at the smallest |
| Price-only workload (28 minutes) | 8.6 |

Six one-point changes combined within the recorded ranges would put article data first, and in the worst-case stress test article data leads (68.6 against 62.2). Four of those six changes depend on the test account.

**Updated boundary (decision 5).** Checking supplier quotations before ordering and confirmations after ordering against the PO, for price, delivery date, quantity and missing or extra lines.

**Workload evidence:**
- 98 of 560 in-scope minutes (17.5%), in 23 records and 19 case-days, on all five days; 66 of the minutes are on 18 September.
- From the notes alone: 28 minutes name price, 6 are a price check that could not be completed and 4 name a missing delivery date.
- My clarification as observer (7 October): the 56 minutes whose note gives no subject were regular price and delivery-date checks.
- So **94 of the 98 minutes are price or delivery-date checks**. Attaching the confirmation (4 minutes) always happens but was not always written down, so it is not counted as checking.
- The 28 price-named minutes remain the lower bound, and the result holds at that bound.
- The scores were set for the earlier price boundary and are unchanged. Ask her to review them against the widened boundary.

**Question to ask:** is the observer's clarification acceptable as evidence, when it is reported as a clarification and not as recorded data?

### Item 4: the proposed AI workflow

1. **Input:** the PO from Exact and the supplier's quotation or confirmation (PDF, scan, email or website).
2. **AI reads the document:** article, description, quantity, price, delivery date.
3. **AI matches** supplier lines to PO lines, even when the descriptions differ.
4. **Rules compare** price, quantity and delivery date, and find missing or extra lines. This step needs no AI.
5. **Summary** per order, with a recommended action: accept, review, or contact the supplier.
6. **AI drafts** the supplier email, for example listing the five PO lines missing from a confirmation, or proposes the correct value for Exact.
7. **Arno approves** before anything is sent or changed. This respects the buyers' concern of 1 October; in the test account the change itself may be automated.

**Possible objection:** "the comparison itself is just rules." Reply: yes, by design. The AI contribution is reading varied documents, matching lines and drafting. A precedent for invoices is Tater et al. (2022), not yet read in full.

### Item 5: gates

Checks PC1–PC4 in the test account:
- Are POs stored with their confirmations or quotations?
- Do the confirmations show delivery dates and all lines?
- Can the approved price per line be traced?
- Are there enough representative cases, and can they be exported?

For dates, quantities and missing lines, the PO itself is the reference answer; the price needs the approved price. If gates 2–3 fail, article / supplier data is assessed next (checks AR1–AR2). Report the result of the test-account check if it is done by then.

### Item 6: evaluation

Fix these before the prototype is built:
- **Unit:** one PO with its confirmation, or one line.
- **Eligible cases**, split into development cases and held-out evaluation cases.
- **The manual comparator, timed on the same cases.** The observed time per line is too imprecise to serve as the baseline: 0.87 minutes per line pooled; mean per check 1.24, with a 95% interval of 0.70–1.78.
- **The workload endpoint,** including the buyer's review and correction time.
- **The reference answer.**
- **The quality guardrail:** no missed critical difference.
- **The smallest worthwhile reduction Δ and the acceptable minor-error margin δ** ([methodology §6.1](../methodology/Phase_1_Current_Methodology.md#61-workload-endpoint-and-quality-guardrail)).

### Item 7: method checks

- **Task register:** it placed 137 of the 285 analysed records (48%) on one of its tasks, and only 14 of its 31 tasks were ever used.
- **Kinds of work:** they cover 257 of the 285 records. Linked back to the register: 8 kinds covered, 9 partly, 14 outside it.
- **The links agree with the September Task IDs:** 75%, 36% and 10% of the records were placed on a register task.
- The 285 records are the 287 minus the two lost-focus records of 8 September.

### Decisions to record during the meeting

| Decision | Outcome |
|---|---|
| Anchors confirmed or changed | |
| Zhongxin's swings received; differences over 10 points settled; weights frozen | |
| Buyer acceptance as a veto gate | |
| Updated boundary of the focal case accepted | |
| Observer clarification accepted as evidence | |
| The AI workflow is an appropriate artifact | |
| Focal case stays provisional until the test account passes; fallback order | |
| Evaluation in the test environment is sufficient | |
| Targeted label review instead of the 45-record recoding | |
| Short written confirmation from Arno instead of a session | |
| Dennis involved only where the focal case affects him | |
| Feedback route during the cancelled meetings | |
