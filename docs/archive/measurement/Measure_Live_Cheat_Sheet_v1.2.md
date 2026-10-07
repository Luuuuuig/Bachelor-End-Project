# Measure Live Cheat Sheet v1.2

Use beside the observer for official exploratory Measure observations after the 31 August 2026 first baseline session.

## 1. Session header

```text
Date:
Buyer:
Observer:
Observation start:
Observation end:
Breaks / observer unavailable:
Net observed time:
Context: normal / quiet / busy / system issue / other
Acclimatization? yes/no
```

## 2. Restricted case index — fill once per new case

`Case | Origin | Channel | First observed | PO known?`

**Origin:** External request / Exact demand / Supplier confirmation / Finance return / Colleague question / Unknown

**Channel:** Email / Phone / Desk / Letter-Paper / Exact / Other / Unknown

## 3. Live row

`Case | Activity | Start | End | Volume | INT | DEC? | Result / short note`

## 4. Activity codes

| Code | Meaning | Rule |
|---|---|---|
| **REQ** | actively receive/read/listen/organize/comprehend request | TIME IF; tally if instantaneous |
| **CLAR** | clarify / investigate / missing information | TIME IF |
| **DEC** | genuinely standalone decision | TALLY only |
| **PO** | create/change/prepare/process PO/order work in Exact | TIME |
| **CHECK** | price / confirmation / information verification | TIME |
| **SEND** | forward/send purchasing communication | TIME |
| **EXC** | aftercare / tracing / rework / exception | TIME IF |
| **OTHER** | relevant purchasing work that does not fit | TIME IF |

## 5. MAX rule

**Every order gets the maximalisatie check in the current AS-IS interpretation.**

If MAX and PO happen seamlessly, keep **one PO timed row**. Do not invent a split.

Use in the note:
- `MAX=ADD` = useful extra demand added
- `MAX=NONE` = nothing useful added
- `MAX=?` = outcome unclear
- then `ORD` or `HOLD`

If `MAX=NONE`:
- small + non-urgent -> HOLD
- small + urgent -> ORD
- otherwise ready/large enough -> ORD

## 6. DEC? field

- `Y` = judgement/decision observed in this episode
- `—` = no distinct decision event in this episode
- `?` = uncertain

If decision is embedded in PO/REQ/CLAR/CHECK/EXC, use `DEC?=Y` and **do not add another DEC row for the same decision**.

## 7. Mandatory no-blank rules

- **Start / End:** clock time or `—`
- **Volume:** value such as `4L` or `—`
- **INT:** always a number; `0` = no interruption observed
- **DEC?:** `Y`, `—`, or `?`
- Do not use a blank to mean zero, not applicable or unknown.

## 8. Shorthand

- `L` = lines/items
- `D` = deviations
- `ORD` = proceed/order
- `HOLD` = hold
- `MI` = missing/ambiguous information
- `FIN` = Finance-related issue
- `J` = observable judgement
- `EXP` = observable experience/tacit cue
- `MISS` = known purchasing work could not be captured

## 9. Rules to remember

1. New purchasing case = new OBS.
2. Same case returning later = same OBS.
3. Origin + Channel are recorded once in the case index.
4. REQ can be timed when intake itself is real work.
5. MAX is normally embedded in PO; do not split seamless MAX/PO minutes.
6. A standalone DEC is only for a genuinely separate quick decision.
7. If an interruption stops active work, put INT on the segment being left.
8. If the episode was already finished before a call/conversation starts, that is not its interruption.
9. Observer-unavailable time is removed from net observed time; it is not automatically INT.
10. System waiting is not active buyer time.
11. If work happened but could not be coded, record MISS.
12. Do not infer J/EXP or reasoning when uncertain.
13. Do not create overlapping active time for one buyer; resolve the boundary or mark it uncertain.
14. No example rows are pre-filled in the actual data area.

## 10. Post-session — do immediately

For every row:
- retain the raw live record;
- add Detailed Task ID where supported;
- add confidence `C / P / U / ?`;
- preserve U/OTHER subtype;
- do not reconstruct unsupported time, outcome or reasoning.

**Register-review trigger:** review a U subtype for addition to the AS-IS register if it appears in at least two official baseline sessions and at least three times total, or repeated observation plus buyer/manager validation confirms it is normal recurring work.
