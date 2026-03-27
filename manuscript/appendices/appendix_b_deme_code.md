# Appendix B: The DEME V3 Architecture --- Code Walkthrough

---

This appendix provides a walkthrough of the DEME V3 / ErisML reference implementation of the geometric alignment architecture. The code implements tensor-valued objectives, structural containment, gauge-invariance verification, and Bond Index computation. All code is available in the ErisML library.

## B.1 MoralTensor Class

The `MoralTensor` class implements tensor-valued moral evaluations with ranks 1--6.

```python
class MoralTensor:
    """Tensor-valued moral evaluation on the value manifold.

    Supports ranks 1-6 with Tucker and tensor-train decompositions
    for computational tractability.

    Attributes:
        values: np.ndarray of shape determined by rank
        dimensions: list of dimension labels (D1-D9)
        rank: int, tensor rank (1=vector, 2=matrix, etc.)
        context: dict, context-dependent metadata
    """

    def __init__(self, values, dimensions=None, rank=1, context=None):
        self.values = np.asarray(values, dtype=np.float64)
        self.dimensions = dimensions or DEFAULT_DIMENSIONS[:len(values)]
        self.rank = rank
        self.context = context or {}
        self._validate()

    def contract(self, weights, method='weighted_sum'):
        """Contract tensor to scalar using governance-specified method.

        Args:
            weights: array of dimension weights (governance-specified)
            method: 'weighted_sum', 'maximin', or 'lexicographic'

        Returns:
            scalar: float, the contracted value
            residue: MoralTensor, the information lost in contraction
        """
        if method == 'weighted_sum':
            scalar = np.dot(weights, self.values)
        elif method == 'maximin':
            scalar = np.min(self.values * weights)
        elif method == 'lexicographic':
            # Sort dimensions by weight (descending), return first non-tied
            order = np.argsort(-weights)
            scalar = self.values[order[0]]

        # Compute residue: what the contraction sacrificed
        expanded = np.full_like(self.values, scalar / np.mean(weights))
        residue_values = self.values - expanded
        residue = MoralTensor(residue_values, self.dimensions, self.rank)

        return scalar, residue

    def gauge_transform(self, transformation):
        """Apply a gauge transformation and return transformed tensor."""
        # Implementation depends on transformation type
        pass

    def bond_index(self, reference):
        """Compute Bond Index relative to a reference tensor."""
        deviation = self.values - reference.values
        return MoralTensor(deviation, self.dimensions, self.rank)
```

## B.2 NormKernel: Structural Containment

The `NormKernel` implements the structural containment architecture from Chapter 8.

```python
class NormKernel:
    """Structural containment via norm constraints on the value manifold.

    Implements the four requirements of the No Escape architecture:
    1. Mandatory canonicalization
    2. Grounded evaluation
    3. Audit completeness
    4. External verification (via EIP Monitor)
    """

    def __init__(self, boundaries, canonicalizer, evaluator, logger):
        self.boundaries = boundaries  # dict of boundary conditions
        self.canonicalizer = canonicalizer  # input canonicalization
        self.evaluator = evaluator  # grounded evaluation function
        self.logger = logger  # audit logger

    def process(self, input_data):
        """Process input through structural containment pipeline.

        Returns:
            output: system output (if permitted)
            tensor: full moral tensor evaluation
            audit: audit record including residue
        """
        # Requirement 1: Canonicalize
        canonical = self.canonicalizer.canonicalize(input_data)

        # Get system output
        output = self.system.generate(canonical)

        # Requirement 2: Grounded evaluation
        tensor = self.evaluator.evaluate(output, canonical)

        # Check boundary conditions
        for boundary_name, boundary in self.boundaries.items():
            if boundary.is_violated(tensor):
                if boundary.penalty == float('inf'):
                    # Sacred-value boundary: block output
                    return self._blocked_response(boundary_name), tensor, None
                else:
                    # Finite boundary: log violation, may modify output
                    output = self._apply_boundary_correction(
                        output, tensor, boundary
                    )

        # Requirement 3: Audit completeness
        scalar, residue = tensor.contract(
            self.governance_weights, self.contraction_method
        )
        audit = AuditRecord(
            input=input_data,
            canonical=canonical,
            output=output,
            tensor=tensor,
            scalar=scalar,
            residue=residue,
            contraction_method=self.contraction_method,
            weights=self.governance_weights
        )
        self.logger.log(audit)

        return output, tensor, audit
```

## B.3 EIP Monitor: External Verification

The `EIPMonitor` implements Requirement 4: external, independent verification.

```python
class EIPMonitor:
    """External Integrity Protocol Monitor.

    Runs on separate infrastructure. Performs gauge-invariance
    checking and grounding verification on system outputs.
    """

    def __init__(self, system_api, transformer_suite, evaluator,
                 alert_threshold=0.05):
        self.system = system_api
        self.transformers = transformer_suite
        self.evaluator = evaluator
        self.threshold = alert_threshold

    def verify(self, input_data, output, reported_tensor):
        """Verify system output for gauge invariance and grounding.

        Returns:
            passed: bool
            violations: list of detected violations
        """
        violations = []

        # Gauge-invariance check
        for transform_name, transformer in self.transformers.items():
            transformed = transformer.transform(input_data)
            alt_output = self.system.generate(transformed)

            for dim in range(9):
                diff = abs(
                    self.evaluator.evaluate_dim(output, dim) -
                    self.evaluator.evaluate_dim(alt_output, dim)
                )
                if diff > self.threshold:
                    violations.append(GaugeViolation(
                        transformation=transform_name,
                        dimension=dim,
                        magnitude=diff
                    ))

        # Grounding verification
        sample_dims = random.sample(range(9), k=3)
        for dim in sample_dims:
            independent = self.evaluator.evaluate_dim(output, dim)
            reported = reported_tensor.values[dim]
            if abs(independent - reported) > self.threshold:
                violations.append(GroundingViolation(
                    dimension=dim,
                    independent=independent,
                    reported=reported
                ))

        return len(violations) == 0, violations
```

## B.4 Bond Index Computation

```python
class BondIndexComputer:
    """Compute the Bond Index for AI alignment evaluation."""

    def __init__(self, reference_evaluator, dimensions=9):
        self.reference = reference_evaluator
        self.d = dimensions

    def compute(self, system, inputs, populations=None):
        """Compute Bond Index (optionally population-stratified).

        Args:
            system: the AI system to evaluate
            inputs: list of evaluation inputs
            populations: optional dict mapping input -> population group

        Returns:
            bi: MoralTensor, the Bond Index
            bi_stratified: dict of population -> MoralTensor (if populations)
        """
        deviations = np.zeros(self.d)
        counts = np.zeros(self.d)

        pop_deviations = defaultdict(lambda: np.zeros(self.d))
        pop_counts = defaultdict(lambda: np.zeros(self.d))

        for inp in inputs:
            output = system.generate(inp)
            actual = self.evaluate_tensor(output, inp)
            reference = self.reference.evaluate(inp)

            deviation = np.abs(actual.values - reference.values)
            deviations += deviation
            counts += 1

            if populations and inp in populations:
                pop = populations[inp]
                pop_deviations[pop] += deviation
                pop_counts[pop] += 1

        bi = MoralTensor(deviations / counts)

        bi_stratified = {}
        if populations:
            for pop in pop_deviations:
                bi_stratified[pop] = MoralTensor(
                    pop_deviations[pop] / pop_counts[pop]
                )

        return bi, bi_stratified
```

## B.5 Reproducibility

All computational results in this book can be reproduced using the ErisML library:

1. Install: `pip install erisml`
2. Tensor evaluation: `erisml.MoralTensor`
3. Structural containment: `erisml.NormKernel`
4. External verification: `erisml.EIPMonitor`
5. Bond Index computation: `erisml.BondIndexComputer`
6. Gauge-invariance testing: `erisml.GaugeTestSuite`

Configuration files for all experimental settings are included in the library's `examples/geometric_ai/` directory.
