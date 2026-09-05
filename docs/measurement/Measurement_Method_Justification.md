# Measurement Method Justification — Exploratory Workload Baseline

**Status:** Methodological rationale added 3 September 2026. This document explains the evidence chain behind `Measurement_Protocol_v1.3.md`; it does not change that protocol's live fields, coding boundaries or treatment of earlier observations.

## 1. Short answer

The Measurement Protocol is **not** a measurement instrument taken from Bowling and Kirkendall (2012), Spector and Jex (1998), or Young et al. (2015).

It is a **researcher-developed, procurement-specific structured continuous-observation protocol** with three different foundations:

1. workload literature defines the constructs and prevents overclaiming;
2. continuous-observation time-and-motion literature supports the observation mechanics and workflow measures;
3. the Hytech-Pommec AS-IS process, 31-task register and pilot observations determine the project-specific activity categories and field definitions.

This distinction must remain explicit in the thesis. A source can justify what a construct means without supplying the exact instrument used to observe it.

## 2. Evidence chain

| Layer | Question answered | Governing source or project evidence | Role in this BEP |
|---|---|---|---|
| Construct definition | What does workload mean? | Bowling & Kirkendall (2012); Spector & Jex (1998); Young et al. (2015) | Distinguishes amount, difficulty, organizational constraints and mental workload. These sources do not provide the live procurement codebook. |
| Observation method | How can observable work patterns be recorded? | Mintzberg (1970); Fix et al. (2022); Zheng et al. (2011) STAMP; Lopetegui et al. (2014); Westbrook & Ampt (2009); Westbrook et al. (2012) WOMBAT | Supports structured shadowing, task categories, timestamps/duration, interruptions, non-observed periods, observation coverage, piloting and transparent reporting. |
| Cognitive/expertise elicitation | How can otherwise invisible cues and judgement be explored? | Militello & Hutton (1998) Applied Cognitive Task Analysis | Supports structured follow-up questioning about cues, decisions and expertise. A visual observation or `J/EXP` flag alone is not a validated cognitive-workload measurement. |
| Context-specific operationalization | Which purchasing activities and fields are relevant here? | AS-IS process v1.5, the 31-task register, company evidence and the 28 August pilot | Produces the eight activity families, operational boundaries, case index and post-session task mapping used in this setting. |
| Measurement-quality controls | How is unsupported precision avoided? | STAMP principles plus project-specific controls | Uses explicit definitions, observer-unavailable time, `MISS`, mapping confidence, retained raw records and dated protocol versions. |

## 3. Why continuous observation fits the Measure purpose

The Measure phase needs to establish what work occurs, how often it occurs, how reliable active buyer time is distributed, and where interruptions or fragmented episodes occur. Continuous-observation time-and-motion is a close methodological fit because an observer follows work as it happens and records task categories and time.

Structured observation also has an established management-research precedent: Mintzberg (1970) describes structured observation as a method for studying managerial work. Fix et al. (2022) make the operationalization step explicit: the research question should determine what is observed, abstract theoretical concepts must be translated into observable definitions, and data-collection tools should be pilot-tested. These sources support the design logic but do not supply the BEP's exact procurement categories.

Zheng et al. (2011) define time-and-motion research around independent, continuous observation of work and propose the STAMP reporting checklist. Relevant STAMP elements include:

- fieldwork duration, shift/daypart distribution and total observation hours;
- definitions and classification of task categories;
- acknowledgement and justification of adapted or newly developed categories;
- observer preparation and pilot sessions;
- treatment of multitasking, non-observed periods and transitions;
- definition of analytical measures;
- optional interruption, interaction and location/context data.

Lopetegui et al. (2014) distinguish **continuous observation** from work sampling. Continuous observation records elapsed task time and is useful for short and non-centralized tasks; work sampling estimates time proportions at selected instants and is weaker for exact task durations, occurrences and workflow sequences. The current BEP method is therefore described as structured continuous observation, not work sampling.

WOMBAT provides the closest published structural analogue. It uses broad, mutually exclusive task categories, timestamps task changes, preserves interrupted tasks for later resumption and can produce:

- proportion of observed time by task category;
- average or median task duration;
- number of tasks in a defined period;
- interruption rate per observed hour;
- contextual profiles involving communication or information resources.

The BEP borrows these **design principles**, not WOMBAT's clinical task taxonomy or a claim that the procurement protocol has inherited WOMBAT's validation.

## 4. Construct-to-indicator map

| Current protocol element | What it can support | Basis | Claim limit |
|---|---|---|---|
| `Activity` family and occurrence count | Observable work mix and recurrence | Continuous-observation time-and-motion; project AS-IS/pilot taxonomy | Does not by itself establish high total or mental workload. |
| `Start` / `End` and active time | Observable buyer-capacity consumption for reliably timed episodes | Time-and-motion / WOMBAT | Active time is not mental workload and excludes passive waiting and untimed micro-activities. |
| Occurrences per net observed hour | Exposure-adjusted frequency within sampled windows | WOMBAT-style task and interruption rates; STAMP reporting | Describes the sampled windows; it is not automatically a representative weekly rate. |
| `Volume` | Case-size context for interpreting time and recurrence | Bowling & Kirkendall's amount facet plus project-specific operationalization | No cited source supplies the exact `lines/items` field; its validity depends on relevance to the selected activity. |
| `INT` and segmented/resumed episodes | Workflow fragmentation and an organizational constraint | STAMP / WOMBAT | An interruption count is not a direct mental-workload score and does not prove harm. |
| `Origin` / `Channel` | Context in which work arrives or is performed | WOMBAT-style contextual dimensions plus project-specific process evidence | These are explanatory/coverage variables, not workload dimensions by themselves. |
| `CLAR`, `EXC`, rework notes | Occurrence and active time of additional or obstructed work | Amount/difficulty concepts plus project-specific process categories | Exception presence can indicate burden but does not quantify perceived difficulty without additional evidence. |
| `DEC?`, `J`, `EXP` and short reasoning notes | Screening evidence for judgement, cues and expertise dependence | CTA-informed elicitation | These flags are not validated workload scales. Use only when observed or explicitly explained; do not infer invisible cognition. |
| `MISS` and mapping confidence | Transparency about measurement uncertainty | STAMP-aligned reporting and researcher-defined data-quality controls | These improve traceability but do not repair missing data. |
| `frequency × representative active time` | Estimated operational time burden for comparable recurring work | Arithmetic combination of observed recurrence and duration | Researcher-defined capacity estimate, not a literature-validated total-workload equation. |

## 5. What the protocol validly measures

The protocol provides an exploratory profile of **observable operational work and workflow burden** during the sampled windows. Its strongest measures are:

- activity occurrence and occurrence rate;
- reliable active handling time and its distribution;
- time allocation across activity families, if coverage is sufficiently complete;
- interruptions and segmented/resumed work;
- observable clarification, exception and rework episodes;
- contextual and qualitative evidence used to generate and screen focal-case candidates.

The protocol does **not** directly measure:

- total workload as one validated score;
- perceived workload;
- mental workload;
- hidden cognitive effort;
- the quality of purchasing outcomes;
- workload reduction caused by an AI artifact.

Those claims require an activity-specific evaluation protocol after the focal case is selected. If perceived or mental workload is important for that case, a suitable validated self-report instrument may be added prospectively rather than inferred from time.

## 6. Methodological qualifications and safeguards

### One-observer design

Because the same student is the only observer, conventional inter-observer reliability cannot be estimated for the baseline. The study should instead report this limitation and use proportionate controls: a precise codebook, pilot refinement, same-observer recoding of a small retained sample where possible, explicit uncertainty codes, and periodic discussion of ambiguous examples with the buyer or supervisor. Same-observer recoding is an intra-rater check and must not be called inter-rater reliability.

### Minute-level timing and sub-minute tallies

Retaining a genuine but unmeasurably brief action as a tally is preferable to inventing a zero- or one-minute duration. However, such a tally measures **occurrence only** and cannot contribute to active-time totals. If sub-minute work becomes frequent enough to affect candidate selection, minute-level timing will systematically understate time burden. That would justify a prospective, documented protocol version using seconds-level timestamps; earlier observations must remain unchanged and cross-version comparisons must state the difference.

### Healthcare origin of the method papers

STAMP and WOMBAT were developed mainly in healthcare workflow research. Their generic observation mechanics transfer plausibly to office purchasing work, but their clinical task categories and validation results do not. The BEP must therefore describe the procurement codebook as locally developed and pilot-refined, and must not claim that the whole protocol is externally validated merely because it follows STAMP/WOMBAT principles.

### Qualitative evidence

Exceptions, uncertainty and judgement notes are valuable screening evidence, but loosely written notes are not yet a reproducible measure of qualitative workload. For any shortlisted judgement-heavy activity, use a small predefined CTA-informed prompt set, for example: what cue was noticed, what decision was required, what made it difficult, what information was missing, what alternatives existed, and what prior experience mattered.

## 7. Thesis-ready method statement

> Operational buyer workload was conceptualized as a multidimensional construct, distinguishing the amount of work from its difficulty and keeping mental workload analytically separate (Bowling & Kirkendall, 2012; Young et al., 2015). The observable objective component was operationalized using a researcher-developed structured continuous-observation time-and-motion protocol informed by the STAMP reporting framework (Zheng et al., 2011) and WOMBAT design principles (Westbrook & Ampt, 2009; Westbrook et al., 2012). The procurement-specific activity taxonomy and operational boundaries were derived from the Hytech-Pommec AS-IS process and refined through pilot observation. Occurrence and active time were treated as indicators of observable operational burden; interruptions and case context as workflow constraints or explanatory variables; and decision/expertise notes as exploratory CTA-informed evidence (Militello & Hutton, 1998). The protocol was used for hotspot screening and focal-case selection and was not interpreted as a validated measure of total or mental workload.

## References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Fix, G. M., Kim, B., Ruben, M. A., & McCullough, M. B. (2022). Direct observation methods: A practical guide for health researchers. *PEC Innovation, 1*, 100036. https://doi.org/10.1016/j.pecinn.2022.100036

Lopetegui, M., Yen, P.-Y., Lai, A., Jeffries, J., Embi, P., & Payne, P. (2014). Time motion studies in healthcare: What are we talking about? *Journal of Biomedical Informatics, 49*, 292–299. https://doi.org/10.1016/j.jbi.2014.02.017

Militello, L. G., & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands. *Ergonomics, 41*(11), 1618–1641. https://doi.org/10.1080/001401398186108

Mintzberg, H. (1970). Structured observation as a method to study managerial work. *Journal of Management Studies, 7*(1), 87–104. https://doi.org/10.1111/j.1467-6486.1970.tb00484.x

Spector, P. E., & Jex, S. M. (1998). Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Westbrook, J. I., & Ampt, A. (2009). Design, application and testing of the Work Observation Method by Activity Timing (WOMBAT) to measure clinicians' patterns of work and communication. *International Journal of Medical Informatics, 78*(Supplement 1), S25–S33. https://doi.org/10.1016/j.ijmedinf.2008.09.003

Westbrook, J. I., Creswick, N. J., Duffield, C., Li, L., & Dunsmuir, W. T. M. (2012). Changes in nurses' work associated with computerised information systems: Opportunities for international comparative studies using the revised Work Observation Method By Activity Timing (WOMBAT). *Nursing Informatics 2012*, 448. https://pmc.ncbi.nlm.nih.gov/articles/PMC3799166/

Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015). State of science: Mental workload in ergonomics. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

Zheng, K., Guo, M. H., & Hanauer, D. A. (2011). Using the time and motion method to study clinical work processes and workflow: Methodological inconsistencies and a call for standardized research. *Journal of the American Medical Informatics Association, 18*(5), 704–710. https://doi.org/10.1136/amiajnl-2011-000083
