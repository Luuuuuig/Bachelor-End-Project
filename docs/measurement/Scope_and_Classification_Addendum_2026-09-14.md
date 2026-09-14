# Measure scope and classification addendum

Prepared 14 September 2026. Applies the scope decisions recorded on 10 September. The phase crosswalk and operational rules below are researcher implementation choices for review, not additional decisions attributed to the supervisor.

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

Use [Van Weele activity mapping](../process/Van_Weele_Activity_Mapping_2026-09-14.md). Preserve the existing live family and add the purchasing-process stage after the session. A work family describes what the observer sees; the stage describes what that work is intended to accomplish in the purchasing process.

Derived record:

`Observation date | Actor | Source file | Source row | OBS ID | Original family | Task ID | Van Weele stage | Stage confidence | Scope status | Reason | Timing status`

Stage values are `VW1` to `VW6`, `MULTI`, `UNKNOWN` and `NA`. Use `MULTI` only when evidence supports several stages within an inseparable episode, and `UNKNOWN` when the purpose is unclear. `NA` is for an event outside purchasing-stage classification, such as a break. Stage confidence is `C` for direct evidence, `P` for a provisional interpretation, or `?` for unresolved evidence. Existing Task-ID confidence remains a separate field.

Map by the purpose of the work, not by the employee, software screen, activity code or the last word in the note. Do not split a timed episode across stages without observed boundaries. Keep its minutes once under `MULTI`; do not duplicate or distribute them equally. A new phase classification does not create a new timed observation or a new unique case.

## Measures and denominators

| Output | Numerator | Denominator and reporting rule |
|---|---|---|
| Within-scope timed workload share | Reliable, eligible minutes for the family or stage | All reliable, eligible timed minutes for that actor. Report unclassified and multi-stage minutes separately. Label the result as a share of included timed work. |
| Activity occurrence rate | Eligible recorded episodes or events | Known net observation hours for the same actor and collection window. State whether excluded-scope intervals are included in exposure. Do not merge rates based on different exposure definitions. |
| Duration of an episode | Reliable active minutes | Eligible timed episodes of a comparable task. An interrupted case may contain several episodes. |
| Case workload | Sum of reliable eligible episodes for a linked case | Cases with adequate observed coverage. Use date plus OBS ID. Report partial cases separately. |
| Per-line workload | Reliable active minutes for a comparable task | Relevant processed lines where that volume is known. Do not confuse newly added lines with the final PO line count. |

If total net exposure is known but the narrower exposure cannot be reconstructed, report the original exposure explicitly and restrict comparisons to that common definition. Do not silently replace 351 historical net minutes or 265 historical timed minutes with narrower totals. Recalculate and label the scope-specific results first. Those historical totals cover 31 August and 1 September only.

Keep Dennis and Arno in separate profiles. Pooling their minutes would change the primary outcome and give more weight to whichever role was observed longer. EXC exclusion narrows what the thesis can conclude about workload; the included profile is not a complete account of all of Arno's work.

## Sources

- [Academic decisions of 10 September](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-10.md), especially EXC scope and Dennis data sufficiency.
- [Academic decisions of 3 September](../meetings/Academic_Supervisor_Meeting_Notes_2026-09-03.md), especially preservation of raw data, observation sufficiency and analysis denominators.
- [Measurement Protocol v1.3](Measurement_Protocol_v1.3.md), retained for timing, interruption and non-fabrication rules except where this addendum changes the scope.
- [8 September observation](Measure_Observation_2026-09-08.md), including the OBS-16 exclusion.
