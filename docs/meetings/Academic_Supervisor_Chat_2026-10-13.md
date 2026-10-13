# Chat with the academic supervisor, 13 October 2026

**Channel:** Teams chat between Zhongxin Hu and Yijie Wang, 10:50 to 11:13. **Recorded by:** Yijie, from the chat. **Topic:** the test for the work pattern across observation days, and whether more observation data are needed.

## What was discussed

- Zhongxin asked to see the data behind the Kruskal-Wallis tests. Yijie sent the episode-length table (episodes per recorded length and day) and the table of in-scope minutes per activity code and day.
- Zhongxin proposed **Kendall's W** instead of Kruskal-Wallis for the question she had in mind: whether the time is distributed over the activities in the same way on each day. The data for it are the table with the activity codes as rows, the days as columns and the minutes of each activity on each day as cells.
- Zhongxin noted that the Kruskal-Wallis test on episode lengths by day answers a different question: whether the working time is equally fragmented on each day.
- The purpose was confirmed: to reason backwards to whether additional data are needed, by testing whether the time-allocation pattern across activities is the same from day to day.
- Zhongxin pointed out that a nonparametric test with p > 0.05 only shows that no significant difference was found; it cannot prove that the groups follow the same distribution. Logically, "no additional data needed" therefore cannot be fully inferred from such a result, but she felt a BEP need not be that strict.
- On which test was named on 8 October: neither remembered exactly. The [8 October meeting notes](Academic_Supervisor_Meeting_Notes_2026-10-08.md) (recording 25:34 to 27:15) record that she shared a table of statistical methods and pointed to the Kruskal-Wallis test, and described the days-by-activities table with shares as cells.
- Zhongxin considered adding a measure of whether the time allocation is consistent across days, for more rigor. Kendall's W is that measure; the pairwise rank correlation between days complements it.

## Results shared in the chat

Kendall's W on the in-scope minutes per activity and day (PO, CLAR, CHECK, SEND, OTHER; the one UNCLEAR minute left out):

| Measure | Value |
|---|---|
| Kendall's W | 0.42 |
| Friedman chi-square | 8.48, df = 4, p = 0.076 (permutation p = 0.066) |
| Mean pairwise Spearman correlation between days | 0.28 |
| Mean correlation of each day with the other four | 31 Aug 0.48, 1 Sep 0.52, 8 Sep 0.08, 18 Sep −0.12, 23 Sep 0.45 |
| Leave one day out | without 31 Aug W = 0.36 (p = 0.22); 1 Sep 0.34 (0.25); 8 Sep 0.56 (0.06); 18 Sep 0.66 (0.03); 23 Sep 0.38 (0.20) |

Minutes and shares of the day give identical ranks within each day, so the result does not depend on the denominator. 31 August, 1 September and 23 September agree strongly (rank correlations 0.7 to 0.8); 8 and 18 September deviate. PO and CLAR are each among the two largest activities on four of the five days, both together on three. With five days the test has low power (below one half even if the pattern is real).

## To write into the thesis (Zhongxin, 11:13)

1. **Why Kendall's W, and not other tests (including Kruskal-Wallis)** must be explained in the thesis.
2. **Why this data table** can be explained in the thesis, in the data-preprocessing or data-preparation section.

Draft wording for both is in the [Analyze outline, section 11](../analyze/Analyze_Conclusion_Outline_2026-10-07.md#11-to-write-into-the-thesis-zhongxin-13-october).

## Open after the chat

- Add the Kendall's W cell, with the pairwise correlations and the leave-one-day-out results, to the analysis notebook (section 4.3 or 4.4); keep the Kruskal-Wallis test on episode lengths as a supplementary result on fragmentation, and the Kruskal-Wallis test on CHECK minutes per line as it is.
- Zhongxin's agreement on further observation is not yet explicit. Yijie's proposal: no further general observation; daily counts of supplier confirmations and purchase orders from Exact over recent months, to see how often days like 18 September occur and whether they fall on Fridays (18 September was the only Friday observed); and a short question to Arno before his leave about what happened on 18 September.
