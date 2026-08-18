# Internship notes, 17 August 2026

## Context

These notes summarize observations and discussions from the internship at Hytech-Pommec on 17 August 2026. They were reconstructed from handwritten notes and clarified afterward.

The project objective is to investigate how AI, automation, or process improvements could reduce the workload of Arnold, the operational buyer, increase his efficiency, and remove unnecessary work from the purchasing process.

A useful way to structure the project is into two connected tracks:

1. **Arnold focus:** identify tasks performed by Arnold that are repetitive, relatively simple, time-consuming, or suitable for AI support.
2. **Process-improvement focus:** examine the wider purchasing process for duplicated work, unnecessary handovers, unclear responsibilities, and steps that could be simplified before deciding whether AI is needed.

## Current staffing situation

There was previously both operational and technical purchasing support related to this work. The technical buyer is no longer available to support Arnold in the same way. The exact reason or transition is not yet clear, but the practical consequence is that Arnold can no longer rely on this technical-buyer support.

This makes Arnold's current workload an important starting point for the project.

## Discussion with Arnold

### 1. Invoice and price control

Arnold explained that he spends time checking price differences between invoices and information in Exact Globe+.

The process appears to work roughly as follows:

1. The Finance department checks incoming invoices first.
2. If Finance detects a possible issue, the task can be assigned to Arnold or another responsible person.
3. Sometimes Arnold receives the task because he is the buyer responsible for the order.
4. Finance may attach a note describing the suspected problem.
5. The note does not always make the mismatch clear.
6. Arnold then investigates the invoice, order, and information in Exact Globe+ to determine what is wrong.

This can create duplicated work because Finance has already performed a check before Arnold performs another investigation.

### 2. Prices are not fixed

A simple fixed-price comparison may not be sufficient because unit prices can fluctuate between purchases and suppliers.

Therefore, an AI or rule-based solution should not automatically treat every price difference as an error. It may instead help by identifying unusual deviations and presenting the most likely mismatches to Arnold before he starts checking manually.

Potential support could include:

- highlighting invoice lines that differ from the corresponding order or ERP information;
- ranking deviations by likelihood or size of the problem;
- showing where the mismatch is located;
- giving Arnold the relevant context before he begins the investigation.

The aim would be to reduce search and checking time while keeping Arnold responsible for cases that require purchasing judgment.

## Order decisions and experience

I asked Arnold whether ordering decisions are mainly based on available data or on experience.

My understanding from the conversation is that experience currently plays a large role.

This is relevant because the project should distinguish between:

- tasks that can be supported through data, rules, or AI;
- tasks that depend on Arnold's practical purchasing knowledge and judgment.

The goal should not be to automate all purchasing decisions. It should identify which parts of Arnold's work genuinely require his expertise and which parts mainly consume time.

## Lead-time uncertainty

Another issue is that the lead time for a required spare part can sometimes be difficult to determine.

This could be explored later as a possible decision-support problem. For example, historical order information, supplier information, or previous delivery performance might help estimate expected lead times if suitable data are available.

This is currently an observation rather than a confirmed AI use case.

## Process-improvement perspective

The project should not assume that every workload problem needs an AI agent.

For each part of the purchasing process, first determine:

1. What task is being performed?
2. Why is the task necessary?
3. Who performs it now?
4. Is the same information checked by more than one person?
5. Does the task require purchasing expertise or mainly administrative checking?
6. Can the process itself be simplified or clarified?
7. If the task remains necessary, could AI or automation support it?

The invoice-control example is especially relevant because it may involve both a process problem and an AI opportunity. Finance performs an initial check, but Arnold may still need to repeat much of the investigation because the reason for the mismatch is not always clearly identified.

## Potential Arnold-focused AI opportunities

Candidate tasks to investigate include:

- repetitive invoice and price comparisons;
- identifying likely mismatches between documents and Exact Globe+;
- highlighting exceptions that require Arnold's attention;
- collecting relevant information before Arnold starts investigating a case;
- supporting routine order-control activities;
- identifying tasks that do not require Arnold's purchasing experience and could be automated or reassigned.

These are candidate areas only. They still need to be validated by observing Arnold's workflow and understanding the available data.

## Exact Globe+ and possible AI integration

Exact Globe+ is the ERP system used in the process.

If an AI agent or AI-based solution needs to retrieve or work with ERP information, it would need controlled access to Exact Globe+. One possible technical direction to investigate is using an MCP-based integration or another controlled interface between the AI solution and Exact.

This should be treated as a technical option rather than a predetermined solution. The required access, available Exact interfaces, permissions, security constraints, and data structure still need to be investigated.

## Confidentiality and deployment considerations

Because company and purchasing data may be confidential, the choice between an external API and a locally hosted model may matter.

Hermes or another locally deployable agent/model was considered as a possible direction, but no tool or architecture has been selected yet.

Later evaluation should compare options based on factors such as:

- confidentiality and data handling;
- whether data are retained by an external provider;
- whether data are used for model training;
- integration with Exact Globe+;
- required model capability;
- maintenance effort;
- reliability;
- cost.

## Working project direction

The current project direction can be summarized as:

> Understand Arnold's actual workflow, identify unnecessary or repetitive work, improve the process where possible, and use AI where it can meaningfully reduce his workload without removing tasks that require buyer expertise.

This creates two levels of analysis:

### Track A: Arnold's individual workflow

Map Arnold's daily and recurring tasks. Determine which tasks are:

- repetitive;
- administrative;
- easy but time-consuming;
- based on pattern matching or document comparison;
- dependent on experience and judgment.

### Track B: Purchasing process improvement

Map the process around Arnold. Determine where:

- work is duplicated;
- information is handed over unclearly;
- responsibilities overlap;
- unnecessary steps exist;
- AI could support a redesigned process rather than simply automate the current process.

## Next questions to investigate

- Which tasks consume the largest share of Arnold's time?
- How often does invoice and price mismatch investigation occur?
- How much time does one mismatch investigation usually take?
- What exactly does Finance check before assigning a case to Arnold?
- What information is passed from Finance to Arnold?
- Why are some mismatch notes insufficient for Arnold to resolve the issue immediately?
- Which data fields in Exact Globe+ are needed to compare an invoice with an order?
- Are invoice documents available in a consistent digital format?
- Which Arnold tasks require experience and which follow relatively stable rules?
- Which other people or departments perform checks that overlap with Arnold's work?
- What technical access to Exact Globe+ is possible and permitted?

## Security note

Physical office or production access credentials are intentionally excluded from this repository.