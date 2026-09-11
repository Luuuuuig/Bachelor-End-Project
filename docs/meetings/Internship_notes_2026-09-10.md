# Internship Notes — 10 September 2026

**Main focus:** Logistics receiving process and Maurice's responsibilities.

## Role split in Logistics

There are two people in Logistics: **Mike** and **Maurice**. They have different responsibilities.

This note covers **Maurice's tasks**. Mike's tasks are not covered here.

## Maurice — receiving and distribution process

### 1. Receive supplier deliveries

After Arno completes and sends a PO, the supplier sends the ordered goods to Hytech-Pommec.

Maurice receives the delivery and places the incoming packages in the receiving cabinet / area.

The unpacking order depends on workload:

- when it is busy, Maurice tries to unpack deliveries from oldest to newest;
- when it is less busy, the unpacking order can be more random.

### 2. Check the delivery against the pakbon

After unpacking the delivery, Maurice checks whether the physical goods match the **pakbon**.

After the check, the pakbon is scanned.

Maurice then opens the **Ontvangst** tab in Exact and finds the related PO.

For each item, he enters the quantity actually received. A PO may be received only partially, while the remaining quantity stays backordered.

Where applicable, the received quantity is registered per related **PR (production order)**.

After entering the received quantities, Maurice clicks **Verwerken**. Exact then prints an **ontvanglijst**.

## PR flow — goods for a production order

If the received goods belong to a PR, Maurice uses the ontvanglijst to distribute the items to the corresponding production-order container.

Inside the PR container there is also a list showing the components required for that production order.

Maurice compares the **ontvanglijst** with the list inside the PR container.

### Partial quantity

If the PR list requires, for example, 3 units of Component A but only 2 units have been received, Maurice writes **2** next to the item on the PR list. This shows that 1 unit is still missing.

### Complete quantity

When the complete required quantity for an item has been received:

- Maurice places a check mark next to the item;
- the item name on the list is coloured.

When all items on the PR list have a check mark and have been coloured, the **PR tag is coloured** and the container is moved to the **ready section**.

### PO completion versus PR completion

A PO can be fully received while the related PR is still incomplete.

This can happen because:

- part of the required quantity may still be backordered; or
- one PR may contain items from multiple POs and multiple suppliers.

## VRD flow — goods for stock

Some received components are not directly assigned to a PR. These are received for **VRD (voorraad)**.

The receiving steps in Exact remain similar:

1. enter the received quantity;
2. click **Verwerken**;
3. print the ontvanglijst.

Instead of a PR number, the ontvanglijst shows a stock location.

Example: `C-05-06`

- `C` = aisle;
- `05` = cabinet;
- `06` = shelf / layer.

Maurice goes to the indicated location, finds the correct storage box by matching the **artikelcode**, and places the received components in that box.

## White tag inside a VRD box

A white tag **inside the box** usually means:

- the box is currently empty; and
- there is still demand for that component for a production order.

The tag remains in the empty box to indicate that the component is still needed.

When stock becomes available again, Maurice can use the tag to identify that there is still production demand. He then:

1. looks up the artikelcode in Exact;
2. identifies which production order requires the component;
3. assigns the required quantity from **VRD to the production order in Exact**;
4. writes down the production-order number;
5. places the required component in the corresponding PR container.

An empty box does **not** automatically contain a white tag. A box can also be empty without a tag, in which case no outstanding production demand is indicated by the box.

## White sticky tag outside a VRD box

A white sticky tag attached **to the outside of the box** indicates temporary stock.

Example:

- production needs 2 units of Component A;
- the MOQ is 50;
- 50 units are ordered;
- 2 units are used for production;
- the remaining 48 units are temporarily stored in the box.

When the remaining temporary stock has eventually all been used, Maurice removes the sticky tag from the outside of the box.

If the empty box is still in good condition, it is stored away for reuse.

## Medical-related goods

If the received goods or components are **medical-related**, additional documentation is required.

Maurice:

1. takes photos of the components per **batch or lot**;
2. sends the photos to **Johan**;
3. Johan prepares and completes the required form;
4. the completed form is saved together with the pakbon as an attachment to the related PO.

After this has been completed, the normal receiving procedure can continue.

## Tekstartikel

A PO can contain a **tekstartikel**.

This is used when Arno orders something that does not have a normal artikelcode. For example, Arno may order a transport service and enter a written description directly in Exact instead of selecting an article code.

For a tekstartikel, Maurice simply receives it in Exact. No further physical receiving or distribution action is required.

## PO changed after it has already been sent

Sometimes Arno changes a PO after it has already been sent to the supplier.

After such a change, Logistics cannot continue the receiving process immediately. Maurice cannot perform **Ontvangst** until the changed PO has again been properly **Gefiatteerd** and **Verricht** by Arno, Dennis, or another authorized person.

Until this is completed, Logistics cannot continue processing the receipt in Exact.

## Tube usage

Engineers can take tubes directly when needed.

When they take tubes, they leave a note on the Logistics desk containing information such as:

- how much tube material they took;
- which type of tube they took;
- for which project or PR it was used.

Maurice then updates Exact to register the quantity used, the tube type, and the related project or production order.

## Scope of this note

The tasks above describe the activities discussed for **Maurice** on 10 September 2026. Mike has different Logistics responsibilities, which are not documented in this note.
