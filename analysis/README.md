# Analysis

Steps 1 to 3 of the analysis for Arno, prepared on 30 September 2026, form the Measure review of the five baseline sessions; step 4 starts Analyze. The review supports pausing broad observation and starting Analyze for Arno; conclusions that depend on the EXC decision or on Dennis's data stay provisional until the supervisor discussion.

| File | What it is |
|---|---|
| [Analysis_Plan_2026-09-30.md](Analysis_Plan_2026-09-30.md) | Step 1: units, denominators, the two views (all data / without EXC), the five-day check and the next Analyze steps |
| [build_combined_table.py](build_combined_table.py) → [output/Arno_Combined_2026-09-30.csv](output/Arno_Combined_2026-09-30.csv) | Step 2: all 287 rows of the five reviewed daily CSVs in one table, with derived columns and flags; nothing dropped |
| [kinds_of_work_review.py](kinds_of_work_review.py) → [Kinds_Of_Work_Review_2026-09-30.md](Kinds_Of_Work_Review_2026-09-30.md) and [output/Kinds_Of_Work_Rows_2026-09-30.csv](output/Kinds_Of_Work_Rows_2026-09-30.csv) | Step 3: the kinds of work in each row, when each first appeared, whether it recurred and what it adds |
| [five_day_check.py](five_day_check.py) → [Five_Day_Coverage_Check_2026-09-30.md](Five_Day_Coverage_Check_2026-09-30.md) | Step 3: coverage, stability, CHECK and saturation results |
| [workload_profile.py](workload_profile.py) → [Workload_Profile_Arno_2026-09-30.md](Workload_Profile_Arno_2026-09-30.md) | Step 4 (Analyze, sub-question 3), draft: Arno's time, frequency, volume and difficulty cues by code, stage, kind of work and candidate; provisional |
| [Measure_Review_Fit_and_Saturation.ipynb](Measure_Review_Fit_and_Saturation.ipynb) | For the supervisor discussion: whether episode durations fit a distribution (lognormal, allowing for whole-minute clock readings), whether the fit and the time shares stay stable when one day is left out, and how many new kinds of work each day adds |

To reproduce the scripts, run from the repository root (standard Python 3, no extra packages):

```
python3 analysis/build_combined_table.py
python3 analysis/kinds_of_work_review.py
python3 analysis/five_day_check.py
python3 analysis/workload_profile.py
```

The notebook reads the outputs above and needs `numpy`, `scipy`, `pandas` and `matplotlib`; open it from the `analysis/` folder and run all cells. It is saved with its results, so it can also be read on GitHub without running it.

The daily CSVs in `docs/measurement/` are only read, never changed.
