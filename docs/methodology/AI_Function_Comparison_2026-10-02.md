# AI functions, observed tasks and buyer acceptance

**Prepared:** 2 October 2026 for the action from the [1 October supervisor meeting](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md): review literature on the kinds of work AI can support and compare them with what the buyers would accept, to set the boundaries of the solution. **Status:** working draft. No buyer acceptance has been assessed yet, and nothing here selects a candidate. Drawing retrieval and completeness, and a defined checking task, are the leading options to investigate; the buyers' answers may change that.

## How to read the table

- **Rows are concrete tasks** observed in Arno's five sessions. Each row names the function the AI would support, following Parasuraman, Sheridan and Wickens (2000): **retrieve** (information acquisition), **analyse** (information analysis), **recommend** (decision and action selection) or **execute** (action implementation). The same task can be supported at different levels of automation, and each level needs its own acceptance answer.
- **Communication is a task area, not a separate function.** Drafting a message (row 10) and sending it automatically (row 11) are separate rows with separate questions.
- **Evidence** names the supporting cases (date and OBS number) and the minutes the notes allow. "Minutes" are the rows whose note shows the task; "attributable" counts only rows that show nothing else. Where the notes cannot separate the task's own time, the table says so. Former EXC minutes are left out because that work is outside the improvement scope. All minutes are observed time in five sessions, not improvement potential or savings.
- **Acceptance** is recorded per person, with status (accepted, accepted with conditions, rejected, not yet assessed), conditions, date and evidence. Nobody's position is filled in without evidence from that person.
- **Sources for cases and minutes:** the [kinds-of-work codebook](../measurement/Kinds_Of_Work_Codebook.md) and the [2 October analysis notebook](../../Arno_Analysis_2026_10_02.ipynb). Literature details and their checking status are in the [literature register](../../literature/README.md#ai-functions-levels-of-automation-and-the-buyers-role).

## The table

| # | Observed task and evidence | Proposed AI function | Buyer's role | Literature and its limits | Acceptance | Feasibility (documents, rules, test examples) |
|---|---|---|---|---|---|---|
| 1 | **Find the drawings needed for an order.** 18 Sep OBS-10 and OBS-11, 23 Sep OBS-12: 6 rows, 24 min (13 attributable). | Retrieve: suggest candidate drawings. | Confirms the right drawing and revision; asks Engineering when one is missing. | Lombardi et al. (2025): title-block extraction supports searching building drawings. Different drawing domain; does not show that a set is complete or correctly revised. | Not yet assessed. | Where drawings are stored and how they link to items or orders: unknown. Test examples: the 18 and 23 September cases. |
| 2 | **Check whether a drawing set is complete.** 18 Sep OBS-10 (noting which drawings are missing, then a final completeness check), 23 Sep OBS-12 (Engineering had left part of the set out). Minutes not separable from row 1. | Analyse: compare required and available drawings and flag gaps. | Decides what is required and follows up with Engineering. | No source found that covers checking a drawing set for completeness. | Not yet assessed. | Needs a list of required drawings per order or item; its source is unknown. |
| 3 | **Interpret an ambiguous request quantity.** 1 Sep OBS-02 ("18 or 2 × 18"): 6 min clarifying and 8 min requesting a visual clarification. One case. | Analyse: flag a possible ambiguity. | Decides the meaning and asks the requester. | Šimsa et al. (2023, DocILE): extracting quantities and line items from business documents. Does not establish the intended meaning. | Not yet assessed. | Requests arrive by desk, mail and Exact; only one example so far. |
| 4 | **Collect item data to create an article in Exact.** 31 Aug OBS-07 (continued on 1 Sep), 1 Sep OBS-17, 8 Sep OBS-09 and OBS-10, 23 Sep OBS-17: 17 rows, 43 min (39 attributable). One case could not be finished because data were missing. | Retrieve and analyse: gather and structure item fields from supplier documents. | Checks the fields before creating the article; decides what to do when data are missing. | Šimsa et al. (2023): field extraction across document layouts. A benchmark, not a tested tool for this setting. | Not yet assessed. | Required Exact fields and supplier document formats: unknown. |
| 5 | **Check prices, and the ETA where stated, before sending the PO.** 31 Aug OBS-04, 1 Sep OBS-18, 8 Sep OBS-08, 18 Sep OBS-21, 23 Sep OBS-02: 6 rows, 37 min (31 attributable). Includes a 29-line check whose mismatch needed renewed approval, and a check blocked by an unpaid invoice. | Analyse: compare PO lines with quotation or website prices and flag differences. | Judges each difference, decides whether to order and seeks approval when needed. | Tater et al. (2022): matching invoice lines to PO lines with human review. Accounts-payable setting, so it needs adaptation and testing. | Not yet assessed. | Quotations come on paper, as PDF or from a website (8 Sep OBS-08 used both a paper quotation and the website). Examples from the five sessions. |
| 6 | **Check a supplier confirmation against the PO and update the ETA.** 13 cases on 31 Aug, 1 Sep and 18 Sep: 15 rows, 50 min (all attributable), including a 32-line check that had started before observation. | Analyse: compare confirmation lines with PO lines and flag price or date differences. Execute: update the ETA in Exact (a separate acceptance question). | Judges each difference and decides on follow-up. | Tater et al. (2022): the closest matching precedent. Šimsa et al. (2023): extracting line items from confirmations. | Not yet assessed. | Confirmation formats (email, PDF) and access to Exact for the comparison: unknown. |
| 7 | **Investigate a price difference.** 18 Sep OBS-02 and OBS-29: 2 rows, 11 min (plus 5 min of screenshots coded EXC, outside the improvement scope). | Analyse: bring together the item's price history. | Explains the difference and decides what to do. | Tater et al. (2022) covers flagging discrepancies, not explaining their cause. | Not yet assessed. | Price history in Exact: access unknown. |
| 8 | **Combine demand into an open PO and decide whether to hold or order (maximalisatie).** 15 cases, 18 rows, 42 min of combined PO and maximalisatie work; the decision time itself cannot be separated. An option to assess, not a selected candidate. | Recommend: suggest a combination or timing. | Makes the hold-or-order decision. | Parasuraman et al. (2000): support for decision selection at low levels of automation. No procurement-specific source yet. | Not yet assessed. | First establish the specific difficulty and what Exact already provides (Advies, Toewijzen). |
| 9 | **Prepare or complete PO lines in Exact.** 35 cases, 43 rows, 112 min (101 attributable). | Execute: prepare a draft order for the buyer to review. | Currently does all of it. | Burger et al. (2023): case studies of human expertise and AI in procurement; collaboration does not automatically improve performance. Parasuraman et al. (2000). | **Concern recorded, 1 October:** Yijie reported that the buyers were uncomfortable with AI preparing orders on its own while they only review and approve, because they would lose track of what was ordered ([meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md)). Not attributed to Arno or Dennis individually, and not a rejection of every form of order assistance. | Access to the Exact interface: unknown. |
| 10 | **Draft a clarification request or supplier message.** Clarifying missing or unclear information: 4 cases, 6 rows, 30 min; how much of that was writing is not recorded. The 71 SEND minutes cover sending and forwarding in general and are not all drafting. | Analyse and recommend: draft a message for the buyer to edit. | Edits the draft and decides whether to send it. | Noy and Zhang (2023): generative AI helped professionals with writing tasks in an experiment; not procurement-specific. Amershi et al. (2019): show limits and make correction easy. | Not yet assessed. | Typical message types and languages (Dutch, English): unknown. |
| 11 | **Send a message or forward a PO automatically.** Forwarding the PO to the supplier: 23 cases, 23 rows, 36 min (27 attributable). Exact generates the PO email and the buyer forwards it with a standard message (AS-IS process). | Execute: send without the buyer. | Currently sends every message. | Parasuraman et al. (2000): action implementation at high levels of automation, where keeping track of the work is hardest. | Not yet assessed; ask separately from row 10. | Exact and Outlook integration: unknown. Linked to the supporting opportunity "PO supplier communication" in the [methodology](Phase_1_Current_Methodology.md#4-current-candidate-portfolio). |

## Questions for Arno

Start with the work before mentioning AI, so the answers describe the problem rather than react to a solution.

These questions are part D of the [Arno follow-up session guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md), which also covers the causes of the work and the list of kinds of work.

1. Of the tasks in the table, which take the most effort or cause the most rework for you, and why?

For each task discussed (start with rows 1–2 and 5–6, then others as time allows):

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

Dennis can be asked after his return. The status values are: accepted, accepted with conditions, rejected, not yet assessed.

## Gaps to close

- No source yet covers checking a drawing set for completeness (row 2) or decision support for maximalisatie (row 8).
- The literature in this table has not been read in full yet; see the reading status in the register. Read Parasuraman et al. and Burger et al. first, then Lombardi et al. and Tater et al.
