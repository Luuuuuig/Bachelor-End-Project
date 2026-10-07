# Analyze

Inputs for the Analyze phase that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) and the [focal-case selection notebook](../../Focal_Case_Selection_2026-10-07.ipynb) load. Measure-phase data, including the kinds-of-work labels, codebook and framework map, stay in [`docs/measurement`](../measurement/README.md).

| File | Content | Used in |
|---|---|---|
| [`Arno_Causes_Draft_2026-10-06.csv`](Arno_Causes_Draft_2026-10-06.csv) | Draft causes for three candidate areas: ID, candidate, fishbone category, cause, evidence type (observed, earlier notes, reported, hypothesis), source, status after Yijie's answers of 2 October, and the answer. | Part 9: causes table and fishbone diagrams |
| [`Candidate_Evidence_Matrix_2026-10-07.md`](Candidate_Evidence_Matrix_2026-10-07.md) | Evidence per candidate and Stage B criterion: what is known, with its source, and what is missing. No scores until the Stage A gates are checked and the weights are frozen. | Candidate selection (Stage A and B) |
| [`Swing_Weights_Yijie_2026-10-07.md`](Swing_Weights_Yijie_2026-10-07.md) | Yijie's individual swing weights, recorded before any candidate was scored; combined with Zhongxin's set and frozen before scoring. | Stage B weights and the sensitivity check |
| [`Swing_Weights_Yijie_2026-10-07.csv`](Swing_Weights_Yijie_2026-10-07.csv) | The same swings as a table, for the selection notebook. | Stage B totals |
| [`Stage_A_Gates_2026-10-07.csv`](Stage_A_Gates_2026-10-07.csv) | Provisional Stage A verdict per candidate and gate (Pass, Provisional pass, Redesign, Reject), with the reason and the check that confirms it. | Stage A in the selection notebook |
| [`Candidate_Scores_2026-10-07.csv`](Candidate_Scores_2026-10-07.csv) | Provisional Stage B score per candidate and criterion, with a low and high value for uncertainty and the evidence behind it. | Stage B and the sensitivity check |
| [`Stage_A_Test_Account_Check_2026-10-07.xlsx`](Stage_A_Test_Account_Check_2026-10-07.xlsx) | Worksheet for the Exact test-account check: 31 checks (account-wide and per candidate) with what to find out and how, and a gate summary per candidate (Pass, Redesign, Reject or Open). Records counts and locations only, no confidential content. | Stage A gates 1–3; data-readiness, prototype and evaluation cells of the evidence matrix |

**History.** The causes were first typed into the notebook on 2 October and moved to this file on 6 October, without changing their content. The causes of the order checks are listed under "Purchase-price control", the candidate name in the [methodology](../methodology/Phase_1_Current_Methodology.md#41-active-primary-case-candidates); in the notebook the broader group of checks is "Order checks and price differences".

**Updating.** Keep `status` and `answer_2_oct` unchanged: they record the state after Yijie's answers of 2 October. Add Arno's later answers in new dated columns, for example `arno_check_2026-10-XX` (confirmed, changed, rejected or not discussed) and `arno_words_2026-10-XX`, and add new causes as new rows with an empty `answer_2_oct`. Then update part 9 of the notebook to show the new columns and rerun it.
