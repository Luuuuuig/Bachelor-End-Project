# Analyze

Inputs for the Analyze phase that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) loads. Measure-phase data, including the kinds-of-work labels, codebook and framework map, stay in [`docs/measurement`](../measurement/README.md).

| File | Content | Used in |
|---|---|---|
| [`Arno_Causes_Draft_2026-10-06.csv`](Arno_Causes_Draft_2026-10-06.csv) | Draft causes for three candidate areas: ID, candidate, fishbone category, cause, evidence type (observed, earlier notes, reported, hypothesis), source, status after Yijie's answers of 2 October, and the answer. | Part 9: causes table and fishbone diagrams |

**History.** The causes were first typed into the notebook on 2 October and moved to this file on 6 October, without changing their content. The causes of the order checks are listed under "Purchase-price control", the candidate name in the [methodology](../methodology/Phase_1_Current_Methodology.md#41-active-primary-case-candidates); in the notebook the broader group of checks is "Order checks and price differences".

**Updating.** Keep `status` and `answer_2_oct` unchanged: they record the state after Yijie's answers of 2 October. Add Arno's later answers in new dated columns, for example `arno_check_2026-10-XX` (confirmed, changed, rejected or not discussed) and `arno_words_2026-10-XX`, and add new causes as new rows with an empty `answer_2_oct`. Then update part 9 of the notebook to show the new columns and rerun it.
