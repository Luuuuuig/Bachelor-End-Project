# Candidate evidence matrix

**Prepared:** 7 October 2026. **Evidence and boundary review:** 9 October 2026. **Status:** evidence supporting a provisional comparison. Final selection requires the relevant Stage A checks, agreed weights and supervisor review ([methodology §5.3](../methodology/Phase_1_Current_Methodology.md#53-formal-two-stage-selection-rule), [scoring brief](https://claude.ai/artifact/P2bsL8ZfyDhdJZanQAdk6n)).

**Update, 7 October:** at Yijie's request a provisional selection was made from this evidence before Zhongxin's weights, in [Focal_Case_Selection_2026-10-07.ipynb](../../Focal_Case_Selection_2026-10-07.ipynb). Its gate verdicts and scores, with the evidence from this matrix, are in parts 3 and 6 of that notebook; they stay provisional until Zhongxin has reviewed them and the test-account checks are done.

For each candidate and Stage B criterion, this file lists what is known, its source and the remaining gap. Provisional scores from 1 to 5 already exist; their final use depends on the agreed anchors, relevant evidence and uncertainty review. These gaps are a menu for resolving consequential uncertainty, not a requirement to investigate every candidate equally.

**Sources used:** the [15 September Dennis notes](../meetings/Internship_notes_2026-09-15.md#prices-and-updates), the [8 October supervisor notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md#buyer-acceptance-and-the-business-value-example), the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) (parts 5–10), the [draft causes](Arno_Causes_Draft_2026-10-06.csv) (cause IDs such as PC-5), [what Yijie reported on 2 October](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october), the [AI function table](../methodology/AI_Function_Comparison_2026-10-02.md) (row numbers), the [1 October meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md) and the [opportunity profiles](../process/Process_Cleaned_V1.5.md#6-improvement-opportunity-profiles). Minutes are recorded minutes without former EXC, out of 560; they are observed parts of work in five sessions of one buyer, not task times or savings. The AI function table contains illustrative cases and acceptance questions; it now defers quantitative reporting to the notebook and this evidence matrix rather than repeating old counts.

## Candidates

The six areas below document the [methodology's portfolio](../methodology/Phase_1_Current_Methodology.md#4-current-candidate-portfolio). The provisional comparison scores order and confirmation checking (called purchase-price control until 7 October), article/supplier data and narrowed versions of maximalisatie and request intake. Stand-alone routing is not a feasible primary artifact in its current form; PO communication remains an ordinary-automation opportunity.

| Candidate | Kinds of work in the notebook | Boundary still to decide |
|---|---|---|
| Order and confirmation checking | K04, K17, K18 | Widened on 7 October: quotations before ordering and confirmations after ordering, checked against the PO for price, delivery date, quantity and missing or extra lines. Review with Zhongxin; no final choice was made on 8 October. Quantity and missing/extra-line coverage still need separate evidence. |
| Order timing / maximalisatie / consolidation | K03 | Provisionally narrowed to presenting related demand/open POs; the buyer retains the hold/order decision. |
| Standard / review / manual process redesign | Process-level; no single kind. Closest task area: K02 | Retained as a design concept rather than a selected stand-alone artifact; buyer acceptance remains open. |
| Request intake & validation | K08, K09, K10, K11 | Provisionally narrowed to retrieving prior POs/drawings; completeness assessment lacks a demonstrated reference. |
| PO supplier communication (supporting) | K05 | Ordinary-automation recommendation rather than primary AI case. |
| Article or supplier data in Exact | K12 | Scored separately as the first fallback; actual source documents and reference records still need checking. |

## Boundary review for final scoring

**Desk review, 9 October.** The boundaries below make the existing alternatives comparable. They are proposed research boundaries, not new buyer approvals. The 8 October meeting selected no final task. Keep the four shortlisted options and the two supporting/design options distinct.

| Candidate | Input and proposed output | Included work | Excluded from this candidate |
|---|---|---|---|
| Order and confirmation checking | A proposed/current PO version plus a quotation before ordering or a confirmation afterwards; show source-linked fields, line matches and discrepancies to the buyer | Read/match/flag price, delivery date, quantity and missing/extra lines; buyer checks and decides | Automatic PO creation, sending, price-master updates, accepting changed dates/prices or autonomous release of an unflagged order |
| Article / supplier data | Supplier source document plus required fields; buyer-reviewed candidate field values | Bounded extraction and preparation of article/supplier data | Autonomous master-data creation or approval; unrelated request clarification |
| Maximalisatie | Permitted open POs/pending demand; list potentially related same-supplier demand | Retrieval and presentation for the buyer | Deciding when to hold/order, optimization without a reference, or treating all 43 K03 minutes as avoidable retrieval time |
| Request intake | Item description plus available earlier POs/drawings; source-linked retrieval results | Finding prior POs/drawings, corresponding to the narrowed 45 recorded minutes | Proving drawing-set completeness, judging technical suitability or claiming all 94 broad intake minutes belong to retrieval |
| PO supplier communication | Existing PO and message/recipient information; possible draft or conventional routing support | A supporting opportunity for later assessment | A primary AI case and assumed approval for automatic sending |
| Standard / review / manual | A design distinction for the chosen bounded task | Human review and manual fallback | A selected end-to-end routing artifact or automatic acceptance of a no-flag result |

For the focal case, the PO is a comparison input, not automatically the correct business answer. Document dates, versions, item identifiers, quantity/units and agreed tolerances must be interpretable. A changed delivery date may be faithfully extracted and correctly flagged while still requiring a buyer decision about acceptability. None of these references has been demonstrated by the current document review.

### Review of the broadened order-checking scores

The 7 October scenario retains scores **5, 3, 4, 3, 3, 3, 4**, ranges and weights unchanged. It gives **76.2/100**. It used price-focused evidence and broad checking workload. This review identifies what carries over and what does not; it does not silently endorse the old scores for new fields. The clarified [criterion definitions and anchors](../methodology/Phase_1_Current_Methodology.md#criterion-definitions-and-rationale) also require review before final rescoring.

| Criterion | Evidence that carries over | What the wider boundary still needs before a final score |
|---|---|---|
| Workload, 5 (4–5) | 98 minutes of broad checks, including 4 minutes attaching a confirmation. 28 minutes explicitly name price. The observer clarified 56 minutes as price/date checks, giving 94 minutes related to price/date. | Review decision-relevant labels. These totals do not separately measure quantity or missing/extra-line checks and do not establish time savings. Two 18 September K18 episodes (source rows 3 and 73, 5 + 6 minutes) have an unresolved quotation/confirmation versus other price-work boundary. Retain broad, price/date and price-named distinctions. |
| Business value, 3 (3–4) | Dennis's account supports qualitative price-related business relevance. | Explain the route from a flag to a useful business action. Date, quantity and missing/extra-line benefits need their own examples if they affect the score. A score above 3 needs the company supervisor's confirmation with examples or figures (the original anchor); do not invent a financial impact. |
| AI fit, 4 (3–4) | Heterogeneous supplier documents and proposed extraction/line matching. | Inspect actual examples for every retained field. Compare AI extraction/matching with simpler methods; exact field comparison remains rule-based where appropriate. |
| Data readiness, 3 (2–4) | Permission and the existence of PO records; paired supplier documents remain unverified. | Inventory paired versions and all retained fields, units and item identifiers. If adequate inputs are unavailable, reopen gate 2 rather than merely lowering a score. |
| Repetition, 3 (3–4) | Checks occurred on five days, with varying formats and 1–29 lines. | Establish whether the broader field checks form a repeatable routine and identify exception boundaries. Historical minutes cannot supply weekly rates. |
| Prototype feasibility, 3 (3–4) | A bounded export-based prototype is proposed. | Demonstrate exports and assess line matching, unit conversion and date handling for the retained scope. No tested export route is claimed. |
| Evaluation feasibility, 4 (3–5) | Price-reference concept and a possible manual-versus-assisted test. | Demonstrate references for transcription, discrepancies and accepted outcomes across retained fields, case mix and buyer availability. Gate 3 stays open until then. |

**Targeted source-review finding, 9 October:** the [review log](Targeted_Label_Review_2026-10-09.csv) records the source-to-label desk check and unresolved coding-owner decisions. 18 September source row 3 is a 5-minute Kayne price enquiry and row 73 a 6-minute price investigation involving the €410 difference. Both remain broad K18 evidence, but the notes do not establish the document/process boundary required for the narrower quotation/confirmation artifact. Their 11 minutes must not be presented as confirmed eligible intervention time. The mixed MAX/PO interval on 31 August row 52 also needs comparison with 18 September row 52 before any K02/K03 relabelling. No raw times, labels or scores are changed here.

**B07 status:** the existing scores have been reviewed for their applicability and the unclosed items identified. No final numerical rescore is justified from the documents alone. Record actual test-account/buyer findings, agree the boundary and anchors, then change scores and ranges with reasons and rerun the comparison.

## Evidence status at a glance

**A** = enough evidence to score once the weights are frozen; **P** = some evidence, with a named gap; **M** = no evidence yet. This describes the evidence, not the candidate: a fully evidenced cell can still score 1.

| Criterion | Order and confirmation checking | Maximalisatie | Standard / review / manual | Request intake | PO communication | Article / supplier data |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Observed workload | P | A | P | A | A | P |
| Business value | P (qualitative relevance supported) | P | M | P | M | M |
| AI–task fit | P | P | M | P | P | P |
| Data readiness | M | M | M | M | M | M |
| Repetition / standardisation | P | P | M | P | P | P |
| Prototype feasibility | M | M | M | M | M | M |
| Evaluation feasibility | P | M | M | M | P | P |

Data readiness and prototype feasibility have no completed inspection result in the reviewed evidence. Permission and a proposed export route are recorded, but do not demonstrate usable paired inputs or a working export. Resolve these checks for the focal case first and extend to alternatives only when the choice depends on them.

---

## Order and confirmation checking

Called purchase-price control until 7 October, when the boundary was widened from price to price, delivery date, quantity and missing or extra lines.

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | All order checks: 98 minutes (17.5%), 23 records, 19 case-days, all five days; 66 of the 98 minutes on 18 September. Of the 98: 28 minutes in 6 records whose note names a price check or difference (8 and 18 September, 25 minutes on 18 September), 6 in a price check that could not be completed, 4 naming a missing delivery date, 4 attaching a confirmation and 56 with an unrecorded subject. By the observer's clarification of 7 October, those 56 were regular price and delivery-date checks, so 94 of the 98 minutes are checks of price and/or delivery date. 26 minutes fall in the 5 case-days with a recorded problem; 47% of its case-days are picked up again (notebook, parts 9 and 10). | Zhongxin's agreement to the widened boundary (brief, decision 5). How many confirmations are checked in a week (session guide, part B, question 3); what a check compares is answered by the clarification. |
| Business value | Dennis reported Sales selling items at a loss because sales prices used outdated purchase prices ([15 September, Prices and updates](../meetings/Internship_notes_2026-09-15.md#prices-and-updates)). The [2 October account](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october) records his explanation that regular updates are not done because the buyers lack time. Yijie repeated the business-value example at the [8 October meeting](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md#buyer-acceptance-and-the-business-value-example). This supports qualitative relevance beyond buyer time. The €410 difference on 18 September OBS-29 is a discrepancy example, not a measured loss or saving. | Johan's view of the effect, with examples or figures, for a score above 3. Financial impact and achievable benefit are not quantified. Establish whether the proposed checking output reaches the price-maintenance/Sales-pricing handoff before claiming it prevents that loss. Extra managerial input is conditional on a consequential unresolved assumption. |
| AI–task fit | Analyse: compare quotation or confirmation lines with PO lines and flag differences (AI table rows 5–7). Closest precedent: Tater et al. (2022), invoice-to-PO matching in accounts payable, not yet read in full. Quotations arrive on paper, as PDF or from a website (8 September OBS-08); confirmations by email (August notes); Exact does not compare them with the PO (PC-6, reported). | Whether simple rules suffice once the fields are read (gate 6). Arno's acceptance of rows 5–6 (session guide, part D). |
| Data readiness | Johan permits using data in the Exact test account (reported 2 October) and processing its documents with an external AI service (confirmed by Yijie on 7 October). The test account holds past cases from an earlier period and is not up to date (reported 2 October). | Test-account check: are confirmations, quotations and approved prices stored with their POs; how many cases and from which period; is the correct outcome (the approved price) traceable? |
| Repetition / standardisation | Checks on all five days in 19 case-days; price named on two days. Inputs vary: 1 to 29 lines, and paper, PDF, website and email formats (notebook, part 5; AI table row 5). | Weekly frequency and the share of checks that find a difference (session guide, part B, question 3). |
| Prototype feasibility | None yet. The AI table lists confirmation formats and access to Exact for the comparison as unknown. | IT and access check: can POs, confirmations and price data be exported, and can a comparison run on exports without integration? |
| Evaluation feasibility | A possible reference answer: a buyer-validated approved price per line, with the applicable source and version. A supplier confirmation states what the supplier confirmed but is not automatically the accepted price. For other fields, distinguish document transcription, comparison with the PO and the accepted business action. The original opportunity profile C proposes objective discrepancy outcomes; it does not demonstrate a validated reference set. Zhongxin's fallback of 1 October: test workloads of orders with different numbers of lines, with human handling time estimated from the observations. The observed time per line is imprecise: 0.87 minutes pooled, a mean of 1.24 per check with a 95% interval of 0.70 to 1.78, and a slope that drops from 0.62 to 0.25 without the 29-line check (notebook, part 5). | Paired documents, agreed source hierarchy and reference labels for price, date, quantity and line presence. Number and mix of cases, buyer time and a manual comparator for the selected scope. Constructed test workloads need validated answers; an estimated time baseline must be reported separately from a timed comparison. |

**Stage A questions first:** permission (gate 1) is confirmed, including an external AI service (7 October); representativeness of the older test-account period (gate 2) and a traceable reference price (gate 3) are open.

## Order timing / maximalisatie / consolidation

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 43 minutes (7.7%), 19 records (16 timed), 16 case-days, all five days; 56% of its case-days are picked up again (notebook, part 9). The decision time cannot be separated from the PO work it is part of (codebook K03; AI table row 8). Holding a PO open is deliberate: Arno runs maximalisatie right after creating a PO and leaves non-urgent POs open for later demand (PO-2, PO-3, reported). Waiting time is not recorded. | Nothing for the share of time. |
| Business value | Dennis: each PO costs time and money (reported 2 October), so combining demand reduces the number of POs. | The company supervisor's view, for example the number or cost of POs avoided. |
| AI–task fit | Recommend: suggest a combination or timing, with the buyer deciding (AI table row 8). No procurement-specific source yet; Parasuraman et al. (2000) on low-level decision support. | What Exact's Advies already shows (notebook, part 9). The buyer's decision cues (session guide, part B, question 6). |
| Data readiness | The methodology names Exact/Orbis data on stock, future demand, open POs and lead times as the main dependency (methodology §4.1). | Test-account check: are open POs, advised demand, stock and lead-time histories available, and is Orbis needed? |
| Repetition / standardisation | 16 case-days on all five days. The decision depends on stock, urgency, minimum order values and context (opportunity profile A). | How demand to combine is found and when a held PO is ready to send (session guide, part B, question 6). |
| Prototype feasibility | None yet. | IT and access check, including Orbis. |
| Evaluation feasibility | None yet: the notebook lists "how an acceptable decision would be judged" as open. | A reference for a good decision, for example the buyer's actual decisions on past cases, and how to compare with it. |

**Stage A questions first:** data availability (gates 1–2) and a reference for a good decision (gate 3).

## Standard / review / manual process redesign

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | A process-level candidate, so no single kind of work. Related figures: PO preparation and completion takes 111 minutes (19.8%) in 34 case-days on all five days. 79 of 98 case-days (406 minutes) have no recorded problem, and 56 of these (213 minutes) are also handled in one stretch; the notebook states that these are not counts of standard cases (part 9). | The boundary: which work the redesign covers, so that a workload figure can be named. |
| Business value | None yet. | The company supervisor's view. |
| AI–task fit | The TO-BE hypothesis uses rules and automation for standard steps and AI only where unstructured information or ambiguity creates value. Yijie reported on 8 October that both buyers strongly opposed the example of automatic PO creation and email sending because of control, awareness and work-interest concerns. This does not establish rejection or acceptance of a bounded reading/matching/flagging aid. | Which step of the redesign would use AI. Arno's view on partial help with order preparation (session guide, part D, question 17). |
| Data readiness | None yet. | Past cases with enough information to label them standard, review or manual. |
| Repetition / standardisation | The standard-case share is not established; a short or partly observed case can hide complexity (notebook, part 9). | What makes a case routine or exceptional (session guide, part B, question 5). |
| Prototype feasibility | None yet; routing cases is likely to need Exact integration. | IT and access check. |
| Evaluation feasibility | The methodology's possible measures need labelled cases: standard-case classification accuracy, exception-detection recall, exception escape rate (methodology §6). | A set of past cases labelled by the buyer. |

**Stage A questions first:** a defined boundary and standard-case criterion, then gates 2–4.

## Request intake & validation

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 94 minutes (16.8%), 19 records, 11 case-days, all five days: clarifying missing or unclear information 26 minutes (4 case-days), judging the requirement 23, searching old POs 21, drawings 20 plus 4 mixed minutes (notebook, parts 6 and 9). 53 of the 94 minutes fall in case-days with a recorded problem, partly because clarifying and finding drawings are problem kinds themselves (part 10). 46% of its case-days are picked up again. | Nothing for the share of time. |
| Business value | Engineering left part of a drawing set out (23 September OBS-12; RI-10). A suspicious serial number took 10–15 minutes to check against 5 minutes of entry (20 August notes; RI-4). | The company supervisor's view, for example delays caused by incomplete requests. |
| AI–task fit | Retrieve drawings (row 1; Lombardi et al., 2025, a different drawing domain); flag an ambiguous quantity (row 3; Šimsa et al., 2023); no source yet for checking that a drawing set is complete (row 2). | Arno's acceptance of rows 1–3 (session guide, part D). |
| Data readiness | Requests arrive by email, at the desk or by phone (RI-1, RI-5), so past requests may not be stored in Exact. Where drawings are stored and how they link to items is unknown (row 1). | Test-account and drawing-archive check. |
| Repetition / standardisation | 11 case-days on all five days. No clear pattern in which requests are incomplete (Arno via Yijie, 2 October). | A list of what each request type needs. |
| Prototype feasibility | None yet. | Access to the drawing archive and request history. |
| Evaluation feasibility | None yet: a reference needs a list of required drawings per item (row 2) or a definition of a complete request per type (notebook, part 9). | Whether such a list exists (session guide, part B, question 4). |

**Stage A questions first:** whether past requests and drawings are stored (gate 2) and a reference for completeness (gate 3).

## PO supplier communication (supporting)

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 36 minutes (6.4%), 23 records, 23 case-days, four days; 56.5% of its case-days are picked up again (notebook, part 9). Exact generates the PO email and the buyer forwards it with a standard message (AS-IS process). | Nothing for the share of time. |
| Business value | None beyond buyer time. | The company supervisor's view. |
| AI–task fit | Drafting a message for the buyer to edit (row 10; Noy and Zhang, 2023, not procurement-specific) and sending automatically (row 11) are separate questions. The notebook notes that ordinary automation may be enough (part 9); the methodology lists this as a supporting quick win, likely too narrow as the main case (§4.3). | Arno's acceptance of rows 10–11 (session guide, part D, question 18). |
| Data readiness | None yet. | Whether past PO emails are available. |
| Repetition / standardisation | 23 case-days on four days, with a standard message (AS-IS process). | Nothing beyond confirming the standard message. |
| Prototype feasibility | None yet; the AI table lists Exact and Outlook integration as unknown. | IT and access check. |
| Evaluation feasibility | The output can be checked against the sent email: recipient, attachment and message. | Access to past sent emails. |

**Stage A questions first:** AI fit beyond ordinary automation (gate 6).

## Article or supplier data in Exact

| Criterion | Evidence now (source) | Missing, and where to get it |
|---|---|---|
| Observed workload | 39 minutes (7.0%), 16 records (12 timed), 5 case-days on four days; 20% of its case-days are picked up again (notebook, part 9). One case continued over two days because required data were missing (31 August OBS-07). Articles are created by Arno or Dennis, suppliers mostly by Dennis (PO-6, reported). | Already scored separately in the 7 October scenario. Keep K12 separate from the narrowed request-intake workload and establish the fallback boundary only if it is pursued. |
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
| Zhongxin | Review criterion definitions, anchors, weighting procedure and focal boundary, as discussed on 8 October (independent weights remain an existing proposal) | Workload for order and confirmation checking; how all cells are scored |
| Exact test account (Yijie) | PC1–PC4 first, then common/focal checks for period, representativeness, exports and testing. Check alternatives when a gate fails or the comparison needs that evidence. | Data readiness and evaluation feasibility |
| Session with Arno | Relevant causes, how often confirmations are checked and differ, trusted prices and accepted support. Other candidate prompts only where needed. | Focal-case repetition and AI–task fit |
| Company supervisor | Business value and feasibility of the proposed choice, with examples or figures; alternatives if needed. Dennis's 15 September explanation is the starting example to confirm. | Business-value evidence |
| IT and access check | Whether the selected bounded prototype can work on permitted exports; integration/Orbis only if necessary | Prototype feasibility |
| Literature | Verify/read the sources actually used for the selected design and analytical method, beginning with the literature register's reading order | Evidence for method and AI–task fit |
| Yijie's classification decisions | Resolve the explicit owner questions in the [9 October source-to-label review](Targeted_Label_Review_2026-10-09.csv). The desk review retained current labels and records boundary limits; it does not establish independent coding reliability. The 45-record exercise remains optional. | Interpretation supporting the comparison, without a whole-dataset reliability claim |
