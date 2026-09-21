# Measure scope and classification addendum

Prepared 14 September 2026. Applies the scope decisions recorded on 10 September. The phase crosswalk and operational rules below are researcher implementation choices for review, not additional decisions attributed to the supervisor.

**21 September classification addition:** The [stage-organized analytical activity list](../process/Purchasing_Activity_Framework_2026-09-21.md) is now the current reference for detailed activity assignments. This addition implements the framework-guided classification direction discussed on 17 September. It retains the original 14 September scope decisions and changes no live fields, timing rules, original observation rows or research questions.

## Scope

The primary objective remains reducing the operational buyer's workload while maintaining purchasing quality. Include Dennis's tactical purchasing work in the process investigation. Keep observations identifiable by actor and role. Dennis's evidence need not match Arno's quantity, but must support interpretable patterns in the relevant work.

Logistics is outside the thesis. EXC time is excluded from the thesis Measure analysis and EXC cannot become the focal improvement case, as directed on 10 September. The earlier exception allowing logistics into detailed scope when it creates buyer rework is superseded. The existing broad raw records remain source evidence.

## Applying the exclusion

1. Preserve every original observation, activity label, timestamp and source note. Apply exclusions in a separate derived dataset.
2. Mark an episode originally coded EXC as `EXCLUDE_EXC` for the thesis timed workload profile and candidate selection. Apply this common scope to historical records when comparing them with later observations. This is a retrospective analytical filter, not a claim that the narrower scope governed the original collection.
3. From the next observation, do not time EXC as a thesis work family. Record when observation of eligible work pauses and resumes, so excluded activity does not enter the duration of an adjacent PO or other episode. A session exclusion interval is exposure bookkeeping, not an EXC workload measure.
4. Keep scope separate from work-family coding. A SEND or PO episode that demonstrably belongs to an excluded logistics or EXC aftercare activity is also excluded. If its purpose is unclear, mark `REVIEW_SCOPE` and resolve it from the source or a targeted question. Do not exclude an entire case merely because one episode is EXC, and do not retain excluded aftercare merely because another episode is labelled SEND.
5. Do not relabel historical EXC as CLAR, CHECK, SEND or PO to make it eligible. Correct a genuine transcription error only with a dated source-based correction.
6. Preserve explicit data-quality exclusions independently of scope. For 8 September, both timed OBS-16 rows remain excluded under the student's contamination note. Unknown time is missing, not zero.

Historical EXC included Finance questions, tracing, cancellations and other exceptions as well as logistics-related work. It is therefore not equivalent to either the logistics department or Van Weele stage 6. The supervisor's EXC exclusion is a scope rule; it is not a theoretical definition of nazorg.

## Van Weele coding

Use the [Purchasing activity framework of 21 September](../process/Purchasing_Activity_Framework_2026-09-21.md) for the current analytical activity list. The [14 September mapping](../process/Van_Weele_Activity_Mapping_2026-09-14.md) remains a historical crosswalk reference. The current list starts from concrete tasks and organizes their analytical labels around the purchasing stages; it is not a replacement live codebook.

Preserve the seven current live families: **REQ, CLAR, DEC, PO, CHECK, SEND and OTHER**. The historical eighth family, **EXC**, remains traceable in earlier or retained source records and subject to the scope exclusion above. A work family provides a broad live description; an analytical activity identifies the task's purchasing purpose within the framework. Record full analytical activity labels after the session rather than requiring additional live codes.

The design chain runs from exploratory observations to the AS-IS task inventory, then to literature-informed observation and pilot refinement, broad live families, the addition of Dennis's relevant context, and the framework-guided analytical list requested on 17 September. Row enrichment connects those records to stage-and-task analysis. Van Weele organizes purchasing activities; it does not originate or validate the measurement instrument. The [method justification](Measurement_Method_Justification.md) explains the evidence and local adaptations.

The supervisor requested a list guided by the framework and distinct categories for similar actions at different stages. Retaining seven live families and applying the detailed labels afterward is the researcher implementation adopted here, not an additional supervisor-validated method. No cited source prescribes or validates the exact number seven.

### Derived record, updated 21 September

`Observation date | Actor | Source file | Source row | OBS ID | Original family | Task ID | Register status | Task confidence | Van Weele stage | Stage confidence | Analytical activity | Activity confidence | Assignment reason | Scope status | Scope reason | Timing status`

Stage values are `VW1` to `VW6`, `MULTI`, `UNKNOWN` and `NA`. Use `MULTI` only when evidence supports several stages within an inseparable episode, and `UNKNOWN` when the purpose is unclear. `NA` is for an event outside purchasing-stage classification, such as a break. Keep register status `Mapped`, `U`, `Mixed` or `Unresolved` separate from confidence: insufficient detail is not evidence that work lies outside the register.

The three confidence fields are independent. `C` means confident, `P` provisional and `?` unresolved, applied separately to the Task ID, purchasing stage and analytical activity. A supported stage does not establish a detailed activity. A supported activity may lack a Task ID when the operational register does not cover it.

| Added field | Rule |
|---|---|
| **Analytical activity** | Use the full activity label from the current framework. For inseparable work, retain an explicit combined description naming only supported activities. Leave the activity unresolved when the evidence does not support a label; do not force a familiar family into one stage. |
| **Activity confidence** | Assess the specific activity assignment independently of task and stage confidence. Uncertainty about a detailed activity does not erase reliably observed work. |
| **Assignment reason** | State the source fact or case context that supports the activity label and any unresolved boundary. Keep this distinct from the scope reason and timing-quality explanation. |

Map by the purpose of the work, not by the employee, software screen, activity code or the last word in the note. Do not split a timed episode across tasks, activities or stages without observed boundaries. Combined work keeps its minutes once; an inseparable episode spanning evidenced stages remains `MULTI`. Do not duplicate minutes, distribute them equally across labels, or split them by line count. A new classification does not create a new timed observation or unique case.

An `UNKNOWN` stage or unresolved analytical activity does not itself exclude reliable, in-scope family-level time. Use `REVIEW_SCOPE` only when eligibility is genuinely unclear. Preserve original task numbering/version where it differs from the current register, original family labels, recorded intervals and source-row order. Label retrospective assignments as later researcher enrichment rather than implying that those fields were collected live.

### Timing continuity

This update leaves the existing active-time, interruption, tally and non-fabrication rules unchanged. The 17 September proposal to record overlapping activity durations separately is not implemented by the activity-list revision. Do not retrofit overlapping intervals or add gross concurrent durations to the historical exclusive active-time baseline. A future timing change requires a dated definition and a comparability assessment.

## Measures and denominators

These outputs describe recorded occurrence and time requirements. The broader workload profile also uses qualitative task evidence, and purchasing quality requires a separate activity-specific assessment.

| Output | Numerator | Denominator and reporting rule |
|---|---|---|
| Within-scope active-time share | Reliable, eligible minutes for the family, analytical activity or stage | All reliable, eligible timed minutes for that actor. Report unresolved, combined and multi-stage minutes separately; distinguish provisional assignments. Label the result as a share of included timed work. |
| Activity occurrence rate | Eligible recorded episodes or events | Known net observation hours for the same actor and collection window. State whether excluded-scope intervals are included in exposure. Do not merge rates based on different exposure definitions. |
| Duration of an episode | Reliable active minutes | Eligible timed episodes of a comparable task. An interrupted case may contain several episodes. |
| Case active time | Sum of reliable eligible episodes for a linked case | Cases with adequate observed coverage. Use date plus OBS ID. Report partial cases separately. |
| Active time per line | Reliable active minutes for a comparable task | Relevant processed lines where that volume is known. Do not confuse newly added lines with the final PO line count. |

If total net exposure is known but the narrower exposure cannot be reconstructed, report the original exposure explicitly and restrict comparisons to that common definition. Do not silently replace 351 historical net minutes or 265 historical timed minutes with narrower totals. Recalculate and label the scope-specific results first. Those historical totals cover 31 August and 1 September only.

Keep Dennis and Arno in separate profiles. Pooling their minutes would change the primary outcome and give more weight to whichever role was observed longer. EXC exclusion narrows what the thesis can conclude about workload; the included profile is not a complete account of all of Arno's work.

Report analytical-activity coverage alongside any activity summary. A subset of rows that can receive detailed labels is not a complete workload profile. Preserve known stages with unresolved activities, combined episodes and eligible family-only evidence in the denominator and coverage accounting instead of discarding them silently.

## Sources

- [Academic decisions of 10 September](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md), especially EXC scope and Dennis data sufficiency.
- [Academic decisions of 3 September](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-03.md), especially preservation of raw data, observation sufficiency and analysis denominators.
- [Measurement Protocol v1.3](Measurement_Protocol_v1.3.md), retained for timing, interruption and non-fabrication rules except where this addendum changes the scope.
- [8 September observation](Measure_Observation_2026-09-08.md), including the OBS-16 exclusion.
- [Academic meeting of 17 September](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-17.md), especially the framework-guided activity-list direction and the separate proposed timing treatment.
- [Purchasing activity framework of 21 September](../process/Purchasing_Activity_Framework_2026-09-21.md), the current analytical labels and assignment boundaries.
- [Measurement method justification](Measurement_Method_Justification.md), including the development chain and the distinction between published observation principles and local choices.
