# Measure Live Cheat Sheet v1.1

Use beside the observer during official exploratory Measure observations from 31 August 2026.

## Session header

```text
Date:
Buyer:
Observer:
Observation start:
Observation end:
Breaks / observer unavailable:
Net observed time:
Context: normal / quiet / busy / system issue / other
Acclimatization session? yes/no
```

## Live row

`Case | Activity | Start | End | Volume | INT | Result / short note`

## Activity codes

| Code | Meaning | Rule |
|---|---|---|
| **REQ** | new purchasing request | TALLY |
| **CLAR** | clarify / investigate / missing information | TIME IF |
| **DEC** | purchasing decision / maximalisatie / hold | TALLY + outcome |
| **PO** | create/change/prepare/process PO in Exact | TIME |
| **CHECK** | price / confirmation / information verification | TIME |
| **SEND** | forward/send purchasing communication | TIME |
| **EXC** | aftercare / tracing / rework / exception | TIME IF |
| **OTHER** | relevant purchasing work that does not fit | TIME IF |

## Shorthand

- `L` = lines/items
- `D` = deviations
- `ORD` = proceed/order
- `HOLD` = hold
- `MAX` = maximalisatie
- `MI` = missing/ambiguous information
- `FIN` = Finance-returned issue
- `J` = observable judgement/decision
- `EXP` = observable experience/tacit-knowledge cue
- `MISS` = work happened but could not be captured

## Rules to remember

1. **New purchasing case = new OBS.**
2. **Same purchasing case = same OBS**, even if it returns later.
3. TALLY/TIME does **not** determine OBS numbering.
4. Unrelated non-purchasing email/work = no OBS.
5. If unrelated work interrupts active purchasing, close the row and record `INT=1`.
6. If an interrupting event becomes work on another purchasing case, give that case its own OBS.
7. System waiting is not active buyer time.
8. Do not infer `J` or `EXP` from a pause or facial expression alone; use only observable/explained evidence.
9. If work moves too fast, record `MISS` rather than guessing.
10. No example rows should be pre-filled on the real live sheet.

## Fast examples

```text
OBS-01 | REQ   | —     | —     | —   | 0 | email request
OBS-01 | DEC   | —     | —     | —   | 0 | HOLD J
OBS-02 | CLAR  | 09:18 | 09:24 | —   | 0 | MI drawing; called requester
OBS-03 | CHECK | 10:00 | 10:06 | 10L | 1 | interrupted by call
OBS-04 | REQ   | —     | —     | —   | 0 | new phone request
OBS-03 | CHECK | 10:11 | 10:15 | 10L | 0 | resumed
OBS-05 | SEND  | 10:20 | 10:22 | —   | 0 | PO forwarded
```

## Post-session — do immediately

For each row, add detailed Task ID only where evidence supports it.

Confidence:
- **C** = confident
- **P** = probable
- **U** = not represented in current 31-task register
- **?** = cannot determine

Do not reconstruct unsupported timing, Task IDs, outcomes or reasoning.
