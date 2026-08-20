# Internship notes, 20 August 2026

## Morning observation with Arnold, approximately 07:00 to 09:00

The purpose of this observation session was to understand what Arnold works on early in the morning, before the normal level of interruptions starts. Arnold regularly starts around 07:00 so that he can work through purchasing tasks with fewer incoming emails, requests, and questions from colleagues.

The observations below focus on concrete tasks, approximate task durations, and the difference between processing an already existing open order in Exact and creating a new purchase order manually when the request originates outside Exact.

## 1. Existing open orders versus manually creating a purchase order

When a purchasing request already exists in the Exact purchase-order overview, Arnold can work from the existing unprocessed order.

However, not every purchasing request starts in Exact. Requests can also arrive through email or directly from a colleague. In those cases, Arnold first has to create the purchase order manually in Exact before he can continue with the normal purchasing workflow.

This means he has to manually enter the relevant component, spare-part, or service information instead of simply processing an already existing open order.

Sometimes the requester provides only a screenshot of the required component or other limited information. Arnold then has to read the information from the screenshot and manually transfer it into Exact.

### Observed timing

In one case involving the purchase of a service for two machines, manually entering the information for two lines took approximately **5 minutes**.

This suggests that manual PO creation from requests outside Exact creates additional administrative work compared with processing an order that already exists in the system.

## 2. Missing or suspicious information can create much more work than the data-entry step itself

During the same service-order example, Arnold noticed that something appeared incorrect in the description supplied by the engineer. In particular, he suspected that the serial number connected to the machine or service information was not correct.

Rather than simply accepting the supplied information, Arnold investigated the issue. He searched through older purchase orders from the same supplier/company to find a previous PO for the same type of service and the same two machines.

The initial data entry took around **5 minutes**, but the investigation and correction work took approximately **10 to 15 minutes**.

This is important because the main workload in such cases is not necessarily typing information into Exact. The larger cost can come from checking whether the information supplied by the requester is correct, tracing historical information, and resolving inconsistencies before the order can be processed safely.

This is also an example of a task where Arnold's experience matters: he noticed that the description or serial number looked suspicious and chose to verify it rather than continuing automatically.

## 3. Proactive supplier price checking before sending certain POs

During the morning, I asked Arnold to explain the Technische Unie Breda case from 19 August in more detail.

Before sending that PO, Arnold manually checked the current prices on the supplier's website. For the relevant order lines, he searched the supplier website for each component, compared the current supplier price with the price recorded in Exact, and manually updated the Exact price where necessary before continuing with the PO.

Arnold explained that he performs this kind of advance price check particularly for **one-off items (eenmalige artikelen)** and **special components**. He also appeared to mention **services (diensten)**, but this part of the explanation is not yet fully clear and should be verified before treating it as a confirmed rule.

### Why check the price before sending the PO?

Arnold gave a simple example to explain the risk of using an outdated purchase price.

Suppose Exact still shows a pencil at **EUR 1.00**, while the supplier's current price has fallen to **EUR 0.50**. If Arnold sends the PO at EUR 1.00 and only waits for the supplier confirmation before correcting the price, the outdated EUR 1.00 value can remain in the system during that waiting period.

In the meantime, another purchase request for the same pencil could be processed and another PO could be sent using the same outdated EUR 1.00 price.

Checking and correcting the supplier price before sending the first PO therefore helps prevent an outdated price from being reused in subsequent purchase orders while the first supplier confirmation is still pending.

This adds an important distinction to the price-control process observed on 19 August. Price checking is not only a later comparison against the supplier confirmation. For some types of purchases, Arnold also performs a **proactive price check before the PO is sent**.

### Unclear case: service for two machines

In the service-order case involving two machines, Arnold did **not** perform the same visible advance supplier-price check before working on the order.

The reason is currently unknown. One possible explanation is that this type of service is harder to price-check through a public supplier source, but this is only my assumption and was not confirmed by Arnold. Another possibility is simply that the advance price check was not performed in this individual case.

This should therefore remain an open point rather than being used to conclude that all services are excluded from advance price checking.

## 4. Maximizing supplier orders instead of immediately purchasing every small request

A purchasing request from Johan had already been left open from the previous day because it was a small, non-urgent order.

Instead of immediately sending a separate PO for a small-value purchase, Arnold may leave such demand open temporarily and combine it with other demand from the same supplier. This is referred to here as **maximalisatie**.

The purpose is to create a more efficient supplier order. Sending a very small PO can still create ordering and transport costs, while combining demand may reduce unnecessary small orders and may sometimes improve commercial conditions such as discounts.

During the morning observation, Arnold spent roughly **4 minutes** adding one additional item while working through this type of supplier-order maximization.

## 5. Exact purchasing advice and adding advised items

For this process, Arnold can use an Exact screen that provides purchasing advice for open demand. Based on the observed workflow, the route was approximately related to purchasing items to process/open purchasing orders and opening a predefined view or template in which a row/field called **Advies** shows a recommended quantity to purchase.

The exact menu path should still be verified separately before it is documented as a definitive system instruction.

The advice appears to be based on demand generated by future projects or production requirements.

Arnold can use these advised quantities when combining multiple demands into one PO for the same supplier.

## 6. Toewijzen is necessary after combining demand into a PO

An important part of the observed workflow is that adding an advised quantity to a purchase order is not enough by itself.

After Arnold includes the advised components in a PO, the purchased quantity also needs to be **toegewezen** to the corresponding project or production demand.

If the purchased items are added to the supplier PO but are not assigned to the underlying demand, Exact can continue to treat that project or production demand as unfulfilled. As a result, the same demand may later appear again in the purchasing advice even though Arnold has already included the required quantity in an existing PO.

This creates a risk of duplicated purchasing if the assignment step is missed.

## 7. Concrete example: advised quantity and project allocation

Arnold spent approximately **30 to 35 minutes** on one case involving purchasing advice, order maximization, and assigning the purchased items correctly.

In this case, Exact showed an advised quantity of **2** for one component.

The important issue was not simply whether the number 2 was correct. Arnold had to understand which underlying project or production demands the advised quantity represented, combine the relevant demand into the current PO where appropriate, and then assign the purchased items back to those corresponding demands.

Without this assignment, Exact could later continue to show the same needs as open demand even though Arnold had already bought the items as part of the maximized supplier order.

This means that the purchasing workflow contains a relationship between:

1. future project or production demand;
2. the quantity advised by Exact;
3. the supplier PO into which Arnold combines the demand; and
4. the later **toewijzen** step that marks the underlying demand as covered by that purchase.

The 30 to 35 minute duration indicates that this can become a substantial task when several demands and project relationships have to be understood and allocated correctly.

## 8. Early-morning work appears deliberately focused on low-interruption purchasing tasks

Compared with the afternoon observation from 19 August, the early-morning period gives Arnold more uninterrupted time to work through open orders, historical checks, purchasing advice, and order allocation.

This supports the earlier observation that interruptions during the normal working day may affect how efficiently Arnold can complete purchasing tasks. It may therefore be useful to distinguish between:

- the intrinsic processing time of a purchasing task; and
- the additional elapsed time caused by interruptions, incoming requests, and task switching.

## Initial workload observations from this morning

The morning session provides several useful categories for further measurement:

- processing an already existing open order in Exact;
- manually creating a purchase order when the request originates through email or a colleague;
- manually transcribing information from screenshots or incomplete requests;
- correcting suspicious or incomplete technical information;
- searching historical POs to verify machine, serial-number, service, or supplier information;
- proactively checking supplier website prices for certain one-off or special purchases before sending a PO;
- manually searching components one by one on supplier websites and updating deviating prices in Exact;
- holding small non-urgent demand open for supplier-order maximization;
- using Exact purchasing advice to identify additional demand;
- assigning purchased quantities back to the corresponding project or production demand;
- preventing duplicated demand from reappearing because items were purchased but not assigned correctly.

## Approximate timings observed

These timings are single observations and should not yet be treated as averages:

- manually entering two service-related purchase lines: approximately **5 minutes**;
- investigating and correcting suspicious information using historical POs: approximately **10 to 15 minutes**;
- adding one item while working on a small-order maximization case: approximately **4 minutes**;
- purchasing-advice, maximization, and allocation case: approximately **30 to 35 minutes**.

Further observations are needed to determine how representative these durations are.

## Possible process and AI opportunities to investigate later

These remain hypotheses and are not selected solutions:

- structured intake for purchase requests that currently arrive through email, screenshots, or verbal requests;
- automatically extracting component/service information from screenshots or email requests and preparing a draft PO for Arnold to review;
- checking incoming descriptions, serial numbers, or other identifiers against historical Exact records and highlighting possible inconsistencies;
- making previous purchases for the same machine, service, supplier, or component easier to retrieve;
- supporting proactive comparison of current supplier prices with the prices stored in Exact before a PO is sent;
- identifying price records that may be stale and could otherwise be reused in later POs while supplier confirmation is pending;
- improving visibility of small open orders that could be combined with new demand from the same supplier;
- showing the relationship between Exact purchasing advice, the supplier PO, and the underlying project/production demand more clearly;
- reducing the risk that purchased quantities reappear as open demand because the toewijzen step was missed;
- supporting Arnold in identifying which purchasing activities require expert judgment and which are mainly administrative.

## Questions for further observation

- How often do purchasing requests originate outside Exact?
- What proportion arrive through email, screenshots, direct verbal requests, or other channels?
- How often is important information missing or incorrect in those requests?
- How often does Arnold need to search historical POs to correct or validate supplied information?
- Which fields are most commonly incorrect or missing?
- For which categories of purchases does Arnold perform an advance supplier-price check before sending the PO?
- Are services normally included in that advance price-check rule, or was that part of the explanation misunderstood?
- How often does the price stored in Exact differ from the current supplier website price before the PO is sent?
- How much time does proactive website price checking take for different order sizes?
- How many small non-urgent orders are intentionally held open for maximization?
- What rules or experience does Arnold use to decide when to stop waiting and place the combined order?
- What exactly determines the quantity shown in the Exact **Advies** field?
- How does Arnold determine which project or production demand each purchased quantity needs to be assigned to?
- How often does a missed or incorrect toewijzen step cause demand to reappear?
- Can Exact or Orbis expose the relationship between advised demand, supplier PO lines, and project/production assignments?
- How much faster is Arnold able to process comparable work between 07:00 and 09:00 compared with periods with frequent interruptions?

## Current interpretation

The morning observation strengthens the view that Arnold's workload comes from several different sources rather than one single purchasing task.

Some work is straightforward manual administration, such as creating a PO from information supplied outside Exact. Other work is investigative, such as recognizing suspicious technical information and searching historical POs to verify it. A further layer involves purchasing logic, such as combining small orders for the same supplier and correctly assigning purchased quantities to project or production demand.

The additional Technische Unie explanation shows that price control can also happen proactively before a PO is sent. For certain one-off or special purchases, Arnold manually checks current supplier prices so that an outdated Exact price is corrected before it can be reused in another purchase order. This should be analyzed separately from the later supplier-confirmation price check.

The most important new observation is that purchasing advice and order maximization cannot be analyzed only at the level of supplier PO quantities. The underlying project or production demand and the **toewijzen** step are important because failing to connect the purchase back to the demand can cause the same need to appear again later.

This makes the process suitable for further task decomposition before choosing an AI or automation use case.