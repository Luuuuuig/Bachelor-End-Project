"""Exploratory Day-5 analysis of Arno's five baseline observation days.

Reads the 21 September enriched dataset (31 Aug, 1 Sep, 8 Sep, 18 Sep) and the
raw 23 September observation table, applies the thesis scope filter, and writes
summary tables plus distribution fits to ``analysis/output/``.

23 September has not yet received the post-session enrichment used for the other
days. Its scope assignment below is a PROVISIONAL researcher rule set, applied
only in this derived analysis and never written back to the observation file.

Run:  python3 analysis/day5_exploratory_analysis.py
Needs: numpy, pandas, scipy, matplotlib
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, special, stats

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "docs/measurement/Activity_Framework_Enriched_Observations_2026-09-21.csv"
OBS_0923 = ROOT / "docs/measurement/Measure_Observation_2026-09-23.md"
OUT = ROOT / "analysis/output"

RNG = np.random.default_rng(20260925)
N_BOOT = int(os.environ.get("N_BOOT", 1000))

# Exposure per day. Only 31 Aug and 1 Sep have a verified net observed time;
# for the other days the notebook window is an UPPER bound on exposure, so any
# rate computed from it is a LOWER bound.
EXPOSURE = {
    "2026-08-31": (165, "verified net"),
    "2026-09-01": (186, "verified net"),
    "2026-09-08": (113, "window upper bound"),
    "2026-09-18": (240, "window upper bound"),
    "2026-09-23": (196, "window upper bound"),
}
WEEKDAY = {d: pd.Timestamp(d).day_name() for d in EXPOSURE}

# Provisional scope for 23 September, keyed by (case, family, start).
# EXC rows are excluded by the 10 September decision; everything else defaults
# to INCLUDE unless listed here.
SCOPE_0923 = {
    ("OBS-06", "OTHER", "11:23"): ("REVIEW_SCOPE", "Client question concerning Dennis; purchasing purpose unclear."),
    ("OBS-09", "OTHER", "11:49"): ("REVIEW_SCOPE", "Exact fault resolution; system constraint rather than a purchasing activity."),
    ("OBS-16", "CLAR", "13:37"): ("REVIEW_SCOPE", "Desk request that became the excluded missing-item trace; CLAR purpose unclear."),
    ("OBS-18", "SEND", "14:47"): ("EXCLUDE_LOGISTICS", "Case note: asking the transport company about next week's timing."),
}


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

def hhmm(t: str) -> int | None:
    m = re.fullmatch(r"\s*(\d{1,2}):(\d{2})\s*", t or "")
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def family(raw: str) -> str:
    raw = raw.strip()
    if raw.upper().startswith("REQ"):
        return "REQ"
    if raw in {"OTHER/EXC"}:
        return "EXC"
    if raw.startswith("["):
        return "UNCLEAR"
    return raw


def lines(vol: str) -> float:
    m = re.fullmatch(r"\s*(\d+)\s*L\s*", vol or "")
    return float(m.group(1)) if m else np.nan


def int_count(v: str) -> float:
    return float(v) if (v or "").strip().isdigit() else np.nan


def load_enriched() -> pd.DataFrame:
    df = pd.read_csv(CSV, dtype=str).fillna("")
    df = df[df["Session"] == "Baseline"].copy()
    out = pd.DataFrame({
        "date": df["Date"],
        "case": df["Case"],
        "family": df["Original family or pilot Task IDs"].map(family),
        "start": df["Start as recorded"].map(hhmm),
        "end": df["End as recorded"].map(hhmm),
        "minutes": pd.to_numeric(df["Recorded exact activity minutes"], errors="coerce"),
        "scope": df["Scope"],
        "quality": df["Quality"],
        "lines": df["Volume as recorded"].map(lines),
        "int": df["INT as recorded"].map(int_count),
        "stage": df["Purchasing stage"],
        "activity": df["Analytical activity"],
        "enriched": True,
    })
    # Partial segment (18 Sep OBS-01 CHECK began before observation) is valid
    # time but not a complete episode duration.
    out["complete_episode"] = ~df["Timing status"].str.contains("began earlier")
    return out


def load_0923() -> pd.DataFrame:
    rows = []
    for line in OBS_0923.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or not cells[0].startswith("OBS-"):
            continue
        case, fam, s, e, vol, intv, dec, note = cells
        f = family(fam)
        start, end = hhmm(s), hhmm(e)
        if f == "EXC":
            scope, reason = "EXCLUDE_EXC", "EXC family excluded (10 September decision)."
        else:
            scope, reason = SCOPE_0923.get((case, f, s), ("INCLUDE", "Provisional default."))
        rows.append({
            "date": "2026-09-23", "case": case, "family": f,
            "start": start, "end": end,
            "minutes": (end - start) if start is not None and end is not None else np.nan,
            "scope": scope, "quality": "VALID", "lines": lines(vol), "int": int_count(intv),
            "stage": "", "activity": "", "enriched": False, "complete_episode": True,
            "scope_reason_provisional": reason,
        })
    return pd.DataFrame(rows)


def load_all() -> pd.DataFrame:
    df = pd.concat([load_enriched(), load_0923()], ignore_index=True)
    df["timed"] = df["minutes"].notna() & (df["minutes"] > 0)
    df["in_scope"] = (df["scope"] == "INCLUDE") & (df["quality"] == "VALID")
    df["in_scope_or_review"] = df["scope"].isin(["INCLUDE", "REVIEW_SCOPE"]) & (df["quality"] == "VALID")
    df["day_no"] = df["date"].map({d: i + 1 for i, d in enumerate(EXPOSURE)})
    return df


# --------------------------------------------------------------------------
# Rounding-aware distribution fitting
# --------------------------------------------------------------------------
# A clock shows whole minutes, so recorded duration d = floor(U + T) with the
# start-second phase U ~ Uniform(0,1) and true duration T. Then
#   P(d = k) = G(k+1) - 2 G(k) + G(k-1),   G(x) = integral_{-inf}^x F(t) dt
# Sub-minute actions (d = 0) are tallied, not timed, so the timed sample is
# conditioned on d >= 1:  P(d = k | d >= 1) = P(d = k) / (1 - G(1) + G(0)).
# For positive distributions G(x) = x F(x) - E[T; T <= x], and the partial
# mean has a closed form for every family below.

def _G_positive(cdf, pmean):
    def G(x):
        x = np.asarray(x, float)
        xp = np.clip(x, 1e-12, None)
        return np.where(x > 0, xp * cdf(xp) - pmean(xp), 0.0)
    return G


def _families():
    def expo(p):
        (lam,) = np.exp(p)
        G = _G_positive(lambda x: 1 - np.exp(-lam * x), lambda x: special.gammainc(2, lam * x) / lam)
        return G, lambda n: RNG.exponential(1 / lam, n), {"rate_per_min": lam, "mean_min": 1 / lam}

    def gamma(p):
        a, th = np.exp(p)
        G = _G_positive(lambda x: special.gammainc(a, x / th), lambda x: a * th * special.gammainc(a + 1, x / th))
        return G, lambda n: RNG.gamma(a, th, n), {"shape": a, "scale": th, "mean_min": a * th}

    def lognorm(p):
        mu, s = p[0], np.exp(p[1])
        G = _G_positive(lambda x: stats.norm.cdf((np.log(x) - mu) / s),
                        lambda x: np.exp(mu + s * s / 2) * stats.norm.cdf((np.log(x) - mu - s * s) / s))
        return G, lambda n: RNG.lognormal(mu, s, n), {
            "mu_log": mu, "sigma_log": s, "median_min": np.exp(mu), "mean_min": np.exp(mu + s * s / 2)}

    def weibull(p):
        k, lam = np.exp(p)
        G = _G_positive(lambda x: 1 - np.exp(-(x / lam) ** k),
                        lambda x: lam * special.gamma(1 + 1 / k) * special.gammainc(1 + 1 / k, (x / lam) ** k))
        return G, lambda n: lam * RNG.weibull(k, n), {"shape": k, "scale": lam, "mean_min": lam * special.gamma(1 + 1 / k)}

    return {"Lognormal": (lognorm, 2), "Gamma": (gamma, 2), "Weibull": (weibull, 2),
            "Exponential": (expo, 1)}


FAMILIES = _families()


def normal_reference(d):
    """What a mean +/- SD summary implies: a normal with the sample mean and SD."""
    m, sd = d.mean(), d.std(ddof=1)
    return {"n": len(d), "mean": round(m, 2), "median": float(np.median(d)), "sd": round(sd, 2),
            "skewness": round(float(stats.skew(d)), 2),
            "normal_share_below_0_min": round(float(stats.norm.cdf(0, m, sd)), 3),
            "observed_share_over_mean_plus_2sd": round(float((d > m + 2 * sd).mean()), 3),
            "normal_share_over_mean_plus_2sd": 0.023}


def normal_G(m, sd):
    def G(x):
        z = (np.asarray(x, float) - m) / sd
        return sd * (z * stats.norm.cdf(z) + stats.norm.pdf(z))
    return G


def _start(name, d):
    m, v = d.mean(), d.var(ddof=1) if len(d) > 1 else d.mean()
    ld = np.log(d)
    return {
        "Exponential": [np.log(1 / m)],
        "Gamma": [np.log(max(m * m / v, 0.2)), np.log(v / m)],
        "Lognormal": [ld.mean(), np.log(max(ld.std(), 0.1))],
        "Weibull": [np.log(1.2), np.log(m)],
    }[name]


def pmf_rounded(k, G):
    k = np.asarray(k, float)
    p = G(k + 1) - 2 * G(k) + G(k - 1)
    norm = 1 - (G(1.0) - G(0.0))
    return np.clip(p, 1e-300, None) / max(float(norm), 1e-300)


def fit_one(name, d, x0=None):
    builder, npar = FAMILIES[name]
    ks, cnt = np.unique(d, return_counts=True)

    def nll(p):
        with np.errstate(all="ignore"):
            try:
                G = builder(p)[0]
                val = -(cnt * np.log(pmf_rounded(ks, G))).sum()
            except (FloatingPointError, OverflowError, ValueError):
                return 1e12
        return val if np.isfinite(val) else 1e12

    starts = [np.asarray(x0)] if x0 is not None else [np.array(_start(name, d)) + j for j in (0.0, 0.3, -0.3)]
    best = None
    for s0 in starts:
        res = optimize.minimize(nll, s0, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 4000})
        if best is None or res.fun < best.fun:
            best = res
    G, sampler, params = builder(best.x)
    return {"name": name, "k": npar, "nll": best.fun, "aic": 2 * npar + 2 * best.fun,
            "p": best.x, "params": params, "G": G, "sampler": sampler}


def rounded_sample(sampler, n):
    """Simulate the recording process: floor(U + T), keep d >= 1."""
    out, batch = [], 4 * n
    for _ in range(50):
        t = sampler(batch)
        d = np.floor(RNG.uniform(0, 1, t.size) + t)
        out.extend(d[d >= 1].tolist())
        if len(out) >= n:
            return np.array(out[:n])
        batch *= 4
    raise RuntimeError("model puts almost no mass on durations >= 1 minute")


def discrete_ks(d, G):
    ks = np.arange(1, int(d.max()) + 2)
    model_cdf = np.cumsum(pmf_rounded(ks, G))
    emp_cdf = np.array([(d <= k).mean() for k in ks])
    return np.abs(model_cdf - emp_cdf).max()


def bootstrap_gof(name, d, fit, n_boot=N_BOOT):
    """Parametric bootstrap p-value for the discrete KS statistic, refitting each replicate."""
    obs = discrete_ks(d, fit["G"])
    exceed = 0
    for _ in range(n_boot):
        sim = rounded_sample(fit["sampler"], len(d))
        f2 = fit_one(name, sim, x0=fit["p"])
        if discrete_ks(sim, f2["G"]) >= obs:
            exceed += 1
    return obs, (exceed + 1) / (n_boot + 1)


def fit_all(d, label, n_boot=N_BOOT):
    d = np.asarray(d, float)
    fits = [fit_one(n, d) for n in FAMILIES]
    best_aic = min(f["aic"] for f in fits)
    rows = []
    for f in sorted(fits, key=lambda f: f["aic"]):
        ks_stat, p = bootstrap_gof(f["name"], d, f, n_boot)
        rows.append({
            "sample": label, "n": len(d), "model": f["name"], "AIC": round(f["aic"], 1),
            "dAIC": round(f["aic"] - best_aic, 1),
            "akaike_weight": None, "KS_discrete": round(ks_stat, 3), "bootstrap_p": round(p, 3),
            "params": {k: round(float(v), 3) for k, v in f["params"].items()},
        })
    w = np.exp(-0.5 * np.array([r["dAIC"] for r in rows]))
    for r, wi in zip(rows, w / w.sum()):
        r["akaike_weight"] = round(float(wi), 3)
    return rows, {f["name"]: f for f in fits}


# --------------------------------------------------------------------------
# Summaries
# --------------------------------------------------------------------------

def q(x, p):
    return float(np.percentile(x, p)) if len(x) else np.nan


def per_day(df):
    rows = []
    for date, g in df.groupby("date"):
        exp_min, exp_kind = EXPOSURE[date]
        inc = g[g.in_scope & g.timed]
        rows.append({
            "day": int(g.day_no.iloc[0]), "date": date, "weekday": WEEKDAY[date],
            "enriched": bool(g.enriched.all()),
            "exposure_min": exp_min, "exposure_kind": exp_kind,
            "rows": len(g), "timed_rows": int(g.timed.sum()),
            "recorded_min_all": int(g.loc[g.timed, "minutes"].sum()),
            "exc_min": int(g.loc[g.timed & g.scope.str.startswith("EXCLUDE"), "minutes"].sum()),
            "review_min": int(g.loc[g.timed & (g.scope == "REVIEW_SCOPE"), "minutes"].sum()),
            "in_scope_timed_rows": len(inc), "in_scope_min": int(inc.minutes.sum()),
            "in_scope_min_per_exposure_hour": round(inc.minutes.sum() / exp_min * 60, 1),
            "cases": g.case.nunique(),
            "cases_per_exposure_hour": round(g.case.nunique() / exp_min * 60, 2),
            "in_scope_episodes_per_exposure_hour": round(len(inc) / exp_min * 60, 2),
            "median_in_scope_episode_min": q(inc.minutes, 50),
            "INT_total": int(np.nansum(g["int"])),
        })
    return pd.DataFrame(rows)


def family_by_day(df, fams):
    inc = df[df.in_scope & df.timed]
    t = inc.pivot_table(index="family", columns="date", values="minutes", aggfunc="sum", fill_value=0)
    return t.reindex(fams).fillna(0).astype(int)


def cumulative_stability(df, fams):
    """Family shares of in-scope minutes and median episode durations after each added day."""
    inc = df[df.in_scope & df.timed]
    share_rows, med_rows, rank_rows = [], [], []
    dates = list(EXPOSURE)
    for i in range(1, len(dates) + 1):
        sub = inc[inc.date.isin(dates[:i])]
        tot = sub.minutes.sum()
        s = sub.groupby("family").minutes.sum().reindex(fams).fillna(0)
        share_rows.append({"through_day": i, **{f: round(100 * s[f] / tot, 1) for f in fams}})
        med_rows.append({"through_day": i, "ALL": q(sub.minutes, 50),
                         **{f: q(sub[sub.family == f].minutes, 50) for f in fams}})
        rank_rows.append({"through_day": i, "ranking_by_minutes": " > ".join(s.sort_values(ascending=False).index[s.sort_values(ascending=False) > 0])})
    shares, meds, ranks = pd.DataFrame(share_rows), pd.DataFrame(med_rows), pd.DataFrame(rank_rows)
    shift = (shares[fams].diff().abs().max(axis=1)).round(1)
    shares["max_share_shift_pp"] = shift
    return shares, meds, ranks


def leave_one_day_out(df, fams):
    inc = df[df.in_scope & df.timed]
    rows = []
    for date in EXPOSURE:
        sub = inc[inc.date != date]
        s = sub.groupby("family").minutes.sum().reindex(fams).fillna(0)
        rows.append({"left_out": date, **{f: round(100 * s[f] / s.sum(), 1) for f in fams},
                     "ranking": " > ".join(s.sort_values(ascending=False).index[:4])})
    return pd.DataFrame(rows)


def heterogeneity(df):
    inc = df[df.in_scope & df.timed & df.complete_episode]
    out = {}
    for label, sub in {"ALL in-scope": inc, "PO": inc[inc.family == "PO"],
                       "CLAR": inc[inc.family == "CLAR"], "SEND": inc[inc.family == "SEND"]}.items():
        groups = [g.minutes.values for _, g in sub.groupby("date") if len(g) >= 3]
        if len(groups) >= 2:
            h, p = stats.kruskal(*groups)
            out[label] = {"days_with_n>=3": len(groups), "H": round(h, 2), "p": round(p, 3)}
    # Family mix x day: Monte Carlo chi-square on in-scope episode counts
    tab = pd.crosstab(inc.family, inc.date)
    tab = tab.loc[tab.sum(axis=1) >= 5]
    obs_chi = stats.chi2_contingency(tab, correction=False)[0]
    fam_labels = np.repeat(tab.index.values, tab.sum(axis=1).values)
    day_counts = tab.sum(axis=0).values
    exceed = 0
    for _ in range(5000):
        perm = RNG.permutation(fam_labels)
        cuts = np.cumsum(day_counts)[:-1]
        parts = np.split(perm, cuts)
        sim = np.array([[np.sum(p == f) for p in parts] for f in tab.index])
        if stats.chi2_contingency(sim, correction=False)[0] >= obs_chi:
            exceed += 1
    out["family mix x day (counts)"] = {"families": list(tab.index), "chi2": round(obs_chi, 2),
                                        "monte_carlo_p": round((exceed + 1) / 5001, 3)}
    return out


def po_volume(df):
    po = df[df.in_scope & df.timed & (df.family == "PO") & df.lines.notna()]
    rho, p = stats.spearmanr(po.lines, po.minutes)
    return {"n": len(po), "spearman_rho": round(rho, 2), "p": round(p, 3),
            "min_per_line_median": round(float(np.median(po.minutes / po.lines)), 2)}


def switch_intervals(df):
    """Minutes between the first timed episode of successive new cases, within a day."""
    gaps = []
    for date, g in df[df.timed].groupby("date"):
        first = g.groupby("case").start.min().sort_values().values
        d = np.diff(first)
        gaps.extend(d[(d > 0) & (d < 60)].tolist())  # drop lunch/block gaps
    gaps = np.array(gaps, float)
    return gaps


def daypart(df, fams):
    """Morning (start before 12:45) versus afternoon, in-scope timed work only."""
    inc = df[df.in_scope & df.timed & df.complete_episode].copy()
    inc["daypart"] = np.where(inc.start < 12 * 60 + 45, "AM", "PM")
    rows = []
    for dp, g in inc.groupby("daypart"):
        s = g.groupby("family").minutes.sum().reindex(fams).fillna(0)
        rows.append({"daypart": dp, "days": g.date.nunique(), "episodes": len(g),
                     "minutes": int(g.minutes.sum()), "median": q(g.minutes, 50),
                     **{f"{f}_%": round(100 * s[f] / s.sum(), 1) for f in fams}})
    mw = stats.mannwhitneyu(inc[inc.daypart == "AM"].minutes, inc[inc.daypart == "PM"].minutes)
    return pd.DataFrame(rows), {"mann_whitney_U": float(mw.statistic), "p": round(float(mw.pvalue), 3)}


def saturation(df):
    """New analytical activities per enriched day; new families per day (all five)."""
    seen_a, seen_f, rows = set(), set(), []
    for date, g in df.groupby("date", sort=True):
        acts = set(g.loc[g.enriched & ~g.activity.isin(["", "Unresolved activity"]), "activity"])
        fams = set(g.family)
        rows.append({"date": date,
                     "new_analytical_activities": len(acts - seen_a) if g.enriched.all() else None,
                     "cum_analytical_activities": len(seen_a | acts) if g.enriched.all() else None,
                     "new_families": sorted(fams - seen_f)})
        seen_a |= acts
        seen_f |= fams
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------
# Figures
# --------------------------------------------------------------------------

def figures(df, fits_all, fits_po, shares, fams):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Reference categorical palette (fixed slot order, validated light mode).
    # Text stays in ink tokens; colour marks carry identity only.
    ink, ink2, muted, grid, surface = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
    slot = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
    fam_order = ["PO", "CLAR", "CHECK", "SEND", "OTHER"]
    fam_col = dict(zip(fam_order, slot))
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": grid, "axes.labelcolor": ink2,
                         "xtick.color": ink2, "ytick.color": ink2, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": surface,
                         "axes.facecolor": surface, "savefig.facecolor": surface})

    def pmf_panel(ax, d, fits, title):
        ks = np.arange(1, int(d.max()) + 1)
        emp = np.array([(d == k).mean() for k in ks])
        ax.bar(ks, emp, color="#cfd3d8", width=0.8, label=f"Observed episodes (n={len(d)})")
        ax.plot(ks, pmf_rounded(ks, fits["Lognormal"]["G"]), marker="o", ms=4, lw=2,
                color=slot[0], label="Lognormal fit")
        ax.plot(ks, pmf_rounded(ks, fits["Exponential"]["G"]), marker="s", ms=4, lw=2,
                color=slot[1], label="Exponential fit")
        ax.plot(ks, pmf_rounded(ks, normal_G(d.mean(), d.std(ddof=1))), ls="--", lw=1.5,
                color=ink2, label="Normal with sample mean and SD")
        ax.set_xlabel("Recorded episode duration (whole minutes)")
        ax.set_ylabel("Share of episodes")
        ax.set_title(title, loc="left", color=ink, fontsize=11)
        ax.set_xlim(0.3, min(d.max(), 22) + 0.7)
        ax.set_xticks([1, 2, 3, 4, 5, 10, 15, 20])
        ax.grid(axis="y", color=grid, lw=0.6)
        ax.set_axisbelow(True)
        ax.legend(frameon=False, fontsize=8, labelcolor=ink2)

    inc = df[df.in_scope & df.timed & df.complete_episode]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    pmf_panel(axes[0], inc.minutes.values, fits_all, "All in-scope episodes, five days")
    pmf_panel(axes[1], inc[inc.family == "PO"].minutes.values, fits_po, "PO episodes only")
    fig.tight_layout()
    fig.savefig(OUT / "fig1_duration_fits.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.5, 4))
    x = shares.through_day.values
    for f in fam_order:
        ax.plot(x, shares[f], marker="o", ms=6, lw=2, color=fam_col[f], label=f,
                mec=surface, mew=1.5)
    # End labels, nudged apart so close values do not collide.
    ends = sorted(((shares[f].iloc[-1], f) for f in fam_order))
    placed = []
    for v, f in ends:
        y = max(v, placed[-1] + 2.2) if placed else v
        placed.append(y)
        ax.annotate(f"{f} {v:.0f}%", (x[-1], v), xytext=(x[-1] + 0.12, y), textcoords="data",
                    va="center", color=ink2, fontsize=9)
    ax.set_xticks(x, ["Day 1" if i == 1 else f"Days 1–{i}" for i in x])
    ax.set_ylabel("Share of in-scope timed minutes (%)")
    ax.set_ylim(0, None)
    ax.set_title("Family mix after each added day", loc="left", color=ink, fontsize=11)
    ax.grid(axis="y", color=grid, lw=0.6)
    ax.set_axisbelow(True)
    ax.set_xlim(0.8, len(x) + 0.9)
    ax.legend(frameon=False, fontsize=8, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.1),
              labelcolor=ink2)
    fig.tight_layout()
    fig.savefig(OUT / "fig2_cumulative_family_shares.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4))
    dates = list(EXPOSURE)
    data = [inc[inc.date == d].minutes.values for d in dates]
    ax.boxplot(data, showfliers=False, widths=0.5, medianprops={"color": slot[0], "lw": 2},
               boxprops={"color": ink2}, whiskerprops={"color": ink2}, capprops={"color": ink2})
    for i, v in enumerate(data, 1):
        ax.scatter(np.full(len(v), i) + RNG.uniform(-0.14, 0.14, len(v)), v, s=10, color=muted,
                   alpha=0.6, lw=0)
    labels = [f"{pd.Timestamp(d):%d %b}\n{WEEKDAY[d][:3]}" + ("\n(provisional)" if d == "2026-09-23" else "")
              for d in dates]
    ax.set_xticks(range(1, 6), labels)
    ax.set_yscale("log")
    ax.set_yticks([1, 2, 5, 10, 20], ["1", "2", "5", "10", "20"])
    ax.set_ylabel("Episode duration (min, log scale)")
    ax.set_title("In-scope episode durations by day", loc="left", color=ink, fontsize=11)
    ax.grid(axis="y", color=grid, lw=0.6)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_durations_by_day.png", dpi=160)
    plt.close(fig)


# --------------------------------------------------------------------------

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_all()
    fams = ["PO", "CLAR", "SEND", "CHECK", "OTHER", "REQ"]

    df.drop(columns=["stage"]).to_csv(OUT / "combined_five_day_rows.csv", index=False)

    days = per_day(df)
    fam_day = family_by_day(df, fams)
    shares, meds, ranks = cumulative_stability(df, fams)
    lodo = leave_one_day_out(df, fams)
    het = heterogeneity(df)
    vol = po_volume(df)
    sat = saturation(df)
    dparts, dpart_test = daypart(df, fams)

    inc = df[df.in_scope & df.timed & df.complete_episode]
    samples = {
        "ALL in-scope": inc.minutes.values,
        "PO": inc[inc.family == "PO"].minutes.values,
        "CLAR": inc[inc.family == "CLAR"].minutes.values,
        "SEND": inc[inc.family == "SEND"].minutes.values,
        "CHECK": inc[inc.family == "CHECK"].minutes.values,
        "ALL incl. REVIEW_SCOPE (sensitivity)": df[df.in_scope_or_review & df.timed & df.complete_episode].minutes.values,
        "ALL days 1-4 only (enriched)": inc[inc.enriched].minutes.values,
    }
    fit_rows, fit_objs = [], {}
    for label, d in samples.items():
        rows, objs = fit_all(d, label)
        fit_rows += rows
        fit_objs[label] = objs

    normal_ref = [{"sample": k, **normal_reference(np.asarray(v, float))} for k, v in samples.items()]

    gaps = switch_intervals(df)
    gap_rows, _ = fit_all(np.clip(np.round(gaps), 1, None), "Minutes between new-case starts")
    fit_rows += gap_rows
    gap_summary = {"n": len(gaps), "mean": round(gaps.mean(), 2), "sd": round(gaps.std(ddof=1), 2),
                   "cv": round(gaps.std(ddof=1) / gaps.mean(), 2)}

    fam_summary = []
    for f in fams:
        v = inc[inc.family == f].minutes.values
        occ = df[(df.family == f) & df.in_scope]
        fam_summary.append({"family": f, "occurrences_incl_untimed": len(occ), "timed_n": len(v),
                            "minutes": int(v.sum()) if len(v) else 0,
                            "median": q(v, 50), "p25": q(v, 25), "p75": q(v, 75),
                            "p90": q(v, 90), "max": float(v.max()) if len(v) else np.nan,
                            "mean": round(float(v.mean()), 2) if len(v) else np.nan,
                            "cv": round(float(v.std(ddof=1) / v.mean()), 2) if len(v) > 1 else np.nan})
    fam_summary = pd.DataFrame(fam_summary)

    figures(df, fit_objs["ALL in-scope"], fit_objs["PO"], shares, fams)

    results = {
        "per_day": days.to_dict("records"),
        "family_minutes_by_day": fam_day.reset_index().to_dict("records"),
        "family_summary": fam_summary.to_dict("records"),
        "cumulative_shares": shares.to_dict("records"),
        "cumulative_medians": meds.to_dict("records"),
        "cumulative_ranking": ranks.to_dict("records"),
        "leave_one_day_out": lodo.to_dict("records"),
        "heterogeneity": het,
        "po_duration_vs_lines": vol,
        "saturation": sat.to_dict("records"),
        "daypart": dparts.to_dict("records"),
        "daypart_duration_test": dpart_test,
        "distribution_fits": fit_rows,
        "normal_reference": normal_ref,
        "new_case_start_gaps": gap_summary,
    }
    (OUT / "results.json").write_text(json.dumps(results, indent=2, default=lambda o: None if (isinstance(o, float) and np.isnan(o)) else str(o)))

    pd.set_option("display.width", 200, "display.max_columns", 30)
    print("\n== Per day ==\n", days.to_string(index=False))
    print("\n== In-scope minutes by family x day ==\n", fam_day.to_string())
    print("\n== Family summary (in-scope, complete episodes) ==\n", fam_summary.to_string(index=False))
    print("\n== Cumulative shares (%) ==\n", shares.to_string(index=False))
    print("\n== Cumulative medians ==\n", meds.to_string(index=False))
    print("\n== Cumulative ranking ==\n", ranks.to_string(index=False))
    print("\n== Leave one day out ==\n", lodo.to_string(index=False))
    print("\n== Heterogeneity ==\n", json.dumps(het, indent=1))
    print("\n== PO duration vs lines ==\n", vol)
    print("\n== Saturation ==\n", sat.to_string(index=False))
    print("\n== Daypart ==\n", dparts.to_string(index=False), dpart_test)
    print("\n== New-case start gaps ==\n", gap_summary)
    print("\n== Normal reference ==\n", pd.DataFrame(normal_ref).to_string(index=False))
    print("\n== Distribution fits ==")
    print(pd.DataFrame(fit_rows).to_string(index=False))


if __name__ == "__main__":
    main()
