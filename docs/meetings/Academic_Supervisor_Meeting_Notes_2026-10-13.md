# Academic Supervisor Meeting Notes, 13 October 2026

## 1. Meeting Overview

- **Date:** 13 October 2026.
- **Time:** The chat ran from 10:40 to 12:22 CEST.
- **Attendees:** Yijie Wang and Zhongxin Hu, academic supervisor.
- **Meeting type:** BEP academic supervision, conducted as a written Teams chat.
- **Purpose:** Review Yijie's written update (the Kruskal-Wallis results, the seven selection criteria with swing weights and the corrected CHECK-per-line figures), settle which test and which data table to use for the activity pattern across observation days, and decide whether more observation data are needed before Arno's leave.
- **Source:** The Teams chat export of 13 October (10:40 to 12:22). Times below are clock times of the chat messages. Test results were shared as screenshots; the figures quoted are those of the analysis notebook that produced them.

## 2. Executive Summary

Hu replaced the Kruskal-Wallis test with Kendall's W for the activity pattern across observation days, to be run on the table of time per activity and observation day, and agreed that she had named the wrong test on 8 October. Kendall's W gave moderate agreement (**W = 0.42**, **p = 0.075**) and the Jensen-Shannon divergence singled out 8 September, with 18 September borderline; Hu read this as no single clearly most time-consuming activity, which supports adding further criteria to choose the activity to optimise. Yijie will collect two more observation days, on Wednesday 14 and Friday 16 October, and write into the thesis why Kendall's W and why this data table; the remaining items of the update were declared not urgent and the 15 October meeting was cancelled.

## 3. Key Discussion Points

### Yijie's written update and open questions

**Chat: 10:40–10:42**

- Yijie reported two Kruskal-Wallis tests. On activity handling time across the **5** observation days (**182** in-scope activity records) he obtained **H = 2.76, p = 0.60**; on CHECK handling time per order line, 18 September against the other days, **H = 0.66, p = 0.42**. Neither showed a statistically significant difference. He noted that this did not show that the five days had the same work pattern, nor that the daily activity shares were stable.
- He asked whether, given these results, no further data needed to be collected. He explained that the question was pressing because Arno's leave was approaching and any further collection would have to follow quickly.
- He presented seven selection criteria with provisional swing weights: workload contribution (swing **100**, **27.0%**), business value (**40**, **10.8%**), AI suitability (**50**, **13.5%**), data readiness (**60**, **16.2%**), repetitiveness and standardisation (**30**, **8.1%**), technical feasibility (**40**, **10.8%**) and evaluation feasibility (**50**, **13.5%**); total swing **370**. His proposed procedure was to apply six non-compensatory feasibility conditions first and then the weighted score.
- He asked whether the seven criteria were reasonable, whether any overlapped or were missing, and whether Hu wanted to set her own swing weights or review and adjust his.
- He corrected the CHECK-per-line figures: **0.90 minutes per line on 18 September**, **0.83** on the other observation days and **0.87** overall. The difference between 18 September and the other days is about **4.6 seconds per line**; the **1.8 seconds** quoted on 8 October referred to the overall average. He asked whether Hu's earlier judgement that a small absolute difference was acceptable still held.
- He also asked whether the existing CHECK data could serve directly as the manual handling-time baseline for the later AI evaluation, or whether separate baseline data had to be collected.
- The questions on the criteria, the weights, the corrected CHECK difference and the baseline were not answered in the chat; see the last topic below.

### Which data table and which test

**Chat: 10:50–11:03 and 11:14–11:15**

- Hu asked to see the data used for the Kruskal-Wallis test and, after checking, proposed that the appropriate test was **Kendall's W**, not Kruskal-Wallis.
- Yijie sent a screenshot of the first table. Hu asked what its rows in minutes meant; Yijie explained that the rows were individual activity records, for example nine records of under one minute on one day. Hu concluded that a test on that table analyses whether the working time is fragmented.
- Hu described the table she had in mind: **activity categories as rows**, **observation days as columns**, and **the time spent on each activity on each day as the cell values**. Yijie sent a screenshot of this table as well.
- Hu first confirmed the purpose: the final aim is to find which activity should be prioritised for optimisation. Yijie noted that the present step was about whether additional data were needed; Hu agreed and said she was reasoning backwards from the final aim. The question to test is therefore whether the allocation of working time over the activities is the same from day to day, which is why the rows should be the working time of the different activities.
- Yijie asked to confirm that Kendall's W on this table would decide whether he needed additional data. Hu asked him to run this test first, before the rest of the update.
- Hu confirmed the table to use: the upper part in minutes and the lower part in percentages. Either can be used, because Kendall's W tests the ranking.

### Limits of the inference, the test named on 8 October and two items for the thesis

**Chat: 11:05–11:13**

- Hu noted a limitation of nonparametric tests: with **p > 0.05** one can only say that no significant difference was found; the tests cannot prove that the days follow the same distribution. Logically, "no additional data needed" therefore cannot be fully inferred from such a result, but she considered that a BEP need not be that strict.
- Yijie asked whether he had misremembered the test or Hu had misspoken on 8 October. Hu did not remember and recalled seeing the abbreviation KW at that meeting. After Yijie showed a screenshot from the 8 October recording, Hu agreed that she had named the wrong test.
- Hu considered adding a further measure of whether the time allocation is consistent across days, to make the analysis more rigorous.
- Hu stated that the explanation of **why Kendall's W is used and not other tests (including Kruskal-Wallis)** needs to go into the thesis, and that **why this data table was chosen** can also go into the thesis, in the data preprocessing or data preparation section. Yijie agreed.

### Kendall's W and Jensen-Shannon divergence results

**Chat: 11:28–11:55**

- Yijie sent the Kendall's W result: **W = 0.42**, Friedman chi-square **8.48**, **df = 4**, **p = 0.075**.
- Hu found the result "not very positive" and asked whether the minutes had been divided by the number of orders. Yijie said they had not, because the number of orders per day had not been recorded.
- Hu asked for a Jensen-Shannon divergence as well. Yijie sent the result: a mean JSD of **0.113** over the **10** pairs of days, against **0.075** by chance when whole case-days are shuffled between the days (**p = 0.089**); per day, only 8 September differed more than chance (**p = 0.010**), with 18 September borderline (**p = 0.090**).
- Hu's interpretation of Kendall's W: the time spent on the activities is consistent to some degree but not strongly (**0.05 < p < 0.1**), so there is no single clearly most time-consuming activity; that is why further evaluation criteria are added to decide which activity to optimise.
- Hu's reading of the divergence: the time-allocation shares show some similarity, but some dates differ clearly, mainly **8 and 18 September**.

### Whether more observation data are needed

**Chat: 11:56–12:12**

- Hu wondered whether data collected shortly before Arno's leave might also be atypical.
- Yijie asked whether the two deviating days could be interpreted as follows: 8 September was interrupted by a company event for the interns, and 18 September reflects a Friday effect, because many of the week's orders receive an update on Friday.
- Hu set out the options: either explain why the data of 8 September are special, or add one more day of data, which might not help. She left the decision to Yijie.
- Yijie said he leaned towards Hu's interpretation of Kendall's W, followed by an explanation of 8 and 18 September. Hu replied that this interpretation explains the Kendall's W result, whereas the question of adding data concerns the JSD result.
- Hu's standard: the analysis should be scientific and the conclusions and inferences rigorous and correct; a BEP is about experiencing the research process, and limited data are acceptable if that is what is available.
- Hu then suggested collecting one more day the next day. Yijie agreed, repeating her own caveat that one extra day might not change the result. Hu advised adding the day first and then judging the result. If the result is good, the thesis should explain deliberately, in the data processing and analysis, why that day was collected so much later than the others: five days were collected first, the conclusion was not good, and another day was added. If the result is not good, that would be considered then.
- Yijie asked whether to collect on Wednesday or on Friday, reasoning that a second check-heavy Friday would support the Friday explanation of 18 September, with 8 September then classed as cut short by the company event. Hu preferred Wednesday, so that the atypical Friday data could be dropped, and considered this more important than proving that Fridays are really unusual. She added that if both Wednesday and Friday were possible, both should be collected. Yijie agreed to collect both days.
- Whether 18 September is removed from the dataset was not decided in the chat.
- In answer to Hu's question, Yijie confirmed that Arno's leave starts at the end of October.

### Remaining items of the update and the Thursday meeting

**Chat: 12:05 and 12:14–12:20**

- Hu asked whether the remaining items of the update, the seven criteria with swing weights and the CHECK handling-time correction, were not urgent. Yijie confirmed that they were not.
- Hu will read these items carefully when she has time, and on that basis proposed not holding the Thursday meeting. Yijie agreed.

## 4. Decisions Made

1. Use Kendall's W, not Kruskal-Wallis, for the activity pattern across observation days, on the table of time per activity (rows) and observation day (columns); minutes or shares may be used, because the test works on the ranks.
2. Collect two more observation days: Wednesday 14 October and Friday 16 October.
3. Write into the thesis why Kendall's W was used and not other tests (including Kruskal-Wallis), and why this data table was chosen, the latter in the data preprocessing or data preparation section.
4. The seven criteria, the swing weights and the CHECK handling-time correction are not urgent; Hu will read them when she has time.
5. The Thursday meeting of 15 October 2026 is cancelled.

## 5. Action Items

| Task | Owner (Who) | Deadline (When) |
|---|---|---|
| Collect two further observation days with Arno, with the same protocol. | Yijie | Wednesday 14 and Friday 16 October 2026 |
| Add the new days to the analysis and review the result; if it is good, explain in the data processing and analysis why the extra days were collected after the first five. | Yijie | None noted |
| Interpret the Kendall's W result as Hu proposed and explain the deviations of 8 and 18 September in the analysis. | Yijie | None noted |
| Write into the thesis why Kendall's W was used and not other tests, including Kruskal-Wallis. | Yijie | None noted |
| Write into the thesis why this data table was chosen, in the data preprocessing or data preparation section. | Yijie | None noted |

## 6. Next Meeting

- **Date and time:** None noted.
- The Thursday meeting of **15 October 2026** was cancelled. Hu will read the remaining items of the update (the seven criteria with swing weights and the CHECK handling-time correction) when she has time; no date for that reading or for the next meeting was stated.
