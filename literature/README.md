# Literature package: operational purchasing, AI support, workload, quality, and research methodology

This register tracks recorded and possible uses of literature. **Listed, cited, citation-verified, abstract-reviewed and full-text-reviewed are different statuses.** “Confirmed use” below means a role is recorded in a project document; it does not certify that the source has been fully read or its claims independently verified. A DOI or stored PDF establishes an access route, not reading completion. Where no reading status is recorded, do not infer one. Detailed methodology, operational definitions and candidate decisions belong in the corresponding authoritative files under `docs/`.

**Audited 13 October 2026** against the citations in the two notebooks, the repository README and the current documents under `docs/` (the archive excluded); the "likely literature" list in the 10 June 2026 meeting notes was seen and is deliberately not registered, as dated leads with no recorded role.

## Current conceptual literature structure

The current BEP uses workload as the amount and difficulty of purchasing work. Mental-workload sources remain background literature, with no current mental-workload assessment:

- **Overall / occupational workload:** grounded primarily in Bowling & Kirkendall (2012), who review workload as a broad construct reflecting the amount and/or difficulty of work and distinguish quantitative, qualitative, objective/perceived, and mental/physical aspects.
- **Quantitative workload:** supported by Spector & Jex (1998), especially their Quantitative Workload Inventory (QWI), which focuses on the quantity/pace of work.
- **Mental workload:** Young et al. (2015) is retained as historical background. It does not govern the current Plan of Work or add a measurement requirement.
- **Organizational constraints:** Spector & Jex (1998) provides a separate construct for conditions that interfere with work, useful when interpreting interruptions, inadequate information, system limitations or other work-process constraints.
- **Quality:** grounded generically in ISO 9000:2026 as fulfilment of relevant requirements. The concrete rubric remains activity-specific; the project predeclares that workload improvement cannot compensate for a failed quality guardrail.

### Reporting principle

The current literature does not justify adding indicators with different meanings and units into one total-workload score. The study reports separate indicators and qualitative task evidence. The focal evaluation must justify its selected workload endpoint and purchasing-quality criteria before development and testing.

---

## Reading order for the current work

Read to support the claims being written or the design decision being made; the full register is not a compulsory reading list. No new reading completion is claimed by this order.

1. **Define the research claims:** Bowling & Kirkendall for amount/difficulty of work; Bäckstrand et al. for the purchasing framework; Zheng et al. for reporting the observation method. Use the current definitions and method justification to identify the exact passages needed. Add Spector & Jex or WOMBAT sources where those constructs or mechanics are actually discussed.
2. **Support the current analysis:** Kendall & Babington Smith and Friedman for Kendall's W and its Friedman test on the order of the activities by day, and Lin for the Jensen-Shannon divergence between the days' shares (section 4.3 of the [analysis notebook](../Arno_Analysis_2026_10_02.ipynb); chosen with Zhongxin on 13 October). The NIST Kruskal-Wallis page and SciPy only for the Kruskal-Wallis tests kept for episode lengths by day (7.1) and CHECK minutes per line (5.4). Ebeling, Montgomery & Runger and the NIST/SEMATECH handbook (section 8.2.2.1) for the probability-plot fits (7.2 and Appendix A). Hsieh & Shannon, Guest et al. and Cohen belonged to the note-based coding layer [archived](../docs/archive/kinds_of_work/README.md) on 12 October; they are historical leads.
3. **Bound the proposed AI support:** Parasuraman et al. for functions and automation levels, then Burger et al. for the buyer's role in procurement. For the provisional focal case (order and confirmation checking), read Tater et al.; add DocILE if the design uses document-field/line extraction. Check what each source demonstrates and the limits of transferring it to this task.
4. **Write the design and evaluation rationale:** de Mast & Lokkerbol for DMAIC and Peffers et al. **2007** for DSRM; the stored 2006 paper is a different source. Consult the MCDA sources for the selection methods actually used (Edwards & Barron for the swing weights; Belton & Stewart, the DCLG manual and Goodhue & Thompson for the criteria; Triantaphyllou & Sánchez for the sensitivity check), and the quality/human–AI interaction sources for the chosen rubric and review interface.

Drawing-search, maximalisatie, process-mining, advice-taking and mental-workload sources remain conditional or historical. Read them only if the corresponding question enters the selected study; do not add those studies to the work plan merely because the references are listed.

**Gaps with no source yet (13 October):**

- Checking supplier quotations or order confirmations against a PO; Tater et al. cover invoices, later in the process.
- Process redesign directions (eliminate, simplify, standardise, automate or support), named in the [methodology's](../docs/methodology/Phase_1_Current_Methodology.md#2-research-structure) description of Analyze.
- Evaluating the artifact in DSRM beyond Peffers et al.; needed early in Improve.
- The permutation reference for the Jensen-Shannon p-value (whole case-days shuffled between the days, section 4.3 of the analysis notebook) cites no source; add one if the thesis reports that p-value.
- A full reference for Van Weele (2018), which the [activity framework](../docs/process/Purchasing_Activity_Framework_2026-09-21.md) cites as the origin of the purchasing-process model (Figure 1.2, p. 9); this register records only its reproduction in Bäckstrand et al.

Sources may be listed provisionally, with their citation status shown. Verify the citation before a source is used in the thesis, and set "full text reviewed" only after Yijie has read it.

---

## Plan of Work reference check, 22 September 2026

All five references in the submitted [Plan of Work](../docs/proposal/Plan_of_Work_Final_2026-09-22.pdf) were already recorded in the repository before this check. Four appeared in this register; Bäckstrand et al. appeared in the purchasing-framework documents and is now included under Confirmed use.

**A recorded reference is not the same as a stored PDF.** None of the five exact publications cited in the Plan of Work has a PDF stored in `literature/open-access/`. Existing DOI and full-text links provide their access routes. The stored Peffers PDF is a related 2006 conference paper, not the 2007 journal article. This check confirms repository presence and use in the proposal; it does not establish that every full text has been read.

| Reference used in the Plan of Work | Purpose in the proposal | Existing repository evidence | Access and file status |
|---|---|---|---|
| Bäckstrand et al. (2019) | Van Weele's purchasing stages and the operational/tactical process context | [Activity framework](../docs/process/Purchasing_Activity_Framework_2026-09-21.md) and [earlier mapping](../docs/archive/process/Van_Weele_Activity_Mapping_2026-09-14.md), both explicitly cite section 3.2 and Figure 3 | Existing [university-hosted full text](https://repub.eur.nl/pub/123697/Repub_123697_O-A.pdf); no stored PDF |
| Bowling & Kirkendall (2012) | Workload as the amount and difficulty of work | This register and [workload definition](../docs/methodology/Workload_Definition.md) | Existing DOI link below; no stored PDF |
| de Mast & Lokkerbol (2012) | DMAIC as the overarching problem-solving structure | Confirmed use in this register | Existing DOI link below; no stored PDF |
| Peffers et al. (2007) | DSRM for artifact design, demonstration and evaluation | Confirmed use in this register | Existing DOI link below; the stored 2006 paper is a different publication |
| Zheng et al. (2011) | Structured continuous observation and transparent method reporting | This register and [measurement-method justification](../docs/measurement/Measurement_Method_Justification.md) | Existing DOI link below; no stored PDF |

The proposal's five references are retained because they are already part of the project's recorded literature. Unrelated stored PDFs are not substitutes for the workload, DMAIC, purchasing-process or observation-method sources. The confirmed-use entries below explain each source's role and limits.

---

## Confirmed use

### Purchasing-process framework: Van Weele's stages

**Bäckstrand, J., Suurmond, R., van Raaij, E., & Chen, C. (2019).** *Purchasing process models: Inspiration for teaching purchasing and supply management*. *Journal of Purchasing and Supply Management, 25*, Article 100577. https://doi.org/10.1016/j.pursup.2019.100577

**Access:** [University-hosted full text](https://repub.eur.nl/pub/123697/Repub_123697_O-A.pdf), already linked in the activity-framework and mapping documents. No PDF of this article is stored in the repository.

**Use:** Section 3.2 and Figure 3 reproduce Van Weele's purchasing-process model and support the six-stage framework used in the Plan of Work and the [analytical activity framework](../docs/process/Purchasing_Activity_Framework_2026-09-21.md). The source provides the process structure. The task register, seven live recording families and row-level stage/activity assignments are this project's local operationalization, not a validated coding instrument supplied by the article. The analysis notebook cites it in *How the analysis is done* for the purchasing stages of part 4.2, which the selection notebook's candidate definitions reuse.

**Also cited for the stages, not recorded here with a full reference (13 October):** the activity framework names Van Weele (2018, Figure 1.2, p. 9) as the model's origin, [Nevi's purchasing-process explanation](https://nevi.nl/inkoop/inkoopkennis/inkoopproces) for the six stages and the [author's chapter 2 teaching materials](https://www.arjanvanweele.com/presentations-powerpoint/) for the placement of order-confirmation requests. Add the book's full reference before the thesis cites it directly; the two web pages should be cited with an access date, which the framework does not record.

### Process-improvement methodology: DMAIC / Six Sigma

**de Mast, J., & Lokkerbol, J. (2012).** *An analysis of the Six Sigma DMAIC method from the perspective of problem solving*. *International Journal of Production Economics, 139*(2), 604–614. https://doi.org/10.1016/j.ijpe.2012.05.035

**Use:** Primary peer-reviewed academic support for treating DMAIC as a structured problem-solving/improvement method and for explaining the logic of Define–Measure–Analyze–Improve–Control in the BEP. The analysis notebook's executive summary cites it to place the analysis in the Analyze phase.

**Schroeder, R. G., Linderman, K., Liedtke, C., & Choo, A. S. (2008).** *Six Sigma: Definition and underlying theory*. *Journal of Operations Management, 26*(4), 536–554. https://doi.org/10.1016/j.jom.2007.06.007

**Use:** Peer-reviewed background on Six Sigma as an organized process-improvement approach and its organizational structure. Useful for academic justification beyond practitioner manuals.

**The Council for Six Sigma Certification. (2018).** *Six Sigma Green Belt Certification Training Manual*. June 2018 edition. https://www.sixsigmacouncil.org/wp-content/uploads/2018/09/Six-Sigma-Green-Belt-Certification-Training-Manual-CSSC-2018-06b.pdf

**Use:** Practitioner source for terminology and practical DMAIC structure. It should not be the sole academic justification for DMAIC in the thesis.

### Artifact design and evaluation: DSRM

**Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007).** *A design science research methodology for information systems research*. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

**Use:** The current Plan of Work cites this journal article for the Design Science Research Methodology (DSRM) guiding artifact objectives, design/development, demonstration and evaluation within Improve. The selection notebook lists it in its reference list (Appendix D).

**Access:** The journal article is recorded through its DOI. Its PDF is not stored in this repository. The similarly named local PDF below is an earlier publication with a different author list and must not be presented as the journal article.

**Related stored source:** Peffers, K., Tuunanen, T., Gengler, C. E., Rossi, M., Hui, W., Virtanen, V., & Bragge, J. (2006). *The design science research process: A model for producing and presenting information systems research*. In *Proceedings of the First International Conference on Design Science Research in Information Systems and Technology (DESRIST 2006)* (pp. 83–106). Claremont Graduate University. [Stored PDF](open-access/05-design-science-research-process.pdf); [university publication record](https://research.aalto.fi/en/publications/the-design-science-research-process-a-model-for-producing-and-pre/).

The stored 2006 paper describes the six-activity design-science research process (DSRP), including demonstration and evaluation. It is relevant supporting material, but it is not cited in the current Plan of Work. Its title page and PDF pages 8, 10 and 11 were checked on 22 September 2026.

### Multi-criteria focal-case selection

Belton & Stewart, the DCLG manual and Goodhue & Thompson are cited in the [methodology's](../docs/methodology/Phase_1_Current_Methodology.md#53-formal-two-stage-selection-rule) section 5.3 and in section 3 of the [selection notebook](../Focal_Case_Selection_2026-10-07.ipynb); Edwards & Barron in the [swing-weight record](../docs/analyze/Swing_Weights_Yijie_2026-10-07.md) of 7 October and the notebook's section 3; Triantaphyllou & Sánchez in the methodology's reference list; all five in the notebook's Appendix D. The criteria, anchors and cut-offs are project judgements informed by these sources, not numbers they prescribe.

**Belton, V., & Stewart, T. J. (2002).** *Multiple Criteria Decision Analysis: An Integrated Approach*. Kluwer Academic Publishers. https://doi.org/10.1007/978-1-4615-1495-4

**Use:** Governing academic basis for structuring the candidate decision, separating objectives/criteria, modelling stakeholder preferences and using MCDA as decision support rather than as an automatic truth machine.

**Department for Communities and Local Government. (2009).** *Multi-Criteria Analysis: A Manual*. ISBN 978-1-4098-1023-0. https://www.gov.uk/government/publications/multi-criteria-analysis-manual-for-making-government-policy

**Use:** Official practitioner guidance for documenting the decision context, options, criteria, performance matrix, scoring, weighting and uncertainty. It supports the transparent selection procedure but does not supply universally correct project weights.

**Edwards, W., & Barron, F. H. (1994).** SMARTS and SMARTER: Improved simple methods for multiattribute utility measurement. *Organizational Behavior and Human Decision Processes, 60*(3), 306–325. https://doi.org/10.1006/obhd.1994.1087

**Use:** Primary source for the swing-weighting procedure used in the selection: an additive score in which each criterion's weight is the value of its swing from worst to best, relative to the most important swing (SMARTS).

**Triantaphyllou, E., & Sánchez, A. (1997).** *A sensitivity analysis approach for some deterministic multi-criteria decision-making methods*. *Decision Sciences, 28*(1), 151–194. https://doi.org/10.1111/j.1540-5915.1997.tb01306.x

**Use:** Supports testing whether the candidate ranking is robust to plausible changes in weights and evidence scores. The BEP uses a proportionate sensitivity check rather than claiming that one provisional weight set is objectively correct.

**Goodhue, D. L., & Thompson, R. L. (1995).** Task-technology fit and individual performance. *MIS Quarterly, 19*(2), 213–236. https://doi.org/10.2307/249689

**Use:** Supports the AI–task-fit criterion: technology should match the actual task if it is expected to improve individual performance. Literature supports the criteria and method; the student and academic supervisor agree project-specific research weights, while the company supervisor validates the operational evidence and feasibility.

### Selection criteria adopted from the literature (16 October 2026)

Cited in sections 2 and 3 of the [selection notebook](../Focal_Case_Selection_2026-10-07.ipynb) for the criteria set adopted on 16 October; the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md) records what each source contributes and the recurrence counts. Zhongxin's other two sources (Parasuraman et al., 2000; the Futran blog) are listed under the AI functions and in the synthesis.

**Agaton, B., & Swedberg, G. (2018).** *Evaluating and developing methods to assess business process suitability for robotic process automation: A design research approach* [Master's thesis, Chalmers University of Technology and University of Gothenburg]. https://odr.chalmers.se/handle/20.500.12380/255664

**Use:** Gates before scores and the value floor (gate 7): a process must show value in at least one category and pass the mandatory criteria; an early count of criteria across 23 mostly industry sources.

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (sections 3.2–3.3 and 4.2–4.3); citation from its reference list, to verify against the publisher record before thesis use.

**Bédard, M., Leshob, A., Benzarti, I., Mili, H., Rab, R., & Hussain, O. (2024).** A rule-based method to effectively adopt robotic process automation. *Journal of Software: Evolution and Process, 36*(11), e2709. https://doi.org/10.1002/smr.2709

**Use:** Suitability as two sub-goals that must both hold, relevance and feasibility: the basis of the value and feasibility families; proneness to human error as relevance (A2).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Brakemeier, H., Gerbert, P., Hartmann, P., Liebl, A., Schamberger, M., & Waldmann, A. (n.d.).** *Applying AI: How to find and prioritize AI use cases*. appliedAI Initiative. https://www.appliedai.de/assets/images/280323_AI_Whitepaper_UseCase_Screen.pdf

**Use:** AI use cases assessed on value and ease of implementation: data (B6), a minimum accuracy (B7), effort (B8). A practitioner source; cite as such.

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Costa, D. S., Mamede, H. S., & da Silva, M. M. (2023).** A method for selecting processes for automation with AHP and TOPSIS. *Heliyon, 9*(3), e13683. https://doi.org/10.1016/j.heliyon.2023.e13683

**Use:** One of Zhongxin's sources: a published criteria list with five-point scales (frequency and duration, A1) and an AHP-TOPSIS ranking. Cite the criteria and the procedure, not its weights, which do not reproduce from the printed tables.

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Engel, C. T. (2022).** *Cognitive automation: Assessing business process automation potentials in organizations driven by artificial intelligence* [Doctoral dissertation no. 5217, University of St.Gallen].

**Use:** Criteria for cognitive rather than rule-based automation: machine-learning suitability (B5, after Sturm et al.), a measurable goal (B7) and effort (B8).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (the assessment model and the method); citation from its reference list, to verify against the publisher record before thesis use.

**Farinha, D., Pereira, R., & Almeida, R. (2024).** A framework to support robotic process automation. *Journal of Information Technology, 39*(1), 149–166. https://doi.org/10.1177/02683962231165066

**Use:** The most complete single RPA criteria set (review and fuzzy Delphi), and the only one with a test-data criterion (B7).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Flechsig, C., Anslinger, F., & Lasch, R. (2022).** Robotic Process Automation in purchasing and supply management: A multiple case study on potentials, barriers, and implementation. *Journal of Purchasing and Supply Management, 28*(1), 100718. https://doi.org/10.1016/j.pursup.2021.100718

**Use:** The purchasing precedent: suitable purchasing tasks, the value-by-feasibility matrix of the families, and purchasing uses close to the focal task (comparing documents with the PO).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (accepted manuscript); citation from its reference list, to verify against the publisher record before thesis use.

**Haan, W. J. (2021).** *How can process mining be used to identify robotic process automation opportunities?* [Bachelor's thesis, University of Twente]. https://purl.utwente.nl/essays/85792

**Use:** Technical suitability against added value; simple workload and error indicators (A1, A2).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (sections 4–5); citation from its reference list, to verify against the publisher record before thesis use.

**Herm, L.-V., Janiesch, C., Helm, A., Imgrund, F., Hofmann, A., & Winkelmann, A. (2023).** A framework for implementing robotic process automation projects. *Information Systems and e-Business Management, 21*(1), 1–35. https://doi.org/10.1007/s10257-022-00553-8

**Use:** Business impact (A3) among the selection criteria, and the screening of simpler technologies before selection (gate 6).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Jongeling, H. E., Lu, X., Beerepoot, I., van de Weerd, I., & Reijers, H. A. (2023).** Getting your RPA priorities straight with process mining: The PLOST framework. In *ECIS 2023 Research Papers* (Paper 308). https://aisel.aisnet.org/ecis2023_rp/308

**Use:** One of Zhongxin's sources: must-pass gates before a ranking, the structure of Sections 2 to 4 of the selection notebook; data access (B6) and few variations (B2).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Shafik Salah Elsayed, N., & Kassem, G. (2022).** Assessing process suitability for robotic process automation: A process mining approach. In *Wirtschaftsinformatik 2022 Proceedings* (Student Track, 18). https://aisel.aisnet.org/wi2022/student_track/student_track/18

**Use:** Structured digital input as a knock-out (gate 2, B4), with criteria measured on a purchase-to-pay log.

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Spreitzenbarth, J. M., Bode, C., & Stuckenschmidt, H. (2024).** Artificial intelligence and machine learning in purchasing and supply management: A mixed-methods review of the state-of-the-art in literature and practice. *Journal of Purchasing and Supply Management, 30*(1), 100896. https://doi.org/10.1016/j.pursup.2024.100896

**Use:** AI in purchasing: business value against ease of implementation per use-case cluster (A3, B6, B8).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Sturm, T., Fecho, M., & Buxmann, P. (2021).** To use or not to use artificial intelligence? A framework for the ideation and evaluation of problems to be solved with artificial intelligence. In *Proceedings of the 54th Hawaii International Conference on System Sciences* (pp. 206–215).

**Use:** Machine-learning suitability: rules that cannot be defined and a measurable goal (B5, B7).

**Status:** read only through Engel (2022), as summarised in the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md); cite as summarised there or read the paper before thesis use.

**Syed, R., Suriadi, S., Adams, M., Bandara, W., Leemans, S. J. J., Ouyang, C., ter Hofstede, A. H. M., van de Weerd, I., Wynn, M. T., & Reijers, H. A. (2020).** Robotic process automation: Contemporary themes and challenges. *Computers in Industry, 115*, 103162. https://doi.org/10.1016/j.compind.2019.103162

**Use:** A review of RPA process criteria (repetition and standardisation, B1; exceptions, B2) and of where the literature contradicts itself.

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (author's version); citation from its reference list, to verify against the publisher record before thesis use.

**Wanner, J., Hofmann, A., Fischer, M., Imgrund, F., Janiesch, C., & Geyer-Klingeberg, J. (2019).** Process selection in RPA projects: Towards a quantifiable method of decision making. In *Proceedings of the 40th International Conference on Information Systems (ICIS 2019)*. https://aisel.aisnet.org/icis2019/business_models/business_models/6/

**Use:** Quantified indicators of automation potential: execution frequency and time (A1), exceptions (B2).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026; citation from its reference list, to verify against the publisher record before thesis use.

**Wellmann, C., Stierle, M., Dunzer, S., & Matzner, M. (2020).** A framework to evaluate the viability of robotic process automation for business process activities. In *Business Process Management: Blockchain and Robotic Process Automation Forum* (Lecture Notes in Business Information Processing, pp. 200–214). Springer. https://doi.org/10.1007/978-3-030-58779-6_14

**Use:** Viability criteria in five perspectives; data at least semi-structured (B4).

**Status:** full text read for the [criteria synthesis](../docs/analyze/Selection_Criteria_Literature_2026-10-16.md), 16 October 2026 (accepted manuscript); citation from its reference list, to verify against the publisher record before thesis use.

### Activity pattern across the observation days: concordance and divergence

Cited in section 4.3 of the [analysis notebook](../Arno_Analysis_2026_10_02.ipynb) and in its reference list, for the test of whether the five observation days allocate Arno's time over the activities in the same way. Zhongxin chose Kendall's W on 13 October in place of the Kruskal-Wallis test named on 8 October, and asked for the Jensen-Shannon divergence ([13 October notes](../docs/meetings/Academic_Supervisor_Meeting_Notes_2026-10-13.md)); she asked that the thesis explains why Kendall's W and not other tests, and why this data table. The decision of 13 October to add two observation days (14 and 16 October) rests on these results. The Kruskal-Wallis test is kept only for episode lengths by day (7.1) and CHECK minutes per line (5.4); whether those results are reported as supplementary is a question put to Zhongxin ([reading guide](../docs/Current_Status_and_Reading_Guide.md#5-questions-for-zhongxin-15-october), question 2). Each entry records three separate statuses: citation verified, abstract reviewed and full text reviewed.

**Kendall, M. G., & Babington Smith, B. (1939).** The problem of m rankings. *The Annals of Mathematical Statistics, 10*(3), 275–287. https://doi.org/10.1214/aoms/1177732186

**Use:** Kendall's coefficient of concordance W: how far the days agree on the ranking of the activities by minutes (W = 0.42 on five days, 0.31 on seven). The notebook reads W as moderate agreement together with the descriptive tables, the rank correlation between each pair of days and the result with each day left out; with five days the test has little power.

**Status:** citation details copied from the analysis notebook's reference list, still to verify; abstract and full text not yet reviewed.

**Friedman, M. (1937).** The use of ranks to avoid the assumption of normality implicit in the analysis of variance. *Journal of the American Statistical Association, 32*(200), 675–701. https://doi.org/10.1080/01621459.1937.10503522

**Use:** The significance test of W is the Friedman test on the same ranks (chi-square = 8.48, df = 4, p = 0.075). Its null hypothesis is that the days rank the activities independently, so a significant W would be positive evidence of a shared pattern; a non-significant result does not show that the days differ or are the same.

**Status:** citation details copied from the analysis notebook's reference list, still to verify; abstract and full text not yet reviewed.

**Lin, J. (1991).** Divergence measures based on the Shannon entropy. *IEEE Transactions on Information Theory, 37*(1), 145–151. https://doi.org/10.1109/18.61115

**Use:** The Jensen-Shannon divergence between the days' activity shares (base 2, from 0 to 1; mean 0.113 over the 10 pairs of days). The notebook builds its reference distribution by shuffling whole case-days between the days; that permutation step cites no source (see the gaps above). The source defines the measure; it does not set a threshold for "different".

**Status:** citation details copied from the analysis notebook's reference list, still to verify; abstract and full text not yet reviewed.

### Overall occupational workload

**Bowling, N. A., & Kirkendall, C. (2012).** *Workload: A Review of Causes, Consequences, and Potential Interventions*. In J. Houdmont, S. Leka, & R. R. Sinclair (Eds.), *Contemporary Occupational Health Psychology: Global Perspectives on Research and Practice, Volume 2* (pp. 221–238). https://doi.org/10.1002/9781119942849.ch13

**Use:** Primary broad workload source for the BEP. Supports treating workload as broader than processing time alone and distinguishes important facets including quantitative workload (amount of work) and qualitative workload (difficulty of work), as well as objective/perceived and mental/physical distinctions. This source provides the umbrella framing; it does **not** imply that heterogeneous workload indicators should be summed into one unvalidated score.

### Quantitative workload and organizational constraints

**Spector, P. E., & Jex, S. M. (1998).** *Development of four self-report measures of job stressors and strain: Interpersonal Conflict at Work Scale, Organizational Constraints Scale, Quantitative Workload Inventory, and Physical Symptoms Inventory*. *Journal of Occupational Health Psychology, 3*(4), 356–367. https://doi.org/10.1037/1076-8998.3.4.356

**Use:** Supports the distinction between quantitative workload and organizational constraints. The Quantitative Workload Inventory is relevant to the quantity/pace of work; the Organizational Constraints Scale is relevant conceptually when interpreting barriers that interfere with task completion. These validated self-report scales are literature anchors, not automatic requirements to administer them in the BEP.

### Structured workflow observation and time-and-motion

**Mintzberg, H. (1970).** *Structured observation as a method to study managerial work*. *Journal of Management Studies, 7*(1), 87–104. https://doi.org/10.1111/j.1467-6486.1970.tb00484.x

**Use:** Management-domain precedent for using structured observation to study how work is actually performed. It supports the general choice of method, not the BEP's specific workload indicators or procurement categories.

**Fix, G. M., Kim, B., Ruben, M. A., & McCullough, M. B. (2022).** *Direct observation methods: A practical guide for health researchers*. *PEC Innovation, 1*, 100036. https://doi.org/10.1016/j.pecinn.2022.100036

**Use:** Supports defining what abstract, theory-informed concepts look like in observable practice, using a systematic collection tool and refining it through pilot testing. Its healthcare examples do not validate the procurement codebook.

**Zheng, K., Guo, M. H., & Hanauer, D. A. (2011).** *Using the time and motion method to study clinical work processes and workflow: Methodological inconsistencies and a call for standardized research*. *Journal of the American Medical Informatics Association, 18*(5), 704–710. https://doi.org/10.1136/amiajnl-2011-000083

**Use:** Primary methodological basis for describing the Measure approach as structured continuous observation and for reporting fieldwork duration, daypart/shift coverage, observation hours, task definitions, category development, observer preparation, non-observed periods, task transitions, analytical measures and interruptions. STAMP was developed in healthcare; it supports the generic method architecture, not validation of the procurement taxonomy.

**Westbrook, J. I., & Ampt, A. (2009).** *Design, application and testing of the Work Observation Method by Activity Timing (WOMBAT) to measure clinicians' patterns of work and communication*. *International Journal of Medical Informatics, 78*(Supplement 1), S25–S33. https://doi.org/10.1016/j.ijmedinf.2008.09.003

**Westbrook, J. I., Creswick, N. J., Duffield, C., Li, L., & Dunsmuir, W. T. M. (2012).** *Changes in nurses' work associated with computerised information systems: Opportunities for international comparative studies using the revised Work Observation Method By Activity Timing (WOMBAT).* *Nursing Informatics 2012*, 448. https://pmc.ncbi.nlm.nih.gov/articles/PMC3799166/

**Use:** Closest published structural analogue for broad task categories, timestamped activity changes, interruptions/resumption and outputs such as task frequency, task duration, time allocation and interruptions per observed hour. The BEP adopts these design principles but does not reuse the clinical taxonomy or inherit WOMBAT's setting-specific validation.

**Lopetegui, M., Yen, P.-Y., Lai, A., Jeffries, J., Embi, P., & Payne, P. (2014).** *Time motion studies in healthcare: What are we talking about?* *Journal of Biomedical Informatics, 49*, 292–299. https://doi.org/10.1016/j.jbi.2014.02.017

**Use:** Supports the explicit distinction between continuous observation and work sampling. This matters because the BEP records complete observable task episodes and durations within selected windows rather than sampling the activity present at periodic instants.

### Cognitive task analysis for judgement and expertise cues

**Militello, L. G., & Hutton, R. J. B. (1998).** *Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands*. *Ergonomics, 41*(11), 1618–1641. https://doi.org/10.1080/001401398186108

**Use:** Supports structured follow-up elicitation of cognitive skills, cues and demands for judgement-heavy work. It does not turn visually observed `DEC?`, `J` or `EXP` flags into validated mental-workload measurements; those remain screening prompts unless a fuller CTA procedure is used.

### Generic quality definition

**International Organization for Standardization. (2026).** *ISO 9000:2026 — Quality management — Fundamentals and vocabulary*. https://www.iso.org/standard/9000.html

**Use:** Generic quality anchor. ISO 9000 defines quality in relation to the degree to which characteristics fulfil requirements. For this BEP, the relevant purchasing requirements and therefore the concrete quality criterion will depend on the focal activity selected after Measure/Analyze. This avoids prematurely equating quality with accuracy, completeness, decision consistency, or any one task-specific metric.

---

## High chance to use

### AI functions, levels of automation and the buyer's role

Used for the [AI function comparison](../docs/methodology/AI_Function_Comparison_2026-10-02.md) requested on 1 October. Each entry records three separate statuses: citation verified, abstract reviewed and full text reviewed.

**Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000).** *A model for types and levels of human interaction with automation*. *IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 30*(3), 286–297. https://doi.org/10.1109/3468.844354

**Use:** Framework for the comparison table. It separates which function receives support (information acquisition, information analysis, decision and action selection, action implementation) from how independently the system performs it. A general automation model, not procurement-specific. Also listed in the selection notebook's reference list (Appendix D).

**Status:** citation verified 2 October 2026 (PubMed record); abstract and full text not yet reviewed.

**Burger, Nitsche & Arlinghaus (2023).** *Hybrid intelligence in procurement: Disillusionment with AI's superiority?* *Computers in Industry*, article 103946. https://doi.org/10.1016/j.compind.2023.103946 (free text as the first paper in https://d-nb.info/132636524X/34)

**Use:** Four procurement case studies of how buyers' expertise and AI complement each other, and their limits. Relevant to the buyers' concern about losing track of their work; does not show that human–AI collaboration automatically improves performance.

**Status:** citation verified 2 October 2026 (RWTH publication record; complete the author initials from it); abstract and full text not yet reviewed.

**Spreitzenbarth, J. M., Bode, C., & Stuckenschmidt, H. (2024).** *Artificial intelligence and machine learning in purchasing and supply management: A mixed-methods review of the state-of-the-art in literature and practice*. *Journal of Purchasing and Supply Management, 30*(1), 100896. https://doi.org/10.1016/j.pursup.2024.100896

**Use:** Background on procurement AI use cases from 46 studies and 20 expert interviews, and a source of further references. The included studies run from 1989 to 2020, so recent generative AI is not covered. Not cited in the comparison table or in another project document (checked 13 October); retained as background for the same section.

**Status:** citation details still to verify; abstract and full text not yet reviewed.

**Noy, S., & Zhang, W. (2023).** *Experimental evidence on the productivity effects of generative artificial intelligence*. *Science, 381*(6654), 187–192. https://doi.org/10.1126/science.adh2586

**Use:** Experimental evidence that generative AI helped professionals with writing tasks; supports investigating drafting help for clarification and supplier messages. Not procurement-specific.

**Status:** citation details still to verify; abstract and full text not yet reviewed.

The existing entry for Amershi et al. (2019) under *Human-AI interaction and appropriate reliance* also supports the comparison: buyers should be able to understand, inspect and correct AI suggestions.

### Statistics used in the analysis notebook

Sources for the probability-plot fits (section 7.2 and Appendix A) and the two Kruskal-Wallis tests kept after 13 October (7.1, episode lengths by day; 5.4, CHECK minutes per line) of the [analysis notebook](../Arno_Analysis_2026_10_02.ipynb). The fits describe the recorded episodes; no later result depends on them. The sources for the activity pattern across days are under Confirmed use. Same three statuses as above.

**Ebeling, C. E. (2019).** *An Introduction to Reliability and Maintainability Engineering* (3rd ed.). Waveland Press.

**Use:** Chapter 13, probability plots and least-squares fitting of the exponential, lognormal and Weibull distributions to the recorded durations. Course textbook. Cited in *How the analysis is done* and the reference list.

**Status:** citation details still to verify; the chapters used are known from the course.

**Montgomery, D. C., & Runger, G. C. (2014).** *Applied Statistics and Probability for Engineers* (6th ed.). Wiley.

**Use:** Sections 6-7 (probability plots) and 9-7 (comparing observed and expected counts), used descriptively. Course textbook. Cited in *How the analysis is done* and the reference list.

**Status:** citation details still to verify; the sections used are known from the course. The analysis notebook's reference list gives 2015 for the same edition; settle the year against the book's title page before citing it.

**NIST/SEMATECH.** *e-Handbook of Statistical Methods.* https://www.itl.nist.gov/div898/handbook/

**Use:** The plotting-position and least-squares equations ([section 8.2.2.1](https://www.itl.nist.gov/div898/handbook/apr/section2/apr221.htm)), cited in section 7.2 and the reference list. The notebook's current text does not cite the conditions for a chi-square goodness-of-fit test (section 1.3.5.15): no fit is tested, and the Pearson discrepancy is reported descriptively.

**Status:** web source; cite with the access date.

**NIST, Kruskal-Wallis method page** ([official method page](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/kruskwal.htm)) and **SciPy, `scipy.stats.kruskal`** ([official documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)), both accessed 9 October 2026.

**Use:** The independence and equal-distribution assumptions of the Kruskal-Wallis test, and the tie correction with the chi-square reference p-value, for the tests kept in 7.1 and 5.4. Since the 12 October report version the notebook's text and reference list no longer cite these pages; the tests are computed in its code cells. Cite them with the access date if the Kruskal-Wallis results are reported in the thesis. They do not establish that the observations meet the test's assumptions, and they are not used for the activity pattern across days (see the 13 October note at the end of this register).

**Status:** web sources; not cited in the current notebook text.

### Human-AI interaction and appropriate reliance

**Schemmer, M., Hemmer, P., Nitsche, M., Kühl, N., & Vössing, M. (2023).** *Appropriate Reliance on AI Advice*. PDF stored as `open-access/01-appropriate-reliance-ai-advice.pdf`. https://doi.org/10.1145/3581641.3584066

**Use:** Relevant if the final artifact provides advice that a buyer can accept, modify or reject.

**Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019).** *Guidelines for Human-AI Interaction*. PDF stored as `open-access/03-guidelines-human-ai-interaction.pdf`. https://doi.org/10.1145/3290605.3300233

**Use:** Design principles for feedback, control, correction and failures in an AI-supported interface. Cited in the AI function comparison (row 10).

**Bansal, G., Nushi, B., Kamar, E., Horvitz, E., & Weld, D. S. (2021).** *Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance*. PDF stored as `open-access/02-human-ai-complementary-team-performance.pdf`. https://doi.org/10.1145/3411764.3445717

**Use:** Relevant if evaluation examines the performance of a buyer–AI team. It is **not** used as the generic definition of purchasing quality; ISO 9000 provides that broader quality anchor.

*13 October:* Schemmer et al. and Bansal et al. are not cited in a project document yet. They stay here because the provisional focal case is a reading, matching and flagging aid whose output Arno accepts, corrects or asks to clarify (selection notebook, section 6), and because quality is predeclared to be measured on the final human-approved outcome (methodology, section 6.1).

---

### Document retrieval, extraction and matching

Candidate-specific sources for rows of the [AI function comparison](../docs/methodology/AI_Function_Comparison_2026-10-02.md). Same three statuses as above. *Moved up from "possible use" on 7 October:* Tater et al. is the main precedent for the provisional focal case, order and confirmation checking (called purchase-price control until 7 October), and Šimsa et al. (DocILE) for document-field extraction; see the reading order above.

**Lombardi et al. (2025).** *Title block detection and information extraction for enhanced building drawings search*. EC³ / CIB W78 conference, 2025. https://doi.org/10.35490/EC3.2025.344 (manuscript: https://arxiv.org/abs/2504.08645)

**Use if needed:** Closest applied work for finding drawings: AI extraction of title-block metadata supports searching and filtering drawings. Building drawings rather than component drawings; does not show whether a drawing set is complete or correctly revised.

**Status:** citation verified 2 October 2026 (EC³ publication record; complete the author list from it); abstract and full text not yet reviewed.

**Tater et al. (2022).** *AI driven accounts payable transformation*. *Proceedings of the AAAI Conference on Artificial Intelligence, 36*(11), 12405–12413. https://doi.org/10.1609/aaai.v36i11.21506

**Use if needed:** Precedent for comparing documents and flagging discrepancies: invoice lines are matched to PO lines using text similarity, price and quantity checks, with human review. Accounts-payable setting, so price checks before ordering or against supplier confirmations need adaptation and testing. Also listed in the selection notebook's reference list (Appendix D).

**Status:** citation verified 2 October 2026 (AAAI proceedings record; complete the author list from it); abstract and full text not yet reviewed.

**Šimsa et al. (2023).** *DocILE benchmark for document information localization and extraction*. In *Document Analysis and Recognition – ICDAR 2023*, 147–166. https://arxiv.org/abs/2302.05658

**Use if needed:** Benchmark for locating fields in business documents and grouping them into line items across layouts; relevant to extracting item descriptions, quantities and prices before checking them. Shows feasibility of extraction, not usefulness here, and does not resolve the intended meaning of an ambiguous quantity.

**Status:** citation details still to verify; abstract and full text not yet reviewed.

## Possible use when we know more

### Subjective mental-workload measurement

**Hart, S. G., & Staveland, L. E. (1988).** *Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research*. In P. A. Hancock & N. Meshkati (Eds.), *Human Mental Workload* (pp. 139–183). Elsevier. https://doi.org/10.1016/S0166-4115(08)62386-9

**Hart, S. G. (2006).** *NASA-Task Load Index (NASA-TLX); 20 years later*. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 50*(9), 904–908. https://doi.org/10.1177/154193120605000909

**Use:** Historical candidate instrument, retained as background. The current Plan of Work does not include a NASA-TLX or other mental-workload assessment.

### Agreement statistic for the optional recoding

**Cohen, J. (1960).** *A coefficient of agreement for nominal scales*. *Educational and Psychological Measurement, 20*(1), 37–46. https://doi.org/10.1177/001316446002000104

**Possible use only:** Cohen's kappa would be relevant if the optional recoding exercise is undertaken and its comparison is justified. It is not required for the current targeted review and no agreement statistic is reported as completed. Such a check would not establish independent reliability of the original observation. The [methodology](../docs/methodology/Phase_1_Current_Methodology.md#7-current-remaining-actions-reviewed-9-october-2026) still lists the retained 45-record recoding sheet and κ as optional, not completion gates; no project document cites this source by name. Moved here from *High chance to use* on 13 October.

**Status:** citation details still to verify; abstract and full text not yet reviewed.

### Duration distributions

**Brown, L., Gans, N., Mandelbaum, A., Sakov, A., Shen, H., Zeltyn, S., & Zhao, L. (2005).** *Statistical analysis of a telephone call center: A queueing-science perspective*. *Journal of the American Statistical Association, 100*(469), 36–50. https://doi.org/10.1198/016214504000001808

**Use if needed:** An example where service times were close to lognormal while a formal test rejected exact lognormality. It would support considering the lognormal for task durations if the thesis discusses the duration fits of section 7.2, not that Arno's durations follow it. The 9 October version was the last to cite it; the 12 October rebuild dropped it, and the "step 11 of Appendix A" it supported no longer exists (Appendix A now holds the tie-handling and leave-one-day-out refits). Moved here from *High chance to use* on 13 October.

**Status:** citation details still to verify; check the exact statement used against the paper before citing it in the thesis.

### Purchasing automation

**Flechsig, C., Anslinger, F., & Lasch, R. (2022).** *Robotic Process Automation in purchasing and supply management*. https://doi.org/10.1016/j.pursup.2021.100718

**Use:** Direct procurement-automation evidence for evaluating which administrative purchasing activities are suitable for automation.

**Syed, R., Suriadi, S., Adams, M., Bandara, W., Leemans, S. J. J., Ouyang, C., ter Hofstede, A. H. M., van de Weerd, I., Wynn, M. T., & Reijers, H. A. (2020).** *Robotic Process Automation: Contemporary themes and challenges*. *Computers in Industry, 115*, 103162. (Author list corrected on 16 October 2026 against Crossref and the QUT author manuscript.) https://doi.org/10.1016/j.compind.2019.103162

**Use:** Automation limitations, implementation risks and governance.

*13 October:* no project document cites these two sources. They would support the gate-6 comparison of AI with simpler automation and the quick-win recommendation for PO supplier communication (selection notebook, section 2) if the thesis makes that argument. Moved here from *High chance to use*.

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

**DeLone, W. H., & McLean, E. R. (2003).** *The DeLone and McLean Model of Information Systems Success: A Ten-Year Update*. https://doi.org/10.1080/07421222.2003.11045748

**Use if needed:** Broader implementation / information-system success evaluation.

---

## Historical background, not confirmed for the current study

### Mental workload

**Young, M. S., Brookhuis, K. A., Wickens, C. D., & Hancock, P. A. (2015).** *State of science: Mental workload in ergonomics*. *Ergonomics, 58*(1), 1–17. https://doi.org/10.1080/00140139.2014.956151

**Use:** Historical background on mental workload. The current project does not assess this construct. The active workload framework follows the amount/difficulty distinction in `docs/methodology/Workload_Definition.md`.

**Longo, L., Wickens, C. D., Hancock, G., & Hancock, P. A. (2022).** *Human mental workload: A survey and a novel inclusive definition*. *Frontiers in Psychology, 13*, 883321. https://doi.org/10.3389/fpsyg.2022.883321

**Use:** Background review retained for traceability; mental-workload measurement is not part of the current study. No project document cites it. Moved here from *High chance to use* on 13 October.

<a id="coding-the-observation-notes"></a>
### Note-based coding and saturation, archived 12 October

The note-based coding of 30 September used an inductive coding rationale. That layer is [archived](../docs/archive/kinds_of_work/README.md) since 12 October; the analysis uses the original observation codes and the agreed stages, so the sources below are historical leads. The source statuses distinguish citation verification, abstract review and full-text review. Moved here from *High chance to use* on 13 October.

**Hsieh, H.-F., & Shannon, S. E. (2005).** *Three approaches to qualitative content analysis*. *Qualitative Health Research, 15*(9), 1277–1288. https://doi.org/10.1177/1049732305276687

**Use:** Basis for the archived note-based coding of 30 September: in conventional (inductive) content analysis, the categories come from the data instead of a scheme fixed beforehand. Supports that method; it does not validate the 31 labels or their coding, and the current analysis does not use them. The [measurement-method justification](../docs/measurement/Measurement_Method_Justification.md) still cites it (section 2.1 and the thesis-ready method statement) for that archived layer. The justification's thesis-ready statement must either keep that clause (then the source stays cited for the archived layer) or drop it; settle this before the thesis method section is written.

**Status:** citation details still to verify; abstract and full text not yet reviewed.

**Guest, G., Namey, E., & Chen, M. (2020).** *A simple method to assess and report thematic saturation in qualitative research*. *PLOS ONE, 15*(5), e0232076. https://doi.org/10.1371/journal.pone.0232076

**Use:** Informed the retrospective saturation assessment of the 9 October notebook version, which counted new note-based labels per later session. Since the rebuild of 12 October on the original codes the [analysis notebook](../Arno_Analysis_2026_10_02.ipynb) uses a leave-one-day-out check (section 4.4) instead, so this source is a historical lead unless a saturation argument returns to the thesis. The assessment used a base set, a run of later sessions and the share of new information in that run. The authors tested bases of 4–6 interviews with runs of 2–3 and call 5% new information an optional benchmark; applying base and run sizes to observation days is this project's adaptation, used retrospectively, not a validated stopping rule. Open access; the full text still has to be read before it is cited in the thesis. No project document cites it since 12 October.

---

## Copyright and access note

Only public, open-access or author-posted PDFs are stored in this repository. Publisher-restricted articles and standards are represented by DOI or official links and are not copied into the repository.


## 13 October: day-pattern method references

The 9 October table of Kruskal-Wallis references that stood here is replaced by this note. On 13 October Zhongxin chose Kendall's W, with the Friedman test on the same ranks, for the activity pattern across the observation days, and asked for the Jensen-Shannon divergence between the days' shares; the Kruskal-Wallis test named on 8 October is kept only for episode lengths by day (section 7.1) and CHECK minutes per line (5.4). The sources for the new tests are Kendall & Babington Smith (1939), Friedman (1937) and Lin (1991), under Confirmed use; the Kruskal-Wallis method page and the SciPy documentation (accessed 9 October) are listed under *Statistics used in the analysis notebook* and are no longer cited in the notebook. The reasons for not applying Kruskal-Wallis or a chi-square test of homogeneity to the activity-by-day table (the activity minutes of a day are parts of the same day's total; minutes are not independent counts) are the notebook's methodological assessment in section 4.3, not a claim that these sources studied Hytech-Pommec. Whether the Kruskal-Wallis results are reported as supplementary is open until Zhongxin reads the update; the 15 October meeting is cancelled.
