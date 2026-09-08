# Academic Supervisor Meeting Notes — 10 June 2026

## 1. Meeting overview

- **Date:** Wednesday, 10 June 2026
- **Attendees:** Yijie Wang; supervisor name not specified in the source document
- **Topic:** Aligning the Hytech-Pommec internship assignment, *“Stagiair(e) HBO/WO — AI & Procesoptimalisatie Inkoop”*, with the research group's direction for the Bachelor End Project.
- **Source:** `Meeting notes supervisor 2026-06-10.docx`
- **Record status:** Extracted from the original meeting-note document. This file preserves the source framing and does not update the meeting with later project decisions.

## 2. Key points discussed

### Overall direction

The company assignment should be matched to the research group's direction.

The source describes the intended sequence as:

`literature review of the purchasing process → possibly introduce agent-based simulation built on that process`

The company side was described as asking for:

- process analysis;
- AI application scan;
- optimisation proposal;
- implementation advice.

The meeting notes state that a simulation study could potentially provide evidence for these deliverables.

### Methodology

The BEP should be **quantitative research**.

The meeting notes specifically emphasize:

- measurable outcomes;
- an experimental or simulation-based design;
- statistical analysis;
- not producing only a qualitative/advisory internship report.

### Research-group context: LLMs and decision making

The research group was described as studying how AI / large language models influence human decisions.

One example discussed was the effect of stated model certainty, such as an AI saying it is “95% certain,” on how strongly people follow its advice. The notes also state that people generally over-estimate LLM confidence.

### Deviating from the AI optimum

A warehouse example was discussed:

- AI prescribes an optimal pick route, for example aisle `1 → 3 → 5`;
- the worker instead follows `1 → 5 → 3` because aisle 5 is closer;
- the worker therefore deviates from the prescribed optimum because following the prescribed route may not align with the worker's own interests.

The research direction discussed was to:

1. observe such deviations;
2. use them to compute a new behaviour-aware optimum that anticipates actual behaviour.

The purchasing analogue mentioned in the source is **maverick buying**, where buyers ignore prescribed suppliers or contracts.

### Design idea for the BEP

If the AI agent produces a purchasing proposal, the **platform / LLM on which the agent runs** could be treated as a decision variable.

The source proposes:

- provide identical purchasing cases to agents on different platforms;
- compare their purchasing proposals quantitatively.

### Supervision logistics

The supervisor might be on exchange in Paris during **September–October 2026**, which could reduce availability.

The notes therefore state that:

- the proposal and study design should be agreed before September;
- supervision during September–October may need to be asynchronous.

## 3. Working BEP design recorded in the source

The source summarizes the discussion into one possible coherent design:

```text
Map Hytech-Pommec purchasing process
(literature + company analysis)
        ↓
Build LLM agents for one well-defined purchasing task
        ↓
Use standardized purchasing cases
        ↓
Run a quantitative simulation experiment
with LLM platform as the main factor
        ↓
Translate findings into the company's advice report
```

The following behavioural topics were recorded as an **optional extension layer**:

- stated certainty;
- algorithm aversion;
- maverick buying;
- re-optimising around observed deviations;
- what happens to performance when buyers only partly follow the agent's proposals.

## 4. Action items recorded in the source

| Action | Timing / note |
|---|---|
| Draft the research proposal and discuss it with the supervisor | Well before September; source notes that draft v0.1 had been prepared |
| Read the starting literature | Also check whether the literature mapping in the source accurately reflects what the supervisor meant |
| Confirm the BEP 2026-A timeline | Official start/end dates and defense window |
| Confirm company start date / contract status | Open at the time of the meeting |
| Agree the September–October supervision arrangement | Written weekly updates, video calls and possibly a second group contact |
| Ask Hytech-Pommec what data are available for realistic purchasing cases | Examples in source: ERP purchase orders, supplier quotes, lead times, approved supplier list |
| Clarify confidentiality rules for company data | Open at the time of the meeting |

## 5. Literature mapping included in the original notes

The original document contains a section titled **“Literature matching the supervisor's references”** and explicitly labels these as **likely sources** behind the points mentioned in the meeting. The source does not establish that the supervisor personally confirmed each citation.

| Topic mentioned in meeting | Likely literature listed in the source |
|---|---|
| “95% certainty” / stated confidence affects reliance | Steyvers et al. (2025), *Nature Machine Intelligence*; Kim et al. (2024), ACM FAccT |
| Workers do not follow the AI optimum | Dietvorst et al. (2015), *JEP: General*; Elbert et al. (2017), *Computers & Industrial Engineering* |
| Use deviations to establish a new optimum | MIT–Amazon Last-Mile Routing Challenge; *Learning from Drivers* (2022) |
| Similar phenomenon in purchasing | Karjalainen et al. (2009), *Journal of Business Ethics* — maverick buying |
| Agent simulation in purchasing / supply chain | *LLMs for Supply Chain Management* (2025); *Agentic LLMs in the Supply Chain*, IJPR (2025) |
| Different platforms decide differently | *LLM Consistency: Stated vs. Revealed Preferences* (2025) |

The original notes state that the literature links had been checked on 10 June 2026.

## 6. Historical interpretation boundary

This file is a **dated historical evidence record**.

It should not be read as the current project methodology or final artifact design. The June meeting captured an early direction centred on quantitative experimentation, simulation and LLM-agent comparison. Later project decisions should remain documented in their own dated meeting notes and current methodology files rather than being back-written into this record.
