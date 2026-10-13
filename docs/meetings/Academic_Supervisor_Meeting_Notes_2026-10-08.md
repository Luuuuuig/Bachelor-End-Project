# Academic Supervisor Meeting Notes, 8 October 2026

## 1. Meeting Overview

- **Date:** 8 October 2026.
- **Time:** Recording began at approximately 15:00 CEST. The transcript runs to 28:08.
- **Attendees:** Yijie Wang and Zhongxin Hu, academic supervisor.
- **Meeting type:** BEP academic supervision meeting.
- **Purpose:** Review CHECK-time variation and data sufficiency, discuss how to select an AI improvement task, and plan the next analysis steps around buyer availability.
- **Source:** [BEP meeting recording and its automatic transcript](https://tuenl-my.sharepoint.com/personal/z_hu1_tue_nl/_layouts/15/stream.aspx?id=%2Fpersonal%2Fz%5Fhu1%5Ftue%5Fnl%2FDocuments%2FRecordings%2FBEP%20%2D%20Yijie%2D20261008%5F150055%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ee3489469%2Dcd22%2D4e2f%2Dbc9a%2D30bacb07e522). Timestamps below refer to elapsed recording time.

## 2. Executive Summary

Hu accepted the small absolute difference in CHECK handling time discussed, while advising further analysis of patterns across observation days before deciding whether more data are needed. Yijie proposed a feasibility screen and weighted comparison to select one improvement task, taking workload, AI suitability, buyer and company willingness, and business value into account; the approach and weights remained provisional. Yijie will continue analysing the available data, investigate the suggested Kruskal-Wallis test, and write down the selection criteria and their rationale.

## 3. Key Discussion Points

### CHECK handling time and the remaining variation

**Recording: 00:03–03:31 and 07:07–09:27**

- Yijie revisited the effect of the 18 September observations on CHECK results and reported examining average handling time per order line, following the previous meeting.
- He quoted approximately **0.90 minutes per line on 18 September**, compared with **0.87 minutes per line for the other observations**. He described the absolute difference as **0.03 minutes, or 1.8 seconds**.
- Yijie also corrected an earlier oral estimate of approximately 10% to **8.3%**. The discussion did not establish how this percentage related to the quoted averages.
- Yijie suggested that the small absolute difference could reflect measurement variation. Hu said that the difference discussed was acceptable.
- This acceptance concerned the CHECK comparison. No final conclusion on the sufficiency of the full dataset was reached.
- Yijie mentioned using mean absolute error and an approach from his quality and reliability course, but could not name the method. He had not yet established an acceptance criterion for that calculation.

### Comparing observation days and assessing data sufficiency

**Recording: 03:31–07:02 and 25:34–27:15**

- Hu proposed comparing patterns across the observation days using a table with **days as columns**, **activity categories as rows**, and **each activity's share of observed time as the cell values**. Hu specified proportions rather than raw durations.
- The proposed comparison concerned the overall activity pattern across days, rather than CHECK alone.
- Near the end of the meeting, Hu shared a table of statistical methods and identified the **Kruskal-Wallis test**, in the category for nonparametric comparisons across multiple groups, as the method to investigate. *Correction, 13 October: Hu agreed she had named the wrong test; for the activity pattern across days the test is Kendall's W ([chat record](Academic_Supervisor_Chat_2026-10-13.md)).*
- Yijie agreed to work on this analysis during the coming week. The meeting did not establish the detailed test setup, a significance threshold, or a test result.
- Hu advised analysing the existing data first and avoiding further observations if the distribution did not appear very unusual. This remained conditional guidance, not confirmation that data collection was complete.

### Selecting the improvement task

**Recording: 10:11–20:15 and 22:13–25:06**

- Yijie reported that PO preparation accounted for the largest share of time in his preliminary analysis. He questioned whether workload alone should determine the improvement focus.
- He proposed an initial feasibility screen, followed by a weighted comparison using swing weighting. Proposed considerations included workload, AI suitability, buyer and company willingness, and business value.
- Yijie's intended approach was to develop a solution for one selected task and provide recommendations for other tasks. No specific task or final solution was selected during this meeting.
- Hu supported giving a clear justification for the selection and considering feasibility and stakeholder willingness. Hu described the weighted comparison as support for the choice and advised putting the more substantial analysis into evaluating the developed solution and its value.
- Hu cautioned against using time savings obtained after implementing the solution as a criterion for deciding which solution to develop, because that would make the reasoning circular.
- Hu also noted that a weighted ranking could still select a task that buyers did not want automated. Yijie said that his rough trial weights had not produced that outcome, but that small changes to the weights could noticeably affect the ranking.
- The weights remained unsettled. Yijie proposed reviewing them with Hu the following week if he had calculated them by then; Hu agreed.
- Hu asked Yijie to write down the proposed criteria, define what each means, and explain why each belongs in the selection process. Yijie agreed.

### Buyer acceptance and the business-value example

**Recording: 15:27–16:35 and 20:15–22:13**

- Yijie reported discussing possible AI functions with Arno and Dennis after an observation session. The example involved automatic PO creation and sending orders by email.
- According to Yijie, both buyers strongly opposed that arrangement. They expected review-only work to become less interesting and were concerned about losing control and awareness of what had been ordered.
- Yijie explained that buyers currently retain enough familiarity with their orders to answer colleagues' questions. He reported that they feared losing this familiarity under full automation.
- As an example of business value beyond time savings, Yijie discussed price checking and updating. He reported that Arno and Dennis had described outdated purchase prices feeding into sales prices and, in some cases, products being sold at a loss.
- This was an example supporting the proposed selection criteria, not a confirmed choice to develop a price-checking solution.

### Buyer availability and immediate priorities

**Recording: 09:26–09:52 and 25:06–26:23**

- Dennis had not yet returned from his business trip. Yijie hoped he would return the following week, but did not have a confirmed return date.
- Yijie reported that Dennis would change roles after returning and that Arno planned to take leave at the end of October.
- Hu advised continuing the analysis of the available data while Dennis remained away.
- Yijie raised the need to assess data sufficiency by around the following week so that any necessary additional observations could be arranged before Arno's leave. Hu advised completing the analysis first.

## 4. Decisions Made

1. Continue analysing the available observation data without waiting for Dennis to return.
2. Treat the small absolute CHECK-time difference discussed as acceptable, while leaving the broader data-sufficiency assessment open.
3. Investigate the suggested Kruskal-Wallis comparison during the coming week to support the assessment of patterns across observation days.
4. Document the proposed task-selection criteria, their definitions and their rationale before finalising the weights.

## 5. Action Items

| Task | Owner (Who) | Deadline (When) |
|---|---|---|
| Continue analysing the available observation data and assess whether additional observations are needed. | Yijie | Following week discussed as the target; no fixed date |
| Investigate and carry out the proposed Kruskal-Wallis analysis of patterns across observation days. | Yijie | Coming week |
| Write down the proposed selection criteria, define each criterion, and explain why it is included. | Yijie | None noted |
| Develop the proposed weights and review them with Hu once ready. | Yijie; review with Hu | Following week, if the calculations are ready |

## 6. Next Meeting

- **Date and time:** None noted.
- Yijie proposed discussing the weights the following week if they were ready. No specific meeting date or time was confirmed in the recording.
