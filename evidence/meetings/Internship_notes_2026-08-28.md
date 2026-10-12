# Internship Notes — 28 August 2026

**Main focus:** Measure-phase pilot, measurement-system review, and baseline preparation.

## Work completed today

### 1. Ran the first live Measure pilot

A live observation pilot was carried out with the operational buyer from approximately **09:36–12:10**, with a break from **10:02–10:35**.

The purpose was not to create a representative workload baseline yet, but to test whether the measurement protocol could be used reliably in real work.

The pilot showed that:
- purchasing cases are highly fragmented by emails, phone calls, colleague questions, missing information and case switching;
- the same case can return several times after being interrupted or parked;
- direct live coding against the detailed 31-task register is too granular for one observer to use reliably while also recording time, interruptions, outcomes and qualitative cues;
- some operational work did not fit the existing detailed register cleanly, especially clarification, PO aftercare, technical drawing/specification retrieval and order-status tracing;
- case identity was lost twice because returning cases were given new OBS numbers;
- some information became unrecoverable soon after the session, confirming the need for immediate post-session enrichment;
- missed observations must be recorded explicitly rather than silently omitted.

The detailed cleaned pilot record is maintained separately in:
`Pilot_Measure_Observation_2026-08-28.md`.

### 2. Changed the live measurement architecture

The 31-task register remains the detailed AS-IS process model, but it will no longer be used as the primary live coding layer.

The official live categories are now:

- `REQ` — new purchasing request;
- `CLAR` — clarification / investigation / missing information;
- `DEC` — purchasing decision / maximalisatie / hold;
- `PO` — create/change/prepare/process PO in Exact;
- `CHECK` — price / confirmation / information verification;
- `SEND` — forwarding/sending purchasing communication;
- `EXC` — aftercare / tracing / rework / exception;
- `OTHER` — relevant purchasing work that does not yet fit.

The live sheet is simplified to:

`Case | Activity | Start | End | Volume | INT | Result / short note`

Detailed Task IDs are added after the observation session only where the evidence supports the mapping.

### 3. Refined TIME / TALLY logic

The pilot and follow-up discussion clarified that:
- `REQ` is normally **TALLY**, because recognition/intake often happens within seconds;
- `DEC` is normally **TALLY + outcome**, because many decisions are made very quickly;
- `CLAR` is **TIME IF**, because clarification may take only seconds or may become a long investigation;
- `PO` and `CHECK` are normally **TIME**;
- `SEND` is **TIME** because repetitive manual forwarding can contribute to capacity use;
- `EXC` is **TIME IF**, because exception work varies greatly in duration.

This avoids false precision for fast cognitive decisions while preserving measurable active-processing time where duration is meaningful.

### 4. Corrected key measurement rules

The baseline protocol now explicitly states:
- a substantial interruption that stops active work is counted on the segment being left;
- system waiting is not active buyer time;
- unrelated non-purchasing email/work is not assigned an OBS case;
- if unrelated work interrupts active purchasing, the active segment is closed and `INT=1` is recorded;
- `J` means observable judgement/decision and `EXP` separately means observable experience/tacit-knowledge evidence;
- the same purchasing case keeps the same OBS number even when it returns later;
- `MISS` is used when the observer cannot keep up instead of reconstructing unsupported details afterward;
- every official session must record the observation window, breaks, net observed time and contextual notes;
- rework during live observation is reported as occurrence/time rather than an invalid percentage using unmatched cases;
- very small timed samples are treated as exploratory rather than as stable representative estimates.

### 5. Froze Measurement Protocol v1.1

`Measurement_Protocol_v1.1.md` was created as the official baseline-ready protocol following the pilot.

A compact `Measure_Live_Cheat_Sheet_v1.1.md` was also created for use beside the live sheet during observation.

Official exploratory baseline observations are planned to begin on **31 August 2026**.

### 6. Reviewed procurement-dashboard information provided by Johan

Johan provided a procurement dashboard view. The dashboard demonstrates that company/system data can provide useful transactional-volume context, such as PO counts and PO-line counts, while live observation captures human work that the dashboard cannot show, such as clarification, interruptions, judgement, expertise dependence and exception handling.

The current plan is therefore to combine:
- **live observation** for active work and qualitative/contextual evidence; and
- **approved aggregated/system information** for transactional volume where Johan can provide it.

Direct dashboard access is not required to start the official observation baseline.

No raw supplier-level commercial dashboard data is stored in the repository as part of this note.

### 7. Reorganized Measure documentation

A dedicated `docs/measurement/` folder was created to keep Measure-phase data-collection materials separate from the broader methodology folder.

The folder contains:
- historical Measurement Protocol v1.0;
- current frozen Measurement Protocol v1.1;
- Measure Live Cheat Sheet v1.1;
- a folder README explaining ownership and links.

Repository navigation, methodology references, the project timeline and the pilot note were updated to point to the new measurement folder.

## Current status at end of day

The pilot has been completed and the measurement system has been revised based on observed usability problems.

The project is now ready to move from pilot testing into the official exploratory Measure baseline, subject to preparing the practical blank observation sheet and starting the planned observation sessions.

## Next actions

1. Prepare the blank live observation sheet for Monday with no example rows.
2. Keep a simple running OBS case index during each session.
3. Start official baseline observations on 31 August 2026.
4. Perform post-session Task-ID enrichment immediately after each observation block.
5. Record `MISS`, `INT`, `J` and `EXP` consistently.
6. Ask Johan whether approved aggregated PO/PO-line data by week/month can be provided.
7. Continue observing different days/dayparts until the baseline has sufficient coverage of routine work, interruptions, clarification, exceptions and relevant candidate activities.
8. Do not freeze a final focal AI/artifact case until Measure evidence and subsequent Analyze-stage feasibility support it.
