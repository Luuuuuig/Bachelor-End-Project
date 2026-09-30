"""Workload profile for Arno (Analyze step 4, sub-question 3).

Reads the combined table and the kinds of work, and writes
analysis/Workload_Profile_Arno_2026-09-30.md. Indicators are reported separately,
never added into one workload score (docs/methodology/Workload_Definition.md).
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
REPORT = ROOT / "analysis" / "Workload_Profile_Arno_2026-09-30.md"

DAYS = ["2026-08-31", "2026-09-01", "2026-09-08", "2026-09-18", "2026-09-23"]
LABEL = {"2026-08-31": "31 Aug", "2026-09-01": "1 Sep", "2026-09-08": "8 Sep", "2026-09-18": "18 Sep", "2026-09-23": "23 Sep"}
NET_MINUTES = {"2026-08-31": 165, "2026-09-01": 186, "2026-09-08": 104, "2026-09-18": 240, "2026-09-23": 197}
FAMILY_ORDER = ["PO", "CLAR", "CHECK", "SEND", "OTHER", "REQ", "DEC", "EXC", "UNCLEAR"]
STAGE_ORDER = ["Specification", "Supplier selection", "Ordering", "Monitoring",
               "Follow-up and evaluation", "Not applicable", "(blank)"]

# Kinds that record something interfering with the work (organizational constraints in the workload definition).
CONSTRAINTS = ["K08", "K14", "K18", "K20", "K26", "K07"]

# Current candidates in docs/methodology/Phase_1_Current_Methodology.md and the kinds that carry their evidence.
CANDIDATES = [
    ("Order timing / maximalisatie", ["K03"]),
    ("Purchase-price control", ["K04", "K17", "K18"]),
    ("Request intake & validation", ["K08", "K09", "K10", "K11"]),
    ("PO supplier communication (supporting)", ["K05"]),
]


def load():
    with COMBINED.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with KINDS.open(encoding="utf-8") as handle:
        kinds = {}
        names = {}
        for r in csv.DictReader(handle):
            ids = [k for k in r["kinds"].split(";") if k]
            kinds[(r["date"], r["row"])] = ids
            for k, name in zip(ids, r["kind_names"].split("; ")):
                names[k] = name
    for r in rows:
        r["kinds"] = kinds[(r["date"], r["row"])]
        r["minutes"] = int(r["minutes"]) if r["minutes"] else 0
        for key in ("timed", "flag_exc", "flag_lost_focus"):
            r[key] = int(r[key])
        # Lost-focus minutes stay visible as rows but are not counted as workload time.
        r["work_minutes"] = 0 if r["flag_lost_focus"] else r["minutes"]
    return rows, names


def ordered(keys, order):
    return [k for k in order if k in keys] + sorted(k for k in keys if k not in order)


def is_number(value):
    return bool(re.fullmatch(r"[-+]?\d+(\.\d+)?%?", str(value).strip()))


def table(header, rows):
    numeric = [i > 0 and all(is_number(r[i]) for r in rows if str(r[i]).strip()) for i in range(len(header))]
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join("---:" if n else "---" for n in numeric) + "|"]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def pct(part, whole):
    return f"{100 * part / whole:.1f}" if whole else "0.0"


def lines_of(r):
    match = re.fullmatch(r"\s*(\d+)\s*L\s*", r["volume"])
    return int(match.group(1)) if match else None


def code_section(rows):
    hours = sum(NET_MINUTES.values()) / 60
    out = ["## 1. By activity code", "",
           "Minutes exclude the 9 lost-focus minutes on 8 September. Share is of recorded minutes in the same view. "
           "The daily range shows the lowest and highest share on a single day.", ""]
    for name, data in (("A. All data", rows), ("B. Without EXC", [r for r in rows if not r["flag_exc"]])):
        total = sum(r["work_minutes"] for r in data)
        body = []
        for f in ordered({r["family"] for r in data}, FAMILY_ORDER):
            fr = [r for r in data if r["family"] == f]
            timed = [r["minutes"] for r in fr if r["timed"]]
            minutes = sum(r["work_minutes"] for r in fr)
            daily = []
            for d in DAYS:
                day_total = sum(r["work_minutes"] for r in data if r["date"] == d)
                daily.append(100 * sum(r["work_minutes"] for r in fr if r["date"] == d) / day_total)
            body.append([f, len(fr), len(timed), minutes, pct(minutes, total), f"{min(daily):.0f}–{max(daily):.0f}",
                         f"{statistics.median(timed):.0f}" if timed else "—", f"{len(fr) / hours:.2f}"])
        body.sort(key=lambda b: -b[3])
        out += [f"### {name}", "", f"{total} recorded minutes.", "",
                table(["Code", "Rows", "Timed rows", "Minutes", "Share %", "Daily share range %",
                       "Median min per timed row", "Rows per observed hour"], body), ""]
    return out


def stage_section(rows):
    out = ["## 2. By Van Weele stage", ""]
    views = {"A": rows, "B": [r for r in rows if not r["flag_exc"]]}
    totals = {v: sum(r["work_minutes"] for r in data) for v, data in views.items()}
    body = []
    for s in ordered({r["stage"] for r in rows}, STAGE_ORDER):
        cells = [s]
        for v, data in views.items():
            sr = [r for r in data if r["stage"] == s]
            minutes = sum(r["work_minutes"] for r in sr)
            cells += [len(sr), minutes, pct(minutes, totals[v])]
        body.append(cells)
    out += [table(["Stage", "Rows A", "Minutes A", "Share A %", "Rows B", "Minutes B", "Share B %"], body), ""]
    return out


def kinds_section(rows, names):
    out = ["## 3. By kind of work", "",
           "Minutes are totals of the rows showing each kind. A row with two kinds counts under both, so the column does "
           "not add up to the recorded total; it shows where time was spent, not an additive ranking. B counts only "
           "non-EXC rows. Kinds are defined in the [kinds-of-work review](Kinds_Of_Work_Review_2026-09-30.md).", ""]
    body = []
    for k in sorted(names):
        kr = [r for r in rows if k in r["kinds"]]
        kb = [r for r in kr if not r["flag_exc"]]
        body.append([k, names[k], len(kr), sum(r["work_minutes"] for r in kr), len(kb), sum(r["work_minutes"] for r in kb),
                     len({r["date"] for r in kr}), len({r["case_ref"] for r in kr})])
    body.sort(key=lambda b: (-b[3], b[0]))
    out += [table(["ID", "Kind of work", "Rows A", "Minutes A", "Rows B", "Minutes B", "Days seen", "Cases"], body), ""]
    return out


def volume_section(rows):
    out = ["## 4. Volume (lines)", "",
           "Rows with a line count in the Volume field (for example `5L`). Other rows record `—`, `/` or nothing, so "
           "these figures describe only the rows where volume was noted.", ""]
    body = []
    for f in ordered({r["family"] for r in rows}, FAMILY_ORDER):
        counts = [lines_of(r) for r in rows if r["family"] == f and lines_of(r) is not None]
        if counts:
            body.append([f, len([r for r in rows if r["family"] == f]), len(counts), sum(counts),
                         f"{statistics.median(counts):.0f}", max(counts)])
    out += [table(["Code", "Rows", "Rows with lines", "Total lines", "Median lines", "Largest"], body), "",
            "The same order can appear in several rows (for example a PO row and its CHECK row), so total lines count "
            "order lines per activity, not distinct order lines.", ""]
    return out


def cues_section(rows, names):
    out = ["## 5. Difficulty and constraint cues", "",
           "These are separate indicators, not part of a time total. They show where judgement, interruptions or "
           "obstacles were recorded. A handwritten `/` in INT or DEC? means none ([scope addendum](../docs/measurement/"
           "Scope_and_Classification_Addendum_2026-09-14.md#recording-marks)); blank DEC? cells on 31 August mean the "
           "flag was not recorded.", ""]
    body = []
    for f in ordered({r["family"] for r in rows}, FAMILY_ORDER):
        fr = [r for r in rows if r["family"] == f]
        body.append([f, len(fr), sum(r["interruptions"] not in ("", "0") for r in fr)] +
                    [sum(r["decision"] == v for r in fr) for v in ("yes", "no", "uncertain", "not recorded")])
    out += ["**Interruption and decision marks by activity code.**", "",
            table(["Code", "Rows", "Interrupted", "Decision: yes", "no", "uncertain", "not recorded"], body), ""]

    body = []
    for d in DAYS:
        dr = [r for r in rows if r["date"] == d]
        interrupted = sum(r["interruptions"] not in ("", "0") for r in dr)
        body.append([LABEL[d], len(dr), interrupted,
                     f"{interrupted / (NET_MINUTES[d] / 60):.2f}", sum(r["decision"] == "yes" for r in dr),
                     sum(r["decision"] == "not recorded" for r in dr)])
    maxi = [r for r in rows if "K03" in r["kinds"]]
    early, late = [r for r in maxi if r["date"] in DAYS[:2]], [r for r in maxi if r["date"] not in DAYS[:2]]
    out += ["**Per day.**", "",
            table(["Day", "Rows", "Interrupted rows", "Per observed hour", "Decision marked", "Decision not recorded"], body), "",
            "- **Interruptions** are recorded on every row of all five days, so they can be compared between days.",
            f"- **Decision marks fall sharply after 1 September.** {sum(r['decision'] == 'yes' for r in early)} of the "
            f"{len(early)} maximalisatie rows on 31 August and 1 September are marked as a decision, and "
            f"{sum(r['decision'] == 'yes' for r in late)} of the {len(late)} later ones, although their notes still describe combining or trying to combine orders. "
            "Decision marks are therefore reported as recorded but not used to compare days or candidates; judgement "
            "evidence comes from the notes.", ""]

    body = []
    for k in CONSTRAINTS:
        kr = [r for r in rows if k in r["kinds"]]
        body.append([k, names[k], len(kr), sum(r["work_minutes"] for r in kr), len({r["date"] for r in kr}),
                     len({r["case_ref"] for r in kr}), sum(r["flag_exc"] for r in kr)])
    out += ["**Kinds that record an obstacle** (organizational constraints in the workload definition):", "",
            table(["ID", "Kind of work", "Rows", "Minutes", "Days seen", "Cases", "of which EXC rows"], body), ""]
    return out


def candidates_section(rows):
    out = ["## 6. Evidence per current candidate (input for step 6)", "",
           "The kinds of work that carry each candidate's evidence in the [methodology](../docs/methodology/Phase_1_Current_Methodology.md#4-current-candidate-portfolio). "
           "Minutes count each row once, even if it shows two of the candidate's kinds. This is workload evidence only; "
           "business relevance, technical feasibility and the need for human expertise come in step 6. The process-redesign "
           "candidate is process-wide and needs the workflow of step 5.", ""]
    body = []
    for name, ks in CANDIDATES:
        cr = [r for r in rows if set(ks) & set(r["kinds"])]
        cb = [r for r in cr if not r["flag_exc"]]
        body.append([name, ", ".join(ks), len(cr), sum(r["work_minutes"] for r in cr), sum(r["work_minutes"] for r in cb),
                     len({r["date"] for r in cr}), len({r["case_ref"] for r in cr})])
    out += [table(["Candidate", "Kinds", "Rows", "Minutes A", "Minutes B", "Days seen", "Cases"], body), ""]
    return out


def reading_section(rows):
    b = [r for r in rows if not r["flag_exc"]]
    total_a, total_b = sum(r["work_minutes"] for r in rows), sum(r["work_minutes"] for r in b)

    def share(data, key, value, total):
        return 100 * sum(r["work_minutes"] for r in data if r[key] == value) / total

    def kind_minutes(k, data):
        return sum(r["work_minutes"] for r in data if k in r["kinds"])

    def candidate(ks):
        cr = [r for r in rows if set(ks) & set(r["kinds"])]
        return (sum(r["work_minutes"] for r in cr), sum(r["work_minutes"] for r in cr if not r["flag_exc"]),
                len(cr), len({r["case_ref"] for r in cr}))

    exc_daily = []
    for d in DAYS:
        day = [r for r in rows if r["date"] == d]
        exc_daily.append(100 * sum(r["work_minutes"] for r in day if r["flag_exc"]) / sum(r["work_minutes"] for r in day))
    price, maxi, intake = candidate(["K04", "K17", "K18"]), candidate(["K03"]), candidate(["K08", "K09", "K10", "K11"])
    finance = [r for r in rows if "K20" in r["kinds"]]
    return ["## 7. First reading (provisional)", "",
            f"- **Time without EXC (view B):** PO ({share(b, 'family', 'PO', total_b):.0f}%) and CLAR "
            f"({share(b, 'family', 'CLAR', total_b):.0f}%) carry most recorded time, and Ordering is "
            f"{share(b, 'stage', 'Ordering', total_b):.0f}% of it. With EXC (view A), EXC is the largest code "
            f"({share(rows, 'family', 'EXC', total_a):.0f}%) but ranges from {min(exc_daily):.0f}% to {max(exc_daily):.0f}% by day.",
            f"- **Where the time goes by kind:** creating or completing POs ({kind_minutes('K02', rows)} minutes) is the largest kind. "
            f"Most follow-up and logistics time is EXC: {kind_minutes('K19', rows) - kind_minutes('K19', b)} of "
            f"{kind_minutes('K19', rows)} follow-up minutes and {kind_minutes('K23', rows) - kind_minutes('K23', b)} of "
            f"{kind_minutes('K23', rows)} logistics minutes, so their weight depends on the EXC decision.",
            f"- **Candidates differ in the kind of workload they carry.** Purchase-price control has the most recorded time "
            f"({price[0]} minutes in view A, {price[1]} in view B, {price[3]} cases). Maximalisatie has less time "
            f"({maxi[0]} minutes, {maxi[3]} cases), but its notes record hold-or-order outcomes and failed attempts to combine "
            f"orders, which is judgement evidence rather than volume. Request intake and validation takes {intake[0]} minutes "
            f"over {intake[3]} cases, about {intake[0] / intake[3]:.0f} minutes per case. These are different facets of workload "
            "and are not ranked into one score.",
            f"- **A recurring obstacle:** Finance-related issues appear on {len({r['date'] for r in finance})} of 5 days "
            f"({len(finance)} rows, {sum(r['work_minutes'] for r in finance)} minutes), including unpaid invoices that blocked "
            "a supplier and a price check.",
            "- **Limits:** the profile covers 892 minutes of net observation in five sessions, of which 150 minutes have no "
            "recorded activity; decision marks fall sharply after 1 September and are not compared between days; minutes per "
            "line for CHECK is exploratory "
            "(see the [five-day check](Five_Day_Coverage_Check_2026-09-30.md)).", ""]


def main():
    rows, names = load()
    lines = ["# Workload profile, Arno (draft)", "",
             "**Analyze step 4, sub-question 3.** Prepared 30 September 2026 from the [combined table](output/Arno_Combined_2026-09-30.csv) "
             "and the [kinds of work](Kinds_Of_Work_Review_2026-09-30.md). Every result is shown for view A (all data) and "
             "view B (without EXC); which view is the thesis result depends on the supervisor discussion on EXC, so "
             "conclusions here are **provisional**. Following the [workload definition](../docs/methodology/Workload_Definition.md), "
             "time, frequency, volume and difficulty cues are reported separately and never added into one score. "
             "Generated by `analysis/workload_profile.py`; do not edit by hand.", ""]
    lines += code_section(rows)
    lines += stage_section(rows)
    lines += kinds_section(rows, names)
    lines += volume_section(rows)
    lines += cues_section(rows, names)
    lines += candidates_section(rows)
    lines += reading_section(rows)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
