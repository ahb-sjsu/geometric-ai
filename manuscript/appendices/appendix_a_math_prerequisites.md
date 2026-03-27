# Appendix A: Mathematical Prerequisites

---

This appendix provides the mathematical background needed to follow the formal arguments in this book. It is self-contained for a reader with undergraduate linear algebra, basic real analysis, and familiarity with optimization. For complete treatments, see *Geometric Methods for Complex Systems* (Bond, 2026a) and *Geometric Reasoning* (Bond, 2026c).

## A.1 Riemannian Geometry

### A.1.1 Manifolds

A *smooth manifold* $M$ of dimension $d$ is a topological space that is locally homeomorphic to $\mathbb{R}^d$. Every point $p \in M$ has a neighborhood that looks like an open subset of $\mathbb{R}^d$, with smooth transition maps between overlapping neighborhoods. The key idea: a manifold is globally curved but locally flat.

For AI alignment, the value manifold $\mathcal{V}$ is a 9-dimensional smooth manifold. Each point represents a value state --- a configuration of nine value dimensions. The manifold is not $\mathbb{R}^9$ because it has curvature, boundaries, and non-trivial topology.

### A.1.2 Tangent Spaces and Vectors

The *tangent space* $T_pM$ at a point $p \in M$ is the vector space of all directions in which one can move from $p$. It has the same dimension as $M$. A *tangent vector* $v \in T_pM$ represents an infinitesimal displacement from $p$.

For AI alignment, a tangent vector at a point on the value manifold represents an infinitesimal change in the value state --- a small adjustment in one or more value dimensions.

### A.1.3 The Metric Tensor

A *Riemannian metric* $g$ assigns to each point $p \in M$ a symmetric, positive-definite bilinear form $g_p: T_pM \times T_pM \to \mathbb{R}$. In local coordinates, $g$ is represented by a $d \times d$ matrix $g_{\mu\nu}(p)$.

The metric defines:
- **Distance:** The length of a curve $\gamma: [a,b] \to M$ is $L(\gamma) = \int_a^b \sqrt{g_{\mu\nu}(\gamma(t)) \dot{\gamma}^\mu(t) \dot{\gamma}^\nu(t)} \, dt$.
- **Angle:** The angle between tangent vectors $u, v \in T_pM$ is $\cos\theta = g_p(u,v) / (|u| \cdot |v|)$.
- **Inner product:** $\langle u, v \rangle_g = g_{\mu\nu} u^\mu v^\nu$.

For AI alignment, the value metric $g_{\mu\nu}$ encodes the cost of changing value states. The off-diagonal terms encode trade-offs between dimensions.

### A.1.4 Geodesics

A *geodesic* is a curve that locally minimizes length. It is the manifold analogue of a straight line. Geodesics satisfy the geodesic equation:

$$\frac{d^2\gamma^\mu}{dt^2} + \Gamma^\mu_{\nu\rho} \frac{d\gamma^\nu}{dt} \frac{d\gamma^\rho}{dt} = 0$$

where $\Gamma^\mu_{\nu\rho}$ are the Christoffel symbols, computed from the metric:

$$\Gamma^\mu_{\nu\rho} = \frac{1}{2} g^{\mu\sigma} \left( \frac{\partial g_{\sigma\nu}}{\partial x^\rho} + \frac{\partial g_{\sigma\rho}}{\partial x^\nu} - \frac{\partial g_{\nu\rho}}{\partial x^\sigma} \right)$$

For AI alignment, the value geodesic is the minimum-cost trajectory between two value states --- the aligned behavior that satisfies all value constraints at minimum total moral cost.

### A.1.5 Curvature

The *Riemann curvature tensor* $R^\mu_{\nu\rho\sigma}$ measures the manifold's intrinsic curvature: how much parallel transport around a closed loop rotates a vector. Non-zero curvature means the manifold is not flat --- the geometry varies from point to point.

The *sectional curvature* $K(\Pi)$ in a 2-plane $\Pi \subset T_pM$ is the Gaussian curvature of the surface obtained by shooting geodesics in the directions of $\Pi$. Positive sectional curvature means geodesics converge; negative means they diverge.

For AI alignment, curvature encodes context-dependence: the cost of a value trade-off depends on where you are on the manifold.

### A.1.6 Parallel Transport and Holonomy

*Parallel transport* carries a tangent vector along a curve while keeping it "as constant as possible" relative to the manifold's geometry. On a flat manifold, parallel transport preserves the vector exactly. On a curved manifold, the vector rotates during transport.

The *holonomy* of a closed loop is the total rotation accumulated by parallel transport around the loop:

$$\text{Hol}(\gamma) = \mathcal{P} \exp\left(-\oint_\gamma \Gamma^\mu_{\nu\rho} d\gamma^\rho\right)$$

Holonomy is zero on flat manifolds and non-zero on curved manifolds. For AI alignment, holonomy measures the alignment loss from transporting human values to an AI's extended value space (Chapter 17).

## A.2 Gauge Theory

### A.2.1 Fiber Bundles

A *fiber bundle* $(E, B, \pi, F)$ consists of a total space $E$, a base space $B$, a projection $\pi: E \to B$, and a fiber $F$. Above each point $b \in B$, there is a copy of $F$: the set $\pi^{-1}(b) \cong F$.

For AI alignment, the base space is the moral content (what is being evaluated), the fiber is the set of descriptions (how it is described), and the total space is the set of described moral situations.

### A.2.2 Gauge Groups and Gauge Invariance

A *gauge group* $G$ acts on the fibers of a fiber bundle: it transforms descriptions while preserving content. *Gauge invariance* means that a function defined on the total space depends only on the base-space component --- it is independent of the fiber component.

For AI alignment, the gauge group $G_A = D_4 \times T \times R \times F$ (Chapter 7) acts on descriptions of moral situations. Gauge invariance means the system's output depends on moral content, not on the description.

### A.2.3 The Gauge Violation Tensor

The *gauge violation tensor* $V_{ij}$ measures the failure of gauge invariance: the magnitude of the output change under gauge transformation $i$ on output dimension $j$. Perfect gauge invariance: $V_{ij} = 0$ for all $i, j$. Gauge violation: $V_{ij} > 0$ for some $i, j$.

## A.3 The Mahalanobis Distance

The *Mahalanobis distance* between points $x$ and $y$ with respect to a covariance matrix $\Sigma$ is:

$$d_M(x, y) = \sqrt{(x-y)^T \Sigma^{-1} (x-y)}$$

It generalizes Euclidean distance by accounting for correlations between dimensions and different dimensional scales. The Mahalanobis distance is the natural distance on a manifold with metric $g_{\mu\nu} = \Sigma^{-1}_{\mu\nu}$.

## A.4 Simplicial Complexes

A *simplicial complex* is a collection of simplices (points, edges, triangles, tetrahedra, ...) satisfying closure and intersection properties. It is a discrete analogue of a manifold, useful when the space has discontinuities that a smooth manifold cannot represent.

For AI alignment, the value manifold's boundary structure (Section 4.4) is most naturally represented as a simplicial complex: the boundaries are discrete transitions between moral regimes, not smooth interpolations.

## A.5 A* Search and Heuristic Fields

The *A* algorithm* finds the shortest path in a graph using a heuristic function $h(x)$ that estimates the cost-to-go from state $x$ to the goal. The heuristic is *admissible* if it never overestimates the true cost-to-go: $h(x) \leq h^*(x)$ for all $x$. An admissible heuristic guarantees that A* finds the optimal path.

The *heuristic field* generalizes the heuristic function to continuous manifolds: $h: M \to TM$ is a vector field that provides a gradient signal at each point, guiding trajectories toward the goal. The value heuristic field (Definition 4.4) is the alignment analogue: it guides the system's trajectory toward the value-aligned region of the manifold.

## A.6 Hyperbolic Geometry

*Hyperbolic space* is the unique simply connected Riemannian manifold with constant negative sectional curvature. In the Poincare ball model, hyperbolic space is the open unit ball $\mathbb{B}^d = \{x \in \mathbb{R}^d : |x| < 1\}$ with metric:

$$ds^2 = \frac{4}{(1 - |x|^2)^2} |dx|^2$$

The volume of a ball of radius $r$ grows exponentially with $r$ (unlike Euclidean space, where it grows polynomially). This makes hyperbolic space ideal for embedding hierarchical structures: the exponential volume growth matches the exponential branching of trees.

For AI alignment, hyperbolic embeddings represent value hierarchies: abstract principles near the origin, specific rules at middle radius, concrete applications near the boundary (Section 4.4.3).

---

## References for Further Reading

- do Carmo, M. P. (1992). *Riemannian Geometry*. Birkhauser.
- Nakahara, M. (2003). *Geometry, Topology and Physics*. CRC Press.
- Bond, A. H. (2026a). *Geometric Methods for Complex Systems*. [Series reference.]
- Bond, A. H. (2026c). *Geometric Reasoning*. [Series reference.]
