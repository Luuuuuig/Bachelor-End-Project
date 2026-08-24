# Official Purchasing Document Register — 21 August 2026

**Status:** Internal project evidence register  
**Integration status (24 August 2026):** The high-level findings from this document package have now been integrated into `docs/process/Process_Cleaned_V1.0.md` and `docs/methodology/Phase_1_Current_Methodology.md`. The project is **not waiting for the purchasing SOP anymore**.

**Source:** Documents supplied by the purchasing manager on 21 August 2026 after a request for the formal purchasing/SOP documentation.

## Confidentiality handling

The supplied company documents state that the documentation is **proprietary information** and may not be forwarded, published or copied, in whole or in part, without prior written explicit consent of Hytech-Pommec B.V.

For that reason, this repository currently stores **this evidence register and analytical references only**, rather than copies of the original proprietary binary files. The original files should only be copied into a third-party repository/storage environment if Hytech-Pommec explicitly confirms that this is permitted.

SHA-256 hashes below identify the exact source files used for the analysis without reproducing their contents.

---

## 1. Documents received

| # | Source document | Document role / current relevance | SHA-256 |
|---|---|---|---|
| 1 | `SOP740-01 Rev.A Purchasing and verification of purchased product.pdf` | **Primary formal purchasing SOP.** Most relevant document for comparing the observed buyer workflow with formal company procedure. | `f07cdbee7bc69df5f1b5c55ba40a087b673d6ba54491fb0083cf6bbd2575e28c` |
| 2 | `SOP741-01 Rev. B  Supplier control.pdf` | Formal supplier-selection, approval, monitoring and supplier-change procedure. Important for establishing organizational ownership of supplier selection. | `f93f98bd42ab6cc74a1ef120f9d4476ae30cceb7c69aed5cd2c3fec985c3963b` |
| 3 | `FRM741-01-001 Rev. B Selection and approval supplier.dotx` | Supporting formal supplier-selection/approval form referenced by SOP741-01. | `e5ad249ed95d163897a92c2dd741186fed7a380ac9db2ed4ce14f356b79fd37e` |
| 4 | `FRM741-01-002 Rev.A Supplier (re)evaluation.docx` | Supplier review/re-evaluation form. Contains monitoring and review criteria such as delivery reliability, NCRs, corrective action, communication/service and supplier audit results. | `efa2263b827fa1d445e2231f578f4b905439d928e3cedc5f441f542e49256ec4` |
| 5 | `FRM741-01-003 Rev.A Suppliers List.xltx` | Approved supplier list/template referenced by SOP741-01. Used for approved supplier status/classification. | `7b1a1d995eb6071c53e5b3d70a0e131458ed02d720c49e60573733f63bd783c8` |
| 6 | `WI741-01-001 Rev.- Artikelbeheer.pdf` | Exact work instruction for creating/managing articles. Useful as a formal system instruction but not an end-to-end operational purchasing workflow. | `08a3c31cc86f1b1ae523c415a29df48a00929bd3c678a91ca595a18c11c90b75` |
| 7 | `FRM740-01-002 Rev.- Incoming inspection - check MDR device.docx` | Incoming-inspection checklist for MDR devices. Primarily relevant after receipt and therefore mostly outside the current buyer-side process boundary through `Bevestigd`. | `36fba2ea67d56eb6ddd23162494ea520830947650a6b1164910202db9e5a91d9` |
| 8 | `FRM740-01-001 Rev.A Inkoopvoorwaarden_Terms and conditions Hytech-Pommec B.V..pdf` | General purchasing terms and conditions. Relevant contractual background but not a detailed description of the buyer's daily workflow. | `0f0b03d67984c34b280625ad729b8987175655359a60bcf257a93f499cf5e9fa` |

---

# 2. Formal purchasing procedure — SOP740-01

## 2.1 Scope and responsibility

SOP740-01 is the main formal procedure relevant to the current operational-purchasing study.

The SOP states that:

- it applies to purchased materials, equipment and services;
- the Manager Procurement is responsible for the purchasing procedure;
- the Manager Procurement is responsible for verifying that a written agreement exists with the supplier;
- Service & Logistics owns the prescribed incoming-inspection activities, especially for MDR products.

## 2.2 Formal purchasing decision inputs

The purchasing section explicitly identifies several inputs used to decide whether products need to be purchased:

- e-mails containing article number/description or reference and quantity;
- stock in the ERP system;
- customer orders;
- customer forecasts.

For critical products, purchasing is restricted to approved suppliers from the approved supplier list.

The SOP then requires a Purchase Order to be produced in the ERP with a unique automatically assigned number.

## 2.3 Formal PO completion and confirmation handling

The SOP states that, after completion and authorization, the PO is placed with the supplier and archived.

If an order confirmation is received, it must be archived using the uniquely assigned PO number in the designated purchasing mailbox.

## 2.4 Important comparison with observed operational practice

SOP740-01 describes the purchasing process at a **high procedural level**. It does not provide the detailed operational decision rules observed during the Week-1 buyer shadowing.

The following observed activities are not explicitly operationalized in the purchasing section of SOP740-01:

- Exact `Advies` interpretation;
- `Toewijzen`;
- maximalisatie / deliberately holding a requirement to consolidate supplier demand;
- the detailed rule for `order now` versus `wait`;
- proactive pre-PO supplier-price checking;
- the practical >€10,000 e-mail/`Fiatteren` route;
- manual forwarding of generated POs to the supplier;
- detailed confirmation-price comparison;
- the later Finance-return/rework loop.

This does **not** imply that these activities conflict with the SOP. The current interpretation is that the SOP specifies the required formal process at a higher level, while the observed workflow contains the detailed operational work needed to execute it in practice.

This distinction should be retained in the process analysis as:

- **Documented / formally required**;
- **Partly documented / SOP gives the high-level requirement**;
- **Observed operational practice not explicitly described by the SOP**;
- **Potential divergence** only where direct contradictory evidence exists.

No divergence should be claimed merely because an operational activity is absent from the high-level SOP.

---

# 3. Supplier control — SOP741-01

## 3.1 Organizational ownership

SOP741-01 formally assigns the supplier-control process to the Manager Procurement. The Manager Procurement and QA Manager jointly assure supplier classification, approval and performance monitoring. The Manager Procurement is also responsible for adding approved suppliers to the supplier list and ERP system.

## 3.2 Supplier selection and approval

Formal supplier selection/approval is documented through the supplier list and, when applicable, FRM741-01-001.

For suppliers/articles/services with possible direct or indirect impact on a medical device, the formal selection-and-approval form is used to document the required level of control.

The procedure describes initiation of a new-supplier process when, for example:

- the current supplier is disqualified;
- a new critical product/process/service cannot be provided by an approved supplier;
- a second/backup supplier is required.

Formal approval is based on defined quality and other requirements, and satisfactory approval requires Manager Procurement and QA Manager involvement before the supplier becomes an approved supplier in the organization/ERP.

## 3.3 Implication for the BEP supplier-selection candidate

This formal documentation supports the Week-1 finding that **supplier selection is not normally an operational-buyer decision performed by Arnold**.

The supplier-selection candidate from the original proposal should therefore no longer be treated as the default Arnold-workload case merely because it fits an optimization benchmark well.

Supplier selection can remain relevant as a wider organizational procurement process, but its formal ownership and approval structure makes it a weak default case for an artifact specifically intended to reduce Arnold's recurring operational workload.

---

# 4. Supplier re-evaluation — FRM741-01-002

The supplier re-evaluation form documents monitoring/review dimensions including:

- validity of certificates;
- validity of agreements;
- supplier incidents/complaints;
- incoming-inspection monitoring;
- delivery reliability (criterion shown as >85%);
- NCR performance, with different limits for critical/non-critical suppliers;
- continuous improvement and feedback;
- response to complaints;
- implementation of corrective actions;
- communication and service;
- audit results;
- overall re-approval outcome.

This material may become relevant if supplier performance or supplier-risk data are later considered as explanatory variables, but it is not currently central to the operational buyer workload baseline.

---

# 5. Artikelbeheer work instruction

WI741-01-001 is a formal Exact work instruction intended to standardize how new articles are created/managed in Exact.

It confirms that correct article entry is a Purchasing responsibility and provides detailed system-field instructions.

For the current BEP it should be treated as:

- evidence of formal ERP/system working requirements;
- supporting documentation for request/article-validation work;
- **not** a substitute for the end-to-end operational purchasing process map.

---

# 6. Incoming inspection documents

SOP740-01 and FRM740-01-002 establish a formal receipt/incoming-inspection process involving Logistics/Service & Logistics and additional MDR controls where applicable.

Because the current detailed buyer-side process scope ends around `Bevestigd`, these activities should remain outside the detailed workload map unless later evidence shows that they generate meaningful purchasing rework.

---

# 7. Current documentary-evidence conclusion

The formal documentation materially strengthens the current-state analysis because the project now has three different evidence sources:

1. **Direct observation** — what the operational buyer actually does;
2. **Buyer validation** — the operational buyer's 21 August walkthrough/corrections of the process model;
3. **Formal documentation** — what SOP740-01, SOP741-01 and supporting forms/work instructions formally prescribe.

The key Week-1 documentary finding is:

> The formal SOP identifies the high-level purchasing inputs and required PO process, but leaves much of the detailed operational judgement and execution logic unspecified. The observed process therefore remains necessary for explaining the actual workload and for eliciting tacit rules such as order-now-versus-wait/maximalisatie decisions.

This also supports continuing the scenario-based decision elicitation: the formal SOP identifies relevant decision information (requests, ERP stock, orders and forecasts) but does not define a complete decision rule for how those inputs should be traded off in real operational cases.

---

# 8. Integration status — completed at high level

The high-level comparison requested when this register was first created has now been incorporated into the current process and methodology masters.

Use:

- `docs/process/Process_Cleaned_V1.0.md` for the synchronized current-state workflow, formal-versus-practice interpretation, active candidate portfolio and open questions;
- `docs/methodology/Phase_1_Current_Methodology.md` for current case-selection and research-method status.

Further document validation is only needed when a **specific open question** requires more detailed formal evidence. The repository should no longer carry a generic action saying “receive/compare the SOP” as though the documentation were still unavailable.
