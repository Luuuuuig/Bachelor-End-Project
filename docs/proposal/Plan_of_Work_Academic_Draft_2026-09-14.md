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

Operational procurement at Hytech-Pommec covers the daily execution of procurement decisions. The operational buyer processes requests in Exact, prepares and monitors purchase orders (POs), checks prices and supplier confirmations, and resolves missing or incorrect data. Initial observations also show decisions about when to order and whether demand for the same supplier can be combined. These tasks require manual information handling, verification and judgement, but their relative workload contributions and underlying causes have not yet been established.

The business concern is the effort required to carry out this work while maintaining purchasing quality. Manual handling and clarification may limit the time available for other purchasing responsibilities. Their operational effect still needs measurement; the evidence does not yet establish excessive workload, a dominant root cause or achievable savings. An intervention selected too early could address a small task or transfer effort to checking and correction elsewhere.

Research provides concepts for investigating this concern. Bowling and Kirkendall (2012) distinguish the amount and difficulty of work. Young et al. (2015) discuss mental workload, supporting a distinction between handling time and cognitive demands. Van Weele's purchasing-process model, discussed by Bäckstrand et al. (2019), locates tasks within specification, supplier selection, contracting, ordering, monitoring and evaluation. These concepts organize the investigation; they do not establish which local task should receive AI support.

This Bachelor End Project (BEP) focuses primarily on operational procurement and investigates how artificial intelligence (AI) supported tools can reduce the workload of operational procurement specialists while maintaining procurement quality. Relevant tactical work will be examined where needed to understand information flows, decision-making responsibilities and the division of work within the procurement department. One procurement task or coherent process step will be selected for detailed redesign and optimization using AI. Evaluation will compare the intervention with current practice. Other supported opportunities will become recommendations.

<!-- PAGE_BREAK -->

### 2. Research question

#### Main research question

To what extent can an AI-supported solution reduce the operational buyers' workload at Hytech-Pommec without reducing the quality of the purchasing outcome?

#### Sub-research questions

1. Which parts of the operational purchasing workflow contribute most to the operational buyer's workload in terms of frequency, processing time, rework and judgement required?
2. What conditions and control measures are required for the proposed solution to be implemented reliably in the operational purchasing workflow?
3. Which of these activities offers the greatest potential for AI-supported improvement, considering workload contribution, business relevance, technical feasibility and the need for human expertise?
4. To what extent does the proposed AI-supported solution reduce workload while maintaining the required quality of the purchasing activity, when compared with current practice?

The questions retain the approved purchasing terminology. Purchasing refers here to the operational procurement work described above. The empirical operational baseline concerns Arno. Results describe his included observed work; they do not estimate every specialist's workload. Dennis's evidence remains identifiable by actor and provides additional procurement context. Rework in the questions refers to work within the agreed analytical scope.

### 3. Empirical context (incl. company description)

Hytech-Pommec develops and manufactures hyperbaric oxygen and life support systems. Procurement ensures that the company receives the right materials from suitable suppliers at the required time, price and quality. It includes strategic, tactical and operational activities. Strategic and tactical procurement cover supplier selection, contracts, sourcing decisions and supplier relationships. Operational procurement executes these decisions through requests, orders, monitoring and information checks. Exact supports request processing, order administration, allocation to underlying demand and supplier information.

Arno performs operational purchasing work. Dennis provides the tactical purchasing perspective, including relevant tasks and information exchanged with operational purchasing. Johan is the company supervisor and supports access to employees, business context and feasibility decisions. Actual observation will establish Dennis's tasks and responsibilities; job titles alone do not determine which process stages each buyer performs.

The detailed operational flow runs from the purchasing need to supplier confirmation, recorded as Bevestigd in Exact. Relevant tactical work extends the context to specification, supplier selection and agreements. Existing agreements can be reused, so each PO need not repeat every stage. Following the academic decision of 10 September, logistics and EXC time are excluded from the thesis Measure analysis and focal-case selection. Earlier raw records remain preserved. The thesis workload profile therefore covers included purchasing work and does not represent all of Arno's purchasing and aftercare responsibilities.

<!-- PAGE_BREAK -->

### 4. Method

#### Research Design/Approach

The study combines exploratory process investigation with a quantitative comparison of the selected intervention and current practice. Define, Measure, Analyze, Improve and Control (DMAIC) provides the overarching process-improvement structure, following de Mast and Lokkerbol (2012). Define and Measure establish the current process and an interpretable workload profile. Analyze investigates causes and selects a bounded improvement component. This sequence is suitable because the workload contributors and improvement case remain open.

Within Improve, Design Science Research Methodology (DSRM) guides the artifact's objectives, design, development, demonstration and evaluation, following Peffers et al. (2007). Control translates findings into recommendations for use and monitoring. Depending on the selected activity, AI could support information extraction and validation, document comparison, detection of missing or inconsistent data, or routine decisions. These remain possibilities; the technical form, level of autonomy and integration requirements have not been selected.

#### Sources of data and data collection

| Source | Data and collection | Purpose |
|---|---|---|
| Arno | Structured observation of tasks, times, volume, interruptions and decisions; case questions | Establish the operational workload profile |
| Dennis | Targeted observation and walkthroughs of actual cases | Establish tactical tasks and purchasing handoffs |
| Purchasing documents | Review SOPs, forms and formal process documents | Compare documented and observed practice |
| Purchasing records and systems | Relevant requests, POs, confirmations and available Exact or Orbis information, subject to access | Trace cases and assess data and technical feasibility |
| Evaluation cases | Record current-practice and AI-supported handling, review, corrections and outcomes | Assess workload change and purchasing quality |

Structured observation follows time-and-motion principles, including explicit coverage and task-transition recording, consistent with Zheng et al. (2011). Live work families describe observable actions. After each session, supported tasks are mapped separately to detailed task IDs and Van Weele stages. A phase assignment requires the purpose of the work; CHECK or SEND can occur in several stages.

Request intake is timed when intake itself involves visible work. Standalone instantaneous decisions are tallied; embedded decisions remain attributes of their timed episode. No duration is inferred for unobserved cognition. Source date, actor, case identifier, timing quality and uncertainty are retained. Actual buyer activity is distinguished from automatic system events and supplier actions.

Five operational observation days form the initial sufficiency checkpoint. Coverage, cumulative patterns and newly observed work determine whether targeted extension is needed. Dennis's dataset need not be equally large, but it must support interpretable patterns. The review will examine missing weekdays, dayparts, task families and case types. Interviews and walkthroughs provide context and will not be treated as timed observation evidence.

<!-- PAGE_BREAK -->

### 5. Data analysis approach(es)

#### Workload profile and process analysis

For sub-question 1, the analysis will describe task occurrence, reliable active handling time, processed volume, interruptions, in-scope rework and qualitative evidence of judgement or difficulty. Amount and difficulty will remain separate dimensions. Processing time will not be treated as a direct measure of mental workload or combined into an unvalidated overall workload score.

Raw records will remain unchanged. A derived dataset will apply logistics and EXC exclusions, retain explicit data-quality exclusions and record uncertain classifications. Reliable eligible minutes will be reported by family and process stage for each actor. Workload shares will use all reliable included timed minutes for that actor as the denominator. Occurrence rates will state the observation exposure used. Comparable episode or case durations will be reported only where timing and coverage support comparison. Multi-stage or unresolved episodes will retain their uncertainty without duplicated minutes.

The process map, observed cases, purchasing records and targeted follow-up will be used to trace possible causes. A proposed cause will remain a hypothesis until evidence supports it. The analysis will examine whether work originates in the focal task or an earlier purchasing step. An upstream intervention may be appropriate even when its effect is measured in Arno's work.

#### Conditions and selection of the improvement

Sub-questions 2 and 3 will be addressed through feasibility investigation and a documented candidate comparison. Candidates must first pass the existing permission and data-access, reference-outcome, risk-control, study-time and meaningful-AI-fit conditions. Eligible candidates will be compared using workload contribution, business relevance, data readiness, AI suitability, evaluation feasibility and the need for human expertise. Criteria, score anchors and weights will be agreed with the academic supervisor before aggregate ranking. Johan will validate operational evidence and business feasibility.

Sensitivity analysis will examine whether plausible changes in weights or uncertain scores alter the preferred candidate. Targeted Exact and Orbis checks will establish practical access and interface requirements. One component will be selected when its evidence, access and evaluation fit the study period. If a leading candidate fails a feasibility condition, another eligible candidate will be considered through the same procedure. EXC and logistics will not enter the candidate set.

#### Evaluation of workload and quality

For sub-question 4, the evaluation protocol will define eligible cases, the current-practice comparator, the primary workload measure, a meaningful improvement threshold and an activity-specific quality rubric before development and formal testing. Active human handling time per comparable case or line is the current workload-measure direction. It will include preparation, review, correction and rework attributable to the intervention. Required human review and approval will be agreed for the selected use case.

Development material will remain separate from formal evaluation cases. Where repeatability permits, comparable or matched cases and balanced condition order will help address case difficulty and learning effects. The final sample size and statistical analysis will follow case characteristics and feasible observations. Analysis will report workload differences, uncertainty, purchasing quality, AI cost and any work transferred to another purchasing role. Improvement requires both the predeclared workload threshold and the quality requirement to be met. A finding of no benefit remains a valid research outcome.

<!-- PAGE_BREAK -->

### 6. Deliverables

#### Anticipated practical implications for the company

The project will deliver an AS-IS purchasing description, a workload profile within the agreed scope, a documented improvement selection and one evaluated AI-supported artifact. The practical contribution is evidence about whether the selected change reduces buyer effort while maintaining purchasing quality. Recommendations will describe use, ownership, monitoring and relevant process changes. Other supported purchasing opportunities will be recorded as recommendations. Benefits and production implementation remain subject to evaluation and feasibility findings.

#### Anticipated theoretical insights

The study aims to provide context-specific evidence about the conditions under which AI support changes human handling time while preserving purchasing quality. It will examine the roles of information requirements, verification and human review in the tested task. Relating observed work to a purchasing-process model will help explain where the intervention operates. The discussion will assess how task characteristics and the single-company setting limit transfer of the findings to other purchasing activities.

### References

Bäckstrand, J., Suurmond, R., van Raaij, E., & Chen, C. (2019). Purchasing process models: Inspiration for teaching purchasing and supply management. *Journal of Purchasing and Supply Management, 25*, Article 100577. https://doi.org/10.1016/j.pursup.2019.100577

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice* (Vol. 2, pp. 221-238). Wiley-Blackwell. https://doi.org/10.1002/9781119942849.ch13

de Mast, J., & Lokkerbol, J. (2012). An analysis of the Six Sigma DMAIC method from the perspective of problem solving. *International Journal of Production Economics, 139*(2), 604-614. https://doi.org/10.1016/j.ijpe.2012.05.035

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45-77. https://doi.org/10.2753/MIS0742-1222240302

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1-17. https://doi.org/10.1080/00140139.2014.956151

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
