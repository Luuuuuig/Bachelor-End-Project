# Project Charter — Operational Purchasing Workload Reduction

**Status:** Current lightweight Define-phase control document, synchronized 26 August 2026.

This charter is intentionally short. It does not replace the proposal, AS-IS process, methodology or measurement protocol; it freezes the project-control decisions that should remain stable while the BEP moves through Measure and Analyze.

## Business problem

The operational purchasing process contains recurring administrative work, manual verification, rework, information-handling burden, interruptions and judgement-intensive activities. The amount and distribution of that workload have not yet been quantified sufficiently to select one improvement case defensibly.

## Business objective / Voice of Customer

Reduce meaningful operational-buyer workload while maintaining the required quality of purchasing outcomes.

The current company direction expects the BEP to produce an **AI-supported contribution where a suitable high-value activity can be justified**. The broader DMAIC analysis remains open to identifying conventional digital/process improvements and quick wins that should be recommended even when they are not appropriate as the main AI artifact.

## Academic objective

Use DMAIC to establish the current process, workload baseline and improvement opportunity; select one high-value focal activity; then use DSRM to design, demonstrate and evaluate the selected digital/AI-supported artifact.

## Primary stakeholders

- Operational buyer — main process user and domain expert.
- Company manager / project sponsor — business relevance and implementation direction.
- TU/e supervisor — academic scope, methodology and evaluation validity.
- Supporting stakeholders as required — Finance, IT/system owners and other purchasing roles.

## In scope

The operational purchasing process from purchasing need arising through `Bevestigd`, including the task families represented in the 31-task AS-IS register.

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

Quality remains a separate CTQ. The concrete quality metric will be defined for the selected focal activity.

## Current evidence state

- AS-IS process mapped through `Bevestigd`.
- 31-task register aligned with the workflow.
- Buyer walkthrough completed and formal SOP/WI evidence integrated.
- Workload construct defined.
- Exploratory Measurement Protocol v1.0 prepared for pilot.
- Representative baseline frequencies and active processing times are not yet established.
- Exact/Orbis production-data/interface feasibility has not yet been investigated in depth and is intentionally deferred until after exploratory Measure.

## DMAIC tollgates

| Gate | Exit condition |
|---|---|
| **Define → Measure** | AS-IS sufficiently stable, scope/workload construct defined, measurement protocol ready for pilot. **Current status: passed provisionally.** |
| **Measure pilot → baseline** | Pilot shows the observation sheet is usable; timing/task-switch rules are workable; confidentiality and sampling rules are clear; protocol is frozen. |
| **Measure → Analyze** | Representative task-level workload evidence exists with documented observation coverage, sample sizes and limitations. |
| **Analyze → Improve** | One focal activity is selected using workload contribution, business value, standardizability, quality risk, required expertise, evaluation feasibility and post-Measure technical/data feasibility. Supervisor alignment obtained. |
| **Improve → Control** | Artifact/future-state intervention is evaluated against current practice using predeclared workload and quality measures; implementation safeguards/KPIs are defined. |

## Current priority

1. Run the Measurement Protocol pilot on the next working day.
2. Revise once if required and freeze the baseline protocol.
3. Collect the exploratory workload baseline.
4. After Measure, investigate Exact/Orbis and other technical/data feasibility for the shortlisted candidate(s) during Analyze.
5. Select the focal thesis artifact with supervisor alignment.

## Key control rule

Do not select or build the final artifact because a single observed case appears interesting. The focal case must pass the Measure/Analyze evidence gates above.
