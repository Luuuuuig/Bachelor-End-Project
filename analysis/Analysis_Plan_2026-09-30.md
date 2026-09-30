# Analysis plan, steps 1 to 3

**Prepared:** 30 September 2026. **Covers:** Arno's five baseline sessions only. The 28 August pilot stays separate. Dennis's data, the workload profile (sub-question 3), the workflow and Arno–Dennis relationship (sub-question 1) and the candidate comparison (sub-question 4) are later steps, after the supervisor discussion on Dennis.

This plan fixes the units, the two views and the five-day check rules before the check is run. It follows the 3 September supervisor meeting, which asked for the Day-5 coverage, stability and saturation checks and for each measure's unit and denominator to be defined first.

## Data

| Source | Content |
|---|---|
| `docs/measurement/Arno_Measurement_2026-{08-31,09-01,09-08,09-18,09-23}.csv` | 287 rows; the original eight observation columns plus the reviewed Van Weele stage |
| `docs/measurement/Observation_Time_Register_2026-09-25.csv` | Confirmed net observation: 165, 186, 104, 240 and 197 minutes (892 in total) |
| Case index in `Measure_Observation_2026-09-01.md` | Request channel for 1 September, where the REQ code itself has no channel |

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
- **Activity code:** the family at the start of the code as written (REQ, CLAR, DEC, PO, CHECK, SEND, OTHER, EXC). `[uncertain]` becomes UNCLEAR.
- **Case:** date plus OBS number, because OBS numbers restart each day. Carried-over references such as `31AUG-OBS-07` keep their own label.
- **Daypart:** morning when the row starts before 12:45, otherwise afternoon. Untimed rows take the daypart of the nearest earlier timed row, or the next one if none precedes.
- **Request channel:** from the REQ code suffix (mail/email, phone/call, Exact, desk, letter); for 1 September from the case index.

## Denominators

- **Time share** = minutes of a group ÷ all minutes in the same view.
- **Rate per observed hour** = occurrences ÷ confirmed net observation hours for the same sessions (892 minutes for all five days). Net observation already leaves out the 9 lost-focus minutes; those rows stay in the counts and are reported as a flag, so this adds at most two occurrences.
- **Per-day values** use that day's minutes and net observation only.

## Two views

Every result is shown twice:

- **A. All data:** all 287 rows and 752 minutes.
- **B. Without EXC:** the same, minus the EXC-coded rows (182 minutes).

The lost-focus rows appear in both views as a flagged line. No other exclusion is applied in steps 1 to 3.

## Five-day check rules

These are the rules for the Day-5 review asked for on 3 September. They are **proposed and still need Zhongxin's confirmation**. They were first proposed on 30 September during the data-sufficiency discussion, after an informal look at family shares; they have not been adjusted since.

**Coverage.** Report weekdays, morning and afternoon minutes, observation clock range, request channels and the activity codes seen on each day. Document every gap; a gap is a limitation, not automatically a reason for more observation.

**Stability** (checked separately in views A and B):

- **S1.** The two largest activity codes by time stay the same when any single day is left out.
- **S2.** Adding day 5 changes every activity code's cumulative time share by less than 5 percentage points.
- **S3.** Adding day 5 changes the cumulative rate per observed hour by less than 10% for each activity code with at least one occurrence per hour.
- **S4.** Adding day 5 changes every Van Weele stage's cumulative time share by less than 5 percentage points.

**Saturation.**

- **Q1.** Day 5 shows no activity code, stage or request channel that days 1 to 4 did not show.
- **Q2.** Kinds of work that appear for the first time on day 5, taken from the notes, are listed and judged as recurring or one-off.

**Outcome.** If coverage gaps are documented and S1 to S4 and Q1 to Q2 hold, Measure can close for Arno, subject to the supervisor's agreement. If a rule fails, the report names the gap and whether targeted observation would close it.

## Outputs

| File | Step |
|---|---|
| `analysis/build_combined_table.py` → `analysis/output/Arno_Combined_2026-09-30.csv` | 2: one table with all rows and the derived columns above |
| `analysis/five_day_check.py` → `analysis/Five_Day_Coverage_Check_2026-09-30.md` | 3: coverage, stability and saturation results |

Both scripts use only the Python standard library: run `python3 analysis/build_combined_table.py` and then `python3 analysis/five_day_check.py` from the repository root.
