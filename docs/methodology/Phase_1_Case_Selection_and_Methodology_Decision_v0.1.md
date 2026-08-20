# Phase 1 — Case Selection and Methodology Decision v0.1

**Status:** Working draft, 20 August 2026

**Purpose:**  
This document connects the current-state purchasing observations to the BEP research design and forces an early methodology decision without prematurely closing the current-state investigation.

The current-state process model and this document have different purposes:

- **Process Cleaned V1.0:** What does operational purchasing currently look like?
- **This document:** Which observed purchasing problem can support the BEP research design, and what methodological changes are required if another problem is selected?

The current-state investigation can remain open while the research-design decision is made earlier.

---

# 1. Why a decision is needed now

The proposal defines Phase 1 as **process mapping and case selection**.

Candidate purchasing decisions should be assessed on:

1. data availability;
2. decision frequency;
3. measurable performance;
4. business value;
5. ability to build a benchmark;
6. suitability for repeated scenarios.

The selected case then feeds directly into Phase 2, where a **deterministic optimization benchmark** is built, and Phase 3, where AI proposals are evaluated primarily using **optimality gap versus that benchmark**.

Therefore, case selection is not only a business-priority decision. It determines whether the current research architecture remains valid.

The critical review also identifies the benchmark as carrying a large part of the evaluation: proposal quality, good/bad advice, appropriate reliance and optimality gap all depend on it.

Consequently:

> A candidate can be operationally valuable while still being incompatible with the current BEP evaluation architecture.

The research-design decision should therefore be made before the end of August, while evidence gathering on the detailed current-state process can continue afterward.

---

# 2. Methodological distinction: optimization vs. verification

The observed purchasing problems do not all have the same mathematical or evaluation structure.

## 2.1 Optimization / decision problems

These involve choosing one action from several feasible alternatives according to an objective or combination of objectives.

Examples may include:

- which supplier to select;
- when to order;
- whether to consolidate demand;
- how much to order;
- how to allocate quantities.

These can potentially support:

**Decision → benchmark optimum → optimality gap**

This is compatible with the current proposal architecture if:

- a meaningful objective can be defined;
- constraints can be represented;
- relevant data are available;
- repeated comparable scenarios can be constructed.

## 2.2 Verification / detection problems

These ask whether information is correct or whether a discrepancy exists.

Examples include:

- does the supplier confirmation match Exact?
- is the current supplier price different from the stored Exact price?
- does the incoming serial number appear incorrect?
- does a Finance-returned case contain a discrepancy?

These have a **ground truth**, rather than an optimization optimum.

Typical evaluation would therefore use measures such as:

- precision;
- recall;
- false-positive / false-negative rate;
- detection accuracy;
- processing time;
- rework avoided.

They do **not naturally produce an optimality gap against a deterministic purchasing benchmark**.

Selecting one of these as the primary BEP case would therefore require changing important parts of the existing methodology.

## 2.3 Administrative automation

Some activities primarily involve executing known steps.

Examples:

- manually transferring request information;
- creating PO lines;
- forwarding the generated PO email;
- attaching confirmations.

The main evaluation questions are likely:

- time saved;
- manual actions eliminated;
- error rate;
- reliability;
- user workload.

These may be strong company improvement opportunities, but they do not naturally fit the proposal's optimization-based experimental design.

## 2.4 Process / information-flow problems

Examples include:

- requests entering through multiple channels;
- unclear Finance feedback;
- missed `toewijzen`;
- unavailable requirements becoming difficult to track;
- interruptions and task switching.

These may require process redesign, information-system changes or workflow controls rather than an AI optimization advisor.

---

# 3. Candidate A — Supplier / quotation selection

**Observed evidence:**  
Genuine supplier-selection or quotation-comparison decisions have not yet been clearly observed during Week 1.

**Evaluation shape:**  
Optimization / multi-criteria decision.

**Fit with current proposal:**  
**High in principle.**

Supplier-selection naturally supports alternative choices, constraints, cost/lead-time/quality/risk criteria and a deterministic benchmark.

**Main problem:**  
It is currently unknown whether this decision occurs frequently enough in the operational buyer's actual work to support the BEP.

### Decision gate A

**If genuine supplier choice occurs sufficiently often and historical alternatives/data are available:**

→ keep supplier selection as a viable primary case.

**If supplier choice is rare or mostly predetermined:**

→ remove supplier selection as the default primary case.

**P0 evidence required:**

- frequency of genuine supplier-selection decisions;
- whether multiple supplier/quotation alternatives are recorded;
- historical supplier, price, lead-time, quality/risk information availability.

---

# 4. Candidate B — Order timing and supplier-order consolidation

Examples observed include:

- order now versus wait;
- urgency versus MOQ/minimum value;
- combining small requirements from the same supplier;
- considering stock, future demand, open POs and lead time.

**Observed evidence:**  
This type of judgement has been observed repeatedly.

**Evaluation shape:**  
Potential optimization / operations-research decision.

**Potential benchmark form:**

Inputs:

- current stock;
- safety stock;
- future demand;
- open purchase orders;
- expected receipt dates;
- lead times;
- order costs;
- transport/minimum-order conditions;
- urgency/service constraints.

Decision:

- order now or later;
- which demand to consolidate;
- potentially order quantity.

Possible objective:

- purchasing/order cost;
- inventory exposure;
- transport/order frequency;
- shortage/rush-order risk;
- service constraints.

**Fit with current proposal:**  
**Potentially high.**

This candidate could preserve:

- deterministic benchmark;
- optimality-gap metric;
- repeated scenarios;
- LLM-provider comparison;
- buyer deviation from prescribed optimum;
- human–AI simulation.

However, that fit is conditional on the required data and objective being operationalizable.

### Decision gate B

If Exact/Orbis exposes the necessary historical and planning inputs and a defensible objective can be constructed:

→ Candidate B becomes a strong primary-case option.

If essential inputs are inaccessible or the buyer's decision depends mainly on undocumented information unavailable to the model:

→ benchmark feasibility falls substantially.

**P0 evidence required:**

- Exact/Orbis availability of stock;
- safety stock;
- future demand;
- open POs;
- expected delivery dates;
- lead time;
- MOQ/minimum-value information;
- historical ordering decisions;
- whether a meaningful objective can be defined.

---

# 5. Candidate C — Exact Advies and Toewijzen

Observed workflow:

**underlying project/production demand → Exact Advies → supplier PO → Toewijzen**

One observed combined Advies/maximalisatie/toewijzen case took approximately 30–35 minutes.

**Evaluation shape:**  
Currently unclear.

It could be:

- an assignment/matching problem;
- a system-usability problem;
- an administrative control problem;
- or potentially an optimization problem if there are meaningful alternative allocations.

**Fit with current proposal:**  
**Uncertain / conditional.**

Before treating it as an optimization case, the project needs to know what `Advies` actually calculates and what decision freedom the buyer has.

### Decision gate C

If the buyer is selecting among meaningful alternative allocations with an objective:

→ investigate an optimization benchmark.

If the difficulty is mainly interpreting Exact and correctly recording an already-determined relationship:

→ treat it as process/system support rather than the primary optimization case.

**P0 evidence required:**

- Exact `Advies` calculation;
- underlying demand data;
- mapping between demand, PO lines and allocation;
- whether multiple valid allocation alternatives exist;
- frequency of these cases.

---

# 6. Candidate D — Purchase-price control

This contains two separate observed activities:

### D1 — Pre-PO price control

Current supplier price  
↔  
price stored in Exact

### D2 — Post-PO confirmation control

Supplier confirmation  
↔  
PO / Exact

**Observed evidence:**  
Manual line-by-line checking has been observed, including a large case estimated at approximately 30–40 minutes.

**Evaluation shape:**  
Verification / discrepancy detection.

**Fit with current proposal:**  
**Low without methodological redesign.**

The correct result is whether the price/document comparison detects the true discrepancy. There is no natural purchasing optimum from which to calculate an optimality gap.

A primary price-control study would instead require metrics such as:

- precision;
- recall;
- missed discrepancies;
- false alerts;
- processing time;
- rework reduction.

### Consequence of selecting D

Selecting price control as the primary case would mean:

> Keep the business problem, change the evaluation architecture.

Phase 2 would become a detection/ground-truth benchmark rather than a deterministic optimization benchmark.

Phase 3 metrics and the operationalization of good/bad AI advice would also need to change.

This is feasible, but it is a larger redesign of the proposal.

---

# 7. Candidate E — Request validation

Examples:

- suspicious serial number;
- incomplete description;
- inconsistent machine/service information;
- historical PO lookup.

**Evaluation shape:**  
Verification / anomaly detection / information retrieval.

**Fit with current proposal:**  
**Low.**

Like price control, this has a correctness/ground-truth structure rather than a clear optimum.

Potential company value remains meaningful, especially if the activity is frequent, but it is not currently a natural fit for optimality-gap evaluation.

---

# 8. Candidate F — PO supplier communication

Examples:

- generated PO appears in Outlook;
- buyer checks recipient;
- types standard message;
- forwards supplier email.

**Evaluation shape:**  
Administrative automation.

**Fit with current proposal:**  
**Very low as the central research case.**

Potential company improvement:

- semi-automatic email preparation;
- human verification before send.

Likely evaluation:

- time;
- clicks/actions;
- recipient errors;
- reliability.

This can remain a process-improvement opportunity without becoming the main BEP experimental case.

---

# 9. Candidate G — Finance rework

Observed/stated process:

Finance identifies a problem  
→ returns case  
→ buyer investigates Exact / PO / confirmation / invoice information.

**Evaluation shape:**  
Currently likely verification/process redesign.

**Fit with current proposal:**  
**Low unless a genuine optimization decision is discovered inside the rework process.**

Important unknowns:

- frequency;
- root causes;
- percentage involving price discrepancies;
- quality/detail of Finance feedback;
- repeated checking.

This should remain in the process-improvement scan while being measured.

---

# 10. Provisional candidate matrix

| Candidate | Business evidence | Evaluation shape | Benchmark fit | Current proposal fit | Current status |
|---|---|---|---|---|---|
| **A. Supplier selection** | Not yet observed | Optimization | High | **High if frequent** | **P0 gate** |
| **B. Timing & consolidation** | Repeatedly observed | Optimization | Potentially high | **High if data available** | **P0 gate / promising** |
| **C. Advies & toewijzen** | One substantial case | Unclear / assignment | Uncertain | **Conditional** | **P0 investigation** |
| **D. Price control** | Clearly observed | Verification | Low | **Requires methodology change** | Strong company candidate |
| **E. Request validation** | Observed | Verification | Low | **Requires methodology change** | Measure further |
| **F. PO communication** | Repeated | Administrative | Very low | **Not central research case** | Process-improvement candidate |
| **G. Finance rework** | Observed/stated | Verification/process | Low | **Not currently compatible** | Measure further |

---

# 11. Three coherent methodology routes

## Route 1 — Keep the current research architecture

Select an **optimization-shaped purchasing decision**.

Most plausible current candidates:

- A — supplier selection, if sufficiently frequent;
- B — order timing/consolidation, if the required data exist;
- possibly C — if it turns out to contain a real optimization decision.

Advantages:

- preserves deterministic benchmark;
- preserves optimality gap;
- preserves provider comparison;
- preserves most of the current hypotheses;
- preserves the behavioural-operations interpretation of buyer deviations.

Disadvantage:

- the largest operational workload may ultimately lie in a different, verification-shaped task.

## Route 2 — Select a verification problem and redesign the methodology

For example:

**price control**

Then:

Deterministic optimization benchmark  
→ **ground-truth discrepancy benchmark**

Optimality gap  
→ **precision / recall / detection performance**

Good/bad optimization advice  
→ **correct/incorrect detection or recommendation**

This could better match the company's operational pain point if price checking proves dominant.

However, it would require substantial changes to the current proposal and evaluation logic.

## Route 3 — Optimization core + process-improvement secondary stream

Use an optimization-compatible case such as timing/consolidation for the quantitative BEP core.

At the same time, document other high-value opportunities such as:

- price comparison;
- request intake;
- PO email semi-automation;
- Finance hand-off;
- `toewijzen` controls.

These become part of:

- the process-improvement analysis;
- the implementation recommendation;
- future automation opportunities.

This preserves the academic research architecture while still giving Hytech-Pommec a broader process-improvement output.

**At the moment, Route 3 appears to be the lowest-risk structure, but this is provisional and depends on the P0 gates below.**

---

# 12. Phase-4 buyer-study gate

The current proposal describes the buyer study as an extension and targets approximately **6–9 buyers**.

It is explicitly a go/no-go component: if recruitment or ethics is insufficient, the core thesis should still stand without it.

A key operational question is therefore:

> How many people actually perform the type of purchasing decision selected for the experiment?

This is different from simply asking how many employees are called buyers.

### P0 buyer-study questions

- Is the operational buyer the only person currently performing this work?
- Do other buyers make sufficiently similar decisions?
- Could 6–9 meaningful participants realistically be recruited?
- If not, should Phase 4 remain literature/simulation-based rather than a live buyer study?

This does **not** kill the core thesis, but it determines whether the Phase-4 extension is realistic.

---

# 13. Evidence priorities

The full current-state question list should remain available, but not every question has equal urgency.

## P0 — methodology/case-selection gates

Answer before the methodology decision:

1. **Supplier selection:** How often does genuine supplier choice occur?
2. **Supplier selection:** Are alternatives/quotes and outcomes historically available?
3. **Timing/consolidation:** Are the necessary Exact/Orbis inputs accessible?
4. **Timing/consolidation:** Can a defensible objective/constraint model be defined?
5. **Advies:** What generates the `Advies` quantity?
6. **Advies/toewijzen:** Is there genuine decision freedom or mainly administration?
7. **Buyer-study feasibility:** How many people perform comparable decisions?
8. **Process validity:** Which relevant activities are mandatory/company process versus individual working practice?

## P1 — candidate value and baseline

Answer during continued Week-2 measurement:

- price-checking frequency and duration;
- frequency of price deviations;
- Advies/toewijzen frequency;
- request-route frequencies;
- Finance rework frequency;
- PO volume and lines per PO;
- interruption burden.

## P2 — background / full process understanding

Useful but not necessary for the immediate methodology decision:

- downstream ownership after `Bevestigd`;
- detailed VRD differences;
- interruption categories;
- exact handling of less common exceptions;
- lower-frequency administrative details.

---

# 14. Decision schedule

The current-state investigation should continue.

However, case/methodology selection cannot wait until every current-state question has been answered.

### 20–24 August

- collect P0 evidence;
- validate process with operational buyer;
- inspect Exact/Orbis data availability;
- determine supplier-selection frequency;
- clarify `Advies`;
- establish buyer population.

### Before end of August

Take a provisional recommendation to the supervisor:

**Option A:** retain supplier selection  
**Option B:** move quantitative core to timing/consolidation  
**Option C:** redesign around verification  
**Option D:** optimization core + secondary process-improvement stream

Agree:

- primary purchasing case;
- evaluation shape;
- benchmark type;
- whether optimality gap remains appropriate;
- Phase-4 feasibility.

### After methodology decision

Continue process measurement and use later evidence to:

- validate the choice;
- refine objectives/constraints;
- establish baseline workload;
- identify secondary implementation opportunities.

The case may still be revised if later evidence clearly invalidates a P0 assumption.

---

# 15. Current provisional recommendation

Based only on Week-1 evidence:

### Supplier selection

Methodologically attractive, but currently unsupported by observed frequency.

### Timing and consolidation

Currently the most plausible **optimization-shaped alternative**, but the required Exact/Orbis data and benchmark objective must be confirmed.

### Price control

Potentially high operational value, but is fundamentally a **verification problem** and therefore does not fit the current optimality-gap architecture without redesign.

### Recommended structure to test first

> **Route 3: optimization-compatible quantitative core + broader process-improvement stream.**

The immediate task is therefore not to declare timing/consolidation the final use case, but to determine whether it survives its P0 gates before the supervisor methodology decision.

If it fails those gates, the project must choose between another optimization-shaped decision and a deliberate redesign of the evaluation architecture.
