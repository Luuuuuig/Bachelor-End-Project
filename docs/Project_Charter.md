# Project Charter — Operational Purchasing Workload Reduction

**Status:** Project-control decisions and evidence state synchronized 9 October 2026. The [current status and reading guide](Current_Status_and_Reading_Guide.md) owns the immediate priorities.

This charter is intentionally short. It does not replace the proposal, AS-IS process, methodology, measurement protocol or project timeline; it freezes the project-control decisions that should remain stable as Analyze moves toward focal-case confirmation and Improve.

## Business problem

The operational purchasing process contains recurring administrative work, manual verification, rework, information-handling burden, interruptions and judgement-intensive activities. The five-session analysis now describes where the recorded work is concentrated. Order and confirmation checking (called purchase-price control until 7 October) is the provisional focal case: checking supplier quotations and confirmations against the PO for price, delivery date, quantity and missing or extra lines. Its data, reference answers, buyer acceptance and supervisor review still need to support the final choice.

## Business objective / Voice of Customer

Reduce meaningful operational-buyer workload while maintaining the required quality of purchasing outcomes.

The company expects the focal thesis artifact to contain a **meaningful AI-supported contribution**. Conventional automation and process redesign may be supporting components or separate quick-win recommendations. A non-AI focal artifact is an exception and requires documented Analyze evidence that no candidate passes the responsible-AI, data, quality and evaluation-feasibility gates, followed by explicit company and academic-supervisor approval.

## Academic objective

Use DMAIC to establish the current process, workload baseline and improvement opportunity; select one high-value focal activity; then use DSRM to design, demonstrate and evaluate the selected digital/AI-supported artifact.

## Primary stakeholders

- Operational buyer — main workload outcome and domain expert.
- Tactical buyer Dennis — relevant tasks, information exchanges, and participation in design and evaluation where the selected improvement affects his work.
- Company manager / project sponsor — business relevance and implementation direction.
- TU/e supervisor — academic scope, methodology and evaluation validity.
- Second academic assessor — Plan of Work approval and co-assessment of the final report under the 1BEPIE procedure.
- Supporting stakeholders as required — Finance, IT/system owners and other purchasing roles.

## In scope

The detailed operational purchasing flow runs from purchasing need through `Bevestigd`. Include Dennis's tactical purchasing work in the surrounding process investigation, as decided on 10 September. Arno's workload remains the primary outcome; retain separate actor-specific evidence. The existing 31-task register describes operational work, not a completed Dennis inventory. Use the [purchasing activity framework](process/Purchasing_Activity_Framework_2026-09-21.md) for stage definitions and the [current kinds-to-framework map](measurement/Kinds_Framework_Map_2026-10-06.csv) for the analysis. The 14 September crosswalk is historical.

Define/Measure/Analyze cover operational purchasing and Dennis's relevant tactical tasks and connections with Arno. Improve/DSRM will focus deeply on **one selected primary activity or coherent process component**. Other supported opportunities remain company recommendations/quick wins rather than disappearing from scope.

## Out of detailed scope for now

- Logistics and former EXC work as an improvement focus, following the [10 September academic decision](meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md). Since [1 October](meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md) their time stays in the total time record under OTHER, outside the work considered for AI improvement. This supersedes the earlier logistics/buyer-rework exception. Preserve historical raw evidence and use explicit analytical exclusions.
- Independent optimization of Dennis's workload. Tactical purchasing tasks, including supplier selection where observed, can inform a coherent purchasing improvement tied to the primary objective.
- Full technical integration or production deployment before the focal use case and feasibility gates are justified.

## Y / outcome structure

The project does **not** use one invented total-workload score.

The Measure-phase outcome is a multidimensional profile of included purchasing work. Apply the [scope and classification addendum](measurement/Scope_and_Classification_Addendum_2026-09-14.md); former EXC and logistics work stays visible in the total time record but cannot contribute to candidate ranking. The profile uses, where relevant:

- task frequency;
- active processing time;
- case/line volume;
- rework occurrence and rework time;
- interruptions / organizational constraints;
- qualitative difficulty / uncertainty / exception evidence;
- expertise dependence.

Quality remains a separate CTQ. The concrete quality metric is focal-activity-specific, but the success structure is already fixed: the predeclared workload endpoint must improve by at least a meaningful threshold **and** the quality guardrail must pass. Thresholds and the activity-specific rubric are frozen after focal-case selection and manual-baseline review, before artifact development/formal testing.

## Current evidence state

- The operational AS-IS process, 31-task register, buyer walkthrough, formal SOP/WI evidence, workload construct and 28 August pilot are established.
- Five official Arno sessions are recorded: 31 August and 1, 8, 18 and 23 September, with **892 minutes of confirmed net observation**. The [analysis notebook](../Arno_Analysis_2026_10_02.ipynb) starts from 287 rows and 751 recorded activity minutes. Excluding the 9 contaminated OBS-16 minutes leaves **742 valid recorded activity minutes**, including **182 former-EXC minutes** under OTHER and **560 minutes within the improvement scope**. Clock exposure and recorded activity time are different quantities.
- The workload description, purchasing-stage summaries, case/line comparisons, limitations and draft cause analysis are substantially complete. These observations support descriptive selection evidence; they are not a validated time standard or evidence of achieved savings.
- The [selection notebook](../Focal_Case_Selection_2026-10-07.ipynb) provisionally favors order and confirmation checking. Test-data/reference checks, Arno's focused feedback, Zhongxin's review and an agreed weighting procedure, and Johan's business-value evidence remain relevant to confirming the choice. Dennis's explanation that outdated purchase prices led to loss-making sales (15 September) is evidence of business value; financial impact and achievable benefit remain unquantified.
- Dennis has qualitative evidence from 15 September and a timed session on 25 September. His evidence stays separate. Following the [1 October decision](meetings/Academic_Supervisor_Meeting_Notes_2026-10-01.md), Arno analysis proceeds now; further Dennis observation is conditional on a specific remaining question after his return.
- Measurement Protocol v1.3 is retained with the later scope/timing addendum. The initial five-day target has been reached. Neither 40 net hours, another broad Arno observation round, two more Dennis days, nor a goodness-of-fit test is a current completion requirement. Targeted label review is useful; the 45-record recoding/κ exercise is optional and does not block the next phase.
- The [final Plan of Work](proposal/Plan_of_Work_Final_2026-09-22.pdf) was submitted. It includes the named second assessor, completed start-BEP reflections and signed scientific-conduct declaration. Its main question and five sub-questions are authoritative; the [readable assignment](proposal/BEP_Assignment_1BEPIEX.md) mirrors their submitted wording and order, as confirmed by Yijie on 7 October.

## Time boundary and study load

- The combined normative workload for **1BEPIE + 1BEPIEX is 420 hours in total**.
- Company placement / Hytech-Pommec contract runs through **7 January 2027**. This is the company-work boundary, not the end of all academic obligations.
- Final report, scientific-conduct item and end-BEP reflection: **15 January 2027 at 23:59**.
- Final presentation / assessment meeting: **on or before 29 January 2027**.
- Final assessment deadline: **7 February 2027**.
- Detailed sequencing, deadline-control notes and planned-versus-actual effort tracking are maintained in `Project_Timeline.md`.

## DMAIC tollgates

| Gate | Exit condition |
|---|---|
| **Define → Measure** | AS-IS sufficiently stable, scope/workload construct defined, measurement protocol ready for pilot. **Current status: passed.** |
| **Measure pilot → baseline** | Pilot shows the observation sheet is usable; timing/task-switch rules are workable; confidentiality and sampling rules are clear; controlled protocol established. **Current status: passed; v1.3 is controlled from 2 September without changing the live coding structure.** |
| **Measure → Analyze** | At least five distinct observation days are documented; the v1.3 Day-5 coverage review passes; representative activity-family workload evidence exists, with detailed Task-ID enrichment where justified, plus documented windows, net observed time, coded-active time, case mix, unmapped work and limitations. **Current status: on 1 October Zhongxin instructed Yijie to begin the analysis with the five Arno sessions; coverage limitations remain.** The coverage review is retrospective (analysis notebook, part 3), and no numerical stability threshold or statistical fit test was agreed. The instruction does not establish that the sessions are representative or that the data are finally sufficient. The 8 October meeting requested further day-pattern analysis and a Kruskal-Wallis investigation. The 9 October notebook additions are prepared for review; final sufficiency remains open. Additional observations address a specific evidence gap. |
| **Analyze → Improve** | Candidates first pass non-compensable AI/data/ground-truth/risk/time gates, then are compared with pre-agreed weighted criteria and sensitivity analysis. One focal activity is selected and supervisor alignment obtained. **Current status: in progress.** A provisional comparison with Yijie's weights favours order and confirmation checking (7 October); the source and reference checks, Arno's acceptance, Zhongxin's review and the final weighting/scoring decision, and Johan's business-value confirmation are still open. Dennis's qualitative business-value evidence is recorded. |
| **Improve → Control** | Before development/formal testing, the primary workload endpoint, meaningful-improvement threshold, quality rubric and guardrail are frozen. The artifact is then evaluated against current practice; implementation safeguards/KPIs are defined. |

## Current priority

Use the [current status and reading guide](Current_Status_and_Reading_Guide.md) for the ordered worklist and reading route. The immediate task is to confirm the provisional focal case through the remaining data, buyer and supervisor checks, then write the Analyze conclusion. Requirements, evaluation design, prototype development, evaluation and thesis completion follow that decision. The workload threshold and quality guardrail must still be frozen before artifact development/formal testing.

## Key control rule

Do not select or build the final artifact because a single observed case appears interesting. The focal case must pass the Measure/Analyze evidence gates above.

