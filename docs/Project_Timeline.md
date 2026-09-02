# Project Timeline / Gantt — Bachelor End Project

**Status:** Current planning draft, synchronized 2 September 2026.

**Purpose:** This file is the project-planning companion to `Project_Charter.md`. It turns the current DMAIC/DSRM sequence, supervisor milestones and known dependencies into a shareable Gantt chart. The Mermaid source can be copied into draw.io / diagrams.net for visual editing.

**Supervisor-facing visual master:** [Ganttchart.drawio.png](https://drive.google.com/file/d/1Qe29SYs5xBGpjUXFTREVlIS7x2jsy18P/view?usp=sharing). Keep this Drive copy synchronized with the Mermaid planning source below.

## Planning assumptions

- Project start: **17 August 2026**.
- Hytech-Pommec contract end / latest company-placement boundary: **7 January 2027**. The BEP/company work may finish earlier if the required project activities are completed and this is agreed with the relevant parties.
- Current project state: **Define largely complete; the pilot and two official baseline days are complete, and exploratory baseline collection continues under v1.3 from 2 September**. Current evidence totals 351 net observed minutes and 265 timed coded-active minutes.
- Pilot: completed on **28 August 2026**; v1.1 established the two-level architecture. The 31 August session led to v1.2. The 1 September session then exposed the post-MAX interpretation, stopping-rule and governance clarifications internally controlled in v1.3 from 2 September. Academic methodological review is scheduled for 3 September. Any supervisor-required change will be dated and versioned; earlier data remain usable unless the review identifies a material measurement-system validity problem.
- Official baseline observations began **31 August 2026**. The eight-day Gantt bar is the collection window, not a promise of eight observation days. The current planning minimum is meaningful coverage on **five distinct working days**, followed by the v1.3 Day-5 coverage review. The two completed partial days contribute evidence, but whether they count as two of the five days must be confirmed with the academic supervisor. Five days is not automatically 40 net observed hours; both days/windows and net minutes are reported.
- Detailed Exact/Orbis production-data/interface feasibility is intentionally scheduled in **Analyze, after the exploratory Measure baseline**.
- Supervisor milestones from the 25 August meeting are fixed: **15 September half-page project description; 20 September Plan of Work draft; 27 September final Plan of Work submission**. Internal complete-package targets are **18 September** for the draft and **25 September** for the final package. The attached template also requires five start-BEP professional-skill reflections (approximately 1,500–2,000 words total) and the scientific-conduct declaration; these are part of the submission workload.
- Weekly academic supervision: **Thursday 15:00–16:00**, with agenda prepared/sent on Wednesday.
- Durations after Measure are **planning estimates**, because the final artifact and evaluation design depend on the selected focal case.
- FMEA is **not a mandatory timeline item**. A solution-risk analysis/FMEA is added during Improve/Control only if the selected intervention creates failure modes for which systematic risk prioritization is useful.

---

## Gantt chart

```mermaid
gantt
    title Bachelor End Project - Hytech-Pommec
    dateFormat  YYYY-MM-DD
    axisFormat  %d-%m
    tickInterval 1week
    weekday monday
    excludes weekends

    section DEFINE
    Project kick-off                         :done, d1, 2026-08-17, 1d
    Shadowing and initial process mapping    :done, d2, 2026-08-17, 5d
    AS-IS validation and SOP integration     :done, d3, 2026-08-21, 4d
    Workload framework and Measure protocol  :done, d4, 2026-08-25, 2d
    Define tollgate                          :milestone, done, dm, 2026-08-26, 0d

    section MEASURE
    Pilot Measurement Protocol               :done, m1, 2026-08-28, 1d
    Pilot review and protocol v1.1 freeze    :done, m2, 2026-08-28, 1d
    First baseline session and v1.2 freeze   :done, m2b, 2026-08-31, 1d
    Second baseline day                      :done, m2c, 2026-09-01, 1d
    Protocol v1.3 internal control           :done, m2d, 2026-09-02, 1d
    Supervisor Measure-method review         :milestone, crit, m2e, 2026-09-03, 0d
    Baseline window - target 5 distinct days :crit, m3, 2026-08-31, 8d
    Daily cleaning and enrichment            :crit, m4a, 2026-08-31, 8d
    Coverage review and extension decision   :milestone, crit, m3a, after m3, 0d
    Cross-day summaries and Measure closure  :crit, m4b, after m3a, 3d
    Measure tollgate                         :milestone, crit, mm, after m4b, 0d

    section ACADEMIC DELIVERABLES
    Confirm final TU/e completion dates      :milestone, crit, ad0, 2026-09-03, 0d
    Half-page project description            :milestone, ad1, 2026-09-15, 0d
    PoW Parts A+B - proposal and Gantt       :crit, ad2, 2026-09-07, 10d
    PoW Part C - professional reflections    :crit, ad2b, 2026-09-07, 10d
    Internal complete draft                  :milestone, crit, ad2c, 2026-09-18, 0d
    Official Plan of Work draft deadline     :milestone, crit, ad3, 2026-09-20, 0d
    Scientific-conduct declaration           :ad3b, 2026-09-21, 1d
    Supervisor feedback and revision         :crit, ad4, 2026-09-21, 5d
    Internal final package ready             :milestone, crit, ad4b, 2026-09-25, 0d
    Official final Plan of Work submission   :milestone, crit, ad5, 2026-09-27, 0d

    section ANALYZE
    Workload profile and candidate evidence  :crit, a1, after m4b, 5d
    Selection model freeze                   :milestone, crit, a1b, after a1, 0d
    Root-cause analysis and candidate scoring:crit, a2, after a1b, 5d
    Targeted Exact/Orbis feasibility         :crit, a3, after a1, 5d
    Benchmark and ground-truth feasibility   :a4, after a1, 5d
    Sensitivity analysis and focal-case gate :milestone, crit, a5, after a2 a3 a4, 0d

    section IMPROVE / DSRM
    Artifact requirements and objectives     :crit, i1, after a5, 5d
    Define workload endpoint and guardrail   :crit, i1b, after i1, 3d
    Evaluation protocol freeze               :milestone, crit, i1c, after i1b, 0d
    Artifact and TO-BE design                :crit, i2, after i1c, 7d
    Prototype and development                :crit, i3, after i2, 15d
    Demonstration and refinement             :i4, after i3, 5d
    Artifact ready for evaluation            :milestone, crit, i6, after i4, 0d

    section EVALUATE
    Current-practice vs AI evaluation        :crit, e1, after i6, 10d
    Analyze evaluation results               :crit, e2, after e1, 5d
    Evaluation complete                      :milestone, crit, e3, after e2, 0d

    section CONTROL AND THESIS
    Conditional solution risk analysis FMEA :c2, after i2, 3d
    Control plan and safeguards              :c1, after e2, 5d
    Thesis writing and evidence integration  :t1, 2026-09-01, 2026-12-18
    Integrate final evaluation results       :crit, t2, after e2, 7d
    Final review revisions and handover      :crit, t3, after t2, 7d
    Company placement outer boundary         :milestone, crit, t4, 2027-01-07, 0d
```

The axis deliberately uses the numeric format `DD-MM` rather than abbreviated month names. Some embedded Mermaid renderers can display `%b` literally instead of converting it to a month abbreviation. Weekly ticks start on Monday to keep the chart readable when imported into draw.io.

---

## Critical-path logic

The main dependency chain is:

`Pilot → v1.2/v1.3 controlled baseline → five-day coverage review → workload/candidate analysis → targeted Exact/Orbis feasibility → veto gates + weighted/sensitivity-tested focal-case selection → evaluation-protocol freeze → artifact design/development → held-out evaluation → final thesis integration / handover`

The Plan of Work is developed **in parallel** with Measure/Analyze and should use the strongest evidence available at each submission milestone. The TU/e template requires a defensible prospective research method and detailed Gantt; it does not state that the focal use case must already be selected. Therefore the 27 September submission and a later focal-case gate are compatible only if the Plan of Work predefines the candidate population, veto/score method, evidence, decision owner, fallback and evaluation-freeze milestone. A provisional shortlist before submission is preferable.

The 7 January 2027 milestone is an **outer contractual boundary, not a required finish date**. If the artifact, evaluation, thesis/handover obligations and academic/company agreements allow it, the project may conclude earlier.

## DMAIC tollgate interpretation

| Tollgate | Planned evidence / decision |
|---|---|
| **Define → Measure** | AS-IS stable enough, scope/workload construct defined, protocol ready for pilot. |
| **Pilot → baseline** | Observation sheet usable; timing/task-switch rules workable; v1.3 sampling/coverage and private-repository governance controlled without changing live fields. |
| **Measure → Analyze** | Five distinct observation days plus a passed Day-5 coverage review; representative activity-family workload profile, with detailed Task-ID enrichment where justified, plus windows, net/coded-active time, case mix and limitations. |
| **Analyze → Improve** | Focal activity passes the non-compensable gates and wins/stays credible under pre-agreed weighted scoring and sensitivity analysis; supervisor aligned. |
| **Improve → Control** | Workload endpoint, meaningful threshold, quality rubric/guardrail and held-out evaluation design frozen before development/formal testing; artifact evaluated and implementation controls defined. |

## Recommended visual-editing workflow: draw.io / diagrams.net

For this **Gantt chart**, draw.io is the preferred visual editor.

1. Open **app.diagrams.net**.
2. Create a new diagram and store it in Google Drive or OneDrive if you want a shareable collaborative file.
3. Choose **Arrange → Insert → Mermaid** (or `+ → Mermaid`, depending on the editor version).
4. Copy only the Mermaid code inside the fenced block above.
5. Keep the default **Diagram** option so the result is inserted as native draw.io shapes rather than a static SVG image.
6. If the inserted diagram behaves as one locked Mermaid group, click the **unlock** icon or right-click and **Ungroup** when you want completely independent shape editing. Ungrouping removes the stored Mermaid source from that group, so keep the GitHub source as the canonical code version.
7. Adjust labels, positions, sizing and styling visually.
8. Share the Drive/OneDrive diagram link with the supervisor.

### Lucidchart limitation for this Gantt

Lucid can render Mermaid Gantt syntax, but Mermaid diagrams created through Lucid's **diagram-as-code / Mermaid editor** are rendered as an image and are edited by changing the code. Lucid also has a newer direct-paste feature that converts supported Mermaid elements into native Lucid shapes; however, unsupported elements/features are retained as static SVGs. In practice, a Gantt may therefore not become fully shape-editable even when the same Mermaid code renders correctly.

For that reason, use **draw.io as the supervisor-facing visual master** for this Gantt rather than relying on Lucid for direct bar-by-bar editing.

### Important synchronization rule

The Mermaid version in GitHub is the **planning source** until a visually edited draw.io copy becomes the supervisor-facing master. Once extensive manual visual edits are made in draw.io, do not assume that regenerating from Mermaid will preserve every manual position. If dates/dependencies change materially, update both the GitHub planning source and the supervisor-facing diagram.

## Items that are deliberately provisional

The following should be revised as evidence becomes available rather than treated as fixed promises:

- whether the two completed partial days count as two of the five distinct observation days and whether the Day-5 coverage review requires targeted extension;
- exact Analyze duration;
- artifact-development duration (depends strongly on selected case);
- evaluation duration and participant/case requirements after the predevelopment protocol freeze;
- whether the project finishes before the 7 January 2027 contractual boundary;
- Part D signing/logistics and the official final BEP submission/presentation date if different from the company contract;
- whether FMEA is useful for the selected intervention.

The fixed dates currently known are the **15 / 20 / 27 September 2026 academic milestones** documented in the 25 August supervisor meeting notes and the **7 January 2027 Hytech-Pommec contract end**.
