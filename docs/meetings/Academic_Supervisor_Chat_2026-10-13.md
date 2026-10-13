# Chat with the academic supervisor, 13 October 2026

**Channel:** Teams chat between Zhongxin Hu and Yijie Wang, 10:40 to 12:22 (local time). **Source:** the Teams export of the chat, read on 13 October; this record keeps the project-relevant content. **Topic:** the test for the work pattern across observation days, whether more observation data are needed, and the open questions of the update.

## Decisions

1. **Two more observation days: Wednesday 14 October and Friday 16 October** (12:03 to 12:11). Zhongxin proposed collecting one more day tomorrow; Yijie proposed Friday as well, to see whether a second Friday is again heavy on checking; Zhongxin: if both days are possible, collect both. Collecting is preferred over trying to prove that Fridays are special.
2. **Kendall's W, not Kruskal-Wallis, for the activity pattern across days** (10:55 to 11:15). The data are the in-scope minutes (or shares) per activity and day; both give the same result, because Kendall's W uses the ranks.
3. **The Thursday meeting of 15 October is cancelled** (12:14). Zhongxin reads the remaining update when she has time.
4. **The criteria, swing weights and the CHECK-per-line correction are not urgent** (12:05).

## To write into the thesis (11:13)

1. **Why Kendall's W, and not other tests (including Kruskal-Wallis).**
2. **Why this data table**, in the data-preprocessing or data-preparation section.

Draft wording for both is in the [Analyze outline, section 11](../analyze/Analyze_Conclusion_Outline_2026-10-07.md#11-to-write-into-the-thesis-zhongxin-13-october).

## Course of the chat

- **10:40.** Yijie sent the summary of the Kruskal-Wallis tests, the seven criteria with the swing weights and the corrected CHECK-per-line figures, and asked whether more data were needed before Arno's leave and whether the existing CHECK data could serve as the manual baseline.
- **10:50 to 10:58.** Zhongxin asked to see the Kruskal-Wallis data and proposed Kendall's W instead. The table she had in mind has the activities as rows, the days as columns and each activity's time on each day as cells. She noted that the Kruskal-Wallis test on episode lengths by day measures whether the working time is fragmented.
- **11:00 to 11:03.** The purpose was confirmed: the final aim is to find which activity should be prioritised for optimisation, and this step reasons backwards to whether more data are needed, by testing whether the time allocation over the activities is the same from day to day.
- **11:05.** Zhongxin: with p > 0.05 a nonparametric test can only say that no significant difference was found; it cannot prove the same distribution. Logically "no more data needed" cannot be fully inferred from it, but a BEP need not be that strict.
- **11:06 to 11:10.** On 8 October Zhongxin had named the Kruskal-Wallis test (see the [8 October notes](Academic_Supervisor_Meeting_Notes_2026-10-08.md)). After Yijie showed the recording, she agreed that she had named the wrong test.
- **11:09.** Zhongxin considered adding a measure of whether the time allocation is consistent across days.
- **11:28.** Yijie sent the Kendall's W result: W = 0.42, Friedman chi-square = 8.48, df = 4, p = 0.075; pairwise rank correlations and the result with each day left out.
- **11:38 to 11:39.** Zhongxin found the result "not very positive" and asked whether the minutes were divided by the number of orders. Yijie: the number of orders per day was not recorded. (Dividing every activity of a day by any per-day count leaves the ranks, and W, unchanged; checked afterwards with the case-days per day.)
- **11:41.** Zhongxin asked for a Jensen-Shannon divergence. **11:48:** Yijie sent the result: mean JSD over the 10 pairs of days 0.113, against 0.075 when whole case-days are shuffled between the days (p = 0.089); per day only 8 September differs more than chance (p = 0.010), 18 September is borderline (p = 0.090).
- **11:49 to 11:50.** Zhongxin's interpretation of Kendall's W: the time spent on the activities is consistent to some degree but not strongly, so there is no single clearly most time-consuming activity, which is why other criteria are added to choose the activity to optimise. The shares are similar to some degree, but some dates differ clearly, mainly 8 and 18 September.
- **11:56.** Zhongxin: data collected just before Arno's leave might not be typical either. Yijie: 8 September was cut short by a company event for the interns, and 18 September might reflect a Friday effect, when many of the week's orders get an update. (The [observation-time register](../measurement/Observation_Time_Register_2026-09-25.csv) shows 8 September as the only session without an afternoon block: 10:30 to 12:23.)
- **11:57 to 12:02.** Zhongxin's options: explain why 8 September is special, or add one more day, which might not help. She left the decision to Yijie, separated the interpretation of Kendall's W from the question of more data (which rests on the JSD result), and gave her standard: the analysis should be scientific and the conclusions and reasoning rigorous and correct; a BEP is about experiencing the research process, and limited data are acceptable.
- **12:03 to 12:11.** Decision 1 above. Zhongxin suggested that, if the new data turn out well, the thesis explains in the data processing and analysis why the extra days were collected after the first five.
- **12:12 to 12:22.** Arno's leave starts at the end of October. The Thursday meeting is cancelled; Zhongxin will read the remaining update later.

## How the extension is reported

The two days are added after the five-day analysis, so the extension is reported as a sequential decision, fixed in advance of the new data:

- exactly two days (14 and 16 October), with the same protocol and a morning and an afternoon block, whatever their result;
- all seven days are kept, including 8 and 18 September; no day is removed because it does not fit;
- the five-day results stay in the analysis as the first analysis and are reported next to the seven-day results;
- the thesis states when and why the extension was decided (13 October: moderate agreement, 8 and 18 September deviating, the Friday question).

## Open

- Collect and code the two days with protocol v1.3; add them to the observation-time register; assign their stages with the rules of the [stage review](../measurement/Stage_Review_2026-10-12.md); rerun both notebooks on seven days.
- Ask Arno to confirm what happened on 8 and 18 September.
- Daily counts of supplier confirmations and purchase orders from Exact over recent months, to see how often check-heavy days occur.
- The criteria, swing weights and the CHECK-per-line correction wait for Zhongxin's reading of the update.
