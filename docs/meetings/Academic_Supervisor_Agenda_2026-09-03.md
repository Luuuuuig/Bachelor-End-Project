# Academic Supervisor Meeting Agenda — 3 September 2026

**Time:** 15:00–16:00  
**Student:** Yijie Wang  
**Supervisor:** Zhongxin Hu  
**Project:** Reduce Operational Purchasing Workload at Hytech-Pommec using AI

## Meeting objective

Review progress since the 25 August supervision meeting, validate the current Measure approach, clarify the intended baseline-observation coverage, and confirm the next steps toward Analyze and the Plan of Work.

## 1. Progress since the previous meeting — 5 min

- Completed the live Measure pilot on 28 August.
- Started the official exploratory baseline:
  - 31 August: 165 minutes net observed time.
  - 1 September: 186 minutes net observed time.
  - Current official baseline total: **351 net observed minutes (5 h 51 min)** across two partial observation days; after the OBS-05 correction, **265 timed coded-active minutes**. These are different quantities.
- Measurement Protocol v1.2 is now the controlled protocol for subsequent observations.
- Updated the AS-IS process understanding:
  - external/email request handling and Exact/PO work are parallel work streams rather than one mandatory sequence;
  - when there is no open PO and no external request currently requiring attention, the buyer generates the next PO record from Exact demand;
  - a newly generated PO appears as `Besteld` in Exact and then becomes open PO work;
  - `Besteld` is treated as an Exact system status, not as proof that the PO has already been forwarded to the supplier;
  - after maximalisatie, the resulting order can still be either held or allowed to proceed, regardless of whether additional demand was added.

**Discussion:** Is this level of AS-IS detail sufficient for continuing Measure, with remaining operational details validated during observation/buyer clarification rather than delaying the baseline?

## 2. Measurement Protocol v1.2 — methodological validation — 10 min

The pilot showed that directly coding the full detailed task register live was too granular for one observer. The current two-level design therefore uses:

- broad activity families during live observation;
- `DEC?` as an attribute when judgement is embedded in another observable activity;
- case context recorded separately;
- post-session Task-ID enrichment only where the evidence supports it;
- explicit uncertainty rather than reconstructing missing detail.

**Questions for supervisor:**

1. Is this two-level measurement architecture academically defensible for the exploratory Measure phase?
2. Is post-session Task-ID enrichment acceptable when the original live observation record is preserved?
3. Are there additional reliability/validity checks that should be added before collecting substantially more baseline data?

## 3. Workload construct and operationalization — 10 min

Current framing:

- broad/occupational workload: amount and difficulty of work;
- quantitative burden: frequency, active processing time, volume and rework;
- organizational constraints: interruptions, missing information and system/process obstacles;
- mental workload: treated as a specific component rather than equated with processing time;
- expertise dependence: kept separate from mental workload.

The live sheet does not directly quantify mental workload. A validated activity-specific instrument such as NASA-TLX remains an option later if the selected focal activity requires it.

**Questions for supervisor:**

1. Does this layered workload framework address the concern from the previous meeting about defining and measuring workload clearly?
2. Is it acceptable to use objective/observational workload indicators during exploratory Measure and only add a subjective mental-workload instrument later if it is needed for the selected focal activity?

## 4. Baseline coverage: operationalize the five-working-day guidance — 10 min

The student's recollection is that the academic advisor specifically indicated that approximately **five working days should be sufficient**. The 25 August written notes currently describe five days as student-proposed and not finalized. Preserve that historical note and resolve the evidence discrepancy explicitly in this meeting's decision log.

The later idea of **40 net observed hours** is a separate, stricter student interpretation. Five scheduled working days normally include breaks and unavailable/non-observed periods, so five days must not be converted automatically into 40 net hours.

Current coverage is 351 net observed minutes across two partial days; these partial windows contribute evidence but are not silently treated as two full-day equivalents.

**Confirmation requested:**

1. Confirm five distinct working days with meaningful coverage as the planning minimum, rather than 40 net hours.
2. Confirm that actual windows, breaks/unavailable time and net minutes should be reported separately.
3. Confirm the proposed Day-5 extension rule: continue only for a documented abnormal day, missing daypart, material measurement failure, missing recurring work pattern, or materially new recurring pattern on the final day.

## 5. Measure → Analyze and focal-case selection — 10 min

Planned sequence:

1. Complete the exploratory workload baseline.
2. Build an activity-family workload profile using frequency, active time, rework, interruptions, qualitative difficulty and expertise evidence.
3. Identify the strongest candidate activities.
4. Only then perform targeted Exact/Orbis/data/technical feasibility for the shortlisted candidates.
5. Select one focal activity based on workload contribution, business relevance, standardizability, quality risk, expertise dependence, technical feasibility and evaluation feasibility.

**Questions for supervisor:**

1. Is this sequence appropriate, especially deferring detailed technical feasibility until after the workload baseline?
2. What level of quantitative Measure evidence would be sufficient before selecting the focal activity?
3. Confirm a two-stage selection method: non-compensable AI/data/ground-truth/risk/time veto gates, followed by anchored weighted scoring.
4. Confirm that literature/theory should justify criteria and method, while the buyer/company stakeholders set local trade-off weights and the academic supervisor validates them.
5. Confirm the proposed sensitivity check before declaring one winner.

## 6. 1BEPIEX feedback and project framing — 7 min

Review the intended revisions based on the supervisor's comments:

- keep the problem description focused on observed/current-state evidence;
- avoid putting Analyze-phase conclusions into the problem description;
- maintain a clear logical transition from practical problem → workload measurement → focal solution;
- retain the current RQ/SQ direction focused on workload reduction and quality.

**Discussion:** Confirm that the company expects a meaningful AI-supported focal artifact; conventional automation/process redesign may support it or remain recommendations. If no candidate passes the responsible-AI/data/quality/evaluation gates, confirm that any non-AI focal artifact requires explicit company and academic approval.

## 7. Plan of Work and planning milestones — 5 min

Known milestones:

- **15 September:** half-page project description for identifying the second supervisor.
- **20 September:** Plan of Work draft for feedback.
- **27 September:** final Plan of Work submission.

**Discussion:**

- Confirm whether the current DMAIC → DSRM sequence and Gantt are suitable for the Plan of Work.
- The attached template requires a prospective method and detailed Gantt, but does not state that the focal use case must already be selected. Confirm that a post-submission focal-case gate is acceptable when the candidate set, veto/score method, fallback and evaluation-freeze milestone are predefined.
- Confirm that the focal-case workload endpoint and quality guardrail will be frozen before artifact development/formal testing.
- Confirm the submission package includes the template's Part C five professional-skill reflections and Part D scientific-conduct declaration, in addition to the proposal and Gantt.
- Confirm that DMAIC is the overarching improvement structure, while specific Lean Six Sigma tools are selected only when relevant rather than applied mechanically.

## 8. Decisions / next actions — 3 min

Before closing, record agreement on:

- Measurement Protocol v1.2;
- workload operationalization;
- baseline target/coverage rule;
- Measure → Analyze gate;
- AI requirement and no-feasible-AI escalation rule;
- candidate-selection matrix/weighting owner;
- workload endpoint and quality-guardrail freeze;
- any required changes to the 1BEPIEX / Plan of Work;
- activities to complete before the next supervision meeting.

## Useful repository references

- Current AS-IS process: `../process/Process_Cleaned_V1.5.md`
- Current Measure protocol: `../measurement/Measurement_Protocol_v1.3.md`
- 31 August baseline: `../measurement/Measure_Observation_2026-08-31.md`
- 1 September baseline: `../measurement/Measure_Observation_2026-09-01.md`
- Workload definition: `../methodology/Workload_Definition.md`
- Current methodology/case-selection logic: `../methodology/Phase_1_Current_Methodology.md`
- Project timeline/Gantt: `../Project_Timeline.md`
