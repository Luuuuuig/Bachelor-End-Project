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

## Observation session with Arnold, 09:00 to 13:00

From approximately 09:00 until 13:00, I sat next to Arnold and observed his actual work as operational buyer. The goal was to understand how ordering, stock checking, purchase-order generation, supplier communication, and follow-up are handled in practice.

The observations below are descriptive and should be treated as input for further process analysis. They do not yet imply that a specific AI or automation solution should be implemented.

## 1. Identifying what needs to be ordered

Arnold checks orders in Exact Globe+ to determine which requested spare parts still need purchasing action.

There may be several separate internal orders that eventually need to be purchased from the same supplier. These requests are not necessarily grouped together automatically.

Arnold therefore needs to inspect the open orders and decide whether items should be purchased immediately or whether some requests can be combined into a later supplier order.

### MOQ and urgency trade-off

Supplier minimum order requirements, such as a minimum order quantity or minimum order value, can affect this decision.

If a requested item is not urgent and the current order is too small, Arnold may wait for additional demand from the same supplier so that multiple items can be ordered together.

If a spare part is urgently needed for production or a project, the urgency can outweigh the benefit of waiting to reach a larger or more efficient supplier order.

This means that ordering is not based on a single fixed rule. Arnold combines information about current demand, supplier constraints, urgency, stock position, expected future demand, and lead time.

## 2. Manual review of orders in Exact

Arnold manually reviews orders in Exact Globe+ and checks which orders have not yet been **gefiatteerd** and/or **verricht**.

For an order requiring action, he may need to:

1. open the individual order;
2. identify the relevant supplier;
3. inspect the requested items;
4. check the current and expected stock situation;
5. determine whether other stock items from the same supplier may also need ordering soon;
6. decide whether to order now or wait and combine demand.

This requires repeated navigation between individual orders and stock information.

## 3. Current stock, safety stock, future stock and lead time

Arnold does not only look at today's stock level.

He also considers whether an item may fall below its safety-stock level in the coming days or weeks. An item can currently appear to have sufficient stock while still being likely to become understocked soon.

Lead time makes this more difficult. For example, an item may still be above safety stock today, but expected usage could push it below safety stock in one or two weeks while the supplier lead time is relatively long.

There can also be situations where an order was already sent recently, so the current and future stock position has to be interpreted together with outstanding purchase orders.

This appears to be an area where Arnold currently relies strongly on manual checking and purchasing experience.

A possible later research question is whether the system could provide a clearer trigger or overview based on:

- current stock;
- safety stock;
- expected usage;
- already placed purchase orders;
- expected delivery dates;
- supplier lead time;
- urgency of current project or production demand.

This is only a potential direction and needs further validation.

## 4. VRD orders and project/production orders

A **VRD order** refers to a voorraad, or stock, order. However, the practical use of an item can change after ordering.

For example, an item may be ordered today with the intention of replenishing stock, but if it arrives tomorrow and a project immediately needs it, the item may go directly to that project instead of remaining in stock.

Other purchase-order instructions can be directly connected to a project or production requirement from the start.

This makes the distinction between stock replenishment and direct project or production demand important when interpreting the purchasing process.

## 5. The employee field versus the person who actually performs the action

On a specific order page in Exact Globe+, the **Medewerker** field can show a person's name. However, this does not necessarily mean that this person is the employee who actually performs the next purchasing action.

According to Arnold, the person who actually performs the action can be identified through the **verricht** information.

For this workflow, performing or 'verrichten' the order results in the purchase order document being generated, for example `POxxxxx`, and sent to the employee's email so that it can then be sent to the supplier.

This distinction may matter later if Exact data are used to reconstruct who actually performs purchasing work.

## 6. Purchase-order generation and manual supplier email

After Arnold performs the required action in Exact, Exact generates a purchase-order PDF, for example `POxxxxx`, and sends it to his email.

Arnold then manually forwards this email and the PO document to the supplier.

During this forwarding step, he repeatedly types a short message such as:

`Hoi/goedemorgen, hieronder zie je onze PO ...`

This is a repetitive administrative step.

### Previous automation

During a later conversation, Arnold indicated that this supplier-email step had been automated in the past, but the automation did not work reliably enough.

One reason mentioned is that supplier email addresses can change, which can cause fully automatic sending to fail or send information to the wrong address.

Therefore, automatic PO emailing may still be worth investigating, but the earlier failure shows that supplier-contact maintenance and validation would need to be addressed first.

## 7. Supplier confirmation and price checking

After the PO has been sent, the supplier usually responds by email with a confirmation document.

Because supplier prices can fluctuate, Arnold manually opens the supplier document and checks the price of the ordered spare parts against what is recorded in the Exact order.

If the prices are aligned, he attaches the supplier PDF to the Exact order and confirms the order in Exact.

This adds another document-comparison step to Arnold's work.

A possible later direction is to investigate whether price differences could be detected and highlighted automatically so that Arnold only needs to review exceptions. This idea still needs to account for legitimate price fluctuations and should not assume that every difference is an error.

## 8. Email interruptions and Finance hand-offs

While waiting for Exact to generate and email a PO, Arnold may use the waiting time to process other emails.

For example, suppliers sometimes email him about outstanding payments. These payment-related emails are not part of his purchasing responsibility, so he forwards them to Katja in the Finance department.

This is a small example of work arriving through Arnold even when another department is responsible for resolving it.

## 9. Purchase authority

According to Arnold, he has authority to place orders with a value below **EUR 10,000**.

Orders above that amount require involvement or authorization from someone else.

The exact approval process above EUR 10,000 still needs to be mapped if it becomes relevant to the project.

## Initial process opportunities observed today

Today's observation suggests several areas that may be worth investigating further. These are hypotheses, not selected solutions:

- better grouping of separate requests that go to the same supplier;
- decision support for the MOQ versus urgency trade-off;
- clearer visibility of current stock, safety stock, expected future stock, outstanding purchase orders, and lead time;
- identifying which open orders still require purchasing action without repeated manual navigation;
- reducing repetitive manual PO email forwarding;
- validating supplier contact information before automated communication;
- automatically comparing supplier confirmation prices with Exact order prices and highlighting deviations;
- reducing unnecessary email hand-offs for issues that belong to another department;
- distinguishing administrative tasks from tasks that genuinely require Arnold's purchasing experience.

These observations should be compared with the official Exact buyer instruction document and with further observations of Arnold's work before choosing a project use case.

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

## Questions for further workflow observation

- How many open orders does Arnold normally inspect in a day?
- How often are several requests from the same supplier available at the same time?
- How often does Arnold delay a non-urgent purchase because of MOQ or order-value considerations?
- Which Exact fields show current stock, safety stock, planned usage, outstanding purchase orders, and expected receipt dates?
- Can Exact already calculate projected stock levels, or does Arnold currently combine this information manually?
- How often are generated POs forwarded manually to suppliers?
- How often do supplier email addresses create problems for automated sending?
- How often does a supplier confirmation contain a price difference that Arnold needs to investigate?
- How much time does the price-checking and attachment process take?
- How are orders above EUR 10,000 approved?
- Can the `verricht` information be reliably used to identify the person who actually processed an order?

## Current interpretation

Today provided a more detailed view of Arnold's actual purchasing work. A significant part of the workflow involves manually combining information from separate orders, stock levels, safety-stock considerations, outstanding orders, supplier constraints, urgency, lead time, emails, and supplier documents.

Some steps appear repetitive and potentially suitable for process improvement or automation, while other decisions depend on context and Arnold's purchasing experience. More observation is needed before deciding which problem should become the main BEP use case.