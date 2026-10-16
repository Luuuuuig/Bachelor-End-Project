# Measurement

The Measure phase: how the observations were made, the records of each session, and the data the analysis uses.

## Status on 16 October 2026

- **Observation of Arno is complete:** seven sessions on 31 August, 1, 8, 18 and 23 September and 14 and 16 October, with **1,159 minutes** of confirmed observation (165, 186, 104, 240, 197, 184 and 83 minutes; see the [observation-time review](Observation_Time_Review_2026-09-25.md) and the [register](Observation_Time_Register_2026-09-25.csv)). The first five sessions (892 minutes) were analysed first; on 13 October it was decided to add exactly two more days ([meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-13.md)). The 28 August pilot stays separate.
- **The stages are agreed.** The seven daily CSVs carry the agreed `Van Weele stage`: the 287 rows of the first five days since 12 October, when 100 values changed from the previous version, and the 39 and 26 rows of 14 and 16 October since those days (stage review, sections 7 and 8); every row has a stage. The previous values are listed in the stage review's appendix; the column `Original Van Weele stage` that held them was removed on 16 October because no analysis reads it. The [stage review of 12 October](Stage_Review_2026-10-12.md) records the rules, the nine observer confirmations, the 15 rows from the context review and every change. The eight observation fields, row order, missing durations and recorded times are unchanged.
- **The analysis uses the original codes and the agreed stages only.** The kinds-of-work layer of 30 September to 9 October is archived in [docs/archive/kinds_of_work](../archive/kinds_of_work/README.md).
- **Dennis:** qualitative notes from [15 September](../meetings/Internship_notes_2026-09-15.md) and one timed observation on [25 September](Measure_Observation_2026-09-25.md), kept separate from Arno's data. His net observation time is not confirmed, so his record supports a separate task and handoff summary, not a per-hour comparison. Further Dennis observation addresses a specific remaining question after his return (decision of [1 October](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md)).
- **Still open:** Arno's answers to the questions of the [session guide](Arno_Follow_Up_Session_Guide_2026-10-02.md); since 13 October there is no separate session, the questions are to be asked in passing, and no answer is recorded yet.

## Files the analysis uses

| File | Content | Where used in the analysis notebook |
|---|---|---|
| `Arno_Measurement_<date>.csv`: [31 August](Arno_Measurement_2026-08-31.csv), [1 September](Arno_Measurement_2026-09-01.csv), [8 September](Arno_Measurement_2026-09-08.csv), [18 September](Arno_Measurement_2026-09-18.csv), [23 September](Arno_Measurement_2026-09-23.csv), [14 October](Arno_Measurement_2026-10-14.csv) (stages assigned on 14 October, [stage review, section 7](Stage_Review_2026-10-12.md#7-addendum-14-october-2026-the-sixth-observation-day)), [16 October](Arno_Measurement_2026-10-16.csv) (stages assigned on 16 October, [section 8](Stage_Review_2026-10-12.md#8-addendum-16-october-2026-the-seventh-observation-day)) | One row per recorded activity: the original eight observation columns and the agreed Van Weele stage | Everywhere; the selection notebook checks each file's SHA-256 against the committed version |
| [`Observation_Time_Register_2026-09-25.csv`](Observation_Time_Register_2026-09-25.csv) | Observation blocks and confirmed net observation per session | 3.1 (coverage per day), 4.3 (observed-clock denominator), 4.5 (requests per observed hour) |

The analysis notebook and the selection notebook read the same seven CSVs; the analysis of the first five as it stood on 13 October is kept as the [five-day notebook](../../Arno_Analysis_Five_Days_2026_10_13.ipynb). The [pilot CSV](Arno_Measurement_2026-08-28_Pilot.csv) is kept separate and is not analysed. The [stage review of 30 September](Stage_Review_2026-09-30.md) records the earlier stage decisions per session; the 12 October review supersedes its unresolved-stage status. The 21 and 25 September enrichment exports are in the [archive](../archive/README.md#measurement) and are not read by the notebooks.

## Totals

The frame the notebooks use, after leaving out the two 8 September OBS-16 rows recorded during a loss of observer focus (12:04 to 12:13, 9 minutes):

| Session | Rows | Timed rows | Recorded minutes | of which former EXC | In scope |
|---|---:|---:|---:|---:|---:|
| 31 August | 63 | 39 | 103 | 4 | 99 |
| 1 September | 50 | 42 | 161 | 38 | 123 |
| 8 September | 40 | 36 | 97 | 27 | 70 |
| 18 September | 74 | 57 | 196 | 47 | 149 |
| 23 September | 58 | 48 | 185 | 66 | 119 |
| *First five days* | *285* | *222* | *742* | *182* | *560* |
| 14 October | 39 | 32 | 170 | 83 | 87 |
| 16 October | 26 | 22 | 75 | 29 | 46 |
| **All seven days** | **350** | **276** | **987** | **294** | **693** |

With the two excluded rows the 8 September CSV holds 42 rows and 106 minutes, and the seven CSVs 352 rows (the first five 287); nothing is deleted from the files, the exclusion is a label in the notebook.

- **987 minutes** (742 on the first five days) are the recorded activity minutes the notebooks start from.
- **693 minutes** (560) are without former EXC. Since 1 October, former EXC (codes EXC, OTHER/EXC and, on 16 October, PO/EXC; 294 minutes, 182 on the first five days) is grouped under "OTHER (outside improvement)" and kept outside the improvement scope; its time stays in the totals ([meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md)).

Other conventions:

- Untimed rows count as occurrences but add no minutes. Since 2 October, the 1 September OBS-02 REQ row is a tally ([observer decision](Measure_Observation_2026-09-01.md#observer-decision-2-october-2026)). The 40 incoming requests (35 on the first five days) are all untimed; the 15 REQ-Exact markers (14) are earlier POs, not requests ([addendum](Scope_and_Classification_Addendum_2026-09-14.md)).
- Recorded minutes are activity minutes: the one-minute overlap on 23 September (11:42 to 11:43) counts in both activities, following the [rule for simultaneous activities](Scope_and_Classification_Addendum_2026-09-14.md#timing-of-simultaneous-activities).
- Stage "Not applicable" remains separate (32 in-scope minutes in 63 records; 25 in 55 on the first five days). Current stage assignments contain no blanks.
- A handwritten `/` in the observation sheets means none: no interruption in INT, no decision marked in DEC? ([recording marks](Scope_and_Classification_Addendum_2026-09-14.md#recording-marks)).
- Rates per hour use confirmed net observation from the time register, never the sum of recorded activity minutes.

## Recording rules and method

- [Measurement Protocol v1.3](Measurement_Protocol_v1.3.md): the recording rules from 2 September; its live fields and timing are the same as v1.2, used on 1 September. Older versions are in the [archive](../archive/README.md#measurement).
- [Scope and classification addendum](Scope_and_Classification_Addendum_2026-09-14.md): the scope decisions of 10 September and 1 October (logistics and former EXC), the Van Weele stages, simultaneous activities and recording marks. Read it with v1.3.
- [Measurement method justification](Measurement_Method_Justification.md): why structured continuous observation was used, and what it cannot show.
- [Live cheat sheet v1.3](Measure_Live_Cheat_Sheet_v1.3.md): the one-page observer guide.
- [Stage review of 12 October](Stage_Review_2026-10-12.md): the rules and the row-level record behind the agreed stages.

## Guides for further sessions

- [Session guide for Arno](Arno_Follow_Up_Session_Guide_2026-10-02.md): the priority walkthrough for the checking case, what an order check compares and how often, the explanations he still has to confirm, and which support he would accept.
- [Dennis observation guide](Dennis_Observation_Guide_2026-09-14.md): the preparation guide of 14 September, for any further session with Dennis that addresses a defined gap.

## Observation records

Each record holds the raw observation table of the session, the observer's corrections and, for most sessions, a post-session enrichment. The enrichment sections and their subtotals are historical; current figures come from the daily CSVs.

- [Pilot, 28 August](Pilot_Measure_Observation_2026-08-28.md) (outside the baseline)
- [31 August](Measure_Observation_2026-08-31.md), [1 September](Measure_Observation_2026-09-01.md), [8 September](Measure_Observation_2026-09-08.md) (OBS-16 lost focus), [18 September](Measure_Observation_2026-09-18.md), [23 September](Measure_Observation_2026-09-23.md), [14 October](Measure_Observation_2026-10-14.md) (afternoon mostly aftercare), [16 October](Measure_Observation_2026-10-16.md) (morning only; Arno came in on a day off to cover for Johan and Dennis)
- [Dennis, 25 September](Measure_Observation_2026-09-25.md); his purchasing activities are also described in the [15 September internship notes](../meetings/Internship_notes_2026-09-15.md)
- [Observation-time review](Observation_Time_Review_2026-09-25.md) and [register](Observation_Time_Register_2026-09-25.csv)

## Confidentiality

The repository is private. Company permission, confirmed by Yijie on 2 September, allows the recorded buyer names and case-specific commercial values to stay for the authorised research audience. The thesis anonymises or aggregates them; personal contact details, unrestricted production exports and new kinds of confidential data need separate approval.
