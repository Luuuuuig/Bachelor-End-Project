# Observation exposure review, 25 September 2026

The existing records confirm **351 net observed minutes across 31 August and 1 September**. The remaining three dates require a short confirmation from the observer. Their notebook headings and recorded task intervals do not establish when observation actually continued or stopped.

This review completes the arithmetic and documents the missing evidence. It does not manufacture net exposure, change raw observations, or rerun the workload analysis.

| Date | Recorded blocks or notebook headings | Block clock minutes | Recorded interval sum | Interval union | Confirmed net observation |
|---|---|---:|---:|---:|---:|
| 31 August | 10:30–12:27; 13:16–14:12 | 173 | 103 | 103 | 165 |
| 1 September | 10:31–12:30; 13:15–14:22 | 186 | 162 | 162 | 186 |
| 8 September | 10:30–12:23 | 113 | 106 | 106 | Unconfirmed |
| 18 September | 10:30–12:30; 13:00–15:00 | 240 | 196 | 196 | Unconfirmed |
| 23 September | 11:00–12:30; 13:00–14:26; 14:40–15:00 | 196 | 185 | 184 | Unconfirmed |

All quantities are minutes. The interval sum retains all source intervals, including scoped exclusions, contaminated episodes and intervals that establish elapsed boundaries only. It is not a total of verified active purchasing work.

## What each quantity means

- **Block clock time:** arithmetic from recorded session headings. Where observation boundaries and availability are unconfirmed, this is a notebook window, not a denominator for occurrence rates.
- **Recorded interval sum:** end minus start for every source row with both timestamps. Concurrent rows each keep their full recorded duration under the supervisor's adopted rule. Source intervals still need scope and timing-quality checks before becoming analysis minutes.
- **Interval union:** clock minutes covered by at least one recorded interval, counting simultaneous coverage once. This is an arithmetic check. It does not prove continuous observation or recover uncoded work.
- **Net observed time:** verified observation blocks minus observer absence or other periods when observation did not take place. An uncoded interval is not automatically an observer absence, a break, or inactivity.
- **Included scoped minutes:** eligible activity durations after scope and timing-quality checks. The existing four-session review has 91, 116, 32 and 121 minutes respectively, totalling 360. The completed 23 September enrichment adds 102 included minutes, with 15 further minutes held under scope review. These totals cannot replace observation exposure.

## Evidence and unresolved boundaries

**31 August.** The source explicitly states 111 morning minutes and 54 afternoon minutes. The morning window is 117 minutes with 11:11–11:17 observer unavailability. The afternoon window is 56 minutes with 13:38–13:40 buyer absence/not observed working. Thus 173 − 6 − 2 = 165. Uncoded intervals remain within confirmed observation exposure; they are not filled with invented activities.

**1 September.** The session coverage table explicitly states 119 morning minutes and 67 afternoon minutes, totalling 186. This carries forward the existing confirmed net figure. The arithmetic does not newly infer zero breaks for other sessions merely because no breaks are written.

**8 September.** The window spans 113 minutes, of which 106 have recorded timestamp intervals. Seven minutes lack a timed row. The source also excludes OBS-16 at 12:04–12:13 because the observer lost focus. This is a known nine-minute quality problem. The record does not establish overall observer availability, so neither 113 nor 104 can currently be called verified net exposure. If the observer confirms the full window and no additional unavailable periods, report 113 minutes of observation presence and 104 minutes after the recorded loss-of-focus interval is excluded from reliable event-capture exposure. State the definition used before calculating any rates.

**18 September.** The notebook headings span 240 minutes. Timed rows run 10:30–12:25 and 13:08–14:55, with internal gaps. The rows cover 196 distinct minutes. None of these quantities establishes whether the observer arrived at 13:00 or 13:08, stayed until the heading end, or took other breaks. Confirm actual blocks and any unavailable periods, including the edge intervals 12:25–12:30, 13:00–13:08 and 14:55–15:00.

**23 September.** The headings total 196 minutes, but OBS-12 CLAR ends at 12:31, one minute after the morning heading. If 12:31 is confirmed as the actual morning observation end, the three block lengths total 197 minutes before any unavailable periods are deducted. Keep the heading and row unchanged until that clarification is recorded.

The 185-minute recorded sum exceeds its 184-minute union by the intentional one-minute EXC/PO overlap at 11:42–11:43. Keep both activity intervals in full; do not deduct one minute from the PO. Overlap arithmetic concerns activity totals, not observer availability.

OBS-16 at 13:42–14:24 covers 42 elapsed minutes while Arno helped Maurice with a received item. The source does not establish that the observer followed him continuously, or that every minute was active work. Ask about observer presence separately from active task duration. This logistics/EXC episode remains excluded from thesis workload analysis regardless of the exposure answer.

Within the written 23 September headings, 183 minutes have a timed row and 13 minutes do not. One additional recorded minute lies outside the morning heading. Therefore simply subtracting the 184-minute union from the 196-minute headings would hide the one-minute boundary mismatch. The block CSV lists the uncovered intervals without interpreting them.

## Minimum questions for Yijie

Please confirm actual observation blocks and periods when you could not follow Arno. Approximate recollections should stay labelled approximate; they cannot become exact exposure denominators.

1. **8 September:** Were you observing from 10:30 to 12:23? During the flagged 12:04–12:13 interval, were you still present, and did loss of focus affect all nine minutes or only part? Give any other breaks or periods when you could not follow Arno, or confirm there were none.
2. **18 September:** Were you observing throughout 10:30–12:30 and 13:00–15:00, including the untimed edges at 12:25–12:30, 13:00–13:08 and 14:55–15:00? Give actual start/end times and any unavailable intervals if different.
3. **23 September:** Did the morning observation end at 12:31, and were the other actual blocks 13:00–14:26 and 14:40–15:00? Did you follow Arno continuously during 13:42–14:24 while he helped Maurice, or was observation unavailable for some/all of it? List any other unavailable intervals within the blocks.

There is no need to identify an activity for every blank minute to answer these questions. They concern observer presence and reliable capture. If the observer cannot remember a period, retain unknown exposure for that part and use the existing data for included-minute profiles, case comparison and qualitative patterns. Do not report pooled per-hour occurrence rates across unverified exposure.

## Files and reproducibility

- `Session_Exposure_Audit_2026-09-25.csv`: one row per date, explicitly blank unknown net values, evidence and questions.
- `Block_Clock_Coverage_2026-09-25.csv`: ten recorded blocks and all clock gaps lacking timed rows.
- `exposure_arithmetic_provenance.json`: raw source line references for each timed row and SHA-256 hashes.
- `build_exposure_audit.py`: reproducible arithmetic against the five source notes saved in `five_session_analysis_2026-09-25/sources`.

Checks: 225 timestamped source rows across five sessions; recorded interval sum 752 minutes; interval union 751 minutes; the only positive overlap is the confirmed minute on 23 September. The first four interval sums reproduce 567 minutes from the prior review. These are timestamp checks, not a five-session net-exposure estimate.
