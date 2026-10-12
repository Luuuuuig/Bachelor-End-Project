# Update for Zhongxin, 15 October 2026

**From:** Yijie Wang. **Attached:** the analysis notebook and the selection notebook as HTML. **Purpose:** report what was done after the 8 October meeting, put the selection criteria to you for review, and ask for your decision on the weights.

## What changed since 8 October

- The analysis was rebuilt on 12 October on the original observation codes (PO, CLAR, CHECK, SEND, OTHER, REQ, DEC) and the agreed purchasing stage of each record. The later note-based labels (kinds of work) are archived and no longer used. The data are unchanged: five sessions, 892 observed minutes, 742 recorded minutes, 560 in the improvement scope.
- Your table of activity shares by day, the Kruskal-Wallis test and the corrected CHECK-per-line comparison are in the analysis notebook (sections 4.3, 7.1 and 5.4, 5.3).
- The selection method is unchanged. Its evidence now comes from the raw codes; no score changed and two uncertainty ranges widened. Everything in the selection remains provisional until your review.

## 1. The criteria

| Criterion | Definition | Why it belongs | 1 / 3 / 5 anchors | Evidence source |
|---|---|---|---|---|
| Observed workload contribution | Arno's recorded effort within the bounded activity | Reducing his workload is the objective (SQ3, SQ4) | Under 5% of in-scope minutes / 5 to 15% / over 15% with recorded burden on several days | Analysis notebook, parts 4, 5 and 8 |
| Business value beyond counted workload | A consequence for purchasing or the company beyond buyer time | SQ4 requires business relevance | No effect named / one effect with an example / confirmed by the company supervisor with examples or figures | Dennis's 15 September explanation; Johan's confirmation (open) |
| AI-task fit | Whether a useful AI function is needed beyond rules | The focal solution must have a real AI role | Just passes gate 6 / AI needed for one part / the core needs reading documents or judging patterns, with a precedent | Observed documents; AI function comparison; literature |
| Data readiness above the gate minimum | Usability of permitted inputs once the gate is passed | Decides how good the prototype and test can be | Few hand-collected examples / enough past cases with moderate cleaning / exportable representative cases with a traceable correct outcome | Exact test-account checks PC1 to PC4 (open) |
| Repetition / process standardisation | Recurrence and stability of inputs, outputs and exceptions | Support must be reusable across cases | Fewer than 3 of 5 days or varying inputs / every day but varying inputs / many stable cases every day | Case-days and days per candidate (part 8) |
| Prototype / technical feasibility | Build effort and dependencies within the BEP | A bounded build must be possible | Needs Exact integration / buildable on exports with manual steps / buildable on available data and tools | Permitted exports and tools |
| Evaluation feasibility | A defensible manual-versus-assisted comparison for SQ5 | The thesis must evaluate the artifact | No reference or comparable cases / some cases and a rubric / enough repeated cases with a reference answer and buyer time | Reference answers from the test account (open); per-line timing |

Six feasibility gates come before the scores (permission, suitable data, reference answer, controlled risk with buyer review, feasible build and evaluation, meaningful AI contribution); a failed gate cannot be compensated by points. The full definitions, the safeguards against double counting and the gate verdicts are in the selection notebook, sections 2 and 3, and in the methodology, section 5.3.

## 2. Your table: activity shares by day

Share of each day's in-scope recorded minutes (%). The columns add up to 100 except on 18 September, where one UNCLEAR minute (0.7%) is not shown. The second version of the table, on the observed clock minutes of each day (165, 186, 104, 240, 197), is in section 4.3 of the analysis notebook; the ranking within a day is the same.

| Code | 31 Aug (99 min) | 1 Sep (123) | 8 Sep (70) | 18 Sep (149) | 23 Sep (119) | Range |
|---|---:|---:|---:|---:|---:|---|
| PO | 22.2 | 41.5 | 35.7 | 19.5 | 31.9 | 19.5 to 41.5 |
| CLAR | 39.4 | 21.1 | 5.7 | 26.2 | 39.5 | 5.7 to 39.5 |
| CHECK | 13.1 | 10.6 | 4.3 | 38.3 | 4.2 | 4.2 to 38.3 |
| SEND | 15.2 | 14.6 | 20.0 | 9.4 | 8.4 | 8.4 to 20.0 |
| OTHER | 10.1 | 12.2 | 34.3 | 6.0 | 16.0 | 6.0 to 34.3 |

The daily mix varies: CLAR is largest on 31 August and 23 September, PO on 1 and 8 September, CHECK on 18 September, when 57 of its 91 minutes were recorded. With 18 September left out, CHECK falls from 16.2% to 8.3% of the improvement minutes; PO and CLAR stay the two largest codes with any day left out (section 4.4). The Kruskal-Wallis test on episode lengths by day gives H = 2.76, p = 0.60 (182 in-scope episodes); on CHECK minutes per line, 18 September against the other days, H = 0.66, p = 0.42. Neither test establishes equal days or a stable activity mix. The corrected CHECK-per-line comparison is 0.90 minutes per line on 18 September against 0.83 on the other days (0.87 pooled): about 4.6 seconds per line, not the 1.8 seconds I quoted on 8 October.

## 3. Why order and confirmation checking leads, on the raw codes

1. **A recurring, bounded block of work.** CHECK is 21 records and 91 minutes (16.2% of the 560 in-scope minutes) in 19 case-days on all five days.
2. **Two control points in two stages.** 37 of the 91 CHECK minutes are checks before ordering, in Ordering (the largest stage, 56.8% of the in-scope time); the other 54 minutes are checks at the confirmation, in Monitoring (12.1%), of which 49 fall on 18 September.
3. **The buyers reject autonomous ordering, not review-only flagging.** Arno and Dennis opposed automatic PO creation and sending (reported 8 October); a tool that reads, matches and flags while the buyer decides has not been rejected and is still to be asked (Arno).
4. **A business effect beyond buyer time.** Dennis explained on 15 September that outdated purchase prices led Sales to sell at a loss; Johan's confirmation is still open.
5. **One gate passed, five open.** Permission for test-account data and an external AI service was given on 7 October; suitable data, a reference answer, buyer review, build and evaluation feasibility and the AI contribution are provisional until the test-account checks.
6. **AI for reading and matching, rules for comparing.** Quotations and confirmations arrive on paper, as PDF, by e-mail and from websites, with item descriptions that can differ from the PO; the comparison of price, date and quantity is a rule.
7. **A checkable outcome per line is plausible, not yet established.** Each check compares order lines, so a reference answer per line (the approved price, date and quantity) is conceivable, and the observed time per line (0.87 pooled; mean rate per check 1.24, 95% CI 0.70 to 1.78) shows that a timed comparison on matched cases is feasible. Whether a trustworthy reference exists is gate 3, still open until the test-account checks.

With Yijie's provisional weights the totals are 76.2 for checking, 56.8 for article/supplier data, 51.9 for maximalisatie and 50.8 for request intake (57.8 if the whole Specification stage counted for it). Checking leads every single-change check; six combined one-point changes within the recorded ranges would put article/supplier data ahead.

**Limits.** 57 of the 91 CHECK minutes fall on 18 September; one buyer, five partial sessions; a price or delivery date is recorded in the note for 33 of the 91 minutes, an unspecified mismatch for 20, and nothing specific for 38; no test-account check has been made yet. **Fallbacks:** (a) confirmation-against-PO checking only (the Monitoring part, 54 minutes); (b) article/supplier data in Exact (43 minutes), the runner-up.

## 4. The weights

The weights used so far are my own provisional swing weights of 7 October (swings 100, 40, 50, 60, 30, 40, 50 for workload, business value, AI fit, data readiness, repetition, prototype feasibility and evaluation feasibility; weights 27.0, 10.8, 13.5, 16.2, 8.1, 10.8, 13.5%). They were set after I had seen the workload figures. You can choose:

- **Option A:** set your own swings for the seven criteria. This update already shows my swings and the ranking, so your set would be an informed review rather than an independent elicitation; it becomes the agreed weights, recorded with the date, and mine is kept only as a sensitivity scenario. We discuss any swing on which we differ by more than 10 points.
- **Option B:** review my swings and the anchors and tell me what to change; the agreed set is recorded with the date and the totals are rerun.

Until one of these is done, the ranking above is a provisional scenario, not the selection.

## 5. Questions for you

1. **Sufficiency.** Do you agree that no further general observation day is needed for the provisional selection, given that 18 September changes the CHECK share but not the ranking of PO and CLAR? Which targeted checks do you want before Arno's leave at the end of October?
2. **Kruskal-Wallis.** The tests detect no clear rank difference under their assumptions. Can we treat them as supplementary and use the descriptive table to judge the daily pattern?
3. **Criteria and weights.** Are the seven criteria distinct enough? Option A or option B for the weights?
4. **CHECK per line.** The corrected comparison is 0.90 against 0.83 minutes per line. Does your conclusion of 8 October still hold?
5. **Arno.** Is a short written confirmation enough (what a check compares, where the trusted price comes from, which support he accepts) instead of a full session?
6. **Evaluation participant.** Arno is on leave from the end of October. Who takes part in the evaluation, and when?
7. **Stage provenance.** The agreed stage of 15 records (56 minutes, 5 records and 14 minutes in scope) comes from a context review by an assistant, not from the observer. Is this acceptable if it is reported as such?

## 6. Next steps and dates

| When | What |
|---|---|
| 13 to 14 October | Exact test-account checks PC1 to PC4: paired POs and confirmations or quotations, a traceable approved price per line |
| 15 October | This update and the criteria with you; weights procedure agreed |
| 19 to 20 October | Arno: written confirmation or short session; evaluation participant settled |
| 22 October | Focal-case alignment: Johan's business-value confirmation, final weights and rerun of the totals |
| Before 29 October | Evaluation protocol drafted and sent for agreement |
