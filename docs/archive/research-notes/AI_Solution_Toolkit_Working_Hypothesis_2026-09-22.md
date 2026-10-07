# AI solution toolkit — working hypothesis

**Date:** 22 September 2026  
**Status:** Working solution-design note only. This is not a selected focal solution and does not change the approved Plan of Work, research questions, methodology, or candidate-selection procedure.

## Purpose

Record the essential technical building blocks discussed for possible AI-supported purchasing solutions. The exact combination depends on the focal purchasing component selected during Analyze. Not every candidate requires every tool below.

## Essential building blocks

| Building block | Main role | Why it may be needed |
|---|---|---|
| **Exact integration layer** | Read from and, where supported and approved, write to Exact Globe+ | Gives the prototype controlled access to purchasing data and transactions. Candidate technical routes include Exact Entity Services / API, Exact SDK, or another Hytech-approved integration. Read-only SQL may support retrieval during feasibility work; unrestricted raw SQL writes are not the preferred design. |
| **Safe domain-specific wrapper tools** | Expose only narrowly defined purchasing actions to the AI | Prevent the agent from receiving unrestricted ERP/database control. Example tools: `get_open_demand()`, `get_supplier_demand()`, `get_purchase_order()`, `generate_po_from_demand()`, `add_demand_to_po()`. Each wrapper validates the request, executes the approved Exact operation, reads the result back, verifies it and returns a structured result. |
| **Deterministic rules / validation layer** | Perform hard checks that do not require AI | Examples: required fields present, same supplier, demand still open, authorization/value limits, duplicate-order checks, valid IDs, allowed PO status. Rules should be used instead of AI where the logic is explicit. |
| **Jev decision layer** | Make bounded probabilistic decisions where judgement is genuinely needed | Potential outputs include `AUTO / REVIEW / MANUAL`, and candidate-specific decisions such as `ADD / NONE / REVIEW` or `ORDER / HOLD / REVIEW`. Jev should not be added where a deterministic rule is sufficient. |
| **LLM / AI agent** | Handle unstructured information and execute approved multi-step work | Possible roles: extract information from emails/documents, retrieve supporting information, prepare communications, call safe Exact tools, verify returned results and complete a workflow after an automation decision has been approved. |
| **Orchestration layer / thin custom harness** | Control the order in which rules, Jev, the LLM agent, Exact tools and human review are used | Makes Jev a mandatory decision gate where required rather than leaving the entire flow to a general-purpose agent harness. This can be a small domain-specific Python workflow instead of a new general-purpose agent framework. |
| **Human review interface** | Keep Arno involved only where review or expert judgement is required | Review queue for uncertain/high-risk cases; approve, modify or handle manually. The goal is to remove routine handling while preserving intervention capability. |
| **Audit / evaluation log** | Record what happened for safety and thesis evaluation | Store case input, rule results, Jev output/confidence, agent actions, Exact result, human corrections, failures, time and AI/API cost where relevant. This supports both traceability and quantitative evaluation. |

## Core architecture

```text
Exact / requests / documents
          ↓
Data retrieval
          ↓
Deterministic rules and validation
          ↓
Jev decision where bounded judgement is required
          ↓
   AUTO / REVIEW / MANUAL
      ↓       ↓        ↓
 AI agent    Arno      Arno
      ↓
Safe domain-specific Exact tools
      ↓
Exact supported integration
      ↓
Exact Globe+
      ↓
Read back + verify result
      ↓
Audit log + Arno overview
```

## Important design principle

**Jev is not itself the workload reduction.** Workload is reduced only if the workflow removes, shortens or prevents Arno's handling.

A weak design would be:

```text
Jev recommendation → Arno still inspects every case → Arno still decides → Arno still performs every Exact action
```

A stronger design, if supported by evidence, is:

```text
high-confidence standard case → AUTO → agent executes approved workflow
uncertain case → REVIEW → Arno performs a short check
complex/high-risk case → MANUAL → Arno handles the case
```

## Visibility principle

Automation should **remove handling work, not process visibility**.

Possible Arno-facing design:

- **Overview:** what was automatically processed, what is waiting for review, what failed and what remains manual.
- **Review queue:** only cases requiring an action from Arno.
- **Drill-down:** Jev result/confidence, relevant rule results, agent actions and Exact outcome.
- **Exact trace:** where appropriate, a minimal automation reference/run ID rather than placing the full AI reasoning in the PO note.

## Example safe wrapper

Conceptual example only:

```python
def generate_po_from_demand(demand_ids):
    demand = exact.get_demand(demand_ids)

    validate_ids_exist(demand)
    validate_still_open(demand)
    validate_same_supplier(demand)
    validate_required_fields(demand)
    validate_no_duplicate_po(demand)

    result = exact_supported_interface.generate_po(demand_ids)

    created_po = exact.get_purchase_order(result.po_id)
    verify_created_po(created_po, demand)

    return {
        "success": True,
        "po_id": created_po.id,
        "status": created_po.status,
        "verification": "passed"
    }
```

The exact implementation depends on which Exact interface reproduces the required business action. In particular, it is still an open feasibility question whether Arno's observed `Inkoop` selection/click workflow can be invoked through Entity Services, the Globe SDK, or another supported Hytech integration.

## Candidate-specific use

The toolkit is modular.

### Standard-case / PO automation
Likely emphasis: deterministic rules + Jev routing + AI agent + safe Exact tools.

### Supplier-confirmation / price checking
Likely emphasis: document extraction + deterministic comparison + selective Jev triage + Exact update/archiving tools. Jev may play only a secondary role.

### Request intake / clarification
Likely emphasis: LLM extraction + completeness rules + Jev routing + human/requester escalation.

### Maximalisatie / HOLD / ORDER
Likely emphasis: Exact state retrieval + hard constraints + Jev bounded decisions + AI agent execution, but only if a defensible reference outcome and safe automation boundary can be established.

## Thesis relevance

If this architecture becomes part of the selected focal solution, the relevant evaluation is not simply whether the AI can produce an answer. It should assess whether the redesigned workflow:

- reduces Arno's attributable active handling/review time;
- reduces the share of cases requiring Arno;
- maintains purchasing quality;
- avoids incorrect automatic actions;
- keeps correction/review work acceptable;
- preserves adequate process visibility and intervention capability;
- remains technically feasible within Exact and Hytech's permissions/security constraints.

## Decision boundary

Do not treat this architecture, Jev, or AUTO/REVIEW/MANUAL as selected before Analyze.

Use this note only as a solution option to revisit if the selected focal component shows:

1. a meaningful amount of addressable Arno workload;
2. sufficiently repeatable/standardizable cases;
3. defensible decision/reference outcomes;
4. suitable data access;
5. safe Exact integration;
6. a justified role for AI beyond deterministic rules;
7. feasible quantitative evaluation.
