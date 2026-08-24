# Official Purchasing Document Register — 21 August 2026

**Status:** Authoritative formal-company-evidence register for the BEP.

**Source:** Documents supplied by the purchasing manager on 21 August 2026 after a request for formal purchasing/SOP documentation.

**Ownership:** This file records what the received company documents formally support. Current operational practice belongs in `docs/process/Process_Cleaned_V1.5.md`; thesis-candidate implications belong in `docs/methodology/Phase_1_Current_Methodology.md`.

## Confidentiality handling

The supplied company documents state that the documentation is proprietary and may not be forwarded, published or copied, in whole or in part, without prior written explicit consent of Hytech-Pommec B.V.

The repository therefore stores this analytical evidence register rather than copies of the proprietary source files. SHA-256 hashes identify the exact source files used.

---

# 1. Documents received

| # | Source document | Formal role / relevance | SHA-256 |
|---|---|---|---|
| 1 | `SOP740-01 Rev.A Purchasing and verification of purchased product.pdf` | Primary formal purchasing SOP | `f07cdbee7bc69df5f1b5c55ba40a087b673d6ba54491fb0083cf6bbd2575e28c` |
| 2 | `SOP741-01 Rev. B Supplier control.pdf` | Supplier selection, approval, monitoring and supplier-change procedure | `f93f98bd42ab6cc74a1ef120f9d4476ae30cceb7c69aed5cd2c3fec985c3963b` |
| 3 | `FRM741-01-001 Rev. B Selection and approval supplier.dotx` | Supplier-selection/approval form referenced by SOP741-01 | `e5ad249ed95d163897a92c2dd741186fed7a380ac9db2ed4ce14f356b79fd37e` |
| 4 | `FRM741-01-002 Rev.A Supplier (re)evaluation.docx` | Supplier review/re-evaluation criteria and outcome | `efa2263b827fa1d445e2231f578f4b905439d928e3cedc5f441f542e49256ec4` |
| 5 | `FRM741-01-003 Rev.A Suppliers List.xltx` | Approved supplier list/template | `7b1a1d995eb6071c53e5b3d70a0e131458ed02d720c49e60573733f63bd783c8` |
| 6 | `WI741-01-001 Rev.- Artikelbeheer.pdf` | Exact work instruction for article creation/management | `08a3c31cc86f1b1ae523c415a29df48a00929bd3c678a91ca595a18c11c90b75` |
| 7 | `FRM740-01-002 Rev.- Incoming inspection - check MDR device.docx` | Incoming-inspection checklist, mainly after current buyer-side scope | `36fba2ea67d56eb6ddd23162494ea520830947650a6b1164910202db9e5a91d9` |
| 8 | `FRM740-01-001 Rev.A Inkoopvoorwaarden_Terms and conditions Hytech-Pommec B.V..pdf` | General purchasing contractual background | `0f0b03d67984c34b280625ad729b8987175655359a60bcf257a93f499cf5e9fa` |

---

# 2. SOP740-01 — purchasing and verification of purchased product

## Scope and responsibility

SOP740-01 formally establishes that:

- the purchasing procedure applies to materials, equipment and services;
- the Manager Procurement is responsible for the purchasing procedure;
- the Manager Procurement is responsible for verifying that a written agreement exists with the supplier;
- Service & Logistics owns prescribed incoming-inspection activities, especially for MDR products.

## Purchasing inputs and PO control

The procedure identifies purchasing-decision inputs including:

- e-mails containing article number/description or reference and quantity;
- ERP stock;
- customer orders;
- customer forecasts.

For critical products, purchasing is restricted to approved suppliers from the approved supplier list.

A Purchase Order is produced in the ERP with a unique automatically assigned number. After completion and authorization, the PO is placed with the supplier and archived.

If an order confirmation is received, it must be archived using the unique PO number in the designated purchasing mailbox.

---

# 3. SOP741-01 — supplier control

## Ownership and control

SOP741-01 assigns supplier-control responsibility to the Manager Procurement. The Manager Procurement and QA Manager jointly assure supplier classification, approval and performance monitoring. The Manager Procurement also maintains approved suppliers in the supplier list and ERP system.

## Supplier selection and approval

Formal supplier selection/approval uses the supplier list and, where applicable, FRM741-01-001.

A new-supplier process may be initiated when, for example:

- the current supplier is disqualified;
- a critical product/process/service cannot be supplied by an approved supplier;
- a second/backup supplier is required.

For suppliers/articles/services that may directly or indirectly affect a medical device, the formal selection-and-approval form documents the required level of control. Approval requires the relevant Procurement/QA involvement before the supplier becomes formally approved in the organization/ERP.

The current research implication of this ownership structure is maintained in the methodology file rather than duplicated here.

---

# 4. Supporting documents

## FRM741-01-002 — supplier re-evaluation

The form includes review dimensions such as:

- certificate and agreement validity;
- incidents/complaints;
- incoming-inspection monitoring;
- delivery reliability;
- NCR performance;
- continuous improvement and feedback;
- response to complaints;
- corrective actions;
- communication/service;
- audit results;
- re-approval outcome.

These data may become relevant if supplier performance/risk later enters the selected research case.

## WI741-01-001 — Artikelbeheer

This work instruction standardizes creation/management of articles in Exact and supports that correct article entry/management is a Purchasing responsibility. It is a system/article-management instruction, not an end-to-end operational purchasing map.

## Incoming inspection documentation

SOP740-01 and FRM740-01-002 establish receipt/incoming-inspection controls involving Logistics/Service & Logistics and additional MDR controls where applicable. These activities are mainly beyond the current detailed buyer-side scope through `Bevestigd`.

## Purchasing terms and conditions

FRM740-01-001 provides contractual purchasing background. It is not a description of the buyer's daily operating workflow.

---

# 5. Formal procedure versus operational practice

The formal SOP package describes the purchasing process at a **higher procedural/control level** than the observed day-to-day buyer workflow.

Use the following evidence distinction across the project:

- **Formal requirement:** explicitly stated by SOP/work instruction;
- **Partly documented:** formal documentation defines the high-level requirement but not the detailed execution;
- **Observed operational practice:** seen or buyer-validated but not explicitly detailed by the SOP;
- **Potential divergence:** only when direct contradictory evidence exists.

An operational activity being absent from a high-level SOP is **not** sufficient evidence of non-compliance.

The actual observed activities and their evidence labels are maintained in `Process_Cleaned_V1.5.md` rather than repeated here.

---

# 6. Current document status

The purchasing SOP package has been received and registered. There is no generic outstanding action to “wait for” or “receive” the purchasing SOP.

Further formal-document analysis should be opened only when a specific unresolved process or research question requires it.