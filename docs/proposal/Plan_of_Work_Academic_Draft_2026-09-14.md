# Plan of Work

**Name student:** Yijie Wang

**Student ID:** [Student ID]

**Name TU/e supervisor:** Zhongxin Hu

**Name 2nd assessor:** [Second assessor]

**Name company:** Hytech-Pommec

## Part A. BEP Research Proposal

### Project Title

AI-supported operational procurement at Hytech-Pommec

### 1. Introduction

Operational procurement at Hytech-Pommec covers the daily execution of purchasing decisions. Arno, the operational buyer, processes requests in Exact, prepares and monitors purchase orders (POs), checks prices and supplier confirmations, and resolves missing or incorrect data. Initial observations also show decisions about when to order and whether demand for the same supplier can be combined. These tasks require manual information handling, verification and judgement, but their relative workload contributions and underlying causes have not yet been established.

The business concern is the time Arno requires to carry out this work while maintaining purchasing quality. Some of the information and decisions used in operational purchasing originate in tactical purchasing. Dennis's relevant work and its connections with Arno therefore form part of the investigation. The study will examine whether those connections help explain observed handling time or repeated work. It does not yet establish a dominant root cause or achievable savings.

Bowling and Kirkendall (2012) provide a broad conceptual account of workload. This study focuses on observable work and uses active handling time as its measured workload outcome. Task frequency, volume and qualitative evidence about judgement help interpret the work. Van Weele's purchasing-process model, discussed by Bäckstrand et al. (2019), locates tasks within specification, supplier selection, contracting, ordering, monitoring and evaluation. It supports analysis of how the purchasing roles connect.

The primary objective of this Bachelor End Project (BEP) is to reduce Arno's workload within the included purchasing work while maintaining purchasing quality. The investigation includes Dennis's relevant tactical tasks, information exchanges and decision responsibilities. One coherent purchasing-process component will be selected for redesign and evaluation using artificial intelligence (AI). The component may involve both buyers where evidence links the proposed change to Arno's work. Other supported opportunities will become recommendations.

<!-- PAGE_BREAK -->

### 2. Research question

#### Main research question

To what extent can an AI-supported improvement to a selected purchasing-process component reduce the operational buyer's workload at Hytech-Pommec while maintaining purchasing quality?

#### Sub-research questions

1. How is the operational buyer's active handling time distributed across included purchasing tasks, and what patterns occur in task frequency, volume and rework?
2. Which factors in operational and relevant tactical purchasing, including information flows, decisions and handoffs involving Dennis, explain the observed handling time and repeated work?
3. Which coherent purchasing-process component offers the strongest supported opportunity to reduce Arno's workload through AI, considering the work it could address, business relevance, feasibility and human expertise?
4. What functional requirements, controls and division of responsibilities are needed for reliable use of the selected AI-supported improvement?
5. To what extent does the improvement reduce Arno's active handling time while maintaining purchasing quality, and what changes does it create in other affected purchasing roles?

The operational buyer in these questions is Arno. Purchasing and procurement refer to the same research setting. His included work provides the primary workload baseline and evaluation outcome. Dennis's observed tasks and their connections with Arno inform process diagnosis, candidate selection and design. Changes to Dennis's work will be assessed where the selected component affects him. Rework refers to work within the analytical boundary below.

### 3. Empirical context (incl. company description)

Hytech-Pommec develops and manufactures hyperbaric oxygen and life support systems. Procurement ensures that the company receives the right materials from suitable suppliers at the required time, price and quality. Strategic and tactical procurement include supplier selection, contracts, sourcing decisions and supplier relationships. Operational procurement executes purchasing decisions through requests, orders, monitoring and information checks. Exact supports order administration, allocation to underlying demand and supplier information.

The study will observe Arno's operational work and Dennis's relevant tactical work, including their inputs, outputs, decisions and exchanges. Johan has identified overlap between the roles, including cover during absences. Task purpose and observed responsibility will determine process-stage assignments; job titles alone will not. Johan provides company supervision, business context and support for access and feasibility decisions.

The detailed operational flow runs from the purchasing need to supplier confirmation, recorded as Bevestigd in Exact. Relevant tactical work extends the investigation to specification, supplier selection and agreements. Existing agreements can be reused, so each PO need not repeat every stage. Following the academic decision of 10 September, logistics and EXC time are excluded from the thesis Measure analysis and focal-case selection. Raw records remain preserved. The resulting workload profile covers Arno's included purchasing work and does not estimate his entire workload.

<!-- PAGE_BREAK -->

### 4. Method

#### Research Design/Approach

The study combines process investigation with a quantitative comparison of the selected intervention and current practice. Define, Measure, Analyze, Improve and Control (DMAIC) provides the overarching structure, following de Mast and Lokkerbol (2012). Define and Measure establish the purchasing process across the relevant roles and Arno's operational workload profile. Analyze uses both buyers' evidence to investigate causes and select a bounded improvement component.

Within Improve, Design Science Research Methodology (DSRM) guides the artifact's objectives, design, development, demonstration and evaluation, following Peffers et al. (2007). Control translates findings into recommendations for use and monitoring. AI could support information extraction, document comparison, validation or routine decisions. The technical form, level of autonomy and integration requirements will follow the selected component and its evidence.

#### Sources of data and data collection

| Source | Data and collection | Purpose |
|---|---|---|
| Arno | Structured observation of tasks, active time, volume, interruptions and decisions; case questions | Establish his included workload profile |
| Dennis | Targeted observation and case walkthroughs recording tasks, inputs, outputs, decisions and exchanges with Arno | Identify relevant task patterns, handoffs and possible causes |
| Purchasing documents | Review SOPs, forms and formal process documents | Compare documented and observed practice |
| Purchasing records and systems | Relevant requests, POs, confirmations and available Exact or Orbis information, subject to access | Trace supported connections and assess feasibility |
| Evaluation cases | Record Arno's handling, review, correction and outcomes; record changes to affected tasks in Dennis's work separately | Evaluate the primary outcome and effects on other roles |

Observation follows time-and-motion principles, including explicit coverage and task transitions, consistent with Zheng et al. (2011). Live work families describe observable actions. Supported tasks are subsequently mapped to task IDs and Van Weele stages using their purpose. CHECK or SEND can occur in several stages. Request intake is timed when it involves visible work. Instantaneous decisions are tallied, while embedded decisions remain attributes of their timed episode. Date, actor, case identifier, timing quality and uncertainty are retained.

Five Arno observation days form the initial sufficiency checkpoint. Coverage, cumulative patterns and newly observed work determine whether targeted extension is needed. Dennis's evidence need not be equally large, but must support interpretable patterns in relevant tasks and connections. Follow-up targets missing information rather than an equal observation quota. Walkthroughs and interviews inform interpretation; only reliably observed durations enter time summaries.

<!-- PAGE_BREAK -->

### 5. Data analysis approach(es)

#### Workload profile and process analysis

For sub-question 1, workload is operationalized as the active handling time Arno requires to complete included purchasing work. It includes preparation, review, correction and in-scope rework. Frequency, volume and interruptions describe the observed work and help interpret time requirements. Judgement and expertise evidence inform task interpretation and AI suitability. Mental workload is not assessed, and these indicators will not be combined into an overall workload score.

Raw records remain unchanged. A derived dataset applies logistics, EXC and timing-quality exclusions. Arno's reliable included minutes will be summarized by task family and process stage. Time shares use all his reliable included timed minutes; occurrence rates state their observation exposure. Uncertain and multi-stage episodes remain identifiable without duplicated minutes. Dennis's patterns and reliable durations remain separate; unequal coverage prevents direct comparisons of overall workloads.

Sub-question 2 uses process maps, cases, records and follow-up questions to investigate causes of Arno's handling time and repeated work. Analysis will trace information and decisions through both roles, examining missing inputs, clarification exchanges and overlapping responsibilities where supported. Proposed causes remain hypotheses until supported. The selected component may include Dennis's work even when the primary effect is measured in Arno's tasks.

#### Selection and requirements of the improvement

For sub-question 3, candidates must meet conditions for permission, data access, reference outcomes, risk control, study time and meaningful AI use. Eligible components will be compared on the Arno work they could address, business relevance, data readiness, AI suitability, evaluation feasibility and human expertise. Addressable workload includes Arno's work arising later in the process. EXC and logistics remain excluded.

Criteria, score anchors and weights will be agreed with the academic supervisor before ranking. Sensitivity analysis will test whether uncertain evidence or plausible weights alter the choice. Johan will validate business feasibility. Targeted Exact and Orbis checks will establish access and interface requirements. For sub-question 4, the selected component's inputs, outputs, review controls and responsibilities will be specified with the affected buyers. Dennis participates where the design changes his work or information exchanges.

#### Evaluation of workload and quality

For sub-question 5, the primary outcome is Arno's active handling time per eligible case or line passing through the selected component, including attributable preparation, review, correction and rework. The protocol will fix the unit, eligibility, comparator, meaningful improvement threshold and purchasing-quality rubric before development and formal testing. Equivalent incoming cases remain eligible when the intervention prevents a clarification task or removes the need for Arno to act.

Development and evaluation cases remain separate. Comparable or matched cases and balanced condition order will be used where feasible to address case mix and learning. Sample size and analysis will follow case characteristics and available observations. Results will report Arno's time change, uncertainty, purchasing quality and AI cost. Any changes to Dennis's affected tasks will be reported separately, with time estimates only where supported. Arno's savings will not be presented as department-wide savings when work transfers to Dennis. Success requires the workload threshold and quality requirement; a finding of no benefit remains valid.

<!-- PAGE_BREAK -->

### 6. Deliverables

#### Anticipated practical implications for the company

The project will deliver an AS-IS purchasing map showing Arno's work, Dennis's relevant tasks and their connections, including observed role overlap. It will provide Arno's workload profile within the analytical boundary, a supported diagnosis and candidate comparison, and one evaluated AI-supported improvement to a coherent process component. The intervention may involve both buyers where the evidence supports that design.

Evaluation will establish whether the selected change reduces Arno's active handling time while maintaining purchasing quality and will report effects on Dennis's affected work separately. Recommendations will describe responsibilities, use, monitoring and other supported purchasing opportunities. Production implementation and wider savings remain subject to the findings and feasibility.

#### Anticipated theoretical insights

The study aims to provide context-specific evidence about how AI-supported changes to purchasing tasks and information exchanges affect an operational buyer's handling time and purchasing quality. It will examine information requirements, verification and human review in the selected component. Relating the findings to Van Weele stages will help explain how the intervention operates across relevant purchasing roles. The discussion will address the limits of the single-company setting, observation coverage and included work.

### References

Bäckstrand, J., Suurmond, R., van Raaij, E., & Chen, C. (2019). Purchasing process models: Inspiration for teaching purchasing and supply management. *Journal of Purchasing and Supply Management, 25*, Article 100577. https://doi.org/10.1016/j.pursup.2019.100577

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice* (Vol. 2, pp. 221-238). Wiley-Blackwell. https://doi.org/10.1002/9781119942849.ch13

de Mast, J., & Lokkerbol, J. (2012). An analysis of the Six Sigma DMAIC method from the perspective of problem solving. *International Journal of Production Economics, 139*(2), 604-614. https://doi.org/10.1016/j.ijpe.2012.05.035

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45-77. https://doi.org/10.2753/MIS0742-1222240302

Zheng, K., Guo, M. H., & Hanauer, D. A. (2011). Using the time and motion method to study clinical work processes and workflow: Methodological inconsistencies and a call for standardized research. *Journal of the American Medical Informatics Association, 18*(5), 704-710. https://doi.org/10.1136/amiajnl-2011-000083

<!-- PAGE_BREAK -->

## Part B - Planning

The BEP combines 420 study hours for 1BEPIE and 1BEPIEX. The supplied Ganttchart.drawio schedules work from 17 August 2026 to the final assessment on 7 February 2027. Its task dates and milestones are retained in Figures 1-3. Company-dependent access, observation and evaluation must fit before the placement ends on 7 January. Actual effort will be logged by work package and reviewed weekly with progress and remaining tasks.

The literature study supports the workload and measurement framework, the September candidate comparison and the design and evaluation of the selected artifact. Data collection continues alongside process validation and cleaning. Analyze depends on the Measure coverage review and usable summaries. Artifact design and testing follow the focal-case and evaluation-protocol gates. Thesis writing runs alongside the research, with final result integration in December and report checks in January.

The repository records the pilot and three official Arno sessions. The 8 September session still requires derived-data preparation, including its explicit OBS-16 exclusion. Dennis fieldwork and the Measure sufficiency review remain open. Prepared documents do not by themselves complete submission or observation milestones.

| Milestone | Planned date |
|---|---|
| Half-page project description | 15 September 2026 |
| Internal complete PoW draft; Measure sufficiency review | 18 September 2026 |
| Supervisor PoW review draft; Measure tollgate | 20 September; 22 September 2026 |
| Final Plan of Work | 27 September 2026 at 23:59 |
| ILBEP | 28 September 2026 at 23:59 |
| Focal AI case gate; evaluation protocol freeze | 7 October; 15 October 2026 |
| Artifact ready; evaluation complete | 20 November; 11 December 2026 |
| Company placement ends; final report | 7 January; 15 January 2027 at 23:59 |
| Presentation completed by; final assessment | 29 January; 7 February 2027 |

The planned focal-case gate follows Plan of Work submission. The proposal therefore defines how the improvement will be selected and tested. Research gates require sufficient evidence. If data or feasibility conditions are unmet, targeted extension and its effect on later tasks will be discussed at the weekly supervisor meeting.

Source: [Ganttchart.drawio](https://drive.google.com/file/d/1Qe29SYs5xBGpjUXFTREVlIS7x2jsy18P/view), supplied 14 September 2026. Figures 1-3 retain its recorded statuses. The historical logistics walkthrough is background activity; logistics remains outside the thesis.

<!-- LANDSCAPE -->

### Figure 1. Gantt chart for Define and Measure

![Define and Measure schedule](../planning/figures/PoW_Gantt_Define_Measure_2026-09-14.svg)

<!-- PAGE_BREAK -->

### Figure 2. Gantt chart for Academic deliverables and Analyze

![Academic deliverables and Analyze schedule](../planning/figures/PoW_Gantt_Academic_Analyze_2026-09-14.svg)

<!-- PAGE_BREAK -->

### Figure 3. Gantt chart for Improve Control and thesis completion

![Improve Control and thesis completion schedule](../planning/figures/PoW_Gantt_Improve_Control_2026-09-14.svg)

<!-- PORTRAIT -->

## Part C - Reflection at start BEP

Complete each of the five reflections in approximately 300-400 words, for a total of 1,500-2,000 words. Use concrete experiences and actual feedback from earlier courses, projects or other relevant contexts. For each skill, address the experience, feedback, self-assessment, learning goals and action plan. Explain how progress will be monitored and evaluated during the BEP semester. Replace the bracketed prompts with your own reflection.

### 1. Planning and Organizing

**Experiences:** [Describe a previous course or project, your planning responsibilities and what happened.]

**Feedback:** [Summarize feedback on planning, deadlines or organizing work, and identify who gave it.]

**Self-assessment:** [Explain the strengths and development needs shown by this experience and feedback.]

**Learning goals:** [State a specific planning improvement for this BEP semester.]

**Action plan:** [Describe actions, timing and evidence for monitoring and evaluating progress.]

### 2. Writing

**Experiences:** [Describe a previous writing assignment, its context, your contribution and its outcome.]

**Feedback:** [Summarize actual feedback from a teacher, peer or trainer on your writing.]

**Self-assessment:** [Explain the writing strengths and development needs supported by this evidence.]

**Learning goals:** [State a specific writing improvement for this BEP semester.]

**Action plan:** [Describe practice, feedback moments and how you will evaluate progress.]

<!-- PAGE_BREAK -->

### 3. Presenting

**Experiences:** [Describe a previous presentation, its context, your role and what happened.]

**Feedback:** [Summarize actual presentation feedback from peers, teachers or trainers.]

**Self-assessment:** [Explain the presenting strengths and development needs shown by that evidence.]

**Learning goals:** [State a specific presenting improvement for this BEP semester.]

**Action plan:** [Describe planned practice, feedback moments and progress evaluation.]

### 4. Collaborating

**Experiences:** [Describe a previous team task, its context, your responsibilities and the outcome.]

**Feedback:** [Summarize feedback on your collaboration and identify its source.]

**Self-assessment:** [Explain what the evidence shows about how you work with others.]

**Learning goals:** [State a specific collaboration skill to develop during the BEP semester.]

**Action plan:** [Describe actions, feedback arrangements and evidence for monitoring progress.]

### 5. Dealing with Scientific Information

**Experiences:** [Describe previous work finding, evaluating or using scientific literature and its course or context.]

**Feedback:** [Summarize actual feedback on searches, source assessment, referencing or synthesis.]

**Self-assessment:** [Explain the strengths and development needs supported by this evidence.]

**Learning goals:** [State a specific improvement in dealing with scientific information during the BEP semester.]

**Action plan:** [Describe practice, review moments and how you will evaluate progress.]

<!-- PAGE_BREAK -->

## Part D - Declaration of scientific conduct

<!-- DECLARATION_IMAGE -->

The Word version retains the unsigned declaration from the supplied university template. Complete the name, ID, date and signature fields after reading the TU/e Code of Scientific Conduct.
