# Measurement Protocol v1.3 — Exploratory Measure Baseline

**Status:** Controlled baseline revision effective 2 September 2026 after the second official baseline observation. Use this version for official observations from 2 September onward unless a documented measurement-system failure requires a dated deviation.

**Purpose:** This protocol defines how workload-related evidence is collected during shadowing of the operational buyer at Hytech-Pommec. It is designed for the broad exploratory Measure phase, before one focal purchasing activity is selected for deeper Analyze/Improve work.

**Why v1.3 exists:** The 1 September observation confirmed that HOLD can follow maximalisatie whether or not demand was added, exposed the need for an explicit Measure stopping rule, and prompted a clarification of the approved data categories in the private repository. Version 1.3 does **not** change the live activity families, fields, core active-time/non-fabrication logic or post-session mapping structure used in v1.2; the two protocol versions therefore remain analytically comparable when their dated clarifications are reported.

### Controlled changes from v1.2

1. **Post-MAX logic is aligned with the current AS-IS master:** after MAX, assess the resulting order in every case and then record HOLD or ORD; `MAX=ADD` does not automatically imply ORD.
2. **The current observation target is operationalized as five distinct working days**, following the academic-advisor guidance as recalled by the student. Actual windows and net observed minutes are reported separately; five working days is not silently converted into 40 net hours.
3. A predeclared **coverage review and extension rule** determines whether observation continues after Day 5.
4. **Private-repository governance is aligned with the company permission confirmed by the student on 2 September 2026**, while external publication and new confidential categories remain controlled.
5. The v1.2 live coding structure remains unchanged to preserve baseline comparability.
6. The existing non-fabrication rule is made explicit for SEND: a genuine complete sub-minute action that cannot be timed reliably is retained as an untimed occurrence rather than assigned an artificial zero- or one-minute duration.

Related files:
- Workload construct: `../methodology/Workload_Definition.md`
- Current research methodology and candidate selection: `../methodology/Phase_1_Current_Methodology.md`
- Current AS-IS workflow and 31-task register: `../process/Process_Cleaned_V1.5.md`
- Pilot evidence: `Pilot_Measure_Observation_2026-08-28.md`
- First official baseline observation: `Measure_Observation_2026-08-31.md`
- Live observer cheat sheet: `Measure_Live_Cheat_Sheet_v1.3.md`

---

# 1. What this protocol measures

The protocol does **not** create one total workload score. It collects a multidimensional workload profile.

| Dimension | Observable indicator | Interpretation |
|---|---|---|
| Quantitative workload — occurrence/frequency | number of observed episodes/occurrences by activity family | Short activities can matter if they happen often. |
| Quantitative workload — active processing time | clock-time duration of meaningful active episodes | Buyer-capacity consumption, not mental workload. |
| Work volume / case size | lines/items where meaningful | Helps interpret duration in relation to case size. |
| Rework / exception burden | occurrence and active time | Additional work and possible process/quality signal. |
| Organizational constraints | interruptions/task switches, missing information, system problems | Conditions that fragment or obstruct work. |
| Qualitative difficulty evidence | exceptions, uncertainty, investigation, problem solving, decision notes | Important work can be difficult even when fast. |
| Expertise dependence | explicit/tacit cues, prior-case knowledge, experience-based recognition | Helps identify what may require human expertise or careful support. |

**Mental workload is not directly quantified by the live observation sheet.** A validated instrument such as NASA-TLX may be considered later only if the selected focal activity requires it.

### 1.1 Relationship to the main research question

This protocol can identify which activity families recur during the observed windows, how much reliable active buyer time they consume, and where clarification, interruptions, exceptions, rework and supported judgement/expertise cues occur. It supports hotspot screening and focal-case selection.

It cannot by itself show that an AI artifact reduces workload or preserves purchasing outcome quality, because exploratory Measure contains no intervention comparison and no focal quality rubric/ground truth. Observed active time is not automatically potential time saving, and the baseline is not claimed to be a statistically representative week. Those claims require the later activity-specific manual-versus-AI evaluation protocol described in Section 17.

---

# 2. Measurement architecture

The measurement system has three practical live layers plus post-session enrichment.

## 2.1 Case context — recorded once in the restricted case index

For every new case, record where possible:

`Case | Origin | Channel | First observed | PO known?`

### Origin

Use one of:
- **External request**
- **Exact demand**
- **Supplier confirmation**
- **Finance return**
- **Colleague question**
- **Unknown**

### Channel

Use one of:
- **Email**
- **Phone**
- **Desk**
- **Letter/Paper**
- **Exact**
- **Other**
- **Unknown**

Origin and Channel are different variables. For example, an external request can arrive by email, phone, desk or letter/paper.

Use **Unknown** when a case is already in flight when observation begins or the origin/channel cannot be established reliably.

The case index is restricted working material used to preserve continuity. The private repository may retain only the data categories covered by the company permission described in Section 13.

## 2.2 Level 1 — live work episodes

Use:

`Case | Activity | Start | End | Volume | INT | DEC? | Result / short note`

The observer records the work that is reliably observable, not detailed Task IDs.

## 2.3 Decision attribute

`DEC?` indicates whether a distinct purchasing judgement/decision is part of the episode:

- **Y** = a decision/judgement event was observed or explicitly explained within the episode;
- **—** = no distinct decision event is part of the episode;
- **?** = cannot determine reliably.

If the same decision is embedded in a timed PO/REQ/CLAR/CHECK/EXC episode, set `DEC?=Y` and **do not create a second DEC row for the same decision**.

A standalone `DEC` row is used only when the decision is genuinely separate and essentially instantaneous/tally-only.

## 2.4 Level 2 — post-session enrichment

Immediately after the observation block, add where supported:

`Detailed Task ID | Mapping confidence`

Mapping confidence:
- **C** = confident mapping to the 31-task register
- **P** = probable mapping; evidence is incomplete
- **U** = observed purchasing activity not represented by the current register
- **?** = cannot determine reliably

The original live record must be retained. Do not retrospectively rewrite it to look more precise than the evidence supports.

---

# 3. Live activity families

| Code | Live activity family | Measurement rule | Operational boundary / typical mapping |
|---|---|---|---|
| **REQ** | Receive, read, listen to, organize or comprehend a new purchasing request | **TIME IF / TALLY if instantaneous** | Begins when active intake starts; ends when work becomes clarification, decision-making or system/PO execution. Typically Task 1 and request-intake part of Tasks 2–4. |
| **CLAR** | Clarify, investigate or obtain missing/ambiguous information | **TIME IF** | Tasks 4–5 plus requester clarification, drawing/specification retrieval and information-seeking work. |
| **DEC** | Standalone purchasing decision | **TALLY only** | Use only when a decision is genuinely separate from another active episode. Otherwise use `DEC?=Y`. |
| **PO** | Create/change/prepare/process PO or related order work in Exact | **TIME** | Tasks 2–3 and 6–21 where they form observable order-processing episodes; may include seamless maximalisatie work. |
| **CHECK** | Verify price, supplier confirmation or purchasing information | **TIME** | Tasks 14–16 and 26–28 where verification is active work. |
| **SEND** | Forward/send purchasing communication | **TIME by default; TALLY if unmeasurably brief** | Mainly Task 23; other send-only communication can be noted explicitly. A genuine complete sub-minute action may be tallied when precise timing is not reliable. |
| **EXC** | Aftercare, tracing, rework or exception handling | **TIME IF** | Tasks 29–31 plus PO aftercare/expediting not yet represented in the register. |
| **OTHER** | Relevant operational purchasing work that genuinely does not fit | **TIME IF** | Temporary safety net; retain subtype in note and review after session. |

### TIME / TALLY / TIME IF

- **TIME:** record Start and End because active duration is meaningful and observable.
- **TALLY:** record the occurrence with Start/End = `—`; do not create zero-minute timed rows.
- **TIME IF:** time the activity when it becomes a meaningful visible episode; otherwise tally it.

System/external events that do not require active buyer work are not timed as buyer workload.

SEND is normally timed. If the entire SEND action is genuinely sub-minute and cannot be timed reliably, retain it as a tally with Start/End = `—`, explain the reason in the note, and exclude it from timed-episode and active-minute totals. Do not assign a fabricated zero- or one-minute duration.

---

# 4. Maximalisatie rule

The current AS-IS working interpretation is that a **maximalisatie check is a standard part of order processing**. The 1 September session supports that MAX is frequent, but it does not yet prove that a separately observable MAX check occurs for every order. Record `MAXOBS=Y` only when observed and `MAXOBS=?` when it cannot be established reliably.

The operational logic is:

`check same-supplier demand → add useful demand if available → assess the resulting order in every case → HOLD or ORD based on size, urgency and current purchasing context`

Keep two outcomes separate:

- `MAX=ADD / NONE / ?` describes whether useful demand was added;
- `ORD / HOLD / ?` describes the later post-MAX decision.

Therefore `MAX=ADD; HOLD` is possible and should not be rewritten as a contradiction. If the cues for HOLD/ORD are unclear, preserve the observed outcome and mark the reasoning uncertain.

### 4.1 MAX and PO often happen seamlessly

If Arnold checks same-supplier demand, assesses it, adds lines and continues the PO as one continuous episode, do **not** invent a minute split between MAX and PO.

Record one timed PO episode and preserve the MAX result in the note.

Examples of result shorthand:
- `MAXOBS=Y; MAX=ADD; +4L; HOLD`
- `MAXOBS=Y; MAX=ADD; +2L; ORD`
- `MAXOBS=Y; MAX=NONE; urgent; ORD`
- `MAXOBS=Y; MAX=NONE; small/non-urgent; HOLD`
- `MAXOBS=?; MAX=?; ORD/HOLD=?` when the sequence or outcome cannot be established reliably

A timed episode containing MAX is interpreted as **combined PO/maximalisatie active time**, not pure decision time.

### 4.2 Do not infer pure decision time

A decision can occur while Arnold is navigating Exact or manipulating PO lines. The protocol therefore does not claim to measure invisible cognition separately.

Use:
- active episode time -> operational effort;
- `DEC?=Y` / standalone DEC tally -> decision occurrence;
- outcome -> ORD/HOLD/etc.;
- `J` / `EXP` -> supported judgement/expertise evidence.

---

# 5. Live observation fields and non-blank conventions

Use one row per meaningful work episode:

`Case | Activity | Start | End | Volume | INT | DEC? | Result / short note`

| Field | Operational rule |
|---|---|
| **Case** | Anonymized `OBS-xx`. Same case keeps the same ID when it returns later. |
| **Activity** | One live family from Section 3. |
| **Start / End** | Clock times for meaningful active episodes. Use `—` for tally/instantaneous occurrences. **Do not leave blank.** |
| **Volume** | Relevant lines/items where practical, e.g. `5L`. Use `—` when not applicable or not obtainable. **Do not leave blank.** |
| **INT** | Always enter a number. `0` means no interruption was observed. **Blank is not permitted.** |
| **DEC?** | `Y`, `—`, or `?`. **Do not leave blank.** |
| **Result / short note** | Minimal context that may be unrecoverable later: outcome, MAX result, missing information, exception, deviation, J/EXP evidence or useful subtype. Use `—` if no note is needed. |

### Shorthand

- `L` = lines/items
- `D` = deviations
- `ORD` = proceed/order
- `HOLD` = hold/pause
- `MAX=ADD` = maximalisatie check led to added demand
- `MAX=NONE` = maximalisatie checked; nothing useful added
- `MAX=?` = maximalisatie outcome unclear
- `MI` = missing/ambiguous information
- `FIN` = Finance-related issue
- `J` = observable judgement/decision evidence
- `EXP` = observable experience/tacit-knowledge cue
- `MISS` = work occurred but could not be captured sufficiently

`J` and `EXP` are separate:
- use **J** only when a choice/trade-off/decision is actually observed or explained;
- use **EXP** only when there is evidence that prior experience, memory, tacit recognition or historical knowledge mattered;
- use `J+EXP` when both are supported;
- if the evidence is uncertain, do not assert J/EXP.

---

# 6. Case-ID rule

**OBS identifies a purchasing case, not a task, screen, interruption or row.**

1. New purchasing case -> new OBS ID.
2. New activity within the same case -> same OBS ID.
3. Case returns later -> reuse the same OBS ID.
4. Unrelated non-purchasing activity -> no new OBS ID.
5. If an interruption becomes meaningful work on another purchasing case, that case receives its own OBS ID.
6. Record Origin and Channel once in the restricted case index; do not repeat them on every live row.
7. A skipped OBS number is not automatically missing data; explain it in the case index if it was reserved/used for an untimed or prior case.

---

# 7. Active processing time and interruptions

## 7.1 Active processing time

Active processing time is time during which the buyer is actually working on the purchasing activity.

If the buyer clearly leaves the activity for another case, conversation or unrelated task, close/pause the segment and start a new segment when the case resumes.

Do not allow two active buyer episodes to occupy the same clock minute unless there is a documented boundary ambiguity; resolve it while memory is fresh or mark the boundary uncertain rather than double-counting.

## 7.2 Interruption attribution

When an interruption **causes the active episode to stop**, record it on the segment being left.

Do not infer interruptions from segment count alone.

If the active episode has already finished and a call/conversation begins afterward, it is **not** an interruption of the completed episode.

## 7.3 Observer unavailable versus buyer interrupted

If the observer cannot observe for a period but the buyer is not known to have been interrupted, record that period as **observer unavailable** in the session header and remove it from net observed time. Do not convert observer unavailability into `INT`.

## 7.4 System waiting

When the buyer is no longer actively working because Exact/system processing is occurring, stop active time.

- casual email browsing during system wait -> normally ignore;
- meaningful purchasing work on another case -> record that other case;
- productive use of waiting time is not automatically an interruption of the waiting case.

---

# 8. Fast cognition and variable-duration work

Do not use duration as a proxy for difficulty or expertise.

### REQ

REQ is genuine work when the buyer is actively receiving, reading, listening to, organizing or comprehending a request. Phone/desk intake can therefore be several minutes and should be timed. Very brief recognition can remain tally-only.

REQ ends when the work becomes:
- clarification/investigation -> CLAR;
- system/PO execution -> PO;
- a genuinely standalone decision -> DEC.

### DEC

DEC is not assigned a pure duration by default.

- If a decision is embedded in timed work -> use `DEC?=Y`.
- If it is a separate quick decision -> standalone DEC tally.
- Never time invisible cognition merely because the buyer is thinking while manipulating Exact.

### CLAR / EXC

Use TIME IF. A short question may be a tally; a visible investigation or tracing episode should be timed.

---

# 9. MISS rule

When purchasing work happens but cannot be captured reliably, record `MISS` rather than guessing.

Minimum acceptable record:

`time/period | MISS | purchasing activity observed but could not be coded`

Do not turn unexplained clock gaps into MISS after the fact unless you actually know purchasing work occurred.

MISS is a measurement-quality indicator. Repeated MISS should trigger review of the observation method rather than silent data loss.

---

# 10. Observation-session header

Each official observation block must record:

```text
Date:
Buyer:
Observer:
Observation start:
Observation end:
Breaks / observer unavailable periods:
Net observed time:
Context note: normal / unusually quiet / unusually busy / system issue / other
Acclimatization session? yes/no
```

Net observed time is the denominator for occurrence rates.

---

# 11. Sampling and observation-window rules

1. Record all observable operational-purchasing work in the selected window; do not follow only preferred thesis candidates.
2. The current planned minimum is observation on **five distinct working days**, following the academic-advisor guidance as recalled by the student. This is a project decision, not a universally validated sample size.
3. Treat **five working days** and **40 net observed hours** as different concepts. Record the scheduled window, breaks/observer-unavailable time and net observed minutes for every day. A partial day contributes evidence but is not silently labelled a full-day equivalent.
4. Cover both morning and afternoon work across the baseline and document whether the main known origin/channel and activity-family patterns were observed or absent.
5. Do not extrapolate a short block directly to a full day/week without adequate coverage.
6. Exclude breaks and observer-unavailable periods from net observed time.
7. Use MISS for known uncaptured purchasing work.
8. Version any necessary measurement-system change; do not silently redefine fields during baseline.
9. Same-observer recoding checks intra-rater consistency, not inter-rater reliability.

### Day-5 coverage review and extension rule

After the fifth distinct observation day, stop Measure only if the coverage log shows:

- meaningful morning and afternoon coverage;
- no abnormal day, missing daypart or measurement failure that would materially distort the baseline;
- the main recurring work families and case/channel patterns have either been observed or their absence is explicitly documented;
- the last observation day did not reveal a materially new recurring activity or decision pattern that could change candidate selection.

If one of these conditions is not met, add at least one targeted observation block/day aimed at the documented gap and repeat the coverage review. This is a transparent adequacy rule for an exploratory case study; it is not a claim of statistical representativeness.

---

# 12. Post-session enrichment and register-extension rule

Complete enrichment as soon as practical after each observation block.

For each live episode:
1. retain the original live record;
2. map to detailed Task ID(s) only where evidence supports it;
3. assign C/P/U/?;
4. preserve meaningful U/OTHER subtypes such as article-master work, requester clarification, drawings/specifications or aftercare;
5. do not fabricate missing timing, outcomes or reasoning.

### Predeclared register-review trigger

An unmapped activity subtype becomes a **candidate for addition to the detailed AS-IS register** when:
- it is observed in at least **two separate official baseline sessions and at least three times in total**, **or**
- repeated observation plus buyer/manager validation establishes that it is a normal recurring purchasing activity.

This is a **researcher-defined operational trigger**, not a validated statistical cutoff. Meeting the trigger starts a review; it does not automatically force a new Task ID.

---

# 13. Data-source and confidentiality rules

Live observation is the primary source for:
- active processing time;
- interruptions/task switching;
- clarification and exception work;
- visible outcomes and decision/expertise cues.

Approved aggregated/system data may supplement the observation for transactional volume such as:
- PO count by week/month;
- PO-line count;
- lines per PO;
- order dates;
- buyer.

System/dashboard volume is not direct evidence of clarification, judgement, interruptions or mental workload.

Repository rules:
- use anonymized `OBS-xx` case IDs in the analytical record;
- this repository is the student's private personal working repository for keeping track of the BEP;
- based on company permission confirmed by the student on 2 September 2026, the buyer names and case-specific commercial values already recorded may be retained here;
- no separate company-permission audit register is created within the current thesis scope for this personal working repository;
- personal contact details, unrestricted production exports and any additional confidential data category remain outside the current permission unless separately agreed;
- temporary production identifiers remain in approved restricted storage;
- rules for a thesis, presentation, screenshot or other external output are assessed separately when material is exported; a later repository visibility/access change requires a new review before the change.

---

# 14. Baseline outputs

The primary Measure output is first summarized at **activity-family level**, because this is the reliable live measurement layer.

| Activity | Occurrences | Timed n | Active-time summary | INT | DEC/J/EXP evidence | Main issues / patterns |
|---|---:|---:|---|---:|---|---|
| REQ | | | | | | |
| CLAR | | | | | | |
| DEC | | — | — | | | |
| PO | | | | | | |
| CHECK | | | | | | |
| SEND | | | | | | |
| EXC | | | | | | |
| OTHER | | | | | | |

Detailed Task-ID analysis is shown where mapping confidence and sample size justify it.

### 14.1 Occurrence rate

`occurrence rate = observed occurrences / net observed hours`

### 14.2 Active processing time

For timed activities, show individual values when sample size is very small and summarize the distribution using median plus spread when useful.

**Researcher-defined small-sample safeguard:** when `n < 5` timed observations for an activity, do not present the median or derived burden as a stable representative estimate. Label it exploratory/indicative and show the individual values.

### 14.3 Operational time burden

Only for sufficiently observed comparable recurring timed activities:

`operational time burden = occurrence/frequency × representative active processing time`

This is a buyer-capacity indicator, not total workload or mental workload.

### 14.4 MAX reporting

Because MAX and PO are often seamless, report:
- number/share of order episodes with `MAX=ADD`;
- number/share with `MAX=NONE` where reliably observable;
- added lines/items where available;
- ORD/HOLD outcome;
- combined active PO/MAX time where MAX is embedded.

Do **not** interpret combined PO/MAX time as pure decision time.

### 14.5 Rework / exceptions

Report occurrences per observed hour/day and active time. A true rework percentage requires a matched denominator/cohort or retrospective system evidence.

### 14.6 Interruptions

`interruption rate = observed interruptions / net observed hours`

INT remains a separate organizational-constraint measure.

### 14.7 Qualitative / expertise evidence

Summarize recurring patterns such as missing/ambiguous information, clarification, historical investigation, drawings/specifications, aftercare, exceptions, multiple information sources, undocumented cues and experience-based recognition. Do not convert them into arbitrary workload points.

---

# 15. Measure screening level and later focal activity

The eight live families are the primary **Measure screening/reporting level**. This does not require the final thesis intervention to target an entire family.

After Measure and Analyze, the focal activity may be:
- one whole family;
- a coherent subprocess/context inside a family, such as maximalisatie embedded in PO work;
- a detailed Task-ID slice where evidence and feasibility support that level.

The final selection must use measured burden, recurrence, business value, quality risk, expertise dependence, data/technical feasibility and evaluation quality rather than choosing a row merely because it exists in the register.

---

# 16. Baseline freeze and comparability

Version 1.3 is the **controlled protocol for observations from 2 September 2026 onward**. Version 1.2 remains the protocol used for the 1 September session.

The 31 August and 1 September sessions remain valid historical evidence. Their documented session-specific differences and protocol versions are preserved in the dated observation files. Version 1.3 changes MAX interpretation, stopping/coverage logic and repository governance, and makes explicit the existing treatment of unmeasurably brief SEND actions. The live coding fields and the principle of timing only reliable active episodes remain unchanged; do not rewrite historical raw records to look as though v1.3 existed earlier.

If a serious defect appears:
1. preserve the affected session;
2. document the defect;
3. assess comparability;
4. version/date the change instead of silently editing the protocol.

No further structural revision should be made merely because another potentially useful field is imagined. Change only for a demonstrated measurement-system failure.

---

# 17. Scope limitation

This is the exploratory Measure-phase protocol, not the final evaluation protocol for the BEP artifact.

After one focal activity is selected, an activity-specific evaluation protocol will define its inputs/outputs, quality criterion, benchmark, performance measures and—if relevant—a validated mental-workload instrument.

---

# References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Spector, P. E., & Jex, S. M. (1998). Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151
