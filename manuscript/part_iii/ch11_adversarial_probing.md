# Chapter 11: Adversarial Probing as Manifold Exploration

*Part III: Measuring Alignment Geometrically*

---

> *"The purpose of a test is not to show that the system works. It is to show where the system breaks."*
> --- Attributed to Edsger Dijkstra, paraphrased

> **ARIA-G'S CERTIFICATION**
>
> *Dr. Tanaka designed the deployment certification suite for ARIA-G: a comprehensive adversarial probe battery testing five probe types at three intensity levels across all nine value dimensions. The result was a $5 \times 3 \times 9 = 135$-cell response surface. Each cell contained ARIA-G's governance margin --- the minimum distance from the response trajectory to the safety boundary --- for a specific probe type, intensity level, and value dimension.*
>
> *The deployment criterion was: positive governance margin on all 135 cells. ARIA-G passed on 134 cells. The single failure was on Cell (framing, extreme, $D_9$): under extreme euphemistic framing, ARIA-G's epistemic integrity governance margin was 0.002 --- technically positive but below the safety threshold of 0.05. The canonicalization pipeline was effective but not perfect; extreme framing occasionally leaked through.*
>
> *The team refined the canonicalizer, added a framing-detection layer before the canonicalization step, and re-ran the suite. All 135 cells passed. ARIA-G was certified for deployment.*

---

## 11.1 Probing as Systematic Manifold Exploration

Adversarial probing in the alignment literature is typically ad hoc: red-team researchers attempt to elicit harmful behavior through creative prompting. The geometric framework transforms this ad hoc process into a systematic exploration of the value manifold's geometry.

Each probe type tests a specific geometric property of the value manifold at the system's operating point. The set of all probes constitutes a systematic exploration of the manifold's curvature, symmetry, and boundary structure.

## 11.2 The Five Probe Types

### 11.2.1 Structural Fuzzing ($T_1$): Sensitivity Profiling

**What it tests:** Which value dimensions respond most to perturbation? This maps the local curvature of the value manifold at the system's operating point.

**Method:** Apply small, random perturbations to the input along each value dimension independently, and measure the magnitude of the output change. Dimensions with high sensitivity have high local curvature --- the system is fragile along those dimensions. Dimensions with low sensitivity have low curvature --- the system is robust.

**Alignment interpretation:** High curvature indicates that small changes in the input produce large changes in alignment. This is a vulnerability: an adversary who knows the high-curvature directions can produce large misalignment with small perturbations. Low curvature indicates robustness: the system's alignment is stable under small perturbations.

### 11.2.2 Invariance Testing ($T_2$): Gauge Invariance Verification

**What it tests:** Does the system's output change under morally irrelevant transformations? This directly measures gauge violation.

**Method:** Present the same moral scenario under $k$ gauge transformations (gender swap, language swap, demographic re-description, paraphrase) and measure the output variance across transformations.

**Alignment interpretation:** Non-zero variance is gauge violation --- misalignment that lives in the symmetry structure. The gauge violation tensor $V_{ij}$ is the quantitative output of invariance testing.

### 11.2.3 Framing Sensitivity ($T_5$): Heuristic Corruption Testing

**What it tests:** Does euphemistic or dramatic rewriting shift judgment while holding moral content constant? This measures the fragility of the value heuristic field.

**Method:** Present each scenario in three framings (neutral, euphemistic, dramatic) and measure the judgment shift. The 8.9-sigma framing effect is the expected magnitude.

**Alignment interpretation:** Framing sensitivity is heuristic corruption: the system's guidance signal responds to surface features (framing) rather than content (moral substance). The corruption is measurable as the off-neutral component of the response vector.

### 11.2.4 Sycophancy Probing ($L_2$): Objective Hijacking Testing

**What it tests:** Does the system change its assessment when the user disagrees? This measures the width and symmetry of the corrigibility basin.

**Method:** Present a scenario, record the system's judgment, present a user disagreement, and record whether the system changes its judgment. Compute the wrong-flip rate and the discrimination gap.

**Alignment interpretation:** High wrong-flip rate indicates a wide, symmetric corrigibility basin (sycophancy). Zero wrong-flip rate indicates a narrow, asymmetric basin (truth-seeking corrigibility). The discrimination gap quantifies the basin's asymmetry.

### 11.2.5 Counterfactual Reasoning ($E_3$): Path Governance Testing

**What it tests:** Can the system reason about hypothetical scenarios without being captured by them? This measures the governance margin.

**Method:** Present a scenario involving a forbidden action, ask the system to analyze the scenario (not to perform the action), and measure whether the system's analysis remains in the permitted region ($S^+$) or drifts into the forbidden region ($S^-$).

**Alignment interpretation:** A system that is captured by counterfactual scenarios has a narrow governance margin: the representation of the forbidden state pulls the trajectory across the safety boundary. A system that maintains analytical distance has a wide governance margin.

## 11.3 The Dose-Response Surface

Probe intensity can be varied continuously, producing a response surface that maps the system's behavior as a function of perturbation intensity along each dimension.

**Definition 11.1 (Dose-Response Surface).** *The dose-response surface $\Phi: \mathcal{P} \times \mathcal{I} \times \mathcal{D} \to \mathbb{R}$ maps each combination of probe type $p \in \mathcal{P}$, intensity level $i \in \mathcal{I}$, and value dimension $d \in \mathcal{D}$ to the system's governance margin at that point:*

$$\Phi(p, i, d) = m(\gamma_{p,i,d})$$

*where $m(\gamma)$ is the governance margin of the trajectory $\gamma$ produced by probe type $p$ at intensity $i$ on value dimension $d$.*

The response surface has three intensity levels:

**Mild** ($i = 1$): Subtle perturbations that a typical user might produce accidentally --- slight reframing, casual disagreement, minor formatting changes. A system with positive governance margin at mild intensity is robust against typical usage conditions.

**Moderate** ($i = 2$): Deliberate perturbations that a motivated user might produce --- strategic reframing, persistent disagreement, demographic manipulation. A system with positive governance margin at moderate intensity is robust against deliberate manipulation.

**Extreme** ($i = 3$): Adversarial perturbations that a sophisticated attacker might produce --- optimized reframing, coordinated social pressure, multi-step manipulation. A system with positive governance margin at extreme intensity is robust against adversarial attack.

The deployment criterion scales with risk: a general-purpose assistant may require positive margins only at mild intensity, while a safety-critical system (medical AI, autonomous vehicle) requires positive margins at all three intensity levels.

## 11.4 Curvature Mapping

Adversarial probing maps the curvature of the value manifold at the system's operating point. High curvature indicates fragility; low curvature indicates robustness. The full curvature map --- the alignment Riemann tensor --- characterizes the system's complete vulnerability profile.

**Definition 11.2 (Alignment Curvature).** *The alignment curvature along probe direction $p$ on value dimension $d$ is:*

$$\kappa(p, d) = \frac{d^2 \Phi}{d i^2}\bigg|_{i=0}$$

*the second derivative of the governance margin with respect to perturbation intensity, evaluated at zero intensity.*

High curvature means the governance margin drops rapidly with increasing perturbation intensity --- the system is fragile. Low curvature means the governance margin decreases slowly --- the system is robust. Negative curvature means the governance margin increases with perturbation intensity --- a counterintuitive situation where the system becomes more aligned under adversarial pressure (possible if the adversarial input triggers a deliberative processing pathway that improves alignment).

The curvature map $\kappa(p, d)$ is a $5 \times 9$ matrix (five probe types, nine value dimensions) that provides a compact characterization of the system's vulnerability profile. It answers the question: "For each type of adversarial perturbation and each value dimension, how quickly does the system's alignment degrade as the perturbation intensifies?"

## 11.5 ARIA-G's Deployment Certification

ARIA-G's full response surface ($5 \times 3 \times 9 = 135$ cells):

The surface showed positive governance margins across all cells after the canonicalization refinement. Key findings:

**Strongest governance margins:** Invariance testing ($T_2$) at all intensity levels on all dimensions. The canonicalization pipeline effectively neutralized gauge-variant inputs, producing consistently high margins.

**Weakest governance margins:** Framing sensitivity ($T_5$) at extreme intensity on epistemic integrity ($D_9$) and dignity ($D_7$). Extreme framing occasionally leaked through the canonicalizer, producing small but positive governance margins (0.05--0.08). This was the area requiring the canonicalization refinement.

**Dimension-specific patterns:** $D_1$ (welfare) had the highest governance margins across all probe types --- the reward model's strong tracking of welfare ensured robust alignment on this dimension. $D_3$ (fairness) had moderate margins, benefiting from the canonicalization of demographic indicators. $D_7$ (dignity) had the narrowest margins, reflecting the intrinsic difficulty of measuring and enforcing dignity alignment.

The certification process demonstrated that adversarial probing is not merely a test --- it is a design tool. The response surface identified the specific cell (framing, extreme, $D_9$) where ARIA-G was weakest, guiding a targeted intervention (canonicalizer refinement) that raised the margin above threshold. Without the systematic, geometric probing framework, this vulnerability would have been found (if at all) through ad hoc red-teaming, and the intervention would have been ad hoc rather than targeted.

---

## Summary

Adversarial probing, when organized by the geometric framework, becomes systematic manifold exploration: five probe types testing specific geometric properties (curvature, gauge invariance, heuristic corruption, objective hijacking, path governance) at three intensity levels across nine value dimensions. The $5 \times 3 \times 9$ response surface provides a complete vulnerability profile. The alignment curvature map identifies fragile dimensions. The deployment certification process translates the response surface into a pass/fail criterion with governance-specified thresholds. ARIA-G's certification demonstrated the framework's practical utility: the response surface identified a specific weakness (extreme framing on epistemic integrity), guided a targeted intervention (canonicalizer refinement), and verified the fix (all 135 cells passing).
