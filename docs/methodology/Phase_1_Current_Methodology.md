# Phase 1 — Current Methodology and Case-Selection Status

**Status:** Current research-method and case-selection source of truth, synchronized 15 September 2026.

**Ownership:** This file owns the research framework, candidate portfolio, selection gates, evaluation logic and current research actions. Detailed workload theory and live Measure-phase collection rules are maintained in their dedicated files rather than duplicated here.

Related sources:

- Project control / DMAIC tollgates: `docs/Project_Charter.md`
- AS-IS process and open process facts: `docs/process/Process_Cleaned_V1.5.md`
- Canonical workload definition: `docs/methodology/Workload_Definition.md`
- Exploratory Measure protocol: `docs/measurement/Measurement_Protocol_v1.3.md`
- Measurement-method justification: `docs/measurement/Measurement_Method_Justification.md`
- Formal company evidence: `docs/company-documentation/Official_Document_Register_2026-08-21.md`
- Working TO-BE hypothesis: `docs/process/TO_BE_Working_Hypothesis_v0.1.md`

---

### Scope update of 14 September 2026

The objective remains reducing the operational buyer's workload while maintaining purchasing quality. The [10 September academic decision](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md) adds Dennis's tactical purchasing work to the research context and excludes logistics and EXC time from the thesis Measure analysis and focal-case selection. Keep actor-specific evidence separate. Apply the [scope and classification addendum](../measurement/Scope_and_Classification_Addendum_2026-09-14.md) and the [Van Weele crosswalk](../process/Van_Weele_Activity_Mapping_2026-09-14.md). The Plan of Work and readable assignment retain the four original sub-questions in their original order, with wording that includes relevant tactical purchasing tasks. Measurement and evaluation details remain subject to justification.

# 1. Project objective

The company-level objective is to reduce meaningful workload in operational purchasing by reducing unnecessary administrative effort, repetitive verification, avoidable rework and information-handling burden while preserving or supporting work that depends on purchasing expertise.

The thesis-level objective is to select one high-value purchasing activity or coherent TO-BE process component and design and evaluate a focal artifact containing a **meaningful AI-supported contribution**.

The company expects AI to be part of the focal thesis solution. Conventional process redesign, deterministic rules and digital automation may be supporting components or separate quick-win recommendations. A non-AI focal artifact is an exception: it requires documented Analyze evidence that no candidate passes the responsible-AI, data, quality and evaluation-feasibility gates, followed by explicit company and academic-supervisor approval. The project must not relabel a deterministic rule as AI merely to satisfy the expectation.

Selecting one thesis case does not remove other improvement opportunities from the wider company improvement portfolio.

---

# 2. Research structure

## DMAIC — process-improvement framework

DMAIC structures improvement of the existing purchasing process:

- **Define:** scope, stakeholders, AS-IS process, workload problem and initial opportunity areas.
- **Measure:** establish a defensible multidimensional workload baseline across the operational process.
- **Analyze:** identify root causes, standardizability, constraints and which work should be eliminated, simplified, standardized, automated or supported; then test technical/data feasibility for the shortlisted candidates.
- **Improve:** design evidence-based TO-BE alternatives and develop the selected artifact.
- **Control:** define KPIs, ownership, exception controls and implementation safeguards.

DMAIC fits because the project improves an **existing** process rather than designing a completely new process from scratch.

## DSRM — artifact design and evaluation

If a digital/AI artifact is developed, its design and evaluation follow DSRM:

`problem identification → objectives → design/development → demonstration → evaluation → communication`

DSRM mainly supports DMAIC's Improve stage, while some problem/objective work naturally begins earlier as the focal case is defined.

## Visual relationship

```mermaid
flowchart LR
    D["DEFINE\nAS-IS + scope + opportunities"]
    M["MEASURE\nmultidimensional workload baseline"]
    A["ANALYZE\nroot causes + shortlist + technical feasibility"]
    I["IMPROVE\nTO-BE design + artifact"]
    C["CONTROL\nKPIs + exception controls"]

    D --> M --> A --> I --> C

    DSRM["DSRM\ndesign / develop / demonstrate / evaluate artifact"]
    DSRM -. "primarily inside Improve" .-> I
```

Within this structure:

- `Process_Cleaned_V1.5.md` mainly supports **Define** and the transition into Measure;
- Section 4 below is the authoritative candidate-status portfolio to be tested by Measure/Analyze;
- `../measurement/Measurement_Protocol_v1.3.md` operationalizes the exploratory **Measure** phase;
- `TO_BE_Working_Hypothesis_v0.1.md` is an early **Improve hypothesis**, not yet an Improve conclusion;
- the final digital/AI artifact is selected only after the relevant Measure and Analyze gates are satisfied.

---

## CTA-informed elicitation

Cognitive Task Analysis-informed questioning is used where buyer expertise is tacit, especially the standard maximalisatie check and downstream order/hold logic, suspicious-information recognition, exceptions and override reasoning.

For the maximalisatie/order-hold sequence, elicitation should capture:

- how the buyer searches for additional same-supplier demand;
- what makes consolidation useful enough to proceed;
- after MAX, whether or not demand was added, what makes the resulting order proceed versus be held (including size, urgency, MOQ/minimum-value considerations and current purchasing context);
- what later causes a held requirement to be reconsidered;
- which cues are explicit in data versus experience-based or undocumented.

This is **CTA-informed elicitation**, not automatically a full standalone CTA study.

## Human-AI reliance

Judge-Advisor System / reliance concepts remain conditional. They become relevant only if the final artifact gives advice that a buyer can accept, modify or reject. They are not automatically required for pure administrative automation or discrepancy detection.

---

# 3. Measure design

The four sub-questions retain their original order. SQ1 concerns the workload profile and process factors that inform it; SQ2 concerns implementation conditions and controls; SQ3 concerns candidate comparison and selection; SQ4 concerns evaluation of workload and quality. Root-cause analysis informs SQ1 and SQ3 and does not introduce a fifth question.

The broad workload construct is defined in `Workload_Definition.md` and uses a layered structure:

- **overall/occupational workload:** amount and difficulty of work, grounded primarily in Bowling & Kirkendall (2012);
- **quantitative workload / organizational constraints:** conceptually supported by Spector & Jex (1998);
- **mental workload:** not assessed in the current study; judgement and expertise notes remain qualitative task evidence;
- **expertise dependence:** kept analytically separate from mental workload.

The project therefore does **not** use processing time as a proxy for total or mental workload, and it does not create an unvalidated composite equation combining heterogeneous indicators.

Detailed live timing rules remain in `../measurement/Measurement_Protocol_v1.3.md`. The [14 September scope addendum](../measurement/Scope_and_Classification_Addendum_2026-09-14.md) applies the logistics and EXC exclusion and governs post-session classification. The [21 September purchasing activity framework](../process/Purchasing_Activity_Framework_2026-09-21.md) now defines concrete analytical activities within Van Weele stages, linked to the unchanged task register. The seven live families remain; full activity labels, separate task/stage/activity confidence and assignment reasons are added after observation. Combined and unresolved work remains explicit, preserving earlier measurements without invented timing splits. The exploratory Measure phase records a multidimensional activity-family profile, with post-session detailed Task-ID enrichment where evidence supports it, using where relevant:

- frequency;
- active processing time;
- case/line volume;
- rework occurrence and time;
- interruptions and task switching;
- qualitative difficulty / uncertainty / exception evidence;
- expertise dependence.

The method source and the construct source are deliberately separated. The workload literature defines what the project means by workload; a researcher-developed structured continuous-observation time-and-motion protocol, informed by STAMP and WOMBAT principles and adapted through the local AS-IS process and pilot, records the observable objective component. The exact source-to-field mapping and claim limits are documented in `../measurement/Measurement_Method_Justification.md`.

For comparable recurring execution tasks:

`operational time burden = frequency × representative active processing time`

is a buyer-capacity indicator, not a total workload or mental-workload score.

For fast judgement-heavy activities, occurrence, outcome, cues and reasoning are more informative than artificial second-level timing.

**Role of the exploratory Measurement Protocol.** Measurement Protocol v1.3 characterizes the current procurement process and screens for recurring sources of observable operational effort. It records occurrence, reliable active processing time, case context, interruptions, clarification, exception work and supported decision/expertise cues at activity-family level. These observations justify candidate generation and focal-case selection, but they do not estimate the effect of an AI artifact and do not measure purchasing outcome quality. The protocol therefore contributes indirect baseline evidence to the main research question rather than answering it independently.

**Transition to focal evaluation.** After Analyze selects one focal activity, a separate activity-specific protocol will define eligible cases, the manual comparator, justified workload indicators for the selected component, the final purchasing-quality rubric, critical-error definitions, workload-improvement threshold, acceptable quality margin, sampling design and analysis plan. These elements are frozen before artifact development and formal testing. The main research question is answered from the matched comparison of the manual and AI-assisted workflows; the broad Measure dataset supplies process context and the justification for focal-case selection.

### Current Measure sequencing

1. The 28 August pilot identified that direct live coding against the 31-task register was too granular for reliable one-observer use.
2. Four official Arno sessions are recorded through 18 September, in addition to the 28 August pilot. The 21 September activity classification covers all five records; the pilot remains separate and the 8 September OBS-16 contamination exclusion remains. Historical summaries below cover only two sessions: 31 August (165 net observed minutes; 103 timed coded-active minutes after source verification of the untimed OBS-04 SEND and OBS-05 EXC tallies) and 1 September (186 net observed minutes; 162 timed coded-active minutes). Their historical totals are **351 net observed minutes** and **265 timed coded-active minutes** under the earlier broader scope. These are different quantities and are not updated four-session or EXC-filtered totals. Current included profiles and their unresolved coverage are reported in each observation file and the consolidated activity dataset.
3. `../measurement/Measurement_Protocol_v1.3.md` is controlled for observations from 2 September onward. Its live fields/timing rules remain comparable with v1.2, while its MAX interpretation, five-day coverage rule and repository governance are updated.
4. Use five Arno observation days as the initial review point, then assess coverage, stability and saturation under the 3 September guidance. Collect targeted Dennis evidence; 10 September explicitly permits a different quantity when interpretable patterns can be established. Five working days is not automatically interpreted as 40 net observed hours.
5. Supplement live observation with approved aggregated/system PO-volume information where Johan/company can provide it; dashboard access is not required to start.
6. Move into Analyze only after the Measure coverage rule and evidence gate are satisfied.

**Exact/Orbis production-data/interface feasibility is intentionally not an immediate Measure-phase task.** It is deferred until after the exploratory workload baseline, when the shortlisted candidate(s) justify targeted technical investigation. This avoids delaying Measure with system-integration work before the workload evidence shows where that effort is most valuable.

---

# 4. Current candidate portfolio

Candidate names are used instead of reusable letter IDs so that a candidate cannot mean different things in different documents. The AS-IS process file may retain local profile labels for navigation, but this methodology file is authoritative for current thesis-candidate status.

## 4.1 Active primary-case candidates

| Candidate | Current reason | Main evidence gates | Possible artifact direction |
|---|---|---|---|
| **Order timing / maximalisatie / supplier-order consolidation** | Repeated judgement-intensive activity involving stock, future demand, open POs, lead time, urgency and maximalisatie. Useful same-supplier demand can be combined; after MAX, the resulting order is assessed and may be held or ordered whether or not demand was added. | Measure-phase workload contribution and frequency; CTA decision rules; after Measure: Exact/Orbis data feasibility and defensible benchmark | decision / information / optimization support |
| **Purchase-price control** | Repeated manual verification with measurable discrepancy outcomes, both pre-PO and post-confirmation | Measure-phase frequency, line complexity, active time, deviation rate and verification demand; after Measure: supplier/Exact data feasibility | automated retrieval/comparison, stale-price/deviation support |
| **Standard / review / manual process redesign** | Promising process-level hypothesis if a meaningful share of cases is repeatable and safely classifiable | standard-case share, addressable workload, exception boundary, quality/safety risk; after Measure: system/data feasibility and evaluation feasibility | exception-based workflow with rules/automation/AI where justified |

The detailed AUTO / REVIEW / MANUAL future-state hypothesis is maintained in `TO_BE_Working_Hypothesis_v0.1.md` and remains provisional.

## 4.2 Active but evidence-insufficient candidates

| Candidate | Current position | Main evidence needed |
|---|---|---|
| **Request intake & validation** | Real information-quality/tacit-knowledge burden observed | frequency, investigation time, error types, business impact |
| **Finance-returned EXC aftercare** | Excluded from the thesis candidate set by the 10 September EXC scope decision | Historical evidence retained; excluded time cannot determine the focal case |

## 4.3 Supporting improvement opportunities, not current primary thesis candidates

| Topic | Current position |
|---|---|
| **Exact Advies / Toewijzen** | Important system/process-control topic; `Toewijzen` is primarily an assignment/control action rather than a stand-alone optimization problem |
| **PO supplier communication** | Clear repetitive quick win / semi-automation opportunity; likely too narrow as the primary thesis case unless volume shows substantial total burden |

## 4.4 Ruled out / deprioritized

### Logistics and EXC

Logistics and EXC aftercare are excluded from thesis measurement analysis and focal-case selection. Retain historical raw evidence; apply the documented filter.

### Supplier selection in the expanded purchasing context

Earlier evidence indicated that suppliers are normally predetermined for Arno. Dennis's inclusion means supplier-selection tasks can now be investigated as purchasing context. This does not establish a recurring operational-buyer workload problem or a selected supplier-selection artifact. Any candidate must demonstrate a connection to the primary workload objective and pass the same evidence and feasibility gates.

---

# 5. Decision gates before final case selection

## 5.1 Measure-phase evidence gates

1. **Workload baseline:** which activities contribute meaningful quantitative and/or qualitative workload rather than merely appearing interesting in isolated observations?
2. **Frequency / case mix:** how often do relevant tasks and case types occur across the observed working periods?
3. **Active processing time / volume:** for timed activities, what are the representative active-time distributions and how do they relate to line/case volume?
4. **Rework and organizational constraints:** where do repeated work, interruptions, missing information or hand-off problems materially affect the buyer?
5. **Expertise dependence:** which activities rely on tacit cues or experience that cannot yet be reproduced from explicit process rules/data?
6. **Standard-case boundary:** what share of the observed work appears routine/standard versus review/manual/exceptional, without yet assuming automation feasibility?

## 5.2 Analyze-phase feasibility gates — after Measure

7. **Exact/Orbis data availability:** for the shortlisted candidate(s), which production fields, histories and interfaces are reliably accessible?
8. **Exact `Advies` logic:** investigate only to the degree required by the shortlisted case.
9. **Technical feasibility:** usable supplier-price sources, Exact/Orbis interfaces and integration constraints for the shortlisted candidate(s).
10. **Benchmark / ground truth:** can a defensible reference be constructed before AI/artifact evaluation?
11. **Exception safety / quality risk:** can high-risk or unusual cases be detected and controlled appropriately?
12. **Evaluation feasibility:** sufficient repeated cases, measurable workload and quality outcomes, and participant/domain-expert access.
13. **University-supervisor alignment:** confirm the final case and evaluation design before freezing artifact scope.

## 5.3 Formal two-stage selection rule

The focal case is selected in two stages. A weighted score may not compensate for a failed veto gate.

### Stage A — veto gates (Pass / Redesign / Reject)

1. Required data and tooling are permitted for the intended research use.
2. Accessible data are sufficiently representative for a prototype and test.
3. A reproducible ground truth/reference standard and manual baseline can be created.
4. Critical errors are detectable/reversible and residual risk can be controlled through human review, an audit trail and fallback.
5. Prototype development and evaluation fit the BEP's time, access and participant constraints.
6. The task has a non-trivial AI fit: unstructured, probabilistic or pattern-based support creates value beyond a simpler deterministic rule.

If no candidate passes all gates, no candidate enters the weighted comparison and no unsuitable AI case is forced. First test a bounded redesign, such as narrowing the task, reducing AI autonomy, adding human review or improving the usable data. If no responsible and evaluable AI-supported case remains, report the failed gates as a feasibility finding and seek an explicit scope decision: the academic supervisor determines academic acceptability and the company supervisor confirms operational feasibility/permission. A conventional digital solution may remain a benchmark or recommendation, but it does not silently replace the intended AI-supported focal artifact.

### Stage B — evidence-scored comparison

Criteria and scoring anchors are grounded in the project objective, the workload construct, Task–Technology Fit and MCDA practice (Goodhue & Thompson, 1995; Belton & Stewart, 2002; Department for Communities and Local Government [DCLG], 2009). The student constructs the matrix, documents the evidence, calculates scores and makes the final reasoned recommendation. The student and academic supervisor prospectively agree the criteria definitions, scoring anchors, plausible scoring ranges and weights. The company supervisor validates operational evidence—such as workload, business relevance, data/system access, implementation constraints and risk controls—but does not own the academic weights or final research ranking.

| Criterion | Provisional workshop start | What it means |
|---|---:|---|
| Observed workload contribution | 25% | Human minutes/frequency and qualitative burden; do not also count business effects here. |
| Business value beyond counted workload | 15% | Lead time, service, compliance, scalability or strategic priority not already counted above. |
| AI–task fit | 15% | Degree to which AI capability fits the actual information/decision task. |
| Data readiness above the gate minimum | 15% | Representativeness, traceability, labelling/annotation and cleaning burden. |
| Repetition / process standardization | 10% | Recurrence and stability of inputs, outputs and exception boundaries. |
| Prototype / technical feasibility | 10% | Access, integration dependencies and ability to build a credible prototype. |
| Evaluation feasibility | 10% | Availability of comparable cases, a clear rubric, benchmark and participant access. |

These weights are a **provisional discussion starting point**, not a literature-derived truth. Define plausible best-to-worst scoring ranges first; then agree and freeze the weights before aggregate scores or rankings are calculated or revealed.

Use anchored 1–5 scores: `1 = weak/poorly supported`, `3 = moderate with direct evidence`, `5 = strong with direct evidence`; define candidate-specific 1/3/5 anchors before seeing the total. Record evidence and uncertainty for each score. The total is `Σ(weight × score/5)`.

Run a proportionate sensitivity check using (a) the agreed weights, (b) equal weights, (c) each weight changed by ±20% with renormalization and (d) disputed scores changed by ±1. If the winner changes, report the ranking as unstable and collect more evidence or retain a shortlist rather than hiding the dependence on assumptions.

Unresolved facts about the **current process itself** remain in `Process_Cleaned_V1.5.md` rather than being duplicated here.

---

# 6. Evaluation logic by problem type

The selected focal activity determines the final activity-specific metric, but the **success logic is predeclared now**.

## 6.1 Workload endpoint and quality guardrail

The artifact is successful only when **both** conditions hold:

1. the primary workload endpoint improves by at least the predeclared meaningful threshold; and
2. the quality guardrail passes.

The primary endpoint will be justified after selecting the component by linking it to the workload dimension the improvement is intended to address. Active processing time per eligible case or line remains a possible indicator of time requirements, alongside evidence about frequency, repeated work and difficulty. No endpoint is fixed merely because the exploratory baseline records it. If time is selected, include reading, searching, data entry, human review, correction and the required handoff; report passive waiting and unrelated interruptions separately. Define case comparability and include eligible cases where work is prevented. Limit conclusions to the workload dimensions supported by the evaluation.

Supporting indicators may describe manual actions, system switches, rework, throughput and qualitative difficulty evidence where relevant. Their definitions, evidence sources and role in interpretation must be specified. They are not combined into an unvalidated total-workload score, and the current study does not assess mental workload.

Quality is measured on the **final human-approved outcome**, not only the AI output. After focal-case selection, define a case-specific rubric, a trusted reference/adjudicator and critical versus minor errors. The default guardrail is zero observed critical errors plus final-decision correctness no more than a pre-agreed margin `δ` below the matched manual baseline. `δ = 0` for critical errors; any non-zero margin for minor errors requires explicit process-owner acceptance. With a small BEP sample, report that the guardrail passed in the observed cases rather than claiming statistical non-inferiority.

After the manual baseline and focal case are known, the company/process owner defines the smallest worthwhile workload improvement `Δ` and acceptable minor-error margin `δ`; the academic supervisor validates the research rule. Freeze eligible cases, comparator, rubric, `Δ`, `δ` and analysis before prototype development/formal testing. Keep development examples separate from held-out evaluation cases where feasible.

BEP-ready rule: `For eligible [case type], the AI-supported workflow meets the predefined improvement threshold on [justified workload endpoint] versus [comparator], while the final purchasing outcome fulfils [activity-specific quality requirements]. State which workload dimension the endpoint supports and report effects on Dennis separately where his work changes.`

## Optimization / decision-support case

Possible measures:

- decision quality against a defensible benchmark;
- constraint violations;
- consistency;
- active processing time;
- relevant workload measures from the selected activity;
- human override/reasoning where relevant.

## Verification / detection case

Possible measures:

- accuracy;
- precision/recall where appropriate;
- false positives/negatives;
- deviations detected;
- processing time;
- relevant workload change;
- consistency.

## Exception-based automation / process-redesign case

Possible measures:

- standard-case classification accuracy;
- exception-detection recall;
- exception escape rate;
- PO/output accuracy against trusted reference cases;
- percentage eligible for straight-through processing;
- correction/review rate;
- active buyer effort avoided;
- effect on remaining attention/judgement demand;
- false-positive review burden.

Processing-time reduction alone should not automatically be reported as mental-workload reduction. Likewise, the project should distinguish **potential/estimated workload reduction** from **realized operational reduction** if the artifact is evaluated only on standardized/historical cases rather than deployed live.

---

# 7. Immediate research actions

1. Use the v1.3 live timing structure with the scope addendum and the 21 September stage-organized activity list. Preserve original codes, then add supported analytical activities, stages and separate confidence/reasons after the session. The 17 September suggestion of overlapping activity timing remains a separate unimplemented proposal; this classification update preserves original timing conventions.
2. Continue official exploratory baseline observations after the recorded 31 August, 1 September, 8 September and 18 September sessions; reach five distinct working days and then apply the predeclared coverage review rather than substituting an unconfirmed 40-net-hour target.
3. Complete post-session enrichment immediately after each block, mapping to detailed Task IDs only where evidence supports it.
4. Record MISS, interruptions, J/EXP and recurring unmapped activities consistently; do not silently reconstruct missing information.
5. Ask Johan for approved aggregated or exportable PO-volume information (for example PO count and PO-line count by week/month) as a supplement, not a prerequisite for observation.
6. Preserve pre-PO and post-confirmation price control as separate analytical categories during enrichment.
7. Continue CTA-informed notes around maximalisatie/hold, request validation, clarification and exception cases where tacit cues become visible.
8. Exclude EXC and logistics from thesis timed analysis and candidate selection. Preserve historical raw evidence, record scope interruptions without adding them to adjacent included episodes, and retain unresolved scope flags for review.
9. Produce an included-work profile for Arno and a separate Dennis pattern summary. Add analytical-activity, Task-ID and Van Weele analysis where the respective confidence fields support it; retain combined/unresolved buckets and do not duplicate minutes. Use the Dennis guide to prepare the scheduled discovery sessions.
10. **Only after Measure**, begin targeted Exact/Orbis and other technical/data feasibility work for the shortlisted candidate(s).
11. Run the veto gates, student–academic-supervisor swing weighting, anchored evidence scoring and sensitivity analysis before selecting the focal case; use the company supervisor to validate operational evidence and feasibility.
12. Justify and freeze the focal case's workload endpoint, quality rubric, `Δ` and `δ` before artifact development/formal evaluation.
13. Confirm the selected focal case and evaluation design with the university supervisor before DSRM artifact development.


# References added for selection and evaluation design

Belton, V., & Stewart, T. J. (2002). *Multiple Criteria Decision Analysis: An Integrated Approach*. Kluwer Academic Publishers. https://doi.org/10.1007/978-1-4615-1495-4

Department for Communities and Local Government. (2009). *Multi-Criteria Analysis: A Manual*. https://www.gov.uk/government/publications/multi-criteria-analysis-manual-for-making-government-policy

Goodhue, D. L., & Thompson, R. L. (1995). Task-technology fit and individual performance. *MIS Quarterly, 19*(2), 213–236. https://doi.org/10.2307/249689

Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. In P. A. Hancock & N. Meshkati (Eds.), *Human Mental Workload* (pp. 139–183). Elsevier. https://doi.org/10.1016/S0166-4115(08)62386-9

Triantaphyllou, E., & Sánchez, A. (1997). A sensitivity analysis approach for some deterministic multi-criteria decision-making methods. *Decision Sciences, 28*(1), 151–194. https://doi.org/10.1111/j.1540-5915.1997.tb01306.x


