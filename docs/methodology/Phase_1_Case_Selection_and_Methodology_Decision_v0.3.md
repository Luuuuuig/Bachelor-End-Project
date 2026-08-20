# Phase 1 — Case Selection and Methodology Decision v0.3

**Status:** Working draft, 20 August 2026

**Purpose:**  
This document connects the current-state purchasing observations to the BEP research design and forces an early methodology decision without prematurely closing the current-state investigation.

The current-state process model and this document have different purposes:

- **Process Cleaned V1.0:** What does operational purchasing currently look like?
- **This document:** Which observed purchasing problem can support the BEP research design, and what methodological consequences follow from selecting that problem?

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

The selected case then feeds directly into the later research design. In the current proposal, Phase 2 builds a **deterministic optimization benchmark**, and Phase 3 evaluates AI proposals using measures including **optimality gap versus that benchmark**.

Case selection is therefore not only a business-priority decision. It determines whether the current evaluation architecture remains appropriate.

The critical review also identifies the benchmark as carrying a large part of the evaluation: proposal quality, good/bad advice, appropriate reliance and optimality gap all depend on it.

Consequently:

> A candidate can be operationally valuable while still requiring a different evaluation architecture from the one currently written in the proposal.

The research-design decision should therefore be made before the end of August, while evidence gathering on the detailed current-state process can continue afterward.

---

# 2. Research-methodology position

## 2.1 DSRM remains the formal thesis methodology

The current proposal already positions **Design Science Research / DSRM** as the methodology that structures the whole BEP:

**problem identification → define objectives → design/develop artifact → demonstrate → evaluate → communicate**.

That structure should remain the primary thesis-level methodology.

In the current project this means:

- **Problem identification:** understand the operational purchasing process and its most important problems;
- **Define objectives:** select a purchasing case and specify what a useful solution must achieve;
- **Design/development:** build the selected AI, decision-support, verification or process-support artifact;
- **Demonstration:** apply it to realistic historical and/or synthetic purchasing cases;
- **Evaluation:** evaluate technical performance, practical usefulness and, where applicable, human–AI interaction;
- **Communication:** thesis, company recommendation, implementation roadmap and presentation.

The current-state investigation therefore belongs naturally within the first DSRM steps rather than requiring a second thesis lifecycle.

## 2.2 DMAIC as a company-facing process-improvement lens

The internship problem is also clearly a process-improvement problem: an existing purchasing process is being studied to identify workload, waste, rework, repetitive work and opportunities for improvement.

DMAIC vocabulary can therefore still be useful for the **company-facing improvement work**:

- **Define:** scope the purchasing process and pain points;
- **Measure:** quantify workload, frequency, processing time, errors and rework;
- **Analyze:** identify root causes and distinguish administrative, verification, judgement and process problems;
- **Improve:** design and test a suitable intervention;
- **Control:** formulate monitoring, governance and implementation controls for continued use.

However, DMAIC is **not treated as a second overarching academic methodology** for the thesis.

The BEP may not remain in the company long enough to demonstrate a sustained post-deployment Control phase. The appropriate claim is therefore that DMAIC provides a practical process-improvement vocabulary for company-facing analysis and recommendations, while **DSRM remains the formal research methodology**.

A question to validate with the supervisor is:

> Does it make sense to retain DSRM as the formal thesis methodology while using DMAIC only as a complementary company-facing process-improvement lens?

## 2.3 CTA-informed elicitation is on the critical path

Observation suggests that important purchasing decisions depend partly on experience and tacit knowledge rather than only on visible Exact fields or formal procedures.

This is particularly important because a future benchmark may require buyers to define or validate:

- hard constraints;
- relevant decision cues;
- objective trade-offs;
- practical feasibility conditions;
- exception rules;
- information that is considered trustworthy;
- reasons for overriding a seemingly optimal recommendation.

A **CTA-informed semi-structured elicitation approach** should therefore be used during Phase 1 and the early benchmark-design work.

The goal is not to run a large standalone Cognitive Task Analysis study. The goal is to systematically elicit tacit knowledge around real purchasing cases.

Useful prompts include:

- What made you notice that something might be wrong?
- Which information did you check first, and why?
- What makes you order now instead of waiting?
- Which conditions would make you combine this demand with another order?
- Which constraints are not visible in Exact?
- When would you deliberately deviate from the cheapest or mathematically preferred option?
- Which parts of this decision are rule-based and which depend on experience?
- Would a less experienced buyer make the same decision?

CTA is especially important for **Candidate B — timing and consolidation**. One of its main failure modes is that the decision may depend on undocumented information or tacit constraints unavailable to the model. CTA is the method for discovering whether that is true.

It also supports the critical-review concern that a buyer deviation from a benchmark is not automatically irrational. A deviation may reveal a missing constraint, private information or an objective that the benchmark does not yet represent.

## 2.4 Judge–Advisor System is conditional

The proposal frames the buyer as final decision-maker and the AI as an advisor. This fits a **Judge–Advisor System (JAS)** when the selected artifact gives a recommendation that the buyer can accept, modify or reject.

JAS is therefore particularly relevant for:

- supplier selection;
- order timing/consolidation;
- other multi-attribute purchasing recommendations where the buyer remains responsible.

It is less central for an artifact whose primary function is automatic discrepancy detection or administrative automation.

Therefore:

> JAS should remain central only if the selected primary artifact is genuinely advisory.

The reliance metric and buyer-study design should be revisited after the primary case is selected.

## 2.5 FEDS for artifact-evaluation planning

The critical review recommends making the DSR evaluation strategy more explicit and classifying evaluation episodes using **FEDS**.

This can later distinguish, for example:

- artificial evaluation on held-out purchasing scenarios;
- formative prototype evaluation;
- naturalistic/exploratory evaluation with operational buyers;
- summative evaluation of final artifact performance.

The exact FEDS strategy should be defined after the case, artifact and evaluation shape are selected.

## 2.6 Methodological consequence of case selection

The working methodological structure is therefore deliberately small:

- **DSRM:** formal thesis methodology;
- **DMAIC:** complementary company-facing process-improvement vocabulary;
- **CTA-informed elicitation:** method for tacit constraints, cues and decision logic;
- **JAS:** conditional human–AI interaction framework for advisory cases;
- **FEDS:** evaluation-planning framework for the DSR artifact.

The primary quantitative evaluation metric depends on the **shape of the selected problem**.

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

They do not naturally produce an optimality gap against a deterministic purchasing benchmark.

Importantly, selecting a verification case does **not** eliminate the LLM-provider comparison. Providers can still be run on identical cases and compared on detection performance, consistency, processing time and cost. What changes is the benchmark and the interpretation of proposal quality and reliance.

## 3.3 Administrative automation

Some activities primarily involve executing known steps.

Examples:

- manually transferring request information;
- creating PO lines;
- forwarding the generated PO email;
- attaching confirmations.

Likely evaluation measures include:

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

**Methodological fit:**  
**High if the decision occurs often enough and usable alternatives/data exist.**

Supplier selection naturally supports alternative choices, constraints, cost/lead-time/quality/risk criteria and a deterministic benchmark.

### Decision gate A

If genuine supplier choice occurs sufficiently often and historical alternatives/data are available:

→ keep supplier selection as a viable primary case.

If supplier choice is rare or mostly predetermined:

→ remove supplier selection as the default primary case and explicitly revise that part of the proposal.

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

### Potential benchmark inputs

- current stock;
- safety stock;
- future demand;
- open purchase orders;
- expected receipt dates;
- lead times;
- order costs;
- MOQ/minimum-order conditions;
- urgency/service constraints;
- project or production requirement;
- buyer authorization/control constraints.

The operational buyer has stated that purchases above **€10,000** require an additional approval step. The exact approval path is currently unmapped. If Candidate B is selected, this may need to be represented as a hard constraint or scenario/control condition rather than ignored.

### Potential decision variables

- order now or later;
- which demand to consolidate;
- potentially order quantity.

### Possible objective components

- purchasing/order cost;
- inventory exposure;
- transport/order frequency;
- shortage/rush-order risk;
- service constraints.

**Methodological fit:**  
**Potentially high if the required data, objective and constraints can be operationalized.**

This candidate could preserve:

- deterministic benchmark;
- optimality-gap metric;
- repeated scenarios;
- LLM-provider comparison;
- buyer deviation from prescribed optimum;
- human–AI simulation.

### Decision gate B

If Exact/Orbis exposes the necessary historical/planning inputs and CTA-informed elicitation produces a defensible set of objectives and constraints:

→ Candidate B becomes a strong primary-case option.

If essential inputs are inaccessible or the buyer's decision depends mainly on undocumented information that cannot be captured reliably:

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
- relevant authorization/control constraints;
- whether a meaningful objective can be defined;
- which important cues/constraints exist only in buyer expertise.

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

**Methodological fit:**  
**Conditional.**

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

This contains two separate observed activities.

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

The pre-PO activity also suggests a **propagation problem**: when an outdated Exact price remains stored while supplier confirmation is pending, the same stale value may be reused in another PO before it is corrected.

**Evaluation shape:**  
Verification / discrepancy detection.

**Methodological fit:**  
**Requires a verification architecture rather than the current optimality-gap architecture.**

A primary price-control study would use measures such as:

- precision;
- recall;
- missed discrepancies;
- false alerts;
- processing time;
- rework reduction;
- consistency across repeated runs.

### Consequence of selecting D

The provider comparison can remain:

**same purchasing documents → Provider A / B / C → compare detection performance, consistency, processing time and cost**.

What changes is mainly:

- deterministic optimization benchmark → ground-truth discrepancy benchmark;
- optimality gap → detection metrics;
- definition of good/bad AI output;
- some hypotheses and dependent variables;
- reliance-against-optimum classification;
- sub-questions that explicitly assume optimization.

Selecting price control therefore requires a **targeted redesign**, not a complete restart of the project.

---

# 8. Candidate E — Request validation

Examples:

- suspicious serial number;
- incomplete description;
- inconsistent machine/service information;
- historical PO lookup.

**Evaluation shape:**  
Verification / anomaly detection / information retrieval.

**Methodological fit:**  
**Requires a verification or retrieval-oriented evaluation architecture.**

Like price control, this has a correctness/ground-truth structure rather than a clear optimum.

Potential company value remains meaningful, especially if the activity is frequent.

---

# 9. Candidate F — PO supplier communication

Examples:

- generated PO appears in Outlook;
- buyer checks recipient;
- types standard message;
- forwards supplier email.

**Evaluation shape:**  
Administrative automation.

**Methodological fit:**  
**Low as the central experimental research case.**

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

**Methodological fit:**  
**Low under the current optimization architecture unless a genuine optimization decision is discovered inside the rework process.**

Important unknowns:

- frequency;
- root causes;
- percentage involving price discrepancies;
- quality/detail of Finance feedback;
- repeated checking.

This should remain in the process-improvement scan while being measured.

---

# 11. Provisional candidate matrix

| Candidate | Evidence | Evaluation shape | Data feasibility | Business value | Methodological fit | P0 gate |
|---|---|---|---|---|---|---|
| **A. Supplier selection** | Not yet observed | Optimization | Unknown | Potentially high | **High if frequent/data available** | Frequency + alternatives/data |
| **B. Timing & consolidation** | Repeatedly observed | Optimization | Unknown / to verify | Potentially high | **High if data + objective + constraints are viable** | Exact/Orbis + CTA |
| **C. Advies & toewijzen** | One substantial case | Unclear / assignment | Unknown | Potentially meaningful | **Conditional** | Advies logic + decision freedom |
| **D. Price control** | Clearly observed | Verification | Potentially feasible | Potentially high | **Requires verification architecture** | Frequency + ground truth + data access |
| **E. Request validation** | Observed | Verification / retrieval | Unknown | Unknown | **Requires verification architecture** | Frequency + labelled/traceable errors |
| **F. PO communication** | Repeated | Administrative | Likely feasible | Depends on volume | **Not strong primary research case** | Daily volume/value |
| **G. Finance rework** | Observed/stated | Verification/process | Unknown | Unknown | **Not currently optimization-shaped** | Frequency + root causes |

No final ranking should be made from Week-1 evidence alone. The P0 gates exist to make the methodology choice quickly without pretending the current-state investigation is complete.

---

# 12. Two research-design routes

The supervisor decision can be reduced to **two coherent research-design routes**.

## Route A — Optimization-shaped primary case

Select an optimization-shaped purchasing decision, most plausibly:

- supplier selection if it occurs often enough;
- timing/consolidation if the necessary data and tacit constraints can be captured;
- possibly Advies/toewijzen if genuine alternative decisions exist.

This route preserves most of the current proposal architecture:

- deterministic optimization benchmark;
- optimality gap;
- provider comparison;
- constraint-violation analysis;
- behavioural-operations interpretation of deviations;
- JAS-style buyer reliance where applicable;
- simulation around acceptance/modification/rejection.

**Secondary process-improvement work remains mandatory.** Price checking, request intake, PO communication, Finance hand-off and other opportunities should still be documented for the company even if they are not the central quantitative case.

### Route-A gate

Route A is only viable if at least one optimization-shaped candidate passes its P0 gate.

At present Candidate B is the most frequently observed optimization-shaped alternative, but it is **not yet selected**. Its data and CTA gates must still be closed.

## Route B — Verification-shaped primary case

Select a verification problem, most plausibly price control if measurement confirms its business importance.

This route keeps the **cross-provider comparison** but changes the evaluation architecture:

- deterministic optimum → ground-truth benchmark;
- optimality gap → precision/recall/error metrics;
- optimization proposal quality → detection/recommendation quality;
- reliance classification → human review/use of correct versus incorrect alerts or recommendations.

The LLM-provider question therefore survives. What must be revised are the benchmark, several dependent variables/hypotheses, and the parts of the research questions that explicitly assume optimization.

Secondary process-improvement opportunities also remain part of the company deliverables under this route.

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

# 14. Evidence priorities and immediate actions

The full current-state question list should remain available, but not every question has equal urgency.

## P0-ACTIONS — close before methodology decision

### P0-ACTION-1 — Exact/Orbis data feasibility

**Request from IT immediately.** Determine whether the following can be accessed reliably:

- stock;
- safety stock;
- planned/future demand;
- open POs;
- expected receipt dates;
- lead time;
- historical PO decisions;
- project/production demand;
- allocation/toewijzen relationships;
- supplier and purchase-price history where permitted.

This directly gates Candidate B and partly Candidate C.

### P0-ACTION-2 — Supplier-selection frequency

Ask the operational buyer and inspect historical cases:

- how often genuine supplier choice occurs;
- whether supplier is normally predetermined;
- whether alternative quotations are recorded;
- what data exist for historical alternatives/outcomes.

This directly gates Candidate A and determines whether the proposal's default supplier-selection case remains viable.

### P0-ACTION-3 — Advies/toewijzen decision structure

Determine:

- what generates `Advies`;
- whether the buyer chooses among meaningful alternatives;
- whether the difficulty is decision-making, matching, administration or system usability.

This gates Candidate C.

### P0-ACTION-4 — CTA constraints for timing/consolidation

Use CTA-informed questions around real timing/consolidation cases to identify:

- hard constraints;
- undocumented cues;
- objective trade-offs;
- override reasons;
- information not represented in Exact.

This gates whether Candidate B can be represented in a defensible benchmark.

### P0-ACTION-5 — Buyer-study population

Determine how many people perform sufficiently comparable decisions for a meaningful buyer study.

This gates the Phase-4 extension, not the core thesis.

### P0-ACTION-6 — Formal process validity

Digitise/compare the official buyer instruction and determine which relevant activities are:

- mandatory company/system procedure;
- observed practice;
- buyer-specific working method;
- absent from the documented process.

## P1 — candidate value and baseline

Continue measuring:

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

The current-state investigation should continue, but case/methodology selection cannot wait until every current-state question has been answered.

### 20–24 August

- request Exact/Orbis data-access answers from IT;
- determine supplier-selection frequency;
- clarify `Advies`/`toewijzen`;
- use CTA-informed questioning on timing/consolidation cases;
- establish buyer-study population;
- continue targeted process measurement.

### Before end of August

Take a provisional recommendation to the supervisor and decide:

1. **Route A — optimization-shaped primary case**, or
2. **Route B — verification-shaped primary case**.

Also agree:

- primary purchasing case;
- benchmark type;
- primary performance metrics;
- whether optimality gap remains appropriate;
- whether JAS remains central;
- Phase-4 buyer-study feasibility;
- DSRM as formal thesis methodology and DMAIC as company-facing process-improvement vocabulary.

### After methodology decision

Continue process measurement and use later evidence to:

- validate the case choice;
- refine objectives and constraints;
- establish baseline workload;
- identify secondary implementation opportunities;
- design the DSRM/FEDS evaluation episodes.

The case may still be revised if later evidence clearly invalidates a P0 assumption.

---

# 16. Current provisional position

Based only on Week-1 evidence:

### Supplier selection

Methodologically attractive under Route A, but currently unsupported by observed frequency.

### Timing and consolidation

Currently the most plausible **observed optimization-shaped alternative**, but it is not selected until the Exact/Orbis data gate and CTA constraint/objective gate are passed.

### Price control

Potentially high operational value and clearly observed. It is fundamentally a **verification problem**, but the cross-provider comparison would survive under Route B using ground-truth detection metrics.

### Current decision position

> Do not choose a final case yet. Close the P0 gates immediately and force the research-design choice between an optimization architecture and a verification architecture before the end-of-August methodology freeze.

If Candidate B passes its data and CTA gates, Route A remains the lower-change path because it preserves the current benchmark, optimality-gap and behavioural-operations architecture.

If no optimization-shaped candidate passes its P0 gate while a verification task such as price control proves frequent, measurable and high-value, deliberately move to Route B rather than forcing an artificial optimization framing onto the wrong business problem.
