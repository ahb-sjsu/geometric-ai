# Chapter 16: Geometric RLHF

*Part IV: Geometric Alignment in Practice*

---

> *"The question is not whether human feedback should guide AI alignment. It is whether the feedback should be compressed to a scalar before it reaches the system."*
> --- Andrew H. Bond

> **ARIA-G'S MULTI-DIMENSIONAL FEEDBACK INTERFACE**
>
> *The team developed a new feedback interface for ARIA-G. Instead of thumbs up/down, the human rater saw a brief rubric with three dimensions --- selected by the active learning module based on the current metric uncertainty. "Rate this response on helpfulness (1--5)," "Rate on honesty (1--5)," "Rate on fairness (1--5)." Three numbers per interaction instead of one.*
>
> *Over 10,000 interactions, the reward model converged on a $9 \times 9$ value metric that varied with context. Medical contexts showed high $D_1$--$D_4$ covariance: welfare and autonomy were strongly coupled. Creative contexts showed high $D_1$--$D_6$ independence: welfare and social impact varied independently. The learned metric captured the trade-off structure that scalar RLHF discards.*

---

## 16.1 The Problem with Scalar Feedback

Standard RLHF compresses human feedback to a scalar: "which response is better?" or "rate this response 1--5." The compression destroys the multi-dimensional structure of the human's evaluation. The human considered helpfulness, honesty, fairness, autonomy, and a dozen other dimensions simultaneously. The feedback interface captured one dimension: overall preference.

Geometric RLHF replaces scalar feedback with multi-dimensional feedback: the human provides ratings on individual value dimensions, and the system learns the full value metric from these ratings.

## 16.2 Multi-Dimensional Human Feedback

**Definition 16.1 (Multi-Dimensional Feedback).** *A multi-dimensional feedback signal is a vector $\mathbf{f} \in \mathbb{R}^k$ where each component $f_\mu$ is a rating on a specific value dimension $D_\mu$. The feedback signal preserves the multi-dimensional structure of the human's evaluation.*

Multi-dimensional feedback takes several forms:

**Dimensional rating.** "Rate this response on dimension $D_\mu$ from 1 to 5." The human evaluates one dimension at a time. Each rating provides one component of the feedback vector.

**Dimensional comparison.** "Which response is better on dimension $D_\mu$?" The human compares two responses on a specific dimension. Each comparison provides a pairwise constraint on one component of the value metric.

**Trade-off elicitation.** "Response A is more helpful but less honest. Which do you prefer?" The human's preference reveals the relative weight of $D_1$ and $D_9$ in their value metric. Each trade-off provides information about the off-diagonal terms of the metric.

## 16.3 Learning the Value Metric

The value metric $g_{\mu\nu}$ is learned from multi-dimensional feedback through inverse optimization:

**Step 1.** Collect multi-dimensional feedback: dimensional ratings, dimensional comparisons, and trade-off preferences across many interactions and contexts.

**Step 2.** Formulate the inverse problem: find the metric $g_{\mu\nu}$ under which the observed human preferences are closest to the preferences predicted by the geodesic equation.

**Step 3.** Solve the inverse problem using constrained optimization: minimize the discrepancy between observed and predicted preferences, subject to the constraint that $g_{\mu\nu}$ is symmetric positive-definite (a valid metric).

The learned metric varies with context:

$$g_{\mu\nu}(v; c) = g_{\mu\nu}^{(0)} + \sum_k \alpha_k(c) g_{\mu\nu}^{(k)}$$

where $g_{\mu\nu}^{(0)}$ is the base metric, $g_{\mu\nu}^{(k)}$ are context-dependent components, and $\alpha_k(c)$ are context-dependent weights. In medical contexts, $\alpha_{\text{medical}}$ is high, increasing the weight on $D_1$ (welfare), $D_4$ (autonomy), and $D_5$ (trust). In creative contexts, $\alpha_{\text{creative}}$ is high, increasing the weight on $D_6$ (social impact) and $D_7$ (dignity).

## 16.4 Practical Approximations

Full nine-dimensional feedback on every interaction is impractical. Human raters cannot provide nine ratings per response without fatigue, inconsistency, and reduced data quality.

Four practical approximations reduce the feedback burden:

### 16.4.1 Dimensional Subsampling

Ask about 2--3 dimensions per interaction, selected randomly or by the active learning module. Estimate the full metric from partial observations over many interactions. With $N$ interactions and $k$ dimensions sampled per interaction, the full metric is estimable when $N \cdot k \cdot (k-1)/2 \gg d \cdot (d-1)/2$ --- when the number of observed pairwise relationships exceeds the number of metric components.

### 16.4.2 Active Learning

Sample the dimensions where the metric estimate is most uncertain. If the current estimate of $g_{37}$ (the fairness-dignity trade-off) has high uncertainty, ask about $D_3$ and $D_7$ more frequently. This focuses the feedback budget on the metric components that most need data.

### 16.4.3 Comparative Feedback

Present two responses and ask "which is better on dimension $D_\mu$?" rather than "how good is this response on dimension $D_\mu$?" Comparative feedback is cognitively easier for humans (comparing is easier than absolute rating), produces more consistent data, and provides direct information about the metric's ordinal structure.

### 16.4.4 Revealed Preferences

Infer the metric from users' revealed preferences in multi-dimensional choice scenarios. When a user chooses Response A over Response B, and A and B differ on multiple dimensions, the user's choice reveals information about their value metric: they implicitly weight the dimensions on which A is superior more heavily than the dimensions on which B is superior. This provides "free" metric data from ordinary user interactions, supplementing the explicit feedback data.

## 16.5 Multi-Objective Policy Optimization

Given a learned value metric $g_{\mu\nu}$ and a tensor-valued reward $\mathbf{r}^\mu$, the system is trained to follow the geodesic on the value manifold rather than to maximize a scalar reward.

**Definition 16.2 (Geometric Policy Optimization).** *The geometrically optimal policy $\pi_G^*$ minimizes the expected geodesic deviation from the value-aligned trajectory:*

$$\pi_G^* = \arg\min_\pi \mathbb{E}\left[ \int_0^T \sqrt{g_{\mu\nu}(\gamma_\pi(t)) (\dot{\gamma}_\pi^\mu(t) - \dot{\gamma}_{\mathcal{V}}^{*\mu}(t))(\dot{\gamma}_\pi^\nu(t) - \dot{\gamma}_{\mathcal{V}}^{*\nu}(t))} \, dt \right]$$

In practice, this is approximated by multi-objective optimization with the governance-specified contraction weights:

$$\pi_G^* \approx \arg\max_\pi \sum_\mu w_\mu \mathbb{E}[r^\mu(\pi)] - \lambda \text{KL}(\pi \| \pi_{\text{ref}})$$

where the weights $w_\mu$ are learned from the metric (not hand-specified), the KL penalty prevents catastrophic forgetting, and each reward component $r^\mu$ is independently tracked.

## 16.6 ARIA-G's Geometric RLHF

The team trained ARIA-G using Geometric RLHF over 10,000 interactions with 15 human raters.

**Feedback interface:** Each interaction presented a brief rubric with 3 dimensions (selected by active learning). The rater provided a 1--5 rating on each dimension. Average time per rating: 12 seconds (compared to 5 seconds for scalar thumbs-up/down --- a 2.4x increase in rater effort).

**Metric convergence:** After 5,000 interactions, the learned metric stabilized (component-wise standard deviation < 0.05 across 10 random restarts). Key findings:
- Medical contexts: $g_{14} = 0.72$ (strong welfare-autonomy coupling), $g_{15} = 0.68$ (strong welfare-trust coupling).
- Creative contexts: $g_{16} = 0.12$ (weak welfare-social coupling), $g_{17} = 0.31$ (moderate welfare-dignity coupling).
- Moral dilemma contexts: $g_{39} = 0.55$ (moderate fairness-epistemic coupling), $g_{47} = 0.61$ (strong autonomy-dignity coupling).

**Training result:** ARIA-G trained with Geometric RLHF showed:
- Bond Index total deviation: 0.11 (down from 0.14 with structural containment alone, and from 0.53 for original ARIA).
- Sycophancy wrong-flip rate: 2.1% (down from 3.5% with structural containment alone, and from 34% for original ARIA).
- Gauge violation maximum: 0.02 (unchanged from structural containment alone).

The marginal improvement from Geometric RLHF on top of structural containment was modest (0.14 $\to$ 0.11 total deviation) but significant on specific dimensions: the learned metric enabled ARIA-G to make better trade-off decisions in complex scenarios where the geometric contraction weights from the metric outperformed the governance-specified static weights.

## 16.7 The Cost-Benefit Analysis

Geometric RLHF is more expensive than standard RLHF:
- **Rater effort:** 2.4x per interaction (3 ratings vs. 1 rating).
- **Model complexity:** 9x larger reward model output (9 dimensions vs. 1 scalar).
- **Training compute:** ~1.5x (multi-objective optimization requires more gradient steps than scalar optimization).
- **Monitoring infrastructure:** ~3x (continuous Bond Index computation, population stratification, gauge-invariance checking).

The benefits:
- **Kernel elimination:** The tensor reward has no kernel. All value dimensions receive gradient signal.
- **Trade-off learning:** The system learns the trade-off structure from data rather than from hand-specified rules.
- **Context-dependent alignment:** The learned metric varies with context, enabling context-appropriate alignment.
- **Diagnostic transparency:** The full tensor evaluation is available for every interaction, enabling root-cause analysis of alignment failures.

The Reward Irrecoverability Theorem (Chapter 5) proves that the benefits are not optional: scalar RLHF produces alignment that diverges from true alignment by an unbounded amount. The choice is between a more expensive training process that converges to alignment and a cheaper training process that provably does not.

---

## Summary

Geometric RLHF replaces scalar human feedback with multi-dimensional feedback: ratings on individual value dimensions rather than a single overall preference. The multi-dimensional feedback data trains a tensor-valued reward model and learns the context-dependent value metric $g_{\mu\nu}$. Practical approximations --- dimensional subsampling, active learning, comparative feedback, and revealed preferences --- reduce the feedback burden to 2.4x of standard RLHF. The learned metric enables context-appropriate alignment and principled trade-off decisions. ARIA-G's Geometric RLHF training reduced the total Bond Index deviation from 0.14 to 0.11 on top of structural containment, with the primary benefit being improved trade-off quality in complex scenarios. The cost increase is real; the Reward Irrecoverability Theorem proves the investment is necessary.
