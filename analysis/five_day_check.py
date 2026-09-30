"""Five-day coverage, stability and saturation check for Arno's baseline.

Step 3 of analysis/Analysis_Plan_2026-09-30.md. Reads the combined table from
build_combined_table.py and the observation-time register, applies the rules
in the plan and writes analysis/Five_Day_Coverage_Check_2026-09-30.md.
Run from the repository root after build_combined_table.py.
"""

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMBINED = ROOT / "analysis" / "output" / "Arno_Combined_2026-09-30.csv"
REGISTER = ROOT / "docs" / "measurement" / "Observation_Time_Register_2026-09-25.csv"
REPORT = ROOT / "analysis" / "Five_Day_Coverage_Check_2026-09-30.md"

DAYS = ["2026-08-31", "2026-09-01", "2026-09-08", "2026-09-18", "2026-09-23"]
LABEL = {"2026-08-31": "31 Aug", "2026-09-01": "1 Sep", "2026-09-08": "8 Sep",
         "2026-09-18": "18 Sep", "2026-09-23": "23 Sep"}
FAMILY_ORDER = ["PO", "CLAR", "CHECK", "SEND", "OTHER", "REQ", "DEC", "EXC", "UNCLEAR"]
STAGE_ORDER = ["Specification", "Supplier selection", "Ordering", "Monitoring",
               "Follow-up and evaluation", "Not applicable", "(blank)"]
AFTERNOON_FROM = 12 * 60 + 45
SHARE_LIMIT = 5.0      # percentage points (S2, S4)
RATE_LIMIT = 10.0      # percent (S3)
RATE_FLOOR = 1.0       # occurrences per observed hour (S3)

# Q2: kinds of work first seen on day 5, from the observation notes.
FIRST_ON_DAY5 = [
    ("OBS-09, 11:49–12:01", "Troubleshooting a fault in Exact as its own 12-minute episode (stage Not applicable).",
     "An Exact error was recorded earlier inside a SEND row (31 Aug OBS-02). A separate troubleshooting episode was seen once. It is system support, not a new purchasing activity, so it does not affect candidate selection. Treated as a one-off pending further evidence."),
    ("OBS-16, 13:42–14:24", "Helping Logistics locate an item that had already been received (42 minutes, EXC).",
     "Short logistics coordination with Maurice was seen on 18 Sep (OBS-08, OBS-12). Arno said this situation usually never happens. One-off; EXC."),
]


def clock(value):
    match = re.fullmatch(r"\s*(\d{1,2}):(\d{2})\s*", value or "")
    return int(match.group(1)) * 60 + int(match.group(2)) if match else None


def load_rows():
    with COMBINED.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["minutes"] = int(row["minutes"]) if row["minutes"] else 0
        for key in ("timed", "flag_exc", "flag_lost_focus"):
            row[key] = int(row[key])
    return rows


def load_exposure():
    """Net observation per day and per daypart from the register."""
    with REGISTER.open(encoding="utf-8-sig") as handle:
        register = {r["date"]: r for r in csv.DictReader(handle)}
    exposure = {}
    for day in DAYS:
        entry = register[day]
        parts = Counter()
        for block in entry["notebook_or_recorded_blocks"].split(";"):
            start, end = (clock(x) for x in block.strip().split("-"))
            parts["Morning" if start < AFTERNOON_FROM else "Afternoon"] += end - start
        for gap in re.findall(r"(\d{1,2}:\d{2})-(\d{1,2}:\d{2})", entry["documented_unobserved_intervals"]):
            start, end = clock(gap[0]), clock(gap[1])
            parts["Morning" if start < AFTERNOON_FROM else "Afternoon"] -= end - start
        net = int(entry["confirmed_net_observed_minutes"])
        assert sum(parts.values()) == net, day
        exposure[day] = {"net": net, "blocks": entry["notebook_or_recorded_blocks"], **parts}
    return exposure


def view(rows, with_exc):
    return rows if with_exc else [r for r in rows if not r["flag_exc"]]


def minutes_by(rows, key):
    totals = Counter()
    for row in rows:
        if row["timed"]:
            totals[row[key]] += row["minutes"]
    return totals


def shares(rows, key):
    totals = minutes_by(rows, key)
    whole = sum(totals.values())
    return {k: 100 * v / whole for k, v in totals.items()} if whole else {}


def ordered(keys, order):
    return [k for k in order if k in keys] + sorted(k for k in keys if k not in order)


def fmt(value, digits=1):
    return f"{value:.{digits}f}"


def is_number(value):
    return bool(re.fullmatch(r"[-+]?\d+(\.\d+)?%?", str(value).strip()))


def table(header, rows):
    numeric = [i > 0 and all(is_number(r[i]) for r in rows if str(r[i]).strip()) for i in range(len(header))]
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join("---:" if n else "---" for n in numeric) + "|"]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def coverage_section(rows, exposure):
    out = ["## 1. Coverage", ""]
    body = []
    for day in DAYS:
        day_rows = [r for r in rows if r["date"] == day]
        e = exposure[day]
        body.append([LABEL[day], day_rows[0]["weekday"], e["blocks"].replace("-", "–"), e.get("Morning", 0),
                     e.get("Afternoon", 0), e["net"], len(day_rows), sum(r["timed"] for r in day_rows),
                     sum(r["minutes"] for r in day_rows), sum(r["minutes"] for r in day_rows if r["flag_exc"])])
    body.append(["**Total**", "", "", sum(exposure[d].get("Morning", 0) for d in DAYS),
                 sum(exposure[d].get("Afternoon", 0) for d in DAYS), sum(exposure[d]["net"] for d in DAYS),
                 len(rows), sum(r["timed"] for r in rows), sum(r["minutes"] for r in rows),
                 sum(r["minutes"] for r in rows if r["flag_exc"])])
    out += [table(["Day", "Weekday", "Observation blocks", "Morning net min", "Afternoon net min",
                   "Net min", "Rows", "Timed rows", "Recorded min", "of which EXC"], body), ""]

    channels = sorted({r["request_channel"] for r in rows if r["family"] == "REQ"})
    body = []
    for channel in channels:
        body.append([channel] + [sum(1 for r in rows if r["date"] == d and r["family"] == "REQ"
                                     and r["request_channel"] == channel) for d in DAYS])
    out += ["**Request channels** (REQ occurrences):", "",
            table(["Channel"] + [LABEL[d] for d in DAYS], body), ""]

    families = ordered({r["family"] for r in rows}, FAMILY_ORDER)
    body = [[f] + [sum(1 for r in rows if r["date"] == d and r["family"] == f) for d in DAYS] for f in families]
    out += ["**Activity codes** (occurrences, timed and untimed):", "",
            table(["Code"] + [LABEL[d] for d in DAYS], body), ""]

    out += ["**Coverage gaps (documented, not automatically a reason to observe more):**", "",
            "- **Weekday:** no Thursday (the weekly supervision meeting). Monday, Tuesday (twice), Wednesday and Friday are covered. On 17 September the supervisor advised treating this as a limitation only if patterns differ across days; see section 2.",
            "- **Time of day:** all measured observation falls between 10:30 and 15:00. The early morning (from about 07:00) was observed on 20 August but not measured; the kinds of work seen then also appear in the measured sessions.",
            f"- **Daypart balance:** {sum(exposure[d].get('Morning', 0) for d in DAYS)} morning and {sum(exposure[d].get('Afternoon', 0) for d in DAYS)} afternoon net minutes; 8 September has a morning block only.",
            "- **Channels:** email, Exact, phone, desk and letter requests all occur; several requests have no recorded channel.", ""]
    return out


def stability_section(rows, exposure, with_exc):
    name = "A. All data" if with_exc else "B. Without EXC"
    data = view(rows, with_exc)
    first4 = [r for r in data if r["date"] in DAYS[:4]]
    results = {}
    out = [f"### {name}", ""]

    # Per-day and cumulative family shares.
    families = ordered({r["family"] for r in data if r["timed"]}, FAMILY_ORDER)
    per_day = {d: shares([r for r in data if r["date"] == d], "family") for d in DAYS}
    cum = {k: shares([r for r in data if r["date"] in DAYS[:k]], "family") for k in range(1, 6)}
    body = []
    for f in families:
        body.append([f] + [fmt(per_day[d].get(f, 0)) for d in DAYS] +
                     [fmt(cum[4].get(f, 0)), fmt(cum[5].get(f, 0)), fmt(cum[5].get(f, 0) - cum[4].get(f, 0))])
    out += ["**Time share by activity code (%).** Per day, then cumulative over days 1–4 and 1–5.", "",
            table(["Code"] + [LABEL[d] for d in DAYS] + ["Days 1–4", "Days 1–5", "Change"], body), ""]

    # S1: leave-one-day-out top two.
    top_all = [f for f, _ in sorted(cum[5].items(), key=lambda kv: -kv[1])[:2]]
    body, s1 = [], True
    for d in DAYS:
        s = shares([r for r in data if r["date"] != d], "family")
        top = [f for f, _ in sorted(s.items(), key=lambda kv: -kv[1])[:2]]
        same = set(top) == set(top_all)
        s1 &= same
        body.append([f"without {LABEL[d]}", ", ".join(f"{f} {fmt(s[f])}%" for f in top), "yes" if same else "**no**"])
    results["S1"] = s1
    out += [f"**S1, leave one day out.** Top two over all five days: {' and '.join(top_all)}.", "",
            table(["Left out", "Top two (share)", "Same pair"], body), ""]

    # S2: day-5 change in cumulative family shares.
    worst = max(families, key=lambda f: abs(cum[5].get(f, 0) - cum[4].get(f, 0)))
    change = cum[5].get(worst, 0) - cum[4].get(worst, 0)
    results["S2"] = abs(change) < SHARE_LIMIT
    out += [f"**S2, day-5 change in time shares.** Largest change: {worst} {change:+.1f} points "
            f"(limit {SHARE_LIMIT:.0f}). {'Met' if results['S2'] else '**Not met**'}.", ""]

    # S3: rates per observed hour.
    hours4 = sum(exposure[d]["net"] for d in DAYS[:4]) / 60
    hours5 = sum(exposure[d]["net"] for d in DAYS) / 60
    count4 = Counter(r["family"] for r in first4)
    count5 = Counter(r["family"] for r in data)
    body, s3 = [], True
    for f in ordered(count5.keys(), FAMILY_ORDER):
        rate4, rate5 = count4[f] / hours4, count5[f] / hours5
        pct = 100 * (rate5 - rate4) / rate4 if rate4 else float("inf")
        tested = rate5 >= RATE_FLOOR
        ok = abs(pct) < RATE_LIMIT
        if tested:
            s3 &= ok
        body.append([f, fmt(rate4, 2), fmt(rate5, 2), f"{pct:+.0f}%",
                     ("yes" if ok else "**no**") if tested else "not tested (<1/h)"])
    results["S3"] = s3
    out += [f"**S3, occurrences per observed hour.** Days 1–4: {hours4:.1f} h; days 1–5: {hours5:.1f} h. "
            f"Limit ±{RATE_LIMIT:.0f}% for codes with at least {RATE_FLOOR:.0f} per hour.", "",
            table(["Code", "Days 1–4", "Days 1–5", "Change", "Within limit"], body), ""]

    # S4: stage shares.
    s4_4, s4_5 = shares(first4, "stage"), shares(data, "stage")
    stages = ordered(set(s4_4) | set(s4_5), STAGE_ORDER)
    body = [[s, fmt(s4_4.get(s, 0)), fmt(s4_5.get(s, 0)), fmt(s4_5.get(s, 0) - s4_4.get(s, 0))] for s in stages]
    worst_stage = max(stages, key=lambda s: abs(s4_5.get(s, 0) - s4_4.get(s, 0)))
    results["S4"] = abs(s4_5.get(worst_stage, 0) - s4_4.get(worst_stage, 0)) < SHARE_LIMIT
    out += [f"**S4, time share by Van Weele stage (%).** {'Met' if results['S4'] else '**Not met**'}.", "",
            table(["Stage", "Days 1–4", "Days 1–5", "Change"], body), ""]
    return out, results


def saturation_section(rows):
    earlier = [r for r in rows if r["date"] in DAYS[:4]]
    day5 = [r for r in rows if r["date"] == DAYS[4]]
    out = ["## 3. Saturation", ""]
    new = {}
    for key, label in (("family", "activity codes"), ("stage", "stages"), ("request_channel", "request channels")):
        seen = {r[key] for r in earlier if r[key]}
        new[label] = sorted({r[key] for r in day5 if r[key]} - seen)
    q1 = not any(new.values())
    out += [f"**Q1, new codes, stages or channels on day 5.** {'Met' if q1 else '**Not met**'}: "
            + "; ".join(f"{k}: {', '.join(v) if v else 'none new'}" for k, v in new.items()) + ".", ""]
    out += ["**Q2, kinds of work first seen on day 5** (from the 23 September note):", "",
            table(["Row", "Work", "Earlier evidence and judgement"], FIRST_ON_DAY5), "",
            "The other day-5 work (missing drawings, a specification question, an item-creation request, maximalisatie, a service order, forwarding an offer and a transport enquiry) was already seen on earlier days.", ""]
    return out, {"Q1": q1, "Q2": True}


def meaning_section(rows, exposure, results):
    """Plain-language reading of the result, built from the same numbers."""
    checks = {d: sum(1 for r in rows if r["date"] == d and r["family"] == "CHECK") for d in DAYS}
    check_min = {d: sum(r["minutes"] for r in rows if r["date"] == d and r["family"] == "CHECK") for d in DAYS}
    exc_share = {d: 100 * sum(r["minutes"] for r in rows if r["date"] == d and r["flag_exc"]) /
                 sum(r["minutes"] for r in rows if r["date"] == d) for d in DAYS}
    na_day5 = sorted((r for r in rows if r["date"] == DAYS[4] and r["stage"] == "Not applicable" and r["timed"]),
                     key=lambda r: -r["minutes"])
    big = na_day5[0]
    top_all = sorted(shares(rows, "family").items(), key=lambda kv: -kv[1])[:2]
    flip_days = []
    for d in DAYS:
        s = shares([r for r in rows if r["date"] != d], "family")
        if {f for f, _ in sorted(s.items(), key=lambda kv: -kv[1])[:2]} != {f for f, _ in top_all}:
            flip_days.append(d)
    out = ["## 5. What this means", "",
           "**Without EXC (view B, the current scope rule).** The main pattern is stable: PO and CLAR are the two largest "
           "activity codes whichever day is left out, and day 5 moved no time share by 5 points or more. "
           "The one rule not met is the CHECK frequency: CHECK occurred " +
           ", ".join(str(checks[d]) for d in DAYS[:4]) + f" and {checks[DAYS[4]]} times on the five days (" +
           ", ".join(str(check_min[d]) for d in DAYS[:4]) + f" and {check_min[DAYS[4]]} minutes). "
           "CHECK therefore varies strongly from day to day, and most of its time comes from 18 September.", "",
           "**With EXC (view A).** EXC is the largest or second-largest code on most days, but its share varies from "
           + " to ".join(f"{min(exc_share.values()):.0f}%" if i == 0 else f"{max(exc_share.values()):.0f}%" for i in range(2)) +
           " of a day's minutes, so the top pair changes when " + " or ".join(LABEL[d] for d in flip_days) +
           " is left out. "
           f"The stage rule fails mainly because of the {big['minutes']}-minute {big['case']} episode on 23 September "
           "(stage Not applicable), which Arno described as unusual.", "",
           "**Coverage.** No Thursday and no measured time before 10:30 or after 15:00. Because the main pattern "
           "without EXC is consistent across the five days, the missing Thursday is a limitation rather than a gap "
           "that changes the result, following the supervisor's advice of 17 September.", "",
           "**Saturation.** Day 5 brought no new activity code, stage or request channel. The two kinds of work "
           "first seen on day 5 are judged one-off.", "",
           "**Open for the supervisor discussion:**", "",
           "1. Confirm the proposed thresholds (5 points for shares, 10% for rates).",
           "2. Decide how to treat CHECK. One extra session is unlikely to settle a 10% rate rule on its own, because "
           "CHECK varies between 1 and 8 occurrences per session. The options are to report CHECK frequency as "
           "variable, with its range, or to observe more days.",
           "3. Decide on EXC. With EXC included, the ranking depends on which days are observed, because EXC work "
           "comes in irregular episodes.",
           "4. If the thresholds and the CHECK treatment are accepted, Measure can close for Arno.", ""]
    return out


def main():
    rows = load_rows()
    exposure = load_exposure()
    lines = ["# Five-day coverage check, Arno", "",
             "**Run:** 30 September 2026, following [the analysis plan](Analysis_Plan_2026-09-30.md). "
             "**Data:** [combined table](output/Arno_Combined_2026-09-30.csv) built from the five reviewed daily CSVs; "
             "no row dropped. **Thresholds** are proposed and still need the supervisor's confirmation. "
             "Generated by `analysis/five_day_check.py`; do not edit by hand.", ""]
    lines += coverage_section(rows, exposure)
    lines += ["## 2. Stability", "",
              "Every result is shown for view A (all data) and view B (without EXC). "
              "The 9 lost-focus minutes on 8 September stay in both views.", ""]
    all_results = {}
    for with_exc in (True, False):
        part, res = stability_section(rows, exposure, with_exc)
        lines += part
        all_results["A" if with_exc else "B"] = res
    sat_lines, sat = saturation_section(rows)
    lines += sat_lines

    lines += ["## 4. Result", "",
              table(["Rule", "A. All data", "B. Without EXC"],
                    [[rule] + [("met" if all_results[v][rule] else "**not met**") for v in ("A", "B")]
                     for rule in ("S1", "S2", "S3", "S4")] +
                    [["Q1", "met" if sat["Q1"] else "**not met**", "same"],
                     ["Q2", "day-5 novelties judged one-off", "same"]]), ""]
    lines += meaning_section(rows, exposure, all_results)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)}")
    for v, res in all_results.items():
        print(v, res)
    print("saturation", sat)


if __name__ == "__main__":
    main()
