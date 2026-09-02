# Academic Supervisor Meeting Agenda — 3 September 2026

**Time:** 15:00–16:00  
**Student:** Yijie Wang  
**Supervisor:** Zhongxin Hu  
**Project:** Reduce Operational Purchasing Workload at Hytech-Pommec using AI

## Meeting outcome

Leave the meeting with four decisions recorded in the meeting notes. These are the items that currently determine whether Measure can close cleanly and whether the later evaluation can answer the main research question.

### Must decide today

1. Approve Measurement Protocol v1.3 as the exploratory Measure architecture and decide how the five-day coverage rule treats the two completed partial days.
2. Approve the exact RQ/SQ wording and the contingency if no responsible, feasible and evaluable AI candidate passes the gates.
3. Approve the candidate-selection method and ownership of gates, scoring anchors and weights.
4. Approve the Plan-of-Work sequencing and the rule that the focal evaluation protocol is frozen before artifact development and formal testing.

## 0. Progress and source corrections — 5 min

- Pilot completed on 28 August.
- Official exploratory baseline so far:
  - 31 August: 165 net observed minutes and 103 timed coded-active minutes.
  - 1 September: 186 net observed minutes and 162 timed coded-active minutes.
  - Combined: **351 net observed minutes** and **265 timed coded-active minutes**. These quantities must remain separate.
- Measurement Protocol v1.3 is internally controlled from 2 September; v1.2 remains the historical protocol for 1 September.
- Source verification confirms that both **OBS-04 SEND** and **OBS-05 EXC** on 31 August were genuine sub-minute actions. They are retained as untimed tally occurrences and do not change the 103-minute or 265-minute totals.
- Current AS-IS rule: after maximalisatie, HOLD or ORD can follow whether or not additional demand was added.

## 1. Must decide: protocol validity and baseline coverage — 15 min

The protocol is intended to characterize the current process and screen for recurring workload hotspots. It measures activity-family occurrence, reliable active time, case context, interruptions, clarification, exception/rework and supported judgement/expertise cues. It does **not** by itself estimate the effect of an AI artifact or prove that purchasing outcome quality is preserved.

### Decision questions

1. Is the two-level architecture—broad live coding plus evidence-supported post-session Task-ID enrichment—academically defensible for exploratory Measure?
2. Is the intended research architecture correct: exploratory Measure selects the focal case, followed by a separate activity-specific manual-versus-AI evaluation protocol?
3. Do 31 August and 1 September count as two of the five distinct observation days when their combined coverage contributes both dayparts, or are five substantially covered days required?
4. Confirm five distinct days plus the Day-5 coverage review as the planning rule, rather than converting five working days into 40 net observed hours.
5. Confirm the extension triggers: abnormal day, missing daypart, material measurement failure, missing recurring pattern, or a materially new recurring pattern on the final day.
6. Confirm the reliability checks: delayed same-observer recoding of a sample, targeted buyer validation of ambiguous mappings, and explicit uncertainty rather than reconstruction.
7. Confirm the analysis table records protocol version, timed-versus-tally status, occurrence inclusion, mapping confidence and Unknown conventions.

## 2. Must decide: RQ/SQ wording and AI contingency — 12 min

### Proposed main research question

**To what extent can an AI-supported artifact reduce operational buyer workload at Hytech-Pommec without reducing purchasing outcome quality?**

### Proposed subquestion order

1. Which current purchasing activities contribute most to observable operational buyer workload?
2. Which recurring activity is most suitable for responsible and feasible AI support?
3. To what extent does the selected artifact reduce active human handling time while meeting the predeclared purchasing-quality guardrail?
4. Which implementation controls and human-oversight arrangements are required for responsible use?

### Decision questions

1. Approve the exact RQ and SQ order.
2. Confirm that the company expectation makes an AI-supported artifact the intended intervention.
3. Confirm the predeclared contingency: if no candidate passes the non-compensable gates, test bounded redesigns where sensible, report the failed gates as a feasibility finding, and obtain an explicit scope decision before replacing the AI-supported focal artifact.
4. Confirm that this contingency belongs in the thesis methodology; it becomes a substantive result only if it is triggered.

## 3. Must decide: focal-case selection and ownership — 10 min

Proposed method:

1. Apply non-compensable veto gates first: responsible-use boundary, usable data, ground truth/quality benchmark, technical access, evaluation feasibility and remaining project time.
2. Score only candidates that pass all gates using predeclared criteria and anchored 1–5 scales.
3. Agree criteria, anchors, plausible weight ranges and final weights before aggregate scores are calculated.
4. Perform sensitivity analysis before declaring a robust winner.

### Decision questions

1. Confirm that the student and academic supervisor own the academic criteria, anchors, ranges and weights.
2. Confirm that the company supervisor validates operational evidence, access, constraints and feasibility rather than owning the academic weights.
3. Confirm that literature justifies the structure and criteria, while project-specific weights are transparently agreed for this case rather than presented as universal values.

## 4. Must decide: evaluation logic, Plan of Work and Gantt — 13 min

### Proposed success logic

- Primary endpoint: total active human handling time per comparable eligible case or line, including AI review, correction and required documentation.
- Quality guardrail: evaluate the final human-approved outcome against a frozen rubric and trusted reference; separately report raw AI errors, critical/minor errors, overrides, correction time and review burden.
- Freeze before development/formal testing: eligible cases, manual comparator, unit of analysis, rubric, adjudication, critical-error definition, meaningful workload threshold Δ, acceptable quality margin δ, sampling/matching and analysis plan.
- Default rule: zero observed critical errors; any non-zero minor-error margin requires explicit process-owner acceptance and academic validation.

### Planning questions

1. Confirm that the evaluation protocol freeze must precede artifact design/prototype testing.
2. Confirm that the Plan of Work can be submitted before final focal-case selection when the candidate population, gates, scoring method, contingency and later evaluation freeze are predefined.
3. Confirm the known milestones: 15 September description, 20 September official draft and 27 September official final submission, with internal complete-draft targets on 18 and 25 September.
4. Confirm Part C reflections and Part D scientific-conduct declaration/signing logistics.
5. Record the official final BEP submission/presentation date if it differs from the 7 January company-placement boundary.

## 5. Decisions, owners and next actions — 5 min

For every decision, record:

| Decision/action | Owner | Due date | Evidence/file to update |
|---|---|---|---|
| Protocol and partial-day interpretation |  |  |  |
| Final RQ/SQ and AI contingency |  |  |  |
| Selection model and weights process |  |  |  |
| Evaluation freeze and PoW sequence |  |  |  |
| Next Measure sessions / coverage gaps |  |  |  |

## Written follow-up if time runs out

- Whether NASA-TLX is warranted for the selected focal task.
- Detailed Exact/Orbis interface questions.
- Whether FMEA is useful for the selected solution.
- Lower-priority wording and formatting issues.

## Pre-read repository references

- Current AS-IS process: ../process/Process_Cleaned_V1.5.md
- Current Measure protocol: ../measurement/Measurement_Protocol_v1.3.md
- 31 August baseline: ../measurement/Measure_Observation_2026-08-31.md
- 1 September baseline: ../measurement/Measure_Observation_2026-09-01.md
- Workload definition: ../methodology/Workload_Definition.md
- Methodology and case-selection logic: ../methodology/Phase_1_Current_Methodology.md
- Project timeline/Gantt: ../Project_Timeline.md
