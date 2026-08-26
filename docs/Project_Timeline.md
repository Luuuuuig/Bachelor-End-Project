# Project Timeline / Gantt — Bachelor End Project

**Status:** Current planning draft, synchronized 26 August 2026.

**Purpose:** This file is the project-planning companion to `Project_Charter.md`. It turns the current DMAIC/DSRM sequence, supervisor milestones and known dependencies into a shareable Gantt chart. The Mermaid source can be copied into draw.io / diagrams.net for visual editing.

## Planning assumptions

- Project start: **17 August 2026**.
- Hytech-Pommec contract end / latest company-placement boundary: **7 January 2027**. The BEP/company work may finish earlier if the required project activities are completed and this is agreed with the relevant parties.
- Current project state: **Define largely complete; exploratory Measure begins with the next-working-day pilot**.
- Pilot: planned for **27 August 2026**; if the actual next working day changes, move this task and all dependent Measure tasks accordingly.
- The baseline observation window below is **provisional**. The exact observation coverage/sample window must be frozen after the pilot according to `methodology/Measurement_Protocol_v1.0.md`.
- Detailed Exact/Orbis production-data/interface feasibility is intentionally scheduled in **Analyze, after the exploratory Measure baseline**.
- Supervisor milestones from the 25 August meeting are fixed: **15 September half-page project description; 20 September Plan of Work draft; 27 September final Plan of Work submission**.
- Weekly academic supervision: **Thursday 15:00–16:00**, with agenda prepared/sent on Wednesday.
- Durations after Measure are **planning estimates**, because the final artifact and evaluation design depend on the selected focal case.
- FMEA is **not a mandatory timeline item**. A solution-risk analysis/FMEA is added during Improve/Control only if the selected intervention creates failure modes for which systematic risk prioritization is useful.

---

## Gantt chart

```mermaid
gantt
    title Bachelor End Project — Hytech-Pommec
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    excludes    weekends

    section DEFINE
    Project kick-off                         :done, d1, 2026-08-17, 1d
    Shadowing and initial process mapping    :done, d2, 2026-08-17, 5d
    AS-IS validation and SOP integration     :done, d3, 2026-08-21, 4d
    Workload framework and Measure protocol  :done, d4, 2026-08-25, 2d
    Define tollgate                          :milestone, done, dm, 2026-08-26, 0d

    section MEASURE
    Pilot Measurement Protocol               :crit, m1, 2026-08-27, 1d
    Pilot review and protocol freeze          :crit, m2, after m1, 2d
    Exploratory baseline observation          :crit, m3, after m2, 8d
    Clean/code data and create task summaries :crit, m4, after m3, 3d
    Measure tollgate                          :milestone, crit, mm, after m4, 0d

    section ACADEMIC DELIVERABLES
    Half-page project description             :milestone, ad1, 2026-09-15, 0d
    Plan of Work drafting                     :crit, ad2, 2026-09-07, 10d
    Plan of Work draft to supervisor          :milestone, crit, ad3, 2026-09-20, 0d
    Supervisor feedback and revision          :ad4, 2026-09-21, 5d
    Final Plan of Work submission             :milestone, crit, ad5, 2026-09-27, 0d

    section ANALYZE
    Workload profile and candidate evidence   :crit, a1, after m4, 5d
    Root-cause and candidate analysis          :crit, a2, after a1, 5d
    Targeted Exact/Orbis feasibility           :crit, a3, after a1, 5d
    Benchmark / ground-truth feasibility       :a4, after a1, 5d
    Focal case selection and supervisor gate   :milestone, crit, a5, after a2 a3 a4, 0d

    section IMPROVE / DSRM
    Artifact requirements and objectives       :crit, i1, after a5, 5d
    Artifact / TO-BE design                    :crit, i2, after i1, 7d
    Prototype / development                    :crit, i3, after i2, 15d
    Demonstration and refinement               :i4, after i3, 5d
    Evaluation protocol freeze                 :crit, i5, after i3, 5d
    Artifact ready for evaluation              :milestone, crit, i6, after i4 i5, 0d

    section EVALUATE
    Evaluation / current-practice comparison   :crit, e1, after i6, 10d
    Analyze evaluation results                 :crit, e2, after e1, 5d
    Evaluation complete                        :milestone, crit, e3, after e2, 0d

    section CONTROL AND THESIS
    Control plan and implementation safeguards :c1, after e2, 5d
    Conditional solution risk analysis / FMEA  :c2, after i2, 3d
    Thesis writing and evidence integration    :t1, 2026-09-01, 2026-12-18
    Integrate final evaluation results         :crit, t2, after e2, 7d
    Final review / revisions / handover         :crit, t3, after t2, 7d
    Company placement outer boundary           :milestone, crit, t4, 2027-01-07, 0d
```

---

## Critical-path logic

The main dependency chain is:

`Pilot → Measurement protocol freeze → workload baseline → workload/candidate analysis → targeted Exact/Orbis feasibility → focal-case selection → artifact design/development → evaluation → final thesis integration / handover`

The Plan of Work is developed **in parallel** with Measure/Analyze and should be updated with the strongest evidence available at the time of each submission milestone.

The 7 January 2027 milestone is an **outer contractual boundary, not a required finish date**. If the artifact, evaluation, thesis/handover obligations and academic/company agreements allow it, the project may conclude earlier.

## DMAIC tollgate interpretation

| Tollgate | Planned evidence / decision |
|---|---|
| **Define → Measure** | AS-IS stable enough, scope/workload construct defined, protocol ready for pilot. |
| **Pilot → baseline** | Observation sheet usable; timing/task-switch rules workable; sampling/confidentiality rules frozen. |
| **Measure → Analyze** | Representative task-level workload profile with observation coverage, sample sizes and limitations. |
| **Analyze → Improve** | Focal activity selected based on workload, business relevance, standardizability, quality risk, expertise, technical/data feasibility and evaluation feasibility; supervisor aligned. |
| **Improve → Control** | Artifact evaluated with predeclared workload + quality measures; implementation controls defined. |

## How to edit visually in draw.io / diagrams.net

1. Open **app.diagrams.net**.
2. Create a new diagram and store it in Google Drive or OneDrive if you want a shareable collaborative file.
3. Choose **Arrange → Insert → Advanced → Mermaid** (menu wording can vary slightly by draw.io version).
4. Copy only the Mermaid code inside the fenced block above.
5. Insert it as an editable **Diagram**, not as a static image.
6. Adjust task labels, positions, sizing, styling and notes visually.
7. Share the Drive/OneDrive diagram link with the supervisor.

### Important synchronization rule

The Mermaid version in GitHub is the **planning source** until a visually edited draw.io copy becomes the supervisor-facing master. Once extensive manual visual edits are made in draw.io, do not assume that regenerating from Mermaid will preserve every manual position. If dates/dependencies change materially, update both the GitHub planning source and the supervisor-facing diagram.

## Items that are deliberately provisional

The following should be revised as evidence becomes available rather than treated as fixed promises:

- exact number of baseline observation days;
- exact Analyze duration;
- artifact-development duration (depends strongly on selected case);
- evaluation duration and participant/case requirements;
- whether the project finishes before the 7 January 2027 contractual boundary;
- official final BEP submission/presentation date if different from the company contract;
- whether FMEA is useful for the selected intervention.

The fixed dates currently known are the **15 / 20 / 27 September 2026 academic milestones** documented in the 25 August supervisor meeting notes and the **7 January 2027 Hytech-Pommec contract end**.
