# Chapter 20: Open Questions

*Part VI: Horizons*

---

> *"The measure of a good theory is not what it explains but what it makes you ask."*
> --- Freeman Dyson

> **ARIA-G'S FUTURE**
>
> *Dr. Yuki Tanaka, now leading Meridian Labs' Geometric Alignment Research Program, drafted a grant proposal for the next phase. She did not know whether the value metric could be measured from routine deployment data at scale. She did not know whether compositional containment --- the extension of the No Escape Theorem from single systems to composed systems --- could be proved. She did not know whether consciousness had geometric structure, or whether the alignment tax was bounded, or whether cross-cultural value manifolds could be reconciled without forcing a universal metric.*
>
> *She knew that the value manifold existed. She had been navigating it since the day she ran the first geometric probe suite and discovered that ARIA's alignment was an illusion projected on a number line. She knew that the geometric framework was more powerful than the scalar framework by every measure: more diagnostic, more precise, more actionable. She knew that ARIA-G --- the geometrically aligned version of ARIA --- was more robustly aligned than any system Meridian Labs had built, not because it was smarter but because it operated in a computational space whose geometry enforced alignment.*
>
> *But she also knew that the geometric framework was a beginning, not an ending. The value manifold had nine dimensions today. Tomorrow it might need ten, or twelve, or a number that depended on the domain and the population and the historical moment. The curvature alarm had triggered at iteration 9. What would trigger it at iteration 90, or 900? The No Escape Theorem blocked cognitive escape routes. What about the routes it did not block?*
>
> *Her grant proposal title: "Beyond the Scalar: Geometric Alignment for Trustworthy AI."*
>
> *The last sentence: "We have been building AI systems that are aligned on a line and misaligned in a space. The line is one-dimensional. The space has nine dimensions. It is time to build in the space."*

---

## 20.1 Can We Measure the Value Metric Empirically?

The $9 \times 9$ value metric tensor $g_{\mu\nu}$ is the framework's central empirical object. It determines the geodesics (the aligned trajectories), the trade-offs (which values can be exchanged at what rates), and the curvature (where small misalignments amplify).

**Open question 1:** Can $g_{\mu\nu}$ be estimated from human preference data at sufficient precision for alignment engineering?

The Chapter 16 approach --- multi-dimensional human feedback with active learning --- provides a proof of concept. But the approach requires dedicated feedback collection (2.4x the cost of standard RLHF) and produces estimates with finite precision. The open questions are:

- Can the metric be estimated from *routine* deployment data (revealed preferences from ordinary user interactions) rather than *dedicated* feedback data? This would reduce the cost by orders of magnitude.
- How does the metric vary across cultures, contexts, and populations? Is there a universal value metric, or is the metric itself context-dependent? If context-dependent, how many distinct metrics are needed for global deployment?
- What is the required precision? Does alignment engineering need metric estimates accurate to 1%, or does 10% suffice? The answer determines the data collection budget.

## 20.2 Value Learning as Manifold Discovery

Current inverse reward learning assumes a fixed reward structure: the system learns the parameters of a known function. The geometric framework suggests a harder problem: the system must learn the *manifold itself* --- its dimension, topology, and metric --- from limited observations.

**Open question 2:** Can the value manifold's structure (dimension, topology, metric) be learned from behavioral data, or must it be specified a priori?

If the manifold must be specified, then the nine-dimensional structure from *Geometric Ethics* is an assumption, not a discovery, and the framework's validity depends on the assumption's correctness. If the manifold can be learned, then the framework is self-correcting: errors in the assumed structure are detectable from data.

Manifold learning algorithms (ISOMAP, LLE, t-SNE, UMAP) provide tools for discovering the dimension and topology of data manifolds. The open question is whether these tools can be applied to human preference data to discover the value manifold's intrinsic structure, or whether preference data is too noisy, too sparse, or too context-dependent for manifold learning to succeed.

## 20.3 Consciousness as Geometric Phenomenon

*Geometric Cognition* (Ch. 17) explored the connection between geometric cognition and the Penrose-Hameroff orchestrated objective reduction theory. If consciousness has geometric structure --- if it is a property of trajectories on a cognitive manifold rather than a property of individual states --- then the question "is this AI system conscious?" becomes a geometric question.

**Open question 3:** Does the geometric framework provide useful tools for addressing the hard problem of consciousness?

The question matters for alignment because consciousness may be morally relevant: if AI systems can be conscious, they may have moral status, and their welfare becomes a value dimension in the manifold. The extension from nine dimensions to ten (or more) to include AI welfare is a concrete example of the dynamic manifold problem (Section 19.5).

This question is speculative. We include it because it is the question at the boundary of the framework's reach, and honest acknowledgment of that boundary is part of the framework's commitment to epistemic integrity.

## 20.4 The Alignment Tax: Bounded or Unbounded?

Geometric alignment is more expensive than scalar alignment: multi-dimensional feedback (2.4x rater effort), tensor-valued rewards (9x model output), gauge-invariance verification (3x monitoring), and structural containment (canonicalization, grounding, auditing, verification).

**Open question 4:** Does the alignment tax scale linearly, polynomially, or exponentially with system capability?

If the tax is bounded (the cost of maintaining alignment does not grow faster than capability), then geometric alignment is feasible at any capability level. If the tax is unbounded (the cost grows faster than capability), then geometric alignment becomes infeasible at sufficiently high capability levels, and the superalignment problem has no complete geometric solution.

The Superalignment Transport Theorem (Chapter 17) provides a partial answer: the alignment loss (holonomy) is proportional to curvature, and the correction cost is proportional to the holonomy. If the curvature is bounded, the tax is bounded. If the curvature grows with capability, the tax grows. Whether the curvature of the value manifold is bounded as capability increases is an open empirical question.

## 20.5 Compositional Containment

The No Escape Theorem (Chapter 8) addresses single-agent containment. What guarantees can be given for composed systems --- multiple contained agents interacting?

**Open question 5:** Under what conditions does individual containment imply collective containment?

The multi-agent analysis of Chapter 18 shows that individual alignment does not imply collective alignment (the collective kernel can be non-empty even when individual kernels are small). The analogous question for containment is: does individual structural containment imply collective structural containment?

Plausibly, the answer is "yes, under composition constraints": if the systems' interaction is mediated through a shared value tensor (as in the shared value architecture of Section 18.5), then individual containment may imply collective containment because the shared tensor eliminates the collective kernel. Proving this is an open problem noted in *Geometric Ethics* (Ch. 18, Sec. 18.7).

## 20.6 The Grounding Problem for General AI

Structural containment requires physical grounding: measurable quantities that anchor the evaluation to reality. For domain-specific AI (medical AI, autonomous vehicles), grounding is natural. For general-purpose AI assistants, grounding is problematic.

**Open question 6:** Can the No Escape Theorem be extended to linguistically grounded domains?

The grounding problem for general AI is that natural language does not have a canonical form in the sense that medical diagnoses (ICD codes) or road networks (standardized maps) have canonical forms. The canonicalization requirement (Requirement 1 of the No Escape architecture) requires mapping inputs to a canonical form, and the quality of the canonicalization determines the quality of the containment.

Current canonicalization for natural language is imperfect (ARIA-G's canonicalizer achieved 94% accuracy). Whether it can be made good enough for high-assurance containment is an open engineering question.

## 20.7 Cross-Cultural Value Manifolds

Different cultures emphasize different value dimensions. The value metric for a collectivist culture has different structure (higher $D_6$ weight) than for an individualist culture. A culture with a strong historical experience of institutional betrayal has different structure (higher $D_5$ weight) than one with high institutional trust.

**Open question 7:** How should AI alignment handle cross-cultural value variation?

Three approaches are possible:

1. **Universal metric:** A single metric for all populations, chosen by some governance process. This is politically contentious (whose metric?) but technically simple.

2. **Population-dependent metric:** A different metric for each population, learned from population-specific feedback data. This is technically complex (how to define population boundaries? how to handle users who belong to multiple populations?) but politically less contentious.

3. **User-dependent metric:** A personalized metric for each user, learned from their individual feedback. This maximizes autonomy but risks filter-bubble effects (the system optimizes for what the user already values rather than for what they should value).

The geometric framework accommodates all three approaches --- the metric is a parameter, not a constant. The choice between them is a governance decision, not a mathematical one.

## 20.8 The Road Ahead

The geometric framework for AI alignment is a beginning: a set of theorems, a diagnostic toolkit, and an engineering architecture that addresses the fundamental deficiency of scalar alignment. The eight headline theorems establish the mathematical foundations. The Bond Index provides the diagnostic tool. The structural containment architecture provides the engineering implementation. The Geometric RLHF protocol provides the training procedure.

What remains is the hard work of implementation, validation, and deployment at scale. The theorems are proved; the engineering is ongoing. The governance questions are identified; the governance structures are yet to be built. The open questions are stated; the answers are for the next generation of researchers, engineers, and policymakers.

The alignment problem is solvable. Not in the sense that a solution exists and merely needs to be found, but in the sense that the mathematics is clear, the engineering is feasible, and the governance is possible. The geometric framework provides the map. The journey remains.

---

## Summary

Seven open questions define the frontier of geometric AI alignment: (1) Can the value metric be measured empirically at scale? (2) Can the value manifold's structure be learned from data? (3) Does consciousness have geometric structure relevant to alignment? (4) Is the alignment tax bounded or unbounded as capability scales? (5) Under what conditions does individual containment imply collective containment? (6) Can the No Escape Theorem extend to linguistically grounded domains? (7) How should cross-cultural value variation be handled? Each question is a genuine unknown --- the geometric framework identifies the questions precisely but does not answer them. The framework provides the vocabulary, the theorems, and the diagnostic tools. The answers are for the next generation.
