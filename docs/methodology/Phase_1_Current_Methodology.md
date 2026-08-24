# Phase 1 — Current Methodology and Case-Selection Status

**Status:** Current working source of truth, synchronized 24 August 2026.

This file replaces the earlier `v0.1`–`v0.5` working drafts. Those revisions remain recoverable through Git history but should no longer be treated as active project status.

---

# 1. Project objective

The company-level objective is to reduce workload in operational purchasing by identifying and reducing unnecessary administrative effort, repetitive verification, avoidable rework and information-handling burden, while preserving or supporting activities that depend on purchasing expertise.

The thesis-level objective is to select one high-value purchasing activity and design and evaluate a digital or AI-supported artifact for that activity.

Selecting one primary thesis case does not mean other improvement opportunities disappear. They remain part of the company improvement portfolio.

---

# 2. Research structure

## DMAIC — broader process-improvement framework

DMAIC structures the improvement of the existing operational purchasing process:

- **Define:** scope, stakeholders, workload problem and candidate areas.
- **Measure:** frequency, active processing time, elapsed time, rework, interruptions and transaction complexity.
- **Analyze:** identify root causes and distinguish administrative, verification, judgement, rework and information-flow problems.
- **Improve:** prioritize interventions and select one artifact for deeper development.
- **Control:** define KPIs, ownership, review cadence and implementation controls.

DMAIC is appropriate because the project is improving an **existing** purchasing process rather than designing an entirely new process from scratch.

## DSRM — artifact design and evaluation

The selected AI/digital artifact will follow Design Science Research Methodology:

`problem identification → objectives → design/development → demonstration → evaluation → communication`

DSRM sits mainly inside DMAIC's Improve stage and provides the formal artifact-development/evaluation structure.

## CTA-informed elicitation

Cognitive Task Analysis-informed questioning is used where buyer expertise is tacit, especially for:

- buy-now versus hold decisions;
- maximalisatie;
- interpreting stock/future demand/urgency;
- recognizing suspicious request information;
- exception rules and override reasoning.

## JAS / human-AI reliance

Judge-Advisor System concepts remain conditional. They become relevant only if the final artifact gives advice that a buyer can accept, modify or reject. They are not automatically required for pure administrative automation or discrepancy detection.

---

# 3. Evidence base now available

The methodology and case-selection process now uses:

1. direct observations from 17–21 August;
2. buyer/manager explanations and the 21 August workflow walkthrough;
3. formal purchasing documentation received 21 August;
4. future system/data evidence from Exact/Orbis and structured baseline measurement.

The formal-document package includes SOP740-01, SOP741-01 and supporting forms/work instructions. Its analytical register is stored in `docs/company-documentation/Official_Document_Register_2026-08-21.md`.

**The project is no longer waiting for the formal purchasing SOP.**

---

# 4. Workload baseline

For relevant cases record where practical:

`Task | Trigger | Order type | # lines | Active time | Elapsed time | Manual steps | Rework | Interruption/task switch | Judgement required | Output`

Workload is treated as multidimensional. Time alone is not sufficient.

| Dimension | Example measures |
|---|---|
| Administrative | active time, manual actions, entries, emails |
| Verification | lines checked, deviations, checking time |
| Decision/cognitive | decision frequency, cues, exceptions, judgement requirement |
| Rework/coordination | returned cases, investigation time, hand-offs |
| Interruptions | interruptions/task switches, elapsed-minus-active time |

Clock measurements from Week 1 are single-case elapsed-time observations, not representative averages.

---

# 5. Current candidate portfolio

## 5.1 Active primary-case candidates

### A. Order timing and supplier-order consolidation

Observed repeatedly:

- order now versus wait;
- urgency versus MOQ/minimum value;
- same-supplier consolidation;
- stock, future demand, open POs, expected receipts and lead time.

**Current status:** Strong active candidate.

**Main gates:**

- workload frequency/time;
- Exact/Orbis data availability;
- defensible decision representation/benchmark;
- tacit buyer constraints captured through CTA.

Potential artifact: decision support / optimization / information support.

### B. Purchase-price control

Two distinct activities:

1. pre-PO current supplier price versus stored Exact price;
2. post-PO supplier confirmation versus PO/Exact.

**Current status:** Strong active candidate because manual line-by-line verification has been observed and produces measurable discrepancy outcomes.

**Main gates:**

- normal frequency;
- line count/complexity;
- representative active time;
- price-deviation rate;
- availability of supplier/Exact data or APIs.

Potential artifact: automated retrieval/comparison, stale-price detection, deviation highlighting, human-reviewed correction.

## 5.2 Active but evidence-insufficient candidates

### C. Request intake and validation

Observed issues include screenshots, manual entry, incomplete information, suspicious serial/machine information and historical-PO searching.

**Current status:** Real problem observed, but frequency and business impact are not yet known.

Potential artifact: structured intake, information extraction, retrieval/validation support.

### D. Finance-returned rework

Finance can return cases to the buyer for investigation.

**Current status:** Potential process/rework problem, but frequency and root causes remain unknown.

Potential artifact: structured hand-off, discrepancy classification, automated evidence comparison.

## 5.3 Supporting improvement opportunities, not current primary thesis candidates

### Exact Advies / Toewijzen

`Toewijzen` is now understood primarily as an assignment/control action linking purchased quantity to underlying project/production demand. It is important for process reliability but currently weak as a stand-alone optimization thesis case.

`Advies` logic still needs to be understood and may support another artifact.

### PO supplier communication

Manual forwarding of generated POs is repetitive and likely suitable for a quick win or semi-automation. It is currently too narrow to be the default thesis case unless transaction volume shows substantial total workload.

## 5.4 Ruled out / deprioritized

### Supplier selection

**Removed from the active Arnold-focused candidate portfolio.**

The operational buyer stated that suppliers are usually predetermined or selected elsewhere. Formal SOP741-01 further assigns supplier selection/approval and monitoring to Manager Procurement with QA involvement where required.

Supplier selection may remain relevant as wider procurement context but should no longer appear as a major unresolved Arnold-workload candidate.

---

# 6. Formal procedure versus operational practice — resolved at high level

Earlier methodology drafts treated formal purchasing documentation as a major missing input. That is no longer correct.

The received SOP package confirms the high-level purchasing process and control responsibilities. It does **not** define the detailed operational routines observed during shadowing, such as maximalisatie, Exact `Advies`, `Toewijzen`, proactive price checking and Finance rework.

Therefore current classification is:

- **Formal requirement** where explicitly stated in SOP/work instruction;
- **Partly documented** where the SOP specifies only a high-level requirement;
- **Observed operational practice** where detailed execution is not specified;
- **Divergence** only if direct contradictory evidence exists.

Absence from the SOP is not evidence of non-compliance.

---

# 7. Resolved items removed from the active gate list

The following should no longer be carried forward as unresolved research questions:

- whether the formal purchasing SOP exists/has been received;
- formal ownership of supplier-selection control;
- whether supplier selection is a default Arnold-focused candidate;
- the basic purpose of `Toewijzen`;
- the conceptual difference between VRD and project/production purchasing;
- whether Week-1 timing values were estimates.

These findings can be reopened only if new direct evidence contradicts the current understanding.

---

# 8. Active decision-critical gates

## P0 — required before final primary-case selection

1. **Workload baseline:** which active candidate actually contributes most meaningful workload over a normal period?
2. **Exact/Orbis data availability:** which fields and histories can be accessed reliably?
3. **Exact `Advies` logic:** what determines advised quantities and how often is it operationally relevant?
4. **Buy/hold/maximalisatie logic:** what rules, cues, trade-offs and tacit constraints does the buyer use?
5. **Price-control baseline:** frequency, active time, line complexity and deviation rate.
6. **Finance rework:** frequency, root causes and investigation burden.
7. **Technical feasibility:** supplier price source/API and usable Exact/Orbis interfaces.
8. **Evaluation feasibility:** sufficient repeated cases, benchmark/ground truth and participant access.
9. **University-supervisor decision:** confirm final case and evaluation design before freezing the artifact scope.

## Secondary process questions

- How is an unavailable requirement tracked after removal from a PO?
- How exactly is an above-authority order routed/recorded and continued after `Fiatteren`?
- Are services normally included in proactive pre-PO price checking?
- Who owns later stages after `Bevestigd` where they create purchasing rework?

---

# 9. Evaluation logic by problem type

## Optimization / decision-support case

Potential example: order timing/consolidation.

Possible evaluation:

- decision quality against a defensible benchmark;
- constraint violations;
- workload/time reduction;
- consistency;
- human override/reasoning where relevant.

## Verification / detection case

Potential example: price control.

Possible evaluation:

- accuracy;
- precision/recall where appropriate;
- false positives/negatives;
- deviations detected;
- processing time;
- workload reduction;
- consistency.

The evaluation design should follow the selected problem type rather than forcing every candidate into the same metric.

---

# 10. Immediate methodology actions

1. Collect structured baseline observations without timing every click.
2. Obtain PO/line volumes and relevant historical fields from Exact where possible.
3. Clarify Exact/Orbis access and `Advies` logic with IT.
4. Continue CTA-informed elicitation around real buy/hold/maximalisatie cases.
5. Measure pre-PO and post-confirmation price control separately.
6. Collect/categorize Finance-returned cases.
7. Reassess active candidates using workload, business value, data availability, evaluation quality, implementation risk and human-expertise requirements.
8. Select one primary thesis artifact with the university supervisor.

---

# 11. Decision rule for repository synchronization

Going forward:

- dated meeting notes are **historical evidence snapshots**;
- `docs/process/Process_Cleaned_V1.0.md` is the current operational-process truth;
- this file is the current methodology/candidate-selection truth;
- `docs/company-documentation/Official_Document_Register_2026-08-21.md` is the formal-document evidence register;
- the final proposal in `docs/proposal/` is the approved/current proposal document;
- older hypotheses should not remain in active candidate tables or active question lists once resolved.