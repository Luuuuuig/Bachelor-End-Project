"""Five-day coverage, stability and saturation check for Arno's baseline.

Step 3 of analysis/Analysis_Plan_2026-09-30.md. Reads the combined table from
build_combined_table.py, the kinds of work from kinds_of_work_review.py and the
observation-time register, and writes analysis/Five_Day_Coverage_Check_2026-09-30.md.
Run from the repository root after build_combined_table.py and kinds_of_work_review.py.
"""

import csv
import re
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMBINED = ROOT / "analysis" / "output" / "Arno_Combined_2026-09-30.csv"
KINDS = ROOT / "analysis" / "output" / "Kinds_Of_Work_Rows_2026-09-30.csv"
REGISTER = ROOT / "docs" / "measurement" / "Observation_Time_Register_2026-09-25.csv"
REPORT = ROOT / "analysis" / "Five_Day_Coverage_Check_2026-09-30.md"

DAYS = ["2026-08-31", "2026-09-01", "2026-09-08", "2026-09-18", "2026-09-23"]
LABEL = {"2026-08-31": "31 Aug", "2026-09-01": "1 Sep", "2026-09-08": "8 Sep",
         "2026-09-18": "18 Sep", "2026-09-23": "23 Sep"}
FAMILY_ORDER = ["PO", "CLAR", "CHECK", "SEND", "OTHER", "REQ", "DEC", "EXC", "UNCLEAR"]
STAGE_ORDER = ["Specification", "Supplier selection", "Ordering", "Monitoring",
               "Follow-up and evaluation", "Not applicable", "(blank)"]
AFTERNOON_FROM = 12 * 60 + 45
SHARE_LIMIT = 5.0      # percentage points (S2, S4); proposed, not taken from the literature

# Checks left out of minutes per line because they are known to be incomplete.
INCOMPLETE_CHECKS = {
    ("2026-09-01", "OBS-18"): "price part blocked by an unpaid invoice; only the ETA part was done",
    ("2026-09-18", "OBS-01"): "started before observation began at 10:30, so its full duration is unknown",
}


def clock(value):
    match = re.fullmatch(r"\s*(\d{1,2}):(\d{2})\s*", value or "")
    return int(match.group(1)) * 60 + int(match.group(2)) if match else None


def load_rows():
    with COMBINED.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with KINDS.open(encoding="utf-8") as handle:
        kinds = {(r["date"], r["row"]): [k for k in r["kinds"].split(";") if k] for r in csv.DictReader(handle)}
    for row in rows:
        row["kinds"] = kinds[(row["date"], row["row"])]
        row["minutes"] = int(row["minutes"]) if row["minutes"] else 0
        for key in ("timed", "flag_exc", "flag_lost_focus"):
            row[key] = int(row[key])
    return rows


def load_exposure():
    """Net observation per day and per daypart, and the observed clock minutes, from the register."""
    with REGISTER.open(encoding="utf-8-sig") as handle:
        register = {r["date"]: r for r in csv.DictReader(handle)}
    exposure = {}
    for day in DAYS:
        entry = register[day]
        observed = set()
        for block in entry["notebook_or_recorded_blocks"].split(";"):
            start, end = (clock(x) for x in block.strip().split("-"))
            observed |= set(range(start, end))
        for gap in re.findall(r"(\d{1,2}:\d{2})-(\d{1,2}:\d{2})", entry["documented_unobserved_intervals"]):
            observed -= set(range(clock(gap[0]), clock(gap[1])))
        net = int(entry["confirmed_net_observed_minutes"])
        assert len(observed) == net, day
        parts = Counter("Morning" if m < AFTERNOON_FROM else "Afternoon" for m in observed)
        exposure[day] = {"net": net, "blocks": entry["notebook_or_recorded_blocks"], "observed": observed, **parts}
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


def top(share, n=2):
    return [k for k, _ in sorted(share.items(), key=lambda kv: -kv[1])[:n]]


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


def recorded_minutes(rows, day):
    """Clock minutes inside net observation covered by at least one recorded activity."""
    covered = set()
    for r in rows:
        if r["date"] == day and r["timed"] and not r["flag_lost_focus"]:
            covered |= set(range(clock(r["start"]), clock(r["end"])))
    return covered


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

    # Recorded versus observed time.
    body, totals = [], Counter()
    for day in DAYS:
        covered = recorded_minutes(rows, day)
        outside = covered - exposure[day]["observed"]
        assert not outside, (day, sorted(outside))
        net = exposure[day]["net"]
        untimed = sum(1 for r in rows if r["date"] == day and not r["timed"])
        body.append([LABEL[day], net, len(covered), net - len(covered), fmt(100 * (net - len(covered)) / net, 0) + "%", untimed])
        totals["untimed"] += untimed
        totals.update({"net": net, "covered": len(covered)})
    body.append(["**Total**", totals["net"], totals["covered"], totals["net"] - totals["covered"],
                 fmt(100 * (totals["net"] - totals["covered"]) / totals["net"], 0) + "%", totals["untimed"]])
    recorded = sum(r["minutes"] for r in rows)
    lost = sum(r["minutes"] for r in rows if r["flag_lost_focus"])
    out += ["**Recorded versus observed time.** Minutes of net observation covered by at least one recorded activity, "
            "and minutes with none (between episodes, short untimed actions or work not recorded as an activity).", "",
            table(["Day", "Net observed min", "Min with a recorded activity", "Min with none", "Share with none", "Untimed rows"], body), "",
            "Untimed rows are tallies or short actions without a start and end time; 31 August has the most, which partly "
            "explains its larger share of minutes with no recorded activity.", "",
            f"The {recorded} recorded minutes above count the one overlapping minute on 23 September twice and include "
            f"the {lost} lost-focus minutes on 8 September, which fall outside net observation; this gives "
            f"{totals['covered']} distinct recorded minutes. **Time shares in section 2 are shares of recorded minutes, "
            "not of observed time.**", ""]

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


def stability_section(rows, with_exc):
    name = "A. All data" if with_exc else "B. Without EXC"
    data = view(rows, with_exc)
    first4 = [r for r in data if r["date"] in DAYS[:4]]
    results = {}
    out = [f"### {name}", ""]

    # Per-day and cumulative family shares.
    families = ordered({r["family"] for r in data if r["timed"]}, FAMILY_ORDER)
    per_day = {d: shares([r for r in data if r["date"] == d], "family") for d in DAYS}
    cum4, cum5 = shares(first4, "family"), shares(data, "family")
    body = []
    for f in families:
        body.append([f] + [fmt(per_day[d].get(f, 0)) for d in DAYS] +
                     [fmt(cum4.get(f, 0)), fmt(cum5.get(f, 0)), fmt(cum5.get(f, 0) - cum4.get(f, 0))])
    out += ["**Time share by activity code (%).** Per day, then cumulative over days 1–4 and 1–5.", "",
            table(["Code"] + [LABEL[d] for d in DAYS] + ["Days 1–4", "Days 1–5", "Change"], body), ""]

    # S1: leave-one-day-out top two, as a sensitivity check.
    top_all = top(cum5)
    body, pair_days, order_days = [], [], []
    for d in DAYS:
        s = shares([r for r in data if r["date"] != d], "family")
        t = top(s)
        same_pair, same_order = set(t) == set(top_all), t == top_all
        if not same_pair:
            pair_days.append(d)
        elif not same_order:
            order_days.append(d)
        body.append([f"without {LABEL[d]}", ", ".join(f"{f} {fmt(s[f])}%" for f in t),
                     "yes" if same_pair else "**no**", "yes" if same_order else "**no**"])
    results["S1"] = (pair_days, order_days, top_all)
    out += [f"**S1, leave one day out.** Top two over all five days: {top_all[0]}, then {top_all[1]}. "
            "With five days, each leave-out removes about a fifth of the data, so this is a sensitivity check, not a test.", "",
            table(["Left out", "Top two (share)", "Same pair", "Same order"], body), ""]

    # S2: day-5 change in cumulative family shares.
    worst = max(families, key=lambda f: abs(cum5.get(f, 0) - cum4.get(f, 0)))
    change = cum5.get(worst, 0) - cum4.get(worst, 0)
    results["S2"] = (abs(change) < SHARE_LIMIT, worst, change)
    out += [f"**S2, day-5 change in time shares.** Largest change: {worst} {change:+.1f} points "
            f"(proposed threshold {SHARE_LIMIT:.0f}). {'Within' if results['S2'][0] else '**Beyond**'} the threshold.", ""]

    # S4: stage shares, and the leading stage per day.
    s4_4, s4_5 = shares(first4, "stage"), shares(data, "stage")
    stages = ordered(set(s4_4) | set(s4_5), STAGE_ORDER)
    body = [[s, fmt(s4_4.get(s, 0)), fmt(s4_5.get(s, 0)), fmt(s4_5.get(s, 0) - s4_4.get(s, 0))] for s in stages]
    worst_stage = max(stages, key=lambda s: abs(s4_5.get(s, 0) - s4_4.get(s, 0)))
    stage_change = s4_5.get(worst_stage, 0) - s4_4.get(worst_stage, 0)
    leading = {d: top(shares([r for r in data if r["date"] == d], "stage"), 1)[0] for d in DAYS}
    results["S4"] = (abs(stage_change) < SHARE_LIMIT, worst_stage, stage_change)
    results["leading"] = leading
    out += [f"**S4, time share by Van Weele stage (%).** Largest change: {worst_stage} {stage_change:+.1f} points "
            f"(proposed threshold {SHARE_LIMIT:.0f}). {'Within' if results['S4'][0] else '**Beyond**'} the threshold.", "",
            table(["Stage", "Days 1–4", "Days 1–5", "Change"], body), "",
            "**Largest stage per day:** " + "; ".join(
                f"{LABEL[d]} {leading[d]} ({fmt(shares([r for r in data if r['date'] == d], 'stage')[leading[d]], 0)}%)"
                for d in DAYS) + ".", ""]
    return out, results


def rates_section(rows, exposure):
    out = ["### Occurrences per observed hour", "",
           "Occurrences (timed and untimed rows) per net observed hour, per day and cumulative. Reported with their "
           "daily range; no threshold is applied. Removing EXC changes only the EXC line.", ""]
    hours = {d: exposure[d]["net"] / 60 for d in DAYS}
    hours4, hours5 = sum(hours[d] for d in DAYS[:4]), sum(hours.values())
    body, ranges = [], {}
    for f in ordered({r["family"] for r in rows}, FAMILY_ORDER):
        per_day = [sum(1 for r in rows if r["date"] == d and r["family"] == f) / hours[d] for d in DAYS]
        count4 = sum(1 for r in rows if r["date"] in DAYS[:4] and r["family"] == f)
        count5 = sum(1 for r in rows if r["family"] == f)
        ranges[f] = (min(per_day), max(per_day))
        body.append([f] + [fmt(x, 2) for x in per_day] +
                    [f"{min(per_day):.2f}–{max(per_day):.2f}", fmt(count4 / hours4, 2), fmt(count5 / hours5, 2)])
    out += [table(["Code"] + [LABEL[d] for d in DAYS] + ["Daily range", "Days 1–4", "Days 1–5"], body), ""]
    return out, ranges


def check_lines(row):
    match = re.search(r"(\d+)\s*L checked", row["note"])
    if match:
        return int(match.group(1))
    match = re.fullmatch(r"\s*(\d+)\s*L\s*", row["volume"])
    return int(match.group(1)) if match else None


def check_section(rows):
    checks = [r for r in rows if r["family"] == "CHECK"]
    out = ["## 3. CHECK", "",
           "A check compares price, and the ETA where the supplier states it, with the PO, quotation or confirmation, "
           "and updates the ETA in Exact to the stated date (clarified on 30 September).", ""]
    body = []
    for d in DAYS:
        day_cases = {r["case_ref"] for r in rows if r["date"] == d}
        check_cases = {r["case_ref"] for r in checks if r["date"] == d}
        body.append([LABEL[d], sum(1 for r in checks if r["date"] == d), sum(r["minutes"] for r in checks if r["date"] == d),
                     len(check_cases), len(day_cases), fmt(100 * len(check_cases) / len(day_cases), 0) + "%"])
    out += [table(["Day", "CHECK rows", "CHECK minutes", "Cases with a CHECK", "Cases", "Share of cases"], body), "",
            "CHECK frequency varies strongly by day and is reported with this range rather than as a single rate.", ""]

    used, left_out = [], []
    for r in checks:
        lines = check_lines(r)
        reason = INCOMPLETE_CHECKS.get((r["date"], r["case"]))
        if lines is None:
            left_out.append([LABEL[r["date"]], r["row"], r["case"], r["minutes"], "no line count recorded"])
        elif reason:
            left_out.append([LABEL[r["date"]], r["row"], r["case"], r["minutes"], reason])
        else:
            used.append((r, lines))
    minutes, lines = sum(r["minutes"] for r, _ in used), sum(n for _, n in used)
    ratios = [r["minutes"] / n for r, n in used]
    biggest = max(used, key=lambda x: x[1])
    rest_minutes, rest_lines = minutes - biggest[0]["minutes"], lines - biggest[1]
    obs18 = [r for r in checks if (r["date"], r["case"]) == ("2026-09-01", "OBS-18")][0]
    with_obs18 = (minutes + obs18["minutes"]) / (lines + check_lines(obs18))
    cases = {r["case_ref"] for r, _ in used}
    body = [[LABEL[r["date"]], r["row"], r["case"], r["stage"], n, r["minutes"], fmt(r["minutes"] / n, 2)] for r, n in used]
    out += ["**Minutes per line (exploratory).**", "",
            table(["Day", "Row", "Case", "Stage", "Lines", "Minutes", "Min per line"], body), "",
            f"- **Pooled:** {minutes} minutes over {lines} lines = **{minutes / lines:.2f} minutes per line**, from {len(used)} "
            f"check segments in {len(cases)} cases. Median per segment {statistics.median(ratios):.2f}; range "
            f"{min(ratios):.2f}–{max(ratios):.2f}.",
            f"- **Sensitivity:** {with_obs18:.2f} with 1 September OBS-18 included; {rest_minutes / rest_lines:.2f} without the "
            f"{biggest[1]}-line check ({LABEL[biggest[0]['date']]} {biggest[0]['case']}), which carries {biggest[1]} of the {lines} lines.",
            "- **Left out:** " + "; ".join(f"{d} row {row} ({case}, {m} min): {why}" for d, row, case, m, why in left_out) + ".",
            "- **Status:** exploratory, not a precise duration estimate. Leaving out the checks known to be incomplete does "
            "not show that every remaining segment covers a complete check of every recorded line. Where a note says how "
            "many lines were checked (31 August OBS-04), that number is used instead of the order volume.", ""]
    return out, {"pooled": minutes / lines, "segments": len(used), "cases": len(cases),
                 "median": statistics.median(ratios), "range": (min(ratios), max(ratios)),
                 "per_day": [sum(1 for r in checks if r["date"] == d) for d in DAYS],
                 "with_obs18": with_obs18}


def kinds_first_day(rows):
    first = {}
    for r in rows:
        for k in r["kinds"]:
            first[k] = min(first.get(k, 9), DAYS.index(r["date"]))
    return [sum(1 for v in first.values() if v == i) for i in range(5)]


def saturation_section(rows):
    earlier = [r for r in rows if r["date"] in DAYS[:4]]
    day5 = [r for r in rows if r["date"] == DAYS[4]]
    out = ["## 4. Saturation", ""]
    new = {}
    for key, label in (("family", "activity codes"), ("stage", "stages"), ("request_channel", "request channels")):
        seen = {r[key] for r in earlier if r[key]}
        new[label] = sorted({r[key] for r in day5 if r[key]} - seen)
    q1 = not any(new.values())
    out += [f"**Q1, new codes, stages or channels on day 5.** " + "; ".join(
        f"{k}: {', '.join(v) if v else 'none new'}" for k, v in new.items()) + ".", ""]

    counts = {"A": kinds_first_day(rows), "B": kinds_first_day(view(rows, False))}
    unclassified = [sum(1 for r in rows if r["date"] == d and not r["kinds"]) for d in DAYS]
    unclassified_min = [sum(r["minutes"] for r in rows if r["date"] == d and not r["kinds"]) for d in DAYS]
    cum = {v: [sum(c[:i + 1]) for i in range(5)] for v, c in counts.items()}
    out += ["**Q2, new kinds of work per day.** From the [kinds-of-work review](Kinds_Of_Work_Review_2026-09-30.md), "
            "which assigns each row the kinds of work its note supports and judges whether each kind adds information "
            "relevant to improvement. In view B a kind counts only if it occurs in a non-EXC row.", "",
            table(["", *[LABEL[d] for d in DAYS]],
                  [["New kinds, A. All data", *counts["A"]], ["New kinds, B. Without EXC", *counts["B"]],
                   ["Kinds seen so far, A", *cum["A"]], ["Kinds seen so far, B", *cum["B"]],
                   ["Rows without a kind", *unclassified], ["Their minutes", *unclassified_min]]), ""]
    for v in ("A", "B"):
        c, s = counts[v], cum[v]
        out.append(f"- **View {v}:** days 1–3 as the base and days 4–5 as the run give {c[3] + c[4]} new kinds against "
                   f"{s[2]} ({100 * (c[3] + c[4]) / s[2]:.0f}%); days 1–4 as the base and day 5 as the run give {c[4]} "
                   f"against {s[3]} ({100 * c[4] / s[3]:.0f}%).")
    out += ["- These base and run sizes adapt Guest, Namey and Chen (2020), who tested bases of 4–6 interviews with runs "
            "of 2–3 and describe 5% new information as an optional benchmark. Applying them to observation days is this "
            "project's adaptation, used retrospectively; the judgement of what each kind adds matters more than the percentage.",
            f"- **23 September:** the classified rows add no new kind under this coding scheme, but {unclassified[4]} rows "
            f"({unclassified_min[4]} minutes) have too little detail to classify, so this does not show that nothing new occurred.",
            "- Two day-5 episodes add detail inside kinds already seen: a 12-minute Exact fault handled as its own episode "
            "(OBS-09; Exact errors were first seen on 31 August) and 42 minutes helping Logistics locate an item already "
            "received (OBS-16, EXC; Arno said this usually never happens).", ""]
    return out, {"Q1": (q1, new), "Q2": counts, "unclassified": (unclassified[4], unclassified_min[4])}


def meaning_section(rows, exposure, results, rates, check, sat):
    exc_share = [100 * sum(r["minutes"] for r in rows if r["date"] == d and r["flag_exc"]) /
                 sum(r["minutes"] for r in rows if r["date"] == d) for d in DAYS]
    na_day5 = sorted((r for r in rows if r["date"] == DAYS[4] and r["stage"] == "Not applicable" and r["timed"]),
                     key=lambda r: -r["minutes"])
    big = na_day5[0]
    a, b = results["A"], results["B"]
    pair_a = " or ".join(LABEL[d] for d in a["S1"][0])
    order_b = " or ".join(LABEL[d] for d in b["S1"][1])
    leading_b = set(b["leading"].values())
    leading_a = set(a["leading"].values())
    check_lo, check_hi = min(check["per_day"]), max(check["per_day"])
    unrecorded = sum(exposure[d]["net"] for d in DAYS) - sum(len(recorded_minutes(rows, d)) for d in DAYS)
    net = sum(exposure[d]["net"] for d in DAYS)
    counts = sat["Q2"]["A"]
    return ["## 6. What this means", "",
            "This is a **retrospective, literature-informed assessment**, not a pre-registered test: the rules were proposed "
            "on 30 September after an informal look at the data, and the literature was consulted afterwards.", "",
            f"**Main pattern without EXC (view B).** {b['S1'][2][0]} and {b['S1'][2][1]} are the two largest activity codes "
            f"whichever day is left out, but their order flips when {order_b} is left out, so the data show which two codes "
            f"lead, not which of the two is larger. "
            + (f"{leading_b.pop()} is the largest stage on every day. " if len(leading_b) == 1 else "")
            + f"Adding day 5 moved no code share and no stage share by {SHARE_LIMIT:.0f} points or more.", "",
            f"**With EXC (view A).** EXC ranges from {min(exc_share):.0f}% to {max(exc_share):.0f}% of a day's recorded "
            f"minutes, so the top pair changes when {pair_a} is left out. The stage share of {a['S4'][1]} changes by "
            f"{a['S4'][2]:+.1f} points on day 5, mainly because of the {big['minutes']}-minute {big['case']} episode "
            "(stage Not applicable), which Arno described as unusual. "
            + (f"{leading_a.pop()} is still the largest stage on every day." if len(leading_a) == 1 else ""), "",
            f"**Rates and CHECK.** Rates per observed hour are reported with their daily range, without a pass/fail rule. "
            f"CHECK varies most ({check_lo} to {check_hi} rows per session). Minutes per line stays exploratory: "
            f"{check['pooled']:.2f} pooled over {check['segments']} segments in {check['cases']} cases (median "
            f"{check['median']:.2f}, range {check['range'][0]:.2f}–{check['range'][1]:.2f}).", "",
            f"**Unrecorded time.** {unrecorded} of {net} net observed minutes have no recorded activity. Shares describe "
            "recorded work, not the whole observed time.", "",
            f"**Saturation.** Day 5 showed no new activity code, stage or request channel. New kinds of work per day were "
            f"{', '.join(str(c) for c in counts[:4])} and {counts[4]}; the later days mainly added detail inside kinds "
            "already seen, such as unpaid invoices blocking checks, approval repeated after a mismatch and incomplete "
            f"drawing sets. {sat['unclassified'][0]} rows ({sat['unclassified'][1]} minutes) on 23 September could not be classified.", "",
            "**Coverage.** No Thursday, no measured time before 10:30 or after 15:00, and 8 September has a morning block "
            "only. Because the main pattern without EXC is consistent across the five days, these are documented "
            "limitations rather than gaps that change the result, following the supervisor's advice of 17 September.", "",
            "**Conclusion.** The evidence supports pausing broad observation and starting Analyze for Arno. Conclusions "
            "that depend on the EXC decision or on the Dennis comparison stay provisional until the supervisor discussion.", "",
            "**Open for the supervisor discussion:**", "",
            f"1. Accept the retrospective reading and the proposed {SHARE_LIMIT:.0f}-point threshold for shares. The threshold "
            "is a pragmatic choice: a work-sampling precision target of ±5% describes uncertainty about a share, not how "
            "much a share may change when a day is added.",
            "2. Decide on EXC. With EXC included, the ranking depends on which days are observed, because EXC work comes in "
            "irregular episodes.",
            "3. Agree how Dennis's data enter the comparison.", ""]


def main():
    rows = load_rows()
    exposure = load_exposure()
    lines = ["# Five-day coverage check, Arno", "",
             "**Run:** 30 September 2026, following [the analysis plan](Analysis_Plan_2026-09-30.md). "
             "**Data:** [combined table](output/Arno_Combined_2026-09-30.csv) built from the five reviewed daily CSVs; "
             "no row dropped. **Reading:** retrospective and literature-informed (section 6); the 5-point threshold for "
             "shares is proposed and still needs the supervisor's confirmation, and rates are reported without a threshold. "
             "Generated by `analysis/five_day_check.py`; do not edit by hand.", ""]
    lines += coverage_section(rows, exposure)
    lines += ["## 2. Stability", "",
              "Every result is shown for view A (all data) and view B (without EXC). The 9 lost-focus minutes on "
              "8 September stay in both views as recorded minutes.", ""]
    results = {}
    for with_exc in (True, False):
        part, res = stability_section(rows, with_exc)
        lines += part
        results["A" if with_exc else "B"] = res
    rate_lines, rates = rates_section(rows, exposure)
    lines += rate_lines
    check_lines_, check = check_section(rows)
    lines += check_lines_
    sat_lines, sat = saturation_section(rows)
    lines += sat_lines

    def s1(v):
        pair_days, order_days, top_all = results[v]["S1"]
        text = ("**pair changes** without " + ", ".join(LABEL[d] for d in pair_days)) if pair_days else "same pair"
        return text + ("; **order flips** without " + ", ".join(LABEL[d] for d in order_days) if order_days else "")

    def within(v, rule):
        ok, name, change = results[v][rule]
        return f"{'within' if ok else '**beyond**'} ({name} {change:+.1f})"

    def leading(v):
        stages = set(results[v]["leading"].values())
        return f"{stages.pop()} every day" if len(stages) == 1 else ", ".join(f"{LABEL[d]} {s}" for d, s in results[v]["leading"].items())

    q1_ok, _ = sat["Q1"]
    lines += ["## 5. Result", "",
              table(["Check", "A. All data", "B. Without EXC"], [
                  ["S1 top two codes, leaving out one day", s1("A"), s1("B")],
                  [f"S2 day-5 change in code shares (threshold {SHARE_LIMIT:.0f} points)", within("A", "S2"), within("B", "S2")],
                  ["Rates per observed hour", "reported with daily range", "same"],
                  [f"S4 day-5 change in stage shares (threshold {SHARE_LIMIT:.0f} points)", within("A", "S4"), within("B", "S4")],
                  ["Largest stage per day", leading("A"), leading("B")],
                  ["Q1 new code, stage or channel on day 5", "none" if q1_ok else "**some**", "same"],
                  ["Q2 new kinds of work per day", ", ".join(map(str, sat["Q2"]["A"])), ", ".join(map(str, sat["Q2"]["B"]))],
              ]), ""]
    lines += meaning_section(rows, exposure, results, rates, check, sat)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)}")
    for v in ("A", "B"):
        print(v, {k: results[v][k] for k in ("S1", "S2", "S4")}, results[v]["leading"])
    print("Q2", sat["Q2"], "check", {k: check[k] for k in ("pooled", "segments", "cases", "median", "range", "with_obs18")})


if __name__ == "__main__":
    main()
