# Measurement Protocol v1.1 — Exploratory Measure Baseline

**Status:** Baseline-ready revision frozen 28 August 2026 after the 28 August pilot. Use this version for official observations from 31 August 2026 onward unless a documented measurement failure requires a dated deviation.

**Purpose:** This protocol defines how workload-related evidence is collected during shadowing of the operational buyer at Hytech-Pommec. It is designed for the broad exploratory Measure phase, before one focal purchasing activity is selected for deeper Analyze/Improve work.

**Reason for v1.1:** The 28 August pilot showed that the detailed 31-task AS-IS register is useful for process analysis but is too granular for reliable live coding by one observer in a fragmented work environment. The baseline therefore separates:
1. a **simple live-observation layer** using broad activity families; and
2. a **post-session enrichment layer** that maps episodes to detailed Task IDs where evidence supports the mapping.

Related files:
- Workload construct: `../methodology/Workload_Definition.md`
- Current research methodology and candidate selection: `../methodology/Phase_1_Current_Methodology.md`
- Detailed 31-task AS-IS register: `../process/Process_Cleaned_V1.5.md`
- Pilot evidence: `Pilot_Measure_Observation_2026-08-28.md`
- Live observer cheat sheet: `Measure_Live_Cheat_Sheet_v1.1.md`

---

# 1. What this protocol measures

The protocol does **not** create one total workload score. It collects a multidimensional workload profile.

| Dimension | Observable indicator | Interpretation |
|---|---|---|
| Quantitative workload — occurrence/frequency | number of observed episodes/occurrences by activity family | Short activities can still matter if they happen often. |
| Quantitative workload — active processing time | clock-time duration of meaningful active episodes | Buyer-capacity consumption, not mental workload. |
| Work volume / case size | lines/items where meaningful | Helps interpret duration in relation to case size. |
| Rework / exception burden | occurrence and active time | Additional work and possible process/quality signal. |
| Organizational constraints | interruptions/task switches, missing information, system problems | Conditions that fragment or obstruct work. |
| Qualitative difficulty evidence | exceptions, uncertainty, investigation, problem solving, decision notes | Important work can be difficult even when fast. |
| Expertise dependence | explicit/tacit cues, prior-case knowledge, experience-based recognition | Helps identify what may require human expertise or careful support. |

**Mental workload is not directly quantified by the live observation sheet.** A validated instrument such as NASA-TLX may be considered later only if the selected focal activity requires it.

---

# 2. Measurement architecture

## 2.1 Level 1 — live observation

During shadowing, the observer codes only broad activity families:

`Case | Activity | Start | End | Volume | INT | Result / short note`

The objective is to capture what happened reliably without forcing detailed Task-ID classification while the buyer is switching rapidly between cases, emails, calls, Exact and colleagues.

## 2.2 Level 2 — post-session enrichment

Immediately after the observation block, the observer may add:

`Detailed Task ID | Mapping confidence`

Mapping confidence:
- **C** = confident mapping to the 31-task register
- **P** = probable mapping; evidence is incomplete
- **U** = observed purchasing activity not represented by the current register
- **?** = cannot determine reliably

The live record must not be retrospectively rewritten to look more precise than the observation supports.

The detailed 31-task register in `Process_Cleaned_V1.5.md` remains the AS-IS analytical model. It is **not** deleted or replaced by the activity families.

---

# 3. Live activity families

| Code | Live activity family | Measurement rule | Typical detailed mapping / examples |
|---|---|---|---|
| **REQ** | Receive/process a new purchasing request | **TALLY** by default | Tasks 1–4; email, phone, colleague/desk request |
| **CLAR** | Clarify, investigate, obtain missing/ambiguous information | **TIME IF** | Task 4–5 plus requester clarification, drawing/specification retrieval |
| **DEC** | Purchasing decision, maximalisatie, order/hold logic | **TALLY** + outcome | Tasks 6–11 |
| **PO** | Create/change/prepare/process PO in Exact | **TIME** | Tasks 2–3, 12–21 where they form active administrative episodes |
| **CHECK** | Verify price, supplier confirmation or purchasing information | **TIME** | Tasks 14–16, 26–28 where verification is active work |
| **SEND** | Forward/send purchasing communication | **TIME** | Mainly Task 23; supplier communication tied to sending |
| **EXC** | Aftercare, tracing, rework, exception handling | **TIME IF** | Tasks 29–31 plus PO aftercare/expediting not yet in register |
| **OTHER** | Relevant operational purchasing work that genuinely does not fit | **TIME IF** | Temporary safety net; review after session |

### TIME / TALLY / TIME IF

- **TIME:** record Start and End because active duration is meaningful and observable.
- **TALLY:** record one occurrence but leave Start/End blank. Do not force minute-level timing onto decisions that happen in seconds.
- **TIME IF:** time the activity only when it becomes a clearly observable work episode; otherwise tally it.

System/external events that do not require active buyer work are not timed as buyer workload.

---

# 4. Live observation fields

Use one row per meaningful work episode.

`Case | Activity | Start | End | Volume | INT | Result / short note`

| Field | Operational rule |
|---|---|
| **Case** | An anonymized case ID such as `OBS-01`. Same purchasing case keeps the same OBS ID when it returns later. |
| **Activity** | One live family from Section 3. |
| **Start / End** | Clock time for a meaningful active segment. Blank for tally-only occurrences. |
| **Volume** | Relevant lines/items where practical, e.g. `5L`. Do not delay observation to obtain it. |
| **INT** | Number of observable interruptions/task switches that pull the buyer away from active work in the episode. |
| **Result / short note** | Outcome, deviation, missing information, exception, decision cue, expertise cue or minimal context that may be unrecoverable later. |

### Suggested shorthand

- `L` = lines/items
- `D` = deviations
- `ORD` = order now / proceed
- `HOLD` = hold/pause
- `MAX` = maximalisatie
- `MI` = missing/ambiguous information
- `FIN` = Finance-returned issue
- `J` = observable judgement/decision
- `EXP` = observable experience/tacit-knowledge cue
- `MISS` = work occurred but could not be captured sufficiently

`J` and `EXP` are separate:
- use **J** only when a choice/trade-off/decision is actually observed or explained;
- use **EXP** only when there is evidence that prior experience, memory, tacit recognition or historical knowledge mattered;
- use `J+EXP` when both are supported;
- leave blank when uncertain.

---

# 5. Case-ID rule

**OBS identifies a purchasing case, not a task, screen, interruption or measurement row.**

Rules:
1. New purchasing case -> new OBS ID.
2. New activity within the same case -> same OBS ID.
3. Case returns later -> reuse the same OBS ID.
4. Unrelated non-purchasing activity -> no new OBS ID.
5. If an interruption becomes meaningful work on a different purchasing case, that different case receives its own OBS ID.

Keep a small restricted running case index during the session so returning cases can be recognized. Do not place commercial identifiers in GitHub-facing material.

---

# 6. Active processing time and interruptions

## 6.1 Active processing time

The primary time metric is **active processing time**: time during which the buyer is actually working on the purchasing activity.

If the buyer clearly leaves the activity for another case, conversation or unrelated task, close/pause the segment and start a new segment when the case resumes.

Example:

```text
OBS-03 | CHECK | 10:00 | 10:06 | 10L | 1 | interrupted by call
OBS-03 | CHECK | 10:11 | 10:15 | 10L | 0 | resumed
```

Active processing time = 6 + 4 = 10 minutes.

## 6.2 Interruption attribution

When a substantial interruption **causes the active episode to stop**, record that interruption on the segment being left, e.g. `INT=1`.

Do not infer interruption counts from the number of segments afterward, because a case can also be intentionally parked or resumed for other reasons.

## 6.3 Brief interruption

A very short exchange that does not meaningfully take the buyer away from the task may remain within the segment and be counted in `INT`.

## 6.4 System waiting

If Arnold clicks an Exact action and the system is processing, buyer active time stops when he is no longer actively working on the case.

- casual email browsing during system wait: normally do not record;
- meaningful purchasing work on another case during the wait: record that other case separately;
- do not mark productive use of waiting time as an interruption of the waiting case.

## 6.5 Non-purchasing email/work

- unrelated email while idle/waiting: do nothing;
- unrelated email that pulls the buyer away from active purchasing work: close the purchasing segment and record `INT=1`;
- unrelated work is not given an OBS ID unless it is operational purchasing work within the study scope.

---

# 7. Fast cognition and variable-duration work

Do not use duration as a proxy for difficulty or expertise.

### REQ
Normally **TALLY**. A request can be recognized in seconds. If processing the request turns into active clarification or data entry, use the relevant family (`CLAR`, `PO`, etc.) for that work.

### DEC
Normally **TALLY** + outcome. Record `J` and/or `EXP` only when supported by observable evidence or immediate explanation.

### CLAR
Use **TIME IF**. A clarification can be a 10-second question or a several-minute investigation. Tally the former; time the latter.

### EXC
Use **TIME IF** for the same reason. A simple aftercare question may be very short, while tracing or rework can become a long investigation.

---

# 8. MISS rule

When the work moves too fast to capture reliably, record `MISS` rather than guessing.

Minimum acceptable entry:

```text
11:50 | MISS | purchasing activity observed but could not be coded
```

If only part of an episode is known, preserve only the supported information.

Do not reconstruct exact timing, Task IDs, outcomes or interruptions after the fact unless there is reliable supporting evidence.

MISS is a measurement-quality indicator. A recurring or high MISS level should trigger simplification or a documented protocol review rather than silent data loss.

---

# 9. Observation-session header

Each official observation block must record:

```text
Date:
Buyer:
Observer:
Observation start:
Observation end:
Breaks / observer unavailable periods:
Net observed time:
Context note: normal / unusually quiet / unusually busy / system issue / other material context
Acclimatization session? yes/no
```

Net observed time is the denominator for occurrence rates.

If the first session appears strongly affected by observation reactivity, flag it as acclimatization rather than automatically pooling it with the baseline.

---

# 10. Sampling and observation-window rules

1. Record all observable **operational-purchasing** work that can be captured during the selected window; do not follow only interesting candidate activities.
2. Cover multiple working days and different dayparts where feasible.
3. Do not extrapolate a short observation block directly to a full day/week without adequate coverage.
4. Keep breaks and observer-unavailable periods outside net observed time.
5. Record `MISS` rather than selectively omitting work when the pace becomes too high.
6. After v1.1 is frozen, do not silently change live codes or definitions. Any necessary change must be dated and its impact on comparability documented.
7. One observer is a limitation. If coding consistency needs checking later, recoding a sample by the same observer assesses **intra-rater consistency**, not inter-rater reliability.

The exact number of baseline days is a pragmatic coverage decision, not a validated universal sample size. Coverage should be sufficient to observe routine work, fragmentation, exceptions and variation across working periods.

---

# 11. Post-session enrichment procedure

Complete enrichment as soon as practical after each observation block, ideally immediately while context is still fresh.

For each live episode:
1. retain the original live code and notes;
2. map to detailed Task ID(s) only where evidence supports it;
3. assign mapping confidence C/P/U/?;
4. mark recurring `OTHER`/U activities for later review of the AS-IS register;
5. do not fabricate missing timing or cognitive reasoning.

Example:

| Case | Live code | Detailed Task ID | Confidence | Interpretation |
|---|---|---:|---|---|
| OBS-05 | CHECK | 26 | C | supplier confirmation comparison |
| OBS-14 | DEC | 8–9 | P | maximalisatie search/decision |
| OBS-16 | EXC | — | U | colleague-initiated PO aftercare |

Repeated unmapped activity is evidence that the detailed AS-IS model may need extension, but one isolated pilot episode does not automatically justify a new permanent Task ID.

---

# 12. Data-source and confidentiality rules

Live observation remains the primary source for:
- active processing time;
- interruptions/task switching;
- clarification and exception work;
- visible outcomes and decision/expertise cues.

System/dashboard data can **supplement** observation for transactional volume where Johan/company can provide aggregated figures or approved exports, for example:
- PO count by week/month;
- PO-line count;
- lines per PO;
- order dates;
- buyer;
- anonymized case/supplier identifiers where permitted.

Dashboard/system volume should not be interpreted as direct evidence of clarification, judgement, interruptions or mental workload.

The researcher's Exact test environment is not evidence of Arnold's production workload.

### Repository/data-governance rule

- Use anonymized `OBS-xx` IDs in GitHub.
- Do not upload raw supplier names, commercial prices, personal data or unrestricted production exports without explicit company approval.
- If a production PO number is needed temporarily to reconnect segments, keep it only in approved restricted working storage.
- GitHub should contain protocols, anonymized/aggregated analysis and non-sensitive conclusions.

---

# 13. Baseline outputs

The primary baseline is first summarized at **activity-family level**, because that is the reliable live measurement layer.

| Activity | Occurrences | Timed n | Active-time summary | INT | J/EXP evidence | Main issues / patterns |
|---|---:|---:|---|---:|---|---|
| REQ | | — | — | | | |
| CLAR | | | | | | |
| DEC | | — | — | | | |
| PO | | | | | | |
| CHECK | | | | | | |
| SEND | | | | | | |
| EXC | | | | | | |
| OTHER | | | | | | |

Detailed Task-ID analysis can then be shown below this where mapping confidence and sample size justify it.

## 13.1 Occurrence rate

`occurrence rate = observed occurrences / net observed hours`

State the observation denominator explicitly.

## 13.2 Active processing time

For timed activities, report individual observations where sample size is very small and summarize the distribution using median plus spread (e.g. range/IQR) when useful.

**Pragmatic small-sample safeguard:** when `n < 5` timed observations for an activity, do not present the median or derived burden as a stable representative estimate. Label it exploratory/indicative and show the individual values. This is a researcher-defined safeguard, not a validated universal cutoff.

## 13.3 Operational time burden

Only for sufficiently observed, comparable recurring timed activities:

`operational time burden = occurrence/frequency × representative active processing time`

This is an estimated buyer-capacity indicator, not total or mental workload.

## 13.4 Volume normalization

Where line count is meaningful:

`active time per line = active processing time / relevant lines`

Use only when the activity genuinely scales with line count.

## 13.5 Rework / exception reporting

During live Measure, report:
- rework/exception occurrences per observed hour/day; and
- active time spent on rework/exception work.

Do **not** calculate `rework cases / relevant processed cases` from the live observation window unless numerator and denominator belong to a properly matched cohort. Finance-returned issues and supplier aftercare can relate to POs created before the observation period. A true rework rate requires matched retrospective/system evidence.

## 13.6 Interruptions

Possible output:

`interruption rate = observed interruptions / net observed hours`

Interruptions are reported separately as organizational constraints.

## 13.7 Qualitative / expertise evidence

Summarize recurring patterns such as:
- missing/ambiguous information;
- clarification;
- historical investigation;
- technical drawings/specifications;
- aftercare/expediting;
- exceptions;
- multiple information sources;
- undocumented cues;
- experience-based recognition;
- problem solving.

Do not convert these into arbitrary numerical workload points.

---

# 14. Baseline freeze and deviation rule

Version 1.1 is the **official baseline collection protocol** following the 28 August pilot.

Before the first official observation, the observer needs only the practical materials:
- blank live sheet with no example rows;
- activity-family cheat sheet;
- running OBS case index;
- session-header area;
- a place to record MISS.

If a serious measurement defect appears during baseline collection:
1. preserve the affected session;
2. document the defect;
3. decide whether the change affects comparability;
4. version/date the protocol change rather than silently editing historical rules.

---

# 15. Scope limitation

This is the exploratory Measure-phase protocol, not the final evaluation protocol for the complete BEP.

After one focal activity is selected, an activity-specific evaluation protocol will define the exact input/output variables, quality criterion, benchmark, performance measures and—if relevant—a validated mental-workload instrument.

---

# References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Spector, P. E., & Jex, S. M. (1998). Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151
