# Documentation Map — Bachelor End Project

**Last synchronized:** 24 August 2026

This folder follows a **one topic, one authoritative owner** rule. Other files should link to the owner instead of repeating the same current interpretation.

## Current authoritative files

| Topic | Authoritative file | Owns |
|---|---|---|
| Final proposal | `proposal/BEP_Assignment_1BEPIEX_Final.docx` | Approved/current BEP assignment |
| AS-IS operational process | `process/Process_Cleaned_V1.0.md` | Scope, workflow, evidence, Step / Task Register, unresolved current-process facts |
| Research methodology and candidate selection | `methodology/Phase_1_Current_Methodology.md` | DMAIC/DSRM, measurement design, candidate portfolio, selection gates, evaluation logic, research actions |
| Workload definition | `methodology/Workload_Definition.md` | Canonical workload construct based on Young et al. (2015) |
| Formal company evidence | `company-documentation/Official_Document_Register_2026-08-21.md` | What received SOPs/forms/work instructions formally support |
| TO-BE working hypothesis | `process/TO_BE_Working_Hypothesis_v0.1.md` | Provisional future-state architecture and technology-allocation logic |
| Literature register | `../literature/README.md` | Literature list, use status and where each source supports the BEP |

## Historical evidence

### `meetings/`

Dated observation and meeting notes are historical snapshots. They may contain questions that were open on that date but have since been resolved. Do not rewrite them to match later knowledge.

### `research-notes/`

Earlier working material is retained for traceability but is not authoritative for current process, methodology, candidate status or open questions.

## Synchronization rule

When new evidence arrives:

1. preserve the dated observation/meeting record as historical evidence;
2. identify the **single authoritative owner** for the new fact;
3. update that owner;
4. update other files only when their own content genuinely changes;
5. replace duplicated explanations with a reference to the authoritative file;
6. remove resolved items from active open-question or decision-gate lists.

Examples:

- a newly understood Exact step → update the AS-IS process file;
- a change in candidate priority → update the methodology file only;
- a change in the workload construct → update `Workload_Definition.md`;
- a new SOP/WI → update the formal-document register;
- a revised future-state design → update the TO-BE hypothesis.

This rule is intended to prevent the repository from drifting into multiple conflicting versions of the same project status.