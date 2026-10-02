# Kinds of work: codebook

**Created:** 30 September 2026, from the notes and case context of Arno's five baseline sessions. **Moved here:** 2 October 2026, together with the labels file, so that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) uses nothing from `analysis/`. The definitions, rules and labels are unchanged; the originals in `analysis/` stay as the record of the 1 October meeting.

- **Labels:** [`Kinds_Of_Work_Rows_2026-09-30.csv`](Kinds_Of_Work_Rows_2026-09-30.csv), one line per record with its date, row, case, activity code, minutes, stage, kinds and note. 275 of the 287 records have at least one kind; a record can have up to three.
- **Use in the notebook:** the saturation check in part 1; part 4 explains why the kinds are needed, where they come from, how each one fits under the analytical activities of the [purchasing activity framework](../process/Purchasing_Activity_Framework_2026-09-21.md), and how reliable they are; parts 5 to 9 use them for tasks, cases, problems, candidates and causes.
- **Reliability:** not yet established. One coder assigned the labels; a blind coding check by Yijie on a [sample of 45 records](Kinds_Coding_Check_Sample_2026-10-02.xlsx) is pending.
- **Method:** inductive (conventional) qualitative content analysis, with categories derived from the notes (Hsieh & Shannon, 2005; see the [literature register](../../literature/README.md#coding-the-observation-notes)).

## Kinds

| Code | Kind of work | Definition |
|---|---|---|
| K01 | Receive a request | Intake of a request: every row coded REQ, on all five days, next to any kind its note shows. |
| K02 | Create or complete a PO for a need | Enter or amend PO lines in Exact for a need, including adding lines, ordering via a supplier website and PO paperwork. |
| K03 | Maximalisatie and HOLD/order decision | Combine demand into an open PO for the same supplier, or try to, and decide to hold or order. |
| K04 | Check before ordering | Check price, and ETA where the supplier states it, against a quotation, website or supplier information before the PO is sent. |
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
| K17 | Check a supplier confirmation | After ordering: compare the confirmation with the PO on price and ETA, update Exact, attach the confirmation. |
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
- **Intake (K01):** every record coded REQ gets K01, next to any kind its note shows (for example 1 Sep row 7 is K01 and K16). K01 records that a request arrived, not what it asked for.
- **Records without a kind:** CLAR or CHECK records with no note (empty or `/`, which means none), or a note of only "Pause for now" or "Forward", which does not say what the work concerned. They have an empty kinds column.

## Decisions on specific records

- **18 Sep row 9 (Primer-C):** no kind, because the note marks it [uncertain].
- **18 Sep row 66 (OBS-21 pre-check, 20 minutes):** K04 only. The mismatch is mentioned under K18, but its minutes are not counted there because its share of the 20 minutes is unknown.
- **18 Sep row 73 (OBS-29, 6 minutes):** K18 only. The case note does not say whether the difference was found before ordering, at confirmation or at invoicing, so it is not also counted as a confirmation check (K17).
- **8 Sep, 12:04–12:13 (OBS-16, rows 35–36):** the 9 lost-focus minutes keep their kind but are left out of the analysis.

## Known corrections, not yet applied

- **REQ-Exact (2 October):** the 14 `REQ-Exact` records are cases that start from a PO Arno generated earlier, not requests ([scope addendum](Scope_and_Classification_Addendum_2026-09-14.md#recording-marks)). Their K01 label will be corrected together with the coding check.
