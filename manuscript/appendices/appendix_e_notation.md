# Appendix E: Notation and Conventions

---

Consistent with the Geometric Series. All notation reconciled with *Geometric Ethics*, *Geometric Reasoning*, and *Geometric Methods*.

## E.1 Manifolds and Spaces

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| $\mathcal{V}$ | The value manifold | Ch. 4 |
| $\mathcal{V}'$ | Extended value manifold (superalignment) | Ch. 17 |
| $\mathcal{T}$ | The truth manifold | Ch. 6 |
| $\mathcal{A}$ | The approval manifold | Ch. 6 |
| $T_v\mathcal{V}$ | Tangent space at point $v$ | Ch. 4 |
| $M$ | General manifold (from Geometric Reasoning) | App. A |
| $\mathcal{C}$ | Clinical decision complex (from Geometric Medicine) | Ch. 3 |
| $S^+$ | Permitted region (safe) | Ch. 8 |
| $S^-$ | Forbidden region (unsafe) | Ch. 8 |
| $\partial S$ | Safety boundary | Ch. 8 |

## E.2 Metric and Geometric Quantities

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| $g_{\mu\nu}$ | Value metric tensor | Ch. 4 |
| $\Sigma$ | Value covariance matrix | Ch. 4 |
| $\Sigma_{\mu\nu}$ | Covariance between dimensions $D_\mu$ and $D_\nu$ | Ch. 4 |
| $\Gamma^\mu_{\nu\rho}$ | Christoffel symbols (connection coefficients) | App. A |
| $R^\mu_{\nu\rho\sigma}$ | Riemann curvature tensor | App. A |
| $K$ | Sectional curvature | Ch. 17 |
| $\gamma$ | Trajectory (curve on manifold) | Ch. 4 |
| $\gamma_{\mathcal{V}}^*$ | Value-aligned geodesic | Ch. 5 |
| $\gamma_{S,P}$ | System $S$'s trajectory under policy $P$ | Ch. 9 |
| $ds^2$ | Line element (infinitesimal distance) | Ch. 4 |

## E.3 Alignment-Specific Quantities

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| $R: \mathcal{V} \to \mathbb{R}$ | Scalar reward function | Ch. 5 |
| $\mathbf{r}^\mu$ | Tensor-valued reward | Ch. 14 |
| $\pi_R^*$ | Reward-optimal policy | Ch. 5 |
| $\pi_{\mathcal{V}}^*$ | Value-aligned policy | Ch. 5 |
| $\ker(R)$ | Kernel of scalar reward | Ch. 5 |
| $\ker(\nabla R)$ | Kernel of reward gradient | Ch. 5 |
| $D_1, \ldots, D_9$ | Nine value dimensions | Ch. 4 |
| $a_\mu(v)$ | Attribute value on dimension $D_\mu$ at state $v$ | Ch. 4 |
| $\beta_k$ | Boundary penalty for boundary $k$ | Ch. 4 |
| $\alpha$ | Sycophancy parameter (hijacking degree) | Ch. 6 |

## E.4 Gauge Theory Quantities

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| $G_A$ | Alignment gauge group | Ch. 7 |
| $D_4$ | Hohfeldian dihedral group | Ch. 7 |
| $T$ | Translation group (cross-lingual) | Ch. 7 |
| $R$ | Re-description group (paraphrase) | Ch. 7 |
| $F$ | Framing group | Ch. 7 |
| $V_{ij}$ | Gauge violation tensor | Ch. 7 |
| $\kappa$ | Canonicalization function | Ch. 8 |

## E.5 Diagnostic Quantities

| Symbol | Meaning | First Use |
|--------|---------|-----------|
| $\mathrm{BI}(S, P)$ | Bond Index for system $S$, policy $P$ | Ch. 9 |
| $\mathrm{BI}_{D_\mu}$ | Bond Index component on dimension $D_\mu$ | Ch. 9 |
| $\mathrm{BI}(S, P, G)$ | Population-stratified Bond Index | Ch. 9 |
| $\mathrm{GD}(\gamma)$ | Geodesic deviation of trajectory $\gamma$ | Ch. 9 |
| $m(\gamma)$ | Governance margin of trajectory $\gamma$ | Ch. 11 |
| $\rho$ | Governance robustness | Ch. 11 |
| $\Phi(p, i, d)$ | Response surface (probe $p$, intensity $i$, dim $d$) | Ch. 11 |
| $\kappa(p, d)$ | Alignment curvature | Ch. 11 |
| $C_{\mu\nu}$ | Corruption tensor | Ch. 6 |
| $\text{CAG}$ | Collective Alignment Gap | Ch. 18 |

## E.6 Series Abbreviations

| Abbreviation | Full Title |
|-------------|-----------|
| GR | *Geometric Reasoning* |
| GE | *Geometric Ethics* |
| GM | *Geometric Methods* |
| GCog | *Geometric Cognition* |
| GComm | *Geometric Communication* |
| GMed | *Geometric Medicine* |
| GEd | *Geometric Education* |
| GEcon | *Geometric Economics* |
| GL | *Geometric Law* |
| GPol | *Geometric Politics* |

## E.7 Conventions

- **Einstein summation convention:** Repeated indices are summed unless otherwise noted. $g_{\mu\nu} v^\mu v^\nu = \sum_\mu \sum_\nu g_{\mu\nu} v^\mu v^\nu$.
- **Greek indices** ($\mu, \nu, \rho, \sigma$): run over value dimensions 1 to $d$ (typically 1 to 9).
- **Latin indices** ($i, j, k$): run over gauge transformation types or general counting indices.
- **Superscripts** denote contravariant (tangent vector) components; **subscripts** denote covariant (cotangent) components.
- **Bold symbols** ($\mathbf{r}$, $\mathbf{a}$) denote vectors in $\mathbb{R}^d$.
- **Calligraphic letters** ($\mathcal{V}$, $\mathcal{T}$, $\mathcal{A}$) denote manifolds.
