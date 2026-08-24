# Workload Definition — Operational Purchasing BEP

**Status:** Canonical project definition, synchronized 24 August 2026.

This file defines how **workload** is interpreted across the BEP. Current process and methodology files should follow this definition rather than introducing separate ad-hoc definitions.

---

# 1. Governing literature source

**Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015).** *State of science: Mental workload in ergonomics*. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

Young et al. describe mental workload as a **multidimensional construct** determined by:

- characteristics of the **task**, such as demands and required performance;
- characteristics of the **operator**, such as skill and attention;
- the **environmental context** in which performance takes place.

They use a global framing in which mental workload concerns the **attentional resources required to meet objective and subjective performance criteria**, with the level of required resources influenced by task demands, external support and past experience.

This Young et al. framework is the **governing definition for this BEP**.

---

# 2. Project interpretation

For this project, workload should therefore be understood as the amount of attentional/cognitive resources the operational buyer must mobilize to perform purchasing work to the required standard, in interaction with:

1. **Task demands** — complexity, information volume, number of simultaneous demands, uncertainty, exception handling and required performance;
2. **Operator characteristics** — experience, skill, familiarity, attention and the degree to which processing is automatic versus controlled;
3. **Context and support** — interruptions, colleagues, technological support, system usability and other environmental conditions.

This means the same task can impose different workload on different people or under different conditions.

It also means a task that takes only a few seconds can still have high mental workload if it requires concentrated judgement or expert recognition. Conversely, a long repetitive task can consume substantial operational time while requiring relatively little cognitive effort.

---

# 3. What workload is NOT in this project

The project must **not** define total workload as:

`workload = frequency × processing time`

That calculation can be useful, but only as an estimate of **operational effort volume** for comparable task categories.

Therefore:

- **active processing time** measures direct hands-on effort;
- **elapsed time** captures the total case duration, including waiting and task switching;
- **frequency** captures exposure to the task;
- **manual actions / line counts / rework** help quantify process burden;
- **judgement, uncertainty, attention, interruptions and experience dependence** help interpret mental workload according to Young et al.

Time and frequency are indicators, not the theoretical definition of workload.

---

# 4. Measurement implications

For relevant observed cases, record where practical:

`Task | Trigger | Order type | # lines | Active time | Elapsed time | Manual actions | Rework | Interruption/task switch | Judgement required | Uncertainty/exception | Experience/tacit knowledge needed | Output`

The following should be considered when interpreting workload:

| Young et al. dimension | Purchasing indicators |
|---|---|
| **Task characteristics** | complexity, # lines, information sources, uncertainty, exceptions, concurrent demands, verification requirements |
| **Operator characteristics** | experience dependence, tacit knowledge, familiarity, automatic vs controlled processing |
| **Environmental context/support** | interruptions, colleague support, Exact/Orbis support, Outlook/task switching, availability of information |
| **Attentional-resource requirement** | judgement required, sustained checking, memory/attention demand, decision difficulty |
| **Performance criterion** | correct PO, correct quantity/price, correct allocation, no duplicate demand, timely order, correct confirmation handling |

For judgement-heavy activities, it is more useful to record **decision + cues + reason** than to attempt to time invisible cognitive operations to the second.

---

# 5. Operational effort versus mental workload

The BEP can report two related but distinct forms of evidence.

## Operational effort / process burden

Examples:

- task frequency;
- active processing time;
- elapsed time;
- number of PO lines/documents checked;
- manual entries/actions;
- rework frequency/time;
- hand-offs;
- interruptions/task switching.

A useful prioritization estimate is:

`operational effort volume = frequency × representative active processing time`

This is useful for identifying large time-consuming task categories, but it is **not a complete workload score**.

## Mental workload

Interpret using the Young et al. framework:

- how much attention/judgement is required;
- how difficult/complex the task is;
- how much expertise changes the task demand;
- whether interruptions or insufficient support increase required resources;
- whether the buyer is near underload/optimal load/overload conditions where relevant.

Unless a validated combined scoring method is introduced later, these heterogeneous indicators should **not be arbitrarily merged into one numerical workload index**.

---

# 6. Use in DMAIC

## Define

Frame the problem as reducing meaningful buyer workload, not merely reducing minutes.

## Measure

Collect observable process-effort measures while also capturing task, operator and contextual factors that shape mental workload.

## Analyze

Identify whether workload is driven mainly by:

- repetitive administration;
- verification/comparison;
- expert judgement;
- rework/information problems;
- interruptions/task switching;
- insufficient or poorly designed system support.

## Improve

A solution should reduce resource demand or unnecessary effort without simply transferring workload to another step or creating new monitoring/exception burden.

## Control

KPIs should match the selected intervention. Processing time may be one KPI, but claims of mental-workload reduction require evidence consistent with the Young et al. framework.

---

# 7. Supporting literature

**Longo, L., Wickens, C. D., Hancock, G., & Hancock, P. A. (2022).** *Human mental workload: A survey and a novel inclusive definition*. *Frontiers in Psychology, 13*, 883321.

Longo et al. may be used later to support measurement/operationalization choices, but it is **not the governing workload definition in this BEP**.

**Hart, S. G. (2006).** *NASA-Task Load Index (NASA-TLX); 20 years later* may become relevant if a validated subjective mental-workload measure is needed. Its possible use does not change the Young et al. definition.