# Literature package: operational purchasing, AI support, workload, quality, and research methodology

This register tracks literature by its current likelihood of use and states **where each source supports the BEP**. Detailed methodology, operational definitions and candidate decisions belong in the corresponding authoritative files under `docs/`.

## Current conceptual literature structure

The BEP currently distinguishes the **broad occupational workload construct** from the more specific construct of **mental workload**:

- **Overall / occupational workload:** grounded primarily in Bowling & Kirkendall (2012), who review workload as a broad construct reflecting the amount and/or difficulty of work and distinguish quantitative, qualitative, objective/perceived, and mental/physical aspects.
- **Quantitative workload:** supported by Spector & Jex (1998), especially their Quantitative Workload Inventory (QWI), which focuses on the quantity/pace of work.
- **Mental workload:** grounded specifically in Young et al. (2015). Young et al. is no longer treated as the definition of all operational-buyer workload.
- **Organizational constraints:** Spector & Jex (1998) provides a separate construct for conditions that interfere with work, useful when interpreting interruptions, inadequate information, system limitations or other work-process constraints.
- **Quality:** grounded generically in ISO 9000:2026 as fulfilment of relevant requirements. The concrete quality criterion is intentionally left activity-specific until the focal purchasing activity is selected.

### Reporting principle

The current literature does **not** justify inventing a composite equation such as `total workload = time + interruptions + mental demand + rework`. Indicators with different meanings and units should therefore be reported as a **multidimensional workload profile** unless a validated composite instrument is explicitly selected for a specific construct (for example NASA-TLX for subjective mental workload).

---

## Confirmed use

### Process-improvement methodology: DMAIC

**The Council for Six Sigma Certification. (2018).** *Six Sigma Green Belt Certification Training Manual*. June 2018 edition. https://www.sixsigmacouncil.org/wp-content/uploads/2018/09/Six-Sigma-Green-Belt-Certification-Training-Manual-CSSC-2018-06b.pdf

**Use:** Supports DMAIC terminology and structure in `docs/methodology/Phase_1_Current_Methodology.md`.

### Artifact design and evaluation: DSRM

**Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007).** *A Design Science Research Methodology for Information Systems Research*. Accessible process paper stored as `open-access/05-design-science-research-process.pdf`; cite the original DSRM article: https://doi.org/10.2753/MIS0742-1222240302

**Use:** Supports artifact design/development/evaluation in the methodology file.

### Overall occupational workload

**Bowling, N. A., & Kirkendall, C. (2012).** *Workload: A Review of Causes, Consequences, and Potential Interventions*. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary Occupational Health Psychology: Global Perspectives on Research and Practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

**Use:** Primary broad workload source for the BEP. Supports treating workload as broader than processing time alone and distinguishes important facets including quantitative workload (amount of work) and qualitative workload (difficulty of work), as well as objective/perceived and mental/physical distinctions. This source provides the umbrella framing; it does **not** imply that heterogeneous workload indicators should be summed into one unvalidated score.

### Quantitative workload and organizational constraints

**Spector, P. E., & Jex, S. M. (1998).** *Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory*. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

**Use:** Supports the distinction between quantitative workload and organizational constraints. The Quantitative Workload Inventory is relevant to the quantity/pace of work; the Organizational Constraints Scale is relevant conceptually when interpreting barriers that interfere with task completion. These validated self-report scales are literature anchors, not automatic requirements to administer them in the BEP.

### Mental workload

**Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015).** *State of science: Mental workload in ergonomics*. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

**Use:** Governing source specifically for **mental workload**, not for all operational-buyer workload. Supports treating mental workload as a multidimensional human-factors construct and cautions against inferring it from processing time alone. The detailed project interpretation belongs in `docs/methodology/Workload_Definition.md`.

### Generic quality definition

**International Organization for Standardization. (2026).** *ISO 9000:2026 — Quality management — Fundamentals and vocabulary*. https://www.iso.org/standard/9000.html

**Use:** Generic quality anchor. ISO 9000 defines quality in relation to the degree to which characteristics fulfil requirements. For this BEP, the relevant purchasing requirements and therefore the concrete quality criterion will depend on the focal activity selected after Measure/Analyze. This avoids prematurely equating quality with accuracy, completeness, decision consistency, or any one task-specific metric.

---

## High chance to use

### Supporting mental-workload operationalization and measurement

**Longo, L., Wickens, C. D., Hancock, G., & Hancock, P. A. (2022).** *Human mental workload: A survey and a novel inclusive definition*. *Frontiers in Psychology, 13*, 883321. https://doi.org/10.3389/fpsyg.2022.883321

**Use:** Supporting review for mental-workload theory and measurement choices. It complements rather than replaces Young et al. (2015).

### Purchasing automation

**Flechsig, C., Anslinger, F., & Lasch, R. (2022).** *Robotic Process Automation in purchasing and supply management*. https://doi.org/10.1016/j.pursup.2021.100718

**Use:** Direct procurement-automation evidence for evaluating which administrative purchasing activities are suitable for automation.

**Syed, R., Bandara, W., French, E., & Stewart, G. (2020).** *Robotic Process Automation: Contemporary themes and challenges*. https://doi.org/10.1016/j.compind.2019.103162

**Use:** Automation limitations, implementation risks and governance.

### Human-AI interaction and appropriate reliance

**Schemmer, M., Hemmer, P., Nitsche, M., Kühl, N., & Vössing, M. (2023).** *Appropriate Reliance on AI Advice*. PDF stored as `open-access/01-appropriate-reliance-ai-advice.pdf`. https://doi.org/10.1145/3581641.3584066

**Use:** Relevant if the final artifact provides advice that a buyer can accept, modify or reject.

**Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019).** *Guidelines for Human-AI Interaction*. PDF stored as `open-access/03-guidelines-human-ai-interaction.pdf`. https://doi.org/10.1145/3290605.3300233

**Use:** Design principles for feedback, control, correction and failures in an AI-supported interface.

**Bansal, G., Nushi, B., Kamar, E., Horvitz, E., & Weld, D. S. (2021).** *Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance*. PDF stored as `open-access/02-human-ai-complementary-team-performance.pdf`. https://doi.org/10.1145/3411764.3445717

**Use:** Relevant if evaluation examines the performance of a buyer–AI team. It is **not** used as the generic definition of purchasing quality; ISO 9000 provides that broader quality anchor.

---

## Possible use when we know more

### Subjective mental-workload measurement

**Hart, S. G. (2006).** *NASA-Task Load Index (NASA-TLX); 20 years later*. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 50*(9), 904–908. https://doi.org/10.1177/154193120605000909

**Use if needed:** Candidate validated subjective workload instrument if the selected activity or final before/after evaluation requires a mental-workload measure. NASA-TLX should not be interpreted as a measure of the entire operational-buyer workload construct.

### Supply monitoring and exception handling

**Fernandez et al. (2016).** *Framework for modelling and simulating the supply process monitoring to detect and predict disruptive events*. https://doi.org/10.1016/j.compind.2016.04.002

**Use if needed:** Monitoring/exception-focused artifact direction.

**Xu (2010).** *A Web-based system for proactive management of supply exceptions*. https://doi.org/10.1016/j.jmsy.2010.11.003

**Use if needed:** Proactive supply-exception handling.

### Process mining

**van der Aalst, W. M. P. (2012).** *Process Mining: Overview and Opportunities*. PDF stored as `open-access/04-process-mining-overview-opportunities.pdf`. https://doi.org/10.1145/2229156.2229157

**Use if needed:** Process mining if sufficiently detailed Exact/Orbis event-log data become available.

### Advice-taking, trust and buyer interaction with AI

**Bonaccio, S., & Dalal, R. S. (2006).** *Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences*. https://doi.org/10.1016/j.obhdp.2006.07.001

**Use if needed:** Judge-Advisor System-style buyer study.

**Lee, J. D., & See, K. A. (2004).** *Trust in Automation: Designing for Appropriate Reliance*. https://doi.org/10.1518/hfes.46.1.50_30392

**Use if needed:** Trust/appropriate reliance as an explicit evaluation construct.

**Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015).** *Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err*. https://doi.org/10.1037/xge0000033

**Use if needed:** Rejection of AI advice after errors.

**Logg, J. M., Minson, J. A., & Moore, D. A. (2019).** *Algorithm Appreciation: People Prefer Algorithmic to Human Judgment*. https://doi.org/10.1016/j.obhdp.2018.12.005

**Use if needed:** Counterpoint to algorithm aversion in a buyer-advice study.

### Task-solution fit and implementation evaluation

**Goodhue, D. L., & Thompson, R. L. (1995).** *Task-Technology Fit and Individual Performance*. https://doi.org/10.2307/249689

**Use if needed:** Explicit task-technology-fit evaluation.

**DeLone, W. H., & McLean, E. R. (2003).** *The DeLone and McLean Model of Information Systems Success: A Ten-Year Update*. https://doi.org/10.1080/07421222.2003.11045748

**Use if needed:** Broader implementation / information-system success evaluation.

---

## Copyright and access note

Only public, open-access or author-posted PDFs are stored in this repository. Publisher-restricted articles and standards are represented by DOI or official links and are not copied into the repository.