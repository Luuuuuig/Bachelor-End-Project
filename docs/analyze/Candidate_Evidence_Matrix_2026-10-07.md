# Candidate evidence matrix

**Prepared:** 7 October 2026. **Status:** evidence only. No candidate has been scored, and no score may be added until the Stage A gates are checked and the swing weights are agreed and frozen ([methodology §5.3](../methodology/Phase_1_Current_Methodology.md#53-formal-two-stage-selection-rule), [scoring brief](https://claude.ai/artifact/P2bsL8ZfyDhdJZanQAdk6n)).

For each candidate and Stage B criterion, this file lists what is already known, with its source, and what is still missing and where to get it. When scoring starts, each cell gets a score from 1 to 5 against the agreed anchors, with its evidence and uncertainty.

**Sources used:** the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) (parts 3 and 5–9), the [draft causes](Arno_Causes_Draft_2026-10-06.csv) (cause IDs such as PC-5), [what Yijie reported on 2 October](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october), the [AI function table](../methodology/AI_Function_Comparison_2026-10-02.md) (row numbers), the [1 October meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md) and the [opportunity profiles](../process/Process_Cleaned_V1.5.md#6-improvement-opportunity-profiles). Minutes are recorded minutes without former EXC, out of 560; they are observed parts of work in five sessions of one buyer, not task times or savings. The AI function table was prepared with the labels of 2 October, so its minutes can differ slightly from the notebook's; this file uses the notebook.

## Candidates

The five candidates of the [methodology's portfolio](../methodology/Phase_1_Current_Methodology.md#4-current-candidate-portfolio) and one area that is not yet a candidate.

| Candidate | Kinds of work in the notebook | Boundary still to decide |
|---|---|---|
| Purchase-price control | Order checks and price differences: K04, K17, K18 | Yes: all order checks, or price comparison only (brief, decision 5) |
| Order timing / maximalisatie / consolidation | K03 | No |
| Standard / review / manual process redesign | Process-level; no single kind. Closest task area: PO preparation and completion (K02) | Yes: which work the redesign covers, and what counts as a standard case |
| Request intake & validation | K08, K09, K10, K11 | No |
| PO supplier communication (supporting) | K05 | No |
| Article or supplier data in Exact | K12 | Yes: scored on its own or as part of request intake |

## Evidence status at a glance

**A** = enough evidence to score once the weights are frozen; **P** = some evidence, with a named gap; **M** = no evidence yet. This describes the evidence, not the candidate: a fully evidenced cell can still score 1.

| Criterion | Price control | Maximalisatie | Standard / review / manual | Request intake | PO communication | Article / supplier data |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Observed workload | P | A | P | A | A | P |
| Business value | P | P | M | P | M | M |
| AI–task fit | P | P | M | P | P | P |
| Data readiness | M | M | M | M | M | M |
| Repetition / standardisation | P | P | M | P | P | P |
| Prototype feasibility | M | M | M | M | M | M |
| Evaluation feasibility | P | M | M | M | P | P |

Data readiness and prototype feasibility are missing for every candidate: both depend on the Exact test-account check and the IT and access check, which have not been done.

---

## Purchase-price control

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | All order checks: 98 minutes (17.5%), 23 records, 19 case-days, all five days; 66 of the 98 minutes on 18 September. Of the 98: 28 minutes in 6 records whose note names a price check or difference (8 and 18 September, 25 minutes on 18 September), 56 with an unrecorded subject, 14 on other subjects. 26 minutes fall in the 5 case-days with a recorded problem; 47% of its case-days are picked up again (notebook, parts 8 and 9). | The task boundary (brief, decision 5). What a check normally compares, and how many confirmations are checked in a week (session guide, part B, questions 2–3). |
| Business value | Prices in Exact are not kept up to date because the buyers lack time (PC-5, Dennis via Yijie, 2 October). Supplier prices change (PC-10). One-off items are checked so an outdated price is not reused (PC-2, August notes). A €410 difference on 18 September OBS-29, attributed to a smaller quantity (PC-11). | The company supervisor's view of the effect, such as price errors avoided or costs, preferably with examples or figures. |
| AI–task fit | Analyse: compare quotation or confirmation lines with PO lines and flag differences (AI table rows 5–7). Closest precedent: Tater et al. (2022), invoice-to-PO matching in accounts payable, not yet read in full. Quotations arrive on paper, as PDF or from a website (8 September OBS-08); confirmations by email (August notes); Exact does not compare them with the PO (PC-6, reported). | Whether simple rules suffice once the fields are read (gate 6). Arno's acceptance of rows 5–6 (session guide, part D). |
| Data readiness | Johan permits using data in the Exact test account (reported 2 October). The test account holds past cases from an earlier period and is not up to date (reported 2 October). | Test-account check: are confirmations, quotations and approved prices stored with their POs; how many cases and from which period; is the correct outcome (the approved price) traceable? |
| Repetition / standardisation | Checks on all five days in 19 case-days; price named on two days. Inputs vary: 1 to 29 lines, and paper, PDF, website and email formats (notebook, part 3; AI table row 5). | Weekly frequency and the share of checks that find a difference (session guide, part B, question 3). |
| Prototype feasibility | None yet. The AI table lists confirmation formats and access to Exact for the comparison as unknown. | IT and access check: can POs, confirmations and price data be exported, and can a comparison run on exports without integration? |
| Evaluation feasibility | A possible reference answer: the approved or confirmed price per line (opportunity profile C: "objective discrepancy outcomes"). Zhongxin's fallback of 1 October: test workloads of orders with different numbers of lines, with human handling time estimated from the observations. The observed time per line is imprecise: 0.87 minutes pooled, a mean of 1.24 per check with a 95% interval of 0.70 to 1.78, and a slope that drops from 0.62 to 0.25 without the 29-line check (notebook, part 3). | Number of past cases with a known outcome. Buyer time for testing. Whether the fallback needs a more precise time per line. |

**Stage A questions first:** permission (gate 1) is reported; representativeness of the older test-account period (gate 2) and a traceable reference price (gate 3) are open.

## Order timing / maximalisatie / consolidation

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 43 minutes (7.7%), 19 records (16 timed), 16 case-days, all five days; 56% of its case-days are picked up again (notebook, part 8). The decision time cannot be separated from the PO work it is part of (codebook K03; AI table row 8). Holding a PO open is deliberate: Arno runs maximalisatie right after creating a PO and leaves non-urgent POs open for later demand (PO-2, PO-3, reported). Waiting time is not recorded. | Nothing for the share of time. |
| Business value | Dennis: each PO costs time and money (reported 2 October), so combining demand reduces the number of POs. | The company supervisor's view, for example the number or cost of POs avoided. |
| AI–task fit | Recommend: suggest a combination or timing, with the buyer deciding (AI table row 8). No procurement-specific source yet; Parasuraman et al. (2000) on low-level decision support. | What Exact's Advies already shows (notebook, part 8). The buyer's decision cues (session guide, part B, question 6). |
| Data readiness | The methodology names Exact/Orbis data on stock, future demand, open POs and lead times as the main dependency (methodology §4.1). | Test-account check: are open POs, advised demand, stock and lead-time histories available, and is Orbis needed? |
| Repetition / standardisation | 16 case-days on all five days. The decision depends on stock, urgency, minimum order values and context (opportunity profile A). | How demand to combine is found and when a held PO is ready to send (session guide, part B, question 6). |
| Prototype feasibility | None yet. | IT and access check, including Orbis. |
| Evaluation feasibility | None yet: the notebook lists "how an acceptable decision would be judged" as open. | A reference for a good decision, for example the buyer's actual decisions on past cases, and how to compare with it. |

**Stage A questions first:** data availability (gates 1–2) and a reference for a good decision (gate 3).

## Standard / review / manual process redesign

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | A process-level candidate, so no single kind of work. Related figures: PO preparation and completion takes 111 minutes (19.8%) in 34 case-days on all five days. 79 of 98 case-days (406 minutes) have no recorded problem, and 56 of these (213 minutes) are also handled in one stretch; the notebook states that these are not counts of standard cases (part 8). | The boundary: which work the redesign covers, so that a workload figure can be named. |
| Business value | None yet. | The company supervisor's view. |
| AI–task fit | The TO-BE hypothesis uses rules and automation for standard steps and AI only where unstructured information or ambiguity creates value. Preparing PO lines (AI table row 9): the buyers were uncomfortable with AI preparing orders on its own (1 October). | Which step of the redesign would use AI. Arno's view on partial help with order preparation (session guide, part D, question 17). |
| Data readiness | None yet. | Past cases with enough information to label them standard, review or manual. |
| Repetition / standardisation | The standard-case share is not established; a short or partly observed case can hide complexity (notebook, part 8). | What makes a case routine or exceptional (session guide, part B, question 5). |
| Prototype feasibility | None yet; routing cases is likely to need Exact integration. | IT and access check. |
| Evaluation feasibility | The methodology's possible measures need labelled cases: standard-case classification accuracy, exception-detection recall, exception escape rate (methodology §6). | A set of past cases labelled by the buyer. |

**Stage A questions first:** a defined boundary and standard-case criterion, then gates 2–4.

## Request intake & validation

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 94 minutes (16.8%), 19 records, 11 case-days, all five days: clarifying missing or unclear information 26 minutes (4 case-days), judging the requirement 23, searching old POs 21, drawings 20 plus 4 mixed minutes (notebook, parts 5 and 8). 53 of the 94 minutes fall in case-days with a recorded problem, partly because clarifying and finding drawings are problem kinds themselves (part 9). 46% of its case-days are picked up again. | Nothing for the share of time. |
| Business value | Engineering left part of a drawing set out (23 September OBS-12; RI-10). A suspicious serial number took 10–15 minutes to check against 5 minutes of entry (20 August notes; RI-4). | The company supervisor's view, for example delays caused by incomplete requests. |
| AI–task fit | Retrieve drawings (row 1; Lombardi et al., 2025, a different drawing domain); flag an ambiguous quantity (row 3; Šimsa et al., 2023); no source yet for checking that a drawing set is complete (row 2). | Arno's acceptance of rows 1–3 (session guide, part D). |
| Data readiness | Requests arrive by email, at the desk or by phone (RI-1, RI-5), so past requests may not be stored in Exact. Where drawings are stored and how they link to items is unknown (row 1). | Test-account and drawing-archive check. |
| Repetition / standardisation | 11 case-days on all five days. No clear pattern in which requests are incomplete (Arno via Yijie, 2 October). | A list of what each request type needs. |
| Prototype feasibility | None yet. | Access to the drawing archive and request history. |
| Evaluation feasibility | None yet: a reference needs a list of required drawings per item (row 2) or a definition of a complete request per type (notebook, part 8). | Whether such a list exists (session guide, part B, question 4). |

**Stage A questions first:** whether past requests and drawings are stored (gate 2) and a reference for completeness (gate 3).

## PO supplier communication (supporting)

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 36 minutes (6.4%), 23 records, 23 case-days, four days; 56.5% of its case-days are picked up again (notebook, part 8). Exact generates the PO email and the buyer forwards it with a standard message (AS-IS process). | Nothing for the share of time. |
| Business value | None beyond buyer time. | The company supervisor's view. |
| AI–task fit | Drafting a message for the buyer to edit (row 10; Noy and Zhang, 2023, not procurement-specific) and sending automatically (row 11) are separate questions. The notebook notes that ordinary automation may be enough (part 8); the methodology lists this as a supporting quick win, likely too narrow as the main case (§4.3). | Arno's acceptance of rows 10–11 (session guide, part D, question 18). |
| Data readiness | None yet. | Whether past PO emails are available. |
| Repetition / standardisation | 23 case-days on four days, with a standard message (AS-IS process). | Nothing beyond confirming the standard message. |
| Prototype feasibility | None yet; the AI table lists Exact and Outlook integration as unknown. | IT and access check. |
| Evaluation feasibility | The output can be checked against the sent email: recipient, attachment and message. | Access to past sent emails. |

**Stage A questions first:** AI fit beyond ordinary automation (gate 6).

## Article or supplier data in Exact

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 39 minutes (7.0%), 16 records (12 timed), 5 case-days on four days; 20% of its case-days are picked up again (notebook, part 8). One case continued over two days because required data were missing (31 August OBS-07). Articles are created by Arno or Dennis, suppliers mostly by Dennis (PO-6, reported). | Whether it is scored on its own or as part of request intake (brief, "Where things stand"). |
| Business value | None yet. | The company supervisor's view. |
| AI–task fit | Retrieve and structure item fields from supplier documents (row 4; Šimsa et al., 2023, a benchmark, not a tested tool). | Arno's acceptance of row 4. |
| Data readiness | None yet; required Exact fields and supplier document formats are unknown (row 4). | Test-account check of article records and their source documents. |
| Repetition / standardisation | 5 case-days on four days. | How often new articles are needed in a normal week. |
| Prototype feasibility | None yet. | IT and access check. |
| Evaluation feasibility | Existing article records could serve as the reference for extracted fields. | Whether past records and their source documents can be paired. |

**Stage A questions first:** whether past article records and source documents are available (gates 2–3).

---

## Evidence to collect, by source

| Source | What it settles | Cells |
|---|---|---|
| Zhongxin | Anchors, weights, the price-control boundary (brief, decisions 1–5) | Workload for price control; how all cells are scored |
| Exact test account (Yijie) | For each candidate, whether the needed records exist, how many, from which period, and whether the correct outcome is traceable | Data readiness and evaluation feasibility for all candidates |
| Session with Arno | What checks compare and how often; routine against exceptional cases; how demand is combined; required drawings; acceptance per AI function | Repetition and AI–task fit for all candidates; workload boundary for price control |
| Company supervisor | Business value beyond buyer time, with examples or figures | Business value for all candidates |
| IT and access check | Exports, Exact or Outlook integration, Orbis | Prototype feasibility for all candidates |
| Literature | Read Tater et al. (2022), Parasuraman et al. (2000), Burger et al. (2023) and Lombardi et al. (2025) in full | AI–task fit |
| Yijie's decision | Boundary of the standard / review / manual redesign; whether article data joins request intake | Workload for those two |
