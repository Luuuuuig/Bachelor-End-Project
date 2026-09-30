# Repository consistency check, 30 September 2026

**Scope:** `main` at `37ea223` and the unmerged branch `claude/cool-keller-f5kanx`. The final Plan of Work (PDF dated 22 September 2026) is used as a reference only. This check changes no observation, enrichment or planning file. It records what agrees, what conflicts and what must be settled before the Measure data are analysed.

## 1. Verified as consistent

| Check | Result |
|---|---|
| Source preservation | All 317 enriched CSV rows (259 in the 21 September dataset, 58 in the 23 September CSV) still appear verbatim in their source observation notes. |
| Enrichment commits | The 23 and 25 September enrichment commits only added lines. No raw observation line was removed. |
| Interval arithmetic | End minus start equals the recorded minutes on every timed CSV row. |
| Included minutes | Recomputed totals match the documented values: pilot 59; 31 Aug 91; 1 Sep 116; 8 Sep 32; 18 Sep 121; 23 Sep 102. |
| 23 September note versus CSV | 58 markdown rows equal 58 CSV rows, field by field: case, family, interval, activity, stage, confidences, Task IDs, scope and included minutes. The reconciliation table (38 included / 10 review / 9 EXC / 1 logistics; 102 / 15 / 66 / 2 minutes) is correct. |
| 25 September (Dennis) | 41 rows, 35 timed and 6 untimed, 162 recorded minutes, as stated. Derived scope split: included 48, review 47, EXC 50, aftercare 15 and business administration 2 minutes. |
| Session windows | Block arithmetic is correct: 173 and 165 net (31 Aug), 186 (1 Sep), 113 (8 Sep), 240 (18 Sep), 196 (23 Sep) and 181 (Dennis, 25 Sep). |
| Register hashes | Source hashes in the time register match the files for 31 August to 18 September. For 23 September, the hash reproduces only the raw section before the enrichment heading, not the whole file at the pinned commit. This is a minor provenance note. |

## 2. Conflicts that affect the analysis

### 2.1 Timing rule for simultaneous activities

The 23 September enrichment and the measurement README (25 September) apply the supervisor's 17 September suggestion, so each confirmed concurrent activity keeps its full interval. Four other files still say this rule is **not** adopted and that a change needs a dated timing definition:

- `measurement/Scope_and_Classification_Addendum_2026-09-14.md`, section "Timing continuity";
- `process/Purchasing_Activity_Framework_2026-09-21.md`, final section;
- `measurement/Measurement_Method_Justification.md`, line 79;
- `proposal/Plan_of_Work_Academic_Draft_2026-09-14.md`, line 75 ("each minute is counted once").

No dated timing addendum exists. The effect so far is one minute (23 September, 11:42 to 11:43), but the rule determines whether shares are reported as activity minutes or as buyer elapsed time. **Action:** add a short dated timing rule and point the four files to it.

### 2.2 Enriched data are split across three formats

| Source | Rows | Format | Coverage |
|---|---:|---|---|
| `Activity_Framework_Enriched_Observations_2026-09-21.csv` / `.xlsx` | 259 | 39 columns | Pilot, 31 Aug, 1, 8 and 18 Sep |
| `23_September_Enriched_Rows_2026-09-25.csv` | 58 | 65 columns (adds "Reviewed ..." and analysis columns) | 23 Sep |
| `Measure_Observation_2026-09-25.md` | 41 | Markdown table only | Dennis, 25 Sep |

Label vocabularies also differ, although each mapping is one to one:

- **Stage:** the CSVs use `Unresolved stage` and `Not applicable`; the scope addendum defines `VW1`-`VW6`, `MULTI`, `UNKNOWN` and `NA`; the 18 September note uses VW codes; the 25 September note uses stage names with `UNKNOWN`.
- **Scope:** the addendum defines only `EXCLUDE_EXC` and `REVIEW_SCOPE`. `EXCLUDE_AFTERCARE` and `EXCLUDE_LOGISTICS` are defined in the 8 and 18 September notes. `EXCLUDE_BUSINESS_ADMIN` and `EXCLUDE_SALES` first appear on 25 September.

**Action:** build one combined analysis table for Arno and a separate one for Dennis, with the labels harmonised. No row needs re-coding.

### 2.3 Observation exposure is confirmed for two of five Arno sessions

Only 31 August and 1 September (351 minutes) have confirmed net observation. The 8, 18 and 23 September sessions, and Dennis's 25 September session, need the observer questions in `measurement/Observation_Time_Review_2026-09-25.md`. Time shares can be calculated now. Occurrence rates per hour cannot.

### 2.4 Scope review is still open

| Session | Review rows | Review timed minutes | Included minutes |
|---|---:|---:|---:|
| 1 Sep | 4 | 5 | 116 |
| 8 Sep | 8 | 15 | 32 |
| 18 Sep | 8 | 17 | 121 |
| 23 Sep | 10 | 15 | 102 |
| Dennis, 25 Sep | 10 | 47 | 48 |

The 52 baseline review minutes are about 11% of the 462 included minutes. For Dennis, the review time is about the same as the included time. The open questions are listed at the end of the 23 September (five) and 25 September (five) notes.

### 2.5 Unmerged analysis branch is outdated

`claude/cool-keller-f5kanx` contains a Day-5 exploratory analysis written before the 23 September enrichment was completed. It used a provisional script rule that yields 95 included minutes for 23 September, not 102. It moved the 12-minute Exact fault to review, dropped the concurrent PO row and included the eight-minute service-order case. Its figures are superseded. **Action:** rerun the analysis on the enriched data rather than merging the branch as it is.

## 3. Outdated status and index text

| File | Current text | State of the evidence |
|---|---|---|
| `README.md`, line 31 | "Three official Arno sessions" | Five sessions (31 Aug; 1, 8, 18 and 23 Sep) plus Dennis records on 15 and 25 Sep |
| `docs/README.md`, lines 15 and 148 | "Last synchronized 2 September"; three sessions; meeting list ends on 31 August | As above |
| `docs/Project_Charter.md`, line 65; `docs/Project_Timeline.md`, line 11 | Three sessions | As above |
| `docs/methodology/Phase_1_Current_Methodology.md`, line 143 | Four sessions through 18 September | As above |
| `docs/measurement/README.md`, "Observation evidence" | List ends on 18 September | 23 September appears only in the 25 September section; Dennis's 25 September record is not indexed anywhere |
| `docs/meetings/README.md` | Latest records end on 8 September | The 9, 10, 15 and 17 September notes are not listed |
| `docs/measurement/Observation_Time_Review_2026-09-25.md`, "Files and reproducibility" | Four files and a `sources` folder | None of them is in the repository; only the register CSV exists |

## 4. Protocol versus practice

Rule 3 of the scope addendum says that from 14 September EXC is no longer timed as a work family and that pauses in eligible work are recorded instead. The 18, 23 and 25 September notebooks still time EXC (13, 9 and 7 rows). This is harmless for the included profile, because those rows are excluded, and it helps show where observation left eligible work. **Suggestion:** update the rule so EXC is accepted as a live exclusion marker, rather than changing current practice.

## 5. Differences from the final Plan of Work (reference)

- **Research questions:** the repository's Plan of Work draft, the BEP assignment and the methodology use four sub-questions. The final Plan of Work has five. It adds a new SQ1 (standard workflow and the operational-tactical relationship), keeps SQ2 (conditions and controls), and renumbers workload contributors as SQ3, selection as SQ4 and evaluation as SQ5. `Phase_1_Current_Methodology.md` (line 105) and the activity framework both still refer to "four sub-questions". The analysis should use the final numbering.
- **Title:** "Reduce Operational Purchasing Workload at Hytech-Pommec using AI" in the BEP assignment, "AI-supported operational procurement" in the draft and half-page description, and "AI-supported operational purchasing" in the final Plan of Work.
- **Study load:** `Project_Timeline.md` says 420 hours combined for 1BEPIE and 1BEPIEX. The final Plan of Work says 420 hours for 1BEPIEX. This needs confirmation.
- **Operational boundary:** the draft says "from the purchasing need"; the final text says "from the purchasing request".
- **Source file:** the final Plan of Work is not in the repository.

## 6. Needed before the analysis

1. The observer answers on exposure for 8, 18 and 23 September, and for Dennis on 25 September.
2. Answers to the open scope questions in the 23 and 25 September notes. The Gimi case also refers to an earlier note that could not be located.
3. A dated timing rule for simultaneous activities (section 2.1).
4. Once enrichment is complete: build the harmonised analysis tables (section 2.2), update the indexes (section 3), and run the workload profile for final-PoW SQ1 and SQ3 before candidate comparison for SQ4.
