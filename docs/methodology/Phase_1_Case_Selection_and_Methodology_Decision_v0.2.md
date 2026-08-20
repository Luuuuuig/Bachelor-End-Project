# Phase 1 — Case Selection and Methodology Decision v0.2

**Status:** Working draft, 20 August 2026

**Purpose:**  
This document connects the current-state purchasing observations to the BEP research design and forces an early methodology decision without prematurely closing the current-state investigation.

The current-state process model and this document have different purposes:

- **Process Cleaned V1.0:** What does operational purchasing currently look like?
- **This document:** Which observed purchasing problem can support the BEP research design, what methodological structure should guide the project, and what changes are required if another problem is selected?

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

# 2. Working methodological framing

The BEP currently combines an **organizational process-improvement problem** with the possible design of a **technological decision-support artifact**. A layered methodology is therefore more appropriate than treating one framework as the complete method for the whole project.

The current working structure is:

| Method / framework | Role in the BEP | Main project stage |
|---|---|---|
| **DMAIC** | Overarching process-improvement structure for understanding, measuring, analysing and improving the existing purchasing process | Entire project |
| **Design Science Research / DSRM** | Structures the design, development, demonstration and evaluation of the eventual technological artifact | Mainly Improve / Control |
| **Cognitive Task Analysis (CTA)** | Supporting elicitation method for tacit purchasing knowledge, cues, rules and exception handling that may not be visible in Exact or formal instructions | Define / Measure / Analyze |
| **Judge–Advisor System (JAS)** | Human–AI interaction framing if the selected artifact provides advice while the buyer retains final decision authority | Conditional on decision-support use case |
| **FEDS** | Supports explicit design of artifact-evaluation episodes and their artificial/naturalistic character | Evaluation stage |
| **Practical skill-distillation approaches** | Possible implementation inspiration for converting expert behaviour into structured procedures | Optional implementation support |

These methods are **complementary rather than competing**. Their relevance depends partly on which purchasing case is selected.

## 2.1 DMAIC as the overarching process-improvement structure

The company already has an operational purchasing process. The task is therefore to understand and improve an existing process rather than design an entirely new process from first principles. For that reason, the current working choice is **DMAIC rather than DMADV**.

### Define

Clarify:

- project scope;
- operational purchasing process;
- buyer responsibilities;
- observed pain points;
- stakeholders;
- candidate problems/use cases.

Current outputs include the AS-IS process map and the initial candidate list.

### Measure

Establish a baseline using evidence such as:

- task frequency;
- processing time;
- number of PO lines;
- price deviations;
- Finance rework;
- interruption frequency;
- request routes;
- Advies/toewijzen frequency;
- supplier-selection frequency.

Single observed timings should remain case observations until repeated measurement supports broader claims.

### Analyze

Identify why workload or errors occur and distinguish their underlying type.

Possible causes currently being investigated include:

- stale information in Exact;
- fragmented request channels;
- repeated manual comparison;
- unclear hand-offs;
- system usability or allocation issues;
- supplier constraints;
- tacit purchasing rules;
- expert judgement that is not directly represented in ERP data.

This stage also includes selecting the BEP case and deciding whether it is an optimization, verification, administrative-automation or process-redesign problem.

### Improve

Design the intervention only after the problem and its causes are sufficiently understood.

Possible intervention forms include:

- process redesign;
- simple workflow automation;
- AI-assisted document comparison;
- decision support;
- optimization;
- human–AI advisory support.

If the selected intervention includes a technological artifact, **DSRM becomes the more detailed design/evaluation method inside the Improve stage**.

### Control

Evaluate whether the intervention remains useful and reliable and define how it should be used in practice.

The relevant control/evaluation measures depend on the selected problem shape and may include:

- optimality gap;
- constraint violations;
- precision/recall;
- processing time;
- error/rework rate;
- buyer workload;
- human oversight;
- monitoring and governance requirements.

## 2.2 DSRM inside the improvement cycle

The existing proposal already uses Design Science Research as the artifact-development logic. The critical review considers DSR an appropriate choice but recommends making the relationship between project phases and DSRM more explicit and clarifying the evaluation strategy.

In the current working structure:

**DMAIC answers:**

> Which process problem should be improved, why does it occur, and did the overall process improve?

**DSRM answers:**

> What artifact should be designed for the selected problem, how should it be developed, demonstrated and evaluated?

A tentative relationship is:

| Project activity | DMAIC | DSRM role |
|---|---|---|
| Current-state process mapping | Define | Problem identification context |
| Workload and baseline measurement | Measure | Requirements/evidence for objectives |
| Root-cause analysis and case selection | Analyze | Problem specification + objectives |
| Artifact design/development | Improve | Design & development |
| Demonstration/pilot | Improve | Demonstration |
| Experimental/user evaluation | Improve / Control | Evaluation |
| Implementation recommendation and monitoring | Control | Communication / organizational embedding |

The exact mapping should be refined when the primary case is selected.

## 2.3 Cognitive Task Analysis as a supporting elicitation method

Observation suggests that important purchasing decisions depend partly on experience and tacit knowledge rather than only on visible Exact fields.

Examples include recognizing:

- suspicious request information;
- whether future stock is genuinely sufficient;
- when a small order should be held for consolidation;
- whether a requirement is urgent enough to order immediately;
- when an item deserves an additional price or history check.

CTA can therefore support the Define/Measure/Analyze stages by eliciting:

- decision cues;
- tacit rules;
- information-search strategies;
- exception-handling behaviour;
- differences between novice and experienced judgement;
- which parts of the task are suitable for automation versus human oversight.

This does not require a large standalone CTA study. A lightweight CTA / Critical-Decision-style approach can be used around real observed cases by asking questions such as:

- What made you notice that something might be wrong?
- Which information did you check first?
- What would make you order now rather than wait?
- Would a less experienced buyer make the same decision?
- Which parts of this decision are rule-based and which depend on experience?

## 2.4 Judge–Advisor System as a conditional framework

The proposal frames the buyer as the final decision-maker and the AI as an advisor. This fits a Judge–Advisor System when the selected artifact produces a recommendation that the buyer can accept, modify or reject.

JAS is therefore most relevant for cases such as:

- supplier selection;
- order timing/consolidation;
- other multi-attribute purchasing decisions where the buyer retains final responsibility.

It is less central for a largely automatic verification task such as line-by-line price discrepancy detection.

Therefore:

> JAS should remain in the methodology only if the selected primary artifact is genuinely advisory rather than primarily automatic verification or workflow automation.

The existing proposal's reliance measures and buyer-study design should therefore be revisited after the primary case is selected.

## 2.5 FEDS for evaluation design

The critical review recommends explicitly classifying DSR evaluation episodes using FEDS.

This can later help distinguish, for example:

- artificial evaluation of an artifact on held-out purchasing scenarios;
- naturalistic/exploratory evaluation with operational buyers;
- formative evaluation during prototype iteration;
- summative evaluation of final performance.

The exact FEDS evaluation strategy should be defined after the artifact and case are clearer.

## 2.6 Practical skill-distillation approaches

Practical approaches that convert expert demonstrations or procedures into reusable AI instructions may be useful when translating buyer expertise into an implementation.

They should currently be treated as **implementation inspiration rather than the primary academic methodology**.

## 2.7 Methodological consequence of case selection

The methodology stack is intentionally conditional:

- **DMAIC remains relevant regardless of the selected candidate** because the company problem is process improvement.
- **DSRM remains relevant if a technological artifact is designed.**
- **CTA supports discovery of tacit knowledge and decision rules.**
- **JAS remains central only if the artifact acts as an advisor to the buyer.**
- **FEDS becomes relevant when the artifact evaluation strategy is specified.**
- **The primary quantitative evaluation metric depends on whether the selected task is optimization, verification, automation or process redesign.**

---

# 3. Methodological distinction: optimization vs. verification

The observed purchasing problems do not all have the same mathematical or evaluation structure.

## 3.1 Optimization / decision problems

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

## 3.2 Verification / detection problems

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

## 3.3 Administrative automation

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

## 3.4 Process / information-flow problems

Examples include:

- requests entering through multiple channels;
- unclear Finance feedback;
- missed `toewijzen`;
- unavailable requirements becoming difficult to track;
- interruptions and task switching.

These may require process redesign, information-system changes or workflow controls rather than an AI optimization advisor.

---

# 4. Candidate A — Supplier / quotation selection

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

# 5. Candidate B — Order timing and supplier-order consolidation

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

# 6. Candidate C — Exact Advies and Toewijzen

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

# 7. Candidate D — Purchase-price control

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

# 8. Candidate E — Request validation

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

# 9. Candidate F — PO supplier communication

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

# 10. Candidate G — Finance rework

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

# 11. Provisional candidate matrix

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

# 12. Three coherent methodology routes

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

# 13. Phase-4 buyer-study gate

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

# 14. Evidence priorities

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

# 15. Decision schedule

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
- Phase-4 feasibility;
- which parts of the methodology stack remain applicable.

### After methodology decision

Continue process measurement and use later evidence to:

- validate the choice;
- refine objectives/constraints;
- establish baseline workload;
- identify secondary implementation opportunities;
- refine DSRM/FEDS evaluation design.

The case may still be revised if later evidence clearly invalidates a P0 assumption.

---

# 16. Current provisional recommendation

Based only on Week-1 evidence:

### Supplier selection

Methodologically attractive, but currently unsupported by observed frequency.

### Timing and consolidation

Currently the most plausible **optimization-shaped alternative**, but the required Exact/Orbis data and benchmark objective must be confirmed.

### Price control

Potentially high operational value, but is fundamentally a **verification problem** and therefore does not fit the current optimality-gap architecture without redesign.

### Recommended structure to test first

> **Route 3: optimization-compatible quantitative core + broader process-improvement stream, structured overall through DMAIC and using DSRM for the eventual artifact.**

The immediate task is therefore not to declare timing/consolidation the final use case, but to determine whether it survives its P0 gates before the supervisor methodology decision.

If it fails those gates, the project must choose between another optimization-shaped decision and a deliberate redesign of the evaluation architecture.
