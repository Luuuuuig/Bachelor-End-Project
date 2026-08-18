# Internship notes, 19 August 2026

## IT discussion: access to Exact Globe+ through Orbis

During a conversation with the IT department today, I was informed that Exact Globe+ can be accessed through **Orbis**.

This is relevant to the BEP because a future AI or automation solution may need controlled access to information stored in Exact Globe+.

At this stage, the important confirmed information is:

- Hytech-Pommec uses Exact Globe+ as its ERP system.
- According to the IT department, access to Exact Globe+ is possible through Orbis.
- Orbis should currently be treated as an existing route or integration layer for accessing Exact.

## Relation to MCP

Orbis should **not currently be assumed to be MCP itself**.

If an AI agent is developed later, MCP could potentially be investigated as a separate layer that exposes selected Exact or Orbis functions to the AI agent. However, the actual technical architecture has not yet been confirmed.

Possible future architectures to investigate could include:

1. AI solution -> MCP -> Orbis -> Exact Globe+
2. AI solution -> another approved interface -> Orbis -> Exact Globe+
3. AI solution -> an Exact interface directly, if this is technically available and approved by IT

These are only technical possibilities and are not selected solutions.

## Questions for IT / technical investigation

Before choosing an integration approach, clarify:

- What exactly can Orbis access in Exact Globe+?
- Is the access read-only, or can it also write or update information?
- Which Exact data relevant to purchasing can be retrieved through Orbis?
- What authentication and permission controls are used?
- Does Hytech-Pommec already have an API, service, connector, or other interface available through Orbis?
- Is there already any MCP-compatible interface in the current environment?
- If not, would IT permit an MCP server or another controlled interface to expose selected functions to an AI solution?
- What security and confidentiality restrictions apply to company and purchasing data?

## Current interpretation

This information reduces uncertainty about whether Exact Globe+ can technically be connected to another system. There appears to be an existing access route through Orbis, but the exact capabilities and the relationship to a future AI solution still need to be investigated before deciding on an architecture.