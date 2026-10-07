# Measurement Protocol v1.0 — Exploratory Measure Phase

**Status:** Developed 26 August 2026; ready for pilot validation before full baseline collection.

**Purpose:** This protocol defines how workload-related evidence will be collected during shadowing of the operational buyer at Hytech-Pommec. It is designed for the broad exploratory Measure phase, before one focal purchasing activity is selected for deeper analysis and artifact evaluation.

**Current sequencing decision:** the live-observation pilot and baseline come first. Detailed Exact/Orbis production-data/interface feasibility work is intentionally deferred until the exploratory Measure phase is complete and the evidence justifies which candidate(s) deserve deeper Analyze-phase technical investigation.

**Related files:**

- Workload construct: `../methodology/Workload_Definition.md`
- Current research methodology and candidate selection: `../methodology/Phase_1_Current_Methodology.md`
- Current 31-task AS-IS register: `../process/Process_Cleaned_V1.5.md`
- Project control summary: `../Project_Charter.md`

---

# 1. What this protocol measures

The protocol does **not** attempt to create one total workload score. The workload definition used in this BEP distinguishes between the amount of work, the difficulty of work, mental workload, expertise dependence and organizational constraints.

The observation protocol therefore measures a **multidimensional workload profile**.

| Dimension | Observable indicator in this protocol | Why it is measured |
|---|---|---|
| **Quantitative workload — frequency** | number of times each Task ID occurs | A short task can still consume substantial capacity if it occurs very often. |
| **Quantitative workload — processing time** | active processing time for meaningful work episodes | Estimates how much buyer capacity the activity actually consumes. |
| **Work volume / case size** | lines, items or comparable transaction volume where relevant | Allows processing time to be interpreted in relation to the amount of work in the case. |
| **Rework burden** | rework occurrence and active rework time | Rework represents additional work and can also indicate a process/quality problem. |
| **Organizational constraints** | interruptions/task switches, missing information, system problems | These conditions can interfere with task performance and fragment the buyer's work. |
| **Qualitative workload / difficulty evidence** | exceptions, uncertainty, investigation, problem solving and short decision notes | Some important purchasing activities are difficult even when they take little time. |
| **Expertise dependence** | tacit/undocumented cues, historical knowledge or experience-based recognition | Expertise dependence is important for deciding what can be standardized, automated, supported or retained by the buyer. |

**Mental workload is not directly quantified by this live observation sheet.** If mental workload becomes important for the selected focal activity, a validated subjective instrument such as NASA-TLX may be considered later for the activity-specific evaluation.

---

# 2. Why workload is measured this way

The broad project-level workload construct follows the distinction between the **amount of work** and the **difficulty of work** discussed by Bowling and Kirkendall (2012). Quantitative workload is therefore not reduced to processing time alone: task frequency and case volume also matter.

Spector and Jex (1998) provide useful conceptual distinctions between quantitative workload and organizational constraints. In this project, interruptions, missing information and system limitations are therefore recorded as contextual constraints rather than simply added to a workload score.

Young et al. (2015) are used specifically for **mental workload**. Their work supports the decision not to interpret duration as a direct measure of cognitive demand. A task can be fast but cognitively demanding, while a long repetitive task can consume substantial capacity with relatively little mental demand.

For this reason, the Measure phase combines observable quantitative indicators with qualitative evidence and does **not** aggregate minutes, interruptions, judgement and rework into an unvalidated composite workload equation.

---

# 3. Primary live observation sheet

Use one row per meaningful work episode.

`Case ID | Task ID | Start | End | Volume | INT | Result / short note`

| Field | Operational definition | What it provides |
|---|---|---|
| **Case ID** | Use an anonymized observation/case ID such as `OBS-01` by default. A production PO number may be retained only in the restricted raw working sheet when company permission and storage rules allow it. | Links multiple work episodes belonging to the same case without requiring commercial identifiers in the research repository. |
| **Task ID** | Current task number from the 31-task AS-IS register. If uncertain, write the task name and assign the ID afterward. | Enables frequency and task-level workload analysis. |
| **Start / End** | Clock time for a meaningful active work segment. Leave blank for tally-only activities. | Used to calculate active processing time. |
| **Volume** | Relevant case quantity, usually number of lines/items, e.g. `12L` | Supports case-size and time-per-line analysis where meaningful. |
| **INT** | Number of observable interruptions/task switches during the episode | Describes fragmentation and organizational constraints. |
| **Result / short note** | Short outcome, deviation, rework type, exception or decision cue | Preserves information that cannot reliably be reconstructed later. |

### Example rows

```text
OBS-01 | 7     | —     | —     | —   | 0 | HOLD
OBS-02 | 8-10  | 09:21 | 09:27 | 3L  | 0 | MAX found
OBS-03 | 15-16 | 10:03 | 10:12 | 14L | 1 | 2D
OBS-04 | 26-27 | 10:42 | 10:57 | 22L | 0 | 4D
OBS-05 | 30    | 11:12 | 11:24 | —   | 1 | FIN price issue
```

Suggested shorthand:

- `L` = lines
- `D` = deviations
- `ORD` = order now
- `HOLD` = hold
- `MAX` = maximalisatie
- `HP` = historical PO search
- `J` = judgement / experience cue
- `MI` = missing information
- `FIN` = Finance rework
- `MISS` = observable activity occurred but could not be fully coded live

---

# 4. Active processing time versus elapsed time

## 4.1 Primary metric: active processing time

The primary time metric for workload analysis is **active processing time**: the time during which the buyer is actually working on the purchasing activity.

A raw `Start → End` interval only represents active processing time when the buyer remains on that activity. If an unrelated interruption or task switch clearly takes the buyer away from the current work, the current segment is paused/closed and a new segment is recorded when the buyer returns.

Example:

```text
OBS-03 | 26 | 10:00 | 10:06 | 10L | 0 | confirmation check
OBS-03 | 26 | 10:11 | 10:15 | 10L | 0 | resumed
```

Active processing time:

`6 + 4 = 10 minutes`

Overall elapsed clock time from first start to final end:

`15 minutes`

The BEP uses the **10 minutes active processing time** as the main buyer-capacity measure.

## 4.2 Brief interruptions

A brief interruption can remain inside the current segment when the buyer does not meaningfully leave the task—for example a very short exchange or notification that does not create a separate work episode. Record it in `INT` rather than trying to stopwatch seconds.

## 4.3 Substantial interruptions or task switches

Close/pause the current episode whenever the buyer clearly switches to a different work activity, conversation or case such that leaving the clock running would materially overstate active work on the original task. The pilot should test whether this behavioural rule is sufficiently reproducible; do not invent a second-level threshold unless the pilot shows that one is necessary.

## 4.4 Elapsed time

Elapsed time may still be useful when lead time, waiting or process delay becomes analytically important, but it is kept separate from active processing time.

Existing Week-1 observations in the AS-IS file are mainly **single-case elapsed-time observations** and should not be re-labelled as active processing time.

---

# 5. TIME, TALLY, TIME IF and SYSTEM rules

### TIME

Record `Start` and `End` because duration is meaningful and observable.

Typical examples: manual data entry, verification/comparison, historical investigation, price checking, PO preparation, Finance rework.

### TALLY

Record that the activity occurred, but do not force a duration.

One row = one occurrence.

Typical examples: fast branch decisions such as ready-to-order versus hold, or whether useful consolidation exists.

Tallying is used because a decision may occur in seconds and artificial stopwatch precision would not meaningfully represent its difficulty or expertise requirement.

### TIME IF

Record time only when the activity becomes a clearly observable work episode. If it is effectively instantaneous, record it as an occurrence instead.

### SYSTEM

System/external events are not normally treated as buyer active workload. They may still be tallied when they define case flow or trigger buyer work.

---

# 6. Current 31-task live measurement guide

The IDs below are synchronized with `Process_Cleaned_V1.5.md`.

## A. Request and validation

| ID | Short task | Measurement rule |
|---:|---|---|
| 1 | Identify purchasing need / route | **TALLY** |
| 2 | Create purchasing entry / PO lines | **TIME** |
| 3 | Transfer email/screenshot/request information into Exact | **TIME IF**; may combine with `2-3` |
| 4 | Validate supplied information | **TALLY**; note issue if present |
| 5 | Search historical POs / investigate suspicious information | **TIME** |

## B. Order / hold / maximalisatie

| ID | Short task | Measurement rule |
|---:|---|---|
| 6 | Assess stock, demand, open POs, receipts, lead time and urgency | **TIME IF** clearly observable |
| 7 | Determine small/non-urgent versus ready to proceed | **TALLY** + outcome |
| 8 | Search same-supplier demand for maximalisatie | **TIME** |
| 9 | Determine whether useful consolidation exists | **TALLY** + Yes/No |
| 10 | Combine same-supplier demand | **TIME** |
| 11 | Hold/pause requirement | **TALLY** |

## C. Exact Advies / Toewijzen

| ID | Short task | Measurement rule |
|---:|---|---|
| 12 | Review Exact `Advies` / underlying demand | **TIME IF** |
| 13 | `Toewijzen` to project/production demand | **TIME IF** |

If they are performed as one inseparable episode, record `12-13`.

## D. Pre-PO price control

| ID | Short task | Measurement rule |
|---:|---|---|
| 14 | Decide whether pre-PO price check is required | **TALLY** |
| 15 | Search supplier price and compare with Exact | **TIME** |
| 16 | Update outdated/deviating pre-PO price | **TIME** or combine as `15-16` |

## E. Prepare and authorize PO

| ID | Short task | Measurement rule |
|---:|---|---|
| 17 | Prepare / complete supplier PO | **TIME** |
| 18 | Check buyer authorization | **TALLY** |
| 19 | `Fiatteren` / `Verrichten` within authority | **TALLY** unless measurable effort becomes material |
| 20 | Route above-authority PO to approver | **TIME IF** |
| 21 | Continue workflow after higher-authority `Fiatteren` | **TIME IF** |

## F. Send PO

| ID | Short task | Measurement rule |
|---:|---|---|
| 22 | Exact generates PO and emails buyer | **SYSTEM** |
| 23 | Buyer forwards PO with standard supplier message | **TIME** |
| 24 | PO reaches practical `Besteld` stage | **SYSTEM** |

## G. Supplier confirmation

| ID | Short task | Measurement rule |
|---:|---|---|
| 25 | Supplier confirmation received | **TALLY / external trigger** |
| 26 | Compare confirmation with PO / Exact | **TIME** |
| 27 | Correct confirmation deviations | **TIME** or combine as `26-27` |
| 28 | Attach/archive confirmation + `Bevestigd` | **TIME IF** |

## H. Rework and exceptions

| ID | Short task | Measurement rule |
|---:|---|---|
| 29 | Finance performs later control | **SYSTEM / other actor** |
| 30 | Buyer investigates Finance-returned issue | **TIME** |
| 31 | Handle unavailable-component exception | **TIME IF** investigation occurs |

---

# 7. Rules for ambiguous or combined tasks

1. **Never guess a Task ID.** If the exact ID cannot be recalled live, write a short task name and code it afterward.
2. If several tasks are performed as one inseparable episode, record an ID range such as `15-16` or `26-27` rather than inventing a split.
3. Do not record every click or screen navigation as a separate task. The unit of observation is a **meaningful work episode**.
4. Do not force timing on invisible cognition. For fast judgement, record the occurrence, outcome and relevant cue where visible or elicited.
5. If a judgement turns into an observable investigation, time the investigation episode.
6. If work is observed but the observer cannot code it without falling behind, record `MISS` with a short note and reconstruct only what can be supported afterward. Do not fabricate missing timing or Task IDs.

---

# 8. Sampling and observation-window rules

The exploratory baseline should describe **normal work exposure**, not only interesting cases.

1. During a selected observation window, record all observable operational-purchasing episodes that can be captured without disrupting the buyer; do not selectively follow only candidate activities.
2. Record the start/end of each observation window and total observed hours so task frequencies have a clear denominator.
3. The baseline should cover **multiple working days and different dayparts**, including both relatively quiet periods and periods with normal interruption/task-switching exposure where feasible.
4. A roughly five-working-day baseline was discussed as a possible student proposal with the supervisor, but it is **not yet treated as a fixed validated sample size**. The final baseline window will be frozen after the pilot based on feasibility, coverage and supervisor alignment.
5. Do not extrapolate a short block directly to a full day/week unless the coverage is demonstrably adequate.
6. Keep a simple missed-observation count (`MISS`) when workload is too fast to code fully. A high missed-event rate is a pilot failure signal and should trigger simplification before baseline freeze.
7. Once the baseline version is frozen, do not silently change coding rules. Any necessary deviation must be dated and documented.

---

# 9. Data-source and confidentiality rules

The researcher's own Exact account is a **test environment** and is not linked to the operational buyer's live production environment.

Therefore:

- the **live observation** is the primary source for task occurrence, timing, interruptions, visible outcomes and judgement cues during Measure;
- values visible on the buyer's production screen may be noted during observation only where permitted and only to the level necessary for the research variable;
- the researcher's Exact test environment may be used to understand screen structure, fields, statuses and system functionality;
- the test environment must **not** be used as evidence of the buyer's actual production workload, frequencies or historical cases;
- detailed production-data export/API/interface work is **deferred until after the exploratory Measure phase** and will be taken up in Analyze for shortlisted candidates rather than delaying baseline observation.

Because production cases cannot necessarily be reopened independently after shadowing, information that is easy to lose later—especially line count, deviation count, exception type and important outcome—should be captured live when practical.

### Repository/data-governance rule

- Use anonymized `OBS-xx` / case IDs in GitHub-facing material by default.
- Do **not** store supplier names, supplier-specific commercial prices, personal data, or unrestricted production exports in GitHub unless the company has explicitly approved that storage.
- If a production PO number is temporarily needed to reconnect observation segments, retain it only in the restricted raw working file/storage location approved by the company and remove it from shared analytical outputs where possible.
- GitHub should contain the protocol, schemas, anonymized/aggregated analysis and non-sensitive conclusions—not uncontrolled raw production data.
- The private status of the repository does not by itself constitute company approval for storing confidential production data.

---

# 10. How the collected data will quantify workload

## 10.1 Task frequency

For each task:

`frequency = observed occurrences / observation period`

Report the observation period explicitly. Do not extrapolate a short observation block to a full working day without sufficient evidence.

## 10.2 Representative active processing time

For timed tasks, summarize active processing time using the median and spread (for example IQR/range) together with sample size `n`.

The median is preferred as a robust central indicator when unusual cases can be much longer than normal cases.

## 10.3 Operational time burden

For comparable recurring activities:

`operational time burden = frequency × representative active processing time`

This estimates buyer-capacity consumption. It is **not** a total workload or mental-workload score.

## 10.4 Volume-normalized time

Where line count is meaningful:

`active time per line = active processing time / number of relevant lines`

This helps distinguish a slow process from a simply larger case.

## 10.5 Rework

Possible outputs include:

`rework rate = rework cases / relevant processed cases`

and separately the total/representative active time spent on rework.

Rework occurrence is a process/quality signal; rework time is additional quantitative workload.

## 10.6 Interruptions

Possible output:

`interruption rate = number of interruptions / observed hours`

Interruptions are reported separately as work-context constraints rather than added to a total workload score.

## 10.7 Qualitative workload and expertise evidence

Qualitative observations are summarized by recurring patterns, such as:

- missing/ambiguous information;
- historical investigation;
- exceptions;
- multiple information sources;
- undocumented cues;
- experience-based recognition;
- problem-solving episodes.

These are not converted into arbitrary numerical workload points during the exploratory Measure phase.

---

# 11. Intended Measure-phase output

The baseline should result in a task-level workload profile such as:

| Task | Frequency | Median active time | Operational time burden | Rework | Interruption/context evidence | Difficulty / expertise evidence |
|---|---:|---:|---:|---|---|---|
| Example administrative task | high | low | potentially high | low | low | low |
| Example verification task | medium | medium | high | medium | medium | low-medium |
| Example judgement task | high | not meaningfully timed | low/unknown time burden | low | low | high |
| Example investigation | low | high | medium | possible | medium | high |

The purpose is to determine **where workload occurs and what kind of workload it is**, not to rank all tasks using one unvalidated composite score.

This profile feeds the Analyze phase and final focal-activity selection together with business value, standardizability, quality risk, required human expertise and—after Measure—technical/data feasibility.

---

# 12. Pilot validation before baseline freeze

Before full baseline collection, run a short pilot observation (approximately 1–2 hours) and check:

- Can the observer keep up with the work without disrupting the buyer?
- Are Task IDs recognizable enough with the cheat sheet?
- Are Start/End boundaries usable for active processing time?
- Are task switches being separated consistently enough?
- Is `Volume` practical to record for the tasks where it matters?
- Are important outcomes/deviations being lost?
- Are notes remaining short enough for live use?
- Is the `MISS` rate acceptably low?
- Does the protocol capture routine work as well as unusual/interesting cases?
- Are any fields creating confidentiality problems or unnecessary detail?

After the pilot:

1. document what failed or was ambiguous;
2. make only the changes required for reliable live use;
3. define the final observation-window plan/coverage target;
4. freeze the baseline version before larger-scale collection.

---

# 13. Scope limitation

This is the **exploratory Measure-phase protocol**, not the final evaluation protocol for the complete BEP.

After the focal activity is selected, a second activity-specific protocol will define the exact inputs, quality criterion, performance measures and—if relevant—validated mental-workload instrument required to evaluate the proposed artifact.

---

# References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Spector, P. E., & Jex, S. M. (1998). Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151
