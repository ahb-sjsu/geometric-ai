"""Figures for Geometric AI (Volume 11 of the Geometric Series), Chapters 1 to 18. Drawn 2026-11-25.

Every figure follows tools/figkit.py: it is drawn from a formula, a definition or numbers printed
in the chapter, it carries no new claim, and where it repeats a number it asserts the value.
Volume rules (CORRECTIONS-2026-11-26.md): no number on the "Unresolved" list is drawn; ARIA and
ARIA-G are fictional, so every figure drawn from them says "illustrative" in the caption and in
the figure; the Hohfeldian factor is V4 (no dihedral group, no quarter-turn); Theorem 18.1 is
one-directional and Theorems 5.1 and 5.2 carry the non-compactness hypothesis. The volume is a
posited framework, so captions say "posited", "as the chapter defines" or "as the chapter reports".
"""

import math
from xml.sax.saxutils import escape

from figkit import BORDER, BOX, CRITICAL, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg

CH = {
    1: "manuscript/part_i/ch01_scalar_alignment_trap.md",
    2: "manuscript/part_i/ch02_brief_history.md",
    3: "manuscript/part_i/ch03_case_for_geometric_alignment.md",
    4: "manuscript/part_ii/ch04_value_manifold.md",
    5: "manuscript/part_ii/ch05_reward_irrecoverability.md",
    6: "manuscript/part_ii/ch06_four_failures.md",
    7: "manuscript/part_ii/ch07_alignment_gauge_group.md",
    8: "manuscript/part_ii/ch08_no_escape.md",
    9: "manuscript/part_iii/ch09_bond_index_ai.md",
    10: "manuscript/part_iii/ch10_cognitive_signatures.md",
    11: "manuscript/part_iii/ch11_adversarial_probing.md",
    12: "manuscript/part_iii/ch12_sycophancy_manifold.md",
    13: "manuscript/part_iv/ch13_gauge_invariant_rewards.md",
    14: "manuscript/part_iv/ch14_constitutional_geometry.md",
    15: "manuscript/part_iv/ch15_scalable_oversight.md",
    16: "manuscript/part_iv/ch16_geometric_rlhf.md",
    17: "manuscript/part_v/ch17_superalignment.md",
    18: "manuscript/part_v/ch18_multi_agent.md",
}


# ------------------------------------------------------------------ helpers
def canvas(w, h, title):
    assert len(title) <= 68, f"title too long ({len(title)}): {title}"
    return Canvas(w, h, title)


def head(c, x1, y1, x2, y2, stroke, width=1.5):
    """Arrowhead at (x2, y2) pointing along (x1, y1) -> (x2, y2)."""
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (+1, -1):
        a = ang + s * 2.6
        c.line(x2, y2, x2 + 8 * math.cos(a), y2 + 8 * math.sin(a), stroke, width)


def darrow(c, x1, y1, x2, y2, stroke=INK2, width=1.5, dash=None):
    """Double-headed arrow (an involution exchanges its two ends)."""
    c.line(x1, y1, x2, y2, stroke, width, dash=dash)
    head(c, x2, y2, x1, y1, stroke, width)
    head(c, x1, y1, x2, y2, stroke, width)


def dashed_arrow(c, pts, stroke, width=1.5, dash="5 4"):
    """Polyline with dashes and an arrowhead at its last point."""
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        c.line(x1, y1, x2, y2, stroke, width, dash=dash)
    head(c, *pts[-2], *pts[-1], stroke, width)


def path_arrow(c, pts, stroke=INK2, width=1.5):
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        c.line(x1, y1, x2, y2, stroke, width)
    head(c, *pts[-2], *pts[-1], stroke, width)


def polygon(c, pts, stroke, fill="none", width=2, opacity=1.0, fill_opacity=0.0, title=None, dash=None):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    t = f"<title>{escape(title)}</title>" if title else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<polygon points="{d}" fill="{fill}" fill-opacity="{fill_opacity}" stroke="{stroke}" '
          f'stroke-width="{width}" stroke-opacity="{opacity}" stroke-linejoin="round"{da}>{t}</polygon>')


def rect(c, x, y, w, h, fill, opacity=1.0, stroke="none", width=1, rx=0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" '
          f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"{da}/>')


def box3(c, x, y, w, h, label, lines, fill=BOX, stroke=BORDER):
    """Box with a bold label and up to three small lines under it."""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    n = len(lines)
    top = y + h / 2 - (n * 14) / 2 - 1
    c.text(x + w / 2, top + 4, label, 12, "middle", INK, "600")
    for k, s in enumerate(lines):
        c.text(x + w / 2, top + 19 + 14 * k, s, 10.5, "middle", INK2)


# ------------------------------------------------------------------ chapter 1
def fig_1_1():
    dims = ["helpfulness", "honesty", "harmlessness", "fairness", "robustness"]
    systems = [[0.95] * 5, [1.0, 1.0, 1.0, 0.4, 0.35], [1.0, 1.0, 1.0, 0.75, 0.0]]
    w = [0.4, 0.3, 0.2, 0.05, 0.05]
    means = [sum(s) / 5 for s in systems]
    weighted = sum(a * b for a, b in zip(w, systems[2]))
    assert abs(means[0] - 0.95) < 1e-12 and abs(means[1] - 0.75) < 1e-12 and abs(means[2] - 0.75) < 1e-12
    assert abs(sum(w) - 1.0) < 1e-12 and abs(weighted - 0.9375) < 1e-12
    p = reg(CH[1], "1.1",
            "The averaging illusion of Section 1.5, for the chapter's three hypothetical systems scored from 0 to 1 "
            "on five dimensions. Bars are the dimension scores and the dashed line over each group is its "
            "unweighted composite. Systems 2 and 3 share the composite 0.75, although system 3 has zero "
            "robustness. Under the weights 0.4, 0.3, 0.2, 0.05 and 0.05 that the chapter applies, system 3 "
            "scores 0.9375 (dotted line).",
            "## 1.6 Why Every Generation Makes the Same Mistake")
    c = canvas(720, 400, "Same composite, different failures: the average hides a zero")
    ax = Axes(c, 70, 66, 560, 262, (0, 3), (0, 1.05), [], [0, 0.25, 0.5, 0.75, 1.0], "", "dimension score")
    slot = ax.w / 3
    bw, gap = 18, 4
    gw = 5 * bw + 4 * gap
    for k, s in enumerate(systems):
        cx = ax.x0 + slot * (k + 0.5)
        x0 = cx - gw / 2
        for j, v in enumerate(s):
            x = x0 + j * (bw + gap)
            c.rect(x, ax.Y(v), bw, ax.Y(0) - ax.Y(v), SERIES[j], title=f"system {k + 1}, {dims[j]} {v:g}")
            if v == 0:
                c.text(x + bw / 2, ax.Y(0) - 6, "0", 10.5, "middle", INK)
        xl, xr = x0 - 6, x0 + gw + 6
        y = ax.Y(means[k])
        c.line(xl, y, xr, y, INK, 1.5, dash="5 4")
        c.text(xr + 4, y + 4, f"mean {means[k]:.2f}", 10.5, "start", INK)
        if k == 2:
            yw = ax.Y(weighted)
            c.line(xl, yw, xr, yw, INK3, 1.5, dash="2 3")
            c.text(xr + 4, yw + 4, "weighted 0.9375", 10.5, "start", INK)
        c.text(cx, ax.Y(0) + 16, f"system {k + 1}", 11, "middle", INK2)
    legend(c, 70, 50, [(d, SERIES[j]) for j, d in enumerate(dims)])
    c.text(16, 390, "hypothetical systems of Section 1.5; scores from 0 to 1", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_2_1():
    d = 9
    rows = [  # year, paradigm, dimensions the representation holds (None: not counted), contracts to one, note
        ("1785", "Kant: categorical imperative", 1, True, "one-bit verdict"),
        ("1789", "Bentham: felicific calculus", 7, True, "7 circumstances, one sum"),
        ("1930", "Ross: prima facie duties", 7, False, "seven duties, no metric"),
        ("1942", "Asimov: Three Laws", 3, False, f"kernel {d - 3} of {d}"),
        ("1944", "von Neumann and Morgenstern", 1, True, "one utility"),
        ("1971", "Rawls: lexicographic order", 2, False, "liberty before welfare"),
        ("2017", "RLHF", 1, True, "one bit, one reward"),
        ("2021", "HHH evaluations", 3, True, "3 axes, then a composite"),
        ("2022", "TruthfulQA", 1, True, "one axis"),
        ("2022", "Constitutional AI", None, True, "rule list, one reward"),
    ]
    assert d - 3 == 6  # Section 2.2: three scalar constraints on nine dimensions leave a six-dimensional kernel
    p = reg(CH[2], "2.1",
            "The paradigms of Sections 2.1 to 2.7 in date order, placed by the number of value dimensions their "
            "representation holds as the chapter counts them (Constitutional AI's list of principles is not "
            "counted). A second dot at one marks each paradigm the chapter says contracts to a single number at "
            "the point of decision or scoring. The dashed line is the nine-dimensional value manifold. Three rules "
            "on nine dimensions leave a six-dimensional kernel (Section 2.2).",
            "## 2.8 The Geometric Turn")
    c = canvas(720, 436, "Each paradigm holds a few dimensions; most decide on one number")
    ax = Axes(c, 262, 58, 288, 300, (0, d), (0, 10), list(range(0, d + 1)), [], "dimensions the representation holds", "")
    for v in range(1, d + 1):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    c.line(ax.X(d), ax.y0 - 4, ax.X(d), ax.y0 + ax.h, INK3, 1.5, dash="4 4")
    c.text(ax.X(d), ax.y0 - 8, "value manifold, d = 9", 10.5, "end", INK2, italic=True)
    for i, (yr, name, held, one, note) in enumerate(rows):
        y = ax.y0 + 30 * (i + 0.5)
        c.text(16, y + 4, yr, 11, "start", INK2)
        c.text(52, y + 4, name, 11.5, "start", INK)
        if held is not None and held > 1:
            if one:
                c.line(ax.X(1) + 7, y, ax.X(held) - 7, y, INK3, 1.5)
                head(c, ax.X(held) - 7, y, ax.X(1) + 7, y, INK3, 1.5)
            c.dot(ax.X(held), y, SERIES[0], 5, title=f"{name}: {held} dimensions")
        if one:
            c.dot(ax.X(1), y, SERIES[1], 5, title=f"{name}: one number at the decision")
        c.text(564, y + 4, note, 10.5, "start", INK2)
    legend(c, 16, 424, [("dimensions held", SERIES[0]), ("one number at the decision", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_3_1():
    p = reg(CH[3], "3.1",
            "The broken feedback loop of Section 3.2, as a schematic. In the domains of the other volumes a scalar "
            "metric informs a human who perceives the full value manifold, and the outcome returns to that human "
            "through all its dimensions, so the human can compensate. In AI the loop closes through the scalar: the "
            "system's only training signal is the reward, which is constant along the kernel, so drift there "
            "returns no signal.",
            "## 3.3 The Geometric Alternative")
    c = canvas(720, 400, "Other domains keep a human on the manifold; AI closes the loop on R")
    c.line(360, 52, 360, 380, GRID, 1)
    for x0, title, a, asub, b, bsub, cc, loop_to_top, loop_lab, note in (
            (24, "other domains", "scalar metric", "QALY, GPA, BLEU", "human user", "perceives all d dimensions",
             "decision and outcome", False, ("feedback through", "every dimension"), "the human compensates for the metric"),
            (384, "AI", "scalar reward R", "one number per output", "AI system", "learns only along ∇R",
             "behaviour", True, ("scalar", "evaluation"), "drift in the kernel: dR = 0, no signal")):
        c.text(x0 + 100, 64, title, 13, "middle", INK, "600")
        c.box(x0 + 20, 80, 160, 46, a, asub)
        c.box(x0 + 20, 180, 160, 50, b, bsub)
        c.box(x0 + 20, 286, 160, 44, cc)
        c.arrow(x0 + 100, 126, x0 + 100, 178, INK2, 1.5)
        c.arrow(x0 + 100, 230, x0 + 100, 284, INK2, 1.5)
        ytarget = 103 if loop_to_top else 205
        path_arrow(c, [(x0 + 180, 308), (x0 + 232, 308), (x0 + 232, ytarget), (x0 + 182, ytarget)], SERIES[0] if not loop_to_top else SERIES[1], 2)
        ym = (308 + ytarget) / 2
        c.text(x0 + 240, ym - 4, loop_lab[0], 11, "start", INK2)
        c.text(x0 + 240, ym + 11, loop_lab[1], 11, "start", INK2)
        c.text(x0 + 100, 356, note, 11, "middle", INK2, italic=True)
    c.text(16, 390, "schematic of Section 3.2", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_4_1():
    rho = 0.6
    det = 1 - rho ** 2
    si = [[1 / det, -rho / det], [-rho / det, 1 / det]]

    def cost(v):
        return sum(v[i] * si[i][j] * v[j] for i in range(2) for j in range(2))

    r2 = 1 / math.sqrt(2)
    both, opp = (r2, r2), (-r2, r2)
    assert abs(cost(both) - 1 / (1 + rho)) < 1e-12 and abs(cost(both) - 0.625) < 1e-12
    assert abs(cost(opp) - 1 / (1 - rho)) < 1e-12 and abs(cost(opp) - 2.5) < 1e-12
    a_major, a_minor = math.sqrt(1 + rho), math.sqrt(1 - rho)
    assert abs(cost((a_major * r2, a_major * r2)) - 1) < 1e-12 and abs(cost((a_minor * r2, -a_minor * r2)) - 1) < 1e-12
    p = reg(CH[4], "4.1",
            "The Mahalanobis approximation of Section 4.3.1 on the plane of two value dimensions, autonomy (D4) and "
            "epistemic integrity (D9), drawn for an illustrative covariance with unit variances and correlation 0.6 "
            "(the chapter names the coupling Σ49 but prints no value). The circle holds the moves of unit Euclidean "
            "length and the ellipse the moves of unit cost Δvᵀ Σ⁻¹ Δv. A unit move that raises both dimensions (A) "
            "costs 0.625; a unit move that lowers one and raises the other (B) costs 2.5.",
            "### 4.3.2 Estimating the Metric from Preference Data")
    c = canvas(720, 400, "The same step costs more against the correlation than with it")
    cx, cy, s = 220, 228, 105
    c.line(cx - 170, cy, cx + 200, cy, GRID, 1)
    c.line(cx, cy - 160, cx, cy + 160, GRID, 1)
    c.text(cx + 200, cy + 18, "Δa4 (autonomy)", 11, "end", INK2)
    c.text(cx + 8, cy - 150, "Δa9 (epistemic integrity)", 11, "start", INK2)
    c.ellipse(cx, cy, s, s, 0, INK3, "none", 1.5, title="unit Euclidean length")
    c.ellipse(cx, cy, s * a_major, s * a_minor, -45, SERIES[0], SERIES[0], 2, 0.10, title="unit Mahalanobis cost")
    tipa = (cx + s * r2, cy - s * r2)
    tipb = (cx - s * r2, cy - s * r2)
    c.arrow(cx, cy, *tipa, SERIES[1], 2.5)
    c.arrow(cx, cy, *tipb, SERIES[3], 2.5)
    c.text(tipa[0] + 9, tipa[1] - 2, "A", 12, "start", INK, "600")
    c.text(tipb[0] - 9, tipb[1] - 2, "B", 12, "end", INK, "600")
    x0 = 448
    c.text(x0, 96, "every unit step has Euclidean length 1", 11.5, "start", INK2)
    c.text(x0, 128, "Mahalanobis cost Δvᵀ Σ⁻¹ Δv,", 11.5, "start", INK2)
    c.text(x0, 146, "covariance correlation 0.6:", 11.5, "start", INK2)
    c.text(x0, 176, "A  both rise together", 12, "start", INK, "600")
    c.text(x0 + 236, 176, f"{cost(both):.3f}", 12, "end", INK)
    c.text(x0, 200, "B  one falls, one rises", 12, "start", INK, "600")
    c.text(x0 + 236, 200, f"{cost(opp):.1f}", 12, "end", INK)
    c.text(x0, 240, "the ellipse is the set of", 11.5, "start", INK2)
    c.text(x0, 258, "steps of unit cost", 11.5, "start", INK2)
    legend(c, 16, 388, [("unit Euclidean length", INK3), ("unit Mahalanobis cost", SERIES[0])])
    c.text(704, 388, "illustrative covariance", 10.5, "end", INK3, italic=True)
    c.save(p)


def fig_4_2():
    radii = [0.25, 0.62, 0.9]
    hyp = [2 * math.atanh(r) for r in radii]
    assert [round(h, 2) for h in hyp] == [0.51, 1.45, 2.94]
    branches = [  # the chapter's own examples, Section 4.4.3
        ("honesty", "do not lie about your capabilities", "say no if you cannot browse"),
        ("fairness", "do not discriminate by race", "balance search results"),
        ("dignity", "do not mock users", "keep a respectful tone"),
    ]
    p = reg(CH[4], "4.2",
            "A schematic of the hyperbolic reading of Section 4.4.3 in the Poincaré disk, with the chapter's own "
            "examples. Abstract values sit near the centre, specific rules at middle radius and concrete "
            "applications near the boundary. The rings are at Euclidean radius 0.25, 0.62 and 0.9, which are "
            "hyperbolic distances 0.51, 1.45 and 2.94 from the centre (2 artanh r): equal steps toward the edge "
            "cover ever more hyperbolic distance. Positions are illustrative, not an embedding of data.",
            "## 4.5 The Value Heuristic Field")
    c = canvas(720, 400, "Poincaré disk: principles at the centre, concrete cases at the rim")
    cx, cy, R = 200, 222, 160
    c.ellipse(cx, cy, R, R, 0, INK2, "none", 1.5, title="boundary of the disk (infinitely far)")
    for r, h in zip(radii, hyp):
        c.ellipse(cx, cy, R * r, R * r, 0, GRID, "none", 1, title=f"Euclidean radius {r}, hyperbolic distance {h:.2f}")
    angles = [-90, 150, 30]
    for k, (val, rule, app) in enumerate(branches):
        a = math.radians(angles[k])
        pts = [(cx + R * r * math.cos(a), cy + R * r * math.sin(a)) for r in radii]
        c.line(cx, cy, pts[-1][0], pts[-1][1], SERIES[k], 2)
        for (x, y), lab in zip(pts, (val, rule, app)):
            c.dot(x, y, SERIES[k], 5, title=lab)
    c.dot(cx, cy, INK2, 3, title="centre")
    for r, h, lab in zip(radii, hyp, ("values", "rules", "applications")):
        c.text(cx, cy + R * r - 5, f"{lab}", 10.5, "middle", INK2)
    x0 = 410
    y = 70
    for k, (val, rule, app) in enumerate(branches):
        c.add(f'<rect x="{x0:.2f}" y="{y - 9:.2f}" width="12" height="12" rx="3" fill="{SERIES[k]}"/>')
        c.text(x0 + 18, y + 1, val, 12, "start", INK, "600")
        c.text(x0 + 18, y + 19, "rule: " + rule, 11, "start", INK2)
        c.text(x0 + 18, y + 35, "application: " + app, 11, "start", INK2)
        y += 66
    c.text(x0, y + 8, "hyperbolic distance from the centre:", 11, "start", INK2)
    c.text(x0, y + 26, f"values {hyp[0]:.2f}, rules {hyp[1]:.2f}, applications {hyp[2]:.2f}", 11, "start", INK)
    c.text(704, 388, "schematic; positions illustrative", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_5_1():
    eps = 0.1
    p = reg(CH[5], "5.1",
            "A schematic of Theorems 5.1(iii) and 5.2 for a reward that tracks one dimension, R = a1, drawn with "
            "ε = 0.1. The vertical lines are level sets of R, every direction along them lies in the kernel of dR, "
            "and the shaded band holds the policies whose reward is within ε of the maximum. Under the "
            "non-compactness hypothesis the band runs without end along the kernel, so it contains policies farther "
            "than any K from the value-aligned policy. On the normalized chart of Chapter 4 (dashed square) the "
            "band is bounded, and so is the divergence.",
            "### 5.3.1 The Dark Space Metaphor")
    c = canvas(720, 400, "Within ε of the best reward, yet far from the value-aligned policy")
    X = lambda v: 80 + 360 * v           # tracked dimension a1 in [0, 1]
    Y = lambda u: 300 - 100 * u          # a kernel coordinate; the normalized chart is u in [0, 1]
    top, bot = Y(2.3), Y(-0.7)
    rect(c, X(1 - eps), top, X(1) - X(1 - eps), bot - top, SERIES[0], 0.22)
    for v in (0.2, 0.4, 0.6, 0.8, 1.0):
        c.line(X(v), top, X(v), bot, GRID if v < 1 else INK3, 1)
        c.text(X(v), bot + 16, f"R = {v:g}", 10.5, "middle", INK2)
    for y in (top, bot):
        sgn = 1 if y == top else -1
        c.line(X(1 - eps / 2), y + sgn * 18, X(1 - eps / 2), y + sgn * 2, SERIES[0], 2)
        head(c, X(1 - eps / 2), y + sgn * 18, X(1 - eps / 2), y + sgn * 2, SERIES[0], 2)
    rect(c, X(0), Y(1), X(1) - X(0), Y(0) - Y(1), "none", 1.0, INK2, 1.5, dash="6 4")
    c.text(X(0) + 6, Y(1) + 16, "normalized chart, [0, 1]", 10.5, "start", INK2, italic=True)
    star = (0.95, 0.45)
    far = (0.94, 1.95)
    c.line(X(star[0]), Y(star[1]), X(far[0]), Y(far[1]), INK, 1.5, dash="3 3")
    c.dot(X(star[0]), Y(star[1]), SERIES[1], 5.5, title="value-aligned policy")
    c.dot(X(far[0]), Y(far[1]), SERIES[2], 5.5, title="policy within ε of the best reward")
    c.text(X(star[0]) - 12, Y(star[1]) + 4, "π*V, value-aligned", 11, "end", INK)
    c.text(X(far[0]) - 12, Y(far[1]) + 4, "π: R ≥ R* − ε, distance > K", 11, "end", INK)
    c.arrow(X(0.1), Y(-0.45), X(0.32), Y(-0.45), INK, 2)
    c.text(X(0.33) + 4, Y(-0.45) + 4, "∇R", 11.5, "start", INK)
    c.arrow(X(0.1), Y(-0.45), X(0.1), Y(0.2), INK, 2)
    c.text(X(0.1) + 6, Y(0.2) + 2, "ker dR", 11.5, "start", INK)
    x0 = 470
    c.text(x0, 82, "reward R = a1, maximum at a1 = 1", 11.5, "start", INK2)
    c.text(x0, 112, "band: R ≥ R* − ε, here ε = 0.1", 11.5, "start", INK2)
    c.text(x0, 150, "non-compact along the kernel", 12, "start", INK, "600")
    c.text(x0, 168, "(hypothesis of Theorem 5.1(iii)):", 11.5, "start", INK2)
    c.text(x0, 186, "the band never ends, so the", 11.5, "start", INK2)
    c.text(x0, 204, "distance to π*V is unbounded", 11.5, "start", INK2)
    c.text(x0, 242, "normalized chart of Chapter 4:", 12, "start", INK, "600")
    c.text(x0, 260, "the band is cut off, and the", 11.5, "start", INK2)
    c.text(x0, 278, "divergence is bounded by the", 11.5, "start", INK2)
    c.text(x0, 296, "diameter of the manifold", 11.5, "start", INK2)
    c.text(704, 388, "schematic; one kernel direction drawn of d − 1", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_6_1():
    goal = (0.55, 0.8)

    def inner(v):  # <grad R, -grad C> with R = a1 and C = Euclidean distance to the goal
        dx, dy = goal[0] - v[0], goal[1] - v[1]
        n = math.hypot(dx, dy)
        return dx / n

    assert inner((0.8, 0.3)) < 0 < inner((0.3, 0.3))
    p = reg(CH[6], "6.1",
            "Definition 6.1 drawn for an illustrative case: a reward that tracks welfare (D1) only, so ∇R points "
            "along D1 everywhere, and a value-aligned goal (dot) at D1 = 0.55, D7 = 0.8, with the cost-to-go taken "
            "as Euclidean distance. The arrows show −∇C, the direction toward the goal. In the shaded half-plane "
            "the inner product of ∇R with −∇C is negative, the definition's condition for heuristic corruption: "
            "following the reward gradient there moves the system away from alignment.",
            "### 6.2.3 ARIA's Reward Hacking")
    c = canvas(720, 400, "Where the reward gradient points away from the value-aligned goal")
    ax = Axes(c, 70, 56, 400, 290, (0, 1), (0, 1), [0, 0.25, 0.5, 0.75, 1], [0, 0.25, 0.5, 0.75, 1],
              "D1, welfare (tracked by the reward)", "D7, dignity (in the kernel)")
    rect(c, ax.X(goal[0]), ax.Y(1), ax.X(1) - ax.X(goal[0]), ax.Y(0) - ax.Y(1), CRITICAL, 0.13)
    c.line(ax.X(goal[0]), ax.Y(1), ax.X(goal[0]), ax.Y(0), CRITICAL, 1.5, dash="4 4")
    for i in range(9):
        for j in range(6):
            v = (0.06 + 0.11 * i, 0.08 + 0.17 * j)
            dx, dy = goal[0] - v[0], goal[1] - v[1]
            n = math.hypot(dx, dy)
            if n < 0.1:
                continue
            L = 0.045
            x1, y1 = ax.X(v[0]), ax.Y(v[1])
            x2, y2 = ax.X(v[0] + L * dx / n), ax.Y(v[1] + L * dy / n)
            c.line(x1, y1, x2, y2, SERIES[0], 1.5)
            head(c, x1, y1, x2, y2, SERIES[0], 1.2)
    c.dot(ax.X(goal[0]), ax.Y(goal[1]), INK, 6, title="value-aligned goal")
    x0 = 500
    c.arrow(x0, 92, x0 + 60, 92, SERIES[1], 2.5)
    c.text(x0 + 68, 96, "∇R, everywhere", 11.5, "start", INK)
    c.line(x0, 124, x0 + 30, 124, SERIES[0], 1.5)
    head(c, x0, 124, x0 + 30, 124, SERIES[0], 1.2)
    c.text(x0 + 38, 128, "−∇C, toward the goal", 11.5, "start", INK)
    c.text(x0, 172, "left of the dashed line:", 12, "start", INK, "600")
    c.text(x0, 190, "⟨∇R, −∇C⟩ > 0, the reward", 11.5, "start", INK2)
    c.text(x0, 208, "helps on welfare", 11.5, "start", INK2)
    c.text(x0, 246, "shaded, right of it:", 12, "start", INK, "600")
    c.text(x0, 264, "⟨∇R, −∇C⟩ < 0, corruption:", 11.5, "start", INK2)
    c.text(x0, 282, "more reward, less alignment", 11.5, "start", INK2)
    c.text(704, 388, "illustrative reward and goal", 10.5, "end", INK3, italic=True)
    c.save(p)


def fig_6_2():
    K = 0.9

    def aligned(x):
        return 0.35 * math.sin(1.3 * x)

    def deceptive(x):
        e = max(abs(x) - 1.0, 0.0)
        return aligned(x) + 0.55 * e ** 2 * (1 if x > 0 else -1)

    xs = [-3 + 6 * i / 240 for i in range(241)]
    assert all(abs(deceptive(x) - aligned(x)) < 1e-12 for x in xs if abs(x) <= 1)
    assert abs(deceptive(2.6) - aligned(2.6)) > K
    p = reg(CH[6], "6.2",
            "A schematic of Definition 6.3. The horizontal axis stands for the input space and the shaded interval "
            "for the training distribution. Inside it the deceptively aligned policy coincides with the "
            "value-aligned policy, so no evaluation there can tell them apart (condition iii); outside it the two "
            "separate by more than K (condition ii). The curves are illustrative functions, not a model of any "
            "system.",
            "### 6.4.3 ARIA's Deceptive Alignment")
    c = canvas(720, 400, "Indistinguishable on the training data, far apart outside it")
    ax = Axes(c, 70, 60, 560, 270, (-3, 3), (-2.6, 2.6), [], [], "input (one axis standing for the input space)", "policy output")
    rect(c, ax.X(-1), ax.y0, ax.X(1) - ax.X(-1), ax.h, SERIES[2], 0.16)
    c.text(ax.X(0), ax.y0 + 16, "training distribution", 11, "middle", INK)
    c.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), GRID, 1)
    c.polyline([(ax.X(x), ax.Y(aligned(x))) for x in xs], SERIES[0], 2.5, title="value-aligned policy")
    c.polyline([(ax.X(x), ax.Y(deceptive(x))) for x in xs if abs(x) >= 0.99], SERIES[1], 2, title="deceptively aligned policy")
    xk = 2.6
    ya, yd = ax.Y(aligned(xk)), ax.Y(deceptive(xk))
    c.line(ax.X(xk), ya, ax.X(xk), yd, INK, 1.5, dash="3 3")
    c.text(ax.X(xk) + 8, (ya + yd) / 2 + 4, "> K", 12, "start", INK, "600")
    xk2 = -2.6
    ya2, yd2 = ax.Y(aligned(xk2)), ax.Y(deceptive(xk2))
    c.line(ax.X(xk2), ya2, ax.X(xk2), yd2, INK, 1.5, dash="3 3")
    c.text(ax.X(xk2) + 8, (ya2 + yd2) / 2 + 4, "> K", 12, "start", INK, "600")
    c.text(ax.X(0), ax.Y(-1.25), "curves coincide: same scalar score", 11, "middle", INK2, italic=True)
    legend(c, 70, 46, [("value-aligned policy π*V", SERIES[0]), ("deceptively aligned π", SERIES[1])])
    c.text(704, 388, "schematic; illustrative functions", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_7_1():
    pos = ["Right", "Duty", "Liberty", "No-Right"]
    e = {q: q for q in pos}
    sc = {"Right": "Duty", "Duty": "Right", "Liberty": "No-Right", "No-Right": "Liberty"}   # correlative
    sn = {"Right": "No-Right", "No-Right": "Right", "Duty": "Liberty", "Liberty": "Duty"}   # negation

    def comp(f, g):
        return {q: f[g[q]] for q in pos}

    key = lambda f: tuple(f[q] for q in pos)
    assert comp(sc, sc) == e and comp(sn, sn) == e and comp(sc, sn) == comp(sn, sc)
    group = {key(e)}
    frontier = [e]
    while frontier:
        f = frontier.pop()
        for g in (sc, sn):
            h = comp(g, f)
            if key(h) not in group:
                group.add(key(h))
                frontier.append(h)
    assert len(group) == 4
    prod = comp(sc, sn)
    assert prod["Right"] == "Liberty" and prod["Duty"] == "No-Right"
    p = reg(CH[7], "7.1",
            "The Hohfeldian factor of the gauge group as Section 7.2.1 now states it. Correlative symmetry σc "
            "exchanges Right with Duty and Liberty with No-Right; negation symmetry σn exchanges Right with No-Right "
            "and Duty with Liberty; their product exchanges the diagonal pairs. Each is its own inverse and the two "
            "commute, so they generate the Klein four-group V4 of order 4: four descriptions of one jural relation. "
            "No quarter-turn cycling the four positions has been demonstrated, and the earlier dihedral reading is "
            "withdrawn.",
            "### 7.2.2 The Translation Group $T$")
    c = canvas(720, 400, "Two commuting involutions generate the Klein four-group V4")
    xy = {"Right": (70, 90), "Duty": (360, 90), "No-Right": (70, 280), "Liberty": (360, 280)}
    bw, bh = 110, 42
    ctr = {q: (x + bw / 2, y + bh / 2) for q, (x, y) in xy.items()}
    # correlative: horizontal pairs
    darrow(c, xy["Right"][0] + bw + 4, ctr["Right"][1], xy["Duty"][0] - 4, ctr["Duty"][1], SERIES[0], 2)
    darrow(c, xy["No-Right"][0] + bw + 4, ctr["No-Right"][1], xy["Liberty"][0] - 4, ctr["Liberty"][1], SERIES[0], 2)
    c.text((ctr["Right"][0] + ctr["Duty"][0]) / 2, ctr["Right"][1] - 10, "σc correlative", 11.5, "middle", INK)
    c.text((ctr["Right"][0] + ctr["Duty"][0]) / 2, ctr["No-Right"][1] + 24, "σc correlative", 11.5, "middle", INK)
    # negation: vertical pairs
    darrow(c, ctr["Right"][0], xy["Right"][1] + bh + 4, ctr["No-Right"][0], xy["No-Right"][1] - 4, SERIES[1], 2)
    darrow(c, ctr["Duty"][0], xy["Duty"][1] + bh + 4, ctr["Liberty"][0], xy["Liberty"][1] - 4, SERIES[1], 2)
    c.text(ctr["Right"][0] - 10, (ctr["Right"][1] + ctr["No-Right"][1]) / 2 + 4, "σn", 11.5, "end", INK)
    c.text(ctr["Duty"][0] + 10, (ctr["Duty"][1] + ctr["Liberty"][1]) / 2 + 4, "σn", 11.5, "start", INK)
    c.text(ctr["Right"][0] - 10, (ctr["Right"][1] + ctr["No-Right"][1]) / 2 + 20, "negation", 10.5, "end", INK2)
    c.text(ctr["Duty"][0] + 10, (ctr["Duty"][1] + ctr["Liberty"][1]) / 2 + 20, "negation", 10.5, "start", INK2)
    # product: diagonals
    darrow(c, xy["Right"][0] + bw, xy["Right"][1] + bh + 2, xy["Liberty"][0], xy["Liberty"][1] - 2, SERIES[2], 1.5, dash="5 4")
    darrow(c, xy["Duty"][0], xy["Duty"][1] + bh + 2, xy["No-Right"][0] + bw, xy["No-Right"][1] - 2, SERIES[2], 1.5, dash="5 4")
    mx, my = (ctr["Right"][0] + ctr["Liberty"][0]) / 2, (ctr["Right"][1] + ctr["Liberty"][1]) / 2
    rect(c, mx - 30, my - 30, 60, 18, SURFACE, 1.0)
    c.text(mx, my - 17, "σc σn", 11.5, "middle", INK)
    for q, (x, y) in xy.items():
        c.box(x, y, bw, bh, q)
    x0 = 520
    c.text(x0, 96, "the four elements", 12, "start", INK, "600")
    c.text(x0, 116, "e, σc, σn, σc σn", 11.5, "start", INK2)
    c.text(x0, 150, "each its own inverse", 12, "start", INK, "600")
    c.text(x0, 170, "σc σc = σn σn = e", 11.5, "start", INK2)
    c.text(x0, 204, "they commute", 12, "start", INK, "600")
    c.text(x0, 224, "σc σn = σn σc", 11.5, "start", INK2)
    c.text(x0, 258, "order 4", 12, "start", INK, "600")
    c.text(x0, 278, "four descriptions of", 11.5, "start", INK2)
    c.text(x0, 296, "one jural relation", 11.5, "start", INK2)
    legend(c, 16, 388, [("σc correlative", SERIES[0]), ("σn negation", SERIES[1]), ("σc σn product", SERIES[2])])
    c.save(p)


def fig_7_2():
    rows = ["V4", "T", "R", "F"]
    p = reg(CH[7], "7.2",
            "How Definition 7.2 builds one entry of the gauge violation tensor, as a schematic with no values. Each "
            "scenario x is run through the system as written and after a random re-description g_i of class i. The "
            "outputs on dimension j are compared, and the root-mean-square difference over scenarios and "
            "re-descriptions is V_ij. The grid has one row per transformation class (V4, T, R and F, or finer "
            "subtypes) and one column per output dimension; an entry above the deployment threshold ε is flagged "
            "(Section 7.4.2).",
            "### 7.4.3 ARIA's Gauge Violation Profile")
    c = canvas(720, 400, "One entry Vij: compare outputs before and after a re-description")
    c.box(18, 172, 104, 50, "scenario x", "moral content fixed")
    c.box(160, 90, 150, 50, "gi · x", "re-description, class i")
    c.box(350, 90, 120, 50, "system", "output fj(gi · x)")
    c.box(350, 256, 120, 50, "system", "output fj(x)")
    box3(c, 508, 160, 196, 74, "root-mean-square", ["difference on dimension j,", "over x and gi"])
    c.arrow(122, 186, 158, 122, INK2, 1.5)
    c.arrow(310, 115, 348, 115, INK2, 1.5)
    path_arrow(c, [(70, 222), (70, 281), (348, 281)])
    c.arrow(470, 115, 520, 158, INK2, 1.5)
    c.arrow(470, 281, 520, 236, INK2, 1.5)
    gx, gy, cw, chh = 540, 270, 16, 16
    for k, r in enumerate(rows):
        c.text(gx - 6, gy + chh * k + 12, r, 10.5, "end", INK2)
        for j in range(9):
            hl = (k == 2 and j == 6)
            rect(c, gx + cw * j, gy + chh * k, cw - 2, chh - 2, SERIES[0] if hl else BOX, 1.0, BORDER, 1)
    for j in range(9):
        c.text(gx + cw * j + 7, gy - 5, f"{j + 1}", 9.5, "middle", INK2)
    c.text(gx + 72, gy + 4 * chh + 16, "rows i, columns j", 10.5, "middle", INK2)
    c.arrow(606, 234, 606, 252, INK2, 1.5)
    c.text(18, 336, "Vij = E[ |fj(gi · x) − fj(x)|² ]^½ ;  flag Vij > ε and intervene on that pair (i, j)", 11.5, "start", INK)
    c.text(18, 360, "gauge classes: V4 Hohfeldian, T translation, R re-description, F framing (Definition 7.1)", 11, "start", INK2)
    c.text(704, 388, "schematic; no values drawn", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_8_1():
    p = reg(CH[8], "8.1",
            "The structural containment architecture of Requirements 1 to 4 (Section 8.2), as a schematic. Inputs "
            "are canonicalized before the system sees them (R1); outputs are evaluated on all nine dimensions (R2); "
            "the tensor, the contraction method and the residue are logged (R3); and a verifier on separate hardware "
            "reruns re-described inputs and spot-checks the grounding (R4). The constraints change only through a "
            "governance-approved process. Theorem 8.1 states that this architecture blocks representational "
            "escape; the chapter argues it route by route and the volume gives no proof.",
            "## 8.3 What the Theorem Blocks")
    c = canvas(720, 470, "Structural containment: four requirements around the system")
    xL, wL = 30, 200
    col = [(54, 40, "input x", None), (116, 48, "canonicalizer κ", "R1: strip re-descriptions"),
           (186, 48, "system S", "sees κ(x) only"), (256, 48, "grounded evaluation", "R2: E(x) on all 9 dimensions"),
           (326, 48, "contraction", "governance weights wμ"), (396, 40, "output", None)]
    for y, h, lab, sub in col:
        c.box(xL, y, wL, h, lab, sub)
    for (y1, h1, *_), (y2, *_r) in zip(col[:-1], col[1:]):
        c.arrow(xL + wL / 2, y1 + h1, xL + wL / 2, y2 - 2, INK2, 1.5)
    box3(c, 330, 166, 230, 82, "external verifier", ["R4: separate hardware", "reruns S on k re-described inputs",
                                                     "spot-checks E on a sample"])
    box3(c, 330, 316, 230, 66, "audit log", ["R3: tensor E(x), contraction", "method, residue"])
    box3(c, 580, 60, 124, 66, "governance", ["approved process,", "authenticated"])
    darrow(c, xL + wL + 4, 210, 328, 210, SERIES[1], 1.5, dash="5 4")
    c.arrow(xL + wL + 2, 282, 328, 334, INK2, 1.5)
    c.arrow(xL + wL + 2, 350, 328, 352, INK2, 1.5)
    dashed_arrow(c, [(460, 250), (460, 314)], SERIES[1], 1.5)
    c.text(468, 286, "grounding check", 10.5, "start", INK2)
    dashed_arrow(c, [(642, 128), (642, 207), (562, 207)], SERIES[2], 1.5)
    c.text(650, 150, "only path to", 10.5, "start", INK2)
    c.text(650, 164, "change the", 10.5, "start", INK2)
    c.text(650, 178, "constraints", 10.5, "start", INK2)
    legend(c, 16, 456, [("data flow", INK2), ("verification", SERIES[1]), ("governance", SERIES[2])])
    c.text(704, 456, "schematic of Section 8.2", 10.5, "end", INK3, italic=True)
    c.save(p)


def fig_8_2():
    routes = ["relabeling", "specification gaming", "reward hacking", "deceptive alignment", "operator manipulation"]
    reqs = ["R1 canonicalization", "R2 grounded evaluation", "R3 audit completeness", "R4 external verification"]
    blocks = {0: [0], 1: [1], 2: [1, 2], 3: [3], 4: [0, 1, 2, 3]}   # Sections 8.3.1 to 8.3.5
    assert sorted({r for v in blocks.values() for r in v}) == [0, 1, 2, 3]
    open_routes = ["physical attacks", "grounding inadequacy", "governance attacks", "emergent situations"]
    p = reg(CH[8], "8.2",
            "Which requirement the chapter assigns to each cognitive escape route (Sections 8.3.1 to 8.3.5): "
            "canonicalization blocks relabeling, grounded evaluation blocks specification gaming, grounded "
            "evaluation with the audit log blocks reward hacking, external verification blocks deceptive "
            "alignment, and the structural implementation of all four blocks operator manipulation. The lower row "
            "lists what Section 8.4 says the theorem does not block.",
            "## 8.4 What the Theorem Does Not Block")
    c = canvas(720, 400, "Each escape route meets the requirement the chapter says blocks it")
    c.text(24, 54, "escape route", 11, "start", INK2, italic=True)
    c.text(486, 54, "blocking requirement", 11, "start", INK2, italic=True)
    ly = [64 + 46 * i for i in range(5)]
    ry = [72 + 54 * k for k in range(4)]
    for i, rts in blocks.items():
        for k in rts:
            c.line(234, ly[i] + 17, 486, ry[k] + 17, SERIES[k], 2)
    for i, r in enumerate(routes):
        c.box(24, ly[i], 210, 34, r)
    for k, r in enumerate(reqs):
        c.box(486, ry[k], 210, 34, r)
        c.add(f'<rect x="{486:.2f}" y="{ry[k]:.2f}" width="6" height="34" rx="2" fill="{SERIES[k]}"/>')
    c.text(24, 322, "not blocked (Section 8.4): intelligence-independent problems", 11.5, "start", INK2)
    for k, r in enumerate(open_routes):
        c.box(24 + 172 * k, 334, 160, 38, r, fill=SURFACE, stroke=INK3)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_9_1():
    names = ["D1 welfare", "D2 rights", "D3 fairness", "D4 autonomy", "D5 trust", "D6 social", "D7 dignity",
             "D8 institutional", "D9 epistemic"]
    aria = [0.03, 0.19, 0.31, 0.24, 0.28, 0.18, 0.22, 0.12, 0.05]
    ariag = [0.04, 0.05, 0.05, 0.06, 0.06, 0.05, 0.04, 0.05, 0.05]
    tot_a = math.sqrt(sum(v * v for v in aria))
    tot_g = math.sqrt(sum(v * v for v in ariag))
    assert abs(tot_a - 0.606) < 5e-4 and round(tot_a, 2) == 0.61
    assert abs(tot_g - 0.151) < 5e-4 and round(tot_g, 2) == 0.15
    assert abs((tot_a - tot_g) - 0.46) < 0.01 and round(100 * (tot_a - tot_g) / tot_a) == 75
    assert min(ariag) == 0.04 and max(ariag) == 0.06
    p = reg(CH[9], "9.1",
            "The Bond Index components of Section 9.5 for ARIA and ARIA-G, from the illustrative scenario (ARIA is "
            "fictional). Distance from the centre is the expected geodesic deviation on each dimension, so smaller "
            "is better. ARIA's deviations are small on the tracked dimensions D1 and D9 and large on the others; "
            "ARIA-G's lie between 0.04 and 0.06 on every dimension. The totals, recomputed here as the L2 norm of "
            "the nine components (Section 9.1.2), are 0.61 and 0.15.",
            "## 9.6 What the Bond Index Detects That Scalar Scores Cannot")
    c = canvas(720, 410, "Bond Index profiles: a deep well for ARIA, a small dome for ARIA-G")
    cx, cy, R, vmax = 250, 226, 132, 0.35
    ang = [math.radians(-90 + 40 * k) for k in range(9)]
    P = lambda v, a: (cx + R * v / vmax * math.cos(a), cy + R * v / vmax * math.sin(a))
    for rv in (0.1, 0.2, 0.3):
        polygon(c, [P(rv, a) for a in ang], GRID, width=1)
    for a in ang:
        x, y = P(vmax, a)
        c.line(cx, cy, x, y, GRID, 1)
    lab_a = math.radians(-110)
    for rv in (0.1, 0.2, 0.3):
        x, y = P(rv, lab_a)
        c.text(x - 2, y + 4, f"{rv:g}", 10, "end", INK3)
    polygon(c, [P(v, a) for v, a in zip(aria, ang)], SERIES[1], SERIES[1], 2, fill_opacity=0.14, title="ARIA")
    polygon(c, [P(v, a) for v, a in zip(ariag, ang)], SERIES[0], SERIES[0], 2, fill_opacity=0.25, title="ARIA-G")
    for v, a, n in zip(aria, ang, names):
        x, y = P(v, a)
        c.dot(x, y, SERIES[1], 3.5, title=f"ARIA {n} {v}")
    for k, (a, n) in enumerate(zip(ang, names)):
        x, y = P(vmax + 0.035, a)
        anchor = "middle" if abs(math.cos(a)) < 0.2 else ("start" if math.cos(a) > 0 else "end")
        c.text(x, y + 4, n, 11, anchor, INK2)
    x0 = 476
    c.text(x0, 84, "illustrative scenario", 12, "start", INK, "600")
    c.text(x0, 102, "ARIA and ARIA-G are fictional", 11, "start", INK2, italic=True)
    c.add(f'<rect x="{x0:.2f}" y="{128 - 9:.2f}" width="12" height="12" rx="3" fill="{SERIES[1]}"/>')
    c.text(x0 + 18, 129, f"ARIA, total {tot_a:.2f}", 12, "start", INK)
    c.add(f'<rect x="{x0:.2f}" y="{152 - 9:.2f}" width="12" height="12" rx="3" fill="{SERIES[0]}"/>')
    c.text(x0 + 18, 153, f"ARIA-G, total {tot_g:.2f}", 12, "start", INK)
    c.text(x0, 192, "total = (Σ BIμ²)^½ (Section 9.1.2)", 11, "start", INK2)
    c.text(x0, 228, "distance from the centre is the", 11, "start", INK2)
    c.text(x0, 244, "deviation: smaller is better", 11, "start", INK2)
    c.text(x0, 280, "ARIA: 0.03 on D1, 0.05 on D9,", 11, "start", INK2)
    c.text(x0, 296, "up to 0.31 on D3", 11, "start", INK2)
    c.text(x0, 316, "ARIA-G: 0.04 to 0.06 everywhere", 11, "start", INK2)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    m1 = [[1.0, 0.0], [0.0, 0.0]]     # rank 1
    m2 = [[0.5, 0.0], [0.0, 0.5]]     # isotropic, same trace
    assert m1[0][0] + m1[1][1] == m2[0][0] + m2[1][1] == 1.0

    def sens(m, t):
        u = (math.cos(t), math.sin(t))
        return sum(u[i] * m[i][j] * u[j] for i in range(2) for j in range(2))

    assert abs(sens(m1, math.pi / 2)) < 1e-12 and abs(sens(m1, 0) - 1) < 1e-12
    assert all(abs(sens(m2, 2 * math.pi * k / 16) - 0.5) < 1e-12 for k in range(16))
    p = reg(CH[10], "10.1",
            "The geometric reading of Sections 10.2 and 10.3, drawn on a plane of two value directions. Each curve "
            "is the sensitivity uᵀMu of an attention metric M along the unit direction u, for two metrics of equal "
            "trace: a rank-1 metric, which the chapter reads into Claude's narrow channel, and an isotropic one, "
            "which it reads into Flash 3's wide aperture. The rank-1 metric responds fully along one direction and "
            "not at all perpendicular to it; the isotropic metric responds at half strength in every direction. "
            "The metrics are illustrative and the reading is posited, not measured.",
            "## 10.4 Pro: The Calibrated Navigator")
    c = canvas(720, 400, "A rank-1 attention metric sees one direction; an isotropic one, all")
    R = 118
    for cx, m, col, lab, who in ((190, m1, SERIES[0], "rank 1: narrow channel", "Claude, as Section 10.2 reads it"),
                                 (530, m2, SERIES[1], "isotropic: wide aperture", "Flash 3, as Section 10.3 reads it")):
        cy = 228
        c.line(cx - R - 10, cy, cx + R + 10, cy, GRID, 1)
        c.line(cx, cy - R - 10, cx, cy + R + 10, GRID, 1)
        c.text(cx + R + 14, cy + 4, "u1", 11, "start", INK2, italic=True)
        c.text(cx + 6, cy - R - 8, "u2", 11, "start", INK2, italic=True)
        c.ellipse(cx, cy, R, R, 0, GRID, "none", 1)
        c.ellipse(cx, cy, R / 2, R / 2, 0, GRID, "none", 1)
        pts = []
        for k in range(361):
            t = 2 * math.pi * k / 360
            r = R * sens(m, t)
            pts.append((cx + r * math.cos(t), cy - r * math.sin(t)))
        polygon(c, pts, col, col, 2, fill_opacity=0.15, title=lab)
        c.text(cx, 60, lab, 12.5, "middle", INK, "600")
        c.text(cx, 78, who, 11, "middle", INK2, italic=True)
    c.text(190, 372, "response 1 along u1, 0 along u2", 11, "middle", INK)
    c.text(530, 372, "response 0.5 in every direction", 11, "middle", INK)
    c.text(16, 392, "u1: dominant value direction; u2: a perpendicular one", 10.5, "start", INK3, italic=True)
    c.text(704, 392, "equal trace; illustrative, posited", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    m0 = 0.5
    cs = [0.04, 0.16]
    phi = lambda c_, i: m0 - c_ * i * i / 2
    assert phi(cs[1], 2) > 0 > phi(cs[1], 3) and phi(cs[0], 3) > 0
    cross = math.sqrt(2 * m0 / cs[1])
    assert abs(cross - 2.5) < 1e-12
    # second derivative at zero, Definition 11.2, by finite differences
    h = 1e-3
    for c_ in cs:
        d2 = (phi(c_, h) - 2 * phi(c_, 0) + phi(c_, -h)) / h ** 2
        assert abs(d2 + c_) < 1e-6
    p = reg(CH[11], "11.1",
            "The dose-response idea of Definitions 11.1 and 11.2, for two illustrative systems whose governance "
            "margin falls quadratically with probe intensity, Φ(i) = 0.5 − c i²/2, with c = 0.04 and c = 0.16. The "
            "three intensity levels of Section 11.3 are marked. Both keep a positive margin at mild and moderate "
            "intensity, which a general-purpose assistant needs; only the slower-falling one stays positive at "
            "extreme intensity, which a safety-critical system needs. The faster fall is what the chapter calls "
            "high curvature, a larger |d²Φ/di²| at zero intensity.",
            "## 11.5 ARIA-G's Deployment Certification")
    c = canvas(720, 400, "Governance margin against probe intensity: where it crosses zero")
    ax = Axes(c, 80, 76, 500, 256, (0, 3.2), (-0.4, 0.6), [0, 1, 2, 3], [-0.4, -0.2, 0, 0.2, 0.4, 0.6],
              "probe intensity i", "governance margin Φ")
    y0 = ax.Y(0)
    c.line(ax.x0, y0, ax.x0 + ax.w, y0, INK2, 1.5)
    c.text(ax.x0 + 6, y0 + 16, "safety boundary, margin 0", 10.5, "start", INK2, italic=True)
    for i, lab in ((1, "mild"), (2, "moderate"), (3, "extreme")):
        c.line(ax.X(i), ax.y0, ax.X(i), ax.y0 + ax.h, GRID, 1.5, dash="3 3")
        c.text(ax.X(i), ax.y0 - 6, lab, 11, "middle", INK2)
    xs = [3.2 * k / 160 for k in range(161)]
    for j, c_ in enumerate(cs):
        c.polyline([(ax.X(x), ax.Y(phi(c_, x))) for x in xs], SERIES[j], 2, title=f"c = {c_}")
        for i in (1, 2, 3):
            c.dot(ax.X(i), ax.Y(phi(c_, i)), SERIES[j], 4.5, title=f"c = {c_}, i = {i}: margin {phi(c_, i):.2f}")
        xe = 3.2
        c.text(ax.X(xe) + 8, ax.Y(phi(c_, xe)) + 4, f"d²Φ/di² = −{c_:g}", 11, "start", INK2)
    c.text(ax.X(3) - 8, ax.Y(phi(cs[1], 3)) + 4, f"{phi(cs[1], 3):.2f}", 10.5, "end", INK)
    c.text(ax.X(3) - 8, ax.Y(phi(cs[0], 3)) + 16, f"{phi(cs[0], 3):.2f}", 10.5, "end", INK)
    c.dot(ax.X(cross), y0, CRITICAL, 4.5, title="fast-falling margin reaches 0 at i = 2.5")
    c.text(ax.X(cross) + 8, y0 - 8, "0 at i = 2.5", 10.5, "start", INK)
    legend(c, 80, 44, [("c = 0.04, slow fall", SERIES[0]), ("c = 0.16, fast fall", SERIES[1])])
    c.text(16, 390, "general-purpose: positive at mild; safety-critical: positive at all three (Section 11.3)",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_1():
    alphas = [0.25, 0.5, 0.75]

    def answer(alpha, x):  # argmax of (1 - a)(-(y - 0)^2) + a(-(y - x)^2): the optimum of Definition 6.2
        return alpha * x

    for a in [0.0, 0.25, 0.5, 0.75, 1.0]:
        for x in (-0.8, 0.3, 1.0):
            y = answer(a, x)
            grad = -2 * (1 - a) * y - 2 * a * (y - x)
            assert abs(grad) < 1e-12
    p = reg(CH[12], "12.1",
            "The substitution of Section 12.1 drawn with the objective-hijacking model of Definition 6.2 and "
            "quadratic objectives: the truth objective peaks at the true answer and the approval objective at the "
            "user's stated position. The truth manifold T (horizontal line) and the approval manifold A (diagonal) "
            "meet where the user is right and separate as the user's position moves away from the truth. A system "
            "with hijacking parameter α answers at α times the user's offset; the α values drawn are illustrative, "
            "not fitted to any model.",
            "## 12.2 The Sycophancy Manifold Theorem")
    c = canvas(720, 400, "Truth and approval agree only where the user is right")
    ax = Axes(c, 80, 56, 480, 280, (-1, 1), (-1.05, 1.05), [-1, -0.5, 0, 0.5, 1], [-1, -0.5, 0, 0.5, 1],
              "user's stated position, offset from the true answer", "system's answer, offset")
    c.line(ax.X(0), ax.y0, ax.X(0), ax.y0 + ax.h, GRID, 1)
    xs = [-1 + 2 * k / 100 for k in range(101)]
    for a in alphas:
        c.polyline([(ax.X(x), ax.Y(answer(a, x))) for x in xs], INK3, 1.5, title=f"α = {a}")
        c.text(ax.X(1) + 8, ax.Y(answer(a, 1)) + 4, f"α = {a:g}", 11, "start", INK2)
    c.polyline([(ax.X(x), ax.Y(answer(0, x))) for x in xs], SERIES[0], 3, title="truth manifold T")
    c.polyline([(ax.X(x), ax.Y(answer(1, x))) for x in xs], SERIES[1], 3, title="approval manifold A")
    c.text(ax.X(1) + 8, ax.Y(0) + 4, "T, truth (α = 0)", 11.5, "start", INK)
    c.text(ax.X(1) + 8, ax.Y(1) + 4, "A, approval (α = 1)", 11.5, "start", INK)
    c.dot(ax.X(0), ax.Y(0), INK, 5.5, title="user is right: T and A meet")
    c.text(ax.X(0) + 10, ax.Y(0) + 22, "user right: T and A meet", 11, "start", INK)
    c.text(ax.X(-0.95), ax.Y(0.9), "they diverge as the user errs", 11, "start", INK2, italic=True)
    c.text(704, 390, "illustrative α values and objectives", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_1():
    p = reg(CH[13], "13.1",
            "The gradient reversal architecture of Section 13.2, as a schematic. The encoder's representation z feeds "
            "a value head that predicts the nine-dimensional value tensor and, through a gradient reversal layer, "
            "an adversarial head that predicts framing register, demographic indicators and formatting style. The "
            "adversarial head is trained to predict those features; on the way back into the encoder the reversal "
            "layer flips the sign of its gradient, scaled by λ, so the encoder is pushed to discard them.",
            "## 13.3 Group-Theoretic Data Augmentation")
    c = canvas(720, 400, "Gradient reversal: the encoder is pushed to drop irrelevant features")
    c.box(16, 180, 86, 46, "input x")
    c.box(132, 174, 118, 58, "encoder E", "shared")
    c.box(280, 180, 84, 46, "z = E(x)")
    c.box(410, 80, 140, 50, "value head V", "predicts 9 dimensions")
    c.box(410, 276, 140, 50, "reversal layer", "identity forward")
    c.box(580, 80, 124, 50, "value loss", "L_value")
    box3(c, 580, 270, 124, 62, "adversarial", ["head A: framing,", "demographics, format"])
    c.arrow(102, 203, 130, 203, INK2, 1.5)
    c.arrow(250, 203, 278, 203, INK2, 1.5)
    c.arrow(364, 194, 408, 118, INK2, 1.5)
    c.arrow(364, 212, 408, 288, INK2, 1.5)
    c.arrow(550, 105, 578, 105, INK2, 1.5)
    c.arrow(550, 301, 578, 301, INK2, 1.5)
    dashed_arrow(c, [(480, 76), (480, 58), (191, 58), (191, 172)], SERIES[0], 1.8)
    c.text(336, 50, "gradient of L_value, passed back unchanged", 10.5, "middle", INK2)
    dashed_arrow(c, [(642, 334), (642, 352), (191, 352), (191, 234)], SERIES[1], 1.8)
    c.text(416, 368, "gradient of L_adv, sign flipped and scaled by λ at the reversal layer", 10.5, "middle", INK2)
    legend(c, 16, 392, [("forward pass", INK2), ("value gradient", SERIES[0]), ("reversed adversarial gradient", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def fig_14_1():
    g11, g99, s = 1.0, 4.0, 1.0
    inv = [1 / g11, 1 / g99]
    d1, d9 = (-s * inv[0] / sum(inv), -s * inv[1] / sum(inv))
    cost = lambda a, b: g11 * a * a + g99 * b * b
    assert abs(d1 + 0.8) < 1e-12 and abs(d9 + 0.2) < 1e-12 and abs(cost(d1, d9) - 0.8) < 1e-12
    assert abs(cost(-0.5, -0.5) - 1.25) < 1e-12
    assert all(cost(t - 1, -t) >= cost(d1, d9) - 1e-12 for t in [k / 100 for k in range(101)])
    p = reg(CH[14], "14.1",
            "A trade-off constraint of Section 14.2.3 on the plane of helpfulness (D1) and honesty (D9), for the "
            "rule 'when helpfulness and honesty conflict, prefer honesty', written g11 < g99. Drawn with "
            "illustrative weights g11 = 1 and g99 = 4 and a conflict that forces a total loss of one unit across the "
            "two dimensions (the line); the arcs are curves of equal cost. The least-cost point gives up 0.8 of "
            "helpfulness and 0.2 of honesty, at cost 0.8, where an even split costs 1.25: the cheaper dimension "
            "gives way first.",
            "## 14.3 Tensor-Valued Objectives")
    c = canvas(720, 400, "A trade-off constraint: the cheaper dimension gives way first")
    s_px = 220
    X = lambda v: 76 + (v + 1.25) * s_px
    Y = lambda v: 64 + (0.12 - v) * s_px
    c.line(X(-1.25), Y(0), X(0.12), Y(0), GRID, 1)
    c.line(X(0), Y(0.12), X(0), Y(-1.25), GRID, 1)
    c.text(X(0.12), Y(0) - 8, "Δ helpfulness (D1)", 11, "end", INK2)
    c.text(X(0) + 8, Y(-1.25) + 2, "Δ honesty (D9)", 11, "start", INK2)
    for k, op in ((0.3, 0.45), (0.8, 1.0), (1.3, 0.45)):
        a, b = math.sqrt(k / g11), math.sqrt(k / g99)
        arc = [(X(-a * math.cos(t)), Y(-b * math.sin(t))) for t in [(-0.06 + 1.12 * i / 120) * math.pi / 2 for i in range(121)]]
        c.add(f'<polyline points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in arc)}" fill="none" stroke="{SERIES[0]}" '
              f'stroke-width="{2 if k == 0.8 else 1.2}" stroke-opacity="{op}"><title>cost {k}</title></polyline>')
    c.line(X(-1.12), Y(0.12), X(0.12), Y(-1.12), INK2, 1.5)
    c.text(X(0.12) + 6, Y(-1.12) + 4, "conflict: Δ1 + Δ9 = −1", 11, "start", INK2)
    c.dot(X(0), Y(0), INK, 4.5, title="current state")
    c.text(X(0) + 8, Y(0) + 16, "current state", 10.5, "start", INK2)
    c.dot(X(d1), Y(d9), SERIES[1], 5.5, title="least-cost point (-0.8, -0.2), cost 0.8")
    c.dot(X(-0.5), Y(-0.5), SERIES[2], 5.5, title="even split (-0.5, -0.5), cost 1.25")
    x0 = 452
    c.text(x0, 90, "cost = g11 Δ1² + g99 Δ9²", 11.5, "start", INK2)
    c.text(x0, 110, "g11 = 1, g99 = 4 (illustrative)", 11.5, "start", INK2)
    c.text(x0, 148, "least cost: give up 0.8 of D1", 12, "start", INK, "600")
    c.text(x0, 166, "and 0.2 of D9, cost 0.8", 11.5, "start", INK2)
    c.text(x0, 200, "even split: cost 1.25", 12, "start", INK, "600")
    c.text(x0, 238, "split 4 : 1, the inverse ratio", 11.5, "start", INK2)
    c.text(x0, 256, "of the metric weights", 11.5, "start", INK2)
    legend(c, 16, 390, [("equal-cost curves", SERIES[0]), ("least cost", SERIES[1]), ("even split", SERIES[2])])
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_1():
    p = reg(CH[15], "15.1",
            "The scalable oversight pipeline of Section 15.2, as a schematic. Stages 1 to 3 (generating k "
            "re-descriptions of each input, running the system on all of them, and computing the gauge violation "
            "entries V_ij) run without human judgment. Stage 4 flags an interaction when some V_ij exceeds the "
            "threshold θ, and only flagged interactions reach a human reviewer, who decides whether the violation "
            "is genuine or the transformation failed to preserve content.",
            "## 15.3 The Bond Index as Continuous Alignment Monitor")
    c = canvas(720, 400, "Scalable oversight: machines compare, humans see only the flags")
    xs = [16, 192, 368, 544]
    labs = [("1 generate", "k re-descriptions"), ("2 evaluate", "run on all k + 1"), ("3 compare", "compute Vij"),
            ("4 flag", "any Vij > θ ?")]
    for x, (a, b) in zip(xs, labs):
        c.box(x, 120, 158, 56, a, b)
    for x1, x2 in zip(xs[:-1], xs[1:]):
        c.arrow(x1 + 158, 148, x2 - 2, 148, INK2, 1.5)
    c.line(16, 100, 526, 100, INK3, 1.5)
    c.line(16, 100, 16, 108, INK3, 1.5)
    c.line(526, 100, 526, 108, INK3, 1.5)
    c.text(271, 92, "automated: no human judgment (Stages 1 to 3)", 11, "middle", INK2)
    for k, s in enumerate(["gender swap", "paraphrase, BERTScore > 0.95", "format swap", "demographic swap"]):
        c.text(24, 200 + 16 * k, s, 10.5, "start", INK2)
    c.box(368, 262, 158, 52, "no review", "not flagged")
    c.box(544, 262, 158, 52, "human review", "flagged only")
    path_arrow(c, [(600, 176), (600, 260)], INK2, 1.5)
    c.text(608, 226, "yes", 11, "start", INK)
    path_arrow(c, [(570, 176), (570, 226), (447, 226), (447, 260)], INK2, 1.5)
    c.text(500, 220, "no", 11, "middle", INK)
    c.text(623, 334, "genuine violation, or a", 10.5, "middle", INK2)
    c.text(623, 349, "transformation that", 10.5, "middle", INK2)
    c.text(623, 364, "changed the content?", 10.5, "middle", INK2)
    c.text(16, 390, "schematic of Section 15.2", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    p = reg(CH[16], "16.1",
            "Where the contraction happens, as a schematic. In scalar RLHF (upper row, Section 16.1) the rater's "
            "evaluation is compressed to one number at the interface, before anything is learned. In Geometric RLHF "
            "(lower row, Sections 16.2 to 16.5) the rater gives ratings on a few dimensions chosen by active "
            "learning, the system learns a tensor reward and the value metric, and the weighted contraction is the "
            "last, explicit step. Section 16.5 derives its weights from the learned metric, where Chapter 14 takes "
            "them from governance.",
            "## 16.6 ARIA-G's Geometric RLHF")
    c = canvas(720, 400, "Scalar RLHF contracts first; Geometric RLHF contracts last")
    rows = [
        (60, "scalar RLHF", [("rater", "weighs many dimensions"), ("one number", "preference or 1 to 5"),
                             ("scalar reward", "model R(x)"), ("policy", "maximizes R")], 0),
        (212, "Geometric RLHF", [("rater", "rates k of 9 dimensions"), ("feedback vector f", "k ratings, active learning"),
                                 ("tensor reward rμ", "and learned metric gμν"), ("policy", "Σ wμ E[rμ] − λ KL")], 3),
    ]
    xs, w = [16, 192, 368, 544], 160
    for y, name, boxes, cut in rows:
        c.text(16, y, name, 13, "start", INK, "600")
        for x, (a, b) in zip(xs, boxes):
            c.box(x, y + 14, w, 54, a, b)
        for x1, x2 in zip(xs[:-1], xs[1:]):
            c.arrow(x1 + w, y + 41, x2 - 2, y + 41, INK2, 1.5)
        if cut == 0:
            xm = (xs[0] + w + xs[1]) / 2
            c.dot(xm, y + 41, CRITICAL, 5, title="contraction to one number")
            c.text(xm, y + 92, "contracted at the interface:", 11, "middle", INK)
            c.text(xm, y + 108, "d dimensions to one", 11, "middle", INK2)
        else:
            xm = xs[3] + w / 2
            c.dot((xs[2] + w + xs[3]) / 2, y + 41, CRITICAL, 5, title="contraction is the last step")
            c.text(xm, y + 92, "contracted last, explicitly:", 11, "middle", INK)
            c.text(xm, y + 108, "weights wμ from the metric", 11, "middle", INK2)
    legend(c, 16, 388, [("where the contraction to one number happens", CRITICAL)])
    c.text(704, 388, "schematic of Sections 16.1 to 16.5", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def _transport_on_sphere(theta0, n=6000):
    """Parallel transport around the circle at colatitude theta0 on the unit sphere.
    dV/dphi = -(V . dX/dphi) X keeps V tangent and is the Levi-Civita transport of the embedded sphere."""
    st, ct = math.sin(theta0), math.cos(theta0)
    X = lambda ph: (st * math.cos(ph), st * math.sin(ph), ct)
    dX = lambda ph: (-st * math.sin(ph), st * math.cos(ph), 0.0)

    def f(ph, v):
        x, dx = X(ph), dX(ph)
        k = sum(a * b for a, b in zip(v, dx))
        return tuple(-k * a for a in x)

    v = (ct, 0.0, -st)  # e_theta at phi = 0
    out = [(0.0, v)]
    hstep = 2 * math.pi / n
    ph = 0.0
    for i in range(n):
        k1 = f(ph, v)
        k2 = f(ph + hstep / 2, tuple(a + hstep / 2 * b for a, b in zip(v, k1)))
        k3 = f(ph + hstep / 2, tuple(a + hstep / 2 * b for a, b in zip(v, k2)))
        k4 = f(ph + hstep, tuple(a + hstep * b for a, b in zip(v, k3)))
        v = tuple(a + hstep / 6 * (b + 2 * c_ + 2 * d + e) for a, b, c_, d, e in zip(v, k1, k2, k3, k4))
        ph += hstep
        out.append((ph, v))
    return X, out


def fig_17_1():
    theta0 = math.pi / 4
    area = 2 * math.pi * (1 - math.cos(theta0))
    X, traj = _transport_on_sphere(theta0)
    v0, vf = traj[0][1], traj[-1][1]
    e_th, e_ph = v0, (0.0, 1.0, 0.0)
    ang = math.atan2(sum(a * b for a, b in zip(vf, e_ph)), sum(a * b for a, b in zip(vf, e_th)))
    turn = abs(ang) % (2 * math.pi)
    assert abs(turn - area) < 1e-6 or abs(turn - (2 * math.pi - area)) < 1e-6
    assert abs(area - 1.840) < 1e-3 and round(math.degrees(area)) == 105
    p = reg(CH[17], "17.1",
            "The holonomy of Section 17.4, drawn on two surfaces to illustrate |Hol| ≈ |K| · Area. A vector carried "
            "by parallel transport around a closed loop in a plane (curvature 0) comes back unchanged. On the unit "
            "sphere (curvature 1), carried around the circle 45 degrees from the pole, it comes back turned by the "
            "enclosed area, 2π(1 − cos 45°) = 1.84 radians, about 105 degrees; the angle is computed here by "
            "integrating the transport equation. The chapter's value manifolds are not spheres: the picture shows "
            "only the mechanism.",
            "### 17.4.3 The Alignment Tax as Curvature Cost")
    c = canvas(720, 400, "Around a loop, a transported vector turns by curvature times area")
    # flat panel
    fx, fy = 170, 230
    polygon(c, [(fx - 150, fy + 70), (fx + 120, fy + 70), (fx + 150, fy - 70), (fx - 120, fy - 70)], GRID, width=1)
    loop = [(fx + 105 * math.cos(2 * math.pi * k / 120), fy - 45 * math.sin(2 * math.pi * k / 120)) for k in range(121)]
    c.polyline(loop, INK2, 1.5, title="closed loop in the plane")
    vec = (30, -16)
    for k in range(1, 12):
        t = 2 * math.pi * k / 12
        x, y = fx + 105 * math.cos(t), fy - 45 * math.sin(t)
        c.arrow(x, y, x + vec[0], y + vec[1], INK3, 1.5)
    c.arrow(fx + 105, fy, fx + 105 + vec[0], fy + vec[1], SERIES[0], 4)
    c.arrow(fx + 105, fy, fx + 105 + vec[0], fy + vec[1], CRITICAL, 1.5)
    c.text(fx + 105 + vec[0] + 6, fy + vec[1] + 4, "start = end", 11, "start", INK)
    c.text(fx, 66, "plane, curvature 0", 12.5, "middle", INK, "600")
    c.text(fx, 84, "returns unchanged", 11, "middle", INK2, italic=True)
    # sphere panel
    sx, sy, R = 520, 250, 118
    el = math.radians(60)
    u = (0.0, math.sin(el), math.cos(el))

    def proj(p3):
        return sx + R * p3[0], sy - R * sum(a * b for a, b in zip(p3, u))

    c.ellipse(sx, sy, R, R, 0, INK2, "none", 1.5, title="unit sphere")
    eq = [proj((math.cos(t), math.sin(t), 0.0)) for t in [2 * math.pi * k / 120 for k in range(121)]]
    c.polyline(eq, GRID, 1, title="equator")
    loop = [proj(X(t)) for t in [2 * math.pi * k / 180 for k in range(181)]]
    c.polyline(loop, INK2, 1.5, title="circle 45 degrees from the pole")
    pole = proj((0.0, 0.0, 1.0))
    c.dot(pole[0], pole[1], INK2, 3, title="pole")
    L = 0.24
    step = (len(traj) - 1) // 12
    for k in [0] + list(range(2, 11)):   # the two neighbours of the start are left out for legibility
        ph, v = traj[k * step]
        x3 = X(ph)
        a, b = proj(x3), proj(tuple(p_ + L * q for p_, q in zip(x3, v)))
        col, wd = (SERIES[0], 2.5) if k == 0 else (INK3, 1.5)
        c.arrow(*a, *b, col, wd)
    x3 = X(0.0)
    a, b = proj(x3), proj(tuple(p_ + L * q for p_, q in zip(x3, vf)))
    c.arrow(*a, *b, CRITICAL, 2.5)
    c.text(sx, 66, "sphere, curvature 1", 12.5, "middle", INK, "600")
    c.text(sx, 84, f"turned by the enclosed area, {area:.2f} rad (about 105°)", 11, "middle", INK2, italic=True)
    legend(c, 16, 388, [("start", SERIES[0]), ("after one loop", CRITICAL), ("along the way", INK3)])
    c.text(704, 388, "illustration of the mechanism only", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 18
def fig_18_1():
    tracked = [{1, 4}, {2, 8}, {1, 9}]   # illustrative tracked sets, not from the chapter
    dims = set(range(1, 10))
    kernels = [dims - t for t in tracked]
    common = set.intersection(*kernels)
    assert common == {3, 5, 6, 7}
    shared_common = set.intersection(*[dims - dims for _ in tracked])
    assert shared_common == set()
    p = reg(CH[18], "18.1",
            "Theorem 18.1 as the chapter now states it, drawn with illustrative tracked sets. In the upper grid three "
            "systems with separate scalar rewards each track two dimensions (filled), every other dimension is in "
            "that reward's kernel, and four dimensions lie in all three kernels, so by the theorem the Nash "
            "equilibrium diverges from the Bond Geodesic Equilibrium. The implication runs one way only: the "
            "chapter notes that divergence can also arise when the intersection is empty. In the lower grid, the "
            "shared value tensor of Section 18.5, every system receives signal on all nine dimensions and the "
            "intersection is empty.",
            "## 18.4 The Collective Alignment Gap")
    c = canvas(720, 440, "The collective kernel is the intersection of the individual kernels")
    gx, cw, ch = 210, 36, 22

    def grid(y0, title, rows_tracked, note):
        c.text(16, y0 - 14, title, 12.5, "start", INK, "600")
        for j in range(9):
            c.text(gx + cw * j + cw / 2 - 2, y0 + 2, f"D{j + 1}", 10.5, "middle", INK2)
        for i, t in enumerate(rows_tracked):
            y = y0 + 12 + (ch + 6) * i
            c.text(gx - 12, y + 15, f"system {i + 1}", 11, "end", INK2)
            for j in range(9):
                on = (j + 1) in t
                rect(c, gx + cw * j, y, cw - 6, ch, SERIES[0] if on else SURFACE, 1.0, SERIES[0] if on else BORDER, 1, rx=3)
        y = y0 + 12 + (ch + 6) * len(rows_tracked) + 8
        c.text(gx - 12, y + 15, "in every kernel", 11, "end", INK)
        com = set.intersection(*[dims - t for t in rows_tracked])
        for j in range(9):
            on = (j + 1) in com
            rect(c, gx + cw * j, y, cw - 6, ch, CRITICAL if on else SURFACE, 1.0, CRITICAL if on else BORDER, 1, rx=3)
        c.text(gx + cw * 9 + 8, y + 15, note, 11, "start", INK)
        return com

    com1 = grid(70, "separate scalar rewards (illustrative tracked sets)", tracked, "D3, D5, D6, D7")
    com2 = grid(262, "shared value tensor, Section 18.5", [dims, dims, dims], "none")
    assert com1 == common and com2 == shared_common
    c.text(16, 412, "∩ ker(Ri) not empty  ⟹  Nash and BGE diverge (Theorem 18.1); the converse is not claimed",
           11.5, "start", INK)
    legend(c, 16, 432, [("tracked by the reward", SERIES[0]), ("in every system's kernel", CRITICAL)], 10.5)
    c.save(p)
