# Analyze

Inputs for the Analyze phase that the [analysis notebook](../../Arno_Analysis_2026_10_02.ipynb) loads. Measure-phase data, including the kinds-of-work labels, codebook and framework map, stay in [`docs/measurement`](../measurement/README.md).

| File | Content | Used in |
|---|---|---|
| [`Arno_Causes_Draft_2026-10-06.csv`](Arno_Causes_Draft_2026-10-06.csv) | Draft causes for three candidate areas: ID, candidate, fishbone category, cause, evidence type (observed, earlier notes, reported, hypothesis), source, status after Yijie's answers of 2 October, and the answer. | Part 9: causes table and fishbone diagrams |

**History.** The causes were first typed into the notebook on 2 October and moved to this file on 6 October, without changing their content. The candidate "Order checking and discrepancy handling" is named "Purchase-price control" here, as in the [methodology](../methodology/Phase_1_Current_Methodology.md#41-active-primary-case-candidates).

**Updating.** After the session with Arno, change the `status` and `answer_2_oct` columns (or add a column for Arno's answer) and add new causes as new rows. Rerun the notebook to redraw the fishbones.
