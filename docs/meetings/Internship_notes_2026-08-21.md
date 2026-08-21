# Internship notes — 21 August 2026 (Day 4)

## Day focus

Day 4 was mainly used to consolidate and validate the information gathered during the first three internship days. It was **not** intended as another detailed shadowing/observation day.

The main activities were:

- organizing the current-state process and workload evidence;
- validating the process map with the operational buyer;
- asking Johan for the official SOP / formal purchasing procedure so documented procedure can be compared with observed practice;
- receiving the official purchasing/supplier-control documentation package from Johan;
- clarifying the practical approval route for orders above the operational buyer's authorization limit;
- discussing whether Johan's purchasing decisions are comparable with Arnold's for scenario-based decision elicitation.

---

## 1. Current-state workflow validation with Arnold

The current-state workflow was walked through with Arnold and corrected where the sequence did not match actual working practice.

### Corrected sequence around `Advies`, `Toewijzen`, price checking and PO preparation

The current working sequence is:

`Decision to order → Review Exact Advies → Toewijzen → relevant pre-PO price check / price correction → prepare/complete supplier PO and combine relevant demand from the same supplier → authorization / Fiatteren path → Verrichten / PO generation → supplier communication`

This corrects the earlier process-map version that placed supplier-PO preparation/consolidation before `Advies` and `Toewijzen`.

**Evidence status:** Confirmed through buyer walkthrough on 21 August 2026.

The exact calculation logic behind `Advies` remains open.

---

## 2. Official purchasing documentation received from Johan

Johan was asked whether an official SOP / purchasing procedure exists for this process and supplied the following documentation package on 21 August 2026:

- `SOP740-01 Rev.A Purchasing and verification of purchased product.pdf`;
- `SOP741-01 Rev. B  Supplier control.pdf`;
- `FRM741-01-001 Rev. B Selection and approval supplier.dotx`;
- `FRM741-01-002 Rev.A Supplier (re)evaluation.docx`;
- `FRM741-01-003 Rev.A Suppliers List.xltx`;
- `WI741-01-001 Rev.- Artikelbeheer.pdf`;
- `FRM740-01-002 Rev.- Incoming inspection - check MDR device.docx`;
- `FRM740-01-001 Rev.A Inkoopvoorwaarden_Terms and conditions Hytech-Pommec B.V..pdf`.

The purpose is to compare:

- documented/formal process requirements;
- observed actual working practice;
- operational detail not described in the high-level SOP;
- genuine divergences only where direct contradictory evidence exists.

### Initial documentary findings

`SOP740-01` is the main formal purchasing SOP for the current project. It identifies e-mail/request information, ERP stock, customer orders and forecasts as inputs used to decide whether products need to be purchased, requires a PO to be produced in the ERP, and states that the PO is placed with the supplier after completion and authorization.

The SOP is higher-level than the observed Arnold workflow and does not explicitly operationalize several detailed activities observed during Week 1, including `Advies`, `Toewijzen`, maximalisatie, the detailed buy-now-versus-wait trade-off, proactive pre-PO price checking, the practical >€10,000 approval route, manual PO forwarding, detailed confirmation-price comparison and the Finance-return loop.

This absence should **not** be treated as non-compliance by itself. The current interpretation is that the SOP states formal requirements at a higher level while the observed process captures the detailed work needed to execute those requirements.

`SOP741-01` assigns formal supplier control to Manager Procurement, with Manager Procurement and QA involved in supplier classification/approval/monitoring. This provides formal documentary support for the Week-1 finding that supplier selection is not normally an Arnold-level recurring operational decision.

### Confidentiality handling

The supplied company documents state that they are proprietary and may not be forwarded, published or copied without prior written explicit consent. Therefore the original company binary documents have **not** been copied into the GitHub repository. Instead, an internal evidence register containing filenames, hashes, document roles and analytical findings is stored at:

`docs/company-documentation/Official_Document_Register_2026-08-21.md`

This keeps the project traceable while avoiding unnecessary reproduction of proprietary source documents in a third-party repository.

**Current status:** Documentation received; initial review completed; row-by-row SOP-versus-observed-process comparison remains a next analysis step.

---

## 3. Orders above €10,000 — practical approval route

Johan explained that when an order exceeds the operational buyer's approximately **€10,000** authorization limit, the order is put/sent into **Dennis's or Johan's email** and **Dennis or Johan performs the `Fiatteren` step**.

This gives a clearer practical approval route than the previously unmapped generic approval node.

What is still not fully mapped:

- how the system/email routing is triggered;
- which of Dennis or Johan receives a specific case and according to what rule;
- what Exact records as the approval evidence/status;
- exactly who performs the next system action after their `Fiatteren`;
- typical waiting/elapsed time introduced by this approval route.

**Evidence status:** Stated by Johan on 21 August 2026.

---

## 4. Johan's purchasing context differs from Arnold's

Johan explained that the POs he personally processes are **usually urgent**. Because of this, his normal decision context often leads directly to ordering rather than deliberately waiting for additional demand / maximalisatie.

This means Johan, Arnold and Dennis should **not automatically be treated as interchangeable buyers exposed to the same decision distribution**.

### Implication for the planned Microsoft Forms scenarios

The scenario exercise remains useful, but its purpose should be framed as **standardized scenario-based decision elicitation**, not as a test of which buyer is correct or whether all buyers should naturally make identical decisions.

The scenarios can be used to examine:

- whether the same standardized information produces the same buy/wait choice;
- which cues each participant considers important;
- why their reasoning differs;
- whether differences are caused by role/context rather than different decision quality;
- whether Arnold uses tacit cues not represented in Exact.

For each scenario, add or retain a contextual question such as:

> **Komt een vergelijkbare situatie in uw normale werkzaamheden voor?**  
> Vaak / Soms / Zelden / Nooit

The survey instructions should also ask each participant to assess the scenario **as if they were responsible for that purchasing decision**, even when that type of case is not common in their normal role.

**Evidence status:** Johan's role/context difference is stated evidence; conclusions from the scenario exercise are not yet available.

---

## 5. Day-4 interpretation

The most important Day-4 contribution was **validation and documentary grounding rather than new process discovery**.

The current-state model is stronger because:

- Arnold has now reviewed the workflow sequence directly;
- the `Advies → Toewijzen → pre-PO price check → PO preparation/consolidation` sequence has been corrected;
- the practical >€10,000 `Fiatteren` route has been partially mapped;
- formal purchasing and supplier-control documentation has now been received;
- supplier-selection ownership has formal documentary support;
- a role/context difference relevant to the planned buyer scenario study has been identified.

No final thesis case is selected from these findings alone.
