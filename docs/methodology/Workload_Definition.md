# Workload Definition — Operational Purchasing BEP

**Status:** Canonical project definition, synchronized 2 September 2026.

**Ownership:** This file defines what **workload** means in the BEP. Detailed live Measure-phase data-collection procedure belongs in `../measurement/Measurement_Protocol_v1.3.md`; research/candidate decisions belong in `Phase_1_Current_Methodology.md`; literature status belongs in `../../literature/README.md`.

---

# 1. Governing conceptual structure

The BEP does **not** equate all operational-buyer workload with mental workload.

The project uses a two-level structure:

1. **Operational buyer workload** is the broad project-level construct: the burden associated with carrying out operational purchasing work.
2. **Mental workload** is one specific component of that broader workload and is treated using the human-factors literature.

This distinction is necessary because purchasing work can consume substantial buyer capacity without necessarily being cognitively demanding. For example, repetitive PO forwarding can create operational burden through frequency and time while imposing relatively little mental workload.

The broad workload framing is grounded primarily in occupational-workload literature, especially **Bowling & Kirkendall (2012)**, while mental workload is grounded specifically in **Young et al. (2015)**.

---

# 2. Broad workload: amount and difficulty of work

**Bowling, N. A., & Kirkendall, C. (2012).** *Workload: A Review of Causes, Consequences, and Potential Interventions*. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary Occupational Health Psychology: Global Perspectives on Research and Practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

Bowling & Kirkendall review workload as a broad occupational construct involving both the **amount of work** and the **difficulty of work**. Their review distinguishes, among other facets, quantitative and qualitative workload.

For this BEP, that distinction is used as follows:

| Workload facet | Project interpretation | Purchasing examples |
|---|---|---|
| **Quantitative workload** | How much work must be performed / the quantity and pace of work | task frequency, number of cases, number of lines, repeated checking, repeated corrections, active processing time |
| **Qualitative workload** | How difficult or demanding the work is to perform | uncertainty, exceptions, problem solving, ambiguous information, complex verification, judgement-intensive cases |

This means two activities can contribute to workload in different ways. A repetitive administrative task can have high quantitative workload and low qualitative difficulty, while a fast expert decision can have low measurable time burden but high qualitative difficulty or expertise dependence.

---

# 3. Quantitative workload and organizational constraints

**Spector, P. E., & Jex, S. M. (1998).** *Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory*. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

Spector & Jex provide two useful distinctions for this project:

- the **Quantitative Workload Inventory (QWI)** concerns the quantity and pace of work;
- the **Organizational Constraints Scale (OCS)** concerns conditions that interfere with task performance.

The BEP uses these as conceptual anchors rather than assuming that the validated questionnaires themselves must be administered.

Examples of possible organizational constraints in the purchasing setting include:

- interruptions and task switching;
- unavailable or incomplete information;
- system limitations;
- waiting for another person or approval;
- hand-off problems.

These constraints may increase the burden of performing the work, but they are not automatically treated as identical to workload itself. They should be reported separately where useful.

---

# 4. Mental workload

**Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015).** *State of science: Mental workload in ergonomics*. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

Young et al. are used specifically for **mental workload**, not as the definition of all operational-buyer workload.

Their review treats mental workload as a multidimensional human-factors construct influenced by the interaction of task demands, operator characteristics, environmental/support conditions and required performance.

For this BEP, mental workload concerns the cognitive and attentional resources required to perform purchasing work under the actual work conditions.

Examples include:

| Perspective | Purchasing examples |
|---|---|
| **Task demand** | uncertainty, information volume, exceptions, verification requirement, competing demands |
| **Operator** | experience, familiarity, skill, attention, automatic versus controlled processing |
| **Environment / support** | Exact/Orbis support, information availability, interruptions, colleague support |
| **Required performance** | completing the purchasing activity to the required standard |

A short task should therefore not automatically be interpreted as low mental workload, and a long task should not automatically be interpreted as high mental workload.

---

# 5. Expertise dependence is not the same as mental workload

The BEP keeps **expertise dependence** analytically separate from mental workload.

A task may depend strongly on tacit knowledge or prior experience while being performed quickly and with little conscious effort by an experienced buyer. Therefore observations such as an experienced buyer instantly noticing an implausible specification are evidence of expertise dependence, but not sufficient by themselves to claim high mental workload.

Relevant indicators may include:

- tacit or undocumented cues;
- reliance on prior cases or historical knowledge;
- experience-dependent recognition;
- difficulty for a less experienced buyer to reproduce the same judgement using available rules and data.

Expertise dependence is important later when deciding whether work should be automated, supported, reviewed or retained by the human buyer.

---

# 6. Operational effort and process burden

The Measure phase may record observable process indicators such as:

- task frequency;
- active processing time;
- elapsed time;
- transaction or line volume;
- repeated manual actions;
- rework occurrence and rework time;
- interruptions and task switches;
- exceptions and investigations.

These indicators describe different aspects of the work. They must not automatically be interpreted as interchangeable measures of mental workload.

For comparable execution tasks, an estimate such as:

`operational effort volume = frequency × representative active processing time`

may be useful for estimating buyer-capacity consumption. It is an **operational effort metric**, not a total workload score.

Rework also has two possible analytical meanings:

- **rework occurrence** can indicate a process/quality problem;
- **rework time and repeated activity** add quantitative work for the buyer.

The same observed event may therefore inform more than one analysis, provided the interpretations are kept explicit.

---

# 7. No unvalidated total-workload equation

The BEP will not create an arbitrary equation such as:

`total workload = processing time + interruptions + mental demand + rework`

These indicators have different meanings and measurement units. Adding or weighting them would require a defensible validated aggregation method.

Unless such an instrument is deliberately selected later, workload will therefore be reported as a **multidimensional workload profile** rather than one composite score.

A validated instrument such as NASA-TLX may later be considered if the selected activity requires a subjective **mental-workload** measure. Such a score would apply to mental workload within the instrument's intended scope; it would not automatically represent the entire operational-buyer workload construct.

---

# 8. Reporting rule

When the BEP uses **operational buyer workload** without further qualification, interpret it as the broad project-level construct described in Sections 1–3, not as a synonym for mental workload.

Where evidence concerns only one aspect, use the more precise term, for example:

- `quantitative workload`;
- `qualitative workload`;
- `active processing time`;
- `operational effort volume`;
- `mental workload`;
- `rework burden`;
- `organizational constraint`;
- `expertise dependence`.

Do not claim that one task has greater **total workload** than another solely because it takes more time. Likewise, do not label a task high mental workload solely because it requires expertise.

The specific exploratory Measure indicators and coding rules are defined in `../measurement/Measurement_Protocol_v1.3.md`. After the focal activity is selected, the activity-specific evaluation protocol may introduce additional validated measures when justified.

---

# 9. Relationship to quality

Workload and quality are kept conceptually separate.

Quality is not defined by this file. The literature register currently uses ISO 9000 as the generic quality anchor: quality concerns the extent to which relevant requirements are fulfilled. The concrete purchasing requirements and quality metric depend on the activity eventually selected for design and evaluation.

This separation allows the BEP to ask whether buyer workload can be reduced **without reducing the quality of the purchasing outcome**, without defining quality through time or effort.
