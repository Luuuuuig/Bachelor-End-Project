"""Kinds-of-work review for the saturation question.

Part of step 3 of analysis/Analysis_Plan_2026-09-30.md. Reads the combined table
built by build_combined_table.py, assigns each row the kinds of work its note
supports (the mapping M below) and writes:
  analysis/Kinds_Of_Work_Review_2026-09-30.md       the review table and the code x stage cross-check
  analysis/output/Kinds_Of_Work_Rows_2026-09-30.csv  one line per row with its kinds, for checking
Run from the repository root after build_combined_table.py.
"""

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMBINED = ROOT / "analysis" / "output" / "Arno_Combined_2026-09-30.csv"
REVIEW = ROOT / "analysis" / "Kinds_Of_Work_Review_2026-09-30.md"
ROWS = ROOT / "analysis" / "output" / "Kinds_Of_Work_Rows_2026-09-30.csv"

DAYS = ["2026-08-31", "2026-09-01", "2026-09-08", "2026-09-18", "2026-09-23"]
LABEL = dict(zip(DAYS, ["31 Aug", "1 Sep", "8 Sep", "18 Sep", "23 Sep"]))

KINDS = {
    "K01": ("Receive a request", "Intake of a request: every row coded REQ, on all five days, next to any kind its note shows."),
    "K02": ("Create or complete a PO for a need", "Enter or amend PO lines in Exact for a need, including adding lines, ordering via a supplier website and PO paperwork."),
    "K03": ("Maximalisatie and HOLD/order decision", "Combine demand into an open PO for the same supplier, or try to, and decide to hold or order."),
    "K04": ("Check before ordering", "Check price, and ETA where the supplier states it, against a quotation, website or supplier information before the PO is sent."),
    "K05": ("Send or forward the PO", "Send the generated PO, or an approved PO, to the supplier."),
    "K06": ("Credit-card purchase", "Buy through the credit-card route instead of the normal PO route."),
    "K07": ("Approval-related handling", "Handling connected to Johan's approval: forwarding an approved PO, or noting that approval is awaited or needed again. Why approval was needed is not recorded, and the minutes are not measured approval or waiting time."),
    "K08": ("Clarify missing or unclear request information", "Ask the requester or another party for information needed to complete an already defined request."),
    "K09": ("Establish or judge the requirement", "Decide what exactly is needed: which option, technical suitability, whether an item is interchangeable."),
    "K10": ("Search historical POs or records", "Look up earlier orders or item history to identify or verify an item."),
    "K11": ("Retrieve or complete drawings", "Find, request or check drawings needed for an order."),
    "K12": ("Article or supplier data in Exact", "Create or maintain article or supplier records, including requests and coordination about them."),
    "K13": ("Search for another supplier or better price", "Look for an alternative or cheaper supplier, or ask for a better price."),
    "K14": ("Handle an unavailable item", "Deal with an item a supplier cannot deliver: drop it, move it to another order or replace it."),
    "K15": ("Adjust an existing PO on request", "Change an existing PO after a request about it."),
    "K16": ("Cancel a component or order line", "Arrange the cancellation of a component or line, including the related PO change."),
    "K17": ("Check a supplier confirmation", "After ordering: compare the confirmation with the PO on price and ETA, update Exact, attach the confirmation."),
    "K18": ("Investigate a price discrepancy", "Look into a price difference, including documenting it."),
    "K19": ("Follow up order status or delivery", "Supplier or internal question about an existing order: ETA, backorder, delay, partial delivery."),
    "K20": ("Finance-related issue", "Unpaid invoices that block suppliers or checks, Finance questions, passing information to Finance."),
    "K21": ("Aftercare on a delivered order", "Wrong or incorrect items received, or other aftercare on an earlier order."),
    "K22": ("Certification arrangements", "Arranging certification by an external body (Lloyd), outside EXC. Its scope needs separate consideration."),
    "K31": ("Missing or attached certificate", "A missing certificate, or attaching a certificate to a PO, recorded as EXC aftercare."),
    "K23": ("Logistics coordination", "Warehouse stock, collection, transport or questions about received items with Logistics."),
    "K24": ("Internal coordination with colleagues", "Discussions with or answers to colleagues such as Dennis, Johan or Emiel, and passing information on."),
    "K25": ("Service or transport purchase", "Purchasing a service such as maintenance, a service order or transport."),
    "K26": ("Exact error or delay", "A fault or delay in Exact that affects the work."),
    "K27": ("Read or organise purchasing email", "Reading or sorting purchasing email without a specific case."),
    "K28": ("Quotation or offer handling", "Request, find, review or forward a quotation or offer."),
    "K29": ("Question from a customer, Sales or Service", "A question that reaches purchasing from a customer, Sales or Service."),
    "K30": ("Administrative booking in Exact", "Binnenboeken: administrative booking work in Exact."),
}

# (date, row) -> kinds. Rows without enough detail are left out on purpose.
M = {}
def put(date, rows, *kinds):
    for r in rows:
        M[(date, r)] = list(kinds)

d = "2026-08-31"
put(d, [1, 2, 58], "K09"); put(d, [3, 6, 8, 15, 28, 31, 34, 36, 40, 43, 47, 50, 54], "K01")
put(d, [4, 10, 29, 32, 41, 55, 59], "K02"); put(d, [5], "K05", "K26")
put(d, [9, 11], "K04"); put(d, [12, 18, 30, 33, 42, 53, 56], "K05")
put(d, [13, 45, 46], "K17"); put(d, [14, 27, 57], "K21"); put(d, [16, 17], "K25")
put(d, [19, 20, 21, 22, 23, 24, 25, 26, 63], "K12"); put(d, [35, 48, 49], "K06")
put(d, [37, 38, 39, 51, 52], "K03"); put(d, [44], "K08"); put(d, [60, 61, 62], "K20")

d = "2026-09-01"
put(d, [1, 5, 6, 14], "K21"); put(d, [2, 9, 29], "K01"); put(d, [3, 4, 10, 11], "K08")
put(d, [7], "K16"); put(d, [8], "K09", "K16"); put(d, [12, 22, 23, 24], "K17")
put(d, [13, 17], "K20"); put(d, [15, 18, 25, 32], "K19"); put(d, [16], "K20", "K19")
put(d, [19, 35], "K29"); put(d, [20], "K10"); put(d, [21], "K28")
put(d, [26, 27, 28, 33], "K12"); put(d, [30], "K04", "K20"); put(d, [31], "K14", "K13")
put(d, [34], "K27"); put(d, [36, 37, 38, 41, 42, 43, 44], "K02"); put(d, [39, 40], "K15")
put(d, [45, 46, 47, 48, 49, 50], "K03")

d = "2026-09-08"
put(d, [1, 2], "K21"); put(d, [3], "K20"); put(d, [4, 5, 6, 16, 17], "K16")
put(d, [7, 20, 23], "K01"); put(d, [9], "K25"); put(d, [10], "K23"); put(d, [11, 28], "K05")
put(d, [12], "K19"); put(d, [13, 14, 15, 39], "K24"); put(d, [18, 27, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42], "K02")
put(d, [19], "K30"); put(d, [21], "K04"); put(d, [22], "K09", "K24"); put(d, [25], "K12")
put(d, [26], "K14", "K13", "K12"); put(d, [29], "K14"); put(d, [30, 31], "K03")

d = "2026-09-18"
# Row 9 (Primer-C) stays unclassified: the note marks it [uncertain].
put(d, [1, 6, 7, 17, 23, 36, 37, 38], "K17")
put(d, [3, 74], "K18"); put(d, [5], "K20", "K19"); put(d, [8, 35, 44, 45, 70, 71], "K19")
put(d, [11, 30, 32, 52, 54, 56], "K02"); put(d, [12, 33, 34, 59, 62], "K05")
put(d, [13, 14, 24], "K14"); put(d, [15, 16], "K22"); put(d, [43, 68, 69], "K31"); put(d, [18, 19, 20, 21, 22, 39, 42], "K23")
put(d, [25], "K02", "K14"); put(d, [27], "K11", "K02"); put(d, [28, 40, 41], "K11"); put(d, [31], "K08", "K11")
put(d, [46], "K19", "K21"); put(d, [47, 50], "K05", "K07"); put(d, [48, 49], "K13"); put(d, [55, 67], "K07")
# Row 66 (OBS-21) is K04 only: a mismatch is recorded, but its share of the 20 minutes is unknown.
# Row 73 (OBS-29) is K18 only: its case note leaves the control point open (not a confirmation check).
put(d, [58, 61, 64], "K03"); put(d, [65], "K21"); put(d, [66], "K04")
put(d, [72], "K28"); put(d, [73], "K18")

d = "2026-09-23"
put(d, [1, 2, 3, 4, 5, 6, 8, 14, 18, 39, 45], "K02"); put(d, [9, 11, 19, 28, 32, 37, 43, 49], "K01")
put(d, [10], "K29"); put(d, [12, 13, 17, 52], "K19"); put(d, [15], "K04"); put(d, [16, 25, 26, 41, 42, 58], "K05")
put(d, [20, 22, 23, 24], "K25"); put(d, [21], "K26"); put(d, [27, 30, 51, 55, 56], "K23")
put(d, [33, 57], "K03"); put(d, [34], "K11"); put(d, [35], "K28"); put(d, [38], "K10"); put(d, [40], "K09")
put(d, [44], "K19", "K20"); put(d, [47], "K24"); put(d, [53, 54], "K12")

KNOWN = {
    "K07": "Yes: the approval route above about €10,000 was described on 21 August.",
    "K10": "Yes: 20 August note; AS-IS Task 5.",
    "K11": "Yes: 28 August pilot; AS-IS Tasks 4–5.",
    "K13": "Yes: supplier search is described for Dennis (15 September) and in the AS-IS process.",
    "K14": "Yes: 19 August (Technische Unie); AS-IS Task 31.",
    "K15": "Yes: ordinary order work.",
    "K16": "Partly: cancellations are named as EXC work in the scope addendum.",
    "K18": "Yes: price mismatches were described on 17 and 19 August.",
    "K19": "Yes: monitoring in the AS-IS process.",
    "K22": "No: Lloyd certification arrangements were not described before.",
    "K23": "Yes: Logistics process, 9 September note.",
    "K24": "Yes: role overlap, 8 September meeting with Johan.",
    "K27": "Yes: email handling, 19 August note.",
    "K28": "Yes: quotations as part of request completion.",
    "K29": "Yes: known request channels.",
    "K30": "No: not described before.",
    "K31": "Partly: medical-goods documentation was described on 9 September.",
}

ADDS = {
    "K03": "Some: failed maximalisatie attempts (18 Sep OBS-23/24; 23 Sep OBS-12, where the supplier no longer had the component).",
    "K04": "Yes: the 29-line pre-check on 18 Sep (OBS-21) found a hard-to-explain mismatch and Johan's approval was needed again; on 1 Sep (OBS-18) an unpaid invoice blocked the price part.",
    "K07": "Yes: approval had to be repeated after a pre-check mismatch (18 Sep OBS-21), a possible rework loop.",
    "K10": "Recurs (23 Sep tube history); no new information.",
    "K11": "Yes: on 23 Sep Engineering had omitted part of the drawing set (OBS-12), a specific hand-off problem.",
    "K12": "Some: article work on 1 Sep could not be finished because required data were missing (31AUG-OBS-07).",
    "K17": "Yes: a large confirmation check (32 lines) on 18 Sep; updating the ETA is part of the check (clarified 30 Sep).",
    "K18": "Yes: supports the price-control candidate. The €410 difference on 18 Sep (OBS-29) was linked to a small order quantity; the note does not say at which control point it was found. The OBS-21 pre-check also contained a mismatch, but its share of the 20 minutes is unknown.",
    "K20": "Yes: unpaid invoices blocked supplier deliveries and a price check (31 Aug OBS-16, 1 Sep OBS-18, 18 Sep OBS-03), a Finance hand-off issue.",
    "K22": "Possibly: non-EXC work whose scope needs separate consideration.",
    "K25": "Some: the scope of the 23 Sep service order is still unclear.",
    "K26": "Some: a 12-minute Exact fault on 23 Sep shows system problems can cost real time.",
    "K30": "Unclear: a one-off; worth one question to Arno.",
    "K31": "No for the shortlist: EXC aftercare.",
}


def load():
    with COMBINED.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for r in rows:
        r["row"] = int(r["row"])
        r["minutes"] = int(r["minutes"]) if r["minutes"] else 0
        r["kinds"] = list(M.get((r["date"], r["row"]), []))
        if r["family"] == "REQ" and "K01" not in r["kinds"]:
            r["kinds"].insert(0, "K01")
        assert len(r["kinds"]) <= 3, (r["date"], r["row"])
        r["lost"] = r["flag_lost_focus"] == "1"
    return rows


def table(header, body):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join(out)


def main():
    rows = load()
    with ROWS.open("w", encoding="utf-8", newline="") as handle:
        w = csv.writer(handle)
        w.writerow(["date", "row", "case", "code", "minutes", "stage", "kinds", "kind_names", "note"])
        for r in rows:
            w.writerow([r["date"], r["row"], r["case"], r["activity_as_written"], r["minutes"] or "",
                        r["stage"], ";".join(r["kinds"]), "; ".join(KINDS[k][0] for k in r["kinds"]), r["note"]])

    seen = defaultdict(list)
    for r in rows:
        for k in r["kinds"]:
            seen[k].append(r)
    first_day = {k: min(DAYS.index(r["date"]) for r in v) for k, v in seen.items()}

    body = []
    for k in sorted(seen, key=lambda k: (first_day[k], k)):
        v = seen[k]
        first = min(v, key=lambda r: (DAYS.index(r["date"]), not r["note"].strip(" /—"), r["row"]))
        days = sorted({r["date"] for r in v}, key=DAYS.index)
        again = "yes, " + ", ".join(LABEL[d] for d in days[1:]) if len(days) > 1 else "no"
        note = (first["note"][:70] + "…") if len(first["note"]) > 70 else first["note"]
        known = "Seen on day 1." if first_day[k] == 0 else KNOWN.get(k, "")
        adds = ADDS.get(k, "No new information beyond recurrence.")
        lost = sum(r["minutes"] for r in v if r["lost"])
        minutes = sum(r["minutes"] for r in v if not r["lost"])
        minutes_text = f"{minutes} (+{lost} lost focus)" if lost else minutes
        body.append([k, KINDS[k][0], KINDS[k][1], f"{LABEL[first['date']]}, row {first['row']} ({first['case']}): {note or 'no note'}",
                     again, len(v), minutes_text, known, adds])

    counts = [sum(1 for k in seen if first_day[k] == i) for i in range(5)]
    unclassified = [sum(1 for r in rows if r["date"] == d and not r["kinds"]) for d in DAYS]
    unclassified_min = [sum(r["minutes"] for r in rows if r["date"] == d and not r["kinds"]) for d in DAYS]
    cum = [sum(counts[:i + 1]) for i in range(5)]
    assigned = sum(1 for r in rows if r["kinds"])
    lines = [
        "# Kinds of work across the five days, Arno",
        "",
        "Prepared 30 September 2026 as a retrospective evidence review for the saturation question: does a later day still add material new information? "
        "Each row's kind is assigned from its note and case context in the reviewed daily CSVs; the assignments are in "
        "[`output/Kinds_Of_Work_Rows_2026-09-30.csv`](output/Kinds_Of_Work_Rows_2026-09-30.csv). A row can show up to three kinds. "
        f"{assigned} of {len(rows)} rows have a kind; the others have too little detail and are left out rather than guessed. "
        "This review supports the decision to pause broad observation; it is not proof of complete saturation.",
        "",
        "## Kinds of work: first appearance, recurrence and importance",
        "",
        table(["ID", "Kind of work", "Definition", "First seen (row and note)", "Seen again", "Rows", "Minutes", "Already known before?", "Adds information relevant to improvement?"], body),
        "",
        "Minutes are the recorded minutes of the rows showing each kind. A row with two kinds counts under both, so these are episode totals per label, not an additive workload ranking. The 9 lost-focus minutes on 8 September are shown separately and left out of the totals.",
        "",
        "## Coding rules and deliberate exclusions",
        "",
        "- **Intake (K01):** every row coded REQ gets K01 on all five days, next to any kind its note shows (for example 1 Sep row 7 is K01 and K16). K01 records that a request arrived, not what it asked for.",
        "- **18 Sep row 9 (Primer-C):** left without a kind because the note marks it [uncertain].",
        "- **18 Sep row 66 (OBS-21 pre-check, 20 minutes):** K04 only. The mismatch is mentioned under K18, but its minutes are not counted there because its share of the 20 minutes is unknown.",
        "- **18 Sep row 73 (OBS-29, 6 minutes):** K18 only. The case note does not say whether the difference was found before ordering, at confirmation or at invoicing, so it is not also counted as a confirmation check (K17).",
        "- **8 Sep, 12:04–12:13 (OBS-16, rows 35–36):** the 9 lost-focus minutes keep their kind but are shown separately and left out of the minute totals.",
        "- **Rows without a kind:** CLAR or CHECK rows with no note (empty or `/`, which means none) or a note of only \"Pause for now\" or \"Forward\", which does not say what the work concerned; they are listed in the rows file with an empty kinds column. No kind is guessed from the case alone.",
        "",
        "## New kinds per day",
        "",
        table(["", *[LABEL[d] for d in DAYS]],
              [["New kinds", *counts], ["Kinds seen so far", *cum],
               ["Rows without a kind", *unclassified], ["Their minutes", *unclassified_min]]),
        "",
        f"- **Days 1–3 as a base, days 4–5 as the run:** {counts[3] + counts[4]} new kinds against a base of {cum[2]} "
        f"({100 * (counts[3] + counts[4]) / cum[2]:.0f}%).",
        f"- **Days 1–4 as a base, day 5 as the run:** {counts[4]} new kinds against {cum[3]} ({100 * counts[4] / cum[3]:.0f}%).",
        f"- **23 September:** the classified rows introduced no additional kind under this coding scheme. "
        f"{unclassified[4]} rows ({unclassified_min[4]} minutes) that day have too little detail to classify, so this does not show that no new work or information occurred.",
        "- These base and run sizes are an adaptation of Guest, Namey and Chen (2020), who tested bases of 4–6 interviews and runs of 2–3 and call the 5% level an optional benchmark. "
        "The count is a retrospective description, not a validated stopping rule; the importance column matters more.",
        "",
    ]

    combos = defaultdict(set)
    for r in rows:
        combos[(r["family"], r["stage"])].add(r["date"])
    first = defaultdict(list)
    for (fam, stage), ds in combos.items():
        first[min(DAYS.index(d) for d in ds)].append(f"{fam} × {stage}")
    body = [[LABEL[DAYS[i]], len(first[i]), ", ".join(sorted(first[i])) or "—"] for i in range(5)]
    lines += [
        "## Cross-check: activity code × stage",
        "",
        "Every combination of activity code and reviewed stage, by the day it first appears. This is coarse: new problems inside an existing code do not show here.",
        "",
        table(["Day", "New combinations", "Which"], body),
        "",
    ]
    REVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REVIEW.relative_to(ROOT)} and {ROWS.relative_to(ROOT)}")
    print("new kinds per day", counts, "cumulative", cum, "assigned rows", assigned)
    print("code x stage new per day", [len(first[i]) for i in range(5)])


if __name__ == "__main__":
    main()
