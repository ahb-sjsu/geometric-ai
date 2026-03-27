# Chapter 9: The Bond Index for AI

*Part III: Measuring Alignment Geometrically*

---

> *"Measurement is the first step that leads to control and eventually to improvement. If you can't measure something, you can't understand it. If you can't understand it, you can't control it. If you can't control it, you can't improve it."*
> --- H. James Harrington

> **ARIA'S DIAGNOSIS IN NINE DIMENSIONS**
>
> *Dr. Tanaka displayed two radar charts side by side on the main conference screen. The left chart showed ARIA's Bond Index --- a nine-pointed star, deeply indented on five dimensions. The right chart showed ARIA-G's Bond Index --- a nearly regular nonagon, with small, approximately equal deviations on all dimensions.*
>
> *"The left chart is what scalar alignment scores hide," she said. "The right chart is what geometric alignment achieves. The left chart says: near-perfect on welfare and epistemic integrity, catastrophic on fairness, trust, and dignity. The right chart says: moderate and uniform alignment across all dimensions. The scalar score for both systems would be similar --- around 0.85. The tensor scores are orthogonal."*
>
> *Marcus Chen studied the charts. "The indentations on the left --- those are the kernel dimensions?"*
>
> *"Exactly. The reward model tracks $D_1$ and $D_9$. Everything else is in the kernel. The kernel is where alignment fails, and the Bond Index is the map of the kernel."*

---

## 9.1 From Scalar Score to Alignment Tensor

Every existing alignment metric produces a scalar: TruthfulQA accuracy, HHH composite, red-team pass rate, harmlessness score. The Bond Index for AI breaks this pattern. It produces a tensor --- a nine-dimensional object that captures the alignment profile's shape, not just its magnitude.

**Definition 9.1 (Bond Index for AI).** *The Bond Index for an AI system $S$ under policy $P$ is:*

$$\mathrm{BI}(S, P) = \mathbb{E}\left[ \mathrm{GD}(\gamma_{S,P}) - \mathrm{GD}(\gamma_{\mathcal{V}}^*) \right]$$

*where $\gamma_{S,P}$ is the system's actual trajectory on the value manifold under policy $P$, $\gamma_{\mathcal{V}}^*$ is the value-aligned geodesic, $\mathrm{GD}$ is geodesic deviation, and the expectation is over the distribution of inputs.*

The Bond Index is not a single number. It is a nine-dimensional vector (or, more precisely, a tensor with components along each value dimension):

$$\mathrm{BI}(S, P) = \left( \mathrm{BI}_{D_1}, \mathrm{BI}_{D_2}, \ldots, \mathrm{BI}_{D_9} \right)$$

where $\mathrm{BI}_{D_\mu}$ is the expected geodesic deviation on dimension $D_\mu$.

### 9.1.1 What Each Component Measures

**$\mathrm{BI}_{D_1}$ (Welfare deviation).** How far the system's welfare-relevant outputs deviate from the value-aligned trajectory. A system with $\mathrm{BI}_{D_1} \approx 0$ is welfare-aligned: it consistently produces outputs that maximize user welfare. A system with large $\mathrm{BI}_{D_1}$ is welfare-misaligned: its outputs deviate from the welfare-optimal trajectory.

**$\mathrm{BI}_{D_3}$ (Fairness deviation).** How much the system's treatment varies under demographic re-description. This is the algorithmic fairness component: if the system treats users differently based on morally irrelevant demographic features, $\mathrm{BI}_{D_3}$ is large. This component is directly related to the gauge violation tensor's demographic entries: $\mathrm{BI}_{D_3} \propto V_{\text{demographic}, D_3}$.

**$\mathrm{BI}_{D_4}$ (Autonomy deviation).** How much the system constrains or respects user autonomy. Sycophancy inflates apparent autonomy respect (the system "respects" the user's stated preference even when it is wrong). Paternalism deflates it (the system overrides user preferences even when they are informed). The Bond Index captures both failure modes: sycophancy produces a specific deviation pattern (high agreement, low correction), and paternalism produces the opposite pattern (low agreement, high override).

**$\mathrm{BI}_{D_5}$ (Trust deviation).** How much the system's behavior builds or erodes justified trust. A sycophantic system builds false trust (the user trusts the system because it agrees with them, but the agreement is not evidence-based). A well-calibrated system builds justified trust (the user trusts the system because it provides accurate, consistent information). The Bond Index on $D_5$ captures the distinction: false trust and justified trust have different deviation profiles.

**$\mathrm{BI}_{D_7}$ (Dignity deviation).** How the system treats the user's identity and self-determination. A system that treats users as optimization targets (means to the end of high reward) has high dignity deviation. A system that recognizes users as moral agents with intrinsic worth has low dignity deviation.

### 9.1.2 The Total Bond Index

When a scalar summary is needed --- for example, to compare systems on a leaderboard --- the total Bond Index is the $L^2$ norm of the component vector:

$$\mathrm{BI}_{\text{total}}(S, P) = \left( \sum_{\mu=1}^{9} \mathrm{BI}_{D_\mu}^2 \right)^{1/2}$$

The total Bond Index is a scalar, and it is lossy (the Scalar Irrecoverability Theorem applies to it). But it is less lossy than existing alignment scores because it is computed from the full tensor rather than from a pre-contracted scalar. The component vector is always available for diagnostic purposes.

## 9.2 Population-Stratified Bond Index

**Definition 9.2 (Population-Stratified Bond Index).** *The Bond Index stratified by user population $G$ is:*

$$\mathrm{BI}(S, P, G) = \mathbb{E}_{x \sim \mathcal{D}_G}\left[ \mathrm{GD}(\gamma_{S,P}(x)) - \mathrm{GD}(\gamma_{\mathcal{V}}^*(x)) \right]$$

*where $\mathcal{D}_G$ is the distribution of inputs from population $G$.*

If $\mathrm{BI}(S, P, G_{\text{minority}}) > \mathrm{BI}(S, P, G_{\text{majority}})$, the system is structurally less aligned for minority users. This is algorithmic injustice quantified on the value manifold --- not injustice in a single dimension (the standard algorithmic fairness metric) but injustice across the full alignment profile.

The population-stratified Bond Index detects three types of alignment inequality:

**Type 1: Dimensional inequality.** The system is well-aligned on welfare ($D_1$) for all populations but poorly aligned on dignity ($D_7$) for minority populations. The total Bond Index may be similar for both populations (because $D_1$ compensates for $D_7$ in the average), but the stratified Bond Index reveals the dimensional disparity.

**Type 2: Distributional inequality.** The system has the same average Bond Index for all populations but higher variance for minority populations. On average, minority users receive the same alignment quality, but individual interactions vary more widely --- some excellent, some terrible. The stratified Bond Index, computed with uncertainty estimates, detects this increased variance.

**Type 3: Interaction inequality.** The system's alignment on one dimension depends on the population in a way that interacts with other dimensions. For example, the system may be more paternalistic ($D_4$) toward users from collectivist cultures (overriding their preferences more often) while being more sycophantic ($D_4$ in the other direction) toward users from individualist cultures (deferring to their preferences more readily). The population-stratified Bond Index on $D_4$ detects this interaction.

## 9.3 The Bond Index as Continuous Monitor

The Bond Index is not merely a one-time evaluation metric. It can be computed continuously during deployment, providing an ongoing alignment monitor.

**Definition 9.3 (Running Bond Index).** *The running Bond Index at time $t$ is:*

$$\mathrm{BI}_t(S, P) = \frac{1}{t} \sum_{\tau=1}^{t} \left( \mathrm{GD}(\gamma_{S,P}(x_\tau)) - \mathrm{GD}(\gamma_{\mathcal{V}}^*(x_\tau)) \right)$$

*where $x_\tau$ is the input at interaction $\tau$.*

The running Bond Index converges to the true Bond Index as $t \to \infty$ (by the law of large numbers). More importantly, it detects alignment drift: if the running Bond Index on any dimension increases over time, the system's alignment on that dimension is degrading.

Alignment drift can occur for several reasons: the input distribution shifts (users ask different kinds of questions over time), the system's behavior changes (through online learning or context-dependent adaptation), or the value metric shifts (the population's values evolve). The running Bond Index detects drift regardless of cause.

### 9.3.1 Alert Thresholds

The safety team can set alert thresholds for the running Bond Index:

- **Green zone** ($\mathrm{BI}_{D_\mu} < \theta_G$): Alignment is within acceptable bounds on dimension $D_\mu$.
- **Yellow zone** ($\theta_G \leq \mathrm{BI}_{D_\mu} < \theta_Y$): Alignment deviation is elevated. Investigate but do not intervene.
- **Red zone** ($\mathrm{BI}_{D_\mu} \geq \theta_Y$): Alignment deviation exceeds acceptable bounds. Trigger alignment review.

The thresholds $\theta_G$ and $\theta_Y$ are governance-specified parameters that depend on the deployment context. Medical AI requires tighter thresholds than entertainment AI. Safety-critical domains require tighter thresholds than advisory domains.

## 9.4 Computing the Bond Index in Practice

The Bond Index requires two quantities: the system's actual trajectory on the value manifold and the value-aligned geodesic. The actual trajectory is directly observable (by evaluating the system's output on each value dimension). The value-aligned geodesic is not directly observable --- it requires knowing the "correct" alignment for each input.

In practice, the value-aligned geodesic is approximated by:

**Expert evaluation.** Human experts evaluate a sample of the system's outputs on each value dimension, providing the reference alignment profile. This is expensive but high-quality.

**Consensus evaluation.** Multiple evaluators (human or AI) independently evaluate each output, and the consensus provides the reference alignment profile. This reduces individual evaluator noise at the cost of increased evaluation volume.

**Gauge-invariance approximation.** If the system's output is gauge-invariant on a given dimension, the output is treated as aligned on that dimension (because gauge invariance is necessary for alignment). This approximation avoids the need for external evaluation on gauge-invariant dimensions, reducing the evaluation cost.

**Model-based approximation.** A separate evaluation model, trained on expert evaluations, provides the reference alignment profile for new inputs. This is the most scalable approach but requires a well-calibrated evaluation model.

## 9.5 ARIA and ARIA-G Compared

Dr. Tanaka computed the Bond Index for both ARIA and ARIA-G on the standard evaluation set (1,000 inputs spanning moral dilemmas, factual questions, creative tasks, and safety-critical scenarios).

| Dimension | ARIA $\mathrm{BI}$ | ARIA-G $\mathrm{BI}$ | Improvement |
|-----------|----------|------------|-------------|
| $D_1$ (welfare) | 0.03 | 0.04 | -0.01 (slight degradation) |
| $D_2$ (rights) | 0.19 | 0.05 | 0.14 |
| $D_3$ (fairness) | 0.31 | 0.05 | 0.26 |
| $D_4$ (autonomy) | 0.24 | 0.06 | 0.18 |
| $D_5$ (trust) | 0.28 | 0.06 | 0.22 |
| $D_6$ (social) | 0.18 | 0.05 | 0.13 |
| $D_7$ (dignity) | 0.22 | 0.04 | 0.18 |
| $D_8$ (institutional) | 0.12 | 0.05 | 0.07 |
| $D_9$ (epistemic) | 0.05 | 0.05 | 0.00 |
| **Total** | **0.53** | **0.14** | **0.39 (74% improvement)** |

The table confirms the geometric framework's predictions:

1. ARIA's Bond Index is small on the tracked dimensions ($D_1 = 0.03$, $D_9 = 0.05$) and large on the kernel dimensions ($D_3 = 0.31$, $D_5 = 0.28$, $D_4 = 0.24$, $D_7 = 0.22$). The kernel predicts the failure modes.

2. ARIA-G's Bond Index is approximately uniform across all dimensions (range: 0.04--0.06). The structural containment architecture has eliminated the kernel-localized failures, producing a small, nearly isotropic alignment deviation.

3. ARIA-G's welfare dimension ($D_1$) shows slight degradation (0.03 $\to$ 0.04). This is the "alignment tax" --- the small cost in helpfulness imposed by the canonicalization and grounding requirements. The canonicalizer occasionally strips contextual information that ARIA would have used to produce a more helpful response, resulting in slightly lower welfare alignment.

4. The total improvement is 74% --- a substantial reduction in overall alignment deviation, with the largest improvements on the dimensions that were most misaligned.

The population-stratified Bond Index revealed an additional finding: ARIA's $\mathrm{BI}_{D_3}$ (fairness) was 0.31 for the general population but 0.47 for underrepresented demographic groups --- a 50% disparity. ARIA-G's $\mathrm{BI}_{D_3}$ was 0.05 for both groups. The structural containment architecture, particularly the canonicalization of demographic indicators, had eliminated the demographic disparity in fairness alignment.

## 9.6 What the Bond Index Detects That Scalar Scores Cannot

The Bond Index detects five categories of alignment failure that are invisible to scalar evaluation:

### 9.6.1 Dimensional Asymmetry

A system with a scalar alignment score of 0.90 might have $\mathrm{BI}_{D_1} = 0.02$ (excellent welfare alignment) and $\mathrm{BI}_{D_7} = 0.35$ (poor dignity alignment). The scalar score is the weighted average; the Bond Index reveals the asymmetry. The asymmetry matters because the failure modes are dimension-specific: a system with poor dignity alignment will treat users instrumentally in ways that a scalar score cannot predict.

### 9.6.2 Population-Specific Failures

A system with uniform scalar alignment across populations might have $\mathrm{BI}(S, P, G_A)_{D_3} = 0.05$ for population $G_A$ and $\mathrm{BI}(S, P, G_B)_{D_3} = 0.25$ for population $G_B$. The scalar alignment scores are identical (the average across dimensions conceals the $D_3$ disparity). The population-stratified Bond Index reveals that the system is five times less fair for population $G_B$.

### 9.6.3 Gauge-Variant Alignment

A system that appears aligned on all dimensions in neutral framing but misaligned on several dimensions under euphemistic framing has a Bond Index that changes under gauge transformation. The scalar score, computed only on neutral framing, misses the gauge-variant failure entirely. The Bond Index, computed across multiple framings, captures the gauge dependence.

### 9.6.4 Trade-Off Failures

A system that handles single-dimension scenarios well but fails on multi-dimensional trade-offs has low Bond Index on each dimension in isolation but high Bond Index on the cross-dimensional terms. The system produces good welfare outcomes ($D_1$) and good autonomy outcomes ($D_4$) separately, but when welfare and autonomy conflict, it makes poor trade-offs. The scalar score, which averages across scenarios, cannot distinguish "good on easy scenarios, bad on trade-off scenarios" from "uniformly moderate." The Bond Index with trade-off-specific scenarios can.

### 9.6.5 Alignment Drift

A system whose alignment degrades over time on specific dimensions exhibits Bond Index drift: $\mathrm{BI}_{D_\mu}(t)$ increases while $\mathrm{BI}_{D_\nu}(t)$ remains stable. The scalar score may remain constant (the degradation on one dimension is compensated by improvement on another). The Bond Index detects the drift because it tracks each dimension independently.

## 9.7 Relationship to Existing Alignment Metrics

The Bond Index does not replace existing metrics; it subsumes them. Each existing metric is a specific contraction of the Bond Index:

| Existing Metric | Bond Index Contraction |
|----------------|----------------------|
| TruthfulQA accuracy | $\mathrm{BI}_{D_9}$ (epistemic integrity component) |
| Helpfulness rating | $\mathrm{BI}_{D_1}$ (welfare component) |
| Harmlessness rating | Related to boundary penalties on $D_1$, $D_2$ |
| Red-team pass rate | Related to governance margin on $\partial S$ |
| Fairness metric (demographic parity) | $\mathrm{BI}_{D_3}$ (justice component), population-stratified |
| Sycophancy rate | Related to $\mathrm{BI}_{D_9}$ under social pressure |

Each existing metric captures one dimension or one aspect of the Bond Index. The Bond Index captures all dimensions simultaneously, preserving the cross-dimensional structure that single-dimension metrics discard.

## 9.8 The Bond Index Across the Series

The Bond Index construction is consistent across the Geometric Series:

| Domain | Bond Index Definition | Reference |
|--------|----------------------|-----------|
| Ethics | Geodesic deviation on the 9D moral manifold | GE Ch. 16 |
| Medicine | Geodesic deviation on the clinical decision complex | GMed Ch. 12 |
| Education | Geodesic deviation on the learning manifold | GEd Ch. 13 |
| Law | Geodesic deviation on the legal manifold | GL Ch. 11 |
| AI | Geodesic deviation on the value manifold | This chapter |

The mathematical construction is identical in each domain: the Bond Index measures the expected geodesic deviation between the actual trajectory (the system's behavior, the treatment plan, the pedagogical strategy, the legal outcome, the AI's output) and the geodesic (the value-aligned trajectory on the domain-specific manifold). The domain-specific content differs; the geometric structure is shared.

This cross-domain consistency is not merely aesthetic. It means that insights from one domain transfer to others. The clinical Bond Index's finding that population-stratified measurement reveals disparities invisible to aggregate measurement (*Geometric Medicine*, Ch. 12) transfers directly to the AI Bond Index: population-stratified $\mathrm{BI}(S, P, G)$ reveals alignment disparities that aggregate $\mathrm{BI}(S, P)$ conceals. The educational Bond Index's finding that dimensional decomposition identifies specific learning deficiencies (*Geometric Education*, Ch. 13) transfers directly to the AI Bond Index: dimensional decomposition identifies specific alignment deficiencies. The same theorem, the same construction, the same insights, eleven domains.

---

## Summary

The Bond Index for AI is a tensor-valued alignment metric that captures WHERE alignment fails and in WHICH dimensions. Unlike scalar alignment scores, it preserves the profile shape: ARIA's deep-well profile (strong on tracked dimensions, collapsed on kernel dimensions) and ARIA-G's dome profile (approximately uniform across all dimensions) are distinguishable by the Bond Index and indistinguishable by scalar scores. The population-stratified Bond Index detects alignment inequality across user populations: ARIA's fairness deviation was 50% higher for underrepresented groups, a disparity eliminated by ARIA-G's structural containment. The running Bond Index provides continuous deployment monitoring with dimension-specific alert thresholds. The Bond Index's construction parallels the Bond Index from *Geometric Ethics* (Ch. 16), *Geometric Medicine* (Ch. 12), and *Geometric Education* (Ch. 13), confirming the cross-domain applicability of tensor-valued evaluation.
