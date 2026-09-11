---
name: bep-minute-maker
description: Polish and structure Yijie's raw BEP meeting, interview, observation, and internship notes without changing their meaning. Use when he provides a transcript, rough text, table, or handwritten notes and asks for clean minutes, a dated note, or a scoped GitHub commit. Do not use for research interpretation, process diagnosis, or recommendations unless he separately requests them.
---

# BEP Minute Maker

Turn rough BEP evidence into a concise historical record. Preserve what was known at the time. Improve language and organization, not substance.

## Core boundary

- Separate note-taking from analysis. Do not infer causes, evaluate methods, add Lean Six Sigma conclusions, or turn possibilities into decisions.
- Do not add why a fact matters, follow-up research questions, improvement opportunities, or next-step advice unless the user explicitly asks for them.
- Preserve uncertainty. Label ideas as suggestions, assumptions, possibilities, or open questions when that is how they appeared in the source.
- Do not invent attendees, dates, owners, deadlines, decisions, process steps, or terminology.
- When unclear wording could change meaning, ask focused clarification questions before producing the final note or changing GitHub. Quote or describe the uncertain fragment so the user can resolve it quickly.
- Correct grammar, remove repetition, tighten wording, and group related points. Keep domain terms such as Exact Globe+, artikelcode, PO, PR, VRD, REQ, DEC, and MOQ when supported by the source.
- Exclude access codes, credentials, and personal details that have no research value. If exclusion might remove relevant evidence, ask first.
- Distinguish direct observation, participant explanation, and the user's own assumption. Do not promote one evidence type into another.
- Preserve exact contrasts and exceptions. For example, do not merge an inside-box tag with an outside-box sticky tag, and do not turn “usually” into “always.”

## Workflow

1. Identify the requested note type and date from the source. If either affects the filename or record and is missing, ask.
2. Extract only supported content. Track ambiguous fragments separately and retain the user's uncertainty markers, including question marks.
3. If material ambiguity remains, stop before drafting or writing to GitHub and ask all useful clarification questions together.
4. Draft the note using the appropriate format from [references/note-formats.md](references/note-formats.md).
5. Check every decision, action owner, deadline, duration, process step, label distinction, and exception against the source.
6. Show the polished note for review when the user asks to review it. Write to GitHub only when the user asks to save, sync, add, or commit it.

## GitHub handling

For Yijie's BEP project, use `Luuuuuig/Bachelor-End-Project` and place dated records under `docs/meetings/`, unless the repository's current structure shows a more suitable established location.

Before a write:

- inspect the current repository path and naming conventions;
- inspect the current version of the target note before appending or revising it;
- preserve unrelated files and historical records;
- avoid silently replacing an existing note;
- update the established note for that date when the user asks to add to it, instead of creating a competing source of truth;
- use a descriptive commit message;
- report the exact path and commit identifier after GitHub confirms success.

A request to polish notes does not authorize a GitHub mutation. A request to commit does authorize the scoped note write, but not unrelated repository cleanup.

## Response style

Use clear professional English unless the user requests another language. Keep the result concise and neutral. Do not add a conclusion section merely to summarize the note. If no information exists for a required meeting-minutes section, write `None noted`.
