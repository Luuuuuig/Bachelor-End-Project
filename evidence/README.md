# Evidence and reproducibility

This is a source index. The [root README](../README.md) owns current actions and the notebooks own calculated results. Dated records retain their original scope, uncertainty and author attribution. Their internal links point to historical source versions where needed; use this index and the [migration register](../archive/Repository_Migration_2026-10-12.csv) to find current locations.

## Find supporting evidence

| Evidence | Current location and use |
|---|---|
| Five Arno session CSVs | [data/observations](../data/observations/), original rows and ordering; date plus one-based source row identifies each record. |
| Pilot | [data/pilot](../data/pilot/), separate method-development evidence; not part of the analytical baseline. |
| Dated observation narratives | [observations](observations/), including the pilot, Arno sessions and Dennis's separate 25 September session. Notes contain context missing from CSVs. |
| Net clock exposure | [Observation time register](../data/Observation_Time_Register_2026-09-25.csv) and [dated review](decisions/Observation_Time_Review_2026-09-25.md). Source paths, hashes and URLs inside the CSV are historical provenance, not broken current-file instructions. |
| Reviewed kinds and stage mapping | [data/coding](../data/coding/), [codebook](../docs/reference/Kinds_Of_Work_Codebook.md), [activity framework](../docs/reference/Purchasing_Activity_Framework_2026-09-21.md), [stage review](decisions/Stage_Review_2026-09-30.md) and [targeted label review](decisions/Targeted_Label_Review_2026-10-09.csv). |
| Historical Task-ID placements | [data/provenance](../data/provenance/), the 21/25 September enrichment CSVs remain active Arno notebook inputs. Preserve all provenance columns. |
| Reported causes | [Causes CSV](../data/analysis/Arno_Causes_Draft_2026-10-06.csv), original source/status and `answer_2_oct` remain dated reports. Add future evidence with explicit dates; do not overwrite earlier answers. |
| Selection judgments and source reasoning | [decisions](decisions/), including the frozen candidate matrix, dated swing elicitation and AI-function comparison. The selection notebook owns the applied comparison; these files preserve its provenance. |
| Supervisor and field records | [meetings](meetings/), dated academic/company meetings and internship notes. Agendas remain in [history](../archive/README.md); a question or proposal does not establish an answer or approval. |
| Collection controls | [protocols](protocols/) and [earlier protocols](../archive/protocols/). Read effective rules in [Methods](../docs/METHODS.md): v1.1 applied on 31 August, v1.2 on 1 September, v1.3 from 2 September with later addenda. |
| Working instruments | [working](working/): Stage A workbook, focused Arno guide and Dennis guide. The Arno guide includes attributed answers; the workbook includes recorded permission evidence and formulas. Neither is a disposable export. |
| Optional coding instrument | [45-record sample](working/optional/Kinds_Coding_Check_Sample_2026-10-02.xlsx), an uncompleted optional exercise. Its historical compulsory-kappa wording does not create a current requirement. |
| Submitted project sources | [submissions](submissions/): final Plan of Work, half-page description and submitted-plan figures. Preserve original submitted bytes and five-question authority. |
| Formal company documents | [Company document register](company/Official_Document_Register_2026-08-21.md), permitted descriptions and eight original hashes. Proprietary binaries are intentionally absent. |

## Input contract

The Arno notebook loads 11 CSVs: five daily observations, time register, kinds labels, framework map, causes table and two historical enrichment files. The selection notebook loads six of these: five daily observations and kinds labels. All are byte-identical to their pre-reconstruction sources. The pilot, manual workbooks and historical scoring CSVs are not computational inputs.

Both notebooks pin data to commit `62a17bda64fdd28184aa6465c49378f749d0ceac`. The migration register records each original path, current path, original Git blob, SHA-256 and active-input status. That commit establishes the new paths; its temporary coexistence of old and new paths is historical. This branch's final tree keeps one current copy.

Keep CSV row order, IDs, missing values and historical source fields intact. Occurrences without duration remain untimed; case-days are not complete orders. The notebook's recorded-activity total differs from net clock exposure. Dated coding or observation corrections require a separate documented research change, not a folder cleanup.

Markdown evidence receives link-target-only repairs to keep its citations usable after moves. CSVs, PDFs, DOCX, XLSX and submitted figures retain their original bytes. Historical full versions of every consolidated or retired file remain available through the migration register; no Git history was rewritten.
