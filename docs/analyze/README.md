# Analyze

Inputs for the Analyze phase that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) and the [focal-case selection notebook](../../Focal_Case_Selection_2026-10-07.ipynb) load. Measure-phase data, including the kinds-of-work labels, codebook and framework map, stay in [`docs/measurement`](../measurement/README.md).

Use the [current status and reading guide](../Current_Status_and_Reading_Guide.md) for the remaining work. The current comparison is provisional. The 45-record coding exercise is optional; the active plan is a documented targeted review of ambiguous and decision-relevant labels across competing candidates.

| File | Content | Used in |
|---|---|---|
| [`Arno_Causes_Draft_2026-10-06.csv`](Arno_Causes_Draft_2026-10-06.csv) | Draft causes for three candidate areas: ID, candidate, fishbone category, cause, evidence type (observed, earlier notes, reported, hypothesis), source, status after Yijie's answers of 2 October, and the answer. | Part 9: causes table and fishbone diagrams |
| [`Candidate_Evidence_Matrix_2026-10-07.md`](Candidate_Evidence_Matrix_2026-10-07.md) | Evidence, sources and remaining gaps supporting the existing provisional scores. Relevant gates, agreed weights and review remain necessary for final selection. | Candidate selection (Stage A and B) |
| [`Swing_Weights_Yijie_2026-10-07.md`](Swing_Weights_Yijie_2026-10-07.md) | Yijie's individual weights used for the provisional comparison. Combine with Zhongxin's independent set and freeze before final ranking. | Stage B weights and the sensitivity check |
| [`Swing_Weights_Yijie_2026-10-07.csv`](Swing_Weights_Yijie_2026-10-07.csv) | The same swings as a table, for the selection notebook. | Stage B totals |
| [`Stage_A_Gates_2026-10-07.csv`](Stage_A_Gates_2026-10-07.csv) | Provisional Stage A verdict per candidate and gate (Pass, Provisional pass, Redesign, Reject), with the reason and the check that confirms it. | Stage A in the selection notebook |
| [`Candidate_Scores_2026-10-07.csv`](Candidate_Scores_2026-10-07.csv) | Provisional Stage B score per candidate and criterion, with a low and high value for uncertainty and the evidence behind it. | Stage B and the sensitivity check |
| [`Stage_A_Test_Account_Check_2026-10-07.xlsx`](Stage_A_Test_Account_Check_2026-10-07.xlsx) | A menu of 31 common/candidate checks. G1–G2 permission is answered. Prioritize PC1–PC4 and relevant focal/common checks; investigate alternatives when needed. Record counts and locations only, no confidential content. | Data, reference-answer, risk and feasibility evidence; not a blanket 31-item completion gate |
| [`Analyze_Conclusion_Outline_2026-10-07.md`](Analyze_Conclusion_Outline_2026-10-07.md) | Outline of the Analyze conclusion: evidence base, provisional focal case and boundary, causes and their status, improvement directions, gates and open conditions, the step into Improve, limitations and the order of the remaining work. Names the provisional focal case, so it is shared with Zhongxin only after her swing weights. | Analyze chapter; Analyze → Improve tollgate |

**History.** The causes were first typed into the notebook on 2 October and moved to this file on 6 October, without changing their content. The causes of the order checks are listed under "Purchase-price control", the candidate name in the [methodology](../methodology/Phase_1_Current_Methodology.md#41-active-primary-case-candidates); in the notebook the broader group of checks is "Order checks and price differences".

**Updating.** Keep `status` and `answer_2_oct` unchanged: they record the state after Yijie's answers of 2 October. Add Arno's later answers in new dated columns, for example `arno_check_2026-10-XX` (confirmed, changed, rejected or not discussed) and `arno_words_2026-10-XX`, and add new causes as new rows with an empty `answer_2_oct`. Then update part 9 of the notebook to show the new columns and rerun it.
