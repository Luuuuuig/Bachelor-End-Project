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
| Friedman chi-square | 8.48, df = 4, p = 0.075 (permutation p = 0.066) |
| Mean pairwise Spearman correlation between days | 0.28 |
| Mean correlation of each day with the other four | 31 Aug 0.48, 1 Sep 0.52, 8 Sep 0.08, 18 Sep −0.12, 23 Sep 0.45 |
| Leave one day out | without 31 Aug W = 0.36 (p = 0.22); 1 Sep 0.34 (0.25); 8 Sep 0.56 (0.06); 18 Sep 0.66 (0.03); 23 Sep 0.38 (0.20) |

Minutes and shares of the day give identical ranks within each day, so the result does not depend on the denominator. 31 August, 1 September and 23 September agree strongly (rank correlations 0.7 to 0.8); 8 and 18 September deviate. PO and CLAR are each among the two largest activities on four of the five days, both together on three. With five days the test has low power (below one half even if the pattern is real).

## To write into the thesis (Zhongxin, 11:13)

1. **Why Kendall's W, and not other tests (including Kruskal-Wallis)** must be explained in the thesis.
2. **Why this data table** can be explained in the thesis, in the data-preprocessing or data-preparation section.

Draft wording for both is in the [Analyze outline, section 11](../analyze/Analyze_Conclusion_Outline_2026-10-07.md#11-to-write-into-the-thesis-zhongxin-13-october).

## Addendum, 11:38 to 11:41

- Zhongxin found the Kendall's W result "not very positive" and asked whether the minutes had been divided by the number of orders. Yijie answered that the number of orders per day was not recorded. Dividing every activity of a day by any per-day count leaves the ranks, and W, unchanged (checked with the case-days per day: W = 0.42 either way); the real number of orders per day can be taken from Exact. The volume does explain 18 September: its case-days (24) and PO records (11) were ordinary, but 42 of the 71 checked order lines fell on that day, at an ordinary time per line.
- Zhongxin asked for a **Jensen-Shannon divergence** as well: the whole allocation structure of each day compared between days, all 10 pairs of days, and the mean. JSD has no fixed threshold, so the reference is built by shuffling whole case-days between the days (10,000 shuffles). Result, now in section 4.3 of the analysis notebook: mean JSD over the pairs 0.113 bits, against 0.075 by chance (p = 0.089); per day only 8 September diverges more than chance (p = 0.010), 18 September is borderline (p = 0.090).

## Addendum, 11:49 to 12:02: interpretation and the decision on more data

- **Interpreting Kendall's W (Zhongxin, 11:49).** Because the time spent on the activities is consistent to some degree but not strongly, there is no single clearly most time-consuming activity; that is why other criteria are added to decide which activity to improve. In the notebook "not strongly" is based on W = 0.42 (moderate agreement) rather than on the p-value: the top activity changes from day to day (CLAR two days, PO two days, CHECK one day), and PO (29.5%) and CLAR (27.7%) are nearly equal overall.
- **Whether to add data is decided on the JSD result (Zhongxin, 12:02),** which singles out 8 September. Her options (11:57): explain why 8 September is special, or add one more day, which might not help; she also noted (11:56) that data collected just before Arno's leave might not be typical either. She left the decision to Yijie.
- **Decision (Yijie, 12:01): explain 8 and 18 September; no further observation day.** 8 September is the shortest session (70 in-scope minutes) with several exceptions recorded as OTHER (a problem order discussed with Johan, a supplier that could not deliver, coordination through Dennis); 18 September's difference comes from its checking volume (42 of 71 checked order lines) at an ordinary time per line.
- **Zhongxin's standard (12:01):** the analysis should be scientific and the conclusions and reasoning rigorous and correct; a BEP is about experiencing the research process, and limited data are acceptable.

## Open after the chat

- Done: Kendall's W, the Jensen-Shannon divergence, the explanation of 8 September and the decision on more data are in section 4.3 of the analysis notebook; sections 4.4 and 9 and the executive summary follow.
- Ask Arno before his leave to confirm what happened on 8 and 18 September.
- Daily counts of supplier confirmations and purchase orders from Exact over recent months, to see how often check-heavy days occur and whether they fall on Fridays.
