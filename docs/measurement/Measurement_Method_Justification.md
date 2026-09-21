# Measurement Method Justification — Exploratory Workload Baseline

**Status:** Methodological rationale added 3 September 2026; construct wording synchronized 15 September; the observation-to-analysis chain clarified 21 September. This document explains the evidence chain behind `Measurement_Protocol_v1.3.md` and the current [stage-organized analytical activity list](../process/Purchasing_Activity_Framework_2026-09-21.md). The 21 September clarification changes no live fields, timing rules, original observations or research questions.

## 1. Short answer

The Measurement Protocol is **not** a measurement instrument taken from Bowling and Kirkendall (2012) or Spector and Jex (1998).

It is a **researcher-developed, procurement-specific structured continuous-observation protocol** with three different foundations:

1. workload literature defines the constructs and prevents overclaiming;
2. continuous-observation time-and-motion literature supports the observation mechanics and workflow measures;
3. the Hytech-Pommec AS-IS process, task register and pilot observations provide the local basis for the broad live work families and field definitions.

This distinction must remain explicit in the thesis. A source can justify what a construct means without supplying the exact instrument used to observe it.

Van Weele's purchasing-process framework has a separate role: it organizes the analytical activity list by purchasing stage and task purpose. It did not originate or validate the observation method. Live observation retains the seven current families, **REQ, CLAR, DEC, PO, CHECK, SEND and OTHER**. The historical codebook also contained **EXC**, which remains visible in source records but is excluded under the current thesis scope. Detailed analytical activity labels are assigned after observation, without adding codes to the live sheet.

## 2. Evidence chain

| Layer | Question answered | Governing source or project evidence | Role in this BEP |
|---|---|---|---|
| Construct definition | What does workload mean? | Bowling & Kirkendall (2012); Spector & Jex (1998) | Distinguishes amount, difficulty and organizational constraints. Mental workload is not assessed. These sources do not provide the live procurement codebook. |
| Observation method | How can observable work patterns be recorded? | Mintzberg (1970); Fix et al. (2022); Zheng et al. (2011) STAMP; Lopetegui et al. (2014); Westbrook & Ampt (2009); Westbrook et al. (2012) WOMBAT | Supports structured shadowing, task categories, timestamps/duration, interruptions, non-observed periods, observation coverage, piloting and transparent reporting. |
| Cognitive/expertise elicitation | How can otherwise invisible cues and judgement be explored? | Militello & Hutton (1998) Applied Cognitive Task Analysis | Supports structured follow-up questioning about cues, decisions and expertise. A visual observation or `J/EXP` flag alone is not a validated cognitive-workload measurement. |
| Context-specific operationalization | Which purchasing activities and fields are relevant here? | AS-IS process v1.5, the task register, company evidence and the 28 August pilot | Provides the basis for broad live families, operational boundaries, case context and later task mapping. The historical eight-family codebook includes EXC; the current seven-family collection structure follows its scope exclusion. |
| Analytical activity framework | How are observed tasks distinguished within the purchasing process? | Van Weele purchasing stages, the existing task register, Dennis's relevant purchasing context, and the 17 September meeting; implemented in the [21 September activity list](../process/Purchasing_Activity_Framework_2026-09-21.md) | Organizes full analytical activity labels by stage and purpose. This is a later refinement of classification, not the source or validation of the live observation method. |
| Measurement-quality controls | How is unsupported precision avoided? | STAMP principles plus project-specific controls | Uses explicit definitions, observer-unavailable time, `MISS`, mapping confidence, retained raw records and dated protocol versions. |

### 2.1 How the measurement and analytical structures developed

The project developed its recording and analysis structures through the following linked steps. This is a provenance account, not a claim that the complete current framework existed before the first observations.

| Step | Evidence and resulting design choice |
|---|---|
| Exploratory observation and process understanding | Early shadowing, employee explanations and the buyer walkthrough supplied the AS-IS workflow and detailed task inventory, documented in [Process Cleaned V1.5](../process/Process_Cleaned_V1.5.md). The register continued to develop as observations exposed gaps and clarified the MAX sequence. |
| Literature-informed observation and pilot refinement | Continuous-observation literature supplies the recording principles described below. The [28 August pilot](Pilot_Measure_Observation_2026-08-28.md) exposed fragmented cases, returning-case identification problems, work outside the detailed register and information that could not be recalled reliably afterward. The methodological rationale was documented on 3 September; this does not establish that every later clarification was predefined before collection. |
| Broad families for live recording | The protocol groups observable work into broad families and defers detailed Task IDs to post-session enrichment. This reduces the classification burden while following changes between cases. The current seven-family limit is a practical project choice, not a number prescribed or validated by the literature. Historical EXC records retain their original label and scope exclusion. |
| Broader purchasing context | The [10 September scope decision](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md) includes relevant work by Dennis. The initial operational register is therefore a starting point, not an exhaustive list of every tactical purchasing task. Arno's workload remains the primary outcome; Dennis's evidence remains identifiable and separate. |
| Framework-guided analytical activity list | The [17 September meeting](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-17.md) calls for organizing the activity list around the purchasing framework and distinguishing similar actions at different stages. The [21 September list](../process/Purchasing_Activity_Framework_2026-09-21.md) uses concrete tasks and their purposes to implement that direction. The exact division between seven live families and detailed post-session labels is a researcher implementation choice, not an additional supervisor-validated protocol. |
| Row-level enrichment and analysis | Retained source rows receive supported Task IDs, a purchasing stage and a full analytical activity label. These assignments remain separately auditable. Analysis can compare purchasing activities within stages while preserving a family-level account for observations that lack sufficient detail. |

### 2.2 From one observed episode to an analytical activity

The live row remains `Case | Activity | Start | End | Volume | INT | DEC? | Result / short note`. Its `Activity` field contains a broad live family. The derived dataset additionally records **Analytical activity**, **Activity confidence** and **Assignment reason**, alongside the existing Task-ID and stage fields. The analytical field uses the full label in the stage-organized activity list, not an additional live code.

`Task confidence`, `Stage confidence` and `Activity confidence` answer different questions: whether the register task fits, whether the purchasing stage fits, and whether the specific analytical activity fits. For each, `C` means confident, `P` provisional and `?` unresolved. The assignment reason identifies the recorded purpose or source context supporting the activity label and any remaining limit. Known work outside the operational register can have register status `U` while its analytical activity is supported; a known stage does not automatically establish a detailed activity.

When one episode combines several supported activities, retain the combined description and count its minutes once. Do not manufacture task boundaries or divide minutes by the number of labels. An unknown task, stage or activity remains unknown, with eligible family-level evidence retained. The [scope and classification addendum](Scope_and_Classification_Addendum_2026-09-14.md) specifies these derived fields and the separate scope, quality and timing rules.

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

WOMBAT provides the closest published structural analogue. It uses defined task categories, records task timing, interruptions and simultaneous work, and can produce:

- proportion of observed time by task category;
- average or median task duration;
- number of tasks in a defined period;
- interruption rate per observed hour;
- contextual profiles involving communication or information resources.

The BEP borrows these **design principles**, not WOMBAT's clinical task taxonomy or a claim that the procurement protocol has inherited WOMBAT's validation.

The BEP's controlled baseline uses its own exclusive active-time rule for a buyer. The 17 September suggestion to record overlapping activity durations separately has **not** been implemented by this classification update. Any future timing change needs a dated definition and a comparability assessment; historical intervals remain under their original convention.

## 4. Construct-to-indicator map

| Current protocol element | What it can support | Basis | Claim limit |
|---|---|---|---|
| `Activity` family and occurrence count | Observable work mix and recurrence | Continuous-observation time-and-motion; project AS-IS/pilot taxonomy | Does not by itself establish high total or mental workload. |
| Derived stage and `Analytical activity` | Organization of supported observations by purchasing purpose | Purchasing-process framework plus project-specific task definitions | Classification adds no observation, duration or independent workload measure. Its uncertainty remains separate from live recording quality. |
| `Start` / `End` and active time | Observable buyer-capacity consumption for reliably timed episodes | Time-and-motion / WOMBAT | Active time is not mental workload and excludes passive waiting and untimed micro-activities. |
| Occurrences per net observed hour | Exposure-adjusted frequency within sampled windows | WOMBAT-style task and interruption rates; STAMP reporting | Describes the sampled windows; it is not automatically a representative weekly rate. |
| `Volume` | Case-size context for interpreting time and recurrence | Bowling & Kirkendall's amount facet plus project-specific operationalization | No cited source supplies the exact `lines/items` field; its validity depends on relevance to the selected activity. |
| `INT` and segmented/resumed episodes | Workflow fragmentation and an organizational constraint | STAMP / WOMBAT | An interruption count is not a direct mental-workload score and does not prove harm. |
| `Origin` / `Channel` | Context in which work arrives or is performed | WOMBAT-style contextual dimensions plus project-specific process evidence | These are explanatory/coverage variables, not workload dimensions by themselves. |
| `CLAR`, historical `EXC`, rework notes | Source evidence of additional or obstructed work | Amount/difficulty concepts plus project-specific process categories | Apply the current EXC/aftercare scope exclusion before analysis. Exception presence does not quantify perceived difficulty, and a different live family does not make excluded aftercare eligible. |
| `DEC?`, `J`, `EXP` and short reasoning notes | Screening evidence for judgement, cues and expertise dependence | CTA-informed elicitation | These flags are not validated workload scales. Use only when observed or explicitly explained; do not infer invisible cognition. |
| `MISS` and mapping confidence | Transparency about measurement uncertainty | STAMP-aligned reporting and researcher-defined data-quality controls | These improve traceability but do not repair missing data. |
| `frequency × representative active time` | Estimated operational time burden for comparable recurring work | Arithmetic combination of observed recurrence and duration | Researcher-defined capacity estimate, not a literature-validated total-workload equation. |

## 5. What the protocol validly measures

The protocol provides an exploratory profile of **observable operational work and workflow burden** during the sampled windows. Its strongest measures are:

- activity occurrence and occurrence rate;
- reliable active handling time and its distribution;
- time allocation across activity families, if coverage is sufficiently complete;
- interruptions and segmented/resumed work;
- observable clarification and other included work; historical exception/rework evidence remains available with its scope exclusions;
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

> This study examines the amount and difficulty of the operational buyer's work (Bowling & Kirkendall, 2012). Exploratory observations and the Hytech-Pommec AS-IS task inventory provide the local basis for a structured continuous-observation protocol, informed by STAMP reporting guidance (Zheng et al., 2011) and WOMBAT design principles (Westbrook & Ampt, 2009; Westbrook et al., 2012), and refined through pilot observation. Seven broad work families support live recording under the current scope; historical EXC observations retain their original labels and remain excluded from the thesis workload analysis. After each session, the available evidence supports enrichment with detailed tasks and analytical activities organized by Van Weele's purchasing stages. This later classification refinement incorporates relevant tactical purchasing context without replacing the observation method or adding live codes. Task, stage and activity assignments have separate confidence fields, and unresolved or inseparable work remains explicit. Occurrence and active time provide evidence about the amount of work; interruptions and case context describe workflow conditions; decision and expertise notes provide exploratory evidence about judgement and difficulty, supported where needed by structured follow-up questioning (Militello & Hutton, 1998). Arno's workload remains the primary outcome, with Dennis's evidence analyzed separately. The resulting profile supports problem investigation and subsequent improvement selection; it is not a validated total-workload score or a direct measure of purchasing quality.

## References

Bowling, N. A., & Kirkendall, C. (2012). Workload: A review of causes, consequences, and potential interventions. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary occupational health psychology: Global perspectives on research and practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Fix, G. M., Kim, B., Ruben, M. A., & McCullough, M. B. (2022). Direct observation methods: A practical guide for health researchers. *PEC Innovation, 1*, 100036. https://doi.org/10.1016/j.pecinn.2022.100036

Lopetegui, M., Yen, P.-Y., Lai, A., Jeffries, J., Embi, P., & Payne, P. (2014). Time motion studies in healthcare: What are we talking about? *Journal of Biomedical Informatics, 49*, 292–299. https://doi.org/10.1016/j.jbi.2014.02.017

Militello, L. G., & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands. *Ergonomics, 41*(11), 1618–1641. https://doi.org/10.1080/001401398186108

Mintzberg, H. (1970). Structured observation as a method to study managerial work. *Journal of Management Studies, 7*(1), 87–104. https://doi.org/10.1111/j.1467-6486.1970.tb00484.x

Spector, P. E., & Jex, S. M. (1998). Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Westbrook, J. I., & Ampt, A. (2009). Design, application and testing of the Work Observation Method by Activity Timing (WOMBAT) to measure clinicians' patterns of work and communication. *International Journal of Medical Informatics, 78*(Supplement 1), S25–S33. https://doi.org/10.1016/j.ijmedinf.2008.09.003

Westbrook, J. I., Creswick, N. J., Duffield, C., Li, L., & Dunsmuir, W. T. M. (2012). Changes in nurses' work associated with computerised information systems: Opportunities for international comparative studies using the revised Work Observation Method By Activity Timing (WOMBAT). *Nursing Informatics 2012*, 448. https://pmc.ncbi.nlm.nih.gov/articles/PMC3799166/


Zheng, K., Guo, M. H., & Hanauer, D. A. (2011). Using the time and motion method to study clinical work processes and workflow: Methodological inconsistencies and a call for standardized research. *Journal of the American Medical Informatics Association, 18*(5), 704–710. https://doi.org/10.1136/amiajnl-2011-000083
