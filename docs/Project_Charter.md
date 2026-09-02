# Project Charter — Operational Purchasing Workload Reduction

**Status:** Current lightweight project-control document, synchronized 2 September 2026.

This charter is intentionally short. It does not replace the proposal, AS-IS process, methodology, measurement protocol or project timeline; it freezes the project-control decisions that should remain stable while the BEP moves through Measure and Analyze.

## Business problem

The operational purchasing process contains recurring administrative work, manual verification, rework, information-handling burden, interruptions and judgement-intensive activities. The amount and distribution of that workload have not yet been quantified sufficiently to select one improvement case defensibly.

## Business objective / Voice of Customer

Reduce meaningful operational-buyer workload while maintaining the required quality of purchasing outcomes.

The company expects the focal thesis artifact to contain a **meaningful AI-supported contribution**. Conventional automation and process redesign may be supporting components or separate quick-win recommendations. A non-AI focal artifact is an exception and requires documented Analyze evidence that no candidate passes the responsible-AI, data, quality and evaluation-feasibility gates, followed by explicit company and academic-supervisor approval.

## Academic objective

Use DMAIC to establish the current process, workload baseline and improvement opportunity; select one high-value focal activity; then use DSRM to design, demonstrate and evaluate the selected digital/AI-supported artifact.

## Primary stakeholders

- Operational buyer — main process user and domain expert.
- Company manager / project sponsor — business relevance and implementation direction.
- TU/e supervisor — academic scope, methodology and evaluation validity.
- Second academic assessor — Plan of Work approval and co-assessment of the final report under the 1BEPIE procedure.
- Supporting stakeholders as required — Finance, IT/system owners and other purchasing roles.

## In scope

The operational purchasing process from purchasing need arising through `Bevestigd`, represented by the current AS-IS workflow and 31-task detailed register. The Measure phase uses broader live work families and post-session Task-ID enrichment rather than forcing the detailed register into live coding.

Define/Measure/Analyze cover the broader operational process. Improve/DSRM will focus deeply on **one selected primary activity or coherent process component**. Other supported opportunities remain company recommendations/quick wins rather than disappearing from scope.

## Out of detailed scope for now

- Later stages `Ontvangen → Gefactureerd → Betaald`, except where they generate material buyer rework.
- Supplier selection as a recurring operational-buyer thesis case unless new evidence contradicts the current formal/observational evidence.
- Full technical integration or production deployment before the focal use case and feasibility gates are justified.

## Y / outcome structure

The project does **not** use one invented total-workload score.

The Measure-phase outcome is a multidimensional workload profile using, where relevant:

- task frequency;
- active processing time;
- case/line volume;
- rework occurrence and rework time;
- interruptions / organizational constraints;
- qualitative difficulty / uncertainty / exception evidence;
- expertise dependence.

Quality remains a separate CTQ. The concrete quality metric is focal-activity-specific, but the success structure is already fixed: the predeclared workload endpoint must improve by at least a meaningful threshold **and** the quality guardrail must pass. Thresholds and the activity-specific rubric are frozen after focal-case selection and manual-baseline review, before artifact development/formal testing.

## Current evidence state

- AS-IS process mapped through `Bevestigd` and synchronized through 2 September; post-MAX HOLD/ORD is assessed whether or not demand was added.
- 31-task register aligned with the workflow; maximalisatie outcome (ADD/NONE) is separated from the downstream HOLD/ORD outcome.
- Buyer walkthrough completed and formal SOP/WI evidence integrated.
- Workload construct defined.
- 28 August Measure pilot completed.
- Two official baseline days completed: 31 August (165 net / 103 timed coded-active minutes after the OBS-05 correction) and 1 September (186 net / 162 timed coded-active minutes). Current totals: **351 net observed minutes** and **265 timed coded-active minutes**.
- Measurement Protocol v1.3 is controlled for observations from 2 September onward; its live fields/timing remain comparable with v1.2.
- The current planning target is five distinct observation days, followed by the predeclared coverage review; 40 net hours is not assumed to be equivalent.
- Representative baseline frequencies and active processing-time distributions are still being established across additional sessions.
- Exact/Orbis production-data/interface feasibility remains intentionally deferred until after exploratory Measure.

## Time boundary and study load

- The combined normative workload for **1BEPIE + 1BEPIEX is 420 hours in total**.
- Company placement / Hytech-Pommec contract runs through **7 January 2027**. This is the company-work boundary, not the end of all academic obligations.
- Final report, scientific-conduct item and end-BEP reflection: **15 January 2027 at 23:59**.
- Final presentation / assessment meeting: **on or before 29 January 2027**.
- Final assessment deadline: **7 February 2027**.
- Detailed sequencing, deadline-control notes and planned-versus-actual effort tracking are maintained in `Project_Timeline.md`.

## DMAIC tollgates

| Gate | Exit condition |
|---|---|
| **Define → Measure** | AS-IS sufficiently stable, scope/workload construct defined, measurement protocol ready for pilot. **Current status: passed.** |
| **Measure pilot → baseline** | Pilot shows the observation sheet is usable; timing/task-switch rules are workable; confidentiality and sampling rules are clear; controlled protocol established. **Current status: passed; v1.3 is controlled from 2 September without changing the live coding structure.** |
| **Measure → Analyze** | At least five distinct observation days are documented; the v1.3 Day-5 coverage review passes; representative activity-family workload evidence exists, with detailed Task-ID enrichment where justified, plus documented windows, net observed time, coded-active time, case mix, unmapped work and limitations. |
| **Analyze → Improve** | Candidates first pass non-compensable AI/data/ground-truth/risk/time gates, then are compared with pre-agreed weighted criteria and sensitivity analysis. One focal activity is selected and supervisor alignment obtained. |
| **Improve → Control** | Before development/formal testing, the primary workload endpoint, meaningful-improvement threshold, quality rubric and guardrail are frozen. The artifact is then evaluated against current practice; implementation safeguards/KPIs are defined. |

## Current priority

1. Continue official baseline observations using Measurement Protocol v1.3 and the v1.3 live cheat sheet; reach five distinct working days and then apply the coverage review.
2. Complete Task-ID enrichment immediately after each block and preserve `C/P/U/?`, separate MAX and HOLD/ORD outcomes, interruptions and measurement limitations.
3. Build the activity-family workload profile across multiple sessions/dayparts and supplement it with approved aggregated PO/line-volume data where available.
4. After Measure, investigate Exact/Orbis and other technical/data feasibility for the shortlisted candidate(s) during Analyze.
5. Apply veto gates, student–academic-supervisor weighting, anchored scoring and sensitivity analysis before selecting the focal case; use the company supervisor to validate operational evidence and feasibility.
6. Freeze the focal-case workload threshold and quality guardrail before artifact development/formal testing.

## Key control rule

Do not select or build the final artifact because a single observed case appears interesting. The focal case must pass the Measure/Analyze evidence gates above.
