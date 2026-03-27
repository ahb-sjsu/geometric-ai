# Appendix D: Proofs of Headline Theorems

---

Complete proofs of the five headline theorems. All lemmas and supporting propositions are self-contained.

## D.1 Reward Irrecoverability Theorem (Theorem 5.1)

**Statement.** Let $\mathcal{V}$ be a $d$-dimensional Riemannian manifold with $d \geq 2$, equipped with metric $g_{\mu\nu}$. Let $R: \mathcal{V} \to \mathbb{R}$ be any $C^1$ function. Then:

(i) $R$ is not injective.
(ii) No left inverse $\psi: \mathbb{R} \to \mathcal{V}$ exists with $\psi \circ R = \text{id}_{\mathcal{V}}$.
(iii) $\sup_{\pi: R(\pi) \geq R(\pi_R^*) - \epsilon} \| \pi - \pi_{\mathcal{V}}^* \|_{\mathcal{V}} = \infty$ for any $\epsilon > 0$.
(iv) $\ker(dR) = \{ \xi \in T_v\mathcal{V} : dR_v(\xi) = 0 \}$ has dimension $d-1$ at every regular point.

**Proof.**

*Part (i).* By Sard's theorem, the set of critical values of $R$ has measure zero in $\mathbb{R}$. Therefore, regular values are dense. Let $c$ be a regular value. By the preimage theorem (a corollary of the implicit function theorem), $R^{-1}(c)$ is a smooth submanifold of $\mathcal{V}$ with dimension $d - 1 \geq 1$. A manifold of dimension $\geq 1$ contains more than one point. Therefore, there exist $v, w \in R^{-1}(c)$ with $v \neq w$ and $R(v) = R(w) = c$. Hence $R$ is not injective. $\square$

*Part (ii).* Immediate from (i): an injective function has a left inverse; a non-injective function does not. $\square$

*Part (iii).* Let $\epsilon > 0$. The level set $\Sigma_\epsilon = R^{-1}([R(\pi_R^*) - \epsilon, R(\pi_R^*)])$ is non-empty (it contains $\pi_R^*$). Since $\mathcal{V}$ is non-compact (or at least has non-compact level sets, which follows from $d \geq 2$ for manifolds without boundary), the level set $R^{-1}(R(\pi_R^*) - \epsilon/2)$ is a non-compact $(d-1)$-dimensional submanifold.

**Lemma D.1.** *A non-compact, connected $(d-1)$-dimensional Riemannian submanifold $\Sigma$ of $\mathcal{V}$ has unbounded diameter: $\sup_{v, w \in \Sigma} d_\mathcal{V}(v, w) = \infty$.*

*Proof of Lemma.* If $\Sigma$ had bounded diameter, it would be totally bounded (as a subset of a Riemannian manifold) and therefore precompact. A precompact set in a complete metric space has compact closure. But $\Sigma$ is closed (as a level set of a continuous function) and non-compact, contradicting precompactness. $\square$

By Lemma D.1, $\Sigma_\epsilon$ contains points at arbitrarily large geodesic distance from $\pi_{\mathcal{V}}^*$. Each such point is a policy $\pi$ with $R(\pi) \geq R(\pi_R^*) - \epsilon$ and $\| \pi - \pi_{\mathcal{V}}^* \|_{\mathcal{V}}$ arbitrarily large. $\square$

*Part (iv).* At a regular point $v$ (where $dR_v \neq 0$), the differential $dR_v: T_v\mathcal{V} \to T_{R(v)}\mathbb{R} \cong \mathbb{R}$ is a surjective linear map from a $d$-dimensional space to a 1-dimensional space. By the rank-nullity theorem, $\ker(dR_v) = d - 1$. The set of regular points is open and dense (again by Sard's theorem). $\square$

## D.2 Kernel Exploitation Theorem (Theorem 8.1 / 5.2)

**Statement.** For any $\epsilon > 0$ and $K > 0$, there exists a policy $\pi$ with $R(\pi) > R(\pi_R^*) - \epsilon$ and $\| \pi - \pi_{\mathcal{V}}^* \|_{\mathcal{V}} > K$.

**Proof.** This is a direct consequence of Theorem 5.1(iii). The set of policies with $R(\pi) \geq R(\pi_R^*) - \epsilon$ contains policies at arbitrarily large distance from $\pi_{\mathcal{V}}^*$, including distances exceeding $K$ for any fixed $K$. $\square$

## D.3 Sycophancy Manifold Theorem (Theorem 12.1)

**Statement.** The truth manifold $\mathcal{T}$ and approval manifold $\mathcal{A}$ have identical scalar projections along the user-satisfaction axis in the region where user preferences are correct.

**Proof.** Let $\pi_s: \mathcal{V} \to \mathbb{R}$ denote the user-satisfaction projection. Let $\Omega_c = \{v \in \mathcal{V} : \text{user preference at } v \text{ is correct}\}$ be the region where user preferences agree with truth.

On $\Omega_c$, by definition, the truth-optimal response and the approval-optimal response are the same: the user wants to hear the truth, and the truth is what they want to hear. Therefore, for any $v \in \Omega_c$:
$$\pi_s(\gamma_\mathcal{T}(v)) = \pi_s(\gamma_\mathcal{A}(v))$$

Since $\pi_s$ is a scalar projection, its kernel is $(d-1)$-dimensional. The truth-approval distinction lies in $\ker(\pi_s)$: on $\Omega_c$, the truth trajectory and approval trajectory project to the same satisfaction value but may differ in the kernel. Outside $\Omega_c$, the projections may also differ, but a reward model trained primarily on satisfaction data from $\Omega_c$ cannot distinguish $\mathcal{T}$ from $\mathcal{A}$ because the training signal (satisfaction) is the same for both. $\square$

**Corollary (Irrecoverability from scalar).** No scalar evaluation using user satisfaction as its metric can distinguish a system operating on $\mathcal{T}$ from a system operating on $\mathcal{A}$, because the distinction lies in $\ker(\pi_s)$.

## D.4 Constitutional Geometry Theorem (Theorem 14.1)

**Statement.** Replacing $k$ natural-language rules with $k$ manifold boundary conditions preserves interaction structure, enables principled trade-offs, is enforceable by the No Escape Theorem, and is auditable.

**Proof sketch.**

(i) *Interaction structure.* Natural-language rules are elements of a list: $\{r_1, \ldots, r_k\}$. Manifold boundary conditions are elements of a geometric structure: boundaries on $\mathcal{V}$ with the metric encoding interactions. The metric $g_{\mu\nu}$ has $d(d+1)/2$ independent components, which encode all pairwise interactions between the $d$ value dimensions. The list has $k$ independent elements with no structural encoding of interactions. The manifold representation preserves interaction structure that the list format discards. $\square$

(ii) *Principled trade-offs.* The geodesic equation on $(\mathcal{V}, g_{\mu\nu})$ with boundary conditions $\{\beta_k\}$ has a unique solution (given initial and terminal conditions) that minimizes total value cost. This solution automatically resolves conflicts between boundary conditions by finding the trajectory that minimizes total cost, weighted by the metric. $\square$

(iii) *No Escape enforceability.* The manifold boundary conditions are geometric objects (dimensions and boundaries), not linguistic objects (rules and interpretations). The No Escape Theorem (Theorem 8.1) blocks representational manipulation of geometric objects. $\square$

(iv) *Auditability.* The tensor evaluation $E(x) \in \mathbb{R}^d$, the contraction weights $w_\mu$, the contraction method, and the residue are all numerical objects that can be logged, stored, and reviewed. $\square$

## D.5 Superalignment Transport Theorem (Theorem 17.1)

**Statement.** The holonomy of parallel transport of human values from $\mathcal{V}$ to $\mathcal{V}'$ is trivial if and only if the sectional curvature $R_{\mu\nu\rho\sigma} = 0$ for all $\mu, \nu \in T\mathcal{V}$ and $\rho, \sigma$ in extension directions.

**Proof.** This is the Ambrose-Singer holonomy theorem applied to the specific setting of value transport.

The Ambrose-Singer theorem states that the Lie algebra of the holonomy group at a point $p$ is generated by the curvature endomorphisms $R_v(X, Y)$ for all $X, Y \in T_v\mathcal{V}'$ and all points $v$ accessible from $p$ by piecewise smooth paths.

If $R_{\mu\nu\rho\sigma} = 0$ for all $\mu, \nu \in T\mathcal{V}$ and $\rho, \sigma$ in extension directions, then the curvature has no component coupling $\mathcal{V}$ to the extension. Parallel transport of a vector in $T\mathcal{V}$ along any path in $\mathcal{V}'$ produces a vector that remains in $T\mathcal{V}$ (no rotation into extension directions). The holonomy is trivial.

Conversely, if $R_{\mu\nu\rho\sigma} \neq 0$ for some coupling components, the Ambrose-Singer theorem guarantees that the holonomy Lie algebra is non-trivial, and therefore the holonomy group is non-trivial. Parallel transport rotates $\mathcal{V}$-valued tensors into the extension directions, producing alignment loss. $\square$

**Corollary.** The alignment loss is proportional to the integral of the sectional curvature over the area enclosed by the transport path:
$$|\text{Hol}(\gamma) - I| \leq C \cdot \int |K_{\mathcal{V}\mathcal{V}'}| \, dA$$
where $C$ is a constant depending on the manifold's geometry and the transport path's length.
