# Academic Supervisor Meeting Agenda — 3 September 2026

**Time:** 15:00–16:00  
**Student:** Yijie Wang  
**Supervisor:** Zhongxin Hu  
**Project:** Reduce Operational Purchasing Workload at Hytech-Pommec using AI

## Meeting objective

Review the work completed since last week's meeting, validate the workload definition and Measurement Protocol, and confirm that the project and observation stopping rule are on the right track.

## 1. Review what has been added since last week — 10 min

### Main additions and corrections

- The current AS-IS workflow has been synchronized with the latest observations:
  - after maximalisatie, either HOLD or ORD can follow, whether or not additional demand was added.
- The Measure pilot was completed on 28 August.
- Two official observation sessions were completed:
  - 31 August: 165 net observed minutes; 103 timed coded-active minutes.
  - 1 September: 186 net observed minutes; 162 timed coded-active minutes.
  - Combined: **351 net observed minutes** and **265 timed coded-active minutes**.
- **OBS-04 SEND** and **OBS-05 EXC** were confirmed as genuine sub-minute actions. They are retained as untimed tally occurrences; no duration is invented.
- Measurement Protocol v1.3 and its live cheat sheet were created.
- The workload definition, candidate-selection structure and later evaluation logic were clarified.
- The supervisor-approved RQ/SQ wording and order were synchronized across the current project-definition documents.
- The Gantt was updated with Plan of Work, ILBEP, final-report, presentation and assessment deadlines.

### Question for the supervisor

Are any of these additions, corrections or interpretations inconsistent with what we agreed last week?

## 2. Workload definition: which literature is used and why — 12 min

### Primary definition

The primary conceptual source is:

**Bowling, N. A., & Kirkendall, C. (2012). _Workload: A review of causes, consequences, and potential interventions._**

This source is used because it treats workload as involving both:

- the **amount of work**; and
- the **difficulty of work**.

That distinction fits this BEP better than defining workload as processing time alone. Operational purchasing contains repetitive volume and active handling time, but also clarification, exceptions, judgement, uncertainty, task switching and expertise-dependent work.

### Supporting sources

- **Spector and Jex (1998):** supports the distinction between quantitative workload and organizational constraints such as interruptions.
- **Young et al. (2015):** supports treating mental workload as multidimensional and as one component of the broader workload construct, rather than assuming that duration directly represents mental workload.

### Current interpretation

The project therefore does **not** create one arbitrary “total workload score.” It reports several defensible indicators:

- frequency and volume;
- active processing time;
- rework and exception work;
- interruptions and task switching;
- qualitative evidence of difficulty, judgement and expertise.

### Questions for the supervisor

1. Is Bowling and Kirkendall (2012) suitable as the primary umbrella definition for workload in this BEP?
2. Is the distinction between amount, difficulty, mental workload, organizational constraints and expertise sufficiently clear?
3. Should another source or construct be added before the Plan of Work is finalized?

## 3. Review the Measurement Protocol and explain what it captures — 23 min

### Purpose of the protocol

The protocol is designed to answer the exploratory Measure question:

> Which parts of the operational purchasing workflow contribute most to the operational buyer's observable workload, and which activities should be investigated further as possible AI-support candidates?

### Construct-to-measurement mapping

| What we need to understand | What the protocol records | How it is interpreted |
|---|---|---|
| Amount and recurrence of work | Activity occurrences, case IDs, line/item volume and net observed time | Occurrences per observed hour and activity distribution |
| Operational effort | Reliable start/end times for active work episodes | Active processing-time distribution; not total workload by itself |
| Rework, clarification and exceptions | CLAR/EXC codes, recurrence, active time and short cause/result notes | Where avoidable workload and process friction occur |
| Interruptions and task switching | INT count and segmentation when the buyer leaves and resumes work | Organizational constraint/interruption rate |
| Judgement and expertise | DEC?, J and EXP markers supported by an observed action or explanation | Qualitative evidence; not converted into invented minutes or points |
| Case and channel context | OBS case ID, Origin, Channel, result and relevant notes | Identifies whether patterns differ by request source or case type |
| Observation coverage | Date, daypart, session start/end, breaks, observer-unavailable time and net minutes | Shows what was and was not covered; prevents false full-day claims |
| Measurement quality | Protocol version, timed-versus-tally status, MISS/Unknown conventions, mapping confidence and recoding checks | Makes uncertainty and comparability auditable |

### Important timing rule

- Meaningful active episodes are timed.
- Extremely fast but genuine actions, such as OBS-04 SEND and OBS-05 EXC, are recorded as **tallies without fabricated duration**.
- Net observed time and timed coded-active time remain separate.

### What the protocol can answer

- which activity families occur most often;
- where reliable active handling time is concentrated;
- where clarification, exceptions, rework and interruptions occur;
- where observable judgement or expertise appears;
- which activities deserve deeper Analyze-phase investigation.

### What the protocol cannot answer by itself

- whether an AI artifact causally reduces workload;
- whether purchasing outcome quality is maintained;
- a validated psychometric score for mental workload;
- whether five days or 40 hours are sufficient without checking coverage.

Those questions require a later focal-activity baseline and a separate manual-versus-AI evaluation protocol.

### Questions for the supervisor

1. Does this construct-to-measurement mapping capture the workload dimensions needed for SQ1 and focal-case screening?
2. Are any important observable indicators missing or unnecessary?
3. Is tally-only recording acceptable for genuine sub-minute actions whose duration cannot be measured reliably?
4. Is the two-level design defensible: broad live activity coding followed by evidence-supported Task-ID enrichment?
5. Should a validated mental-workload instrument be considered only after the focal activity is selected?

## 4. Confirm that the project is on the right track and decide the observation target — 15 min

### Current position

- Define is largely complete.
- Measure is in progress.
- Analyze should begin only after the observation evidence and coverage are sufficient.
- The current protocol uses **five distinct working days plus a Day-5 coverage review** as the planned minimum.

### Student's current preference

Count 31 August and 1 September as **Day 1 and Day 2** because they are separate working days. Continue to report their actual observation windows and net minutes, without presenting either as a full eight-hour day.

After the fifth distinct day, check whether morning/afternoon periods, recurring activities and important request channels are sufficiently covered. If a material gap or a new recurring pattern remains, add a targeted observation block or day.

### Decision question

**Does the supervisor think the stopping rule should remain five distinct working days with a coverage review, switch to a minimum of 40 net observed hours, or combine both requirements?**

### Clarifications to record

1. Do the two completed partial sessions count as two of the five distinct working days?
2. If 40 hours is preferred, does “40 hours” mean net observable working time after breaks and observer-unavailable periods?
3. Is one buyer sufficient for this case study, or is additional buyer coverage expected?
4. Which dayparts, activity families or request channels must be covered before Measure can close?
5. What evidence should trigger an extension beyond the minimum?

### Final overall question

Based on the current AS-IS model, workload definition, observations and Measurement Protocol, are we on the right track to continue Measure and then proceed to Analyze?

## Decision record

| Decision | Supervisor conclusion | Follow-up action |
|---|---|---|
| Work added since last week is correctly interpreted |  |  |
| Workload definition and literature are appropriate |  |  |
| Measurement Protocol captures the intended constructs |  |  |
| Partial sessions count as Day 1 and Day 2 |  |  |
| Final stopping rule: 5 days / 40 net hours / combined |  |  |
| Additional coverage required before Analyze |  |  |
| Overall project direction is on track |  |  |

## Pre-read repository references

- Current workload definition: ../methodology/Workload_Definition.md
- Current Measurement Protocol: ../measurement/Measurement_Protocol_v1.3.md
- Live observation cheat sheet: ../measurement/Measure_Live_Cheat_Sheet_v1.3.md
- Current AS-IS process: ../process/Process_Cleaned_V1.5.md
- 31 August observation: ../measurement/Measure_Observation_2026-08-31.md
- 1 September observation: ../measurement/Measure_Observation_2026-09-01.md
- Literature register: ../../literature/README.md
- Project timeline/Gantt: ../Project_Timeline.md

