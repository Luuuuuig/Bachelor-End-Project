# Phase 1 — Case Selection and Methodology Decision v0.5
# Analyze broadly, prioritize systematically, implement deeply in one area, and recommend action for the rest.

**Status:** Working draft, 20 August 2026  
**Supersedes:** v0.4 for current decision status

## Purpose

This document connects the current-state purchasing observations to the BEP research design while preserving the original company objective: **reduce the workload of the operational buyer and improve the efficiency of operational purchasing without removing activities that require purchasing expertise.**

The project has two related levels:

- **Company improvement level:** understand and reduce workload across the broader purchasing process.
- **Thesis research level:** select one high-value and methodologically suitable use case for deep artifact design and scientific evaluation.

Selecting one primary thesis case does **not** mean that it is the only relevant source of workload or the only improvement that should be recommended to Hytech-Pommec.

---

# 1. Objective hierarchy

## 1.1 Primary company objective

> **Reduce the workload of the operational buyer by identifying and reducing unnecessary administrative effort, repetitive verification, avoidable rework and information-handling burden, while supporting rather than replacing purchasing activities that depend on expert judgement.**

Current workload dimensions:

| Workload dimension | Examples currently observed |
|---|---|
| **Administrative** | Manual PO creation, copying information, forwarding generated PO emails, attaching confirmations, updating Exact fields |
| **Verification** | Supplier/current price vs Exact, confirmation vs PO/Exact, checking suspicious request information |
| **Decision / cognitive** | Order now vs wait, maximalisatie, interpreting future stock, deciding whether information is credible |
| **Rework / coordination** | Finance-returned cases, historical PO searching, incomplete requests, unavailable components, unclear hand-offs |
| **Interruption / task switching** | Emails, colleague questions, supplier messages and ad-hoc requests during purchasing work |

## 1.2 Primary research objective

> **Select one high-value, methodologically suitable purchasing activity and design and evaluate an AI-supported or digital artifact for that activity.**

The selected case receives deep research treatment. Other opportunities remain in the company improvement portfolio as quick wins, process redesigns, automation opportunities, future AI opportunities or implementation-roadmap items.

## 1.3 Business importance and research feasibility remain separate

A task may be operationally important but unsuitable as the main thesis experiment. A task may also be easy to benchmark but contribute little to workload reduction.

The primary thesis case should therefore ideally combine:

- high workload/business importance;
- sufficient data availability;
- a defensible benchmark or ground truth;
- enough repeated scenarios;
- an artifact that can be evaluated rigorously within the BEP period.

---

# 2. Methodological position

## 2.1 DMAIC — company improvement engagement

DMAIC structures the broader company-facing improvement work:

- **Define:** workload objective, scope, stakeholders, pain points and candidate improvement areas.
- **Measure:** establish a workload baseline using frequency, processing time, elapsed time, rework, interruptions and transaction complexity.
- **Analyze:** identify causes and distinguish administrative, verification, decision, rework and information-flow problems.
- **Improve:** develop an improvement portfolio and select one intervention for deep DSR treatment.
- **Control:** specify KPIs, owners, review cadence, triggers, response actions and a post-handover monitoring plan.

The project can deliver a Control plan even if it cannot itself demonstrate six months of sustained improvement.

## 2.2 DSRM — formal thesis/artifact methodology

DSRM remains the formal structure for the selected artifact:

**problem identification → define objectives → design/develop → demonstrate → evaluate → communicate**.

> **DMAIC structures the company improvement engagement and supplies the workload baseline, root-cause analysis, improvement portfolio and control plan; DSRM structures the design and scientific evaluation of the selected artifact, which sits within DMAIC's Improve stage and carries the thesis knowledge contribution.**

This methodological separation should still be discussed with the university supervisor before it is frozen.

## 2.3 CTA-informed elicitation

CTA-informed semi-structured elicitation is now on the critical path, particularly for order timing/consolidation.

It should identify:

- hard constraints;
- decision cues;
- objective trade-offs;
- exception rules;
- information that is considered trustworthy;
- reasons for overriding a seemingly optimal recommendation;
- constraints or knowledge not represented directly in Exact.

Week-1 evidence already shows tacit expertise. Examples include recognizing that a requested frame thickness of **33 mm** appears technically implausible and recognizing that a supplied serial number looks unusual based on prior service experience before verifying it in Exact.

This supports treating buyer deviations as potentially informative rather than automatically irrational: the buyer may know something that the benchmark does not yet represent.

## 2.4 JAS and FEDS

JAS remains relevant if the selected artifact gives recommendations that a buyer accepts, modifies or rejects. It is less central for automatic discrepancy detection or administrative automation.

FEDS can later structure formative, artificial, naturalistic and summative evaluation episodes once the selected artifact is clear.

---

# 3. Workload baseline

Case selection should be grounded in a workload baseline rather than isolated Week-1 examples.

For each observed task/case, record where possible:

`Task | Trigger | Order type | # lines | Active time | Elapsed time | Manual steps | Rework | Interruption | Judgement required | Output`

Candidate measures:

| Workload dimension | Measures |
|---|---|
| Administrative | processing time, number of manual actions, PO lines entered, emails forwarded |
| Verification | lines checked, deviations found, processing time, repeated comparisons |
| Decision/cognitive | decision frequency, information sources, exceptions, judgement complexity |
| Rework/coordination | cases returned, investigation time, hand-offs, missing-information cases |
| Interruptions | interruptions/hour, type, task switches, elapsed-minus-active time |

---

# 4. Methodological distinction: optimization vs verification

## 4.1 Optimization / decision problems

Potential examples:

- order timing;
- supplier-order consolidation;
- order quantity;
- supplier selection only if genuine supplier choice exists.

Potential structure:

**Decision → deterministic benchmark → optimality gap**

## 4.2 Verification / detection problems

Examples:

- supplier confirmation vs Exact;
- current supplier price vs stored Exact price;
- suspicious incoming request information;
- Finance discrepancy detection.

These have a ground truth rather than an optimum.

Typical evaluation:

- precision;
- recall;
- false positives/negatives;
- detection accuracy;
- processing time;
- rework avoided;
- consistency.

A verification case does **not** remove the cross-provider comparison. Providers can still receive identical cases and be compared on detection performance, consistency, processing time and cost.

---

# 5. Candidate status after Day-3 clarification

## Candidate A — Supplier / quotation selection

**Updated evidence:** According to the operational buyer, supplier selection is generally **not under his control**. The supplier is normally predetermined or selected elsewhere in the organization, including Finance in some situations.

**Implication:** Supplier selection is no longer treated as a major open mystery for the Arnold-focused workload problem. It becomes a **weak primary thesis candidate for this role**, even though supplier selection remains methodologically suitable in principle for optimization research.

**Remaining verification:** Confirm the formal ownership of supplier selection and whether there are any recurring cases in which Arnold genuinely chooses among suppliers.

**Current status:** **Largely ruled out as the default Arnold-focused thesis case.**

---

# 6. Candidate B — Order timing and supplier-order consolidation

Observed repeatedly:

- order now vs wait;
- urgency vs MOQ/minimum value;
- combining demand from the same supplier;
- considering current/future stock, open POs and lead time.

**Evaluation shape:** Potential optimization / operations-research decision.

**Business importance:** Potentially high, but total workload contribution still needs measurement.

**Research feasibility:** Potentially high if Exact/Orbis data are accessible and tacit constraints can be captured.

Potential benchmark inputs include:

- current stock;
- safety stock;
- future/project demand;
- open POs;
- expected receipts;
- lead time;
- MOQ/minimum-order constraints;
- urgency/service constraints;
- authorization/control constraints.

Purchases above **€10,000** require additional approval. The approval path should be represented as a process/control constraint once fully mapped.

### Remaining P0 gate for Candidate B

1. What Exact/Orbis data can IT expose reliably?
2. What are Arnold's actual rules/cues for buy-now vs hold/maximalisatie?
3. Which relevant cues or constraints exist only in experience and not in Exact?
4. Can these inputs be represented sufficiently to build a defensible benchmark?

---

# 7. Candidate C — Exact Advies and Toewijzen

Observed workflow:

**underlying project/production demand → Exact Advies → supplier PO → Toewijzen**

One observed combined Advies/maximalisatie/toewijzen case took approximately **30–35 minutes**.

## Updated interpretation of Toewijzen

Current understanding is that `toewijzen` is primarily the act of assigning the purchased quantity to the correct underlying project/production demand.

There appears to be little meaningful optimization freedom in the assignment itself:

- assign the purchase correctly to the demand; or
- leave it unassigned, in which case Exact may continue to see the underlying demand as unfulfilled and the requirement can appear again, creating duplicate-order risk.

**Implication:** `Toewijzen` itself currently looks more like an **administrative/system-control step** than a primary optimization decision.

The remaining question is mainly about **Advies**, not `toewijzen`:

- What generates the `Advies` quantity?
- Does Arnold make a meaningful decision when interpreting it?
- Or is he mainly interpreting/connecting system information that is already determined?

**Current status:** **Toewijzen downgraded as an optimization candidate; Advies logic remains open.**

---

# 8. Candidate D — Purchase-price control

Two activities remain distinct:

### D1 — Pre-PO price control

**current supplier price ↔ stored Exact price**

### D2 — Post-PO confirmation control

**supplier confirmation ↔ PO / Exact**

**Evaluation shape:** Verification / discrepancy detection.

**Business importance:** Potentially high, but representative frequency and duration are still unknown.

Time currently appears highly dependent on the number of components/PO lines. Pre- and post-PO checking should **not yet be assumed to take identical time** without measurement.

A current working hypothesis is that Finance-returned cases may create additional burden because the buyer must reopen a completed order and diagnose the cause of a deviation. This is a student hypothesis and must not yet be treated as measured evidence.

**Remaining questions:**

- How frequently are price deviations found?
- How much active time do pre-PO and post-confirmation checks require for different PO sizes?
- How frequently does Finance return cases?
- What causes those returns?
- How much additional investigation/rework time do they create?

---

# 9. Candidate E — Request validation / tacit expertise

Examples now include:

- technically implausible requested dimensions;
- suspicious serial numbers;
- incomplete or inconsistent machine/service information;
- searching historical POs to validate a request.

**Evaluation shape:** Verification / anomaly detection / information retrieval, with a strong tacit-knowledge component.

**Business importance:** Unknown until frequency and investigation time are measured.

**Methodological importance:** High for CTA even if this does not become the primary artifact, because these examples demonstrate that expert knowledge exists outside the explicit ERP data.

---

# 10. Candidate F — PO supplier communication

Manual forwarding of generated PO emails remains a repetitive administrative task.

**Current status:** Likely quick win / semi-automation opportunity, but weak as the central thesis research case unless transaction volume makes the workload substantial.

---

# 11. Candidate G — Finance rework

Finance can return a completed/confirmed case for investigation.

**Evaluation shape:** Verification / process redesign.

**Current status:** Remains open because frequency, root causes and investigation time are not yet measured.

---

# 12. Buyer-study population — partially answered

Current understanding is that comparable purchasing responsibility may involve:

- the operational buyer, with an authorization cap around **€10,000**;
- Dennis, reportedly with a higher authorization cap around **€25,000**;
- Johan, reportedly with a higher authorization cap around **€100,000**.

These authorization limits do **not** prove that the three people perform the same type of purchasing decision.

The remaining question is therefore:

> **Do Johan and Dennis perform sufficiently similar buy/hold/consolidation decisions to Arnold to be meaningful participants in the same study?**

A useful way to test this is a **scenario-based decision elicitation**: show the participants simulated Exact-style purchasing scenarios, collect each person's individual buy/hold decision and reasoning first, then conduct a group debrief. This can simultaneously assess participant comparability and elicit tacit constraints.

---

# 13. VRD vs project/production purchasing — conceptually clearer

Current understanding:

- **VRD (voorraad) purchasing** creates general stock that can later be used by different projects or production requirements.
- **Project/production purchasing** is specifically intended for the named project/order.
- A VRD item may later be allocated/picked for a project, potentially before or after the normal sorting/receipt process depending on the situation.

The exact Exact-system behavior still needs validation, but the conceptual difference is no longer a major case-selection gate.

---

# 14. Formal procedure vs personal working method — still open

A paper Exact work instruction has been received from Johan, but it appears to explain Exact usage rather than the full buyer workflow.

Remaining action:

Ask Johan whether additional documents exist, for example:

- purchasing procedure;
- purchasing policy;
- authorization matrix;
- process description;
- ISO/work instructions;
- role/responsibility description;
- formal exception/approval procedures.

This remains important because the project must distinguish company-required process from Arnold-specific practice.

---

# 15. Important unknowns now narrowed

The project no longer needs to treat supplier selection and `toewijzen` as major unresolved questions. The decision-critical unknowns are now:

## P0 / decision-critical

### 1. Exact/Orbis data availability

**What Exact/Orbis data can IT provide?**

Especially:

- current stock;
- safety stock;
- future/planned demand;
- open POs;
- expected receipt dates;
- lead time;
- historical order decisions;
- project/production demand;
- purchase-price history;
- relevant allocation relationships.

**Why it matters:** This is the biggest technical gate for timing/consolidation.

### 2. Exact `Advies` logic

**How does Exact calculate `Advies`?**

**Why it matters:** Determines whether the observed Advies work contains a meaningful human decision, or mainly system interpretation/administration.

### 3. Buy-now vs hold/maximalisatie decision logic

**What are Arnold's actual rules, cues and trade-offs for ordering now, waiting or consolidating?**

Use CTA-informed questioning around real cases.

**Why it matters:** Determines whether Candidate B can be represented as a defensible optimization/decision-support problem.

### 4. Workload baseline across a normal week

**Which workload category actually consumes the most effort?**

Measure frequency × active time × rework/cognitive burden rather than relying on interesting individual cases.

**Why it matters:** The company objective is overall workload reduction, not preservation of a preferred academic case.

### 5. Price discrepancies and Finance rework

**How frequent and costly are price deviations and Finance-returned cases?**

Measure:

- case frequency;
- PO/line complexity;
- active checking time;
- deviations found;
- Finance-return frequency;
- re-investigation time;
- cause categories.

### 6. Comparable buyer population

**Do Johan and Dennis perform sufficiently similar decisions to Arnold for a buyer study?**

Authorization levels alone do not answer this.

Use targeted questioning and, if approved, scenario-based decision elicitation.

### 7. Formal purchasing/process documentation

**What formal process documents exist beyond the current Exact instruction?**

Ask Johan for additional purchasing procedures, policies, authorization matrices or process/work instructions.

### 8. University-supervisor design decision

**What elements of the original proposal should be preserved?**

In particular:

- optimization benchmark;
- optimality-gap metric;
- cross-provider comparison;
- DMAIC/DSRM relationship;
- CTA elicitation role;
- one deep thesis case vs broader company improvement portfolio;
- buyer-study feasibility.

This should be discussed before the final case/methodology decision is made.

---

# 16. Evidence status summary

| Topic | Current status | Next action |
|---|---|---|
| Supplier selection | **Mostly answered; weak Arnold-focused candidate** | Verify formal ownership only |
| `Toewijzen` | **Mostly answered; administrative/control step** | Validate duplicate-demand mechanism if possible |
| Tacit knowledge outside Exact | **Confirmed qualitatively** | Continue CTA examples |
| Buyer population | **Partially answered** | Test whether decisions are genuinely comparable |
| Price-check duration | **Open** | Time several cases by complexity |
| Interruptions | **Qualitatively confirmed, quantitatively open** | Short structured tallies |
| >€10k approval | **Authority boundary known; detailed workflow partly open** | Map actual approval route if relevant |
| VRD vs project purchasing | **Conceptually clearer** | Validate exact system behavior later |
| Formal process vs personal practice | **Open** | Ask Johan for additional formal documentation |
| Exact/Orbis feasibility | **Open and critical** | Ask IT |
| `Advies` calculation | **Open and critical** | Ask Arnold/IT + inspect Exact |
| Supervisor methodology choice | **Open and critical** | Discuss before design freeze |

---

# 17. Immediate actions

In order:

1. **Ask IT about Exact/Orbis field-level data access.**
2. **Clarify `Advies` calculation and what decision freedom remains for the buyer.**
3. **Continue CTA-informed questioning around buy-now/hold/maximalisatie cases.**
4. **Build the Week-2 workload baseline rather than collecting only exceptional cases.**
5. **Measure price checking and Finance rework separately.**
6. **Determine whether Johan and Dennis make sufficiently comparable decisions.**
7. **Ask Johan for broader purchasing/process documentation.**
8. **Take the remaining methodology questions to the university supervisor before selecting the final primary thesis case.**

---

# 18. Current provisional position

## Company-level conclusion

> Operational-buyer workload is distributed across administrative execution, verification, expert judgement, rework/coordination and interruptions. The project should continue measuring and addressing this broader workload portfolio rather than allowing one thesis artifact to redefine the company problem.

## Thesis-level conclusion

> One primary use case must still be selected for deep artifact design and scientific evaluation. Current evidence weakens supplier selection and `toewijzen` as primary optimization cases. Timing/consolidation remains the strongest currently observed optimization-shaped candidate if its Exact/Orbis and CTA gates pass. Price control remains a strong verification-shaped alternative if workload measurement confirms its business importance.

The immediate goal is to close the remaining decision-critical unknowns, build a defensible workload baseline, and make the final research-design decision together with the university supervisor rather than unilaterally.