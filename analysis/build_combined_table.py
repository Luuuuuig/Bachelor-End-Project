"""Combine Arno's five reviewed daily CSVs into one analysis table.

Step 2 of analysis/Analysis_Plan_2026-09-30.md. Reads the daily CSVs without
changing them, keeps every row and adds derived columns and flags.
Run from the repository root: python3 analysis/build_combined_table.py
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEASUREMENT = ROOT / "docs" / "measurement"
OUTPUT = ROOT / "analysis" / "output" / "Arno_Combined_2026-09-30.csv"

SESSIONS = [
    ("2026-08-31", "Mon"),
    ("2026-09-01", "Tue"),
    ("2026-09-08", "Tue"),
    ("2026-09-18", "Fri"),
    ("2026-09-23", "Wed"),
]
FAMILIES = ["REQ", "CLAR", "DEC", "PO", "CHECK", "SEND", "OTHER"]
AFTERNOON_FROM = 12 * 60 + 45
LOST_FOCUS = ("2026-09-08", "OBS-16", 12 * 60 + 4, 12 * 60 + 13)

FIELDS = [
    "date", "weekday", "row", "case", "case_ref", "activity_as_written",
    "family", "start", "end", "timed", "minutes", "daypart", "request_channel",
    "volume", "int", "dec", "note", "stage", "flag_exc", "flag_lost_focus",
    "flag_stage_na", "flag_stage_blank", "overlap_minutes",
]


def clock(value):
    match = re.fullmatch(r"\s*(\d{1,2}):(\d{2})\s*", value or "")
    return int(match.group(1)) * 60 + int(match.group(2)) if match else None


def family(code):
    upper = code.strip().upper()
    if "EXC" in upper:
        return "EXC"
    for name in FAMILIES:
        if upper.startswith(name):
            return name
    return "UNCLEAR"


def channel_from_code(code):
    suffix = code.strip().lower().partition("-")[2]
    mapping = {"mail": "Email", "email": "Email", "phone": "Phone", "call": "Phone",
               "exact": "Exact", "desk": "Desk", "letter": "Letter"}
    return mapping.get(suffix, "")


def case_index_channels(note_path):
    """Channel per case from a note's case-index tables (Case | Origin | Channel | ...)."""
    channels = {}
    in_index = False
    for line in note_path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[:3] == ["Case", "Origin", "Channel"]:
            in_index = True
            continue
        if in_index and line.startswith("|"):
            if set(cells[0]) <= {"-"}:
                continue
            channels[cells[0]] = cells[2]
        else:
            in_index = False
    return channels


def load_session(date, weekday):
    path = MEASUREMENT / f"Arno_Measurement_{date}.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        source = list(csv.DictReader(handle))
    index_channels = case_index_channels(MEASUREMENT / f"Measure_Observation_{date}.md")
    rows = []
    for number, raw in enumerate(source, 1):
        code = raw.get("Activity") or raw.get("Activity as written") or ""
        start, end = clock(raw["Start"]), clock(raw["End"])
        timed = start is not None and end is not None
        stage = raw["Van Weele stage"].strip()
        fam = family(code)
        channel = ""
        if fam == "REQ":
            channel = channel_from_code(code) or index_channels.get(raw["Case"].strip(), "") or "Unspecified"
            if channel == "Unknown":
                channel = "Unspecified"
        lost_date, lost_case, lost_from, lost_to = LOST_FOCUS
        lost = (date == lost_date and raw["Case"].strip() == lost_case and timed
                and lost_from <= start < lost_to)
        rows.append({
            "date": date,
            "weekday": weekday,
            "row": number,
            "case": raw["Case"].strip(),
            "case_ref": f"{date} {raw['Case'].strip()}",
            "activity_as_written": code,
            "family": fam,
            "start": raw["Start"],
            "end": raw["End"],
            "timed": int(timed),
            "minutes": end - start if timed else "",
            "daypart": "",
            "request_channel": channel,
            "volume": raw["Volume"],
            "int": raw["INT"],
            "dec": raw["DEC?"],
            "note": raw.get("Note") or raw.get("Result / short note") or "",
            "stage": stage or "(blank)",
            "flag_exc": int(fam == "EXC"),
            "flag_lost_focus": int(lost),
            "flag_stage_na": int(stage == "Not applicable"),
            "flag_stage_blank": int(stage == ""),
            "overlap_minutes": 0,
            "_start": start,
            "_end": end,
        })
    assign_dayparts(rows)
    assign_overlaps(rows)
    return rows


def assign_dayparts(rows):
    last = None
    for row in rows:
        if row["_start"] is not None:
            last = "Morning" if row["_start"] < AFTERNOON_FROM else "Afternoon"
        row["daypart"] = last or ""
    following = None
    for row in reversed(rows):
        if row["_start"] is not None:
            following = "Morning" if row["_start"] < AFTERNOON_FROM else "Afternoon"
        if not row["daypart"]:
            row["daypart"] = following or ""


def assign_overlaps(rows):
    timed = [r for r in rows if r["timed"]]
    for i, first in enumerate(timed):
        for second in timed[i + 1:]:
            overlap = min(first["_end"], second["_end"]) - max(first["_start"], second["_start"])
            if overlap > 0:
                first["overlap_minutes"] += overlap
                second["overlap_minutes"] += overlap


def main():
    rows = []
    for date, weekday in SESSIONS:
        rows.extend(load_session(date, weekday))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    minutes = sum(r["minutes"] for r in rows if r["timed"])
    exc = sum(r["minutes"] for r in rows if r["timed"] and r["flag_exc"])
    print(f"{len(rows)} rows, {sum(r['timed'] for r in rows)} timed, {minutes} minutes, "
          f"{exc} EXC minutes -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
