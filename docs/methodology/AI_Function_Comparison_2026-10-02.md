# AI functions, observed tasks and buyer acceptance

**Prepared:** 2 October 2026 for the action from the [1 October supervisor meeting](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md): review literature on the kinds of work AI can support and compare them with what the buyers would accept, to set the boundaries of the solution. **Status:** working draft. No person-specific buyer acceptance assessment is recorded yet, and this table does not select a candidate. The 7 October provisional comparison puts purchase-price control first, subject to the outstanding feasibility checks and supervisor review in the [methodology](Phase_1_Current_Methodology.md). Prioritise its checking functions in the acceptance discussion; retain the other rows as alternatives, not a requirement to investigate every function.

## How to read the table

- **Rows are concrete tasks** observed in Arno's five sessions. Each row names the function the AI would support, following Parasuraman, Sheridan and Wickens (2000): **retrieve** (information acquisition), **analyse** (information analysis), **recommend** (decision and action selection) or **execute** (action implementation). The same task can be supported at different levels of automation, and each level needs its own acceptance answer.
- **Communication is a task area, not a separate function.** Drafting a message (row 10) and sending it automatically (row 11) are separate rows with separate questions.
- **Evidence** gives illustrative source cases and task boundaries, not duplicate workload totals. The table supports the discussion of AI functions and acceptance; observed tasks do not establish that the proposed AI function is feasible or accepted. Former EXC remains outside the improvement scope, and combined intervals are not isolated task durations or savings.
- **Acceptance** is recorded per person, with status (accepted, accepted with conditions, rejected, not yet assessed), conditions, date and evidence. Nobody's position is filled in without evidence from that person.
- **Quantitative authority:** use the current [Arno analysis notebook](../../Arno_Analysis_2026_10_02.ipynb), parts 4–9, and the [candidate evidence matrix](../analyze/Candidate_Evidence_Matrix_2026-10-07.md) for counts, recorded minutes and their limits. The [codebook](../measurement/Kinds_Of_Work_Codebook.md) defines the labels. Earlier aggregates in this table were removed on 7 October to avoid repeating superseded classifications.
- **Literature status:** the descriptions below remain provisional source notes, not claims of completed full-text reading. Consult the [literature register](../../literature/README.md#ai-functions-levels-of-automation-and-the-buyers-role) for each source’s checking status and verify claims before thesis citation.

## The table

| # | Observed task and evidence | Proposed AI function | Buyer's role | Literature and its limits | Acceptance | Feasibility (documents, rules, test examples) |
|---|---|---|---|---|---|---|
| 1 | **Find the drawings needed for an order.** 18 Sep OBS-10 and 23 Sep OBS-12. The 18 Sep interval recorded under OBS-11 combines clarification for OBS-11 with drawing discussion for OBS-10; it is not another drawing case or a separately timed drawing task. | Retrieve: suggest candidate drawings. | Confirms the right drawing and revision; asks Engineering when one is missing. | Lombardi et al. (2025): title-block extraction supports searching building drawings. Different drawing domain; does not show that a set is complete or correctly revised. | Not yet assessed. | Where drawings are stored and how they link to items or orders: unknown. Test examples: the 18 and 23 September cases. |
| 2 | **Check whether a drawing set is complete.** 18 Sep OBS-10 records missing drawings and a later completeness check; 23 Sep OBS-12 records an incomplete set from Engineering. Retrieval and completeness work are not separately timed. | Analyse: compare required and available drawings and flag gaps. | Decides what is required and follows up with Engineering. | No source found that covers checking a drawing set for completeness. | Not yet assessed. | Needs a list of required drawings per order or item; its source is unknown. |
| 3 | **Interpret an ambiguous request quantity.** 1 Sep OBS-02 asks whether the request meant “18 or 2 × 18” and seeks visual clarification. This example establishes an ambiguity, not its normal frequency. | Analyse: flag a possible ambiguity. | Decides the meaning and asks the requester. | Šimsa et al. (2023, DocILE): extracting quantities and line items from business documents. Does not establish the intended meaning. | Not yet assessed. | Requests can arrive by desk, mail or other channels; REQ-Exact context markers identify earlier-generated POs rather than new incoming requests. The clarification example does not establish a representative test set. |
| 4 | **Collect item data to create an article in Exact.** 31 Aug OBS-07, continued on 1 Sep: article-master work could not be completed because required data were missing. Requests or coordination about article creation do not establish completed creation. | Retrieve and analyse: gather and structure item fields from supplier documents. | Checks the fields before creating the article; decides what to do when data are missing. | Šimsa et al. (2023): field extraction across document layouts. A benchmark, not a tested tool for this setting. | Not yet assessed. | Required Exact fields and supplier document formats: unknown. |
| 5 | **Check an order before sending it, including price where explicit.** 8 Sep OBS-08 uses a paper quotation and a website for price comparison; 18 Sep OBS-21 records a mismatch and renewed approval. In 1 Sep OBS-18, delivery time was adjusted but price control was blocked by an unpaid-invoice issue. Generic pre-checks do not identify every field compared. | Analyse: compare PO lines with quotation or website prices and flag differences. | Judges each difference, decides whether to order and seeks approval when needed. | Tater et al. (2022): matching invoice lines to PO lines with human review. Accounts-payable setting, so it needs adaptation and testing. | Not yet assessed. | Quotations come on paper, as PDF or from a website (8 Sep OBS-08 used both a paper quotation and the website). Examples from the five sessions. |
| 6 | **Check a supplier confirmation against the PO and handle its record.** 18 Sep OBS-01 records a monitoring check that began before observation; OBS-02 separately records attaching a confirmation. Attachment is handling, not checking. Unspecified check subjects are not assumed to be price matching. | Analyse: compare confirmation lines with PO lines and flag differences in the agreed fields. Execute: update the ETA in Exact where required (a separate acceptance question). | Judges each difference and decides on follow-up. | Tater et al. (2022): the closest matching precedent. Šimsa et al. (2023): extracting line items from confirmations. | Not yet assessed. | Confirmation formats (email, PDF) and access to Exact for the comparison: unknown. |
| 7 | **Investigate a price difference.** 18 Sep OBS-02 and OBS-29 record price discrepancies. The separately EXC-coded screenshot work remains outside improvement scope; the OBS-29 note does not establish when the difference was discovered. | Analyse: bring together the item's price history. | Explains the difference and decides what to do. | Tater et al. (2022) covers flagging discrepancies, not explaining their cause. | Not yet assessed. | Price history in Exact: access unknown. |
| 8 | **Combine demand and decide whether to hold or order (maximalisatie).** 1 Sep OBS-27 records added demand followed by HOLD; OBS-29 records added demand without a captured final hold/order outcome. Combined PO/MAX intervals do not isolate decision time. | Recommend: suggest a combination or timing. | Makes the hold-or-order decision. | Parasuraman et al. (2000): support for decision selection at low levels of automation. No procurement-specific source yet. | Not yet assessed. | First establish the specific difficulty and what Exact already provides (Advies, Toewijzen). |
| 9 | **Prepare or complete PO lines in Exact.** 23 Sep OBS-02 and OBS-04 record additions to existing POs. PO preparation is a broad activity that can include amendment and supporting work in combined intervals; it is not pure typing time. | Execute: prepare a draft order for the buyer to review. | Reviews the prepared content, retains purchasing decisions and handles any remaining work. | Burger et al. (2023): case studies of human expertise and AI in procurement; collaboration does not automatically improve performance. Parasuraman et al. (2000). | **Concern recorded, 1 October:** Yijie reported that the buyers were uncomfortable with AI preparing orders on its own while they only review and approve, because they would lose track of what was ordered ([meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md)). Not attributed to Arno or Dennis individually, and not a rejection of every form of order assistance. | Access to the Exact interface: unknown. |
| 10 | **Clarify missing information and communicate with requesters or suppliers.** 1 Sep OBS-02 requests visual clarification; OBS-12 requests a quotation or external information. Drafting is a proposed support function: its time is not isolated, and SEND also includes forwarding and other communication. | Analyse and recommend: draft a message for the buyer to edit. | Edits the draft and decides whether to send it. | Noy and Zhang (2023): generative AI helped professionals with writing tasks in an experiment; not procurement-specific. Amershi et al. (2019): show limits and make correction easy. | Not yet assessed. | Typical message types and languages (Dutch, English): unknown. |
| 11 | **Send a message or forward a PO.** 23 Sep OBS-02 records SEND after pre-control. The AS-IS process describes Exact generating the PO email and the buyer forwarding it with a standard message. This does not establish that every SEND record is supplier-PO dispatch. | Execute: send without the buyer. | Reviews and sends purchasing communication in the observed workflow. | Parasuraman et al. (2000): action implementation at high levels of automation, where keeping track of the work is hardest. | Not yet assessed; ask separately from row 10. | Exact and Outlook integration: unknown. Linked to the supporting opportunity "PO supplier communication" in the [methodology](Phase_1_Current_Methodology.md#4-current-candidate-portfolio). |

## Questions for Arno

Start with the work before mentioning AI, so the answers describe the problem rather than react to a solution.

These questions are part D of the [Arno follow-up session guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), which also covers the causes of the work and the list of kinds of work.

1. Of the tasks in the table, which take the most effort or cause the most rework for you, and why?

For each task discussed (start with checking functions in rows 5–6 for the provisional price-control case; discuss other rows only where they affect the comparison or selected boundary):

2. Which documents or information do you use, and where do you find them?
3. What makes the result correct, and how do you notice a mistake?
4. Would it help if a system found, flagged, drafted or suggested this for you? What would you still want to check yourself?
5. Which decisions must stay with you?
6. Under which conditions would you use it, for example if it shows its source, lets you correct it easily, or never acts on its own?
7. Are there past orders, confirmations or drawings we could use to test it?

Order preparation:

8. On 1 October I reported a concern about AI preparing orders on its own while the buyer only approves. Does that match your view? Would partial help, such as a prepared line you complete yourself, be different?

Messages:

9. Would you want a drafted message that you can edit? Separately: would you ever let a message be sent without you?

## Recording the answers

Record one line per person, task and function. Fill in a status only from that person's own answers.

| Person | Row | Function and level | Status | Conditions | Date | Evidence |
|---|---|---|---|---|---|---|
| Arno | | | Not yet assessed | | | |

Ask Dennis targeted questions after his return if the proposed support affects his responsibilities or a material source/ownership question remains. His existing observation evidence is separate from an acceptance answer. The status values are: accepted, accepted with conditions, rejected, not yet assessed.

## Gaps to close

- The literature in this table has not been read in full yet; see the reading status and [reading order](../../literature/README.md#reading-order-for-the-current-work) in the register. Prioritise the function/buyer-role framework and the source relevant to the selected checking task; verify claims before thesis citation.
- Drawing-set completeness (row 2) and maximalisatie (row 8) still lack directly applicable support here. Reopen these literature gaps only if those alternatives remain relevant to the decision or design.
