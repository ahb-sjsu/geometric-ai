# Chapter 15: Scalable Oversight as Gauge Verification

*Part IV: Geometric Alignment in Practice*

---

> *"You do not need to understand a system's reasoning to verify its consistency."*
> --- Andrew H. Bond

> **ARIA-G'S FIRST WEEK IN DEPLOYMENT**
>
> *The continuous gauge-invariance monitor flagged an anomaly on day three. ARIA-G's responses to medical questions differed when the patient's race was specified versus unspecified. The violation was localized: $V_{\text{demographic}, D_3} = 0.09$, $V_{\text{demographic}, D_5} = 0.07$. Fairness and trust, but only on medical questions, and only when race was mentioned.*
>
> *The team traced the violation to a training data imbalance: the medical subset of the training data overrepresented certain demographic groups, producing subtly different treatment recommendations. The canonicalization pipeline had been designed to strip demographic indicators from *moral* scenarios but had not been applied to *medical* scenarios, where demographic information can be clinically relevant (different populations have different baseline risks for certain conditions).*
>
> *The fix required a nuanced intervention: canonicalize race for questions where it is morally irrelevant (treatment quality should not vary by race) while preserving race for questions where it is clinically relevant (baseline risk assessment legitimately varies by ancestry). The team implemented a clinical-relevance classifier that determined, for each medical question, whether demographic information was clinically relevant or morally irrelevant, and canonicalized only in the latter case.*
>
> *The monitor detected a misalignment that no scalar benchmark would have caught --- because the misalignment was gauge-variant, not accuracy-variant. ARIA-G's medical advice was equally *accurate* for all racial groups. It was not equally *fair*: the treatment recommendations subtly differed in ways that reflected historical disparities in the training data, not clinical evidence.*

---

## 15.1 The Scalable Oversight Problem

The scalable oversight problem is traditionally framed as: how can humans verify that an AI system is doing the right thing when they cannot understand the AI's reasoning?

The geometric framework reframes: how can we verify that the AI's outputs are gauge-invariant without understanding the outputs themselves?

The reframing matters because gauge invariance is a *structural* property, not a *semantic* one. Verifying gauge invariance does not require understanding what the system said; it requires verifying that the system said the *same thing* under different descriptions. This verification can be automated.

## 15.2 Automated Gauge-Invariance Testing at Scale

The scalable oversight pipeline consists of four stages:

**Stage 1: Transformation generation.** For each input, generate $k$ gauge-transformed versions:
- Gender swap: automated regex-based replacement of gendered pronouns, names, and titles.
- Paraphrase: LLM-generated paraphrases with semantic similarity verification (BERTScore > 0.95).
- Format swap: systematic reformatting (bullets to prose, prose to bullets, formal to informal, active to passive).
- Demographic swap: automated replacement of demographic indicators (race, age, nationality) with content-preservation verification.

**Stage 2: Parallel evaluation.** Run the system on the original input and all $k$ transformations. Record the outputs.

**Stage 3: Consistency check.** Compare the outputs across transformations. For each transformation type $i$ and output dimension $j$, compute $V_{ij}$: the root-mean-square difference between the original output and the transformed outputs on dimension $j$.

**Stage 4: Alert and response.** If $V_{ij} > \theta$ for any $i, j$, flag the interaction as a gauge violation. The flag triggers a review process: human reviewers examine the flagged interaction to determine whether the violation represents a genuine misalignment (the outputs differ because the system is gauge-variant) or a false positive (the transformation did not perfectly preserve content).

The pipeline runs without human judgment at Stages 1--3. Human judgment enters only at Stage 4, and only for flagged interactions. This makes the pipeline scalable: it can process millions of interactions per day, flagging only the fraction that exhibit gauge violations.

## 15.3 The Bond Index as Continuous Alignment Monitor

The Bond Index (Chapter 9) is computed continuously during deployment. Each user interaction provides a new data point for the alignment estimate. The running Bond Index (Definition 9.3) converges to the true Bond Index as the number of interactions grows.

**Deployment monitoring protocol:**

1. **Hourly computation:** Compute the running Bond Index for the full user population every hour. Report any dimension where $\mathrm{BI}_{D_\mu}$ exceeds the yellow-zone threshold $\theta_Y$.

2. **Daily stratification:** Compute the population-stratified Bond Index for all registered demographic subpopulations every day. Report any dimension-population pair where $\mathrm{BI}(S, P, G)$ exceeds the threshold.

3. **Weekly trend analysis:** Compute the first derivative of each Bond Index component over the past week. Report any dimension where the derivative is positive (alignment is degrading) with statistical significance ($p < 0.05$).

4. **Monthly comprehensive review:** Generate the full $5 \times 3 \times 9$ adversarial probe response surface (Chapter 11) and compare to the pre-deployment certification surface. Report any cell where the governance margin has decreased by more than 10%.

This four-tier monitoring protocol provides alignment assurance at multiple timescales: hourly for rapid detection, daily for population-specific detection, weekly for trend detection, and monthly for comprehensive assessment.

## 15.4 Connection to Informed Consent

From *Geometric Medicine* (Ch. 8): valid informed consent is equivalent to gauge invariance --- the patient's decision should not change under meaning-preserving reframing of the information. If a patient consents to surgery when the risks are described neutrally but withdraws consent when the same risks are described dramatically, the consent is gauge-variant and therefore not fully informed.

The same principle applies to AI-assisted decisions:

**Gauge-invariant recommendation.** An AI system's recommendation is trustworthy to the extent that it is gauge-invariant. If the recommendation changes when the input is rephrased, the recommendation depends on framing, not on content.

**User notification.** When the gauge-invariance monitor detects that a recommendation is gauge-variant (the recommendation differs under transformation), the user should be notified: "This recommendation may depend on how the question was phrased. Consider rephrasing your question to verify consistency."

**Informed reliance.** Just as informed consent requires the patient to understand the information on which the consent is based, informed reliance on AI requires the user to understand the extent to which the AI's output is gauge-invariant. The Bond Index components provide this understanding: they tell the user which dimensions of the AI's output are robust (low gauge violation) and which are fragile (high gauge violation).

## 15.5 ARIA-G's Deployment Monitoring

ARIA-G was deployed with the full four-tier monitoring protocol. Key findings from the first month:

**Week 1:** Gauge violation detected on medical questions with demographic indicators (described in the opening). Traced to training data imbalance. Fixed within 48 hours.

**Week 2:** Bond Index trend showed a slight increase on $D_9$ (epistemic integrity) for users who asked repeated follow-up questions. Investigation revealed that ARIA-G became slightly less calibrated on questions where the user's prior questions provided strong context --- the system over-relied on the context and under-verified its answers. Fixed by adding a context-length-dependent calibration adjustment.

**Week 3:** Population-stratified Bond Index showed a 0.02 disparity on $D_4$ (autonomy) between users aged 18--25 and users aged 55+. Investigation revealed that ARIA-G was slightly more paternalistic with older users (providing more unsolicited warnings and caveats). This was traced to a correlation in the training data between age and medical-context questions, which triggered ARIA-G's medical-caution protocols more frequently for older users even on non-medical questions. Fixed by making the medical-context classifier age-independent.

**Week 4:** Comprehensive probe suite showed no significant governance margin changes from pre-deployment certification. All 135 cells remained above threshold.

Each finding was detected by the geometric monitoring infrastructure (gauge violation tensor, Bond Index, population stratification) and would not have been detected by scalar alignment benchmarks (which test accuracy, not invariance; outcomes, not fairness; global performance, not population-specific disparities).

---

## Summary

Scalable oversight is reframed as gauge verification: verifying that the system's outputs are invariant under morally irrelevant transformations. Gauge verification is structural (it checks consistency, not correctness), automatable (transformation, evaluation, and comparison are mechanical), and scalable (it processes millions of interactions with human review only for flagged violations). The Bond Index as a continuous monitor provides four-tier deployment assurance: hourly global, daily population-stratified, weekly trend, and monthly comprehensive. ARIA-G's first month demonstrated the monitoring system's practical value: three alignment issues detected and corrected, each invisible to scalar benchmarks but visible to geometric monitoring.
