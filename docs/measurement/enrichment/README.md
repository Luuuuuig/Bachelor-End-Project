# Post-session enrichment: 8 and 18 September 2026

Prepared 18 September 2026. Each CSV adds a derived classification to every active row in the corresponding observation note. These are researcher classifications from the recorded evidence, not additional buyer-validated findings. An unresolved field is an explicit enrichment result, not permission to guess.

| Observation date | Source record | Derived record |
|---|---|---|
| 8 September | [Original observations](../Measure_Observation_2026-09-08.md) | [Row-level enrichment](Measure_Enriched_2026-09-08.csv) |
| 18 September | [Original observations](../Measure_Observation_2026-09-18.md) | [Row-level enrichment](Measure_Enriched_2026-09-18.csv) |

## Sources and versions

- Raw evidence: the dated observation records linked above. The 18 September transcription incorporates Yijie's notebook corrections and clarifications. Crossed-out rows are not active observations.
- Timing and original observation structure: [Measurement Protocol v1.3](../Measurement_Protocol_v1.3.md). The later proposal for overlapping activity times is not applied retrospectively to these records.
- Scope and derived-record rules: [Scope and Classification Addendum, 14 September](../Scope_and_Classification_Addendum_2026-09-14.md), implementing the 10 September decisions.
- Stable Task IDs: section 5 of [Process Cleaned V1.5](../../process/Process_Cleaned_V1.5.md), with the [14 September task crosswalk](../../process/Van_Weele_Task_Crosswalk_2026-09-14.csv).
- Classification refinement: *Van Weele framework from the task register*, rebuilt 18 September 2026, supplied as `Van_Weele_Activity_Framework_2026-09-18(1).docx`. The applied rules are recorded below so this enrichment can be read without that document. They retain the original families, use actual task purpose to support the stage, distinguish buyer work from system/supplier events, and preserve scope and data-quality exclusions.
- Repository source version: `9bf8de870d1b4ffbd383304f7645c21a698eb9c7` for the previously published files. The 18 September observation is first published with this enrichment. No task-register IDs or historical stage assignments have been rewritten.

## How to read the CSVs

The key is `observation_date + source_row`. Source rows are numbered from 1 across all active observation tables in their original written order, including rows whose clock times appear out of sequence. They are episode/event counts, not unique purchasing cases. `case_origin_date + case_id` keeps returning cases distinct: the Primer-C episode observed on 18 September refers to **OBS-01 from 31 August**, not the separate OBS-01 of 18 September.

| Field | Meaning |
|---|---|
| `actor`, `source_file`, `source_row` | Buyer and traceable source location. Both datasets concern Arno. |
| `original_family`, `start`, `end`, `volume_raw`, `int_raw`, `dec_raw` | Source values preserved verbatim after whitespace trimming. Slashes and blanks are not converted into zero, no decision or a new activity code. |
| `task_ids` | Supported current-register task or tasks. Several IDs belong to one combined episode; they do not receive separate copies of its minutes. Blank means no defensible ID. |
| `register_status` | `Mapped`: supported registered work; `U`: described work outside the register; `Mixed`: registered plus unregistered work; `Unresolved`: evidence does not identify the task reliably. |
| `task_confidence` | `C`: confident mapping or register-coverage judgment; `P`: probable; `?`: unresolved. Register coverage is separate from confidence, following the earlier enriched observations. A confidently unregistered action can therefore have `U` with `C`. |
| `van_weele_stage`, `stage_confidence` | Purpose-based stage and separate confidence. `VW1` specification; `VW2` supplier selection; `VW3` contracting; `VW4` ordering; `VW5` monitoring; `VW6` follow-up/evaluation. `MULTI` means evidenced inseparable stages; `UNKNOWN` means insufficient evidence; `NA` would mean no purchasing-stage classification applies. |
| `scope_status` | `INCLUDE`, `EXCLUDE_EXC`, `EXCLUDE_AFTERCARE`, `EXCLUDE_LOGISTICS`, or `REVIEW_SCOPE`. Scope review is withheld from the included-time profile until the evidence establishes eligibility. |
| `quality_status` | `VALID`, `EXCLUDE_CONTAMINATED`, or `UNCERTAIN`. This is independent of scope and classification confidence. |
| `timing_status` | `TIMED`: both boundaries recorded; `TIMED_PARTIAL`: only the observed part of a longer episode; `UNTIMED`: no reliable start/end pair. |
| `recorded_minutes` | End minus start for recorded intervals. Retained for audit even when excluded. Blank for untimed rows; never an invented zero. |
| `analysis_minutes` | Recorded minutes only when scope is `INCLUDE`, quality is `VALID`, and timing is `TIMED` or `TIMED_PARTIAL`. Otherwise blank. Classification uncertainty alone does not remove otherwise usable family-level time. |
| `reason` | Evidence, task/stage interpretation, purpose-specific exclusion and remaining uncertainty. It does not replace the source note. |

## Applied boundaries

Task mapping follows the described work, not the original family alone. A CHECK can concern ordering or monitoring. A SEND is Task 23 only when forwarding the supplier order is supported; receiving a drawing or sending a clarification is different work. A price comparison does not establish negotiation. Attaching a confirmation can support the archiving component of Task 28 without proving that *Bevestigd* was set.

Original EXC and mixed OTHER/EXC rows remain excluded. Demonstrated aftercare or logistics also remains excluded when written as SEND, PO, CLAR or OTHER. Conversely, routine confirmation checking is assessed independently of aftercare elsewhere in the same case. Inseparable work with unresolved scope is marked `REVIEW_SCOPE`; minutes are not allocated by line counts or split without observed boundaries. The exclusions apply retrospectively as an analysis filter, not as a claim about how the older observation was collected.

Added lines do not establish every MAX step or a HOLD/ORD decision. The unsuccessful MAX attempts in 18 September OBS-23 and OBS-24 do not establish why consolidation failed or what final decision followed. No standalone decision time, root-cause conclusion, task-extension ID or improvement ranking is created.

## Timing and interpretation

Recorded intervals retain the v1.3 active-episode convention. They are not complete case lead times or independently reconstructed exclusive-effort estimates. Interruptions, waiting and unrecorded gaps are not assigned invented durations. The first 18 September CHECK had already started before 10:30; only its recorded eight-minute segment is included, and it must not be used as a complete episode-duration observation.

The 8 September window is 10:30–12:23. The 18 September notebook headings are 10:30–12:30 and 13:00–15:00. Neither record establishes all break/observer-unavailable intervals, so no verified net observation denominator or occurrence rate is reported. Unexplained gaps are not reconstructed as work, breaks or MISS.

Any coverage below concerns the included recorded subset. Provisional stage assignments remain provisional. Unknown or mixed stages must be shown alongside classified stages, and eligible family-level time must not disappear merely because a detailed task or stage is unresolved. These two days are not silently pooled with the older 351 net observed / 265 timed-minute totals, which used a broader scope.

## Material evidence limits retained

| Date / case | Treatment |
|---|---|
| 8 September OBS-03 | Transport could mean buying a transport service or excluded logistics execution. Scope remains under review. |
| 8 September OBS-08 | Quotation/website comparison does not establish supplier selection or a comparison with the stored Exact price. Finer classification remains unresolved. |
| 8 September OBS-16 | Both timed rows remain excluded because Yijie lost focus and explicitly marked the observation as contaminated. |
| 18 September, OBS-01 from 31 August | Primer-C has the verified dated case link. The calculator action remains unclassified; no CHECK recoding is imposed. |
| 18 September OBS-05 | CLAR has no decision value. The unclear EXC volume is retained as written and is not used as a numeric line denominator. |
| 18 September OBS-09 | The PO episode combines original demand with an unavailable item's replacement. The recorded 2L and the note's 3L total are both preserved; neither is used to allocate minutes. |
| 18 September OBS-10 | The original SEND row describes receiving a drawing. The source family is preserved, but receipt alone does not establish two minutes of active sending by Arno. |
| 18 September OBS-23 and OBS-24 | MAX was attempted unsuccessfully. Final HOLD/ORD and the reason for failure are not reconstructed. |
| 18 September OBS-29 | Arno's screenshot decision and the confirmed €410 difference remain source evidence. The comparison basis is unspecified; no saving, unit-price effect or loss total is calculated. |

Other unknown tasks, stages and scope boundaries are explained in the corresponding CSV row. Resolving them later requires new source evidence and a traceable revision; enrichment completion does not mean every classification is certain.

## Enrichment coverage

The following counts reconcile every active source row. Recorded minutes include excluded intervals solely for audit; they are not the thesis workload total. Untimed occurrences contribute a row and no invented duration.

| Coverage | 8 September | 18 September |
|---|---:|---:|
| Active source rows enriched | 42 | 74 |
| Rows with recorded start/end pairs | 38 | 57 |
| Untimed occurrences | 4 | 17 |
| All recorded interval minutes, before exclusions | 106 | 196 |
| Eligible rows, including untimed occurrences | 16 | 42 |
| Eligible timed rows | 14 | 31 |
| Eligible recorded minutes | 32 | 121 |
| Eligible rows assigned a single stage, including provisional assignments | 9 | 37 |
| Eligible minutes assigned a single stage, including provisional assignments | 15 | 103 |
| Eligible minutes with UNKNOWN stage | 17 | 18 |
| Eligible minutes with MULTI stage | 0 | 0 |

In the next table, data-quality exclusions take precedence over scope in the display so each row appears in exactly one bucket. Both underlying fields remain separate in the CSVs. The contaminated 8 September rows and the uncertain 18 September drawing-receipt row are not included in the eligible totals.

| Disjoint audit bucket | 8 September rows | 8 September recorded min | 18 September rows | 18 September recorded min |
|---|---:|---:|---:|---:|
| Eligible scope and quality | 16 | 32 | 42 | 121 |
| EXCLUDE_EXC | 6 | 27 | 13 | 47 |
| EXCLUDE_AFTERCARE | 9 | 21 | 5 | 2 |
| EXCLUDE_LOGISTICS | 1 | 2 | 5 | 7 |
| REVIEW_SCOPE | 8 | 15 | 8 | 17 |
| EXCLUDE_CONTAMINATED | 2 | 9 | 0 | 0 |
| UNCERTAIN quality | 0 | 0 | 1 | 2 |
| **Total** | **42** | **106** | **74** | **196** |

### Stage coverage within eligible recorded work

This is classification coverage of a selected subset, not a full-workload comparison between days. `C` and `P` assignments are shown separately. The 18 September VW5/C time includes the eight-minute partial first CHECK segment.

| Date | Stage | Confidence | Eligible rows, including untimed | Recorded minutes |
|---|---|---|---:|---:|
| 8 September | VW4 ordering | C | 8 | 14 |
| 8 September | VW4 ordering | P | 1 | 1 |
| 8 September | UNKNOWN | ? | 7 | 17 |
| 18 September | VW2 supplier selection | P | 2 | 10 |
| 18 September | VW4 ordering | C | 15 | 53 |
| 18 September | VW4 ordering | P | 13 | 9 |
| 18 September | VW5 monitoring | C | 2 | 10 |
| 18 September | VW5 monitoring | P | 5 | 21 |
| 18 September | UNKNOWN | ? | 5 | 18 |

No eligible record is currently classified as MULTI. This does not mean mixed-stage work was absent: the excluded 8 September replacement-supplier episode is provisionally MULTI. No stage, task or day is ranked as the focal improvement case from these coverage figures.
