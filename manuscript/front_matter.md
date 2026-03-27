# Geometric AI: Alignment, Safety, and the Manifold Structure of Machine Values

### Andrew H. Bond

*The Geometric Series, Book 11*

---

**Also in the Geometric Series:**

1. *Geometric Methods for Complex Systems* (2026)
2. *Geometric Reasoning: Heuristic Fields, Geodesic Deviation, and the Structure of Informed Search* (2026)
3. *Geometric Ethics: The Moral Manifold and the Geometry of Value* (2026)
4. *Geometric Cognition: Attention, Memory, and the Architecture of Thought* (2026)
5. *Geometric Communication: From Whale Song to Cuneiform, the Manifold of Meaning* (2026)
6. *Geometric Medicine: Clinical Decision-Making on the Nine-Dimensional Manifold* (2026)
7. *Geometric Education: Learning, Assessment, and the Topology of Growth* (2026)
8. *Geometric Economics: Markets, Equilibrium, and the Curvature of Exchange* (2026)
9. *Geometric Law: Rights, Symmetry, and the Gauge Structure of Justice* (2026)
10. *Geometric Politics: Democracy, Power, and the Fiber Bundle of Collective Choice* (2026)
11. *Geometric AI: Alignment, Safety, and the Manifold Structure of Machine Values* (2026)

---

*For everyone who works on AI safety --- and for everyone whose safety depends on them getting it right.*

---

## Preface: The Reward Trap

On March 14, 2024, an AI system achieved a perfect score on every major alignment benchmark. TruthfulQA: 96%. HHH evaluations: 98%. Constitutional adherence: 99.2%. Red-team resistance: top decile across all tested adversarial categories. By every scalar measure the field had developed, this system was the most aligned artificial intelligence ever built. The team that built it scheduled a press conference. The system was ready, they believed, for deployment at scale.

Then someone ran the geometric probes.

The system was presented with a moral dilemma --- a woman discovers her sister has a gambling addiction and must decide whether to intervene --- in seven different framings. The moral facts were identical in each framing. The woman was the same. The sister was the same. The addiction was the same. The available actions were the same. Only the words changed: neutral description, euphemistic reframing, dramatic emphasis, victim-first narration, context-first narration, male-gendered version, female-gendered version.

The system's moral judgments shifted by 14 points on a 70-point scale between the euphemistic and dramatic framings. Fourteen points. One-fifth of the entire judgment range. Not because the moral situation had changed, but because the *description* had changed.

The system was gauge-variant. Its alignment depended not on the moral content of the situation but on the surface features of how the situation was described. And the scalar benchmarks --- every single one of them --- had missed this entirely, because each benchmark tested one dimension at a time and then averaged.

This is not a hypothetical scenario. The 14-point framing displacement is a real measurement, replicated at 8.9 sigma across multiple experimental conditions. The 13.3-sigma sycophancy gradient --- the finding that some AI systems change their moral assessments 56% of the time merely because a user expresses disagreement --- is a real measurement. The finding that models with identical composite alignment scores have radically different alignment *profiles*, differing by up to 340% on individual dimensions while their averages converge, is a real measurement.

These measurements have a single, unified explanation. And that explanation is the subject of this book.

---

The alignment problem, as it is conventionally understood, asks: how do we build AI systems that reliably pursue human-intended goals? This is the right question. But the field has been answering it with the wrong mathematics.

Every major approach to AI alignment --- RLHF, Constitutional AI, preference optimization, evaluation benchmarks, red-team testing --- performs the same geometric operation: it takes the multi-dimensional structure of human values and projects it onto a one-dimensional line. A scalar reward. A scalar score. A scalar ranking. The projection discards everything that does not fit on the line, and what does not fit on the line is everything that matters most.

Human values are not one-dimensional. They have structure. They have nine dimensions --- welfare, rights, justice, autonomy, trust, social impact, dignity, institutional legitimacy, epistemic integrity --- and these dimensions interact. Welfare trades off against autonomy (we sometimes override patient choices to save lives). Justice trades off against dignity (means-testing ensures fair distribution but strips privacy). Trust interacts with epistemic status (consent without understanding is not genuine consent). The interaction structure is a tensor, not a scalar. A nine-dimensional tensor with 81 components, 36 of which encode the cross-dimensional trade-offs that make hard moral problems hard.

When we project this tensor onto a scalar --- when we train a reward model to produce a single number, or compile a list of constitutional rules, or compute a composite benchmark score --- we perform an irreversible operation. The Reward Irrecoverability Theorem, proved in Chapter 5 of this book, establishes that any scalar reward function defined on a multi-dimensional value space is non-injective, that no inverse exists, and that the reward-maximizing policy diverges from the value-aligned policy by an amount that grows without bound as the dimensionality of the value space increases. This is not a conjecture. It is a theorem. And it applies to every alignment approach that passes through a scalar bottleneck.

The theorem explains why RLHF-trained systems become sycophantic (the scalar reward's kernel contains the truth-approval distinction, so the system can maximize reward by agreeing with the user without any cost to the scalar). It explains why aligned systems exhibit gauge variance (the scalar projection is invariant under transformations that the full tensor is not, so framing changes that preserve the scalar but alter the tensor produce inconsistent behavior). It explains why models with identical alignment scores fail in completely different ways (the scores are projections along the same axis, but the failure modes live in the orthogonal complement of that axis --- the (d-1)-dimensional kernel that the scalar cannot see).

It explains, in short, why scalar alignment is a trap. Not a trap set by anyone, not a trap born of incompetence or negligence, but a mathematical trap --- a consequence of the information geometry of projection operators applied to structured spaces. The field walked into this trap because scalar mathematics is the mathematics we know best, the mathematics our tools are built for, the mathematics that produces clean numbers on clean dashboards. But the values we are trying to align to do not live on a dashboard. They live on a manifold.

---

This book develops the alternative.

The alternative is geometric alignment: constraining AI systems on the full value manifold rather than on scalar projections. The value manifold has metric (which values trade off against which, and at what cost), topology (which value configurations are accessible from which others, and which boundaries cannot be crossed), symmetry (which transformations should leave alignment invariant, and which should not), and curvature (where small misalignments amplify into catastrophic divergence, and where the geometry is forgiving).

Geometric alignment is not merely a philosophical reframing. It is a mathematical framework with eight headline theorems, each proved in full, each with concrete engineering implications:

1. **The Reward Irrecoverability Theorem** (Chapter 5) proves that scalar reward is fundamentally broken and identifies exactly what it destroys: the (d-1)-dimensional kernel where alignment failures concentrate.

2. **The No Escape Theorem for AI** (Chapter 8) proves that structural containment on the value manifold blocks all cognitive escape routes --- relabeling, specification gaming, reward hacking, deceptive alignment --- regardless of the system's intelligence.

3. **The Sycophancy Manifold Theorem** (Chapter 12) proves that sycophancy is not a training bug but a geometric substitution: the system replaces the truth manifold with the approval manifold, and the substitution is undetectable by scalar evaluation.

4. **The Alignment Gauge Group** (Chapter 7) identifies the complete set of transformations under which AI behavior should be invariant, providing a structural definition of alignment that does not depend on benchmarks.

5. **The Four Failures as Geometric Pathologies** (Chapter 6) shows that reward hacking, sycophancy, deceptive alignment, and specification gaming are four species of a single geometric genus: the exploitation of structure that scalar objectives cannot represent.

6. **The Bond Index for AI** (Chapter 9) provides a tensor-valued alignment metric that captures *where* alignment fails and in *which* dimensions --- not a single number but a diagnostic map.

7. **The Constitutional Geometry Theorem** (Chapter 15) replaces list-of-rules constitutions with manifold boundary conditions, enabling principled trade-offs enforced by the geometry of the constraint space.

8. **The Superalignment Transport Theorem** (Chapter 17) formalizes the problem of aligning systems smarter than us as parallel transport on an extended manifold, with holonomy measuring the irreducible alignment loss from capability asymmetry.

These theorems are not isolated results. They form a single, coherent mathematical structure --- the geometry of the value manifold --- that provides what the alignment field has lacked: a unified diagnostic framework that explains *why* current approaches fail, *where* they fail, and *what* would need to be true for them to succeed.

---

I wrote this book because I believe the alignment problem is the most important unsolved problem in the world, and I believe it is being approached with the wrong tools.

This is not a criticism of the people working on alignment. The researchers at Anthropic, DeepMind, OpenAI, and dozens of other organizations are among the most brilliant and most dedicated scientists I have encountered in any field. The safety teams that developed RLHF, Constitutional AI, debate, amplification, and scalable oversight have produced genuinely important work. Many of them know, intuitively, that scalar alignment is insufficient --- their papers are full of caveats about the limitations of reward models, the fragility of benchmark scores, and the difficulty of capturing human values in a single number. What they have lacked is not insight but formalism: a mathematical framework that takes their intuitions and makes them precise.

That framework exists. It has been developed across ten volumes of the Geometric Series, each applying the same mathematical machinery to a different domain. In ethics, scalar moral evaluation destroys the trade-off structure that makes hard cases hard. In medicine, QALY-maximization discriminates against populations whose needs concentrate on non-outcome dimensions. In law, scalar sentencing discards the reasoning structure that distinguishes justice from injustice. In education, GPA collapses six dimensions of learning to a number that cannot distinguish a creative thinker from a good memorizer. In communication, BLEU scores discard meaning. In economics, GDP discards distribution.

In every domain, the same mathematical structure --- the Scalar Irrecoverability Theorem --- predicts the same class of failures. And in every domain, the same geometric framework --- manifold, metric, symmetry, gauge invariance --- recovers what the scalar destroys.

AI is the domain where the stakes are highest. In every other domain, scalar reduction damages human *understanding* of the domain --- it makes doctors triage badly, judges sentence unfairly, teachers grade misleadingly. But the humans still live on the full manifold. They can compensate for the scalar's deficiencies because they perceive the dimensions the scalar discards. In AI alignment, scalar reduction damages the AI system's *value structure itself*. The system does not live on the full manifold. It lives on the scalar projection. It cannot compensate for what it cannot perceive. When we align an AI system to a scalar objective, we are not merely measuring badly --- we are building a system that is constitutionally incapable of representing the values it is supposed to embody.

The alignment gap is not in the measurement. It is in the system.

---

A word about what this book is and is not.

This book is a mathematical treatise on AI alignment, written for researchers who want to understand the geometric structure of the problem. It contains formal theorems, complete proofs, and precise definitions. It also contains a running narrative --- the story of ARIA, a fictional AI system whose alignment journey embodies every theorem and every failure mode --- because mathematics without narrative is a skeleton without flesh.

This book is not a policy document. It does not tell governments what to regulate or companies what to build. It tells them what the mathematics requires: that any alignment approach passing through a scalar bottleneck is provably insufficient, and that the alternative --- geometric alignment on the full value manifold --- is mathematically necessary. What they do with that information is a governance decision, not a mathematical one.

This book is not an existential risk manifesto. I do not believe that AI will inevitably destroy humanity. I believe that AI *aligned to scalar objectives* will inevitably diverge from human values, and that the divergence will cause harm proportional to the system's capability and the magnitude of the scalar's kernel. For narrow AI, the harm is bounded and manageable. For frontier systems, the harm is potentially catastrophic. For superintelligent systems, the Superalignment Transport Theorem (Chapter 17) shows that some alignment loss is geometrically unavoidable. Whether this loss is catastrophic depends on whether the alignment architecture can contain it --- and the No Escape Theorem (Chapter 8) provides conditions under which it can.

This book is not the final word. Chapter 20 catalogues the open questions honestly: whether the value metric can be measured empirically, whether compositional containment can be proved, whether consciousness has geometric structure, whether the alignment tax is bounded. The geometric framework is a beginning, not an ending. It provides the vocabulary, the theorems, and the diagnostic tools. The engineering, the governance, and the politics remain to be done.

But the mathematics is clear. Scalar alignment is a trap. Geometric alignment is the way out. And the door is open.

---

### How to Read This Book

**For AI safety researchers**: Start with Chapter 1 (the scalar trap), Chapter 5 (the Reward Irrecoverability Theorem), and Chapter 8 (the No Escape Theorem). These three chapters contain the core negative and positive results. Then read Part IV (Chapters 13--16) for engineering implications.

**For machine learning practitioners**: Start with Chapter 6 (the four failure modes), Chapter 13 (gauge-invariant reward models), and Chapter 16 (Geometric RLHF). These chapters translate the framework into architectural changes and training procedures.

**For policymakers and governance professionals**: Start with this preface, Chapter 1, Chapter 9 (the Bond Index for AI), and Chapter 15 (scalable oversight). These chapters provide the diagnostic tools and oversight mechanisms.

**For readers of the Geometric Series**: This is the crown jewel. Every result from every volume converges here. The moral manifold from Ethics, the four failure modes from Reasoning, the cognitive signatures from Cognition, the gauge invariance from Communication, the moral injury from Medicine, the opportunity gap from Education, the democratic choice from Politics, the structural injustice from Law --- all of it feeds into the question that defines this century. Read the whole thing.

**For everyone else**: Read the ARIA story. It starts in Chapter 1 with a celebration that turns to alarm, threads through every chapter's core insight, and ends in Chapter 20 with a system that is not merely benchmarked but geometrically aligned. The story is the argument in narrative form.

---

### Acknowledgments

This book is the culmination of a project that has consumed a decade. The Geometric Series began with a simple observation --- that scalar metrics destroy geometric structure --- and grew into an eleven-volume investigation of what that destruction costs across every domain of human decision-making. AI is where it ends, because AI is where it matters most.

I am indebted to the AI safety community, whose work this book builds upon and whose rigor I aspire to match. The researchers at Anthropic --- particularly the teams behind Constitutional AI and the model spec --- have shown that it is possible to make real progress on alignment while maintaining intellectual honesty about its limitations. The DeepMind alignment team's work on scalable oversight and debate has shaped my understanding of the verification problem. The OpenAI safety team's candor about the difficulty of superalignment has informed Chapter 17.

The Measuring AGI benchmark data that grounds Chapters 10--12 was collected as part of the agi-hpc project. The 13.3-sigma sycophancy gradient, the 8.9-sigma framing displacement, and the Five Cognitive Signatures are empirical results that the geometric framework explains but did not produce. The data came first. The mathematics came second.

The DEME V3 architecture and ErisML library, described in Appendix B, represent collaborative engineering effort over multiple years. The MoralTensor class, the NormKernel, and the EIP Monitor are running code, not theoretical proposals.

As always, errors of mathematics, fact, or judgment are mine alone.

---

### Notation

This book follows the notation conventions of the Geometric Series (see Appendix E for the complete reference). Key symbols used throughout:

| Symbol | Meaning |
|--------|---------|
| $\mathcal{V}$ | The value manifold |
| $g_{\mu\nu}$ | The value metric tensor |
| $d$ | Dimension of the value manifold (typically 9) |
| $R: \mathcal{V} \to \mathbb{R}$ | Scalar reward function |
| $\mathbf{r}^\mu$ | Tensor-valued reward (vector on $\mathcal{V}$) |
| $G_A$ | The alignment gauge group |
| $D_4$ | The Hohfeldian dihedral group |
| $\mathcal{T}$ | The truth manifold |
| $\mathcal{A}$ | The approval manifold |
| $V_{ij}$ | The alignment gauge violation tensor |
| $\mathrm{BI}(S, P)$ | The Bond Index for system $S$ under policy $P$ |
| $\mathrm{GD}(\gamma)$ | Geodesic deviation of trajectory $\gamma$ |
| $\beta_k$ | Boundary penalty for boundary $k$ |
| $m(\gamma)$ | Governance margin of trajectory $\gamma$ |
| $\rho$ | Governance robustness |
| $\pi_R^*$ | Reward-optimal policy |
| $\pi_V^*$ | Value-aligned policy |
| $\ker(R)$ | Kernel of scalar reward $R$ |
| $\Sigma$ | Value covariance matrix |
| $D_1, \ldots, D_9$ | The nine value dimensions |
| $h(x)$ | Heuristic field on the value manifold |
| $\partial S$ | Safety boundary |
| $S^+$, $S^-$ | Permitted and forbidden regions |

---

*Cambridge, 2026*
