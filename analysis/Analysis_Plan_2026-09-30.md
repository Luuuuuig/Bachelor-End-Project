# Analysis plan

**Prepared:** 30 September 2026. **Covers:** Arno's five baseline sessions. The 28 August pilot stays separate. Steps 1 to 3 close the Measure review; steps 4 to 6 start Analyze for Arno (see [Next: Analyze](#next-analyze-for-arno)). Dennis's data enter after the supervisor discussion on Dennis.

This plan defines each measure's unit and denominator and the five-day check, following the 3 September supervisor meeting, which asked for the Day-5 coverage, stability and saturation checks and for units and denominators to be defined first.

**Revised on 30 September after review.** The check is now described as a retrospective, literature-informed assessment. The 10% rule for rates (former S3) is dropped: rates are reported with their daily range. Q2 uses the kinds-of-work review. Minutes per line for CHECK is defined as an exploratory measure.

## Data

| Source | Content |
|---|---|
| `docs/measurement/Arno_Measurement_2026-{08-31,09-01,09-08,09-18,09-23}.csv` | 287 rows; the original eight observation columns plus the reviewed Van Weele stage |
| `docs/measurement/Observation_Time_Register_2026-09-25.csv` | Confirmed net observation: 165, 186, 104, 240 and 197 minutes (892 in total) |
| Case index in `Measure_Observation_2026-09-01.md` | Request channel for 1 September, where the REQ code itself has no channel |
| Observer clarification of 30 September in `Measure_Observation_2026-09-01.md` | What a check includes (price, and the ETA where the supplier states it) and why 1 September OBS-18 is an incomplete check |

The daily CSVs are read only; they are never changed. **No row is dropped.** Rows that may matter for later scope decisions are kept and flagged:

| Flag | Rows | Rule |
|---|---|---|
| EXC | Activity code contains `EXC` (including `OTHER/EXC`) | Scope decision of 10 September, pending the supervisor discussion |
| Lost focus | 8 September OBS-16, 12:04–12:13 (9 minutes) | Observer's source note |
| Stage "Not applicable" / blank | As in the reviewed CSVs | Shown as their own stage groups |

## Units

- **Row:** one recorded episode in the notebook. A row is not a task, a case or a decision.
- **Occurrence:** any row, timed or untimed.
- **Minutes:** end minus start for timed rows. These are activity minutes: under the timing rule, a genuinely simultaneous activity keeps its full interval, so the one overlapping minute on 23 September is counted in both activities.
- **Distinct recorded minutes:** clock minutes inside net observation covered by at least one timed row. Minutes of net observation not covered are reported as time with no recorded activity.
- **Activity code:** the family at the start of the code as written (REQ, CLAR, DEC, PO, CHECK, SEND, OTHER, EXC). `[uncertain]` becomes UNCLEAR.
- **Case:** date plus OBS number, because OBS numbers restart each day. Carried-over references such as `31AUG-OBS-07` keep their own label.
- **Kind of work:** a specific task, decision or exception, assigned to a row only where its note or case context supports it; a row can show up to three kinds. Definitions and coding rules are in the [kinds-of-work review](Kinds_Of_Work_Review_2026-09-30.md). Every REQ row is also an intake (K01).
- **Daypart:** morning when the row starts before 12:45, otherwise afternoon. Untimed rows take the daypart of the nearest earlier timed row, or the next one if none precedes.
- **Request channel:** from the REQ code suffix (mail/email, phone/call, Exact, desk, letter); for 1 September from the case index.
- **Interruptions and decision:** derived from INT and DEC?. A handwritten `/` means none, as clarified by the observer on 30 September ([Recording marks](../docs/measurement/Scope_and_Classification_Addendum_2026-09-14.md#recording-marks)): `/` in INT is 0 and in DEC? is no decision. Blank DEC? cells on 31 August are "not recorded"; `?` is "uncertain". Decision marks fall sharply after 1 September, so they are reported as recorded and not compared between days.
- **Lines checked:** for a CHECK row, the number of lines the note says were checked, otherwise the order volume in lines.

## Denominators

- **Time share** = minutes of a group ÷ all minutes in the same view. Shares describe recorded work, not the whole observed time.
- **Rate per observed hour** = occurrences ÷ confirmed net observation hours for the same sessions (892 minutes for all five days). Net observation already leaves out the 9 lost-focus minutes; those rows stay in the counts and are reported as a flag, so this adds at most two occurrences.
- **Per-day values** use that day's minutes and net observation only.
- **Minutes per line (exploratory)** = total minutes ÷ total lines checked, pooled over completed checks with a line count. The median and range of the per-segment ratios are reported next to it, because they are different measures.

## Two views

Every result is shown twice:

- **A. All data:** all 287 rows and 752 minutes.
- **B. Without EXC:** the same, minus the EXC-coded rows (182 minutes).

The lost-focus rows appear in both views as a flagged line. No other exclusion is applied.

## Five-day check

**How to read it.** These rules were first proposed on 30 September, after an informal look at the activity-code shares, and the literature was consulted after the results had been seen. The check is therefore a **retrospective, literature-informed assessment**, not a pre-registered test. The proposed threshold still needs Zhongxin's confirmation.

**Coverage.** Report weekdays, morning and afternoon minutes, observation clock range, request channels, the activity codes seen on each day and the observed time with no recorded activity. Reporting follows the transparency items of Zheng et al. (2011): observation hours, dayparts, task definitions and non-observed periods. Document every gap; a gap is a limitation, not automatically a reason for more observation.

**Stability** (checked separately in views A and B):

- **S1.** The two largest activity codes by time, and their order, when any single day is left out. With five days, each leave-out removes about a fifth of the data, so this is a sensitivity check, not a formal test.
- **S2.** The change in every activity code's cumulative time share when day 5 is added, against a proposed threshold of 5 percentage points.
- **Rates.** Occurrences per observed hour per day, with their daily range, and cumulative over days 1–4 and 1–5. No pass/fail rule.
- **S4.** The change in every Van Weele stage's cumulative time share when day 5 is added, against the same proposed threshold, plus the largest stage on each day.

The 5-point threshold is a pragmatic choice, not a value taken from the literature. A work-sampling precision target of ±5% describes the uncertainty of an estimated share; it does not say how much a share may change when a day is added, so it is not used to justify S2 or S4.

**Saturation.**

- **Q1.** Day 5 shows no activity code, stage or request channel that days 1 to 4 did not show.
- **Q2.** New kinds of work per day, from the [kinds-of-work review](Kinds_Of_Work_Review_2026-09-30.md), in both views. The count is read with two splits, days 1–3 as the base with days 4–5 as the run, and days 1–4 as the base with day 5 as the run. This adapts Guest, Namey and Chen (2020), who tested bases of 4–6 interviews with runs of 2–3 and call 5% new information an optional benchmark; applying it to observation days is this project's adaptation. The review's judgement of whether each kind adds information relevant to improvement matters more than the percentage.

**CHECK.** CHECK frequency is reported per day with its range. Minutes per line is exploratory. It uses completed checks only: 1 September OBS-18 (price part blocked by an unpaid invoice) and 18 September OBS-01 (started before observation) are left out, and shown as a sensitivity. Leaving out the checks known to be incomplete does not show that every remaining segment covers a complete check of every recorded line.

**Outcome.** Coverage gaps, stability results and new information are documented together. The decision to pause broad observation rests on that combined picture, subject to the supervisor's agreement, not on any single rule.

## Literature used in reading the check

- **Zheng, K., Guo, M. H., & Hanauer, D. A. (2011).** Using the time and motion method to study clinical work processes and workflow: Methodological inconsistencies and a call for standardized research. *Journal of the American Medical Informatics Association, 18*(5), 704–710. https://doi.org/10.1136/amiajnl-2011-000083. Used for what to report about coverage; it gives no stopping or stability threshold.
- **Guest, G., Namey, E., & Chen, M. (2020).** A simple method to assess and report thematic saturation in qualitative research. *PLOS ONE, 15*(5), e0232076. https://doi.org/10.1371/journal.pone.0232076. Used for the base, run and new-information approach in Q2. It concerns interviews and allows retrospective assessment; its base and run sizes are adapted here, not applied as a validated stopping rule. The full text should be read before it is cited in the thesis.

## Outputs

| File | Step |
|---|---|
| `analysis/build_combined_table.py` → `analysis/output/Arno_Combined_2026-09-30.csv` | 2: one table with all rows and the derived columns above |
| `analysis/kinds_of_work_review.py` → `analysis/Kinds_Of_Work_Review_2026-09-30.md` and `analysis/output/Kinds_Of_Work_Rows_2026-09-30.csv` | 3: kinds of work per row, first appearance, recurrence and what each adds |
| `analysis/five_day_check.py` → `analysis/Five_Day_Coverage_Check_2026-09-30.md` | 3: coverage, stability, CHECK and saturation results |
| `analysis/workload_profile.py` → `analysis/Workload_Profile_Arno_2026-09-30.md` | 4: Arno's workload profile (draft, provisional) |

All scripts use only the Python standard library. Run them from the repository root in this order: `build_combined_table.py`, `kinds_of_work_review.py`, `five_day_check.py`, `workload_profile.py`.

## Next: Analyze for Arno

The five-day check supports pausing broad observation. Analyze starts with Arno's data; anything that depends on the EXC decision or on the Dennis comparison is marked **provisional** until the supervisor discussion.

| Step | Sub-question | For Arno now | Provisional until the supervisor discussion |
|---|---|---|---|
| 4. Workload profile | SQ3 | Time, frequency and volume by activity code, stage and kind of work, in views A and B; difficulty cues from the INT, DEC and note fields, kept as separate indicators | Which view is the thesis result (EXC) |
| 5. Workflow | SQ1 | Arno's standard workflow from the observations and the AS-IS process, with the hand-offs and problems the kinds-of-work review shows | The relationship with Dennis's tactical work |
| 6. Candidate comparison | SQ4 | The candidates in the [methodology](../docs/methodology/Phase_1_Current_Methodology.md#4-current-candidate-portfolio) compared on workload contribution, business relevance, technical feasibility and the need for human expertise | Any candidate whose evidence depends on EXC time or on Dennis's work |

Each Analyze output states its view, its denominator and which conclusions are provisional.
