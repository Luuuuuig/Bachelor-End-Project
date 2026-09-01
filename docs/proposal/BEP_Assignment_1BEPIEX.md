# BEP Assignment 1BEPIEX

**Status:** Current readable repository version, synchronized 2 September 2026. This Markdown file is the authoritative readable project-definition source in the repository. The Word binary retained beside it is an older external/submission copy and should not be assumed to contain every later repository synchronization.

**Project title:** Reduce Operational Purchasing Workload at Hytech-Pommec using AI  
**Student:** Yijie Wang  
**Research group:** OPAC  
**TU/e supervisor:** Zhongxin Hu  
**Company:** Hytech-Pommec

## Description of the context

Hytech-Pommec B.V. is a Netherlands-based company that designs, manufactures and maintains advanced hyperbaric and life-support systems for sectors such as commercial diving, medical applications, governmental and defence organizations, tunnelling and yachting. The company provides both customer-specific systems and standardized products, as well as maintenance, certification and other support services for its equipment.

Hytech-Pommec’s mission is to be an innovation, quality and knowledge leader in hyperbaric and diving solutions. Its vision is to contribute to safer, more efficient and more sustainable operations by remaining at the forefront of technology, investing in people and working closely with customers. Furthermore, recurring principles throughout the company's mission and activities include safety, quality, reliability, innovation, technical expertise and customer focus.

This BEP focuses on the operational purchasing process at Hytech-Pommec and investigates how the workload within this process can be reduced while improving its efficiency and supporting purchasing activities that require human expertise. This fits well with the Operations, Planning, Accounting & Control (OPAC) research group, which focuses on controlling and improving operational processes and supporting organizations in making informed decisions, using resources efficiently and improving operational performance.

## Description of problem

The operational purchasing process at Hytech-Pommec currently involves substantial manual work by the operational buyer. Purchasing activities are performed mainly in Exact and include processing purchasing requirements, checking incoming information, deciding when orders should be placed, combining requirements from the same supplier, checking purchase prices, processing supplier confirmations and handling exceptions or questions that arise during the process.

Initial observations show that the workload does not come from one single problem. It consists of several types of work. Some activities are repetitive and administrative, such as manually creating purchasing lines, forwarding purchase orders to suppliers and updating information in Exact. Other activities involve manual verification, for example comparing current supplier prices with prices stored in Exact or checking supplier confirmations line by line. The buyer also performs judgement-intensive activities, such as deciding whether an item should be ordered immediately or whether the order can be postponed and combined with other demand. In addition, incomplete or suspicious purchasing requests may require the buyer to search through historical orders and use his own experience to determine whether the supplied information is plausible.

The process is also affected by interruptions and rework. Purchasing requests can arrive through different channels, including Exact, email, phone/desk contact, screenshots, direct requests from colleagues and occasionally letter/paper input. Cases can also be returned by Finance when a possible discrepancy is detected, requiring the buyer to investigate an order again. Furthermore, some system actions are important for preventing later problems. For example, purchased quantities need to be correctly assigned to the underlying project or production demand; otherwise the system may continue to regard the demand as unresolved, which can create a risk of duplicate purchasing.

The main problem for the company is therefore that a substantial part of the operational buyer's workload is spent on manual information handling, repetitive checking, investigating exceptions and switching between different tasks. This primarily affects employees involved in the purchasing process, but inefficient purchasing can also indirectly affect production and projects when information is incorrect, purchasing decisions are delayed or unnecessary rework occurs.

The exact size and causes of the workload have not yet been fully quantified. The first phase therefore maps and measures the current process to determine which activities create the most workload and which can support a responsible, testable AI contribution. Conventional process redesign, rules and automation remain possible supporting components and company recommendations.

## Research question and objective

The objective of this BEP is to identify where the main sources of workload occur within the operational purchasing process at Hytech-Pommec and to reduce this workload through a focal solution containing a meaningful AI-supported contribution, while preserving purchasing activities that require human expertise. Conventional automation and process redesign may support the artifact or remain separate recommendations. A non-AI focal artifact requires evidence that no candidate passes the responsible-AI/data/quality/evaluation gates and explicit company plus academic-supervisor approval.

Furthermore, one purchasing activity will be selected for design and evaluation. Candidates first pass non-compensable permission/data, ground-truth, risk-control, BEP-feasibility and meaningful-AI-fit gates. Surviving candidates are compared with literature-grounded, evidence-anchored criteria whose weights are agreed with project stakeholders and checked through sensitivity analysis. The design, artifact and evaluation address only the selected activity; other supported opportunities remain recommendations to Hytech-Pommec.

### Definitions

**Workload.** In this project, operational buyer workload is the broad burden associated with carrying out operational purchasing work. Following Bowling and Kirkendall (2012), the project distinguishes the **amount of work** from the **difficulty of work** rather than defining workload through processing time alone. Observable indicators such as task frequency, active processing time, case volume and rework are used to describe quantitative work burden, while uncertainty, exceptions and problem solving provide qualitative difficulty evidence. **Mental workload** is treated as one specific component of this broader construct and is interpreted using Young et al. (2015). Expertise dependence and organizational constraints are kept analytically distinct where relevant. The exploratory Measure phase therefore produces a multidimensional workload profile rather than one unvalidated total-workload score.

**Quality.** Quality refers to the extent to which the outcome of a purchasing activity fulfils the requirements relevant to that activity. The specific rubric is defined after focal-case selection, but success is always conjunctive: the predeclared workload endpoint must improve by at least a meaningful threshold and the final human-approved outcome must pass its quality guardrail. The case-specific threshold, comparator, rubric and acceptable minor-error margin are frozen before artifact development/formal testing.

### Provisional research question

> **To what extent can an AI-supported artifact reduce the operational buyer's workload at Hytech-Pommec without reducing the quality of the purchasing outcome?**

### Sub-questions

1. Which activities in the operational purchasing process contribute most to the operational buyer's workload in terms of frequency, processing time, rework and judgement required?
2. What conditions and control measures are required for the proposed solution to be implemented reliably in the operational purchasing process?
3. Which of these activities offers the greatest potential for AI-supported improvement, considering workload contribution, business relevance, technical feasibility and the need for human expertise?
4. To what extent does the proposed solution reduce workload while maintaining the required quality of the purchasing activity, when compared with current practice?

## Research Design

This project uses **DMAIC** as the overall framework for improving the operational purchasing process at Hytech-Pommec. Define, Measure and Analyze are used to understand the current process, establish a workload baseline and identify the most suitable improvement opportunity.

The exploratory Measure phase uses structured live observation. The 28 August pilot established a two-level architecture: observable work is coded at broad family level during shadowing, then mapped to detailed Task IDs post-session where evidence supports it. Two official baseline days are complete: 31 August (165 net / 103 timed coded-active minutes after the OBS-05 transcription correction) and 1 September (186 net / 162 timed coded-active minutes), totaling **351 net observed minutes** and **265 timed coded-active minutes**. Measurement Protocol v1.3 is controlled from 2 September without changing the v1.2 live fields/timing. The current target is five distinct observation days followed by a coverage review; five days is not assumed to equal 40 net hours. Detailed Exact/Orbis production-data/interface feasibility remains deferred until Analyze can target shortlisted candidates.

Within the **Improve** phase, **DSRM** guides design, development, demonstration and evaluation of the selected AI-supported artifact. Before development/formal testing, the project freezes the primary workload endpoint (normally active human handling time per eligible case/line), meaningful-improvement threshold and final-human-outcome quality guardrail. The **Control** phase then focuses on implementation recommendations, monitoring and maintaining the improved process.

In this way, DMAIC structures the overall process-improvement project, while DSRM provides the detailed artifact-development and evaluation structure within the Improve phase.

## Communication / Expectations

A meeting with the university supervisor is scheduled on a weekly basis. These meetings will be used to discuss the progress of the BEP, methodological decisions, research findings and upcoming activities. The student is responsible for planning and carrying out the research, communicating progress and preparing material for feedback. Feedback from the supervisor will primarily be provided during the weekly meetings and, when necessary, through email or Teams. The university supervisor has an advisory and academic supervisory role, while the company supervisor supports access to company information, employees and the operational context.

## References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

---

**Origin:** Markdown mirror created from the 26 August 1BEPIEX Word draft and subsequently synchronized through 2 September with the repository's current workload, Measure and methodology framing.
