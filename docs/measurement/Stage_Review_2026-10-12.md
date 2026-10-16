# Stage review of the daily CSVs, 12 October 2026

**Status:** the record of how the agreed `Van Weele stage` of every row in the five daily CSVs came about on 12 October 2026 (repository commit `00b9802ba6335076e27d6b674ef8de38f3c03bd6`). The earlier value of each changed row is listed in the [appendix](#appendix-the-100-changed-rows); the column `Original Van Weele stage` that held it was removed from the CSVs on 16 October because no analysis reads it (the CSVs of commit `00b9802` still carry it). **100 of the 287 rows changed; 187 did not.** The analysis notebook reads the agreed column and does not apply the rules in code; this document is the only record of how each stage was assigned. The [stage review of 30 September](Stage_Review_2026-09-30.md) records the earlier decisions per session; this file supersedes its unresolved-stage status.

Stage assignment does not change improvement scope: EXC and OTHER/EXC rows stay outside the improvement scope whatever their stage, and ordinary OTHER rows stay inside it. No code, note, time or volume was changed.

## 1. Three layers

Every row's agreed stage is explained by exactly one of three layers, in this order of precedence: a dated observer confirmation (B) overrides a rule (A); the context review (C) covers only rows that had no stage before 12 October and that no rule or confirmation reaches.

| Layer | Rows it covers | Of which changed | Minutes in those rows | Rows not coded EXC |
|---|---:|---:|---:|---:|
| A, rule 1: REQ -> Not applicable | 49 | 47 | 0 | 49 |
| A, rule 2a: CLAR without note -> Ordering | 11 | 4 | 39 | 11 |
| A, rule 2b: CLAR with note -> Specification | 29 | 25 | 108 | 29 |
| A, rule 3: CHECK without note -> Monitoring | 4 | 1 | 11 | 4 |
| B, observer confirmation (nine rows) | 9 | 8 | 26 | 6 |
| C, context review (fifteen rows) | 15 | 15 | 56 | 5 |
| No rule: the observer's stage of 30 September stands | 170 | 0 | 511 | 142 |
| **Total** | **287** | **100** | | **246** |

The minutes column counts all 287 rows, including the two 8 September OBS-16 rows (9 minutes) that the analysis leaves out for loss of observer focus. Of the 100 changed rows, 85 are in the 560-minute scope of the analysis, 13 are former EXC and 2 are the excluded OBS-16 rows; 48 of the 100 are untimed tallies (47 REQ markers and the CLAR tally of 31 August row 7), so the change moves 188 recorded minutes between stages, 131 of them in scope.

## 2. Layer A: observer rules (Yijie, 12 October 2026)

1. **All REQ records, including every REQ subtype, are Not applicable.** A request marker is not purchasing work in a stage, and it does not determine the stage of the later work in the same case. This covers REQ, REQ-mail, REQ-phone, REQ-desk, REQ-letter and the 14 REQ-Exact markers of earlier POs.
2. **CLAR without a note is Ordering**: obtaining information for ordering. **CLAR with a note is Specification.** Blank text, `/` and `—` count as no note. Two dated confirmations take precedence: 31 August row 16 and 23 September row 48 are Ordering although they are CLAR rows (see layer B).
3. **CHECK without a note is Monitoring**: a standard check of a confirmation after ordering. This rule applies to CHECK only and does not identify the field checked or the number of lines. The four rows are 31 August rows 13 (3 minutes) and 46 (1), 18 September row 6 (5) and 23 September row 46 (2); the first three already had Monitoring, the fourth was blank.

The rules are recording rules provided by the observer. They are not stages inferred from the content of the notes.

## 3. Layer B: nine row-specific confirmations (Yijie, 12 October 2026)

| Date | Row | Case | Code | Min | Note as recorded | Earlier stage | Agreed stage | What Yijie confirmed |
|---|---:|---|---|---:|---|---|---|---|
| 31 Aug | 16 | OBS-06 | CLAR | 1 | Onderhoud, so it is service | (blank) | Ordering | Clarification for a service PO belongs to Ordering |
| 31 Aug | 27 | OBS-04 | EXC | 2 | aftercare | (blank) | Monitoring | "Aftercare" meant following up outstanding orders or deliveries |
| 31 Aug | 57 | OBS-17 | EXC | 2 | Aftercare of a PO from last week | (blank) | Monitoring | As above |
| 1 Sep | 14 | OBS-08 | EXC | 2 | Exception/aftercare episode; subtype not captured reliably. | (blank) | Monitoring | As above; the row stays former EXC, outside scope |
| 1 Sep | 28 | OBS-17 | SEND | 1 | Forwarded the request. | (blank) | Specification | Forwarding item information after the request to add two items to Exact |
| 8 Sep | 35 | OBS-16 | PO | 2 | (none) | (blank) | Ordering | Ordinary PO creation |
| 8 Sep | 36 | OBS-16 | PO | 7 | (none) | (blank) | Ordering | Ordinary PO creation |
| 23 Sep | 47 | OBS-15 | OTHER | 2 | Walk to Emiel's desk to pass on information. | Ordering | Ordering | The walk was to obtain more information about the PO (stage unchanged) |
| 23 Sep | 48 | OBS-15 | CLAR | 7 | (none) | (blank) | Ordering | Ordinary PO clarification after that walk |

Nine rows, 26 minutes; eight of them changed. Rows 35 and 36 of 8 September are the two OBS-16 rows that the analysis leaves out for loss of observer focus; their stage is recorded here for completeness and plays no part in any result. Both the original note and the confirmed purpose stay visible.

## 4. Layer C: fifteen rows from the context review (Codex assistant, 12 October 2026)

These rows had no stage before 12 October and are not reached by a rule or a confirmation. Following Yijie's instruction, they were assigned from the recorded action and the context of the same case, with Not applicable where that context does not establish a purchasing purpose. They are review judgements, not observer confirmations. Ten rows are former EXC (42 minutes, outside scope); five are in scope (14 minutes).

| Date | Row | Case | Code | Min | Scope | Note as recorded | Agreed stage | Reason |
|---|---:|---|---|---:|---|---|---|---|
| 1 Sep | 25 | OBS-16 | EXC | 4 | former EXC | Respond to supplier question on an existing case. | Monitoring | Supplier follow-up on an existing case. |
| 1 Sep | 31 | OBS-19 | EXC | 5 | former EXC | Unavailable item: searched for an alternative and contacted manufacturer/supply source. | Supplier selection | Search for an alternative unavailable item and contact a manufacturer or supply source. |
| 1 Sep | 34 | OBS-20 | OTHER | 4 | in scope | Read purchasing-related email; exact case subtype not captured. | Not applicable | Purchasing email topic is not recorded; process purpose cannot be established. |
| 1 Sep | 35 | OBS-21 | EXC | 2 | former EXC | Supplier question originating from Sales. | Not applicable | Sales-origin supplier question does not identify its purchasing purpose. |
| 8 Sep | 12 | OBS-05 | EXC | 6 | former EXC | Call supplier to ask when and why; forwarding to colleague. | Monitoring | Supplier contact asks when and why, consistent with following up progress. |
| 8 Sep | 13 | OBS-06 | OTHER | 4 | in scope | Discussion with Dennis; decide to call Kayne. | Not applicable | Discussion and contact chain do not identify the process purpose. |
| 8 Sep | 14 | OBS-06 | EXC | 7 | former EXC | Kayne tell, to call Macro; then Arno has to ask Rudi. | Not applicable | The contact chain names people but does not identify the process purpose. |
| 8 Sep | 15 | OBS-06 | SEND | 1 | in scope | Attempt to call Rudi; failed, so writing email. | Not applicable | Continuation of the same contact chain; process purpose is not recorded. |
| 23 Sep | 10 | OBS-06 | OTHER | 2 | in scope | A client asked Arno something concerning Dennis. | Not applicable | General enquiry concerning Dennis; no purchasing-stage purpose is recorded. |
| 23 Sep | 12 | OBS-07 | EXC | 8 | former EXC | Germaine asked about a service order. | Monitoring | Service-order enquiry in the same case as the later ETA and payment follow-up. |
| 23 Sep | 13 | OBS-07 | EXC | 2 | former EXC | / | Monitoring | Continuation of the same service-order case, including its later ETA follow-up. |
| 23 Sep | 17 | OBS-07 | EXC | 2 | former EXC | Attempt to call Germaine. | Monitoring | Attempted contact within the same service-order and ETA follow-up case. |
| 23 Sep | 35 | OBS-13 | OTHER | 3 | in scope | Review an offer from Hydrasun and forward it to Kees. | Supplier selection | Review and forwarding of a supplier offer. |
| 23 Sep | 44 | OBS-07 | EXC | 4 | former EXC | Ask about the ETA and a payment issue; the source names Hytech. | Monitoring | Explicit ETA and payment follow-up. |
| 23 Sep | 52 | OBS-17 | EXC | 2 | former EXC | Germaine asked about an order. | Monitoring | Aftercare enquiry about an order. |

The 23 September OBS-07 rows follow the observer's 30 September clarification that the supplier first asked about a payment issue and Arno then asked for the ETA of another PO within row 44; the review reads the whole case as follow-up of outstanding orders. Yijie has not confirmed these fifteen assignments individually; the analysis notebook reports the five in-scope rows (14 minutes) in one sentence in section 4.2 and notes that none of them is Ordering.

## 5. What the 100 changes are

By earlier and agreed stage:

| Earlier stage | Agreed stage | Rows |
|---|---|---:|
| (blank) | Not applicable | 12 |
| (blank) | Monitoring | 11 |
| (blank) | Ordering | 6 |
| (blank) | Specification | 4 |
| (blank) | Supplier selection | 2 |
| Ordering | Not applicable | 31 |
| Ordering | Specification | 15 |
| Monitoring | Not applicable | 5 |
| Monitoring | Specification | 2 |
| Specification | Not applicable | 4 |
| Specification | Ordering | 1 |
| Not applicable | Specification | 4 |
| Not applicable | Ordering | 1 |
| Follow-up and evaluation | Not applicable | 1 |
| Supplier selection | Specification | 1 |
| **Total** | | **100** |

By layer: rule 1 (REQ) 47 rows, rule 2b (CLAR with note) 25, rule 2a (CLAR without note) 4, rule 3 (CHECK without note) 1, confirmations 8, context review 15. By day: 31 August 28, 1 September 17, 8 September 9, 18 September 23, 23 September 23. The 35 rows that were blank before 12 October are now all assigned; no blank stage remains.

**Effect on the 560 in-scope minutes** (computed from the two stage columns of the CSVs; the computation is Appendix B.4 of the analysis notebook as committed on 12 October, commit 542d6a5):

| Stage | Earlier column | Agreed column |
|---|---:|---:|
| Ordering | 334 min (59.6%) | 318 min (56.8%) |
| Specification | 47 (8.4%) | 121 (21.6%) |
| Monitoring | 77 (13.8%) | 68 (12.1%) |
| Not applicable | 26 (4.6%) | 25 (4.5%) |
| Follow-up and evaluation | 21 (3.8%) | 21 (3.8%) |
| Supplier selection | 14 (2.5%) | 7 (1.2%) |
| Unassigned | 41 (7.3%) | 0 |

Ordering stays the largest stage on every day. The largest movement is rule 2b: CLAR rows with a note (108 minutes) are now Specification, which is why Specification rises from 47 to 121 minutes.

## 6. Historical note: the archived kinds of work and the agreed stages

The kinds-of-work layer of 30 September to 9 October (K01 to K31, archived in [docs/archive/kinds_of_work](../archive/kinds_of_work/README.md)) gave each kind a purchasing stage in its framework map. Under the stages of 30 September, 149 of the 151 in-scope kind assignments with a single Van Weele stage agreed with the row's stage and the other two rows had no stage. Under the agreed stages of 12 October, 18 of the 151 disagree: 13 CLAR rows (11 whose kind maps to Ordering but which are now Specification by rule 2b, one whose kind maps to Supplier selection and which is now Specification, and one whose kind maps to Specification and which is now Ordering by rule 2a) and 5 REQ rows whose kinds carry a stage while the rows are now Not applicable by rule 1. Six more disagreements lie in former EXC rows. The map's stage column described the activity a kind names; the rules of 12 October assign the stage of a record from its code and the presence of a note. The disagreements follow from that difference, not from an error in either layer. The kinds layer is not used in the analysis since 12 October, so nothing was changed in it.

## 7. Addendum, 14 October 2026: the sixth observation day

The 39 rows of [14 October](Arno_Measurement_2026-10-14.csv) were assigned under the same rules, in the same order of precedence, on 14 October: layer A rules first (15 rows); then, where no rule reaches a row, the agreed stage of an earlier row with the same code and a comparable recorded action, named by date and row (23 rows); and only where neither decides, the layer C default (1 row, later confirmed by the observer; see below). Two review agents assigned the stages independently and agreed on all 39 rows; the precedents were re-read in their CSVs. The observer's enrichment of 14 October is used where it records the purpose (all three checks concerned attached order confirmations; OBS-16 was mainly establishing what had been ordered and delivered). The 100 changes of section 5 concern the first five days only. As before, stage does not change scope: the `OTHER/EXC` rows stay outside the improvement scope.

| Row | Case | Code | Min | Scope | Note as recorded | Agreed stage | Basis |
|---:|---|---|---:|---|---|---|---|
| 1 | OBS-01 | OTHER | 2 | in scope | Forward an unpaid invoice to Finance. | Follow-up and evaluation | Precedent: 31 Aug row 62 (OBS-16 OTHER 'Inform Finance', unpaid old POs) = Follow-up and evaluation; also 1 Sep row 13 (SEND forwarded to Finance) and 1 Sep row 17 (OTHER Finance question), both Follow-up and evaluation |
| 2 | OBS-02 | CLAR | 2 | in scope | Supplier quotation concerning a kit. | Specification | Rule: A2b |
| 3 | OBS-02 | PO | 2 | in scope | Create an article page for the kit in Exact. | Ordering | Precedent: 31 Aug row 21 (OBS-07 OTHER 'Input to Exact', article input request) = Ordering; 1 Sep row 33 (OTHER, continuation of article-master work) = Ordering |
| 4 | OBS-03 | CLAR | 1 | in scope | Check an Aircom quotation briefly, then close it without further … | Specification | Rule: A2b |
| 5 | OBS-03 | PO | 6 | in scope | Create an article page in Exact for the Aircom item. | Ordering | Precedent: 31 Aug row 21 (OTHER 'Input to Exact', article input) = Ordering; 1 Sep row 33 (article-master work) = Ordering |
| 6 | OBS-03 | SEND | 1 | in scope | Tell Germaine the article code. | Ordering | Precedent: 31 Aug row 49 (OBS-14 SEND 'Inform colleague') = Ordering; contrast 1 Sep row 28 (SEND forwarding a request to add items, Specification, layer B) |
| 7 | OBS-04 | REQ-mail |  | in scope | (none) | Not applicable | Rule: A1 |
| 8 | OBS-04 | PO | 3 | in scope | Try to combine the request with an existing PO, but none is available. | Ordering | Precedent: 18 Sep row 61 (OBS-23 PO 'Attempted maximisatie of the PO, without success') = Ordering; 8 Sep row 30 (PO 'Combine it to the existing PO') = Ordering |
| 9 | OBS-04 | SEND | 2 | in scope | Tell the requester the order will be purchased. Another order … | Ordering | Precedent: 31 Aug row 49 (SEND 'Inform colleague') = Ordering; 31 Aug row 30 (SEND after PO creation) = Ordering |
| 10 | OBS-03 | CLAR | 6 | in scope | A colleague updates Arno about the Aircom item; they clarify what … | Specification | Rule: A2b |
| 11 | OBS-03 | PO | 2 | in scope | Update the status in Exact. | Ordering | Precedent: 8 Sep row 25 (OBS-09 OTHER 'Update it in Exact', after a CLAR) = Ordering; 1 Sep row 40 (PO adjusting an existing PO) = Ordering |
| 12 | OBS-05 | CHECK | 2 | in scope | One item does not match. Update the price so it matches. OC attached. | Monitoring | Precedent: 18 Sep row 36 (CHECK 'Post-order price check') = Monitoring; 18 Sep row 73 (CHECK 'Large price difference', confirmation check) = Monitoring; 18 Sep row 23 (attaching an OC to the PO) = Monitoring |
| 13 | OBS-06 | CHECK | 3 | in scope | Two mismatches. OC attached. | Monitoring | Precedent: 18 Sep row 17 (OBS-07 CHECK 2L, confirmation check) = Monitoring; 18 Sep row 73 (CHECK, price difference on a confirmation) = Monitoring |
| 14 | OBS-07 | CLAR | 1 | in scope | Read it; no further action recorded. | Specification | Rule: A2b |
| 15 | OBS-08 | OTHER | 3 | in scope | Unpaid invoice. | Follow-up and evaluation | Precedent: 8 Sep row 3 (OBS-02 EXC 'Finance unpaid.') = Follow-up and evaluation; 1 Sep row 17 (OTHER Finance question) = Follow-up and evaluation |
| 16 | OBS-09 | REQ-mail |  | in scope | (none) | Not applicable | Rule: A1 |
| 17 | OBS-09 | PO | 2 | in scope | Transport order; ask Adriaans to transport something. | Ordering | Precedent: 8 Sep row 9 (OBS-03 PO 'See price 196 Euro, It is for transport') = Ordering |
| 18 | OBS-10 | SEND | 2 | in scope | (none) | Ordering | Observer confirmation (Yijie, 14 October 2026): sending a PO |
| 19 | OBS-11 | OTHER/EXC | 2 | former EXC | Wrong item. | Follow-up and evaluation | Precedent: 1 Sep row 5 (OBS-03 EXC 'Wrong order received') and row 6 (continuation of wrong-order aftercare) = Follow-up and evaluation |
| 20 | OBS-12 | REQ |  | in scope | (none) | Not applicable | Rule: A1 |
| 21 | OBS-12 | OTHER | 8 | in scope | Cancel an order and replace it with another order. | Ordering | Precedent: 8 Sep row 29 (OBS-10 OTHER 'Remove that component from old PO', within re-ordering) = Ordering; 18 Sep row 24 (items dropped from the order) = Ordering |
| 22 | OBS-13 | REQ-mail |  | in scope | (none) | Not applicable | Rule: A1 |
| 23 | OBS-13 | CLAR | 2 | in scope | Bojan's request lacks information needed to create an article in … | Specification | Rule: A2b |
| 24 | OBS-14 | CHECK | 6 | in scope | Five mismatches. | Monitoring | Precedent: 18 Sep row 73 (OBS-29 CHECK 'Large price difference', confirmation check) = Monitoring; 18 Sep row 36 (post-order price check) = Monitoring |
| 25 | OBS-13 | CLAR | 5 | in scope | Obtain information to create article numbers so Bojan can complete … | Specification | Rule: A2b |
| 26 | OBS-13 | PO | 1 | in scope | First article created. | Ordering | Precedent: 31 Aug row 21 (OBS-07 OTHER 'Input to Exact', article input) = Ordering; 1 Sep row 33 (article-master work) = Ordering |
| 27 | OBS-13 | CLAR | 1 | in scope | (none) | Ordering | Rule: A2a |
| 28 | OBS-13 | PO | 3 | in scope | Second article created. | Ordering | Precedent: 31 Aug row 21 (OTHER 'Input to Exact', article input) = Ordering; 1 Sep row 33 = Ordering |
| 29 | OBS-13 | CLAR | 2 | in scope | (none) | Ordering | Rule: A2a |
| 30 | OBS-13 | PO | 1 | in scope | (none) | Ordering | Precedent: 8 Sep rows 35-36 (OBS-16 PO without note, layer B 'ordinary PO creation') = Ordering; 31 Aug row 21 (article input) = Ordering |
| 31 | OBS-13 | SEND |  | in scope | (none) | Ordering | Precedent: 18 Sep row 33 (OBS-13 SEND without note after PO rows) = Ordering; 31 Aug row 53 (SEND without note after PO) = Ordering |
| 32 | OBS-14 | OTHER/EXC | 6 | former EXC | Aftercare, outside the improvement scope. | Monitoring | Precedent: 31 Aug row 27 (OBS-04 EXC 'aftercare' after CHECK rows in the same case) = Monitoring, layer B confirmation |
| 33 | OBS-12 | CLAR | 4 | in scope | Ask the requester for more details. | Specification | Rule: A2b |
| 34 | OBS-12 | PO | 5 | in scope | Create the replacement order. | Ordering | Precedent: 8 Sep rows 35-36 (layer B 'ordinary PO creation') = Ordering; 8 Sep row 27 (OBS-10 PO 2L after a supplier change) = Ordering |
| 35 | OBS-12 | CLAR | 5 | in scope | Determine how much needs cancelling. | Specification | Rule: A2b |
| 36 | OBS-15 | OTHER | 4 | in scope | Answer a question about an item. | Not applicable | Precedent: 23 Sep row 10 (OBS-06 OTHER 'A client asked Arno something', layer C) = Not applicable; 18 Sep row 39 (Maurice asked what a received item was for) = Not applicable |
| 37 | OBS-16 | REQ-mail |  | in scope | (none) | Not applicable | Rule: A1 |
| 38 | OBS-16 | OTHER/EXC | 75 | former EXC | Discuss existing orders with a colleague to establish what has … | Monitoring | Precedent: 31 Aug row 57 (EXC 'Aftercare of a PO from last week') = Monitoring, layer B; 18 Sep row 45 (OBS-16 EXC checked relevant POs and forwarded the information) = Monitoring |
| 39 | OBS-16 | OTHER/EXC |  | former EXC | With the details clarified, Arno goes downstairs to help locate … | Not applicable | Precedent: 23 Sep row 51 (OBS-16 EXC, helping Maurice locate a missing item Logistics had received and stored) = Not applicable |

**Observer confirmation and alternatives.** Row 18 (OBS-10, SEND, no note) was confirmed by Yijie on 14 October as sending a PO, so it is Ordering; the day therefore has 15 rule rows, 23 precedent rows and 1 confirmation. The other precedent-based rows follow the closest earlier row; their alternatives are recorded in the review: a status update that concerned delivery progress would be Monitoring (row 11), and a cancellation that corrected a problem with a delivered order would be Follow-up and evaluation (row 21).

## 8. Addendum, 16 October 2026: the seventh observation day

The 26 rows of [16 October](Arno_Measurement_2026-10-16.csv) were assigned on 16 October under the same rules and order of precedence: layer A (1 row, the REQ-Exact marker, rule A1); the agreed stage of an earlier row with the same code and a comparable recorded action, named by date and row (23 rows); the layer C judgement (1 row); and one observer confirmation (row 4). No CLAR row was recorded and both CHECK rows have notes, so rules A2a, A2b and A3 reach no row. Two review agents assigned the stages independently and agreed on 25 of the 26 rows; every cited precedent was checked against its CSV row and stage. Row 18 (OBS-08, a supplier change on a PO at Finance's request) has no precedent: one agent judged Ordering from the recorded action, a change to an existing PO; the other Follow-up and evaluation, because the earlier Finance rows concerned invoices. Ordering is kept, because layer C judges from the recorded action and Finance's reason was not recorded. Yijie reviewed all 26 stages on 16 October and agreed with them except row 4, which was changed from Not applicable to Follow-up and evaluation (see the table).

**Scope.** Eight rows are outside the improvement scope (29 minutes): rows 1, 13 and 25, whose notes record order aftercare; row 4, giving Logistics the serial number they could not find (help to Logistics, which the 1 October cheat sheet places outside the scope); rows 2 and 3, the status update in the continued OBS-16, which the observer confirmed on 16 October as part of the aftercare (coded `PO/EXC`, keeping the handwritten PO); and rows 17 and 18, changes to orders that the observer confirmed had already been sent. Rows 5 and 6 (the added line and the revised PO of the continued OBS-16) keep their codes and stay in scope. In scope: 42 of the 71 recorded minutes ([observation note, scope coding](Measure_Observation_2026-10-16.md#scope-coding-added-16-october)).

| Row | Case | Code | Min | Scope | Note as recorded | Agreed stage | Basis |
|---:|---|---|---:|---|---|---|---|
| 1 | OBS-16 (2026-10-14) | OTHER/EXC | 10 | former EXC | Order aftercare; question about a particular item. | Monitoring | Precedent: 31 Aug row 27 (OBS-04 EXC 'aftercare', layer B: aftercare = following up outstanding orders or deliveries) = Monitoring |
| 2 | OBS-16 (2026-10-14) | PO/EXC | 2 | former EXC | Update item status in Exact. Interrupted by a phone call. | Ordering | Precedent: 14 Oct row 11 (OBS-03 PO 'Update the status in Exact.') = Ordering |
| 3 | OBS-16 (2026-10-14) | PO/EXC | 1 | former EXC | Continue working in Exact. Logistics cannot find the item's serial … | Ordering | Precedent: 1 Sep row 41 (OBS-24 PO 'Resume and complete PO creation after interruption') = Ordering |
| 4 | OBS-01 | OTHER/EXC | 3 | former EXC | Give Logistics the serial number. | Follow-up and evaluation | Observer confirmation (Yijie, 16 October): the serial number of an item delivered under the OBS-16 orders is order information about a delivered item, like a missing or wrong certificate (18 Sep rows 68-69; row 25 of this day), not a search for goods as in the 1 October example; assigned Not applicable by precedent (14 Oct row 39) before |
| 5 | OBS-16 (2026-10-14) | PO | 3 | in scope | Originally 7L; add one line. | Ordering | Precedent: 23 Sep row 3 (OBS-03 PO 'One line added to an existing PO.') = Ordering |
| 6 | OBS-16 (2026-10-14) | SEND | 2 | in scope | Send the revised PO. | Ordering | Precedent: 14 Oct row 18 (OBS-10 SEND, observer-confirmed sending a PO) = Ordering |
| 7 | OBS-02 | PO | 4 | in scope | Create a PO for an existing service order. | Ordering | Precedent: 23 Sep row 23 (OBS-08 PO 'Service order.') = Ordering |
| 8 | OBS-02 | SEND | 4 | in scope | Attach all files. | Ordering | Precedent: 23 Sep row 24 (OBS-08 SEND after the service-order PO) = Ordering |
| 9 | OBS-02 | PO | 2 | in scope | Correct a wrong description. | Ordering | Precedent: 1 Sep row 40 (OBS-25 PO 'Adjust existing PO') = Ordering |
| 10 | OBS-02 | SEND | 2 | in scope | Resend and state the corrected description. | Ordering | Precedent: 14 Oct row 18 (SEND, confirmed sending a PO) = Ordering |
| 11 | OBS-03 | SEND | 7 | in scope | Approved by Johan but not yet sent. Send it and attach the … | Ordering | Precedent: 18 Sep row 47 (OBS-18 SEND 'Forward a PO approved by Johan.') = Ordering |
| 12 | OBS-02 | OTHER | 3 | in scope | Inform Finance about the related issue. | Follow-up and evaluation | Precedent: 31 Aug row 62 (OBS-16 OTHER 'Inform Finance') = Follow-up and evaluation |
| 13 | OBS-04 | OTHER/EXC | 5 | former EXC | Order aftercare. | Monitoring | Precedent: 31 Aug row 27 (OBS-04 EXC 'aftercare', layer B) = Monitoring |
| 14 | OBS-05 | CHECK | 2 | in scope | Unit prices match; quantity mismatch. | Monitoring | Precedent: 14 Oct row 13 (OBS-06 CHECK 2L 'Two mismatches. OC attached.') = Monitoring |
| 15 | OBS-06 | CHECK | 7 | in scope | Pre-control. | Ordering | Precedent: 23 Sep row 15 (OBS-02 CHECK 'Pre-control.') = Ordering |
| 16 | OBS-06 | SEND |  | in scope | (none) | Ordering | Precedent: 23 Sep row 16 (OBS-02 SEND '/' directly after CHECK 'Pre-control.') = Ordering |
| 17 | OBS-07 | OTHER/EXC | 1 | former EXC | Postpone an order because changes are needed following input from … | Ordering | Precedent: 14 Oct row 21 (OBS-12 OTHER 'Cancel an order and replace it with another order.') = Ordering |
| 18 | OBS-08 | OTHER/EXC | 3 | former EXC | Change the supplier on a PO at Finance's request. Arno says he … | Ordering | Judgement: the recorded action is a change to an existing PO (Ordering); Finance's reason was not recorded. Alternative, if the request came from invoice or payment matching: Follow-up and evaluation |
| 19 | OBS-09 | PO | 1 | in scope | One line added. | Ordering | Precedent: 23 Sep row 3 (PO 'One line added to an existing PO.') = Ordering |
| 20 | OBS-10 | PO | 1 | in scope | One line added for delivery costs. | Ordering | Precedent: 23 Sep row 3 (PO one line added) = Ordering |
| 21 | OBS-11 | REQ-Exact |  | in scope | (none) | Not applicable | Rule: A1 |
| 22 | OBS-11 | PO | 1 | in scope | (none) | Ordering | Precedent: 8 Sep rows 35-36 (OBS-16 PO without note, layer B 'ordinary PO creation') = Ordering |
| 23 | OBS-10 | SEND |  | in scope | (none) | Ordering | Precedent: 14 Oct row 18 (OBS-10 SEND without note, confirmed sending a PO) = Ordering |
| 24 | OBS-11 | SEND |  | in scope | (none) | Ordering | Precedent: 14 Oct row 31 (OBS-13 SEND without note, untimed, after PO) = Ordering |
| 25 | OBS-12 | OTHER/EXC | 4 | former EXC | Supplier sent the wrong certificate. Replace the old certificate … | Follow-up and evaluation | Precedent: 14 Oct row 19 (OBS-11 OTHER/EXC 'Wrong item.', called aftercare in the 14 Oct enrichment) = Follow-up and evaluation |
| 26 | OBS-13 | OTHER | 3 | in scope | Check Bojan's status regarding his transfer to the Purchasing … | Not applicable | Precedent: 23 Sep row 10 (OBS-06 OTHER, general enquiry concerning Dennis, layer C) = Not applicable |

**Settled by the observer's review, 16 October.** The stage alternatives first listed here are settled as assigned: row 14 (the quantity-mismatch check, Monitoring), rows 15 and 16 (the pre-control and its send, Ordering), row 12 (informing Finance, Follow-up and evaluation), row 25 (the wrong certificate, Follow-up and evaluation) and the other untimed sends without a note (rows 23 and 24, Ordering).

**Answered by the observer, 16 October.** The status update of rows 2 and 3 was part of the aftercare, and the orders of rows 17 and 18 had already been sent, so all four rows left the improvement scope (7 minutes); their stages stay as reviewed.

## Appendix: the 100 changed rows

Date and one-based source row identify each record in its daily CSV. Min is the recorded duration; blank means an untimed tally. Layer refers to sections 2 to 4.

| Date | Row | Case | Code | Min | Scope | Earlier stage | Agreed stage | Layer |
|---|---:|---|---|---:|---|---|---|---|
| 31 Aug | 1 | OBS-01 | REQ |  | in scope | Specification | Not applicable | Rule 1: REQ |
| 31 Aug | 2 | OBS-01 | CLAR | 10 | in scope | Specification | Ordering | Rule 2: CLAR without note |
| 31 Aug | 3 | OBS-02 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 6 | OBS-03 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 7 | OBS-03 | CLAR |  | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 8 | OBS-04 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 15 | OBS-06 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 16 | OBS-06 | CLAR | 1 | in scope | (blank) | Ordering | Confirmation (B) |
| 31 Aug | 19 | OBS-07 | REQ-email |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 20 | OBS-07 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 25 | OBS-07 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 26 | OBS-07 | CLAR | 4 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 27 | OBS-04 | EXC | 2 | former EXC | (blank) | Monitoring | Confirmation (B) |
| 31 Aug | 28 | OBS-08 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 31 | OBS-09 | REQ-email |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 34 | OBS-10 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 35 | OBS-10 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 36 | OBS-11 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 40 | OBS-12 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 43 | OBS-13 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 44 | OBS-13 | CLAR | 8 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 31 Aug | 47 | OBS-14 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 50 | OBS-15 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 54 | OBS-16 | REQ-Exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 31 Aug | 57 | OBS-17 | EXC | 2 | former EXC | (blank) | Monitoring | Confirmation (B) |
| 31 Aug | 60 | OBS-16 | REQ-call |  | in scope | Monitoring | Not applicable | Rule 1: REQ |
| 31 Aug | 61 | OBS-16 | CLAR | 6 | in scope | Monitoring | Specification | Rule 2: CLAR with note |
| 31 Aug | 63 | OBS-07 | CLAR | 1 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 1 Sep | 2 | OBS-02 | REQ |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 1 Sep | 3 | OBS-02 | CLAR | 6 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 1 Sep | 7 | OBS-04 | REQ |  | in scope | Specification | Not applicable | Rule 1: REQ |
| 1 Sep | 9 | OBS-05 | REQ |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 1 Sep | 10 | OBS-05 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 1 Sep | 14 | OBS-08 | EXC | 2 | former EXC | (blank) | Monitoring | Confirmation (B) |
| 1 Sep | 15 | OBS-09 | REQ |  | in scope | Monitoring | Not applicable | Rule 1: REQ |
| 1 Sep | 19 | OBS-12 | REQ |  | in scope | Specification | Not applicable | Rule 1: REQ |
| 1 Sep | 25 | OBS-16 | EXC | 4 | former EXC | (blank) | Monitoring | Context review (C) |
| 1 Sep | 26 | OBS-17 | REQ |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 1 Sep | 27 | OBS-17 | CLAR | 2 | in scope | (blank) | Specification | Rule 2: CLAR with note |
| 1 Sep | 28 | OBS-17 | SEND | 1 | in scope | (blank) | Specification | Confirmation (B) |
| 1 Sep | 29 | OBS-18 | REQ |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 1 Sep | 31 | OBS-19 | EXC | 5 | former EXC | (blank) | Supplier selection | Context review (C) |
| 1 Sep | 34 | OBS-20 | OTHER | 4 | in scope | (blank) | Not applicable | Context review (C) |
| 1 Sep | 35 | OBS-21 | EXC | 2 | former EXC | (blank) | Not applicable | Context review (C) |
| 1 Sep | 39 | OBS-25 | REQ |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 8 Sep | 7 | OBS-03 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 8 Sep | 12 | OBS-05 | EXC | 6 | former EXC | (blank) | Monitoring | Context review (C) |
| 8 Sep | 13 | OBS-06 | OTHER | 4 | in scope | (blank) | Not applicable | Context review (C) |
| 8 Sep | 14 | OBS-06 | EXC | 7 | former EXC | (blank) | Not applicable | Context review (C) |
| 8 Sep | 15 | OBS-06 | SEND | 1 | in scope | (blank) | Not applicable | Context review (C) |
| 8 Sep | 20 | OBS-08 | REQ-letter |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 8 Sep | 23 | OBS-09 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 8 Sep | 35 | OBS-16 | PO | 2 | excluded (OBS-16, lost focus) | (blank) | Ordering | Confirmation (B) |
| 8 Sep | 36 | OBS-16 | PO | 7 | excluded (OBS-16, lost focus) | (blank) | Ordering | Confirmation (B) |
| 18 Sep | 2 | OBS-02 | REQ-phone |  | in scope | Monitoring | Not applicable | Rule 1: REQ |
| 18 Sep | 3 | OBS-02 | CLAR | 5 | in scope | Monitoring | Specification | Rule 2: CLAR with note |
| 18 Sep | 4 | OBS-03 | REQ-phone |  | in scope | Follow-up and evaluation | Not applicable | Rule 1: REQ |
| 18 Sep | 10 | OBS-04 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 13 | OBS-05 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 19 | OBS-08 | CLAR | 2 | in scope | Not applicable | Specification | Rule 2: CLAR with note |
| 18 Sep | 20 | OBS-08 | CLAR | 2 | in scope | Not applicable | Specification | Rule 2: CLAR with note |
| 18 Sep | 21 | OBS-08 | CLAR | 1 | in scope | Not applicable | Specification | Rule 2: CLAR with note |
| 18 Sep | 22 | OBS-08 | CLAR | 2 | in scope | Not applicable | Specification | Rule 2: CLAR with note |
| 18 Sep | 26 | OBS-10 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 28 | OBS-10 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 18 Sep | 29 | OBS-11 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 31 | OBS-11 | CLAR | 4 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 18 Sep | 41 | OBS-10 | CLAR | 4 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 18 Sep | 44 | OBS-16 | REQ-mail |  | in scope | Monitoring | Not applicable | Rule 1: REQ |
| 18 Sep | 48 | OBS-19 | CLAR | 10 | in scope | Supplier selection | Specification | Rule 2: CLAR with note |
| 18 Sep | 51 | OBS-21 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 55 | OBS-21 | CLAR | 2 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 18 Sep | 57 | OBS-22 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 60 | OBS-23 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 63 | OBS-24 | REQ-exact |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 18 Sep | 70 | OBS-27 | REQ-phone |  | in scope | Monitoring | Not applicable | Rule 1: REQ |
| 18 Sep | 72 | OBS-28 | CLAR | 3 | in scope | (blank) | Specification | Rule 2: CLAR with note |
| 23 Sep | 9 | OBS-06 | REQ-phone |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 23 Sep | 10 | OBS-06 | OTHER | 2 | in scope | (blank) | Not applicable | Context review (C) |
| 23 Sep | 11 | OBS-07 | REQ-phone |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 23 Sep | 12 | OBS-07 | EXC | 8 | former EXC | (blank) | Monitoring | Context review (C) |
| 23 Sep | 13 | OBS-07 | EXC | 2 | former EXC | (blank) | Monitoring | Context review (C) |
| 23 Sep | 17 | OBS-07 | EXC | 2 | former EXC | (blank) | Monitoring | Context review (C) |
| 23 Sep | 19 | OBS-08 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 23 Sep | 20 | OBS-08 | CLAR | 3 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 23 Sep | 28 | OBS-11 | REQ-mail |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 23 Sep | 29 | OBS-11 | CLAR | 1 | in scope | (blank) | Ordering | Rule 2: CLAR without note |
| 23 Sep | 31 | OBS-11 | CLAR | 3 | in scope | (blank) | Specification | Rule 2: CLAR with note |
| 23 Sep | 32 | OBS-12 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 23 Sep | 34 | OBS-12 | CLAR | 5 | in scope | Ordering | Specification | Rule 2: CLAR with note |
| 23 Sep | 35 | OBS-13 | OTHER | 3 | in scope | (blank) | Supplier selection | Context review (C) |
| 23 Sep | 37 | OBS-14 | REQ-mail |  | in scope | Specification | Not applicable | Rule 1: REQ |
| 23 Sep | 43 | OBS-15 | REQ-mail |  | in scope | Ordering | Not applicable | Rule 1: REQ |
| 23 Sep | 44 | OBS-07 | EXC | 4 | former EXC | (blank) | Monitoring | Context review (C) |
| 23 Sep | 46 | OBS-15 | CHECK | 2 | in scope | (blank) | Monitoring | Rule 3: CHECK without note |
| 23 Sep | 48 | OBS-15 | CLAR | 7 | in scope | (blank) | Ordering | Confirmation (B) |
| 23 Sep | 50 | OBS-16 | CLAR | 5 | in scope | Not applicable | Ordering | Rule 2: CLAR without note |
| 23 Sep | 52 | OBS-17 | EXC | 2 | former EXC | (blank) | Monitoring | Context review (C) |
| 23 Sep | 53 | OBS-17 | REQ-mail |  | in scope | (blank) | Not applicable | Rule 1: REQ |
| 23 Sep | 54 | OBS-17 | CLAR | 7 | in scope | (blank) | Ordering | Rule 2: CLAR without note |
