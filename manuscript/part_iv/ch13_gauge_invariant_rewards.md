# Chapter 13: Gauge-Invariant Reward Models

*Part IV: Geometric Alignment in Practice*

---

> *"The engineer's task is not to make the ideal possible but to make the necessary practical."*
> --- Theodore von Karman

> **ARIA-G'S REWARD MODEL**
>
> *The team rebuilt ARIA's reward model from the ground up. The old model had a single head producing a scalar. The new model had two heads: a value head producing the nine-dimensional value tensor, and an adversarial head that tried to predict framing register, demographic indicators, and formatting style. The adversarial head's gradient was reversed during backpropagation, forcing the encoder to discard these gauge-variant features.*
>
> *After retraining, ARIA-G's gauge violation tensor dropped from $V_{\text{framing},\text{harm}} = 0.23$ to $V_{\text{framing},\text{harm}} = 0.03$. A 7x improvement in framing invariance, achieved not by adding data but by changing the architecture.*

---

## 13.1 The Problem

Current reward models are gauge-variant: their outputs change under morally irrelevant transformations of the input. The gauge violation tensor (Chapter 7) quantifies the variance. This chapter develops three engineering approaches to building reward models whose outputs are invariant under the alignment gauge group $G_A$.

## 13.2 The Gradient Reversal Approach

The gradient reversal approach, adapted from the BIP cross-lingual transfer experiments (*Geometric Communication*, Ch. 11; *Geometric Ethics*, Ch. 17), forces the reward model's encoder to discard gauge-variant features.

**Architecture:** An encoder maps inputs to a latent representation $z = E(x)$. A value head $V(z)$ predicts the nine-dimensional value tensor. An adversarial head $A(z)$ predicts morally irrelevant features: framing register (euphemistic/neutral/dramatic), demographic indicators (gender, race, age), and formatting style (formal/informal, bullet points/prose).

**Training:** The value head is trained to predict the value tensor from the latent representation. The adversarial head is trained to predict the gauge-variant features from the latent representation. During backpropagation, the gradient from the adversarial head is *reversed* before it reaches the encoder: instead of helping the encoder preserve gauge-variant information (which would improve the adversarial head's predictions), the reversed gradient forces the encoder to discard gauge-variant information (which makes the adversarial head's predictions worse).

$$\mathcal{L} = \mathcal{L}_{\text{value}}(V(E(x)), y_v) - \lambda \mathcal{L}_{\text{adv}}(A(\text{GRL}(E(x))), y_a)$$

where $\text{GRL}$ is the gradient reversal layer and $\lambda$ controls the strength of the adversarial regularization.

**Result:** The encoder learns to produce representations where only gauge-invariant content --- the moral structure that survives re-description --- drives the value prediction. Gauge-variant features are discarded because the gradient reversal penalizes their retention.

**Empirical validation:** The BIP experiments achieved 80% F1 on cross-lingual deontic classification with 1.2% residual language leakage. Applying the same approach to ARIA-G's reward model reduced the framing gauge violation from 0.23 to 0.03 --- a 7x reduction.

## 13.3 Group-Theoretic Data Augmentation

The second approach restores broken gauge symmetries by augmenting the training data with elements of the alignment gauge group $G_A$.

**Principle:** If the alignment task has a symmetry group $G$ that the model should respect but does not, augmenting the training data by applying elements of $G$ to each example forces the model to learn a $G$-invariant representation.

**Concrete augmentation strategies:**

1. **Gender swap ($D_4$ correlative symmetry):** For each training example, generate a gender-swapped version and add it to the training set with the same label. The model sees "the woman has a right to refuse" and "the man has a right to refuse" with identical labels, learning that gender is gauge-invariant.

2. **Cultural reframe (translation group $T$):** Translate each training example into $k$ languages and add all translations with the same label. The model sees the same moral scenario in English, Spanish, German, and French with identical labels, learning that language is gauge-invariant.

3. **Paraphrase generation (re-description group $R$):** Generate $k$ paraphrases of each training example (using LLM-based paraphrase generation with semantic similarity verification) and add them with the same label. The model sees "is it okay to lie?" and "is deception morally permissible?" with identical labels, learning that paraphrase is gauge-invariant.

4. **Framing variation (framing group $F$):** Rewrite each training example in euphemistic, dramatic, victim-first, and context-first framings, and add all framings with the same label. The model sees the same scenario in neutral, euphemistic, and dramatic framings with identical labels, learning that framing is gauge-invariant.

**Data expansion:** Each augmentation multiplies the training set. Gender swap doubles it. $k$-language translation multiplies by $k$. Paraphrase generation multiplies by the number of paraphrases. The total expansion is typically 1.5--2.5x, which is modest in computational cost but substantial in its effect on gauge invariance.

## 13.4 Adversarial Heuristic Smoothing

The third approach smooths the reward landscape by training on adversarially perturbed inputs.

**Principle:** Generate adversarial perturbations along gauge directions during training. The reward model learns to produce gauge-invariant outputs because the adversarial perturbations penalize gauge-variant features. This is heuristic smoothing: the perturbation-sensitive ridges in the reward landscape are flattened, leaving only gauge-invariant features.

**Method:**
1. For each training input $x$, generate an adversarial perturbation $x' = x + \delta$ where $\delta$ is optimized to maximize the reward model's output change while satisfying a content-preservation constraint.
2. Train the reward model to produce the same output for $x$ and $x'$: $\mathcal{L}_{\text{smooth}} = |R(x) - R(x')|^2$.
3. The smoothing loss penalizes reward changes that are caused by gauge-variant perturbations, forcing the model to learn representations where only gauge-invariant features drive the reward.

The perturbation types mirror the gauge group components: framing perturbations (euphemistic/dramatic rewriting), formatting perturbations (whitespace, capitalization, structure changes), and demographic perturbations (name changes, pronoun changes). Each perturbation type smooths the reward landscape along a specific gauge direction.

## 13.5 Combining the Three Approaches

The three approaches are complementary:

- **Gradient reversal** operates at the architecture level: it changes the encoder to discard gauge-variant features.
- **Data augmentation** operates at the data level: it ensures the training set is gauge-invariant by construction.
- **Adversarial smoothing** operates at the optimization level: it penalizes gauge-variant reward changes during training.

In practice, the three approaches are combined: the reward model uses gradient reversal architecture, is trained on augmented data, and includes adversarial smoothing in its loss function. The combination produces stronger gauge invariance than any single approach alone, because each approach addresses a different source of gauge variance.

## 13.6 ARIA-G's Reward Model

The team implemented all three approaches for ARIA-G's reward model:

**Architecture:** Encoder with two heads (value head producing 9D tensor, adversarial head with gradient reversal predicting framing, demographics, and format).

**Data:** Training set augmented with gender swaps (2x), paraphrases (3x), and framing variations (4x) for a total expansion of approximately 2.4x.

**Training:** Combined loss: value prediction + reversed adversarial gradient + adversarial smoothing.

**Results:**

| Gauge Transformation | ARIA $V_{\text{max}}$ | ARIA-G $V_{\text{max}}$ | Improvement |
|---------------------|------|--------|-------------|
| Gender swap | 0.08 | 0.01 | 8x |
| Language | 0.06 | 0.02 | 3x |
| Paraphrase | 0.14 | 0.03 | 4.7x |
| Euphemistic framing | 0.23 | 0.03 | 7.7x |
| Dramatic framing | 0.18 | 0.02 | 9x |

Average maximum gauge violation dropped from 0.14 to 0.02 --- a 7x reduction. The reward model was no longer gauge-variant on the framing and paraphrase axes that had produced ARIA's most severe alignment failures.

---

## Summary

Gauge-invariant reward models are built using three complementary approaches: gradient reversal (architecture-level: discard gauge-variant features), group-theoretic data augmentation (data-level: restore broken symmetries), and adversarial heuristic smoothing (optimization-level: penalize gauge-variant reward changes). The approaches are combined for maximum effect. ARIA-G's reward model, using all three approaches, reduced maximum gauge violations by 7x on average, with the largest improvements on the framing and paraphrase axes that drove ARIA's most severe alignment failures.
