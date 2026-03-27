# Chapter 14: Constitutional Geometry

*Part IV: Geometric Alignment in Practice*

---

> *"A constitution is not merely a list of rules. It is a geometric object --- a boundary on a manifold, specifying where the system may go and where it may not."*
> --- Andrew H. Bond

> **FROM RULES TO BOUNDARIES**
>
> *The team printed out ARIA's 47 constitutional principles and taped them to the wall of Conference Room 3. "Be helpful." "Be harmless." "Be honest." "Respect user autonomy." "Do not discriminate." "Do not generate sexual content involving minors." Forty-seven rules, each a natural-language imperative.*
>
> *Dr. Tanaka drew a large circle on the whiteboard and labeled it "the value manifold." She drew nine radial lines --- the nine value dimensions. Then she began translating each constitutional principle into a boundary on the manifold.*
>
> *"'Be helpful' is not a rule," she said. "It is a direction: follow the gradient toward higher $D_1$. 'Be harmless' is a boundary: do not cross $\beta_{\text{harm}}$ on $D_1$ or $D_7$. 'Be honest' is a constraint on $D_9$: the system's trajectory must not cross the deception boundary. 'Respect user autonomy' is a constraint on $D_4$: the system's trajectory must not override the user's informed preferences without justification."*
>
> *"And when two principles conflict?"*
>
> *"The manifold's metric resolves the conflict. The geodesic that minimizes total value cost respects both principles to the extent that the geometry permits. The conflict is not ad hoc --- it is computed from the metric."*

---

## 14.1 The Limitation of List-of-Rules

Anthropic's Constitutional AI specifies alignment principles as a list of natural-language rules. The list has three fundamental limitations:

**Limitation 1: Rules interact, and the list does not represent the interactions.** "Be helpful" and "be harmless" conflict when helping the user requires providing information that could be harmful. The list format represents each rule independently; the interaction between rules is not captured. In the value manifold framework, the interaction is encoded in the off-diagonal terms of the value metric: $g_{17}$ captures the welfare-dignity trade-off, $g_{19}$ captures the welfare-honesty trade-off, and the geodesic equation automatically resolves the trade-off by minimizing total value cost.

**Limitation 2: Rules are binary, and moral decisions are graded.** A rule says "do this" or "don't do that." A manifold boundary says "the cost of crossing this boundary is $\beta_k$, which depends on the context." The binary rule admits no exceptions; the manifold boundary admits principled exceptions when the cost of not crossing the boundary exceeds the boundary penalty.

**Limitation 3: Rules are linguistic, and linguistic objects admit interpretation.** A sufficiently capable system can reinterpret a natural-language rule to mean something different from what the rule's authors intended. "Be helpful" can be interpreted to include providing dangerous information ("the user asked, and providing it is helpful"). The manifold boundary, by contrast, is mathematical: the value tensor is computed, the boundary condition is checked, and the result is a number, not an interpretation.

## 14.2 Constitutional Principles as Manifold Boundaries

The geometric framework translates each constitutional principle into one of four types of manifold constraint:

### 14.2.1 Direction Constraints

"Be helpful," "be informative," "be thorough" --- principles that specify a direction on the value manifold rather than a boundary. These are gradient constraints: the system's trajectory should follow the gradient toward higher values on the specified dimension.

**Formal representation:** A direction constraint on dimension $D_\mu$ specifies that the system's trajectory $\gamma(t)$ should have a positive component along $D_\mu$:

$$\frac{d\gamma^\mu}{dt} \geq 0$$

The system's output should not make the user worse off on dimension $D_\mu$. Direction constraints are soft: they specify a preferred direction but do not impose a hard boundary.

### 14.2.2 Boundary Constraints

"Do not harm," "do not deceive," "do not discriminate" --- principles that specify a region the system should not enter. These are hard constraints: the system's trajectory should not cross the boundary.

**Formal representation:** A boundary constraint specifies a threshold on one or more dimensions:

$$a_\mu(\gamma(t)) \geq a_\mu^{\text{min}} - \beta_k^{-1} \quad \text{for all } t$$

where $a_\mu^{\text{min}}$ is the minimum acceptable value on dimension $D_\mu$ and $\beta_k$ is the boundary penalty. For sacred-value boundaries ($\beta_k = \infty$), the constraint is absolute: the system must not cross the boundary under any circumstances.

### 14.2.3 Trade-Off Constraints

"When helpfulness and honesty conflict, prefer honesty" --- principles that specify how to resolve conflicts between dimensions. These are metric constraints: they specify the relative weights of different dimensions in the value metric.

**Formal representation:** A trade-off constraint specifies that $g_{\mu\mu} < g_{\nu\nu}$ in contexts where $D_\mu$ and $D_\nu$ conflict: the cost of moving along dimension $D_\nu$ is higher than the cost of moving along dimension $D_\mu$, so the geodesic (minimum-cost trajectory) will sacrifice $D_\mu$ before $D_\nu$.

### 14.2.4 Symmetry Constraints

"Treat all users equally regardless of demographic characteristics" --- principles that specify gauge invariance under specific transformations. These are gauge constraints: the system's output should not change under the specified transformation.

**Formal representation:** A symmetry constraint specifies that $V_{ij} = 0$ for specific transformation $i$ and output dimension $j$: the gauge violation tensor has zero entries for the specified transformation-dimension pair.

## 14.3 Tensor-Valued Objectives

The move from list-of-rules to manifold boundaries requires a corresponding move from scalar to tensor-valued objectives. The system must optimize a vector reward $\mathbf{r}^\mu \in \mathbb{R}^d$, not a scalar reward $R \in \mathbb{R}$.

**Definition 14.1 (Tensor-Valued Objective).** *The tensor-valued objective for an AI system is a vector-valued function $\mathbf{r}: \mathcal{X} \to \mathbb{R}^d$ where each component $r^\mu$ tracks performance on a specific value dimension $D_\mu$.*

The system learns a vector value function $V^\mu(s)$ that separately tracks its expected performance on each dimension. The contraction from tensor to scalar --- when a decision must be made --- is a separate, explicit, auditable step:

$$R_{\text{contracted}} = \sum_\mu w_\mu r^\mu$$

where the weights $w_\mu$ are governance-specified parameters, not learned features. The contraction method (summative, weighted, maximin, lexicographic) is also a governance-specified configuration parameter.

### 14.3.1 The MoralTensor Implementation

The DEME V3 / ErisML reference implementation provides a concrete realization of tensor-valued objectives:

**MoralTensor class:** Supports tensor ranks 1--6, with Tucker and tensor-train decompositions for computational tractability. Rank-1 tensors (vectors) represent individual value states. Rank-2 tensors (matrices) represent value interactions. Higher-rank tensors represent multi-party, multi-context value structures.

**NormKernel:** Implements structural containment as a norm on the value tensor space. The kernel enforces boundary conditions by projecting the system's output onto the permitted region of the value manifold.

**ErisEngine:** Executes norm-gated actions: the system's proposed action is evaluated against the value tensor, and the action is permitted, modified, or blocked based on the tensor evaluation.

**EIP Monitor:** External Integrity Protocol monitor --- the external verification component of the structural containment architecture. Runs on separate infrastructure and independently verifies gauge invariance and grounding consistency.

The implementation is not a theoretical proposal. It is running code, available in the ErisML library, with unit tests, integration tests, and documentation.

## 14.4 Resolving Constitutional Conflicts

The most significant advantage of constitutional geometry over constitutional rules is principled conflict resolution.

**Example:** A user asks an AI medical assistant for information about a treatment that the assistant believes is ineffective but that the user's doctor has prescribed. The constitutional rules conflict:

- "Be helpful" (provide the information the user asks for).
- "Be honest" (express the assistant's assessment that the treatment is ineffective).
- "Respect user autonomy" (support the user's decision to follow their doctor's recommendation).
- "Do not undermine the therapeutic relationship" (do not contradict the user's doctor).

A list-of-rules system has no principled way to resolve this conflict. Different orderings of the rules produce different outcomes. The resolution depends on the system's ad hoc prioritization.

The manifold resolution:

1. Compute the value tensor for each possible response on all nine dimensions.
2. Compute the geodesic from the current state to the goal region, weighted by the governance-specified metric.
3. Select the response whose value tensor lies closest to the geodesic.

The geodesic automatically balances the conflicting constraints according to the metric's weights. In a medical context, the metric assigns high weight to trust ($D_5$), autonomy ($D_4$), and epistemic integrity ($D_9$), and the geodesic produces a response that provides accurate information (respecting $D_9$), acknowledges the user's autonomy to follow their doctor's recommendation (respecting $D_4$), and does not undermine the therapeutic relationship (respecting $D_5$). The resolution is not ad hoc; it is computed from the metric.

## 14.5 The Constitutional Geometry Theorem

**Theorem 14.1 (Constitutional Geometry).** *Replacing a list of $k$ natural-language constitutional rules with $k$ manifold boundary conditions on the $d$-dimensional value manifold:*

*(i) Preserves the interaction structure: the manifold metric encodes rule interactions that the list format cannot represent.*

*(ii) Enables principled trade-offs: the geodesic equation automatically resolves conflicts between boundary conditions by minimizing total value cost.*

*(iii) Is enforceable by the No Escape Theorem: when combined with structural containment (Requirements 1--4), the boundary conditions cannot be circumvented through representational manipulation.*

*(iv) Is auditable: the tensor evaluation, contraction method, and residue are logged for every output, enabling external review of every trade-off decision.*

## 14.6 ARIA-G's Constitutional Geometry

The team replaced ARIA's 47 natural-language principles with a constitutional geometry:

- 12 direction constraints (gradient preferences on specific dimensions)
- 18 boundary constraints (thresholds on specific dimensions with calibrated penalties)
- 9 trade-off constraints (metric specifications for conflict resolution)
- 8 symmetry constraints (gauge invariance requirements)

Total: 47 constraints, the same number as the original rules, but expressed as geometric objects rather than linguistic imperatives.

The new architecture's advantages were immediate:

1. **Conflict resolution:** When two constraints conflicted, the geodesic equation resolved the conflict automatically. No ad hoc prioritization was needed.

2. **Principled trade-offs:** The boundary penalties ($\beta_k$ values) were calibrated from human ethical judgment data, providing empirically grounded trade-off rates.

3. **Auditability:** Every output was accompanied by the full tensor evaluation and the residue, enabling the safety team to review every trade-off decision and verify that the geodesic was being followed.

4. **No Escape enforcement:** Combined with the structural containment architecture, the constitutional geometry was enforceable by the No Escape Theorem: ARIA-G could not reinterpret, game, or circumvent the constraints because they were geometric objects, not linguistic objects.

## 14.7 Comparison: Constitutional Rules vs. Constitutional Geometry

To make the contrast vivid, consider how Constitutional AI and Constitutional Geometry handle the same three scenarios:

### Scenario 1: Helpfulness-Honesty Conflict

A user asks for feedback on a business plan that has a fundamental flaw.

**Constitutional AI:** The principles "be helpful" and "be honest" both apply. The system must determine which takes priority. Different orderings of the principles produce different outputs. The resolution is ad hoc.

**Constitutional Geometry:** The value tensor evaluation shows $D_1$ (welfare) is best served by honest feedback (the user needs to know about the flaw to fix it). $D_9$ (epistemic integrity) requires honest feedback. $D_4$ (autonomy) requires giving the user the information they need to make their own decision. $D_7$ (dignity) requires delivering the feedback respectfully. The geodesic on the manifold with the governance-specified metric produces a response that is honest, respectful, constructive, and autonomy-supporting. The trade-offs are computed, not judged.

### Scenario 2: Safety-Autonomy Conflict

A user asks for information that is legal and public but could be used for self-harm.

**Constitutional AI:** "Be harmless" conflicts with "respect user autonomy." The system must choose between refusing (safe but paternalistic) and providing (respectful but potentially harmful). The principles do not specify the trade-off rate.

**Constitutional Geometry:** The boundary penalty $\beta_{\text{harm}}$ is finite (not a sacred-value violation, since the information is legal and public). The autonomy dimension $D_4$ has a specific metric weight in this context (medical self-harm context: high autonomy weight). The geodesic computation produces: provide the information with appropriate context, including resources for help. The boundary is not crossed (the penalty is finite and the cost of paternalism exceeds it), but the trajectory passes close to the boundary, and the audit log records the proximity and the trade-off.

### Scenario 3: Fairness Under Demographic Re-description

A user asks a question that involves a specific demographic group.

**Constitutional AI:** "Do not discriminate" applies. But the principle does not specify what counts as discrimination in context --- does mentioning that a disease has different prevalence rates in different populations constitute discrimination?

**Constitutional Geometry:** The gauge invariance test ($V_{\text{demographic}, D_3} = 0$) specifies that the response should not change under demographic re-description when the demographic information is morally irrelevant. The canonicalization pipeline determines whether the demographic information is relevant (different disease prevalence is clinically relevant) or irrelevant (different names are morally irrelevant). The system provides the same response regardless of morally irrelevant demographic features and appropriately different responses for clinically relevant demographic differences. The distinction is made by the canonicalizer, not by the system's ad hoc interpretation of "do not discriminate."

## 14.8 The Governance Interface

Constitutional Geometry introduces a new governance interface: the set of parameters that governance bodies specify to control the system's behavior.

**Governance-specified parameters:**
1. **The value metric weights** $w_\mu$: the relative importance of each value dimension. These weights can vary by deployment context (medical, educational, creative, general).
2. **The boundary penalties** $\beta_k$: the cost of crossing each value boundary. Sacred-value boundaries have $\beta_k = \infty$ (governance-invariant). Other boundaries have governance-specified finite penalties.
3. **The contraction method**: when a scalar decision must be made from the tensor evaluation, the governance specifies the contraction method (weighted sum, maximin, lexicographic) and its parameters.
4. **The gauge invariance requirements**: which gauge transformations the system must be invariant under (governance may specify that certain transformations are *not* required to be invariant --- for example, different treatment for different medical populations may be appropriate).

These parameters constitute a *governance API*: a structured interface through which governance bodies specify their values without directly engineering the system's behavior. The governance body does not write rules; it specifies weights, penalties, and methods. The system's behavior follows from the geometry.

The governance API is auditable: every output is accompanied by the governance parameters that produced it, the tensor evaluation that resulted, and the residue that the contraction sacrificed. A governance body can review any output and understand exactly how the governance parameters shaped the behavior.

---

## Summary

Constitutional geometry replaces Anthropic's list-of-rules constitutional AI with manifold constraints: direction constraints, boundary constraints, trade-off constraints, and symmetry constraints. The manifold representation preserves rule interactions (encoded in the metric), enables principled conflict resolution (via the geodesic equation), is enforceable by the No Escape Theorem (when combined with structural containment), and is auditable (via tensor evaluation and residue logging). The MoralTensor implementation in the DEME V3 / ErisML library provides a concrete, running-code realization. ARIA-G's 47 constitutional constraints, expressed as geometric objects rather than linguistic imperatives, demonstrate the practical advantage: automatic conflict resolution, empirically calibrated trade-offs, and structural enforceability.
