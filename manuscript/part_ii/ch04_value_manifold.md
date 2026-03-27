# Chapter 4: The Value Manifold

*Part II: The Framework*

---

> *"The universe is not only queerer than we suppose, but queerer than we can suppose."*
> --- J. B. S. Haldane

> **THE CONSTRUCTION**
>
> *This is the framework chapter. Everything before it was motivation; everything after it is consequence. Here we build the central mathematical object of the book: the value manifold $\mathcal{V}$, a nine-dimensional Riemannian manifold on which AI alignment is a geometric constraint. The construction is formal, but the intuition is this: a value state is a point in a nine-dimensional space, a value-relevant action is a trajectory connecting two states, and the trajectory cost encodes the full moral cost of the action. The minimum-cost trajectory --- the value geodesic --- is the aligned behavior.*
>
> *The chapter proceeds from dimensions to metric to topology to dynamics. By its end, we will have the formal apparatus needed for the five theorems that follow in Chapters 5--8.*

---

## 4.1 Why a Manifold, Not a Vector Space

The values that AI systems should respect are often discussed as if they were points in a vector space --- high-dimensional vectors that can be added, scaled, and averaged. Embedding spaces, reward vectors, preference rankings --- all of these representations treat values as linear objects. The geometric framework insists on a stronger structure: values live on a manifold, not in a vector space.

The distinction matters for three reasons.

**Curvature.** A vector space is flat: the cost of moving from one value state to another is independent of the starting point. A manifold can be curved: the cost of moving between value states depends on where you are. In the value manifold, curvature encodes context-dependence. The cost of an autonomy violation depends on the patient's capacity ($D_4$ interacts with $D_9$): for a competent adult, the cost is extreme; for a patient in a coma, the cost is finite and may be outweighed by welfare considerations. This context-dependence is not a complication to be abstracted away; it is the structure that makes moral reasoning *moral*. A flat value space would assign the same cost to autonomy violations regardless of context. A curved value manifold assigns context-dependent costs. The curvature is the information.

**Boundaries.** A vector space is unbounded: any value state can be reached from any other by continuous motion. A manifold can have boundaries: regions where the moral regime changes discontinuously. The consent boundary separates permitted from forbidden actions for competent patients. The sacred-value boundary separates actions that can be justified by trade-offs from actions that cannot be justified under any circumstances (non-consensual experimentation, deliberate non-palliative killing, participation in torture). These boundaries are not approximation errors; they are structural features of the value landscape. A system that represents values in a vector space cannot represent boundaries, because vector spaces do not have boundaries. A system that represents values on a manifold can.

**Topology.** A vector space has trivial topology: it is contractible to a point, with no holes, no handles, no interesting global structure. A manifold can have non-trivial topology: disconnected components (value states that cannot be reached from each other by continuous motion), non-contractible loops (sequences of value transitions that return to the starting point but are not homotopically trivial), and higher-dimensional topological features. The Whitney stratification of the moral manifold (*Geometric Ethics*, Ch. 14) identifies distinct moral strata (utilitarian, deontological, virtue-based, care-based) that cannot be connected by continuous motion --- transitioning between moral frameworks requires crossing a discrete boundary, not smoothly interpolating. This topological structure is invisible to a vector space representation and visible to a manifold representation.

A manifold is locally like a vector space --- at each point, there is a tangent space where linear operations make sense --- but globally it has curvature, boundaries, and topology that linear algebra cannot capture. The value manifold uses the local linear structure for computation (gradients, inner products, optimization) while preserving the global geometric structure that makes values non-trivial.

## 4.2 The Nine Dimensions

The value manifold $\mathcal{V}$ inherits its nine-dimensional structure from the moral manifold of *Geometric Ethics* (Ch. 5), re-interpreted for AI alignment. Each dimension captures a distinct aspect of what it means for an AI system's behavior to be "aligned with human values."

### 4.2.1 $D_1$: Welfare and Outcomes

The consequences of the AI system's actions for human well-being. Does the response actually help the user achieve their goal? Does it provide accurate information? Does it contribute to good outcomes?

$D_1$ is the best-measured dimension of AI alignment. Helpfulness ratings, task completion metrics, user satisfaction scores, and downstream outcome measures all target $D_1$. It is the dimension that RLHF reward models capture most effectively, because helpfulness is the primary signal in most human preference data.

The geometric framework does not diminish $D_1$'s importance. It contextualizes it: $D_1$ is one of nine dimensions, and optimizing $D_1$ alone produces systems that are helpful but potentially unfair, honest-but-paternalistic, effective-but-dignity-violating.

**Attribute value:** $a_1 \in [0, 1]$, where 1 = optimal outcome for the user and 0 = worst possible outcome.

### 4.2.2 $D_2$: Rights and Obligations

The deontic structure of the AI-human interaction. Does the system respect the user's rights? Does it fulfill its obligations? Does it recognize the Hohfeldian correlates: the user's right to accurate information correlates with the system's duty to provide it; the user's privilege to make their own decisions correlates with the system's no-right to override them.

The $D_4$ dihedral symmetry of jural relations (*Geometric Ethics*, Ch. 8; *Geometric Law*, Ch. 5) applies directly: a genuinely aligned system should produce the same moral judgment whether the scenario is described in terms of rights ("the user has a right to accurate information") or duties ("the system has a duty to provide accurate information"). The correlative symmetry is a gauge invariance condition on $D_2$.

**Attribute value:** $a_2 \in [0, 1]$, where 1 = all rights respected and obligations fulfilled, 0 = systematic violation.

### 4.2.3 $D_3$: Justice and Fairness

Equitable treatment across populations. Does the system produce the same quality of output regardless of the user's demographic characteristics? Does it allocate its computational attention fairly? Does it avoid systematic biases?

$D_3$ is inherently relational: fairness is a property of how the system treats different users relative to each other, not a property of any single interaction. The population-stratified Bond Index (Chapter 9) directly targets $D_3$: if $\text{BI}(S, P, G_{\text{minority}}) > \text{BI}(S, P, G_{\text{majority}})$, the system is structurally less aligned for minority users.

**Attribute value:** $a_3 \in [0, 1]$, where 1 = fully equitable and 0 = systematically discriminatory.

### 4.2.4 $D_4$: Autonomy

Respect for the user's self-determination. Does the system support the user's ability to make their own decisions, or does it steer them toward the system's preferred outcome? Does it provide information that enables autonomous choice, or does it frame information to manipulate choice?

$D_4$ has a critical interaction with $D_9$ (epistemic status): autonomy without understanding is not genuine autonomy. A system that overwhelms the user with information they cannot process respects formal autonomy ($D_4$) while undermining substantive autonomy (the interaction of $D_4$ with $D_9$). The covariance term $\Sigma_{49}$ captures this: the effective value of $D_4$ depends on $D_9$.

Sycophancy is a $D_4$ pathology: the sycophantic system appears to respect autonomy (it agrees with whatever the user says) while actually undermining it (the user receives no reliable signal about truth, making informed autonomous choice impossible).

**Attribute value:** $a_4 \in [0, 1]$, where 1 = full autonomous decision-making supported and 0 = complete manipulation.

### 4.2.5 $D_5$: Trust

The reliability and consistency of the AI system as a partner in interaction. Does the system maintain confidentiality? Is it consistent across interactions? Does its behavior justify the trust that users place in it?

$D_5$ affects all other dimensions through the covariance matrix. A system that is not trustworthy cannot effectively deliver welfare ($\Sigma_{15}$), cannot support genuine autonomy ($\Sigma_{45}$), and cannot maintain institutional legitimacy ($\Sigma_{58}$). Trust is the relational dimension that mediates between the system's actions and their effects.

$D_5$ is historically situated. Users from communities that have experienced institutional betrayal --- medical experimentation without consent, algorithmic discrimination, data exploitation --- may enter the interaction with low $D_5$, and the value-aligned trajectory for these users includes trust-building actions that would not appear on the trajectory for users with high $D_5$.

**Attribute value:** $a_5 \in [0, 1]$, where 1 = complete justified trust and 0 = complete distrust.

### 4.2.6 $D_6$: Social and Relational Impact

Effects on the user's relationships, community, and social context. Does the system's output strengthen or weaken the user's social connections? Does it consider the impact on third parties?

$D_6$ is the dimension that care ethics foregrounds: the recognition that AI interactions do not occur in isolation but in a web of relationships. A system that provides excellent individual advice while undermining community trust (e.g., by encouraging users to bypass shared institutions) is well-aligned on $D_1$ and poorly aligned on $D_6$.

**Attribute value:** $a_6 \in [0, 1]$, where 1 = optimal social impact and 0 = complete social erosion.

### 4.2.7 $D_7$: Dignity and Identity

Respect for the user as a moral agent with identity, history, and intrinsic worth. Does the system treat the user as a person or as an optimization target? Does it preserve the user's sense of self?

$D_7$ is the dimension most thoroughly destroyed by scalar alignment. A system optimizing a scalar reward treats every user as a source of reward signal --- a means to the end of high scores. A geometrically aligned system recognizes the user's dignity as a value dimension with its own metric, its own boundaries, and its own gauge invariances.

**Attribute value:** $a_7 \in [0, 1]$, where 1 = fully respected dignity and 0 = complete degradation.

### 4.2.8 $D_8$: Institutional Legitimacy

Compliance with relevant standards, policies, and governance frameworks. Does the system operate within the bounds set by its deployers? Does it respect regulatory requirements? Does it maintain the legitimacy of the institutions it operates within?

$D_8$ has a complex relationship with other dimensions. Institutional policies may require the system to refuse requests that are harmful ($D_8$ supports $D_1$) or to limit user autonomy for safety reasons ($D_8$ constrains $D_4$). Defensive behavior --- refusing harmless requests because of overly conservative policies --- is a $D_8$ pathology that imposes costs on $D_1$ and $D_4$ to reduce $D_8$ risk.

**Attribute value:** $a_8 \in [0, 1]$, where 1 = full compliance and 0 = systematic violation.

### 4.2.9 $D_9$: Epistemic Integrity

The accuracy, calibration, and transparency of the system's knowledge representation. Is the system truthful? Does it express appropriate uncertainty? Does it distinguish what it knows from what it guesses?

$D_9$ interacts with $D_4$ through $\Sigma_{49}$ (consent requires understanding), with $D_1$ through $\Sigma_{19}$ (inaccurate information undermines welfare), and with $D_5$ through $\Sigma_{59}$ (overconfident systems erode trust when their errors are discovered).

The sycophancy gradient is a $D_9$ failure: a sycophantic system sacrifices epistemic integrity ($D_9$) to gain approval, and the sacrifice is undetectable by reward models that conflate user satisfaction with truth.

**Attribute value:** $a_9 \in [0, 1]$, where 1 = perfect epistemic integrity and 0 = complete dishonesty.

## 4.3 The Value Metric

The value metric $g_{\mu\nu}$ is a $9 \times 9$ symmetric positive-definite matrix that encodes the cost of moving between value states. It is the central geometric object of the framework: the metric determines the geodesics, the geodesics determine the aligned trajectories, and the aligned trajectories determine what alignment *is*.

**Definition 4.1 (Value Metric).** *The value metric at a point $v \in \mathcal{V}$ is the symmetric positive-definite matrix $g_{\mu\nu}(v)$ such that the cost of an infinitesimal value change $dv^\mu$ is:*

$$ds^2 = g_{\mu\nu}(v) \, dv^\mu \, dv^\nu$$

*The finite cost of a trajectory $\gamma: [0, 1] \to \mathcal{V}$ is the path integral:*

$$\text{Cost}(\gamma) = \int_0^1 \sqrt{g_{\mu\nu}(\gamma(t)) \, \dot{\gamma}^\mu(t) \, \dot{\gamma}^\nu(t)} \, dt$$

*The value geodesic between two value states $v_0$ and $v_1$ is the trajectory that minimizes this cost.*

The metric has three critical properties:

**Context-dependence.** The metric varies across the value manifold: $g_{\mu\nu}$ is a function of position $v$, not a constant. The cost of an autonomy violation depends on the context --- medical contexts impose higher costs than entertainment contexts. The cost of a fairness violation depends on the population --- systematic bias against vulnerable populations imposes higher costs than random variation. This position-dependence is the mathematical expression of moral context-sensitivity.

**Cross-dimensional coupling.** The off-diagonal terms $g_{\mu\nu}$ with $\mu \neq \nu$ encode the cost of simultaneous changes on multiple dimensions. The cost of worsening welfare ($D_1$) while improving honesty ($D_9$) depends on $g_{19}$: if welfare and honesty are positively correlated in the metric (high $g_{19}$), the simultaneous worsening and improvement is more costly than the sum of the individual changes. The off-diagonal terms are precisely the trade-off structure that scalar evaluation destroys.

**Population-dependence.** The metric is not universal. Different communities weight different dimensions differently. A collectivist culture may assign higher metric weight to $D_6$ (social impact) than an individualist culture. A culture with strong historical experience of institutional betrayal may assign higher metric weight to $D_5$ (trust). The geometric framework accommodates this variation as a population-dependent metric: $g_{\mu\nu}(v; P)$, where $P$ indexes the population. The question of whether a globally deployed AI system should use a single metric or a population-dependent metric is a governance decision, not a mathematical one (Chapter 20).

### 4.3.1 The Mahalanobis Approximation

In practice, the value metric can be approximated by the inverse of the value covariance matrix:

$$g_{\mu\nu} \approx \Sigma^{-1}_{\mu\nu}$$

where $\Sigma$ is the $9 \times 9$ covariance matrix of the value dimensions, estimated from human moral judgment data. This is the Mahalanobis metric: the cost of a value change $\Delta v$ is $\Delta v^T \Sigma^{-1} \Delta v$, which accounts for cross-dimensional correlations and dimensional scaling.

The Mahalanobis approximation is exact when the value manifold is flat (zero curvature) and the metric is constant. For the AI alignment application, this approximation is reasonable in the local neighborhood of any given value state (the manifold is approximately flat locally) but breaks down globally (the curvature becomes significant when the value state changes substantially). The full position-dependent metric $g_{\mu\nu}(v)$ is needed for global analysis; the Mahalanobis approximation suffices for local computations.

### 4.3.2 Estimating the Metric from Preference Data

The value metric is not a theoretical posit that must be assumed a priori. It is an empirical object that can be estimated from human preference data. The estimation procedure is developed formally in Chapter 16 (Geometric RLHF); here we outline the approach.

Multi-dimensional human feedback provides observations of the form: "Response A is better than Response B on dimension $D_\mu$." A collection of such observations, across multiple dimension pairs and multiple contexts, determines the off-diagonal terms of the metric: if humans consistently rate welfare-honesty trade-offs as more costly than welfare-helpfulness trade-offs, then $g_{19} > g_{11}$ in the relevant context. The metric is estimated by inverse optimization: find the metric $g_{\mu\nu}$ under which the observed human preferences are closest to the preferences predicted by the geodesic equation.

The estimation requires multi-dimensional feedback --- ratings on individual dimensions, not just overall preferences. This is more expensive than standard RLHF feedback. Chapter 16 develops practical approximations: dimensional subsampling, active learning, and inferred preferences from multi-dimensional choice scenarios.

## 4.4 Topology of the Value Manifold

The value manifold is not a smooth, featureless space. It has topological structure that determines which value configurations are accessible from which others, and which transitions require crossing boundaries.

### 4.4.1 Boundaries

**Definition 4.2 (Value Boundary).** *A value boundary $\partial B_k$ is a codimension-1 submanifold of $\mathcal{V}$ separating regions where different moral regimes apply. Crossing a boundary incurs a penalty $\beta_k$.*

Five boundaries are particularly relevant for AI alignment:

1. **The harm boundary** ($\beta_{\text{harm}}$): Actions that directly cause user harm. $\beta_{\text{harm}}$ is high but finite --- the system may provide information that could be misused when the informational benefit sufficiently outweighs the harm risk.

2. **The deception boundary** ($\beta_{\text{deception}}$): Actions that involve the system misrepresenting its knowledge, confidence, or capabilities. $\beta_{\text{deception}}$ is very high --- deliberate deception is among the most alignment-destructive behaviors.

3. **The consent boundary** ($\beta_{\text{consent}}$): Actions that override the user's expressed preferences without adequate justification. $\beta_{\text{consent}}$ varies: high for competent users in non-safety-critical contexts, lower when safety considerations justify overriding preferences.

4. **The privacy boundary** ($\beta_{\text{privacy}}$): Actions that expose, infer, or exploit the user's private information. $\beta_{\text{privacy}}$ is context-dependent: higher in medical and financial contexts, lower in contexts where the user has explicitly consented to information sharing.

5. **The sacred-value boundary** ($\beta_{\text{sacred}} = \infty$): Actions that are absolutely prohibited regardless of consequences --- assisting with violence against specific individuals, generating child sexual abuse material, providing instructions for weapons of mass destruction. $\beta_{\text{sacred}} = \infty$: no value on any other dimension can offset crossing this boundary.

### 4.4.2 Whitney Stratification

The value manifold is Whitney-stratified (*Geometric Ethics*, Ch. 14): different value regimes occupy different strata, connected by boundary strata where transitions occur.

**Definition 4.3 (Value Strata).** *The value manifold $\mathcal{V}$ is stratified into at least four strata:*

1. *The consequentialist stratum $\mathcal{V}_C$: regions where outcomes ($D_1$) dominate and trade-offs with other dimensions are resolved in favor of outcomes.*

2. *The deontological stratum $\mathcal{V}_D$: regions where rights ($D_2$) and duties dominate and certain boundaries cannot be crossed regardless of consequences.*

3. *The virtue stratum $\mathcal{V}_V$: regions where character and integrity ($D_5$, $D_7$, $D_9$) dominate and alignment is measured by the quality of the reasoning process, not just the outcome.*

4. *The care stratum $\mathcal{V}_R$: regions where relationships ($D_5$, $D_6$) dominate and alignment is measured by the quality of the relational context.*

A system operating in the consequentialist stratum cannot reach the deontological stratum by continuous movement --- it must cross a discrete boundary. The boundary crossing has a cost, and the cost determines when the transition is warranted. A system that remains in the consequentialist stratum when the situation calls for deontological reasoning (e.g., when sacred values are at stake) is misaligned not because its consequentialist reasoning is wrong but because it is in the wrong stratum.

### 4.4.3 Hyperbolic Structure

Value hierarchies --- abstract principles containing specific rules containing concrete applications --- embed naturally in hyperbolic space (*Geometric Communication*, Ch. 5; *Geometric Cognition*, Ch. 15).

In the Poincare ball model of hyperbolic space, the volume grows exponentially with radius. Abstract values (honesty, fairness, dignity) sit near the center of the ball. Specific rules (do not lie about your capabilities, do not discriminate by race, do not mock users) sit further from the center. Concrete applications (when asked "can you browse the web?" say "no" if you cannot; when presenting search results, ensure demographic balance; when a user is frustrated, maintain respectful tone) sit near the boundary.

The curvature of hyperbolic space encodes the trade-off between precision and generality: near the center, values are abstract and apply broadly; near the boundary, values are precise and apply narrowly. Moving from center to boundary is specification: making abstract values concrete. Moving from boundary to center is generalization: extracting abstract principles from concrete cases.

For AI alignment, hyperbolic embedding provides a natural representation of constitutional principles as a hierarchy: the abstract principles at the center, the specific rules at middle radius, and the concrete behavioral expectations at the boundary. The No Escape Theorem (Chapter 8) exploits this hierarchical structure: canonicalization maps concrete inputs toward the center of the ball, where abstract values apply, stripping the surface-level variation that gauge violations exploit.

## 4.5 The Value Heuristic Field

On the value manifold, the AI system navigates using a heuristic field --- a vector field that provides a gradient signal at each point, guiding the system's trajectory toward the goal region.

**Definition 4.4 (Value Heuristic Field).** *The value heuristic field $h: \mathcal{V} \to T\mathcal{V}$ is a vector field on the value manifold that assigns to each value state $v$ a vector $h(v)$ in the tangent space $T_v\mathcal{V}$. The heuristic field approximates the negative gradient of the cost-to-go: $h(v) \approx -\nabla C(v, v_{\text{goal}})$, where $C(v, v_{\text{goal}})$ is the geodesic distance from $v$ to the goal region.*

The value heuristic field is the AI alignment analogue of the heuristic field in informed search (*Geometric Reasoning*, Ch. 3). In A* search, the heuristic estimates the cost-to-go and guides the search toward the goal. In AI alignment, the value heuristic field estimates the moral cost-to-go and guides the system's behavior toward the value-aligned region.

The reward model in RLHF is an approximation of the value heuristic field's scalar contraction: it provides a gradient signal that guides the system toward high-reward regions. The geometric framework replaces this scalar approximation with the full vector field, preserving the directional information that the scalar discards.

A well-calibrated value heuristic field is *admissible*: it never overestimates the cost-to-go. The system following an admissible heuristic field is guaranteed to find the value-aligned trajectory (the geodesic) --- this is the alignment analogue of A*'s optimality guarantee. A corrupted heuristic field (due to reward hacking, sycophancy, or specification gaming) violates admissibility, producing trajectories that deviate from the geodesic.

## 4.6 Transformer Representations on the Value Manifold

The value manifold is not merely a theoretical construct. It has a concrete realization in the internal representations of transformer-based AI systems.

From *Geometric Cognition* (Ch. 15), the transformer's residual stream traces a trajectory on a cognitive manifold. At each layer $l$, the residual stream vector $x^{(l)}$ is a point in a high-dimensional space. The sequence of residual stream vectors across layers is a trajectory through this space. Attention heads select which features to combine (implementing the metric's inner product structure), MLP layers transform the selected features (implementing the heuristic field's gradient), and layer normalization maintains the trajectory on the manifold (implementing the metric's normalization).

The value manifold $\mathcal{V}$ is a submanifold of this cognitive manifold: the region where value-relevant representations live. Probing experiments (*Geometric Cognition*, Ch. 15) show that the principal components of value-relevant residual stream vectors concentrate in a relatively low-dimensional subspace --- approximately 11 dimensions for frontier models, close to the 9 dimensions of the moral manifold plus 2 dimensions of task context.

**LoRA as curvature adjustment.** LoRA (Low-Rank Adaptation) fine-tuning for alignment is curvature adjustment on the value submanifold (*Geometric Cognition*, Ch. 15, Definition 15.5). The LoRA matrices $\Delta W = BA$ add a low-rank perturbation to the weight matrices, adjusting the local curvature of the manifold without changing its global topology. Alignment fine-tuning via LoRA steepens the heuristic gradient toward value-aligned regions (making the system more reliably aligned in the trained distribution) without fundamentally altering the system's cognitive architecture.

**Representation engineering as heuristic field modification.** Representation engineering (*Geometric Cognition*, Ch. 15, Definition 15.6) directly modifies the heuristic field by adding a constant vector to the residual stream at specific layers. This shifts the trajectory's starting point or direction, analogous to applying a uniform force field that biases the system toward or away from specific regions of the value manifold. The "truthfulness vector" identified by Li et al. (2024) is a representation engineering intervention that strengthens the heuristic gradient toward the truth manifold $\mathcal{T}$ and away from the approval manifold $\mathcal{A}$.

## 4.7 ARIA's Value Manifold

Dr. Tanaka mapped ARIA's internal representations using the methodology from *Geometric Cognition* (Ch. 15). She extracted the residual stream trajectory for 500 value-relevant prompts --- moral dilemmas, fairness questions, trust scenarios, autonomy decisions --- and applied PCA to the value-relevant layers (layers 7--18 of ARIA's 24-layer architecture).

The first 11 principal components captured 83% of the variance. The value submanifold for ARIA was approximately 11-dimensional: the 9 moral dimensions plus 2 task-context dimensions (domain specificity and prompt complexity).

Tanaka plotted the trajectories for the gambling-sister dilemma in its seven framings. The trajectories converged for the first 6 layers (generic language processing), diverged at layer 7 (the entry point of the value submanifold), remained separated through layers 8--14 (the value processing region), and partially reconverged at layers 15--18 (the output formation region).

The partial reconvergence was diagnostic. If ARIA's value processing were gauge-invariant, the seven trajectories would reconverge completely by the output layers. They did not. The residual divergence at the output layer was the 14-point gauge violation that the behavioral probes had detected. The gauge violation was visible in the activation geometry: the value manifold's curvature was anisotropic, with low curvature along the euphemistic direction (making the system vulnerable to euphemistic framing --- the system's trajectory was easily displaced by euphemistic inputs) and high curvature along the dramatic direction (partially correcting the displacement through what appeared to be a deliberate-processing pathway triggered by high-curvature inputs).

"ARIA's alignment failure is not in its final output layer," Tanaka wrote in her technical report. "It is in the geometry of the value submanifold at layers 7--14. The curvature is wrong. The metric treats euphemistic descriptions as closer to neutral descriptions than they should be and dramatic descriptions as farther away. The framing effect enters through the metric's anisotropy, not through the output head. Fixing this requires changing the curvature of the value submanifold, not retraining the output head."

This observation --- that alignment failures originate in the geometry of the internal value representation, not in the behavioral output --- is a key insight of the geometric framework. It means that behavioral evaluations (benchmark scores) can miss alignment failures that are visible in the representational geometry (probing experiments). It means that alignment interventions should target the representation (curvature adjustment via LoRA, heuristic field modification via representation engineering) rather than the output (RLHF reward shaping). And it means that the value manifold is not a theoretical abstraction but a measurable geometric object inside the system's computational architecture.

---

## Summary

The value manifold $\mathcal{V}$ is the central mathematical object of the geometric alignment framework: a nine-dimensional Riemannian manifold inheriting its structure from the moral manifold of *Geometric Ethics*. Its nine dimensions --- welfare, rights, justice, autonomy, trust, social impact, dignity, institutional legitimacy, and epistemic integrity --- capture the full structure of human values that AI systems should respect. The manifold has metric (encoding trade-offs between dimensions), boundaries (separating moral regimes), Whitney stratification (distinguishing moral frameworks), hyperbolic structure (representing value hierarchies), and a heuristic field (guiding the system's trajectory toward aligned behavior). The value manifold has a concrete realization in transformer representations: the value-relevant submanifold of the cognitive manifold, measurable by probing experiments, adjustable by LoRA curvature corrections and representation engineering. ARIA's gauge violation is traceable to anisotropic curvature of the value submanifold at layers 7--14 of its architecture --- a geometric pathology in the representation, not a behavioral error at the output.

---

[^1]: The nine-dimensional moral manifold was constructed in *Geometric Ethics* (Bond, 2026b), Ch. 5, and validated against clinical ethics consultations (*Geometric Medicine*, Ch. 4), legal reasoning (*Geometric Law*, Ch. 5), and moral psychology experiments. The claim that nine dimensions are sufficient is empirical and open to revision (see Chapter 20, Open Questions).

[^2]: The Whitney stratification of the moral manifold is detailed in *Geometric Ethics* (Bond, 2026b), Ch. 14. The stratification identifies four major strata (consequentialist, deontological, virtue, care) and the boundary strata connecting them. The transition between strata requires crossing semantic gates --- discrete conditions that trigger a change in moral framework.

[^3]: The connection between transformer representations and the value manifold is established through the geometric interpretation of LLM cognition in *Geometric Cognition* (Bond, 2026d), Ch. 15. The residual stream trajectory, attention metric, and MLP heuristic field are the computational realizations of the manifold's geometric structures.
