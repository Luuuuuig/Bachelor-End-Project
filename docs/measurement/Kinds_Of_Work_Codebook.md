# Kinds of work: codebook

**Created:** 30 September 2026, from the notes and case context of Arno's five baseline sessions. **Moved here:** 2 October 2026, together with the labels file, so that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) uses nothing from `analysis/`. **Revised:** 6 October 2026, following the notebook review. The changes below preserve the original observation CSVs. The obsolete copies in `analysis/` were removed on 6 October; this codebook and the labels file below remain the current notebook inputs.

- **Labels:** [`Kinds_Of_Work_Rows_2026-09-30.csv`](Kinds_Of_Work_Rows_2026-09-30.csv), one line per record with its date, row, case, activity code, minutes, stage, kinds and note. 259 of the 287 records have at least one kind. Fourteen other records are known earlier-PO context markers, and 14 work records remain unclassified; a record can have up to three kinds.
- **Use in the notebook:** the saturation check in part 1; part 4 explains why the kinds are needed, where they come from, how each one fits under the analytical activities of the [purchasing activity framework](../process/Purchasing_Activity_Framework_2026-09-21.md), and their review status and limitations; parts 5 to 9 use them for tasks, cases, problems, candidates and causes.
- **Coding review (working approach, 7 October):** document a targeted review of ambiguous and decision-relevant labels across the competing candidates, using the original notes and dated clarifications. Record the rows reviewed, reason for review, retained or changed label and effect on the comparison. Preserve unresolved labels and unsplit mixed intervals where evidence is insufficient. This is a proportionate check of analytical decisions, not independent reliability evidence. The [45-record blind coding sheet](Kinds_Coding_Check_Sample_2026-10-02.xlsx) is retained as an optional, uncompleted exercise; neither completing it nor calculating κ is required to move forward.
- **Framework map:** each kind's place under the analytical activities and Van Weele stages is in [`Kinds_Framework_Map_2026-10-06.csv`](Kinds_Framework_Map_2026-10-06.csv).
- **Method:** inductive (conventional) qualitative content analysis, with categories derived from the notes (Hsieh & Shannon, 2005; see the [literature register](../../literature/README.md#coding-the-observation-notes)).

## Kinds

| Code | Kind of work | Definition |
|---|---|---|
| K01 | Receive a request | An incoming request marked REQ, except REQ-Exact, which identifies an earlier-generated PO. |
| K02 | PO preparation and completion | Broad PO preparation, entry, amendment and supporting paperwork. Includes combined intervals; it does not measure typing time separately. |
| K03 | MAX, demand consolidation and HOLD/order decisions | Combine demand into an open PO for the same supplier, or try to, and decide to hold or order. |
| K04 | Check before ordering | A check before release. Price comparison is explicit in some notes; retain unspecified check fields and types where the note does not establish them. |
| K05 | Send or forward the PO | Send the generated PO, or an approved PO, to the supplier. |
| K06 | Credit-card purchase | Buy through the credit-card route instead of the normal PO route. |
| K07 | Approval-related handling | Handling connected to Johan's approval: forwarding an approved PO, or noting that approval is awaited or needed again. Why approval was needed is not recorded, and the minutes are not measured approval or waiting time. |
| K08 | Clarify missing or unclear request information | Ask the requester or another party for information needed to complete an already defined request. |
| K09 | Establish or judge the requirement | Decide what exactly is needed: which option, technical suitability, whether an item is interchangeable. |
| K10 | Search historical POs or records | Look up earlier orders or item history to identify or verify an item. |
| K11 | Retrieve or complete drawings | Find, request or check drawings needed for an order. |
| K12 | Article or supplier data in Exact | Create or maintain article or supplier records, including requests and coordination about them. |
| K13 | Search for another supplier or better price | Look for an alternative or cheaper supplier, or ask for a better price. |
| K14 | Handle an unavailable item | Deal with an item a supplier cannot deliver: drop it, move it to another order or replace it. |
| K15 | Adjust an existing PO on request | Change an existing PO after a request about it. |
| K16 | Cancel a component or order line | Arrange the cancellation of a component or line, including the related PO change. |
| K17 | Monitoring checks and confirmation handling | Monitoring-stage CHECK records and related confirmation handling. Some check subtypes are unspecified; attachment is handling, not checking. Do not equate the entire category with price matching. |
| K18 | Investigate a price discrepancy | Look into a price difference, including documenting it. |
| K19 | Follow up order status or delivery | Supplier or internal question about an existing order: ETA, backorder, delay, partial delivery. |
| K20 | Finance-related issue | Unpaid invoices that block suppliers or checks, Finance questions, passing information to Finance. |
| K21 | Aftercare on a delivered order | Wrong or incorrect items received, or other aftercare on an earlier order. |
| K22 | Certification arrangements | Arranging certification by an external body (Lloyd), outside EXC. Its scope needs separate consideration. |
| K23 | Logistics coordination | Warehouse stock, collection, transport or questions about received items with Logistics. |
| K24 | Internal coordination with colleagues | Discussions with or answers to colleagues such as Dennis, Johan or Emiel, and passing information on. |
| K25 | Service or transport purchase | Purchasing a service such as maintenance, a service order or transport. |
| K26 | Exact error or delay | A fault or delay in Exact that affects the work. |
| K27 | Read or organise purchasing email | Reading or sorting purchasing email without a specific case. |
| K28 | Quotation or offer handling | Request, find, review or forward a quotation or offer. |
| K29 | Question from a customer, Sales or Service | A question that reaches purchasing from a customer, Sales or Service. |
| K30 | Administrative booking in Exact | Binnenboeken: administrative booking work in Exact. |
| K31 | Missing or attached certificate | A missing certificate, or attaching a certificate to a PO, recorded as EXC aftercare. |

## Coding rules

- A record can show up to three kinds.
- Code from the record's note and its case context. No kind is guessed from the case alone.
- **Intake (K01):** incoming REQ records get K01, next to any kind their notes show. REQ-Exact records are context markers for earlier-generated POs; they have `context_only=True` and no intake kind.
- **Records with little or no note:** a note that is empty, `/` (which means none), or only "Pause for now" or "Forward" does not say what the work concerned. Such a record is coded from its activity code, stage and case context where these show it: usually PO records as K02, SEND records as K05 and monitoring-stage CHECK records as K17, unless the case shows other work (for example K25 for a service purchase), and some CLAR records from their case (for example K14 in a case about an unavailable item). Where they do not show it, the record has no kind and an empty kinds column; most of these are CLAR records. *(6 October: this rule was earlier written as "CLAR or CHECK records with no note have no kind", which did not match the labels: seven such CLAR or CHECK records have a kind from their stage or case.)*

## Decisions on specific records

- **18 Sep row 9 (Primer-C):** no kind, because the note marks it [uncertain].
- **18 Sep row 66 (OBS-21 pre-check, 20 minutes):** K04 only. The mismatch is mentioned under K18, but its minutes are not counted there because its share of the 20 minutes is unknown.
- **18 Sep row 73 (OBS-29, 6 minutes):** K18 only. The case note does not say whether the difference was found before ordering, at confirmation or at invoicing, so it is not also counted as a confirmation check (K17).
- **8 Sep, 12:04–12:13 (OBS-16, rows 35–36):** the 9 lost-focus minutes keep their kind but are left out of the analysis.

## Corrections applied on 6 October 2026

- **REQ-Exact:** remove K01 from the 14 earlier-generated PO context markers. The notebook displays their original code as PO-REVISIT; no new work duration is imputed.
- **8 Sep row 18:** remove K02. “Organize” does not identify PO preparation.
- **8 Sep row 25:** remove K12. “Update it in Exact” does not identify master data.
- **18 Sep row 52:** add K03 alongside K02, because the original OBS-21 case note links maximalisatie to the initial PO interval. K03 includes consolidation and HOLD decisions as well as explicit MAX; do not report the whole category as explicit MAX alone.
- **18 Sep row 31:** keep K08 and K11 as occurrences, but mark `mixed_case_interval=True` and `drawings_case=OBS-10`. The four-minute interval combines clarification for OBS-11 with drawing discussion for OBS-10. Its task-level time cannot be split. Drawing-related rows therefore cover two target cases; the notebook shows 20 directly related recorded minutes plus four mixed minutes separately.
- **K17:** use the broader label above. Its 50 associated minutes comprise 46 CHECK minutes and four attachment minutes. Some CHECK subtypes are unknown.
- **1 Sep OBS-02 REQ:** clear the obsolete one-minute value in this derived labels file, matching the authorised tally correction in the original working CSV. The notebook always calculates durations from those working CSVs.

## Interpreting time and cases

Per-kind minutes are recorded interval minutes associated with a tag, not isolated complete-task durations or potential savings. Tags may overlap. Mixed intervals spanning different cases remain visible, with their minutes unallocated at task level. The notebook links the drawing tag in the mixed row to OBS-10 without inventing a separate timed drawing episode. A broad candidate covering both mixed activities may count that physical interval once; its time cannot be assigned to an individual task or target case.

Counts use observed case-days, not complete orders. Untimed occurrences contribute to counts and remain missing in duration summaries. Excluding former EXC is a descriptive filter, not confirmation that all other work is eligible for improvement.
