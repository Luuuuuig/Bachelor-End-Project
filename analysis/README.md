# Analysis

Steps 1 to 3 of the Measure analysis for Arno, prepared on 30 September 2026. Dennis's data and the later steps (workload profile, workflow and Arno–Dennis relationship, candidate comparison) follow after the supervisor discussion.

| File | What it is |
|---|---|
| [Analysis_Plan_2026-09-30.md](Analysis_Plan_2026-09-30.md) | Step 1: units, denominators, the two views (all data / without EXC) and the proposed five-day check rules |
| [build_combined_table.py](build_combined_table.py) → [output/Arno_Combined_2026-09-30.csv](output/Arno_Combined_2026-09-30.csv) | Step 2: all 287 rows of the five reviewed daily CSVs in one table, with derived columns and flags; nothing dropped |
| [five_day_check.py](five_day_check.py) → [Five_Day_Coverage_Check_2026-09-30.md](Five_Day_Coverage_Check_2026-09-30.md) | Step 3: coverage, stability and saturation results |

To reproduce, run from the repository root (standard Python 3, no extra packages):

```
python3 analysis/build_combined_table.py
python3 analysis/five_day_check.py
```

The daily CSVs in `docs/measurement/` are only read, never changed.
