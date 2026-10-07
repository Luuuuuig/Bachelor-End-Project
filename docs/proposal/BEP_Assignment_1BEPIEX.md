# BEP Assignment 1BEPIEX

**Status:** Current working project definition, corrected 7 October 2026 to the main question and five sub-questions in the submitted [Plan of Work](Plan_of_Work_Final_2026-09-22.pdf), section 2. Yijie confirmed the handed-in version is authoritative. This Markdown file mirrors its research questions; the adjacent Word draft is an older copy. Later scope and method decisions remain documented separately.

**Project title:** AI-supported operational procurement at Hytech-Pommec  
**Student:** Yijie Wang  
**Research group:** OPAC  
**TU/e supervisor:** Zhongxin Hu  
**Company:** Hytech-Pommec

### Scope update of 14 September 2026

The objective remains reducing the operational buyer's workload while maintaining purchasing quality. The [10 September academic decision](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md) adds Dennis's tactical purchasing work to the research context and keeps logistics outside the thesis. On 1 October the supervisor decided that former EXC work stays in the total time record, grouped under OTHER and kept outside the work considered for AI improvement ([meeting notes](../meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md)). Keep actor-specific evidence separate. Apply the [scope and classification addendum](../measurement/Scope_and_Classification_Addendum_2026-09-14.md) and the [current purchasing activity framework](../process/Purchasing_Activity_Framework_2026-09-21.md). The main question and five sub-questions below follow the submitted Plan of Work, as confirmed by Yijie on 7 October. The earlier four-question draft and crosswalk are historical. Later scope and method decisions do not change the submitted question wording or numbering.

## Description of the context

Hytech-Pommec B.V. is a Netherlands-based company that designs, manufactures and maintains advanced hyperbaric and life-support systems for sectors such as commercial diving, medical applications, governmental and defence organizations, tunnelling and yachting. The company provides both customer-specific systems and standardized products, as well as maintenance, certification and other support services for its equipment.

Hytech-Pommec’s mission is to be an innovation, quality and knowledge leader in hyperbaric and diving solutions. Its vision is to contribute to safer, more efficient and more sustainable operations by remaining at the forefront of technology, investing in people and working closely with customers. Furthermore, recurring principles throughout the company's mission and activities include safety, quality, reliability, innovation, technical expertise and customer focus.

This BEP focuses on reducing the operational buyer's workload at Hytech-Pommec while maintaining purchasing quality. It includes relevant tactical purchasing work through Dennis to understand purchasing tasks and their connections. Logistics and former EXC work are outside the improvement focus; their time stays visible in the overall time record. This fits well with the Operations, Planning, Accounting & Control (OPAC) research group, which focuses on controlling and improving operational processes and supporting organizations in making informed decisions, using resources efficiently and improving operational performance.

## Description of problem

The operational purchasing process at Hytech-Pommec currently involves substantial manual work by the operational buyer. Purchasing activities are performed mainly in Exact and include processing purchasing requirements, checking incoming information, deciding when orders should be placed, combining requirements from the same supplier, checking purchase prices, processing supplier confirmations and handling exceptions or questions that arise during the process.

Initial observations show that the workload does not come from one single problem. It consists of several types of work. Some activities are repetitive and administrative, such as manually creating purchasing lines, forwarding purchase orders to suppliers and updating information in Exact. Other activities involve manual verification, for example comparing current supplier prices with prices stored in Exact or checking supplier confirmations line by line. The buyer also performs judgement-intensive activities, such as deciding whether an item should be ordered immediately or whether the order can be postponed and combined with other demand. In addition, incomplete or suspicious purchasing requests may require the buyer to search through historical orders and use his own experience to determine whether the supplied information is plausible.

The process is also affected by interruptions and rework. Purchasing requests can arrive through different channels, including Exact, email, phone/desk contact, screenshots, direct requests from colleagues and occasionally letter/paper input. Cases can also be returned by Finance when a possible discrepancy is detected, requiring the buyer to investigate an order again. Furthermore, some system actions are important for preventing later problems. For example, purchased quantities need to be correctly assigned to the underlying project or production demand; otherwise the system may continue to regard the demand as unresolved, which can create a risk of duplicate purchasing.

The main problem for the company is therefore that a substantial part of the operational buyer's workload is spent on manual information handling, repetitive checking, investigating exceptions and switching between different tasks. This primarily affects employees involved in the purchasing process, but inefficient purchasing can also indirectly affect production and projects when information is incorrect, purchasing decisions are delayed or unnecessary rework occurs.

These observations include historical work recorded before the 10 September scope decision. Logistics and EXC aftercare remain preserved in the raw evidence; since 1 October their time is shown in the total workload record under OTHER but does not enter focal-case selection. The five-session analysis now describes observed workload patterns and supports a provisional case comparison; cause confirmation and candidate-specific feasibility checks remain. It does not establish representative weekly workload or the effect of an AI artifact. Conventional process redesign, rules and automation remain possible supporting components and company recommendations.

## Research question and objective

The objective of this BEP is to identify where the main sources of workload occur within the operational purchasing process at Hytech-Pommec and to reduce this workload through a focal solution containing a meaningful AI-supported contribution, while preserving purchasing activities that require human expertise. Conventional automation and process redesign may support the artifact or remain separate recommendations. A non-AI focal artifact requires evidence that no candidate passes the responsible-AI/data/quality/evaluation gates and explicit company plus academic-supervisor approval.

Furthermore, one purchasing activity will be selected for design and evaluation. Candidates first pass non-compensable permission/data, ground-truth, risk-control, BEP-feasibility and meaningful-AI-fit gates. Surviving candidates are compared with literature-grounded, evidence-anchored criteria whose definitions, scoring anchors and weights are agreed by the student and academic supervisor before aggregate rankings are calculated. The company supervisor validates operational evidence and feasibility, and sensitivity analysis checks whether the ranking is robust. The design, artifact and evaluation address only the selected activity; other supported opportunities remain recommendations to Hytech-Pommec.

### Definitions

**Workload.** Operational buyer workload concerns the amount and difficulty of purchasing work, following Bowling and Kirkendall (2012). Task frequency, active processing time, case volume and rework describe observable work demands; evidence about uncertainty, judgement and problem solving informs the assessment of difficulty. Processing time alone does not represent the full construct. Expertise dependence and organizational constraints remain distinct where relevant. Mental workload is not assessed, and the study will not create an unvalidated total-workload score. The selected component will determine which workload indicators can be justified for evaluation.

**Quality.** Quality refers to the extent to which the outcome of a purchasing activity fulfils the requirements relevant to that activity. The specific rubric is defined after focal-case selection, but success is always conjunctive: the predeclared workload endpoint must improve by at least a meaningful threshold and the final human-approved outcome must pass its quality guardrail. The case-specific threshold, comparator, rubric and acceptable minor-error margin are frozen before artifact development/formal testing.

### Main research question

**Authority:** Section 2 of the submitted [Plan of Work](Plan_of_Work_Final_2026-09-22.pdf). The main question and five sub-questions below reproduce its wording and order. The earlier four-question draft was incorrectly restored during the 7 October cleanup; this correction restores the submitted version.

> To what extent can an AI-supported solution reduce the operational buyer’s workload at Hytech-Pommec without reducing the quality of the purchasing outcome?

### Sub-research questions

1. What is the standard workflow of the purchasing process at Hytech-Pommec, and what is the relationship between operational and tactical purchasing tasks?
2. What conditions and control measures are required for the proposed solution to be implemented reliably in the purchasing workflow, including relevant operational and tactical purchasing tasks?
3. Which parts of the purchasing workflow contribute most to the operational buyer’s workload in terms of proposed measures?
4. Which of these activities offers the greatest potential for AI-supported improvement, considering workload contribution, business relevance, technical feasibility, and the need for human expertise?
5. To what extent does the proposed AI-supported solution reduce workload while maintaining the required quality of the purchasing activity?

The operational buyer in these questions is Arno. Relevant tactical purchasing tasks performed by Dennis are included in the investigation and, where relevant, in the design and evaluation of the selected improvement. Reducing Arno’s workload remains the primary objective. Changes to Dennis’s work will be considered where the improvement affects his tasks or responsibilities.

The submitted order is standard workflow and operational–tactical relationships (SQ1), implementation conditions and controls (SQ2), workload contribution (SQ3), candidate selection (SQ4), and workload and purchasing-quality evaluation (SQ5). Process mapping addresses SQ1; workload profiling and investigation of contributing factors support SQ3 and inform SQ4. Proposed measures remain subject to justification: processing time alone does not represent total workload, and the final activity-specific indicators and quality rubric must be specified before development and formal testing.

## Research Design

This project uses **DMAIC** as the overall framework for improving the operational purchasing process at Hytech-Pommec. Define, Measure and Analyze are used to understand the current process, establish a workload baseline and identify the most suitable improvement opportunity.

The exploratory Measure phase uses structured live observation. The 28 August pilot established a two-level architecture: observable work is coded at broad family level during shadowing, then mapped to detailed Task IDs post-session where evidence supports it. Five official Arno sessions are recorded (31 August; 1, 8, 18 and 23 September), with **892 minutes of confirmed net observation**; the 8 September OBS-16 data-quality exclusion remains. Dennis's qualitative notes of 15 September and measured observation of 25 September are available and remain separate from Arno's baseline. Measurement Protocol v1.3 retains the v1.2 live fields; the scope addendum supplies the later scope and simultaneous-activity timing amendments. The initial five-day Arno review point has been reached and analysis proceeds following the 1 October supervisor direction. Review coverage and candidate-relevant uncertainty using the available data, with further observation only for an identified gap. Five dates do not equal 40 net hours; no equal Dennis sample size is required. Targeted Exact/test-account feasibility now belongs to Analyze for the shortlisted candidates.

Within the **Improve** phase, **DSRM** guides design, development, demonstration and evaluation of the selected AI-supported artifact. Before development/formal testing, the project freezes the justified primary workload endpoint for the selected component, meaningful-improvement threshold and final-human-outcome quality guardrail. The **Control** phase then focuses on implementation recommendations, monitoring and maintaining the improved process.

In this way, DMAIC structures the overall process-improvement project, while DSRM provides the detailed artifact-development and evaluation structure within the Improve phase.

## Communication / Expectations

A meeting with the university supervisor is scheduled on a weekly basis, subject to the cancellations recorded in the 1 October notes. Meetings cover progress, methodological decisions, findings and upcoming activities. The student carries out the research, communicates progress and prepares material for feedback. The academic supervisor advises on scope and research quality; the company supervisor supports access, business relevance and operational feasibility. Lijia Tan is named as second assessor in the submitted Plan of Work. The second assessor reviews the Plan of Work and co-assesses the final report under the 1BEPIE procedure; no additional formative role is assumed.

## References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13


---

**Origin:** Markdown mirror created from the 26 August 1BEPIEX Word draft and subsequently synchronized through 2 September with the repository's current workload, Measure and methodology framing.
