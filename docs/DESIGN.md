# Order and confirmation checking: conditional design

Consolidated from the **9 October 2026 draft** and the dated [AI-function comparison](../evidence/decisions/AI_Function_Comparison_2026-10-02.md). These are provisional requirements, not an implemented prototype, approved focal task or frozen evaluation protocol. The [selection notebook](../Focal_Case_Selection_2026-10-07.ipynb) owns candidate boundaries and decisions; [Methods](METHODS.md) owns gates and evaluation rules; [Process](PROCESS.md) describes existing practice.

In the [8 October meeting](../evidence/meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md#buyer-acceptance-and-the-business-value-example), **Yijie reported** Arno and Dennis's opposition to combined automatic PO creation/sending because of lost control, interest and order awareness. The 1 October concern was not individually attributed. Neither report establishes direct acceptance or rejection of bounded reading, matching, flagging or recommendations. The [Arno guide](../evidence/working/Arno_Follow_Up_Session_Guide_2026-10-02.md#priority-case-walkthrough-added-9-october) remains the acceptance instrument. Record direct answers per person, task/function, level, status, conditions, date and evidence; statuses are accepted, accepted with conditions, rejected, or not yet assessed.

## Boundary and human decisions

The proposed aid produces a source-linked comparison for Arno, addressing retrieval, comparison and discrepancy investigation. Correct purchasing outcomes matter alongside workload. Before-release and after-confirmation cases have different sources and completion conditions; select one or retain separately evaluated strata.

| Control point | Candidate inputs | Buyer retains |
|---|---|---|
| Before release | Current PO/Exact lines, applicable quotation, supplier price source or agreed terms | Source applicability; acceptable differences; amendment, approval and sending decisions |
| After confirmation | Issued PO version, corresponding confirmation and applicable terms | Confirmation acceptance; clarification/correction; completion of the existing confirmation workflow |

Candidate fields include price, delivery date, quantity and missing/extra lines. Availability is unverified; historical CHECK minutes cannot be retrospectively divided among those fields or treated as entirely avoidable. AI-table rows **5–7** retain the relevant evidence limits: generic checks do not identify every field, attachment is not checking, the monitoring check in 18 September OBS-01 began before observation, and OBS-29 does not establish when the price difference was discovered. Separately EXC-coded work stays outside improvement.

Excluded functions are supplier selection/negotiation, technical substitution decisions, autonomous PO creation/sending, production Exact changes, logistics and former EXC aftercare. Editable supplier messages or proposed master-data updates are later extensions only if necessary and accepted. The earlier [TO-BE hypothesis](https://github.com/Luuuuuig/Bachelor-End-Project/blob/212ac1cb877072dd65af6e6bca81c62441f5552c/docs/process/TO_BE_Working_Hypothesis_v0.1.md) remains historical: standard/review/manual can organize checking results, but cannot authorize ordering. “No detected difference” means only that successfully checked fields matched; incomplete coverage remains visible.

## Dennis and reference ownership

The [15 September notes](../evidence/meetings/Internship_notes_2026-09-15.md), [25 September session](../evidence/observations/Measure_Observation_2026-09-25.md) and [2 October attributed explanations](../evidence/working/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october) establish relevant context. Dennis described more complex/project work and Arno more Service requests, without a strict division.

| Existing evidence | Design implication and limit |
|---|---|
| Technical questions usually reach Dennis; he researches project needs, lists items and searches suppliers | Uncertain identity/substitution may need his expertise. No service agreement or handoff frequency is established |
| Drager active-article data exported for a fixed-price agreement; expired discount discussed | Reference terms need version, validity and an owner. Preparation does not prove a concluded agreement or accessible dataset |
| Article creation/inactive-item work; both buyers create articles, Dennis reportedly creates most suppliers | Missing identities/stale data need resolution; article upkeep is not exclusively Dennis's responsibility |
| 25 September OBS-13 combines activation, price checking/updating and an alternative-supplier call; supplier had no stock | Availability and supplier knowledge can matter beyond arithmetic. The four-minute interval cannot be isolated as price-check time |
| OBS-12 asks Gimi about earlier-offer validity and purchasing procedure | A historical readable price may be invalid; no agreement, award or purchase is established |
| Arno asks about hybrid-chamber delay in OBS-03; OBS-14 leaves MWC quantity to Johan | Keep unresolved states and source-owner referrals. The record proves neither quantity resolution nor dispatch |
| Dennis reports stale purchase prices feeding sales prices and loss-making sales; later lack-of-time explanation | Qualitative business relevance exists. Financial impact, achievable benefit and Johan's confirmation remain open; savings depend on later updates |

Dennis's net observation exposure is unconfirmed: keep his evidence separate from Arno's totals and avoid per-hour comparisons. Returns and ring repair describe wider work outside improvement. His return and reported role change were unconfirmed on 8 October. Consequential gaps concern who establishes terms, resolves identity/validity, or performs added review/master-data work; this does not imply another broad observation round.

## Requirements and comparison workflow

| ID | Proposed requirement and demonstration |
|---|---|
| F1 | Identify control point, PO version and supplier document; inspectable references, with ambiguous/missing links blocking complete comparison |
| F2 | Extract agreed fields with original values and page/line/text evidence; traceable, correctable values and explicit unreadable/missing information |
| F3 | Avoid forced line matches; expose missing, extra, split, duplicate and ambiguous lines |
| F4 | Use reproducible comparison rules; unknown units, currency, price basis or terms block unsupported conclusions |
| F5 | Show matched results, differences and incomplete coverage together; distinguish no detected difference from inability to compare |
| F6 | Record human acceptance, correction, clarification or unresolved disposition with evidence; never approve a purchase |
| F7 | Preserve buyer-controlled Exact updates, approval requests and communication; minimum prototype supplies comparison output only |

A permitted file export may suffice. Link case/document versions, extract evidence, assess comparability, apply rules where possible, display unresolved information, obtain Arno's review and clarify with the relevant owner as needed. Record disposition and required follow-up before the buyer continues through the existing workflow. Manual handling remains available. Test-account permission does not establish an Exact API, Azure service or document-processing route.

## AI, rules and literature rationale

Following the provisional Parasuraman, Sheridan and Wickens (2000) source notes, distinguish **retrieve** (acquisition), **analyse** (analysis), **recommend** (decision/action selection), and **execute** (implementation). Acceptance is function-specific. Communication is a task area: drafting and autonomous sending are separate functions, preserved as AI-table rows **10** and **11**.

| Component | Proposed mechanism and rationale |
|---|---|
| Structured Exact/export fields | Direct import preserves known identifiers and values without AI copying |
| Variable document layouts/descriptions | Compare AI/document extraction with simpler parsers/templates; actual examples must justify complexity |
| Line matching | Exact identifiers/rules first; AI suggestions for remaining ambiguity, with source evidence and human verification |
| Numbers and explicit dates | Deterministic normalization and comparison for reproducible arithmetic and semantics |
| Acceptable discrepancy/action | Arno plus relevant source owner; a difference from Exact does not identify the correct price or action |
| System updates/communication | Existing buyer workflow; autonomous execution is unnecessary for the checking evaluation |

Tater et al. (2022), cited in rows 5–7, offers invoice-to-PO matching with human review in accounts payable, requiring adaptation here; flagging does not explain causes. Šimsa et al. (2023, DocILE), rows 3–4 and 6, supports field/line extraction research, not intended meaning or a locally tested tool. Confidence scores are not calibrated probabilities unless tested.

The frozen comparison preserves alternative evidence without creating another investigation list: Lombardi et al. (2025), row 1, concerns building-drawing title blocks, not revision/completeness assurance; row 2 lacks directly applicable completeness support. Row 8 lacks procurement-specific MAX support. Burger et al. (2023), row 9, cautions that human-AI procurement collaboration need not improve performance. Noy and Zhang (2023), row 10, concerns experimental professional writing, not procurement; Amershi et al. (2019) motivates visible limitations and easy correction. These remain provisional source notes, **not completed full-text reading**; the [literature register](../literature/README.md) owns verification status. Observed tasks establish neither feasibility nor acceptance. A meaningful AI contribution still needs Stage A support; no model, vendor, interface or deployment route is chosen.

## Logical fields and controls

These are research fields, not verified Exact/API names. Retain raw values alongside normalized values.

| Group | Fields and unresolved rules |
|---|---|
| Case/source | Case ID, control point, supplier ID, PO number/version, source type/date/location/reference; verify linking and permitted storage |
| Line | PO/supplier line IDs, buyer/supplier article IDs, raw description, match status; preserve unmatched/many-to-one cases and human substitution decisions |
| Quantity | Raw quantity, unit, documented pack size/conversion; “each” cannot silently equal “pack” |
| Price | Raw unit/line price, currency, basis, discount, charge/tax inclusion; no approved tolerance or currency conversion |
| Delivery | Raw date/lead-time phrase, unambiguous parsed value, requested/promised type; clarify partial deliveries and missing reference dates |
| Terms | Applicable quotation/agreement/version, validity, reference owner, approval status; Exact is not automatically correct |
| Review | Page/line/text evidence, extraction/match status, rule result, correction and final disposition/unresolved reason; agree retention/access |

Recorded 7 October permission covers test-account data and an external AI service; usable examples and export route still require verification. Preserve source integrity and version derived data, rules, outputs and tools. Log human edits/disposition, failures, delay and correction effort; agree storage, restricted thesis references, retention, response-time and failure criteria rather than inventing targets. Missing data and failed extraction require visible fallback. Existing authorization applies; the reported €10,000 threshold is no permission to automate approval.

## Candidate-specific evaluation draft

The [Stage A workbook](../evidence/working/Stage_A_Test_Account_Check_2026-10-07.xlsx) must establish readable linked examples and reference feasibility. Before substantive development/formal testing, agree the focal boundary, accepted assistance, source/review ownership, usable cases and evaluation choices through the selection workflow. Criteria/weights remain subject to Zhongxin's review; scores cannot override failed gates. [README](../README.md) owns the action list.

| Element | Proposed specification and open choice |
|---|---|
| Comparison/cases | Arno checks manually and with assistance to the same final outcome. Define complete-case start/end and control-point strata; include normal, discrepancy and ambiguous linked cases, formats/line counts and documented exclusions without claiming representativeness |
| Reference | Separately establish document content, correct matches/differences and accepted business disposition; name reviewer/adjudicator, applicable terms and disagreement procedure. Stored price or prior action alone is insufficient |
| Workload | If justified, active human handling time per eligible case, including retrieval, setup, review, correction, rework and handoff. Separate passive waits/unrelated interruptions; record line count/complexity. Count Dennis/others' preparation, clarification and review separately to expose transferred work |
| Quality | Judge final human-approved outcomes against the reference; extraction/matching errors, misses and false flags are diagnostics. Agree critical/minor definitions and denominators. Wrong item/quantity acceptance and unjustified price correction are discussion examples, not approved classes |
| Procedure/analysis | Agree case count, allocation and availability; separate development and held-out evaluation where feasible. Address case mix, order, memory and repeated-case learning; show individual differences, uncertainty and failures |
| Success/interpretation | Apply Methods' joint workload improvement and quality guardrail, with process-owner Δ/δ and academic review agreed before results. Historical cases establish tested conditions; exploratory CHECK rates are not a formal baseline. Time alone proves neither mental-workload reduction nor production savings |

The proposed log records case/control point, condition/order, document versions, line count, start/end and handling components, passive wait, interruptions, corrections, unresolved items, final quality judgement and other-person contribution. Pilot the procedure before freezing it. Zero observed critical errors cannot establish a general zero-error guarantee.
