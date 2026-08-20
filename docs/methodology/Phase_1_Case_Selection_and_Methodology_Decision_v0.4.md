# Phase 1 — Case Selection and Methodology Decision v0.4 
# Analyze broadly, prioritize systematically, implement deeply in one area, and recommend action for the rest.

**Status:** Working draft, 20 August 2026

**Purpose:**  
This document connects the current-state purchasing observations to the BEP research design while preserving the original company objective: **reduce the workload of the operational buyer and improve the efficiency of operational purchasing without removing activities that require purchasing expertise.**

The project therefore has two related but different levels:

- **Company improvement level:** understand and reduce the overall workload across the purchasing process.
- **Thesis research level:** select one high-value and methodologically suitable use case for deep artifact design and scientific evaluation.

Selecting one primary thesis case does **not** mean that it is the only relevant source of workload or the only improvement that should be recommended to Hytech-Pommec.

The current-state process model and this document have different purposes:

- **Process Cleaned V1.0:** What does operational purchasing currently look like?
- **This document:** Where does workload arise, which improvement opportunities matter, and which single case should receive the deep DSR research treatment?

The current-state investigation can remain open while the research-design decision is made earlier.

---

# 1. Objective hierarchy

## 1.1 Primary company objective — reduce operational-buyer workload

The umbrella objective of the internship/BEP is:

> **Reduce the workload of the operational buyer by identifying and reducing unnecessary administrative effort, repetitive verification, avoidable rework and information-handling burden, while supporting rather than replacing purchasing activities that depend on expert judgement.**

The objective is deliberately broader than a single AI use case.

Operational-buyer workload currently appears to contain at least five dimensions:

| Workload dimension | Examples currently observed |
|---|---|
| **Administrative workload** | Manual PO creation, copying information, forwarding generated PO emails, attaching confirmations, updating Exact fields |
| **Verification workload** | Supplier/current price vs Exact, confirmation vs PO/Exact, checking suspicious request information |
| **Decision / cognitive workload** | Order now vs wait, maximalisatie, interpreting future stock, interpreting `Advies`, deciding whether information is credible |
| **Rework / coordination workload** | Finance-returned cases, historical PO searching, incomplete requests, unavailable components, unclear hand-offs |
| **Interruption / task-switching workload** | Emails, colleague questions, supplier messages, payment-related messages and ad-hoc requests during purchasing work |

These dimensions should be measured separately because they may require different interventions.

## 1.2 Primary research objective — select one case for deep evaluation

A bachelor thesis cannot realistically build and experimentally evaluate a separate artifact for every workload source.

The research objective is therefore narrower:

> **Select one high-value, methodologically suitable purchasing activity and design and evaluate an AI-supported or digital artifact for that activity.**

The selected case receives the deepest research treatment:

- explicit problem formulation;
- artifact requirements;
- benchmark or ground truth;
- systematic experiment;
- LLM-provider comparison where appropriate;
- human–AI evaluation where appropriate;
- thesis knowledge claim.

The remaining opportunities stay in the company improvement portfolio and can become:

- quick wins;
- process-redesign recommendations;
- automation opportunities;
- future AI opportunities;
- implementation-roadmap items.

## 1.3 One research case does not replace the broader workload objective

The case-selection exercise must therefore avoid a common failure mode:

> choosing the case that best fits the existing research design and then treating that case as if it were the whole company problem.

A task can be **very important operationally but unsuitable as the main thesis experiment**.

For example, price checking may prove to consume substantial workload while still being a verification problem rather than an optimization problem. It should not disappear from the company recommendations simply because another task is selected for the thesis artifact.

Likewise, a task can be methodologically attractive but create little workload. Such a task should not automatically become the primary BEP case merely because it is easy to benchmark.

The final choice must therefore consider **business importance and research feasibility separately**.

---

# 2. Why a research-design decision is needed now

The proposal defines Phase 1 as **process mapping and case selection**.

Candidate purchasing decisions were originally to be assessed on:

1. data availability;
2. decision frequency;
3. measurable performance;
4. business value;
5. ability to build a benchmark;
6. suitability for repeated scenarios.

The selected case then feeds directly into the later research design. In the current proposal, Phase 2 builds a **deterministic optimization benchmark**, and Phase 3 evaluates AI proposals using measures including **optimality gap versus that benchmark**.

Case selection is therefore not only a business-priority decision. It determines whether the current evaluation architecture remains appropriate.

At the same time, the company objective is workload reduction. The project must therefore avoid selecting a case only because it preserves the existing optimization architecture.

Consequently:

> A candidate can be operationally important while requiring a different evaluation architecture, and a methodologically convenient candidate can still be too small to matter for workload reduction.

The research-design decision should therefore be made before the end of August, while evidence gathering on the broader current-state process and workload can continue afterward.

---

# 3. Research-methodology position

## 3.1 Two audiences, two complementary structures

The project genuinely contains two connected forms of work:

1. a **company process-improvement engagement** aimed at reducing operational-buyer workload;
2. a **research artifact study** aimed at building and evaluating one selected intervention scientifically.

The current methodological position is therefore:

> **DMAIC structures the company improvement engagement and supplies the workload baseline, root-cause analysis, improvement portfolio and control plan; DSRM structures the design and scientific evaluation of the selected artifact, which sits within the Improve stage and carries the thesis's knowledge contribution.**

This should be presented to the supervisor as a methodological proposal rather than assumed as already approved.

## 3.2 DMAIC — company improvement engagement

DMAIC is useful because Hytech-Pommec already has an operating purchasing process and the assignment is to understand and improve it.

### Define

Define:

- company objective: reduce operational-buyer workload;
- process scope;
- stakeholders;
- current pain points;
- workload dimensions;
- candidate improvement areas.

### Measure

Establish the current-state baseline rather than moving directly from process mapping to solution design.

Potential baseline measures include:

- time per task/case;
- frequency per day/week;
- PO volume;
- lines per PO;
- number and duration of price checks;
- frequency of price deviations;
- request-route frequency;
- rework cases from Finance;
- `Advies`/`toewijzen` frequency;
- interruption frequency;
- number of manual hand-offs;
- amount of active processing time versus elapsed time.

The goal is not to prove a stable average from a few Week-1 cases. The goal is to create a defensible baseline showing **where workload is concentrated**.

### Analyze

Determine why the workload occurs and distinguish its underlying type.

Potential causes currently being investigated include:

- stale information in Exact;
- fragmented request channels;
- repeated manual comparison;
- missing or suspicious request information;
- unclear hand-offs;
- system usability or allocation issues;
- supplier constraints;
- tacit purchasing rules;
- expert judgement not directly represented in ERP data;
- interruption and task-switching effects.

The Analyze stage produces both:

1. a prioritized improvement portfolio for the company;
2. the evidence needed to select the primary thesis case.

### Improve

Improve can contain more than one type of recommendation.

Possible interventions include:

- process redesign;
- simple workflow automation;
- data-quality controls;
- AI-assisted document comparison;
- decision support;
- optimization;
- human–AI advisory support.

One selected intervention receives the full DSRM artifact-development and experimental-evaluation treatment. Other improvements can remain recommendations, quick wins or future implementation items.

### Control

The BEP can complete a **Control deliverable** even if it cannot demonstrate six months of sustained post-deployment improvement.

The Control output should specify, for implemented or recommended improvements:

- KPI;
- metric definition;
- baseline;
- target or acceptable range;
- data source;
- metric owner;
- review cadence;
- out-of-control trigger;
- response/escalation action;
- handover responsibility;
- proposed monitoring horizon.

For example, a six-month post-handover monitoring protocol can be specified even though the thesis cannot itself observe the full six months.

The thesis must therefore distinguish between:

- **providing a complete control plan**, and
- **demonstrating sustained long-term improvement**, which may remain outside the available project period.

## 3.3 DSRM — formal thesis/artifact methodology

The current proposal already positions **Design Science Research / DSRM** as the formal methodology for the artifact study:

**problem identification → define objectives → design/develop artifact → demonstrate → evaluate → communicate**.

DSRM remains the structure that supports the thesis knowledge contribution.

For the selected case:

- **Problem identification:** specify the selected purchasing problem and why it matters;
- **Define objectives:** define what the artifact must achieve;
- **Design/development:** build the AI/decision-support/verification artifact;
- **Demonstration:** apply it to realistic historical and/or synthetic cases;
- **Evaluation:** compare performance rigorously;
- **Communication:** thesis, company advice, implementation roadmap and presentation.

DMAIC and DSRM therefore answer different questions:

| | DMAIC | DSRM |
|---|---|---|
| **Main question** | Where does workload come from, how should the process improve, and how should improvement be monitored? | Does the selected artifact work and what can be learned from its evaluation? |
| **Main success evidence** | Baseline + root cause + improvement portfolio + control plan | Artifact demonstration/evaluation + defensible research conclusion |
| **Primary audience** | Company/process owner | Thesis examiner/research group + company |
| **Scope** | Broader operational purchasing process | One selected artifact/use case |

## 3.4 CTA-informed elicitation is on the critical path

Observation suggests that important purchasing decisions depend partly on experience and tacit knowledge rather than only on visible Exact fields or formal procedures.

CTA-informed semi-structured elicitation should therefore be used to identify:

- hard constraints;
- relevant decision cues;
- objective trade-offs;
- practical feasibility conditions;
- exception rules;
- information that is considered trustworthy;
- reasons for overriding a seemingly optimal recommendation;
- constraints not represented in Exact.

This is particularly important for Candidate B — timing and consolidation — because its viability depends on whether the buyer's tacit knowledge can be represented sufficiently in a benchmark or decision-support artifact.

Useful prompts include:

- What made you notice that something might be wrong?
- Which information did you check first, and why?
- What makes you order now instead of waiting?
- Which conditions make you combine demand?
- Which constraints are not visible in Exact?
- When would you deliberately deviate from the cheapest option?
- Which parts are rule-based and which depend on experience?
- Would a less experienced buyer make the same decision?

CTA also helps distinguish irrational deviation from **deviation-as-information**: a buyer may override a benchmark because the benchmark is missing a constraint or private operational knowledge.

## 3.5 Judge–Advisor System is conditional

JAS is relevant if the selected artifact gives a recommendation that the buyer can accept, modify or reject.

It is particularly relevant for:

- supplier selection;
- timing/consolidation;
- other multi-attribute purchasing recommendations.

It is less central for automatic discrepancy detection or simple administrative automation.

The reliance metric and Phase-4 buyer design should therefore be finalized only after the primary case is selected.

## 3.6 FEDS for artifact-evaluation planning

FEDS can structure the evaluation episodes of the DSR artifact, for example:

- artificial evaluation on held-out purchasing scenarios;
- formative prototype evaluation;
- naturalistic/exploratory evaluation with operational buyers;
- summative final-artifact evaluation.

The exact FEDS strategy should be defined after the selected case and artifact are clear.

---

# 4. Workload baseline — what must be measured

Case selection should be grounded in a workload baseline rather than only qualitative impressions.

## 4.1 Baseline unit

For each observed task/case, record where possible:

`Task | Trigger | Order type | Supplier | # lines | Active time | Elapsed time | Manual steps | Rework | Interruption | Judgement required | Output`

## 4.2 Workload dimensions and candidate measures

| Workload dimension | Candidate measures |
|---|---|
| Administrative | processing time, number of manual actions, PO lines entered, emails forwarded |
| Verification | lines checked, deviations found, processing time, repeated comparisons |
| Decision/cognitive | decision frequency, information sources consulted, number of exceptions, judgement complexity |
| Rework/coordination | cases returned, investigation time, hand-offs, missing-information cases |
| Interruptions | interruptions/hour, interruption type, task switches, elapsed-minus-active time |

The purpose is to identify both:

- **where the most workload currently occurs**, and
- **which workload is realistically reducible through an intervention**.

## 4.3 Business importance and research feasibility are separate axes

Each candidate should be considered on two independent dimensions.

### Business importance

Ask:

- How frequent is it?
- How much active time does it consume?
- How much rework/error risk does it create?
- How cognitively demanding is it?
- How much operational value would reducing it create?

### Research feasibility

Ask:

- Are the required data available?
- Is there a defensible benchmark or ground truth?
- Can an artifact be built within the BEP period?
- Can performance be evaluated rigorously?
- Is there enough scenario volume?
- Does the artifact provide a meaningful research question?

The primary thesis case should ideally be **high on both axes**.

A high-business/low-research candidate should remain in the company improvement portfolio even if it is not selected as the experimental case.

---

# 5. Methodological distinction: optimization vs verification

The observed purchasing problems do not all have the same evaluation shape.

## 5.1 Optimization / decision problems

Examples:

- supplier selection;
- order timing;
- consolidation;
- order quantity;
- possibly allocation.

Potential structure:

**Decision → benchmark optimum → optimality gap**

This requires a meaningful objective, constraints, data and repeated scenarios.

## 5.2 Verification / detection problems

Examples:

- supplier confirmation vs Exact;
- current supplier price vs stored Exact price;
- suspicious request information;
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

A verification case does **not** eliminate the LLM-provider comparison. Providers can still receive identical cases and be compared on detection performance, consistency, time and cost.

## 5.3 Administrative automation

Examples:

- manual PO entry;
- supplier email preparation;
- attachments;
- repetitive field updates.

Typical evaluation:

- time saved;
- manual actions eliminated;
- error rate;
- reliability;
- workload reduction.

## 5.4 Process / information-flow problems

Examples:

- fragmented request channels;
- unclear Finance feedback;
- unresolved unavailable items;
- missed `toewijzen`;
- task switching.

These may require workflow redesign or information-system controls rather than an AI decision artifact.

---

# 6. Candidate A — Supplier / quotation selection

**Observed evidence:** Genuine supplier-selection or quotation-comparison decisions have not yet been clearly observed during Week 1.

**Evaluation shape:** Optimization / multi-criteria decision.

**Business importance:** Unknown until frequency is established.

**Research feasibility:** Potentially high if alternatives and historical data exist.

### Decision gate A

If genuine supplier choice occurs sufficiently often and historical alternatives/outcomes exist:

→ retain as a viable primary thesis case.

If supplier choice is rare or mostly predetermined:

→ remove it as the default thesis case, while documenting that change explicitly.

**P0 evidence required:**

- frequency of genuine supplier selection;
- whether multiple alternatives/quotations are recorded;
- historical price, lead-time, quality/risk and outcome data.

---

# 7. Candidate B — Order timing and supplier-order consolidation

Observed examples:

- order now versus wait;
- urgency versus MOQ/minimum value;
- combining small requirements from the same supplier;
- considering stock, future demand, open POs and lead time.

**Observed evidence:** Repeatedly observed.

**Evaluation shape:** Potential optimization / operations-research decision.

**Business importance:** Potentially high, but frequency/time contribution still needs measurement.

**Research feasibility:** Potentially high if Exact/Orbis data and tacit constraints can be captured.

Potential benchmark inputs include:

- current stock;
- safety stock;
- future demand;
- open POs;
- expected receipt dates;
- lead times;
- MOQ/minimum-order conditions;
- urgency/service constraints;
- project/production demand;
- relevant authorization/control constraints.

Purchases above **€10,000** require an additional approval step. The exact path is currently unmapped and may need to be represented as a hard constraint or scenario/control condition.

### Decision gate B

If Exact/Orbis exposes the required inputs and CTA-informed elicitation produces a defensible objective and constraint set:

→ Candidate B becomes a strong primary thesis option.

If essential information cannot be accessed or represented reliably:

→ benchmark feasibility falls substantially.

**P0 evidence required:**

- Exact/Orbis data availability;
- historical ordering decisions;
- relevant authorization/control constraints;
- objective function feasibility;
- important cues/constraints existing only in buyer expertise.

---

# 8. Candidate C — Exact Advies and Toewijzen

Observed workflow:

**underlying project/production demand → Exact Advies → supplier PO → Toewijzen**

One observed combined case took approximately **30–35 minutes**.

**Evaluation shape:** Unclear — potentially assignment/matching, administration, system usability or optimization.

**Business importance:** Potentially meaningful; frequency unknown.

**Research feasibility:** Conditional on understanding what `Advies` calculates and how much decision freedom exists.

### Decision gate C

If the buyer selects among meaningful alternatives with an objective:

→ investigate an optimization/matching artifact.

If the difficulty is mainly understanding or correctly recording an already-determined relationship:

→ treat it as process/system support rather than the primary optimization case.

---

# 9. Candidate D — Purchase-price control

Two separate activities exist:

### D1 — Pre-PO price control

current supplier price ↔ stored Exact price

### D2 — Post-PO confirmation control

supplier confirmation ↔ PO / Exact

**Observed evidence:** Clear manual line-by-line work; one large case estimated at approximately **30–40 minutes**.

The pre-PO activity also suggests a propagation problem: an outdated Exact price can remain available and potentially be reused while supplier confirmation is still pending.

**Evaluation shape:** Verification / discrepancy detection.

**Business importance:** Potentially high; frequency and total workload still need formal measurement.

**Research feasibility:** Potentially high under a verification architecture if ground truth and representative documents are available.

### Consequence of selecting D

The provider comparison survives:

**same documents → Provider A/B/C → compare detection performance, consistency, processing time and cost**.

The changes would be targeted:

- deterministic optimum → ground-truth benchmark;
- optimality gap → precision/recall/error metrics;
- optimization proposal quality → detection quality;
- some hypotheses/dependent variables/reliance measures must be revised.

Price control can therefore be both:

- a strong company workload-reduction opportunity, and
- a viable thesis case if a verification-oriented research design is deliberately selected.

---

# 10. Candidate E — Request validation

Examples:

- suspicious serial number;
- incomplete description;
- inconsistent machine/service information;
- historical PO lookup.

**Evaluation shape:** Verification / anomaly detection / information retrieval.

**Business importance:** Unknown; requires frequency and investigation-time baseline.

**Research feasibility:** Requires traceable/labelled errors or another credible ground-truth strategy.

This remains a company improvement candidate even if not selected for the thesis.

---

# 11. Candidate F — PO supplier communication

Examples:

- generated PO arrives in Outlook;
- buyer checks recipient;
- types standard message;
- forwards PO.

**Evaluation shape:** Administrative automation.

**Business importance:** Likely low per transaction but may accumulate with volume.

**Research feasibility:** Easy to prototype, but weak as the central experimental research case unless the research question changes substantially.

This is a likely quick-win/process-improvement recommendation.

---

# 12. Candidate G — Finance rework

Observed/stated process:

Finance identifies a problem → returns case → buyer investigates Exact / PO / confirmation / invoice information.

**Evaluation shape:** Verification / process redesign.

**Business importance:** Unknown until frequency and rework time are measured.

**Research feasibility:** Currently unclear.

This should remain in the improvement portfolio while real return causes and volumes are measured.

---

# 13. Provisional candidate matrix — dual-axis view

| Candidate | Current evidence | Workload / business importance | Research feasibility | Evaluation shape | P0 gate |
|---|---|---|---|---|---|
| **A. Supplier selection** | Not yet observed | **Unknown** | Potentially high | Optimization | Frequency + alternatives/data |
| **B. Timing & consolidation** | Repeatedly observed | **Potentially high; quantify** | Potentially high if data/CTA gates pass | Optimization | Exact/Orbis + CTA |
| **C. Advies & toewijzen** | One substantial case | **Potentially meaningful; frequency unknown** | Conditional | Assignment/unclear | Advies logic + decision freedom |
| **D. Price control** | Clearly observed | **Potentially high; quantify** | Potentially high under verification design | Verification | Frequency + ground truth + data |
| **E. Request validation** | Observed | **Unknown** | Conditional | Verification/retrieval | Frequency + ground truth |
| **F. PO communication** | Repeated | **Depends on volume** | Technically easy, weak research case | Administrative | PO volume/time |
| **G. Finance rework** | Observed/stated | **Unknown** | Unclear | Verification/process | Frequency + root cause |

The matrix deliberately does **not** collapse business importance into methodological fit.

The thesis case should ideally occupy the **high-business / high-research-feasibility** quadrant.

---

# 14. Two research-design routes

The research-design decision can still be reduced to two main routes.

## Route A — Optimization-shaped primary thesis case

Possible cases:

- supplier selection if frequent;
- timing/consolidation if data/CTA gates pass;
- possibly Advies/toewijzen if genuine alternatives exist.

This route preserves most of the current proposal architecture:

- deterministic optimization benchmark;
- optimality gap;
- provider comparison;
- constraint-violation analysis;
- behavioural-operations interpretation of deviations;
- JAS-style reliance where applicable;
- human–AI simulation.

## Route B — Verification-shaped primary thesis case

Most plausible current example: price control, if workload measurement confirms its importance.

This route preserves the cross-provider comparison but changes:

- benchmark type;
- primary metrics;
- good/bad output classification;
- parts of the reliance operationalization;
- hypotheses/sub-questions that explicitly assume optimization.

## Secondary improvement stream — mandatory under either route

Regardless of Route A or B, the broader workload objective remains active.

The company-facing improvement portfolio can still include:

- price comparison automation;
- request-intake redesign;
- PO email semi-automation;
- Finance hand-off improvement;
- `Advies`/`toewijzen` controls;
- unresolved-item tracking;
- interruption/task-management recommendations.

This is not a third research route. It is part of the company deliverable under **both** research routes.

---

# 15. Phase-4 buyer-study gate

The buyer-study question is:

> **How many people perform the type of decision selected for the experiment?**

Not simply: how many employees are called buyers?

P0 questions:

- Is the operational buyer the only person performing this work?
- Do other buyers perform sufficiently similar decisions?
- Could 6–9 meaningful participants realistically be recruited?
- If not, should the live buyer study remain an extension/go-no-go while the core thesis relies on scenario evaluation and simulation?

This gates Phase 4, not the broader workload-reduction objective.

---

# 16. Evidence priorities and immediate actions

## P0-ACTIONS — close before methodology decision

### P0-1 — Exact/Orbis feasibility

Ask IT immediately whether relevant data can be accessed reliably:

- stock;
- safety stock;
- future/planned demand;
- open POs;
- expected receipt dates;
- lead time;
- historical PO decisions;
- project/production demand;
- allocation/toewijzen relationships;
- supplier and purchase-price history where permitted.

### P0-2 — Supplier-selection frequency

Determine:

- how often genuine supplier selection occurs;
- whether supplier is normally predetermined;
- whether alternative quotes are recorded;
- whether historical alternatives/outcomes exist.

### P0-3 — Advies/toewijzen structure

Determine:

- what generates `Advies`;
- whether there are meaningful alternatives;
- whether the difficulty is decision-making, matching, administration or usability.

### P0-4 — CTA for timing/consolidation

Use real cases to identify:

- hard constraints;
- undocumented cues;
- trade-offs;
- override reasons;
- information missing from Exact.

### P0-5 — Buyer population

Determine how many people perform sufficiently comparable decisions for a meaningful buyer study.

### P0-6 — Formal process validity

Compare the official instruction with practice and classify relevant activities as:

- mandatory company/system procedure;
- observed practice;
- buyer-specific working method;
- absent from documented process.

## P1 — workload baseline and candidate value

Continue measuring:

- price-checking frequency and duration;
- frequency of price deviations;
- Advies/toewijzen frequency;
- external request frequency;
- Finance rework frequency and time;
- PO volume and lines per PO;
- interruption frequency;
- active versus elapsed time;
- administrative actions per case.

These P1 measurements are not secondary in importance to the company objective: they are the workload baseline needed to justify the improvement portfolio.

## P2 — background/process completion

Useful but not necessary for the immediate methodology decision:

- downstream ownership after `Bevestigd`;
- detailed VRD differences;
- interruption subcategories;
- low-frequency exceptions;
- remaining process-map details.

---

# 17. Decision schedule

## 20–24 August

- request Exact/Orbis data-access answers;
- determine supplier-selection frequency;
- clarify `Advies`/`toewijzen`;
- conduct CTA-informed questioning around real timing/consolidation cases;
- establish buyer-study population;
- continue targeted workload measurement.

## Before end of August

Take two things to the supervisor:

### A. Methodology structure

Proposed wording:

> **DMAIC structures the company improvement engagement and supplies the workload baseline, root-cause analysis, improvement portfolio and control plan; DSRM structures the design and scientific evaluation of the selected artifact, which sits within DMAIC's Improve stage and carries the thesis's knowledge contribution.**

Ask whether this separation is acceptable.

### B. Research case decision

Choose provisionally between:

1. **Route A — optimization-shaped primary thesis case**, or
2. **Route B — verification-shaped primary thesis case**.

Also agree:

- primary use case;
- benchmark type;
- primary metrics;
- whether optimality gap remains appropriate;
- whether JAS remains central;
- Phase-4 buyer-study feasibility.

## After the research-case decision

Continue broader DMAIC measurement and analysis so the final company recommendation still addresses **overall workload**, not only the thesis artifact.

Use later evidence to:

- validate the case choice;
- refine artifact objectives/constraints;
- establish a fuller workload baseline;
- design secondary improvements;
- define the Control plan;
- define DSRM/FEDS evaluation episodes.

---

# 18. Current provisional position

The project should currently make **two separate conclusions**.

## 18.1 Company-level conclusion

> Operational-buyer workload is distributed across administrative execution, verification, expert judgement, rework/coordination and interruptions. The project should measure and address this broader workload portfolio rather than treating one AI use case as the whole problem.

## 18.2 Thesis-level conclusion

> One primary use case must still be selected for deep artifact design and scientific evaluation. The preferred case should combine high workload/business importance with strong research feasibility.

Current evidence suggests:

- **Supplier selection:** methodologically attractive but frequency not yet established;
- **Timing/consolidation:** repeatedly observed and potentially suitable for optimization, but Exact/Orbis and CTA gates remain open;
- **Price control:** clearly observed and potentially important for workload reduction; viable as a verification-oriented thesis case if frequency/ground-truth gates pass;
- **Advies/toewijzen:** potentially meaningful but insufficiently understood;
- **PO communication and other administrative issues:** remain valid improvement opportunities even if not selected for the thesis.

The immediate goal is therefore **not** to narrow the company objective to one dimension.

The immediate goal is to:

1. build a defensible workload baseline across the major dimensions;
2. close the P0 research gates;
3. select one primary thesis artifact;
4. retain the remaining workload-reduction opportunities in the company improvement portfolio;
5. later deliver a Control plan defining how improvements should be monitored after handover.
