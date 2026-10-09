# Order and confirmation checking: design draft

**Status, 9 October 2026:** conditional design preparation for **order and confirmation checking**, the provisional leading candidate. The focal task, data readiness, accepted assistance and evaluation protocol remain open. This document does not establish a prototype or new company-system access.

**Relation to the [TO-BE working hypothesis](TO_BE_Working_Hypothesis_v0.1.md) of 2 September:** that file keeps the earlier end-to-end AUTO / REVIEW / MANUAL idea; this draft replaces it, for the focal case, with bounded checking support. In the [8 October academic meeting](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md#buyer-acceptance-and-the-business-value-example), Yijie reported that Arno and Dennis opposed automatic PO creation and sending because they would lose control and awareness of orders. This does not establish rejection or acceptance of a tool that reads documents and flags differences. Standard / review / manual remains a possible way to organize checking results, not permission for automatic ordering.

**Ownership:** this file holds the candidate design, the existing Dennis role/handoff synthesis, and a draft evaluation specification. The [methodology](../methodology/Phase_1_Current_Methodology.md) owns the gates, selection and evaluation rules. The [AS-IS master](Process_Cleaned_V1.5.md) remains the current-process reference.

## 1. Focal-task problem and boundary

The candidate addresses Arno's effort in retrieving purchasing evidence, comparing order information and investigating differences. The proposed output is a source-linked comparison for his decision. Maintaining correct purchasing information is the quality objective; shorter handling time alone is insufficient.

The [AS-IS sections 4.7 and 4.10](Process_Cleaned_V1.5.md#47-pre-po-price-control) identify two control points. The final scope may cover one or both, depending on accessible evidence and evaluation feasibility. Keep their cases, reference sources and results separate.

| Control point | Candidate inputs, subject to access | Proposed output | Buyer decision retained |
|---|---|---|---|
| Before PO release | Current PO/Exact lines plus applicable quotation, supplier price source or agreed terms | Field comparison and missing, conflicting or unclear information, with source references | Which source applies, whether a difference is acceptable, whether to amend or seek approval, and whether to send |
| After supplier confirmation | Issued PO version, corresponding supplier confirmation and applicable agreed terms where needed | Matched/unmatched lines, field differences and unresolved ambiguities, with source references | Whether the confirmation is acceptable, what to clarify or correct, and whether to complete the existing confirmation workflow |

The broadened candidate concerns prices, delivery dates, quantities and missing/extra lines. It does not establish that every field is available or that historical CHECK minutes can be divided among these fields. The [evidence matrix](../analyze/Candidate_Evidence_Matrix_2026-10-07.md) and notebooks own the measured boundary. Observed checking time is not all avoidable time.

**Outside this draft:** supplier selection/negotiation by the tool, technical substitution decisions, autonomous PO creation/sending, automatic production Exact changes, logistics and former EXC aftercare. A draft supplier message or proposed master-data update is a possible later extension only if accepted and necessary. Neither is part of the minimum checking output.

## 2. Dennis's existing role and relevant handoffs

This synthesis uses the qualitative [15 September notes](../meetings/Internship_notes_2026-09-15.md), timed [25 September session](../measurement/Measure_Observation_2026-09-25.md) and dated [2 October reported explanations](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october). It summarises the existing evidence; the targeted gaps are listed below. Dennis said that he handles more complex/project work and Arno more Service requests, with no strict rule separating their requests.

| Dennis's evidenced work | Recorded action/outcome | Connection to Arno or the candidate | Evidence limit or open point |
|---|---|---|---|
| Develop technical requirements and identify suppliers | Research project needs, list required items and search suppliers; technical questions usually reach Dennis | Technical identity or substitution questions may need Dennis rather than a guessed line match | [15 September role explanation](../meetings/Internship_notes_2026-09-15.md#denniss-explanation-of-the-purchasing-roles). Supports a proposed escalation route, not a confirmed service agreement or measured handoff frequency |
| Prepare supplier price arrangements | Drager active-article data exported to Excel for a fixed-price agreement; an expired discount was discussed | Agreed terms and validity may supply the reference for judging a price difference | [15 September section 5](../meetings/Internship_notes_2026-09-15.md#5-drager-bv-pricing-supplier-contact-and-order-information). Preparation does not prove a concluded agreement or accessible reference dataset |
| Maintain articles and suppliers | Article creation and inactive-item questions; Yijie reported that both buyers create articles and Dennis creates most suppliers | Missing identities, inactive items or stale data can block comparison and require an owner to resolve them | [15 September sections 2, 8 and 9](../meetings/Internship_notes_2026-09-15.md#2-creating-an-article-consisting-of-three-components); [2 October account](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october). Not all article upkeep belongs to Dennis |
| Check/update a price while resolving supply | OBS-13 combines item activation, price checking/updating and a call to an alternative supplier, which had no stock | A price/data issue can need supplier knowledge and availability checks beyond numeric comparison | [25 September OBS-13](../measurement/Measure_Observation_2026-09-25.md#afternoon-case-notes). The four-minute combined interval is not isolated price-check time |
| Check offer validity | Dennis asked Gimi whether an earlier offer remained valid and how purchasing would work | A readable historical price may no longer apply | [25 September OBS-12](../measurement/Measure_Observation_2026-09-25.md#afternoon-case-notes). Enquiry recorded; no agreement, award or completed purchase established |
| Resolve order information with colleagues | Arno asked Dennis about the hybrid chamber delay; Dennis left an unresolved MWC quantity to Johan, who had more current information | A checking tool should preserve an unresolved status and identify the missing information | [25 September OBS-03](../measurement/Measure_Observation_2026-09-25.md#morning-case-notes) and [OBS-14 / MWC](../measurement/Measure_Observation_2026-09-25.md#afternoon-case-notes). Neither quantity resolution nor dispatch is established |
| Maintain information used downstream | Dennis reported Sales selling items at a loss because sales prices used outdated purchase prices; Yijie later reported lack of time for updates | Qualitative business relevance exists beyond Arno's time; benefits depend on the later update process | [15 September pricing explanation](../meetings/Internship_notes_2026-09-15.md#prices-and-updates) and [2 October account](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#what-yijie-reported-on-2-october). Financial impact and achievable benefit remain unquantified; no separate Johan reconfirmation is needed for this qualitative point |

The [25 September coverage note](../measurement/Measure_Observation_2026-09-25.md#measurement-quality-and-coverage-notes) records 162 interval minutes but leaves net observation exposure unconfirmed. Keep Dennis separate from Arno's workload totals and avoid per-hour comparisons. Returns, ring repair and other aftercare illustrate his wider role but remain outside improvement scope.

**Targeted Dennis input, only where consequential:** who establishes applicable prices/terms; who resolves uncertain item identity or validity; and who would perform added review or master-data follow-up. His reported role change and unconfirmed return in the [8 October notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md#buyer-availability-and-immediate-priorities) leave current responsibility and availability open. Another general observation round is not implied.

## 3. Draft functional requirements

These proposed acceptance conditions are a first draft of the requirements. They need review after the focal boundary is agreed and do not report implemented functionality.

| ID | Proposed requirement | Demonstration needed |
|---|---|---|
| F1 | Identify the control point, PO version and supplier document | Buyer can inspect source references; absent/ambiguous links prevent a complete comparison |
| F2 | Extract agreed fields while retaining original values and page/line/text evidence | Every displayed value is traceable and correctable; missing/unreadable information stays explicit |
| F3 | Match lines without forcing uncertain or duplicate matches | Missing, extra, split, duplicate or ambiguous lines remain visible for buyer resolution |
| F4 | Apply explicit comparison rules | Differences are reproducible; unknown units, currency, price basis or terms block unsupported numeric conclusions |
| F5 | Display matched results, differences and incomplete coverage together | “No detected difference” is distinct from “could not compare”; checked fields and lines are visible |
| F6 | Record buyer review and disposition | Acceptance, correction, clarification or unresolved outcome is recorded with evidence. The tool does not approve a purchase |
| F7 | Preserve the buyer-controlled handoff | Buyer performs approved Exact updates, authorization requests and supplier communication through the existing process. The minimum prototype supplies comparison output only |

## 4. Proposed checking workflow

A permitted file export may be sufficient; production integration is not a prerequisite. “Test data” does not imply a verified Azure service, Exact API or document-processing route.

```mermaid
flowchart TD
    po["Permitted Exact PO data"] --> link["Identify case and document versions"]
    supplier["Quotation or supplier confirmation"] --> link
    link --> extract["Extract fields with source evidence"]
    extract --> comparable{"Lines and fields comparable?"}
    comparable -- "yes" --> rules["Apply explicit comparison rules"]
    comparable -- "no or uncertain" --> unresolved["Show unresolved information"]
    rules --> review["Arno reviews results and sources"]
    unresolved --> review
    review --> decision{"Buyer can decide?"}
    decision -- "no" --> clarify["Clarify with relevant source owner"]
    clarify --> review
    decision -- "yes" --> record["Record decision and required follow-up"]
    record --> handoff["Buyer uses existing Exact and communication workflow"]
```

A standard result means no difference was detected in fields successfully checked. It does not authorize release, amendment or automatic confirmation. Manual handling remains available when documents, identities or reference terms cannot be established.

## 5. Draft AI-versus-rules decision

| Component | Proposed mechanism | Reason and condition |
|---|---|---|
| Read structured Exact/export fields | Direct structured import | Preserve known identifiers and values; AI adds no justified value to copying them |
| Interpret varying supplier layouts or descriptions | Compare AI/document extraction with a simpler parser/template approach | Actual documents must establish the variability and whether a simpler method suffices |
| Match differently described/identified lines | Exact identifiers/rules first; AI suggestions for remaining ambiguity | Suggestions need source evidence and buyer verification. Confidence scores are not calibrated probabilities unless tested |
| Compare numbers and explicit dates | Deterministic rules and documented normalization | Arithmetic, units, currency, discounts and date semantics should be reproducible |
| Decide whether a discrepancy is acceptable | Arno, involving the relevant source owner where needed | A difference from Exact does not identify the correct price, intended item or accepted action |
| Update systems or communicate | Existing buyer-controlled workflow | Autonomous execution is unnecessary for testing the checking aid |

This is an architecture hypothesis, not evidence that AI is necessary or effective. The [methodology's Stage A gates](../methodology/Phase_1_Current_Methodology.md#53-formal-two-stage-selection-rule) still require a meaningful AI contribution. No model, vendor, interface, hosting environment or deployment route is selected.

## 6. Draft logical field map

These are proposed research fields, not confirmed Exact database/API names. Preserve raw values alongside normalized comparison values. Establish availability through the [Stage A worksheet](../analyze/Stage_A_Test_Account_Check_2026-10-07.xlsx), starting with the relevant PC checks.

| Field group | Proposed fields, if available | Needed rule or open issue |
|---|---|---|
| Case/source identity | Case ID; control point; supplier ID; PO number/version; source reference/type/date/location | Correct order/revision linking and permitted storage remain unverified |
| Line identity | PO/supplier line IDs; buyer/supplier article IDs; raw description; proposed match status | Preserve unmatched/many-to-one cases; substitutions need human judgement |
| Quantity | Raw quantity; unit; documented pack size/conversion | Do not assume “each” equals “pack”. Required equality/conversion rules need validation |
| Price | Raw unit/line price; currency; basis; discount; relevant charge/tax inclusion | No numeric tolerance or currency conversion is approved; different terms can prevent comparison |
| Delivery | Raw date/lead-time phrase; parsed value if unambiguous; requested/promised date type | Clarify date meaning, partial deliveries and missing reference dates |
| Reference terms | Applicable quotation/agreement/version; validity; reference owner; approval status | Stored Exact price is not automatically correct; a supplier document does not establish an accepted business action |
| Evidence/review | Page/line/text; extraction/match status; rule result; correction; final disposition/unresolved reason | Confirm retention/access and the review record needed for traceability |

## 7. Draft non-functional requirements and controls

| Area | Proposed control | Input needed before use |
|---|---|---|
| Permission | Preserve the recorded permission for test-account data and an external AI service (confirmed 7 October) | Verify which usable examples and export route implement that permitted use. New interfaces or production actions are not established by the record |
| Integrity | Unchanged sources; versioned derived data, rules and outputs | Approved storage, access and identifiers |
| Review/failure | Visible missing data, failed extraction and uncertain matches; correction and manual fallback | Arno's accepted display and cases needing full manual handling |
| Auditability | Sources, tool/rule version, edits and final human disposition | Required records, retention and how restricted evidence can be referenced in the thesis |
| Reliability/performance | Record failures, processing delay and correction effort | Feasible response time and failure criteria; no invented service target |
| Authorization | Purchasing decisions and system actions stay in the existing workflow | Trace the chosen case's approval path. The reported €10,000 rule is context, not permission to automate approval |

## 8. Draft evaluation protocol to complete after selection

This prepares the evaluation protocol under [methodology section 6.1](../methodology/Phase_1_Current_Methodology.md#61-workload-endpoint-and-quality-guardrail). It is not a frozen protocol or completed baseline. Resolve these choices before substantive development and formal testing.

| Element | Candidate-specific draft | What remains open |
|---|---|---|
| Comparison | Manual versus assisted checking by Arno with the same required final outcome | Select pre-release, post-confirmation or separately reported strata; define complete-case start/end |
| Cases | Linked historical PO/source documents with reference answers; normal, discrepancy and ambiguous examples | Accessible pool, formats, line counts and coverage; record exclusions without claiming population representativeness |
| Reference answer | Separate document content, correct line matches/differences and accepted business disposition | Named reviewer/adjudicator, applicable terms and disagreement resolution; stored price/prior action alone is insufficient |
| Candidate workload endpoint | Active human handling time per eligible case, if justified; line count/complexity as context | Confirm workload dimension. Include retrieval, setup, review, correction, rework and required handoff; separate passive waits/unrelated interruptions |
| Other affected work | Dennis/other employee reference preparation, clarification and review reported separately | Participants and changed responsibilities; lower Arno time cannot conceal transferred work |
| Quality | Final human-approved outcomes against reference; extraction/matching errors, misses and false flags as diagnostics | Critical/minor definitions and denominators. Wrong item/quantity acceptance or unjustified price correction are discussion examples, not approved classifications |
| Allocation/procedure | Separate development from held-out evaluation where feasible; account for case mix/order and memory | Number of cases, allocation and participant availability. If cases repeat, specify controls and report residual learning bias |
| Analysis | Compare case outcomes, show individual differences/uncertainty and failures | Analysis appropriate to the final design; no post-result choice of success rule |
| Success rule | Joint workload improvement and quality guardrail from the methodology | Process-owner thresholds Δ and δ and academic review; no values or approval supplied here |
| Interpretation | Historical-case results describe tested conditions | The exploratory 0.87 min/line is not a formal baseline; time alone does not establish mental-workload reduction or production savings |

**Proposed log:** case ID, control point, condition/order, document versions, line count, task start/end, active handling components, passive wait, unrelated interruption, corrections, unresolved items, final quality judgement, and Dennis/other-person contribution. Test its practicality in a small procedural pilot before freezing the formal run. Zero observed critical errors would not establish a general zero-error guarantee.

## 9. Inputs needed to agree the design

1. Complete candidate-specific data/reference checks in the Stage A worksheet: readable linked examples and whether a defensible reference can be created.
2. Use the [focused Arno guide](../measurement/Arno_Follow_Up_Session_Guide_2026-10-02.md#priority-case-walkthrough-added-9-october) to resolve accepted controls and support; carry forward the reported objection to automatic creation/sending.
3. Resolve only consequential Dennis/source-owner gaps from section 2. Existing evidence supports qualitative business relevance; quantify impact if making a financial claim.
4. Agree the focal boundary, relevant criteria and weights with Zhongxin through the selection workflow. A high provisional score cannot override failed gates.
5. Freeze selected requirements and evaluation choices, including reference ownership, cases and thresholds, before development/formal testing. The requirements and the evaluation outline remain drafts until these inputs are settled.
