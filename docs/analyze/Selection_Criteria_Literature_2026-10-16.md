# Selection criteria from the literature: synthesis for the focal-case choice

**Prepared:** 16 October 2026, for Yijie's reply to Zhongxin's request of 14 October (summarise the sources she found; find an existing, fairly complete criteria set, or compile the criteria that recur across several sets). **Status:** literature input for the criteria review with Zhongxin. The proposed set of section 3 was adopted by Yijie on 16 October and is used in sections 2 and 3 of the [selection notebook](../../Focal_Case_Selection_2026-10-07.ipynb): A0 became gate 7 (value floor), B3 gate 8 (stable task), B9 stays in gates 1 and 4, and the other criteria are scored; the weights are Yijie's swings of 7 October carried over.

**What this note does.** It summarises each source (section 1), counts which criteria recur across the criteria sets that were actually read (section 2), proposes a criteria set in two families, value and feasibility (section 3), maps the project's seven current criteria onto it (section 4), and lists the limits of transferring RPA criteria to an AI reading-and-matching aid for one buyer (section 5).

**How it was read.** Every criterion below comes from a source text that was opened and read (the copies are described in Appendix B); for Agaton & Swedberg the extracted notes were checked against the text a second time. When only an abstract was available, the source is marked with an asterisk and does not enter the counts. Page numbers are given only where the printed page was seen; otherwise the section or table is named. The one exception is Parasuraman et al. (2000) in section 1.1, which was not re-read for this note and does not enter the counts.

---

## 1. The sources

### 1.1 The supervisor's sources

The four sources below follow her message of 14 October and the IEEE Xplore link (document 844354) she sent afterwards.

**Costa, Mamede & Mira da Silva (2023), *A method for selecting processes for automation with AHP and TOPSIS*, Heliyon (code C23).** Full text read (Europe PMC open-access copy). A design-science study that turns seven process characteristics from the authors' own RPA literature review into nine criteria (rule-based, maturity, data structure, digital data, human input, complexity, multiple systems, frequency, duration), each with a five-point scale (Table 8). AHP pairwise comparisons give the weights and TOPSIS ranks the processes; it was demonstrated on 18 processes in one education unit and checked in one interview with two managers. What transfers: a published, citable criteria list with operational scales, and a reproducible weighting and ranking procedure into which extra criteria can be added. What does not: it is RPA-only, has no financial, customer or strategic-impact criterion and no build or evaluation criterion, and a recomputation for this note found that the published weights sum to 106.21% and that the published ranking cannot be reproduced from the printed tables, so cite the criteria and the procedure, not the numbers.

**Jongeling, Lu, Beerepoot, van de Weerd & Reijers (2023), *Getting your RPA priorities straight with process mining: The PLOST framework*, ECIS 2023, with Jongeling's 2022 master's thesis (code PL).** Full text of both read. The paper merges 26 criteria from four earlier selection methods (Table 1, p. 4) into an eight-step funnel: stakeholders first weight three business values (time savings; quality and accuracy; availability and flexibility) and set a risk level; six qualitative must-pass gates follow (digital and structured input, easy data access, few variations, repetitive, clear rules, mature); process-mining metrics then rank processes and tasks (cycle time, case and activity frequency, standardisation, length, automation rate, human-error proneness, duration, irregular labour). It was evaluated in one ProRail case and two think-aloud sessions. What transfers: a published precedent for exactly the project's design of gates before scores, and a citable way to weight criteria with stakeholders (cumulative voting). What does not: the gates assume rule-based work on structured digital input, and the metrics need an event log, which the project replaces with observation records.

**Parasuraman, Sheridan & Wickens (2000), *A model for types and levels of human interaction with automation*, IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans 30(3), 286-297 (code PA).** Not re-read for this note; the content below is as summarised in the project's literature register and the paper's abstract. It is not a process-selection criteria set. It models four functions that automation can take over (information acquisition, information analysis, decision and action selection, action implementation), each at levels from manual to fully autonomous, and gives criteria for choosing the level: primary, the consequences for human performance (mental workload, situation awareness, complacency, skill degradation); secondary, the reliability of the automation and the costs of the consequences of decisions and actions. It is already in the project's literature register (citation verified 2 October 2026, full text not yet reviewed) and underlies the AI function comparison. What transfers: it supports the feasibility side on how far to automate, where the aid supports information acquisition and analysis while the buyer keeps decision and action, which is the basis of the buyer-acceptance and human-review gate. What does not: it does not select processes, so it is not counted in the frequency matrix.

**Gajula (2024), *How to identify automation opportunities in your workflow*, Futran Solutions blog, 9 December 2024 (code FU).** Full text read. A vendor blog, not research: it names repetitive and time-consuming tasks, high error rates, tasks with predictable patterns and frequent bottlenecks as places to look, and then prioritises by return on investment (complexity, cost and impact), effect on employee roles, and quick wins against long-term projects. What transfers: it confirms, from practice, the value side (time, errors, bottlenecks) and the idea of a pilot. It carries no academic weight and should only be cited, if at all, as an example of practitioner guidance.

### 1.2 Sources behind the supervisor's sources

**Costa et al. (2022), *Robotic process automation (RPA) adoption: A systematic literature review*, Engineering Management in Production and Services (code C22).** Full text read. A Kitchenham-style review of 47 papers; Table 5 lists eight RPA suitability characteristics with the papers supporting each: rule-based (7 papers), mature, structured data and high volume (5 each), digital data and routine (4 each), few exceptions and multiple systems (2 each). It is the evidence base of C23 and is itself a small frequency count of the kind the supervisor asked for. It contains no financial, customer or strategic-impact criterion, and nothing on AI fit or evaluation.

**Costa (2022), *A method to select processes for automation*, master's thesis, Instituto Superior Técnico (not counted separately).** Partly read (section 2.2, chapter 5 tables, conclusions). Same method, criteria and numbers as C23; the conclusions (p. 41) say the weights were "attributed according to case studies and research articles". That this amounts to the author's own judgement is this note's inference, not a statement in the thesis. Cite the journal article instead.

**Agaton & Swedberg (2018), *Evaluating and developing methods to assess business process suitability for robotic process automation*, master's thesis, Chalmers and University of Gothenburg (code AS).** Full text read in part (sections 3.2-3.3 and 4.2-4.3). The authors collected 118 criteria from 23 sources, mostly from industry (only seven academic articles), consolidated them to 49 and counted how often each recurs (Table 4.4, p. 29: rules based 20 of 23 sources, multiple systems 11, error prone 10, high transaction volume 10, repetitive 10, few exceptions 7, stable 7, limited human intervention 6). Their own framework (Figure 4.5, p. 32) has five steps, in order: risk level, business value (a process must show value in at least one of time savings, quality and accuracy, employee satisfaction, availability and flexibility), an optional process-model step (BPMN-R), mandatory criteria, optional criteria. What transfers: the clearest early example of compiling recurring criteria, and a warning that mixing mandatory, optional and value criteria in one list without a rule for using them can select unsuitable processes (section 4.2.3, pp. 29-30).

**Haan (2021), *How can process mining be used to identify robotic process automation opportunities?*, bachelor's thesis, University of Twente (code HA).** Full text read in part (sections 4-5). Splits criteria into technical suitability (rule based, low variations, structured readable input, mature), judged with people, and added value (human-error proneness, frequency, time reduction, FTEs saved, cost reduction, irregular labour), measured from event logs with explicit formulas (pp. 8-14). What transfers: the cleanest cost-versus-benefit split in this literature and simple indicators for workload and error that could be computed from the project's observation records. It is a single-organisation bachelor's thesis.

**Shafik Salah Elsayed & Kassem (2022), *Assessing process suitability for robotic process automation: A process mining approach*, Wirtschaftsinformatik 2022 Proceedings, student track (code EK).** Full text read. A review of 42 articles gave 36 criteria and nine expert interviews gave 20, all of which also appear in the review; the authors kept the 11 that are measurable with process mining (low complexity, high standardisation, rule-based, structured digital data, repetitive or routine, high volume or frequency, low automation rate, low exception handling, number of FTEs, execution time, proneness to human error), each scored 0 or 1 and weighted by the organisation. Structured digital input carries no weight because without it RPA is "not possible at all", which makes it a knock-out gate. The demonstration used a purchase-to-pay event log. The authors note that "cognitive RPA" may need different criteria (section 3.2.1).

**Choi, R'bigui & Cho (2021), *Candidate digital tasks selection methodology for automation with robotic process automation*, Sustainability 13(16), 8980 (code CH).** Full text read (MDPI page). Mines user-interface logs recorded over eight days and selects candidate routines with three criteria: frequency, periodicity (performed at the same time, for example every Friday) and duration. It is narrow but shows that frequency and duration can be measured from recorded user actions, which is close to the project's observation method.

### 1.3 Further criteria sets found (RPA and process automation)

**Wanner et al. (2019), ICIS (code WA).** Full text read. Six event-log indicators of automation potential (execution frequency, execution time, standardisation, stability as low exception probability, failure rate, automation rate; Table 2, p. 9) and a cost comparison of human and robot labour (Table 3). Transfers as a quantified definition of workload volume; note that it treats a high failure rate as a reason to automate.

**Wewerka & Reichert (2020), arXiv:2012.11951, an unrefereed preprint (code WR).** Full text read. A review of 63 publications; the process-selection criteria (section 3.2) are repetitiveness as high volume, rule-based and standardised work in a stable environment with limited exception handling, high manual effort and error proneness, low complexity, long duration, digital and structured inputs, multiple applications, and high business impact. Its Table 3 contrasts RPA with intelligent automation (standardisation high vs low, data structured vs unstructured, decisions rule-based vs knowledge-based, outcome deterministic vs probabilistic), which is the key argument for section 5. A peer-reviewed successor appeared in Enterprise Information Systems 17(2), 1986862 (https://doi.org/10.1080/17517575.2021.1986862); it was not read.

**Syed et al. (2020), Computers in Industry 115, 103162 (code SY).** Full text read (author's version). A review of 125 papers that separates organisational readiness (business drivers, existing technology, RPA maturity) from 13 process and task characteristics: highly rule-based, high volume, mature, easy to achieve and show impact, digitised structured input, highly manual, transactional, standardised, low exception handling, highly repetitive, less complex, well-documented, many systems (section 3.3). It also records contradictions in the literature: medium volumes and business-critical tasks can also suit, and RPA is sometimes used to achieve standardisation rather than requiring it.

**Lacity & Willcocks (2016), MIT Sloan Management Review (code LW).** Full text read (LSE accepted version). From case studies: business operations select tasks that "use structured data, have explicit and well-documented rules, churn out high transaction volumes, and are stable", and RPA is set apart from cognitive automation, which handles unstructured data. Academic authors in a managerial outlet; useful as the classic statement of the RPA minimum.

**Wellmann, Stierle, Dunzer & Matzner (2020), BPM 2020 RPA Forum (code WE).** Full text read (arXiv accepted manuscript). Thirteen criteria in five perspectives (task: standardisation, maturity, determinism, failure rate; time: frequency, duration, urgency; data: structuredness; system: interfaces, stability, number of systems; human: resources, proneness to human error; Table 2). It deliberately leaves out value, says data must be "at least semi-structured", and, unlike Wanner et al., treats a low failure rate as favourable.

**Herm et al. (2023), Information Systems and e-Business Management 21(1), 1-35 (code HE).** Full text read. An implementation framework from 35 project reports, expert interviews and workshops; in the process-selection stage experts name execution frequency, standardisation, low complexity, few exceptions, financial attractiveness, process stability, error proneness and new services to customers (pp. 17, 24), and digital inputs are mandatory. A separate earlier stage screens whether a simpler technology (for example an Excel macro) would do, which supports the project's gate 6.

**Farinha, Pereira & Almeida (2024), Journal of Information Technology 39(1), 149-166 (code FA).** Full text read. The most complete single list found: a review gave 18 criteria (Table 3, p. 154), a fuzzy Delphi with 34 RPA practitioners extended and ranked them to 32 (Tables 4, 7, 8), grouped in five categories (data, environment, human resources, governance, structure; Table 10, p. 161), and tested on 18 processes in six organisations. The top-ranked criteria are feasibility, accurate process description and input and output data; it is also the only RPA set with a "test data" criterion. Many of the top items came from the Delphi rather than the review.

**Bédard et al. (2024), Journal of Software: Evolution and Process 36(11), e2709 (code BE).** Full text read. Defines suitability as two sub-goals that must both be satisfied: feasibility (nine criteria: application access, unambiguous documented rules, stable rules, enforced rules, low cognitive requirements, stable context, structured data, digital data, few exceptions; Table 2) and relevance (executions per day and proneness to human error). This is the clearest published statement of the "worth doing and doable" logic of section 3.

**Meyer, Hinrichsen & Padoano (2024), AHFE Open Access vol. 158, 10-20 (code ME).** Full text read. A review of 15 method papers (including C23, FA, HE, WA, WE) kept the 29 criteria mentioned at least four times, in six clusters (business potential, human, data, process, documentation, application; Table 2), and 16 RPA experts recruited through consultancies and LinkedIn groups weighted them with AHP: data 26.3%, business potential 25.8%, human 17.3%, documentation 16.2%, process 14.4% (the text gives no weight for the application cluster). These five weights already sum to 100.0%, so the application cluster appears to be outside the weighted model, and in the AHP the business-potential cluster consists only of the Volume criterion. It notes that the criteria are not independent of each other.

**Flechsig, Anslinger & Lasch (2022), Journal of Purchasing and Supply Management 28(1), 100718 (code FL).** Full text read (accepted manuscript on Zenodo; page numbers there differ from the journal). A multiple case study of 19 private and public organisations (24 interviews) on RPA in purchasing. Suitable purchasing tasks are repetitive, rule-based, standardised, manual and error-prone, with structured digital input, several systems, good documentation, high volume and low complexity (section 4.1); organisations prioritise on a value-by-feasibility matrix (Fig. 5, section 4.3.1). Appendix F lists purchasing uses close to the focal task, such as comparing the delivery note with the purchase order and matching request, order and invoice. It is the only RPA set from purchasing.

**Erdogan & Dogan (2024), *Process selection for RPA projects with MDCM: The case of Izmir Bakircay University*, Springer CCIS, pp. 15-28 (code ER).** Not accessible: only the title, authors, pages and ISBNs were seen; the Springer page and the university repository were closed. A search-engine snippet said it combines AHP and TOPSIS, but the page behind that claim could not be opened, so nothing about its method or criteria is used here. It may be a second application of the Costa et al. approach; the TU/e library is the route to the full text.

### 1.4 AI-specific sets

**Spreitzenbarth, Bode & Stuckenschmidt (2024), Journal of Purchasing and Supply Management 30(1), 100896 (code SP).** Full text read. A review of 46 works on AI and machine learning in purchasing, clustered into 11 use-case clusters, with 20 expert interviews rating each cluster on business value (financial, customer, strategic) and ease of implementation (input data, know-how, change effort), averaged with equal weights (Table 2, p. 9). The "ordering" cluster had the highest ease of implementation (3.7 of 5) and a business value of 3.0, among the lowest; that is an expert rating of a cluster, not of the focal task. The sub-dimensions were adapted from a consultancy report.

**Brakemeier et al. (no year printed), *Applying AI: How to find and prioritize AI use cases*, appliedAI Initiative (code AA).** Full text read. A practitioner whitepaper: use cases are assessed on value (business value, strategic alignment) and ease of implementation (data, algorithm, processes and systems, required expertise, duration), plus flags for regulation, risk and transparency, cybersecurity and resilience, and the assessed cases are then placed in a prioritisation matrix (assessment on pp. 14-16). It adds two points relevant here: define the minimum accuracy the use case needs, and check whether the algorithm is already running elsewhere.

**Engel (2022), *Cognitive automation: Assessing business process automation potentials in organizations driven by artificial intelligence*, doctoral dissertation, University of St.Gallen (code EN).** Full text available; the assessment model (pp. 124-127) and method (pp. 220-222) were read. It argues that criteria made for rule-based automation do not cover cognitive automation, which is probabilistic and learns from data. Its method sets an automation goal (time back to the business, FTEs, quality, risk), applies a machine-learning suitability gate taken from Sturm, Fecho & Buxmann (2021) (indefinability of rules, self containment, generalisation, measurable goal, continuous adaptation), assesses data, cognition, relationship and transparency requirements, and places use cases on an impact-effort matrix (method Step 8, p. 226 by the table of contents, outside the pages read). Sturm et al. were read only through Engel's summary.

**Bodendorf (2025), Electronic Markets 35, article 22 (code BO\*).** Abstract only. Assesses AI use cases on value (strategic value, financial value) and feasibility (data complexity, model complexity, required expertise, integration complexity, risk classification), tested in eight case studies. The assignment of the sub-dimensions to value and feasibility is inferred from the order in which the abstract lists them; the abstract does not state the split. Shown in the table but not counted.

**Single-criterion sources, not counted.** Brynjolfsson, Mitchell & Rock (2018), AEA Papers and Proceedings 108, 43-47 (full text read): one stated condition for suitability for machine learning is that the set of actions and the corresponding set of outputs "can be measured sufficiently well that a machine can learn the mapping" (pp. 44-45); their 23-statement rubric is in supplementary material that was not read. Eloundou, Manning, Mishkin & Rock (2023), arXiv:2303.10130 (full text read): a task counts as exposed when a language-model tool can cut the time it takes by at least half at equivalent quality (section 3.3). Both support "AI must save time without lowering quality" but are labour-market measures, not selection sets.

### 1.5 Sources that could not be read

Erdogan & Dogan (2024) (metadata only); Fung (2014) on IT process automation criteria (the downloaded pages were a different article); Riedl & Beetz (2019), cited by WR and FA as a multi-criteria evaluation model (download returned an HTML page); Sturm et al. (2021) directly and Hofmann et al. (2020) on AI use cases (bot checks); Godbole (2022) and Brynjolfsson & Mitchell (2017) (bot checks or wrong page). None of them is used.

### Source register

| Code | Source | Kind | Access | Counted |
|---|---|---|---|---|
| C23 | Costa et al. 2023, Heliyon | Academic, design science | Full text | Yes |
| C22 | Costa et al. 2022, EMJ | Academic, literature review | Full text | Yes |
| PL | Jongeling et al. 2023, ECIS, with Jongeling 2022 thesis | Academic, design science | Full text | Yes |
| AS | Agaton & Swedberg 2018, Chalmers thesis | Academic thesis, mostly industry sources | Full text, in part | Yes |
| HA | Haan 2021, Twente thesis | Academic thesis | Full text, in part | Yes |
| EK | Shafik Salah Elsayed & Kassem 2022, WI | Academic, review and interviews | Full text | Yes |
| CH | Choi et al. 2021, Sustainability | Academic | Full text | Yes |
| FU | Gajula 2024, Futran blog | Practitioner (vendor) | Full text | Yes, marked practitioner |
| PA | Parasuraman et al. 2000, IEEE Trans. SMC Part A | Academic, model of human interaction with automation (not a selection set) | Not re-read for this note; content as summarised from the literature register and the paper's abstract | No (does not select processes) |
| WA | Wanner et al. 2019, ICIS | Academic | Full text | Yes |
| WR | Wewerka & Reichert 2020, arXiv | Academic, literature review; unrefereed arXiv preprint (peer-reviewed successor in Enterprise Information Systems not read) | Full text | Yes |
| SY | Syed et al. 2020, Computers in Industry | Academic, literature review | Full text (author version) | Yes |
| LW | Lacity & Willcocks 2016, MIT SMR | Academic authors, managerial outlet | Full text (accepted version) | Yes |
| WE | Wellmann et al. 2020, BPM RPA Forum | Academic | Full text (accepted manuscript) | Yes |
| HE | Herm et al. 2023, ISeB | Academic, reports and interviews | Full text | Yes |
| FA | Farinha et al. 2024, JIT | Academic, review and practitioner Delphi | Full text | Yes |
| BE | Bédard et al. 2024, JSEP | Academic | Full text | Yes |
| ME | Meyer et al. 2024, AHFE | Academic, review and practitioner AHP | Full text | Yes |
| FL | Flechsig et al. 2022, JPSM | Academic, case study in purchasing | Full text (accepted manuscript) | Yes |
| ER | Erdogan & Dogan 2024, CCIS | Academic | Metadata only | No |
| SP | Spreitzenbarth et al. 2024, JPSM | Academic, review and interviews, AI in purchasing | Full text | Yes (AI) |
| AA | Brakemeier et al., appliedAI | Practitioner (non-profit initiative) | Full text | Yes (AI), marked practitioner |
| EN | Engel 2022, St.Gallen dissertation | Academic, cognitive automation | Full text, in part | Yes (AI) |
| BO\* | Bodendorf 2025, Electronic Markets | Academic | Abstract only | Shown, not counted |

---

## 2. How often each criterion recurs

**Counting rules.** A cell is marked when the source uses the criterion as a selection or prioritisation criterion, under any wording; synonyms were merged and the wording each source uses is in the second table. Each source is counted once per row even if it has several matching items. Literature reviews (C22, WR, SY, FA, ME) count as one set each, although each summarises many papers. The counts are split into 18 RPA or process-automation sets and 3 AI sets; BO\* (abstract only) is shown but not counted, and ER and PA (which does not select processes) are left out. Value rows come first (V), feasibility rows second (F).

**Read the counts with care.** The sets are not independent: C23 is built on C22; PL merges AS, HA, CH and EK; ME reviews C23, FA, HE, WA and WE; WE starts from WA; FA cites SY, WR and WE. A high count therefore shows a stable consensus in a self-citing RPA literature, not 18 independent confirmations.

| ID | Criterion (merged) | C23 | C22 | PL | AS | HA | EK | CH | FU | WA | WR | SY | LW | WE | HE | FA | BE | ME | FL | SP | AA | EN | BO\* | RPA sets (of 18) | AI sets (of 3) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | Volume / execution frequency | x | x | x | x | x | x | x |  | x | x | x | x | x | x | x | x | x | x |  |  |  |  | 17 | 0 |
| V2 | Handling time / duration | x |  | x | x | x | x | x | x | x | x |  |  | x |  | x |  | x |  |  | x | x |  | 12 | 2 |
| V3 | Manual effort / labour intensity |  |  |  |  | x | x |  |  |  | x | x |  | x |  | x | x | x | x |  |  | x |  | 9 | 1 |
| V4 | Error-proneness / quality and accuracy gain | x |  | x | x | x | x |  | x | x | x | x |  | x | x | x | x | x | x |  | x | x |  | 15 | 2 |
| V5 | Financial value: cost, savings, ROI |  |  |  |  | x |  |  | x | x |  | x |  |  | x | x |  |  | x | x | x |  | x | 7 | 2 (+1\*) |
| V6 | Wider business impact: customer, strategic, criticality |  |  | x | x |  |  |  |  |  | x |  |  |  | x | x |  |  | x | x | x | x | x | 6 | 3 (+1\*) |
| V7 | Time-criticality, peaks, availability |  |  | x | x | x |  |  | x |  |  |  |  | x |  |  |  |  |  |  |  |  |  | 5 | 0 |
| V8 | Not yet automated (low automation rate) |  |  | x |  |  | x |  |  | x |  |  |  |  |  |  |  | x |  |  |  |  |  | 4 | 0 |
| V9 | Employee-related value |  |  |  | x |  |  |  |  |  |  |  |  |  | x |  |  |  | x |  |  |  |  | 3 | 0 |
| F1 | Repetitive / routine (same way, recurring) |  | x | x | x |  | x | x | x |  |  | x |  |  |  | x |  | x | x |  |  |  |  | 10 | 0 |
| F2 | Standardised execution / few variants |  |  | x | x | x | x |  | x | x | x | x |  | x | x | x |  | x | x |  |  |  |  | 13 | 0 |
| F3 | Few exceptions |  | x | x | x |  | x |  |  | x | x | x |  | x | x | x | x | x | x |  |  |  |  | 13 | 0 |
| F4 | Stable / mature process (few changes) | x | x | x | x | x |  |  |  |  |  | x | x | x | x | x | x | x |  |  |  |  |  | 12 | 0 |
| F5 | Low process complexity | x |  | x | x |  | x |  |  |  | x | x |  |  | x | x |  | x | x |  |  |  |  | 10 | 0 |
| F6 | Decision logic expressible as rules / low judgement | x | x | x | x | x | x |  |  |  | x | x | x | x |  | x | x | x | x |  |  |  |  | 14 | 0 |
| F7 | Structured input | x | x | x | x | x | x |  |  |  | x | x | x | x |  | x | x | x | x |  |  |  |  | 14 | 0 |
| F8 | Digital input | x | x | x | x | x | x |  |  |  | x | x |  | x | x | x | x | x | x |  |  |  |  | 14 | 0 |
| F9 | Data access, availability and quality |  |  | x | x |  |  |  |  |  |  | x |  |  |  |  |  |  |  | x | x | x | x | 3 | 3 (+1\*) |
| F10 | Checkable outcome: test data, measurable goal |  |  |  |  |  |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x |  | 1 | 2 |
| F11 | Multiple systems / application access | x | x |  | x |  |  |  |  |  | x | x |  | x |  | x | x | x | x |  |  |  |  | 10 | 0 |
| F12 | Stable IT environment / applications |  |  |  | x |  |  |  |  |  | x |  |  | x |  | x | x | x | x |  |  |  |  | 7 | 0 |
| F13 | Documented, well-understood process |  |  |  |  |  |  |  |  |  |  | x | x |  |  | x | x | x | x |  |  |  |  | 6 | 0 |
| F14 | Implementation effort / technical feasibility / know-how |  |  |  |  | x |  |  | x | x |  | x |  |  |  | x |  |  | x | x | x | x | x | 6 | 3 (+1\*) |
| F15 | AI-task fit: learning needed, beyond simpler tools |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x | 0 | 1 (+1\*) |
| F16 | Maintenance / continuous adaptation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | x | x |  | 0 | 2 |
| F17 | Risk, security, transparency |  |  |  |  |  |  |  |  |  |  |  |  |  |  | x |  |  |  |  | x | x | x | 1 | 2 (+1\*) |
| F18 | Acceptance / change effort |  |  |  |  |  |  |  | x |  |  |  |  |  |  |  |  |  |  | x |  |  |  | 1 | 1 |

**Wording by source.**

| ID | Wording by source |
|---|---|
| V1 | **C23** Frequency · **C22** High volume · **PL** Case frequency; Activity frequency · **AS** High transaction volume (Time savings) · **HA** High frequency · **EK** High volume/frequency · **CH** Frequency · **WA** Execution frequency · **WR** Repetitiveness (= high volume) · **SY** High volume · **LW** High transaction volumes · **WE** Frequency · **HE** Execution frequency and volume · **FA** Number of transactions; Volume of items per transaction · **BE** Number of times per day (relevance) · **ME** Execution frequency; Volume · **FL** High-volume, many transactions |
| V2 | **C23** Duration · **PL** Cycle time; Duration · **AS** Time savings ('takes a lot of time to perform') · **HA** Time sensitive (time reduction) · **EK** High execution time · **CH** Duration · **FU** Time-consuming tasks · **WA** Execution time · **WR** Duration (high expenditure of time) · **WE** Duration · **FA** Time-consuming · **ME** Execution time; Volume (frequency x time) · **AA** Speed-up (in business value) · **EN** Time-back-to-the-business (KPI) |
| V3 | **HA** Human productivity (FTEs saved) · **EK** High number of FTEs · **WR** High manual efforts · **SY** Highly manual · **WE** Resources (users on the task) · **FA** Human effort; Number of users · **BE** Manual operations per transaction (relevance) · **ME** Human labour intensity; No. of persons involved · **FL** Manually processed; FTE savings, effort reduction (value) · **EN** FTEs (KPI) |
| V4 | **C23** Human input (error-prone copying) · **PL** Human error prone; Quality & accuracy improvement · **AS** Error prone; No fault tolerance; Regulatory; Redundant checks · **HA** Human error prone · **EK** Prone to human error · **FU** High error rates · **WA** Failure rate (high = suitable) · **WR** Prone to errors · **SY** Transactional (fewer transactional errors) · **WE** Proneness to human error · **HE** Prone to human errors · **FA** Human error · **BE** Proneness to human errors (relevance) · **ME** Proneness to human error; Failure rate · **FL** Prone to human error; data quality (value) · **AA** Quality improvement · **EN** Quality (KPI) |
| V5 | **HA** Cost reduction · **FU** ROI · **WA** Profitability (labour vs RPA cost) · **SY** Easy to achieve and show impact (best return) · **HE** Financially lucrative · **FA** Savings; Process cost; Efficiency · **FL** ROI (value axis) · **SP** Financial value · **AA** Business value · **BO\*** Financial value |
| V6 | **PL** Process importance (risk level) · **AS** Essential process (risk level) · **WR** High effect of business failure; influence on the business · **HE** New services to customers · **FA** SLA impact · **FL** Downstream process optimisation (value) · **SP** Customer value; Strategic value · **AA** Strategic alignment; customer satisfaction · **EN** Risk (KPI) · **BO\*** Strategic value |
| V7 | **PL** Irregular labour; Availability & flexibility · **AS** Time critical; Fluctuating demand; 24/7; Contains bottlenecks · **HA** Irregular labour · **FU** Bottlenecks · **WE** Urgency |
| V8 | **PL** Automation rate · **EK** Low automation rate · **WA** Automation rate · **ME** Automation rate |
| V9 | **AS** Employee satisfaction (tedious work); Redeployable personnel · **HE** Retirement of employees · **FL** Employee satisfaction (Priv.B) |
| F1 | **C22** Routine · **PL** Repetitive · **AS** Repetitive · **EK** Repetitive/routine · **CH** Periodicity · **FU** Repetitive tasks · **SY** Highly repetitive · **FA** Repetitive · **ME** Repetitiveness · **FL** Highly repetitive |
| F2 | **PL** Few variations; Standardization · **AS** Standardized process · **HA** Low variations · **EK** High standardization level · **FU** Predictable patterns or sequences · **WA** Standardization · **WR** Standardised · **SY** Standardised · **WE** Standardization · **HE** Standardized processes · **FA** Process standardized · **ME** Standardization · **FL** Standardized |
| F3 | **C22** Few exceptions · **PL** Few variations (merged with few exceptions) · **AS** Few exceptions · **EK** Low exception handling · **WA** Stability (low probability of exception) · **WR** Limited exception handling · **SY** Low levels of exception handling · **WE** Failure rate (low = viable) · **HE** Few exceptions · **FA** Number of exceptions · **BE** Limited exceptions/alternatives · **ME** No. of exceptions · **FL** Little exception handling |
| F4 | **C23** Maturity · **C22** Mature · **PL** Mature · **AS** Stable process and environment · **HA** Mature · **SY** Mature · **LW** Stable · **WE** Maturity · **HE** Process stability · **FA** Process stability · **BE** Stable rules · **ME** Proneness to changes |
| F5 | **C23** Complexity (low variation, few paths) · **PL** Length; Process complexity (risk level) · **AS** Complexity (risk level) · **EK** Low process complexity · **WR** Complexity · **SY** Less complex · **HE** Low complexity · **FA** Process complexity; Number of process steps · **ME** Complexity; No. of process steps · **FL** Low complexity |
| F6 | **C23** Rule-based · **C22** Rule-based · **PL** Clear rules · **AS** Rules based · **HA** Rule based · **EK** Rule-based · **WR** Rule-based; limited human interventions · **SY** Highly rule-based · **LW** Explicit, well-documented rules · **WE** Determinism · **FA** Rule-based; Cognitive requirements; Predictability of outcomes · **BE** Unambiguous rules; Enforced rules; Low cognitive requirements · **ME** Rule-based; Human decisions; Cognitive requirements · **FL** Rule-based |
| F7 | **C23** Data structure · **C22** Structured data · **PL** Digital and structured input · **AS** Digital and structured data · **HA** Structured readable input · **EK** Structured digital data (knock-out) · **WR** Digital and structured inputs/outputs · **SY** Digitised structured data input · **LW** Structured data · **WE** Structuredness (at least semi-structured) · **FA** Input and output data · **BE** Use of structured data · **ME** Structured data; Standard electronic data · **FL** Structured digital input |
| F8 | **C23** Digital data · **C22** Digital data · **PL** Digital and structured input · **AS** Digital and structured data; Digital trigger · **HA** Structured readable input ('structured, digital') · **EK** Structured digital data (knock-out) · **WR** Digital and structured inputs/outputs · **SY** Digitised structured data input · **WE** Data source must be digital · **HE** Digital inputs and outputs (mandatory) · **FA** Data digitalization; OCR involved · **BE** Use only digital data · **ME** Digital data · **FL** Structured digital input |
| F9 | **PL** Easy data access · **AS** Easy data access (authors' own) · **SY** Quality of input data (clarification) · **SP** Input data · **AA** Data (need, quality, integration effort) · **EN** Data requirements; Self containment · **BO\*** Data complexity |
| F10 | **FA** Test data · **AA** Minimum accuracy level · **EN** Measurable goal (Sturm et al.) |
| F11 | **C23** Multiple systems · **C22** Multiple systems · **AS** Multiple systems (optional) · **WR** Accesses multiple applications · **SY** Interacts with many systems · **WE** Number of systems; Interfaces · **FA** Number of systems; Application requirements · **BE** Access to software applications · **ME** No. of applications · **FL** Multiple different systems |
| F12 | **AS** Stable environment · **WR** Stable environment · **WE** Stability (systems) · **FA** Applications maturity; Applications similarity · **BE** Stable context · **ME** Application stability; System-related changes; Application similarity · **FL** Stability of the IT environment |
| F13 | **SY** Well-documented · **LW** Well-documented rules · **FA** Accurate process description · **BE** Clearly documented rules · **ME** Clear process documentation; Process maturity (formally defined) · **FL** Well-documented |
| F14 | **HA** Technical complexity (step 7) · **FU** Complexity and cost; quick wins · **WA** Fixed cost of RPA (configure, maintain) · **SY** Simplest delivery; organisational skills · **FA** Feasibility; Reusability · **FL** Implementation effort · **SP** Know-how · **AA** Processes/systems; Required expertise; Duration; Algorithm: implementations already running elsewhere · **EN** Effort (impact-effort matrix) · **BO\*** Integration complexity; Required expertise |
| F15 | **EN** Indefinability of rules; Self containment; Generalization; Cognition requirements · **BO\*** Model complexity |
| F16 | **AA** Maintenance; dynamic changes; resilience · **EN** Continuous adaptation (Sturm et al.) |
| F17 | **FA** Data security · **AA** Regulatory/ethics; Risk and transparency; Cybersecurity · **EN** Transparency requirements · **BO\*** Risk classification |
| F18 | **FU** Impact on employee roles · **SP** Change effort |

Items in individual sets that fit no row and are left out: SY "transactional" is placed under V4 only for its error argument; FA "number of robots allowed", "automation type" (attended or unattended) and "reusability" (placed under F14); WR "not a priority for the IT department"; HE's advice to start in the back office; PL and AS "risk level", which sets the risk appetite of the programme rather than scoring a process (its importance part is placed under V6 and its complexity part under F5); EN "relationship requirements".

**Coding corrections after the citation check (16 October).** Seven cells were removed because they broke the counting rule or counted one source item twice. WR is no longer in F1: WR defines repetitiveness as high volume, which is already counted in V1. C22 is no longer in V3: the cell came only from its 'High volume' definition ('performed frequently or by several people'), already counted in V1. SY is no longer in V6 or F12: 'business drivers' and 'stability of environment' belong to the organisational level in its section 3.3.1, which SY keeps apart from process characteristics. ME is no longer in V5: 'knowledge about current process cost' is a documentation item, not a financial value. AA's 'algorithm: implementations already running elsewhere' moved from F15 to F14, because it is an ease-of-implementation item (precedent and effort); AA was already counted in F14. HE is no longer in F15: 'screening of technologies' is a project stage before selection, not a selection criterion (it still supports gate G6, see section 4). One omission was added: AS in V2, because its 'Time savings' value covers processes that 'take a lot of time to perform'. Resulting counts: V2 12, V3 9, V5 7, V6 6, F1 10, F12 7, and F15 0 RPA sets and 1 AI set (+ BO\*); every other row is unchanged. Five further cells are kept but flagged, because they rest on an item that is also counted in another row: LW F13 (the same phrase as F6, 'explicit and well-documented rules'); PL F2 and F3 (one 'Few variations' item; PL is also in F2 through Standardization); HA F14 (Step 7 re-applies the indicators counted in F2, F6 and F7); BE V3 and V4 (one proneness-to-human-error measure, based on manual operations); and EN F9 and F15 (self containment; EN is in both rows through other items as well). Removing these duplicates would give F13 5 and F14 5 RPA sets, and V3 8 if BE's measure is kept under V4 only, which would take manual effort below half of the RPA sets; F2, F3, F9 and F15 would not change.

**Frequencies reported inside the reviews (second-order evidence).** Several sets already count how often criteria appear in the literature they reviewed. These tallies point the same way as the matrix:

| Review | What it counts | Most frequent criteria |
|---|---|---|
| Agaton & Swedberg 2018, Table 4.4 | Sources (of 23) naming each criterion | Rules based 20; multiple systems 11; error prone 10; high transaction volume 10; repetitive 10; few exceptions 7; stable 7; limited human intervention 6 |
| Costa et al. 2022, Table 5 | Papers (of 47) supporting each characteristic | Rule-based 7; mature 5; structured data 5; high volume 5; digital data 4; routine 4; few exceptions 2; multiple systems 2 |
| Farinha et al. 2024, Table 4 | Mentions by 34 Delphi experts (round 1) | Input and output data 19; number of exceptions 17; savings 17; repetitive 15; number of applications 14; accurate process description 9; standardised 8; applications maturity 8; number of transactions 7 |
| Farinha et al. 2024, Table 7 | Fuzzy Delphi ranking | Feasibility; accurate process description; input and output data; application access; data security and rule-based (joint 5th) |
| Shafik Salah Elsayed & Kassem 2022, section 3.1.2 | Order of mention in 9 expert interviews | Benefits from automation; rule-based; structured input/output; number of FTEs; repetitive or routine; well-defined rules; complexity |
| Meyer et al. 2024, section on weights | AHP cluster weights from 16 RPA experts | Data 26.3%; business potential 25.8%; human 17.3%; documentation 16.2%; process 14.4% |

**What the counts show.**

- Recurring in at least half of the 18 RPA sets: volume or frequency (17), error-proneness (15), rule-based decisions (14), structured input (14), digital input (14), standardisation (13), few exceptions (13), stability or maturity (12), duration (12), repetitiveness (10), low complexity (10), multiple systems (10), manual effort (9).
- Recurring in a minority of RPA sets: financial value (7), stable IT environment (7), wider business impact (6), implementation effort (6), documentation (6), time-criticality (5), automation rate (4), data access (3), employee value (3).
- Rare in RPA sets but present in at least two of the three AI sets: data access and quality, a checkable outcome (test data, measurable goal, minimum accuracy), maintenance, and risk and transparency. The RPA literature takes these for granted or leaves them to the project stage; the AI literature makes them explicit.
- AI-task fit is rarer still: no RPA set and one AI set (EN, through Sturm et al.) code it, plus BO\* from its abstract. HE's screening of simpler technologies and WR's Table 3 point the same way but are not selection criteria and are not counted.

---

## 3. Proposed criteria set

### 3.1 The two families and how they relate

The supervisor's two families recur in the literature under different names: relevance and feasibility (Bédard et al. 2024), added value and technical suitability (Haan 2021), business value and ease of implementation (Spreitzenbarth et al. 2024; appliedAI), value and feasibility (Flechsig et al. 2022, Fig. 5; Bodendorf 2025\*), impact and effort (Engel 2022).

**Logical relation.** A candidate is suitable only if it is both worth doing and doable: suitability = value AND feasibility. Bédard et al. state this directly ("the sub-goals RPA feasibility and RPA relevance must be satisfied"), and Agaton & Swedberg require value in at least one category as well as every mandatory criterion. The two families therefore have different jobs in the method:

- **Gates handle the minimum.** Each family has a floor that cannot be bought back with points from the other family. Precedents: PLOST's six mandatory criteria (Step 3), Agaton & Swedberg's mandatory criteria and value requirement, Shafik Salah Elsayed & Kassem's unweighted knock-out for structured digital input, and Engel's machine-learning suitability "stage gate".
- **Scores handle the degree.** Above the floors, criteria are scored and weighted to rank the candidates that passed. Precedents: PLOST Steps 6-8, C23 (AHP-TOPSIS), ME (AHP), EK (weighted 0/1 scores).
- **Reporting.** Show each candidate's value subtotal against its feasibility subtotal (the value-by-feasibility matrix of Flechsig et al., appliedAI and Engel), next to the weighted total. A high-value, low-feasibility candidate is then visible as a later project rather than hidden in the total. Spreitzenbarth et al., C23 and ME average both families into one number; that is compensatory above the gates and is the project's current additive model.

The project's six gates (G1 to G6) are all feasibility floors. The literature also has a value floor (Agaton & Swedberg's "potential value in at least one category"; Bédard et al.'s relevance sub-goal). Adding one value gate, for example "the task appears in the recorded work and has at least one named consequence", would make the AND explicit. The wording of that gate is a proposal, not taken from a source.

### 3.2 The criteria

"Support" gives the matrix rows behind each criterion and the number of sets using any of them (RPA sets of 18; AI sets of 3; BO\* noted). "Role" says whether the criterion works as a gate, a score or both; it is a proposal based on the precedents above.

**Value: why the task is worth improving**

| ID | Criterion | One-line definition | Support | Sources (codes) | Role |
|---|---|---|---|---|---|
| A1 | Workload volume | How much of the buyer's working time the task takes: how often it occurs multiplied by the manual handling time per case. | V1 (17), V2 (12 + 2 AI), V3 (9 + 1 AI); any of the three: 18 of 18 RPA, 2 AI. Measured definitions: WA equations 1-2, HA, ME "volume = frequency x time"; five-point scales for frequency and duration in C23 Table 8. | C23, C22, PL, AS, HA, EK, CH, FU, WA, WR, SY, LW, WE, HE, FA, BE, ME, FL; AI: AA, EN | Score  |
| A2 | Error-proneness and accuracy gain | How often manual handling of the task produces errors or rework, and how far the aid can reduce them. | V4: 15 RPA, 2 AI (AA, EN). | C23, PL, AS, HA, EK, FU, WA, WR, SY, WE, HE, FA, BE, ME, FL; AI: AA, EN | Score  |
| A3 | Business impact beyond the buyer's time | Financial, customer or strategic consequences of the task's outcome (for example the cost of a missed price difference), excluding the time saved. | V5 (7 + 2 AI + BO\*), V6 (6 + 3 AI + BO\*); either: 10 RPA, 3 AI. | PL, AS, HA, FU, WA, WR, SY, HE, FA, FL; AI: SP, AA, EN, BO\* | Score; anchor 5 needs the company's confirmation (project rule)  |
| A0 | Value floor | The task has value on at least one of A1 to A3, and is not already automated. | AS (value in at least one category); BE (relevance must hold); V8 automation rate (4 RPA). | AS, BE; V8: PL, EK, WA, ME | Gate  |

**Feasibility: whether it can be built and evaluated within the BEP**

| ID | Criterion | One-line definition | Support | Sources (codes) | Role |
|---|---|---|---|---|---|
| B1 | Repetition and standardisation | The task recurs (daily or weekly) and is done in the same way each time, with few variants. | F1 (10), F2 (13); either: 15 RPA. | C22, PL, AS, HA, EK, CH, FU, WA, WR, SY, WE, HE, FA, ME, FL | Score  |
| B2 | Exception rate | The share of cases that leave the standard path and need special handling is low, and the boundary of an exception is clear. | F3: 13 RPA. | C22, PL, AS, EK, WA, WR, SY, WE, HE, FA, BE, ME, FL | Score (gate in AS, PL)  |
| B3 | Stability | No planned change, during the BEP, to the task, its rules or the systems and document formats it uses. | F4 (12), F12 (7); either: 14 RPA. | C23, C22, PL, AS, HA, WR, SY, LW, WE, HE, FA, BE, ME, FL | Gate (as in AS, PL) with a score if needed  |
| B4 | Digital, readable input | The inputs exist in digital form; fields the rules compare are structured, while the documents the AI reads may be semi-structured. | F7 (14), F8 (14); either: 15 RPA. WE accepts semi-structured data. | C23, C22, PL, AS, HA, EK, WR, SY, LW, WE, HE, FA, BE, ME, FL | Gate for digital (EK, PL, HE); score for structure  |
| B5 | Task-technology fit | Which steps can be written as fixed rules and which need reading or matching that rules cannot define; AI should be needed for a core step and simpler tools should be enough for the rest. | F6 (14 RPA, in the RPA direction: rule-based is good for a bot) and F15 (0 RPA + 1 AI + BO\*): EN/Sturm et al. "indefinability of rules", "generalization". Not counted: HE "screening of technologies" (a stage before selection) and WR Table 3; AA "algorithm running elsewhere" is coded under F14. | Rule side (F6): C23, C22, PL, AS, HA, EK, WR, SY, LW, WE, FA, BE, ME, FL; AI side (F15): no RPA set; AI: EN, BO\* | Gate (G6) and score  |
| B6 | Data access and availability | Permitted access to enough representative past cases with their inputs, in a usable form. | F9: 3 RPA (PL, AS, SY), 3 AI (+ BO\*). | PL, AS, SY; AI: SP, AA, EN, BO\* | Gate (G2) and score  |
| B7 | Checkable outcome | A trustworthy correct answer per case exists or can be built, so the aid's output and the manual work can be compared. | F10: 1 RPA (FA "test data"), 2 AI (EN/Sturm et al. "measurable goal"; AA "minimum accuracy"); Brynjolfsson et al. 2018 (not counted). | FA; AI: AA, EN | Gate (G3) and score  |
| B8 | Implementation effort | Build effort, integration and know-how needed for a working prototype within the BEP. | F14: 6 RPA, 3 AI (+ BO\*). | HA, FU, WA, SY, FA, FL; AI: SP, AA, EN, BO\* | Gate (G5) and score  |
| B9 | Risk, transparency and acceptance | Errors can be detected, the buyer can see why the aid flags a line, data use is permitted, and the buyer accepts the support. | F17, F18: 2 RPA (FA, FU), 3 AI (+ BO\*); FL reports user resistance as a barrier. | FU, FA; AI: SP, AA, EN, BO\* | Gate only (G1, G4)  |

**Considered and not adopted as separate criteria.**

- *Low process complexity* (F5, 10 RPA sets). C23 defines it as "low variation and few execution paths", which is B1, and other sets use it as a proxy for build effort, which is B8. Scoring it separately would count the same property twice; ME warns that the criteria are not independent.
- *Multiple systems* (F11, 10 RPA sets). It rewards RPA because a bot bridges systems that have no interface. For a reading aid, working across Exact, PDFs and e-mail matters through the manual effort it causes (A1) and the integration it needs (B8), not as a separate merit.
- *Documented process* (F13, 6 RPA sets) and *stable IT environment* (F12, 7). Documentation matters for programming a bot step by step; in this project the task is described by the observations. The stable-environment part is folded into B3.
- *Time-criticality* (V7, 5) and *employee-related value* (V9, 3). Low recurrence; a delay or a burden that has a consequence can be named under A3.
- *Maintenance and continuous adaptation* (F16, 2 AI sets). Outside a BEP prototype; it belongs in the handover recommendation.

**Weights.** None of the sets offers transferable weights. C23's weights are, in this note's reading, the authors' judgement (and inconsistent, see 1.1), ME's come from 16 RPA experts and concern RPA, EK and PL leave weights to the organisation (EK used equal weights in its demonstration; PL uses cumulative voting and recommends at least three stakeholders), and SP weights its six dimensions equally. This supports the project's plan to have the weights set or reviewed by Zhongxin (option A or B), and PL's cumulative voting is a citable alternative if Johan or Dennis should take part.

---

## 4. The project's seven criteria against the proposed set

Project definitions read from the selection notebook (section 3, markdown cells 14-15) and the update of 15 October (section 1).

| Project criterion | Project definition, in short | Proposed criterion | Literature support | Verdict |
|---|---|---|---|---|
| Observed workload contribution | Arno's recorded effort and difficulty within the bounded activity; anchors on share of the 560 in-scope minutes and burden on several days | A1 Workload volume | Strong: 18 of 18 RPA sets use volume, duration or manual effort | Supported. The time part matches A1; the "difficulty / recorded burden" part has no counterpart except AS "tedious" under employee satisfaction. Either drop burden from the anchors or name it under A3 when it has a consequence. |
| Business value beyond counted workload | Purchasing or company consequences beyond buyer time; anchor 5 needs Johan's confirmation | A2 and A3 | Strong for A2 (15 RPA, 2 AI) and moderate for A3 (10 RPA, 3 AI) | Supported, but the literature separates error-proneness (how often errors happen) from impact (what they cost). The 15 September example, outdated prices leading to sales at a loss, is both. Splitting it lets A2 be scored from the observations while A3 waits for Johan. |
| AI-task fit | Whether a useful AI function is needed beyond rules; anchor 5 needs reading unstructured documents or judging patterns, with a precedent | B5 Task-technology fit | RPA sets point the other way (rule-based is good, 14 of 18); of the AI sets only EN/Sturm et al. codes it (plus BO\* from its abstract); HE's screening stage and WR Table 3 support it outside the counts | Supported, but thinly. Reword it so that it states the split: the comparison is rules, the reading and matching is where rules fail. AA's "already running elsewhere" (coded under implementation effort, F14) supports the precedent requirement in anchor 5. |
| Data readiness above the gate minimum | Usability of permitted inputs: from a few hand-collected examples to exportable representative cases with a traceable correct outcome | B4 and B6; the "traceable correct outcome" part belongs to B7 | Digital and structured input are strongly supported (15 RPA); data access is supported mainly by AI sets (3 RPA, 3 AI) | Supported, but it mixes three things the literature keeps apart: input form (B4), access to cases (B6) and the correct answer (B7). Move the correct outcome into evaluation feasibility to avoid counting it twice. |
| Repetition / process standardisation | Recurrence and stable inputs, outputs and exception boundaries | B1, B2, B3 | Strong: repetitive or standardised 15, few exceptions 13, stable 14 of 18 RPA sets | Supported. The literature treats these as three criteria; at least the exception rate and stability should be named separately (B3 as a gate). |
| Prototype / technical feasibility | Engineering effort and dependencies of the bounded build | B8 Implementation effort | Moderate: 6 RPA, 3 AI | Supported. Most RPA sets judge effort through process characteristics (complexity, variants) rather than as a criterion of its own; FA ranks "feasibility" first. |
| Evaluation feasibility | A defensible manual-versus-assisted comparison for SQ5 | B7 Checkable outcome | Weak: 1 RPA set (FA "test data"), 2 AI sets (measurable goal, minimum accuracy) | Partly supported. Selection methods choose processes to deploy, not to evaluate in a study, so the comparison with a manual baseline is a project requirement from SQ5 and design science (Peffers et al. 2007), not an automation-suitability criterion. Keep it, and say so. |

**Criteria the literature uses that the project does not name.**

- Exception rate (B2): 13 of 18 RPA sets; a gate in AS and PL. The current repetition criterion mentions "clear exception boundary" only in its score-5 anchor.
- Process stability (B3): 12 of 18 (14 with a stable IT environment); a gate in AS, PL and LW. Not in the project at all; it matters because the prototype and its test cases are built on an Exact copy that ends in October 2025, so the task, its rules and its documents must not have changed since then.
- Input structure and digital input (B4): 14 of 18 each; a knock-out in EK and a gate in PL and HE. The project's gate G2 covers "suitable accessible data" without naming form; the observed mix of paper, PDF, e-mail and websites makes this a real difference between candidates.
- Error-proneness as its own value criterion (A2): 15 of 18 RPA sets and 2 AI sets.
- A value floor (A0): AS and BE; all six project gates are on the feasibility side.

**Project criteria and features the literature does not support.**

- Evaluation feasibility as a selection criterion: only partial support (see the table); it rests on the research design.
- "Difficulty" or "recorded burden" inside workload: not a criterion in any set read.
- The 1/3/5 anchors and cut-offs (under 5%, 5-15%, over 15%; fewer than 3 of 5 days): project judgements. The literature offers other scales (C23 Table 8: frequency from less than monthly to daily, duration from under 15 minutes to over six hours; EK: 0/1 against an organisation-specific threshold), so the anchors can be defended as project choices, not as taken from a source.
- The gates themselves are well supported in form (PL, AS, EK, EN), and individually: G1 permission and G4 risk and acceptance by FA (data security), AA (regulation, risk), EN (transparency), SP (change effort) and FL (user resistance); G2 by PL and AS (easy data access) and EK (knock-out); G3 by FA (test data) and EN/Sturm et al. (measurable goal); G5 by the effort criteria under B8; G6 by EN/Sturm et al. (indefinability of rules) and HE (screen simpler technologies first).

---

## 5. Caveats

**RPA criteria assume a different kind of work.** The sets in section 2 were written to select processes for software robots: rule-based, deterministic work on structured digital input, at high volume, in back offices, usually without a person in the loop. LW describe RPA as tools for "structured data, rules-based processes, and deterministic outcomes"; WR Table 3 sets RPA (standardised, structured, rule-based, deterministic) against intelligent automation (less standardised, unstructured, knowledge-based, probabilistic); EK say their criteria are "mainly relevant to selecting processes suitable for simple RPA applications"; EN argues that criteria for rule-based automation do not cover cognitive automation.

**What changes for an AI reading-and-matching aid for one buyer.**

- *Rule-based and structured-data criteria split rather than apply.* The aid is useful precisely where rules fail: supplier PDFs in their own layouts, German confirmations with week-number dates, two order lines merged into one. For those steps the RPA criteria point the wrong way and the AI criteria (indefinability of rules, generalisation) apply. For the comparison of price, date and quantity the RPA criteria still apply and argue for plain rules. This is why B5 is stated as a split.
- *Volume is judged at a different scale.* RPA sets look for high volumes and FTE savings (one public organisation in FL concluded that a process needs at least 20 to 25 workdays a year of work for a bot to break even). One buyer's task will not reach that scale. Value has to be judged relative to Arno's workload and the consequence of errors, which SY's note that medium volumes and business-critical tasks can also suit supports.
- *A person stays in the loop.* RPA criteria such as "low cognitive requirements" and "limited human intervention" exist because the bot runs alone. The aid flags and the buyer decides, so those criteria fall away and are replaced by transparency and acceptance (B9, EN, AA).
- *Probabilistic output needs a reference.* A bot either follows the rule or fails; an AI reader can be confidently wrong. That makes a checkable outcome and a minimum accuracy (B7; Sturm et al. via EN; AA) more important than in any RPA set.
- *Measurement differs.* PL, WA, WE, EK and HA measure criteria from event logs or user-interface logs; the project measures them from observation records. The indicators carry over (frequency, duration, rework), the data source does not.
- *Multiple systems change meaning.* For RPA it is a reason to automate; for the aid it is a source of manual effort and of integration work.

**Which criteria rest on practitioner rather than academic sources.**

- Futran (FU) and appliedAI (AA) are practitioner documents. Criteria that appear only there or almost only there: bottlenecks (also an AS sub-indicator), effect on employee roles (in academic sets only as SP's change effort and FL's user resistance), "algorithm already running elsewhere", minimum accuracy, and the regulatory, cybersecurity and resilience flags.
- AS drew most of its 23 sources from vendors and consultancies, and "easy data access" was added by the authors without a source (Table 4.6, p. 36). PL's data-access gate inherits this.
- FA's criteria among the top 11 in Table 7 (feasibility, accurate process description, application access, data security, test data, efficiency) came from the practitioner Delphi, not from its literature review (Table 4 shows no review counterpart for them). B7 and B8 lean on these.
- ME's weights come from 16 RPA experts recruited through consultancies and LinkedIn; SP's value and ease sub-dimensions were adapted from a consultancy report and rated by 20 practitioners; EK's and HE's lists were checked or extended in expert interviews and workshops; FL's value-by-feasibility matrix describes what the interviewed organisations do.
- The criteria with the broadest academic base, through the reviews C22, WR, SY, FA (review part) and ME, are rule-based decisions, volume, structured and digital input, standardisation, few exceptions, maturity, complexity, error-proneness, duration and multiple systems. The criteria the BEP needs most beyond these (data access, checkable outcome, implementation effort, AI fit) rest on fewer and more practice-based sources and need to be argued from the research design.

**Other limits.**

- Validation in this literature is thin: most methods were tested in one organisation with a handful of experts (C23: one case, two interviewees; PL: one case and two think-aloud sessions; EK: one purchase-to-pay event log and two experts; ME: one company; BE: 13 processes; FA: 18 processes in six organisations is the largest).
- The sources disagree in places. WA counts a high failure rate as a reason to automate, while WE treats a low failure rate as favourable. SY records that some authors see RPA as suited to temporary processes, against the maturity criterion. WR's body says lower complexity is better while its conclusion lists "complex business processes" among the best suited; this is a reading of the text, not a statement by the authors. C23's "human input" criterion is worded as "activities do not rely on human input" while its scale counts the share of activities that require human input.
- The matrix is a coding by one reader. A second coder would likely place a few cells differently, mostly in V5/V6 and F12/F13. The citation check of 16 October already changed eight cells and flagged five double codings (section 2).

---

## Appendix A. Full citations

Agaton, B., & Swedberg, G. (2018). *Evaluating and developing methods to assess business process suitability for robotic process automation: A design research approach* [Master's thesis, Chalmers University of Technology and University of Gothenburg]. https://odr.chalmers.se/handle/20.500.12380/255664

Bédard, M., Leshob, A., Benzarti, I., Mili, H., Rab, R., & Hussain, O. (2024). A rule-based method to effectively adopt robotic process automation. *Journal of Software: Evolution and Process, 36*(11), e2709. https://doi.org/10.1002/smr.2709

Bodendorf, F. (2025). A data-driven use case planning and assessment approach for AI portfolio management. *Electronic Markets, 35*, Article 22. https://doi.org/10.1007/s12525-025-00759-x (abstract only)

Brakemeier, H., Gerbert, P., Hartmann, P., Liebl, A., Schamberger, M., & Waldmann, A. (n.d.). *Applying AI: How to find and prioritize AI use cases*. appliedAI Initiative. Retrieved 16 October 2026, from https://www.appliedai.de/assets/images/280323_AI_Whitepaper_UseCase_Screen.pdf (No year printed; the PDF read was created in 2024.)

Brynjolfsson, E., Mitchell, T., & Rock, D. (2018). What can machines learn and what does it mean for occupations and the economy? *AEA Papers and Proceedings, 108*, 43-47. https://doi.org/10.1257/pandp.20181019

Choi, D., R'bigui, H., & Cho, C. (2021). Candidate digital tasks selection methodology for automation with robotic process automation. *Sustainability, 13*(16), 8980. https://doi.org/10.3390/su13168980

Costa, D. A. da S. (2022). *A method to select processes for automation* [Master's thesis, Instituto Superior Técnico, Universidade de Lisboa].

Costa, D. A. da S., Mamede, H. S., & Mira da Silva, M. (2022). Robotic process automation (RPA) adoption: A systematic literature review. *Engineering Management in Production and Services, 14*(2), 1-12. https://doi.org/10.2478/emj-2022-0012

Costa, D. S., Mamede, H. S., & da Silva, M. M. (2023). A method for selecting processes for automation with AHP and TOPSIS. *Heliyon, 9*(3), e13683. https://doi.org/10.1016/j.heliyon.2023.e13683

Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2023). *GPTs are GPTs: An early look at the labor market impact potential of large language models* (arXiv:2303.10130v5). https://arxiv.org/abs/2303.10130 Published version: *Science, 384*(6702), 1306-1308 (2024), https://doi.org/10.1126/science.adj0998 (not read; the arXiv version was read).

Engel, C. T. (2022). *Cognitive automation: Assessing business process automation potentials in organizations driven by artificial intelligence* [Doctoral dissertation no. 5217, University of St.Gallen].

Erdogan, A. M., & Dogan, O. (2024). Process selection for RPA projects with MDCM: The case of Izmir Bakircay University. In M. A. Jabbar, S. Tiwari, F. Ortiz-Rodríguez, S. Groppe, & T. Bano Rehman (Eds.), *Applied Machine Learning and Data Analytics* (Communications in Computer and Information Science, pp. 15-28). Springer. https://doi.org/10.1007/978-3-031-55486-5_2 (not accessible; metadata only)

Farinha, D., Pereira, R., & Almeida, R. (2024). A framework to support robotic process automation. *Journal of Information Technology, 39*(1), 149-166. https://doi.org/10.1177/02683962231165066

Flechsig, C., Anslinger, F., & Lasch, R. (2022). Robotic Process Automation in purchasing and supply management: A multiple case study on potentials, barriers, and implementation. *Journal of Purchasing and Supply Management, 28*(1), 100718. https://doi.org/10.1016/j.pursup.2021.100718

Gajula, S. (2024, December 9). *How to identify automation opportunities in your workflow*. Futran Solutions. Retrieved 16 October 2026, from https://futransolutions.com/blog/how-to-identify-automation-opportunities-in-your-workflow/ (the page metadata show a modification on 12 January 2026)

Haan, W. J. (2021). *How can process mining be used to identify robotic process automation opportunities?* [Bachelor's thesis, University of Twente]. https://purl.utwente.nl/essays/85792

Herm, L.-V., Janiesch, C., Helm, A., Imgrund, F., Hofmann, A., & Winkelmann, A. (2023). A framework for implementing robotic process automation projects. *Information Systems and e-Business Management, 21*(1), 1-35. https://doi.org/10.1007/s10257-022-00553-8

Jongeling, H. E. (2022). *Identifying and prioritizing suitable RPA candidates in ITSM using process mining techniques: Developing the PLOST framework* [Master's thesis, Utrecht University]. https://studenttheses.uu.nl/handle/20.500.12932/41751

Jongeling, H. E., Lu, X., Beerepoot, I., van de Weerd, I., & Reijers, H. A. (2023). Getting your RPA priorities straight with process mining: The PLOST framework. In *ECIS 2023 Research Papers* (Paper 308). https://aisel.aisnet.org/ecis2023_rp/308

Lacity, M. C., & Willcocks, L. P. (2016). A new approach to automating services. *MIT Sloan Management Review, 58*(1), 41-49 (Fall 2016). Accepted version: http://eprints.lse.ac.uk/68135/

Meyer, F., Hinrichsen, S., & Padoano, E. (2024). A structured method for the selection of business processes suitable for robotic process automation. In *Human Systems Engineering and Design (IHSED 2024)* (AHFE Open Access, Vol. 158, pp. 10-20). https://doi.org/10.54941/ahfe1005524

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 30*(3), 286–297. https://doi.org/10.1109/3468.844354 (not re-read for this note)

Shafik Salah Elsayed, N., & Kassem, G. (2022). Assessing process suitability for robotic process automation: A process mining approach. In *Wirtschaftsinformatik 2022 Proceedings* (Student Track, 18). https://aisel.aisnet.org/wi2022/student_track/student_track/18

Spreitzenbarth, J. M., Bode, C., & Stuckenschmidt, H. (2024). Artificial intelligence and machine learning in purchasing and supply management: A mixed-methods review of the state-of-the-art in literature and practice. *Journal of Purchasing and Supply Management, 30*(1), 100896. https://doi.org/10.1016/j.pursup.2024.100896

Sturm, T., Fecho, M., & Buxmann, P. (2021). To use or not to use artificial intelligence? A framework for the ideation and evaluation of problems to be solved with artificial intelligence. In *Proceedings of the 54th Hawaii International Conference on System Sciences* (pp. 206-215). (Read only through Engel, 2022; reference as printed there.)

Syed, R., Suriadi, S., Adams, M., Bandara, W., Leemans, S. J. J., Ouyang, C., ter Hofstede, A. H. M., van de Weerd, I., Wynn, M. T., & Reijers, H. A. (2020). Robotic process automation: Contemporary themes and challenges. *Computers in Industry, 115*, 103162. https://doi.org/10.1016/j.compind.2019.103162

Wanner, J., Hofmann, A., Fischer, M., Imgrund, F., Janiesch, C., & Geyer-Klingeberg, J. (2019). Process selection in RPA projects: Towards a quantifiable method of decision making. In *Proceedings of the 40th International Conference on Information Systems (ICIS 2019)*. https://aisel.aisnet.org/icis2019/business_models/business_models/6/

Wellmann, C., Stierle, M., Dunzer, S., & Matzner, M. (2020). A framework to evaluate the viability of robotic process automation for business process activities. In A. Asatiani et al. (Eds.), *Business Process Management: Blockchain and Robotic Process Automation Forum* (Lecture Notes in Business Information Processing, pp. 200-214). Springer. https://doi.org/10.1007/978-3-030-58779-6_14 (accepted manuscript: arXiv:2007.10900)

Wewerka, J., & Reichert, M. (2020). *Robotic process automation: A systematic literature review and assessment framework* (arXiv:2012.11951). https://arxiv.org/abs/2012.11951

## Appendix B. Copies read

The full texts were open-access copies: the publishers' open-access pages, the authors' accepted manuscripts and university repositories named in section 1 (for example Europe PMC for Costa et al. 2023, Zenodo record 5355353 for Flechsig et al. 2022, LSE Research Online for Lacity & Willcocks 2016 and arXiv for Wellmann et al. 2020). They were downloaded in October 2026, read as data and are not stored in the repository. The matrix in section 2 was produced from a hand-coded mapping of the criteria to the merged rows; the wording table records that mapping cell by cell.
