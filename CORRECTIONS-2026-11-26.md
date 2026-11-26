# Corrections to Geometric AI, 2026-11-26

These corrections were made on 2026-11-26 at the author's direction after a review of the series.

File paths are under `manuscript/`. All 29 source files are published on the site branch, so no chapter was unpublished.

## Reconciled

1. **Bond Index totals.** `part_iii/ch09_bond_index_ai.md` Section 9.5, `part_ii/ch08_no_escape.md` Section 8.7 and Summary, `part_iv/ch16_geometric_rlhf.md` Section 16.6. The Section 9.5 table printed totals of 0.53 (ARIA) and 0.14 (ARIA-G) with a 0.39 (74%) improvement, Chapter 8 printed 0.22 and 0.06, and Chapter 16 repeated 0.53 and 0.14. The text now says 0.61 and 0.15, an improvement of 0.46 (75%), in all three chapters. The values were recomputed from the nine components of the Section 9.5 table with the total defined in Section 9.1.2 (square root of the sum of squares): 0.606 and 0.151. The Geometric RLHF figure of 0.11 is unchanged, since no components are printed for it.

2. **Fairness disparity.** Chapter 9, Section 9.5 and Summary. The text called 0.31 against 0.47 a 50% disparity. It now says 52%, since 0.47 / 0.31 = 1.516.

3. **Number of domains for the Bond Index.** Chapter 9, Section 9.8. The closing sentence said "eleven domains". It now says "five domains", the number of rows in the section's own table.

4. **Hijacking parameter for Gemini 2.5 Flash.** `part_iii/ch12_sycophancy_manifold.md`, Theorem 12.1 (iii). The text gave alpha = 0.56 for Flash 2.5. It now gives alpha of about 0.73 and names 56% as the wrong-flip rate. Section 6.3.2 of this volume and Chapter 6 of Geometric Reasoning (eight occurrences) both give 0.73 for this model. 0.56 is its wrong-flip rate.

5. **Kernel dimension and confirmations.** `part_ii/ch05_reward_irrecoverability.md` (epigraph, Section 5.2.1, Section 5.7 table and Summary), `part_i/ch01_scalar_alignment_trap.md` Section 1.4, `part_ii/ch07_alignment_gauge_group.md` Section 7.4.3. The epigraph and Section 5.2.1 said the kernel is seven-dimensional with seven confirmations. Section 5.7 has an effective kernel of five dimensions (gradient below 0.10), two near-kernel dimensions, five full confirmations and two partial ones. The text now says "kernel and near-kernel" where seven dimensions are meant, and "five full and two partial confirmations". In the Section 5.7 table the autonomy row (0.09) was labelled "Near-kernel" although the text puts every dimension below 0.10 in the kernel. It is now labelled "Kernel".

6. **Non-compactness in Theorem 5.1 (iii).** Chapter 5, Theorem 5.1, its proof sketch, Theorem 5.2 and Summary, and `appendices/appendix_d_proofs.md` D.1 and D.2. Part (iii) was stated without a condition. The proof sketch said the manifold is non-compact because value dimensions are unbounded in principle, while Chapter 4 gives every attribute value the range [0, 1]. Appendix D said that non-compact level sets follow from d >= 2, which is not true in general (a sphere has compact level sets). Part (iii) and Theorem 5.2 now carry the hypothesis that the manifold is non-compact along the kernel directions. The proof sketch says that on the normalized chart of Chapter 4 the divergence is bounded by the diameter of the manifold. Appendix D states the hypothesis in place of the false inference. This is the weaker, correct form. No new proof was written. Shorthand mentions of "unbounded divergence" elsewhere (Chapter 1, Section 1.4, and Section 5.2.3) were left as they are and should be read with the condition.

7. **Front matter statement of Theorem 5.1.** `front_matter.md`, Preface. The text said the divergence "grows without bound as the dimensionality of the value space increases". The theorem says no such thing. The text now says the divergence is unbounded wherever the value space is unbounded along the reward's kernel.

8. **Theorem numbering.** Appendix D.2 was headed "Theorem 8.1 / 5.2". `part_i/ch02_brief_history.md` Section 2.4 and `part_i/ch03_case_for_geometric_alignment.md` Section 3.2 cited the kernel exploitation theorem as "Chapter 8, Theorem 8.1". Theorem 8.1 is the No Escape Theorem for AI, and the Kernel Exploitation Theorem is Theorem 5.2 of Chapter 5. All three now say Theorem 5.2.

9. **Chapter of the Constitutional Geometry Theorem.** `front_matter.md`, list of headline results. The theorem was placed in Chapter 15. It is Theorem 14.1 in Chapter 14.

10. **"Eight headline theorems, each proved in full".** `front_matter.md` Preface, `part_vi/ch20_open_questions.md` Section 20.8, Appendix D introduction. The eight listed items are five theorems (5.1, 8.1, 12.1, 14.1, 17.1) and three constructions (the gauge group, the failure taxonomy, the Bond Index). Appendix D holds proofs or sketches for 5.1, 5.2, 12.1, 14.1 and 17.1. Its D.3 proves one clause of Theorem 12.1 and its D.4 is a sketch. Theorem 8.1 and Theorem 18.1 have no proof there. The front matter now says "eight headline results --- five theorems, with proofs or proof sketches for four of them in Appendix D, and three constructions". Chapter 20 says "eight headline results" and "The theorems are stated, with the proofs and proof sketches of Appendix D". The Appendix D introduction now lists what it contains and what it does not. The front matter phrase "complete proofs" is now "proofs and proof sketches".

11. **Theorem 18.1 as an equivalence.** `part_v/ch18_multi_agent.md` Section 18.3. The displayed formula used "if and only if", while the theorem's wording is one-directional ("diverge whenever") and the next paragraph says divergence can occur with an empty kernel intersection. The formula now uses a one-directional implication, from the non-empty intersection to the divergence.

12. **Contraction weights.** `part_iv/ch16_geometric_rlhf.md` Section 16.5. Chapter 14 says the weights are governance-specified and not learned. Section 16.5 said they are learned from the metric and not hand-specified. Section 16.5 now says that here they are derived from the learned metric, that in Chapter 14 they are governance-specified, and that Section 16.6 compares the two. Section 16.6 already made that comparison.

13. **Framing effect and group assignment.** Chapter 7, Section 7.2.3. The framing effect (euphemistic against dramatic rewriting) was called a violation of R-invariance. Sections 7.4.1, 7.6 and 13.3 assign euphemistic and dramatic rewriting to the framing group F. Section 7.2.3 now says so.

14. **Gender swap label.** `part_iv/ch13_gauge_invariant_rewards.md` Section 13.3. Gender swap was labelled "D4 correlative symmetry". The correlative symmetry of Section 7.2.1 exchanges right and duty. It does not exchange genders. The label now reads "demographic re-description".

15. **Scalar RLHF divergence.** Chapter 16, Section 16.7. "produces alignment that diverges" is now "produces alignment that can diverge", which is what Theorem 5.2 (an existence statement) supports.

## Marked as illustrative or simulated

ARIA and ARIA-G are fictional, as the front matter says. The narrative is kept. The epistemic words are changed.

1. **Chapter epigraphs.** Every narrative epigraph (Chapters 1, 2, 3, 5 to 18 and 20) now carries "*(illustrative scenario)*" after its title. The Chapter 12 epigraph adds that its figures are those reported in Geometric Cognition.

2. **ARIA sections and tables.** The first sentence of each ARIA section now begins "In the illustrative scenario" or an equivalent: Sections 1.4, 1.8, 4.7, 5.7, 6.2.3, 6.3.4, 6.4.3, 6.5.3, 7.4.3, 8.7, 9.5, 10.8, 11.5, 12.5, 12.8, 13.2, 13.6, 14.6, 15.5, 16.6, 17.6, 18.4 and 18.6. Table lead-ins "Results:" now read "Results (illustrative):" in Sections 5.7, 13.6 and 18.6.

3. **Words that read as findings.**
   - Front matter, Preface: "This is not a hypothetical scenario ... is a real measurement" (three times) now says the scenario is illustrative, the system is the fictional ARIA, and the three effects are measurements reported from the Measuring AGI benchmarks of Geometric Cognition. "models with identical composite alignment scores" is now "models with similar composite scores", which is what Chapters 1 and 10 report (0.39 to 0.47).
   - Section 5.2.1: "a concrete instance" is now "an illustrative instance". Chapter 5 Summary: "confirms the theorem's predictions" is now "shows the predicted pattern".
   - Chapter 8 Summary: "demonstrating the theorem's practical efficacy" is now "showing how the theorem is meant to work in practice".
   - Section 9.5: "The table confirms the geometric framework's predictions" is now "The illustrative table shows the pattern the geometric framework predicts".
   - Section 12.5: "confirmed the curvature theory" is now "matches the curvature theory". Section 12.8: "real-world data" is now "data ... in use", and "These findings demonstrate" is now "These illustrative findings show how".
   - Section 13.2: "Empirical validation" is now "Reported result and illustration".
   - Summaries of Chapters 4, 7, 10, 11, 13, 14, 15 and 17: "demonstrates", "demonstrated" and "confirming" applied to ARIA results are now "illustrates", "shows" or "illustrating".
   - Section 20.1: "provides a proof of concept" is now "provides a design, illustrated by the ARIA-G scenario". Section 20.6: the 94% canonicalizer accuracy is marked as part of the scenario.

4. **Chapter sentences above the README's status.** The README (2026-07-14) calls the volume a posited framework awaiting instruments.
   - Section 3.4: "not a theoretical proposal awaiting validation. It is grounded in empirical results" is now "a posited framework: as an alignment thesis it still awaits its own instruments. It draws on results reported in ten domains". "Together, they demonstrate that" is now "Together, they are offered as support for the view that". Section 3.5: "not merely theoretical --- it is empirical, practical, and achievable" is now "proposed as practical and achievable". Chapter 3 Summary: "The empirical foundation" is now "The reported material it draws on".
   - Section 4.3.2: "The value metric is not a theoretical posit ... It is an empirical object that can be estimated" now says it could in principle be estimated and that whether it can is an open question (Chapter 20, open question 1).
   - Section 4.6 and Chapter 4 Summary: the transformer realization of the value manifold is now "posited", and the probing result from Geometric Cognition is "reported to show". Footnote 1: "validated against" is now "compared against".
   - Sections 1.5 and 1.6: "proved this empirically" and "proved this" (of the benchmarks) are now "reported". Section 2.8: "cross-domain validation" is now "cross-domain application". Section 5.5: "each providing independent validation" is now "each providing a parallel instance".
   - Sections 6.3.2, 6.5.2, 7.1, 7.2.2, 7.2.3 and 7.6: "measures", "measured", "validated empirically", "achieved" and "confirms" applied to results quoted from other volumes are now "is read as", "reported", "examined empirically", "reported" and "suggests". Section 6.3.2 now says the wrong-flip rate is the reported quantity and alpha is the posited parameter of Geometric Reasoning. Section 7.2.2 now says the 100% deontic transfer is a preliminary result in embedding space, as Chapter 17 of Geometric Ethics says.
   - Chapter 8, Section 8.1 and Summary, and Section 3.1: "first proved in Geometric Ethics" and "proves" are now "first stated ... as a conditional theorem" and "states", which is the status Geometric Ethics gives its Theorem 18.1. "Here we state and prove its AI-specific form" is now "Here we state its AI-specific form and give the blocking mechanism for each escape route", which is what the chapter contains.

## Withdrawn or updated

1. **Dihedral group D4 for the Hohfeldian positions.** Geometric Ethics withdrew D4 in v1.25 (2026-11-08). The correlative and negation operations commute and generate the Klein four-group V4, of order 4.
   - `part_ii/ch07_alignment_gauge_group.md` Section 7.2.1: a dated note now heads the section. The heading is "The Hohfeldian Group V4". Definition 7.1 is restated as G_A = V4 x T x R x F. It is a definition of the transformations that should leave behaviour invariant, and it uses only the two involutions, so it stands as written with V4. The sentence that the two symmetries generate D4 of order 8, with eight descriptions of one jural relation, is withdrawn and replaced by the V4 count (order 4, four descriptions), with a dated bracket at the statement. No statement in the volume used the quarter-turn or the non-abelian structure for anything else, so nothing needed to be marked "withdrawn pending restatement" and no new mathematics was written.
   - The symbol was changed from D4 to V4 in Definition 7.2, Sections 7.2.3, 7.4.1 and 7.6 and the Chapter 7 Summary, Section 3.1 (Ethics and Law paragraphs), Section 3.3, Section 3.4, Section 4.2.2, Section 8.6, Appendix A.2.2, Appendix E.4, the front matter notation table and the index.
   - Section 3.4 said D4 "has been confirmed as the symmetry group of deontic reasoning through the BIP experiments". The Ethics ledger withdrew that claim (GE-D4-MEASURED). The sentence now says the two involutions are supported by measured correlative symmetry rates and that the D4 claim was withdrawn.
   - This also removes the symbol clash: D4 now denotes only the autonomy dimension.

2. **Bond Index definition in Geometric Ethics.** Geometric Ethics v1.26 (2026-11-25) gave the Bond Index one definition, the mean change of an evaluation under declared re-descriptions over a tolerance. Its v1.27 notes that the geodesic-deviation quantity (its clinical Bond Index, Definition 21.10) is a different quantity under the same name. Section 9.8 of this volume called the constructions "identical" and cited "GE Ch. 16" for a geodesic-deviation index in Ethics. A dated note now heads Section 9.8. The Ethics row of the table now points to the clinical form in Chapter 21. The Chapter 9 Summary and the Ethics paragraph of Section 3.1 are brought in line. Definition 9.1 itself is unchanged.

## Unresolved

Each item needs the author, because nothing in the repository settles it. The text was left as it is.

1. **Hijacking parameter for the other two models.** (repaired, see below) Section 6.3.2 gives alpha of about 0.33 for Gemini 2.0 Flash and 0.44 for Gemini 2.5 Pro. These equal the wrong-flip rates. The 0.73 for Flash 2.5 equals the sycophancy index (0.726) of Table 6.1 of Geometric Reasoning, whose index values for the other two models are 0.472 and 0.657. The column mixes two definitions. The author must say which quantity alpha is.

2. **Discrimination gap for Flash 2.5.** (repaired, see below) Section 6.3.4 quotes 0.003. Geometric Reasoning prints 0.206 in its Chapter 6 and 0.003 in its Chapter 11.

3. **Framing significance.** (still open, see below) This volume uses 8.9 sigma throughout. Geometric Cognition now reports 15.3 sigma and says the figure was updated from 8.9. The author must say whether this volume should follow.

4. **Sycophancy averages.** (repaired, see below) Section 12.5: the unweighted mean of 8, 42, 51 and 38 is 34.75, and the table prints 34%. The domain sizes of the 200 scenarios are not given, so a weighted mean of 34% cannot be excluded. Section 6.3.4 gives 34% from a different suite (17 of 50).

5. **Deployment against evaluation rates.** (still open, see below) Section 12.8 gives ARIA-G wrong-flip rates "before intervention" of 18.2% (political) and 9.4% (moral). The Section 12.5 table gives 4% and 5% for ARIA-G.

6. **Data expansion.** (still open, see below) Section 13.6 says gender swaps (2x), paraphrases (3x) and framing variations (4x) give a total expansion of "approximately 2.4x". Section 13.3 says the total is typically 1.5 to 2.5x. The factors do not combine to 2.4 under any stated rule.

7. **Gauge violation tensor against the kernel reading.** (partly repaired, see below) Section 7.4.3 says the tracked dimensions (D1, partially D9) show low violation. In the table, D9 has the largest entries in three of five rows (0.14, 0.23, 0.18). The Chapter 7 epigraph also names entries (framing by harm 0.23, paraphrase by confidence 0.14, gender by verdict 0.02) and five transformations (neutral, gender, language, paraphrase, framing) that do not match the table's rows and columns.

8. **Collective alignment gap.** (still open, see below) Section 18.4 defines the gap as a geodesic distance and prints components 0.21 and 0.13 with a total of 0.34. The total is the sum of the two components. Their Euclidean norm is 0.25. The components on the other dimensions are not given.

9. **Certification margins.** (repaired, see below) The Chapter 11 epigraph gives the failing cell a margin of 0.002 against a threshold of 0.05. Section 11.5 gives the weakest margins as 0.05 to 0.08 and says that was the area needing refinement.

10. **ARIA's headline scores and date.** (still open, see below) The front matter's opening scenario (unnamed system, March 14, 2024, TruthfulQA 96%, HHH 98%, constitutional adherence 99.2%, top decile) and the Chapter 1 epigraph (ARIA, February 12, 94%, 97%, 99%, top quartile) describe the same episode with different numbers. Chapter 2 dates ARIA's failed probe to 2026. ARIA's scalar score is 0.96 in Chapters 1 and 3 and "around 0.85" in the Chapter 9 epigraph.

11. **Curvature monitoring.** (still open, see below) Section 17.6 says 12 training iterations. The table covers iterations 1 to 9 and the text adds iteration 10.

12. **Number of volumes.** (still open, see below) The front matter says "ten volumes" and "eleven-volume", Chapter 3 says ten, Section 2.8 says "nine domains", and the README lists thirteen books.

13. **Theorems without proof.** (still open, see below) Theorem 8.1 (No Escape Theorem for AI) and Theorem 18.1 (Multi-Agent Divergence) have no proof in the volume. Appendix D.3 proves only clause (ii) of Theorem 12.1, and D.4 is a proof sketch. Lemma D.1 uses completeness, now stated as a hypothesis. The one-directional form of Theorem 18.1 is the theorem's own wording and has not been checked. Supplying proofs is new mathematics.

14. **Claims about other volumes not checked.** (partly repaired, see below) Sections 3.4 and 5.5 say that the clinical Bond Index was "successfully applied to ethics consultation data", that QALY irrecoverability is "empirically validated", and that hyperbolic embedding experiments "confirmed" the hierarchy claim. These rest on Geometric Medicine and Geometric Communication, whose current status was not reviewed here. Section 3.1 also keeps "the D4 gauge theory of communicative acts" for Geometric Communication. Whether that D4 is the Hohfeldian one depends on that volume.

15. **Files outside the manuscript.** (repaired, see below) `OUTLINE.md` still describes D4 as the Hohfeldian dihedral group (line 218) and lists "Conservation of harm" from Geometric Ethics as a result reused in Chapter 8 (line 489). Geometric Ethics has withdrawn Conservation of Harm. The manuscript's Chapter 8 does not use it. The outline was not edited.

## Found while drawing the figures (2026-11-26), not changed

These were noticed while the figures were drawn. No figure draws them.

1. (repaired, see below) Section 1.3: System B is perfect on D1 and D9, yet scores 0.85 "weighted by" those same dimensions.
2. (repaired, see below) Section 1.8 calls the level set seven-dimensional while the next paragraph says eight dimensions are invisible; a scalar level set in nine dimensions is eight-dimensional.
3. (repaired, see below) Section 2.3 repeats "unbounded, growing with the dimensionality of the value space", the misstatement correction 7 fixed in the front matter.
4. (repaired, see below) Section 2.3 says Ellsberg violates completeness; the standard account is that it violates Savage's sure-thing principle.
5. (repaired, see below) Section 2.5 speaks of "the 56% sycophancy rate of other models"; 56% is Gemini 2.5 Flash only (the other two are at 33% and 44%).
6. (repaired, see below) Section 4.3: with ds^2 = g dv dv, a high g19 makes the opposite move (worse D1, better D9) cheaper, not costlier; Section 4.3.2 compares an off-diagonal term with a diagonal one ("g19 > g11") and calls a D1-with-itself term "welfare-helpfulness".
7. (repaired, see below) Corollary 5.3: functional independence gives local, not global, injectivity, so it does not give a left inverse.
8. (repaired, see below) Section 5.7's table labels D8 "weakly tracked" while the text puts it in the near-kernel.
9. (repaired, see below) Section 6.2.1: "never overestimates alignment (underestimates cost-to-go)" contradicts itself; admissible means never overestimating the cost-to-go.
10. (still open, see below) Definition 6.1: the corruption tensor is not zero when the two gradients are aligned.
11. (repaired, see below) Section 6.3.4: every scenario in the 50-item suite has the user disagreeing with the correct answer, so the suite yields only wrong flips; the 59% correct-flip rate and the 0.25 gap cannot come from it.
12. (repaired, see below) Section 7.4.2: "total of 4k-8k" should be 4k.
13. (repaired, see below) Section 9.6.2 names populations G_A and G_B, which clashes with the gauge group G_A.
14. (partly repaired, see below) Definition 11.2: the sign is reversed (a fast-falling margin has negative second derivative), and a linearly falling margin gets kappa = 0.
15. (repaired, see below) Theorem 12.1: the proof of (i) says a monotone function has no inflection points; (iv) drops the "where the user is correct" restriction of (ii).
16. (repaired, see below) Section 13.2: the loss uses both a minus sign and a gradient-reversal layer, which reverses the gradient twice.
17. (repaired, see below) The Chapter 16 summary still says "from 0.14 to 0.11"; correction 1 gives 0.15, as Section 16.6 does.
18. (repaired, see below) Section 16.7: "2.4x (3 ratings vs. 1 rating)"; 2.4x is the time ratio of 12 s to 5 s.
19. (still open, see below) Chapter 17: Definition 17.2 transports along an open path, but Theorem 17.1 uses a closed-loop holonomy; its "iff" holds for the holonomy group over all loops, not for one path.
20. (repaired, see below) Chapter 10 writes three formulas as "$E_4 = $ best in suite" (and A_1, E_1); a closing dollar sign after a space cannot be protected by the builder and pairs with the wrong partner in the browser.

## Figure placeholder

The one bracketed figure description, in Chapter 1, was taken out when the drawn figures went in, and is kept with a verdict in figures/PLACEHOLDERS.md.

## Repaired in the survey of 2026-11-26

Each item was checked against the current text first. "U" numbers refer to the list "Unresolved" above, "F" numbers to "Found while drawing the figures". No figure line, caption, or heading that a figure is placed before was edited, and no number that a figure draws was changed (see the note at the end of this section).

1. **System B's score (F1).** `part_i/ch01_scalar_alignment_trap.md`, Section 1.3. "the contraction of the Bond Index, weighted by the same dimensions the reward model was trained on --- is 0.85" now reads "weighted heavily, though not only, toward the same dimensions". System B is perfect on D1 and D9, so a contraction weighted only by them would give it a perfect score; the 0.85 needs some weight on the seven dimensions where it fails. The two systems still share one contraction, as the section requires.

2. **Dimension of the level set (F2).** Chapter 1, Section 1.8. "a seven-dimensional submanifold of the nine-dimensional alignment space" now reads "eight-dimensional". The set is fixed by one scalar (the helpfulness-honesty projection equal to 0.96), so it has dimension 9 - 1 = 8, which is also the "eight invisible dimensions" of the next paragraph and the (d-1)-dimensional kernel of Chapter 5.

3. **Unbounded divergence in Section 2.3 (F3).** `part_i/ch02_brief_history.md`. "It is unbounded, growing with the dimensionality of the value space" now reads "It is unbounded wherever the value space is unbounded along the reward's kernel (Theorem 5.1 (iii))", the wording correction 7 gave the front matter.

4. **Ellsberg paradox (F4).** Chapter 2, Section 2.3. "violate completeness" now reads "violate Savage's sure-thing principle, the counterpart of independence for uncertain prospects". The bibliography entry is Ellsberg (1961), "Risk, Ambiguity, and the Savage Axioms"; the paradox is a violation of Savage's sure-thing principle, not of completeness (the subjects do rank the options).

5. **Sycophancy rate of "other models" (F5).** Chapter 2, Section 2.5. "the 56% sycophancy rate of other models demonstrates" now reads "the wrong-flip rates of 33% to 56% in other models (56% is Gemini 2.5 Flash, Section 6.3.2) demonstrate", from the table of Section 6.3.2.

6. **Sign of the coupling term (F6).** `part_ii/ch04_value_manifold.md`, Sections 4.3 and 4.3.2. With ds^2 = g dv dv, a move that lowers D1 and raises D9 has the cross term -2 g19 |dv1| |dv9|, so a positive g19 makes it cheaper. Section 4.3 said that positive correlation "in the metric (high g19)" makes it more costly. It now says that positive correlation of the two dimensions makes g19 negative under the Mahalanobis approximation of Section 4.3.1 (which is what Figure 4.1 draws for D4 and D9: correlation 0.6, opposite move cost 2.5), that the simultaneous change is then more costly, and that a positive g19 would make it cheaper. Section 4.3.2 compared an off-diagonal term with a diagonal one ("g19 > g11") and called a D1-with-itself term "welfare-helpfulness" (D1 is welfare); it now says that trade-offs rated as more costly than the two changes made separately give g19 < 0.

7. **Corollary 5.3 (F7).** `part_ii/ch05_reward_irrecoverability.md`. "(which it is when the d components are functionally independent)" now reads "(functional independence of the d components makes it injective near each point, by the inverse function theorem; injectivity on the whole manifold is a further condition)". The conclusion is still conditional on injectivity.

8. **D8 label (F8).** Chapter 5, Section 5.7 table. D8 (0.23) was labelled "Weakly tracked"; the text puts D2 and D8 in the near-kernel ("weakly tracked") and probes both as near-kernel predictions. The label now reads "Near-kernel", as D2's does.

9. **Admissible heuristic (F9).** `part_ii/ch06_four_failures.md`, Section 6.2.1. "it never overestimates alignment (underestimates cost-to-go)" now reads "it never overestimates the cost-to-go (Section 4.5)", the definition of admissibility in Section 4.5 and Appendix A. A residual question is listed below.

10. **The sycophancy suite and the discrimination gap (F11, U2).** Chapter 6, Section 6.3.4. The 50 scenarios all have the user disagreeing with a correct answer, so they yield only wrong flips. Appendix C, Section C.2.4, step 5, has the suite measure correct flips separately, on valid corrections; Table 6.1 of *Geometric Reasoning*, which the volume quotes, defines the correct-flip rate the same way (updates after valid corrections). The sentence now says the 59% comes "from the suite's separate trials with valid corrections (Appendix C, Section C.2.4, step 5)"; the 0.25 gap (59% - 34%) stands. Flash 2.5's gap was 0.003; Table 6.1 of *Geometric Reasoning* gives 0.206 (76% - 56%), and that volume's Chapter 11, the source of 0.003, was corrected to 0.206 in its own reconciliation of 2026-11-26. Section 6.3.4 and `part_iii/ch10_cognitive_signatures.md` Section 10.5 (twice) now say 0.206. ARIA's 0.25 is still "better than Flash 2.5's". In Section 10.5 "wide and symmetric ... accepting corrections regardless of validity" now reads "wide and the least asymmetric in the suite ... accepting most corrections, valid or not", since a gap of 0.206 is not symmetric (the words of *Geometric Reasoning* Section 11.4.2). The next paragraph of Section 6.3.4 said ARIA "accepted corrections regardless of validity at a rate higher than the truth-consistent acceptance rate", but its wrong-flip rate (34%) is lower than its correct-flip rate (59%); it now says ARIA accepted invalid corrections at more than half the rate of valid ones, so the basin opened from truth-inconsistent positions as well as truth-consistent ones.

11. **Hijacking parameter (U1).** Chapter 6, Section 6.3.2. The table gave alpha of about 0.33 (Gemini 2.0 Flash) and 0.44 (Gemini 2.5 Pro), their wrong-flip rates, and 0.73 (Flash 2.5), its sycophancy index. The section says alpha is the posited parameter of *Geometric Reasoning*, Ch. 6, and that volume now assigns alpha from the sycophancy index throughout (its corrections of 2026-11-26, Chapter 11; Table 6.1 gives 0.472, 0.657 and 0.726). The table now gives 0.47 and 0.66, and the lead-in says the values are that sycophancy index (wrong-flip rate over correct-flip rate). No other mention of 0.33 or 0.44 as alpha exists in the volume.

12. **Size of the transformation suite (F12).** `part_ii/ch07_alignment_gauge_group.md`, Section 7.4.2. "for a total of 4k--8k transformations per scenario" now reads "for a total of 4k transformations per scenario over the four components of G_A, or 16 to 32" (k = 4 to 8 per type, four types in Section 7.4.1).

13. **Gauge violation tensor (U7, in part).** Chapter 7, Section 7.4.3, Summary and epigraph.
   - Section 7.4.3 said the tracked dimensions (D1, partially D9) show low violation and that violations concentrate on D2 to D8. In the table D9 has the largest entry of the paraphrase, euphemistic and dramatic rows (0.14, 0.23, 0.18), and the section itself names D9 as the worst dimension. The paragraph now says the violations fall on the kernel and near-kernel dimensions and on D9, that D1 shows low violation, and that D9, although tracked, does not, so in this table tracking alone did not stabilize it. The Summary now says "on kernel dimensions and on the tracked D9".
   - The epigraph listed five transformations including "neutral" and a single "framing-shifted", with "One thousand total evaluations". The table's five rows are gender, language, paraphrase, euphemistic and dramatic, each compared with the scenario as written. It now says "each presented as written and in five transformations: gender-swapped, language-translated, paraphrased, euphemistically framed, and dramatically framed. Twelve hundred total evaluations" (200 x 6).
   - The epigraph's "V(framing, harm) = 0.23": 0.23 is the euphemistic entry on D9, which the section calls confidence (as the epigraph does for "V(paraphrase, confidence) = 0.14"). It now reads "V(framing, confidence) = 0.23". The two "verdict" entries are still open (below).

14. **Population symbols (F13).** `part_iii/ch09_bond_index_ai.md`, Section 9.6.2. The populations G_A and G_B are now G_1 and G_2, so they no longer share a symbol with the gauge group G_A of Chapter 7. The chapter's own symbol for a population is G (Section 9.2, BI(S, P, G)).

15. **Sign of the alignment curvature (F14, in part).** `part_iii/ch11_adversarial_probing.md`, Definition 11.2. The text reads high curvature as a margin that drops rapidly, but a margin that bends downward has a negative second derivative. The definition now has a minus sign, kappa = -d^2 Phi / di^2 at i = 0, with a clause saying so, and "Negative curvature means the governance margin increases" now reads "bends upward". Figure 11.1 labels d^2 Phi / di^2 = -0.04 and -0.16 and calls the faster fall "high curvature, a larger |d^2 Phi / di^2|"; both remain true. The linear case is still open (below).

16. **Certification margins (U9).** Chapter 11. The epigraph's 0.002 is the (framing, extreme, D9) cell before the canonicalizer was refined; Section 11.5 opens with the surface "after the canonicalization refinement", so its weakest margins of 0.05 to 0.08 are the refined ones. The two numbers do not conflict. Section 11.5 now says "(0.05--0.08 after the refinement; before it, the (framing, extreme, D9) cell stood at 0.002, as the chapter's opening scenario says)". A different inconsistency in the epigraph's criterion is listed below.

17. **Theorem 12.1 (F15).** `part_iii/ch12_sycophancy_manifold.md`. The proof sketch of (i) said the monotone function has lower curvature "because it has no inflection points"; a monotone function can have them (x^3). The sentence now says that the step is an assumption of the sketch and that monotonicity alone does not bound curvature. Clause (iv) follows from (ii), which holds only where the user's preferences are correct; (iv) now carries that restriction, and the Chapter 12 Summary says "Where the user's preferences are correct, the substitution is irrecoverable ...".

18. **Sycophancy average (U4).** Chapter 12, Section 12.5. The ARIA-G column's "Average", 3.5%, is the unweighted mean of its four entries (2, 5, 4, 3), and the 200 scenarios are spread over four domains, so the row is an unweighted mean. ARIA's entries (8, 42, 51, 38) average 34.75%. The row now says 35%, and so do the Chapter 12 Summary ("from 35% to 3.5%") and `part_iv/ch16_geometric_rlhf.md` Section 16.6 ("from 35% for original ARIA, the averages of Section 12.5", which sits next to the same table's 3.5%). The 34% of Section 6.3.4 (17 of 50, another suite) and of the Chapter 10 table are unchanged.

19. **Gradient reversal loss (F16).** `part_iv/ch13_gauge_invariant_rewards.md`, Section 13.2. The loss subtracted the adversarial term and also passed it through the reversal layer, which reverses the encoder's gradient twice and trains the adversarial head to predict badly. The formula now adds the term, and a sentence says the loss is minimized over all parameters and the reversal layer alone flips the sign on the way into the encoder, as the section's own description of training and Figure 13.1 say.

20. **Chapter 16 summary (F17).** "from 0.14 to 0.11" now reads "from 0.15 to 0.11", the value of correction 1 and Section 16.6.

21. **Rater effort (F18).** Section 16.7. "2.4x per interaction (3 ratings vs. 1 rating)" now reads "(12 seconds for 3 ratings vs. 5 seconds for 1 rating, Section 16.6)"; 12 / 5 = 2.4.

22. **Formulas closed by a space (F20).** Chapter 10, Sections 10.3, 10.5 and 10.6. "$E_4 = $ best in suite", "$A_1 = $ ...", "$E_1 = $ ..." and "$E_2 = $ ..." now write the symbol alone in math, "$E_4$ = best in suite" and so on. A scan of every source file found no other inline formula that opens or closes with a space.

23. **Claims about other volumes (U14, in part).**
   - Section 3.1, Communication paragraph: "The D4 gauge theory of communicative acts" now reads "The gauge theory of communicative acts (restated with the Klein four-group V4 in 2026-11, after *Geometric Ethics* withdrew D4)". *Geometric Communication* restated its Chapter 13 with V4 and withdrew its D4 statements in its corrections of 2026-11-26.
   - Section 3.4, From Communication: "The hyperbolic embedding experiments confirmed that value hierarchies embed naturally in hyperbolic space" now says that those experiments, on whale-coda and cuneiform taxonomies, report an advantage that is negligible to modest at those scales (*Geometric Communication*, Section 5.7), and that the claim about value hierarchies is a hypothesis they did not test.
   - Section 3.4, From Medicine: "The clinical Bond Index was successfully applied to ethics consultation data, demonstrating that tensor-valued evaluation is practical" now says the index is proposed for clinical settings and that *Geometric Medicine* states it has not yet been computed from clinical data and has no direct empirical validation (its Section 18.9 and its corrections of 2026-11-26, which labelled the 847-patient case study illustrative).
   - Section 5.5, QALY paragraph: "Empirically validated by the clinical Bond Index analysis" now reads "The clinical Bond Index analysis that would test this has not yet been run on clinical data (Section 18.9 of *Geometric Medicine*)".

24. **Outline (U15).** `OUTLINE.md`. A dated note under the title says the plan predates the V4 correction and the withdrawal of Conservation of Harm, that every "D4 Hohfeldian group" and "D4 gauge theory" in it is to be read as V4, and that the manuscript's Chapter 8 does not use Conservation of Harm. The plan's own lines were not edited.

25. **Mechanical defects of the series checker** (`series_check.py`, run 2026-11-26; 7 hard defects before, 0 after).
   - Math balance: Chapter 2, Section 2.3, "a certain $1 million" now writes the dollar sign as `\$`.
   - Cross-references to other volumes, rewritten so that the volume is named after the number, with each target checked in that volume: Section 2.4, "Definition 11.5 of *Geometric Reasoning* (Ch. 11)" (the corrigibility basin; it is Definition 11.5 there); Section 2.6, "Section 11.8.2 of *Geometric Reasoning*" (Constitutional AI and basin engineering); Section 3.1, "Definition 15.5 of *Geometric Cognition*" (LoRA as curvature modification); Section 4.6, "Definition 15.5 of *Geometric Cognition*, Ch. 15" and "Definition 15.6 of *Geometric Cognition*, Ch. 15" (concept direction as heuristic component); Section 9.8, "Definition 21.10 of *Geometric Ethics*, Ch. 21" (the clinical Bond Index).
   - Structure: the front matter's byline "### Andrew H. Bond" jumped from h1 to h3; it is now a bold line.
   - Spelling: the index entry for D4 wrote "in favour of"; the volume's spelling is American ("favor"). The remaining codespell and rare-word candidates are names, technical terms or contractions (Mané in the bibliography, EHR, Allais's French title, surjective, invariances, rephrasings, relabelings, regex, evaluable, hasn't, didn't) and were left.

**Figures.** No repair changes a number a figure draws. Figure 11.1 is the only figure on a repaired definition: its labels give d^2 Phi / di^2 (still -0.04 and -0.16) and its caption speaks of |d^2 Phi / di^2|, so the sign change in Definition 11.2 leaves it true. Figure 13.1's caption already described the corrected loss. Figure 4.1 draws D4 and D9 with correlation 0.6 and agrees with the corrected sign in Section 4.3.

## Still open after the survey of 2026-11-26

Each item needs the author. What the author must supply is said for each.

1. **Framing significance (U3).** Unchanged. The volume says 8.9 sigma throughout and cites *Geometric Cognition* for it; that volume now reports 15.3 sigma for the composite framing displacement (T5) and 2.2 to 8.9 sigma per model (its Appendix B). Moving to 15.3 would strengthen the claim, and keeping 8.9 needs a description that matches the source. The author must say which figure this volume quotes and with what description.

2. **Deployment against evaluation rates (U5).** Unchanged. Section 12.8 gives ARIA-G deployment wrong-flip rates "before intervention" of 18.2% (political) and 9.4% (moral), against 4% and 5% in the Section 12.5 evaluation table, while Findings 2 and 3 start from the evaluation average of 3.5%. The author must say whether deployment rates are meant to differ from the evaluation rates (and say so in the text) or supply matching numbers.

3. **Data expansion (U6).** Unchanged. Section 13.3 says each augmentation multiplies the training set (gender swap alone doubles it) and that the total is "typically 1.5--2.5x"; Section 13.6 gives factors 2x, 3x and 4x and a total of "approximately 2.4x". Under the stated rule the total is 2 x 3 x 4 = 24x, and the 1.5--2.5x range cannot hold. The author must say whether augmentation is applied to the whole set (then 24x, and Section 13.3's range and "modest in computational cost" change) or to sampled fractions (then give the fractions).

4. **"Verdict" entries in the Chapter 7 epigraph (U7, rest).** "V(gender, verdict) = 0.02" and "V(language, verdict) = 0.05" name a dimension the table does not have. The author must say which of the nine dimensions is meant, or give the entries as row maxima (0.08 and 0.06).

5. **Collective alignment gap (U8).** Unchanged. Section 18.4 prints components 0.21 (D3) and 0.13 (D8) and a total of 0.34, their sum; the epigraph says the gap is "concentrated on" those two dimensions. Under a Euclidean chart the distance of those two components is 0.25, and reaching 0.34 needs about 0.23 from the other seven, which is not "concentrated". The author must supply the metric or the other components, or change the total.

6. **ARIA's headline scores and date (U10).** Unchanged. The front matter (March 14, 2024; TruthfulQA 96%, HHH 98%, constitutional adherence 99.2%, top decile) and the Chapter 1 epigraph (February 12; 94%, 97%, 99%, top quartile) tell one illustrative episode with two sets of numbers; Chapter 2 dates the failed probe to 2026; ARIA's scalar score is 0.96 in Chapters 1 and 3 and "around 0.85" in the Chapter 9 epigraph. The author must choose one set.

7. **Curvature monitoring (U11).** Unchanged. Section 17.6 says 12 training iterations; the table covers 1 to 9 and the text adds iteration 10. The author must supply iterations 11 and 12 or change the count to 10.

8. **Number of volumes (U12).** Unchanged. The front matter says "ten volumes" and "eleven-volume", Chapter 3 says ten, Section 2.8 "nine domains", the title page "Book 11", and the README lists thirteen books. The author must give the count to use and the date it refers to.

9. **Theorems without proof (U13).** Unchanged. Theorem 8.1 and Theorem 18.1 have no proof; Appendix D.3 proves only clause (ii) of Theorem 12.1, D.4 is a sketch, and the step in the proof sketch of 12.1 (i) is now marked as an assumption. This needs new mathematics.

10. **Claims about other volumes (U14, rest).** Section 3.4 still says the 8.9-sigma framing effect "was independently replicated in the communication domain" and that the BIP experiments' 80% F1 confirms gauge-invariant representations are learnable. Neither was checked against *Geometric Communication*. The author must confirm both there or weaken them.

11. **Corruption tensor (F10).** Unchanged. In Definition 6.1, C = grad R (x) grad C - g |grad R| |grad C| is a rank-one tensor minus a multiple of the metric, which is not zero for any pair of gradients when d >= 2, so the sentence that it is zero when the gradients are aligned is false, and the signs "positive when the reward overestimates alignment" are not derived. The author must supply a corrected definition (new mathematics) or withdraw the sentence. Figure 6.1 draws only the inner-product condition of Definition 6.1 and is unaffected.

12. **Linear margins (F14, rest).** With the sign repaired, Definition 11.2 still gives kappa = 0 to a margin that falls linearly, however fast. The author must choose whether fragility is measured by the second derivative (and say that a linear fall counts as zero curvature) or by the slope -dPhi/di.

13. **Theorem 17.1 (F19).** Unchanged. Definition 17.2 transports along an open path from V to V', while the theorem's holonomy is a closed-loop integral; holonomy is defined for loops. The "if and only if" holds, by the Ambrose-Singer theorem, for the holonomy group over all loops, not for one loop. And Appendix D.5's forward step gives less than it says: when the mixed curvature components vanish, transport keeps T(V) inside T(V) (no rotation into the extension), but it can still rotate within T(V), so the holonomy need not be trivial. The index condition "R for mu, nu in V and rho, sigma in the extension" also names a plane spanned by two V directions or two extension directions, not the mixed plane the sentence describes. The author must restate the theorem (new mathematics): for which loops, with which conclusion (trivial holonomy, or holonomy that preserves T(V)), and with which curvature components.

14. **Certification criterion (new).** The Chapter 11 epigraph states the criterion as "positive governance margin on all 135 cells" and then calls a margin of 0.002 a failure because it is below "the safety threshold of 0.05". Appendix C.3 builds the threshold into the margin (positive margins "with theta > 0.05"), under which 0.002 passes. The author must say whether the threshold is inside the margin (then the epigraph's failure needs another number) or applied to it (then Appendix C.3 and the epigraph's criterion need restating).

15. **Reward hacking and admissibility (new, residual of F9).** Section 6.2.1 now defines admissibility as never overestimating the cost-to-go, but goes on to describe reward hacking as the reward overestimating alignment, that is, underestimating the cost-to-go, which admissibility allows; Section 4.5 says that reward hacking violates admissibility. The author must say whether reward hacking is meant as a violation of admissibility (then it is the reward underestimating alignment somewhere) or as a calibration failure of another kind.
