# Bachelor End Project: operational purchasing support

This TU/e project at Hytech-Pommec investigates how AI-supported tools can reduce the operational buyer's workload while maintaining purchasing quality. Arno's work is the primary outcome. Dennis's relevant tactical work and handoffs provide separate context.

## Current status

The five-session descriptive analysis and provisional focal-case comparison are available in the two notebooks below. **Order and confirmation checking remains the provisional choice.** The proposed aid reads source fields, suggests matches and flags differences for buyer review. Buyer acceptance, suitable reference data and supervisor review remain open. No implemented artifact, achieved saving or completed evaluation is claimed.

Research decisions reflect the dated evidence through 9 October 2026. The 12 October reconstruction simplifies documentation and preserves the analysis; it does not close research gates.

## Read the project

| Entry point | What you will find |
|---|---|
| [Project](docs/PROJECT.md) | Objective, exact submitted questions, scope, stakeholders and deadlines. |
| [Arno analysis](Arno_Analysis_2026_10_02.ipynb) | Workload evidence, patterns, limitations and reproducible calculations. |
| [Focal-case selection](Focal_Case_Selection_2026-10-07.ipynb) | Candidate boundaries, gates, weighted comparison, sensitivity and remaining decisions. |
| [Methods](docs/METHODS.md) | Workload construct, observation and classification rationale, selection and evaluation rules. |
| [AS-IS process](docs/PROCESS.md) | Current purchasing workflow, stable task register and unresolved process facts. |
| [Design](docs/DESIGN.md) | Conditional checking-support requirements, controls, Dennis handoffs and draft evaluation. |
| [Literature](literature/README.md) | Source roles, publication details and reading status. |

For a **company review**, start with Project, the selection notebook's recommendation, and Design. For an **academic review**, start with Project, Methods and the two notebooks; follow their evidence links as needed. Each notebook has a short main argument and supporting appendices.

## Next decisions

1. **Check usable cases and reference answers.** Start with PC1-PC4 in the [Stage A workbook](evidence/working/Stage_A_Test_Account_Check_2026-10-07.xlsx), then relevant export/testing checks. Record actual evidence; a blank worksheet is not a passed gate.
2. **Review the specific aid with Arno.** Use the focused [follow-up guide](evidence/working/Arno_Follow_Up_Session_Guide_2026-10-02.md). Resolve the remaining candidate-boundary questions in the [targeted label review](evidence/decisions/Targeted_Label_Review_2026-10-09.csv), including the two K18 episodes and mixed PO/MAX attribution. Preserve original labels until a dated decision supports a change.
3. **Review selection with Zhongxin and business value with Johan.** Agree the candidate boundary, criteria, scoring anchors, scores, weights and weighting procedure. Data-use permission does not establish business value. The notebook retains the actual score-5 confirmation condition.
4. **Confirm the focal case, then agree design and evaluation.** Freeze the manual comparator, primary workload endpoint, meaningful improvement threshold, quality guardrail and reference ownership before development and formal testing.

Additional broad observation, independent recoding/kappa, extra distribution-fit tests and further Dennis days are conditional on a specific evidence gap. They are not automatic completion requirements. The [8 October meeting record](evidence/meetings/Academic_Supervisor_Meeting_Notes_2026-10-08.md) remains dated evidence; prepared analyses still need substantive review.

## Evidence and document ownership

[Evidence](evidence/README.md) locates observations, source data, decisions, protocols, workbooks and submissions. [Archive](archive/README.md) identifies retained historical sources and superseded files available through Git history. The [migration register](archive/Repository_Migration_2026-10-12.csv) maps every original path to its current location or immutable source.

This README owns the current worklist. Project owns scope and deadlines; Methods owns constructs and research rules; Process owns AS-IS facts; Design owns provisional requirements. The notebooks own computed findings and the applied selection scenario. Dated source records retain their dates, uncertainty and authority; they are not parallel current task lists.

## Reproduce the notebooks

Install the recorded environment with `python -m pip install -r requirements.txt`, then open either root notebook in Jupyter and run all cells from a fresh kernel. Both notebooks read the same unchanged CSV evidence from an **immutable Git commit**, with their paths and input hashes recorded in the migration register. Access to the private repository is required for the raw GitHub URLs. A Colab badge or browser login does not by itself verify that private raw-file retrieval will work.

The pilot remains separate from the five-session baseline. Historical task-register files under `data/provenance/` are active inputs. Do not reorder source rows, edit classifications or change the pinned revision as part of routine document maintenance. A future analysis update needs a dated evidence change and a deliberate new input revision.
