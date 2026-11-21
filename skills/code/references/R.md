# R

Confirm the R version, package environment, input schema, and whether the work is package code, analysis, or reporting. Follow the project's base R or tidyverse conventions and preserve the meaning of the analysis.

- Put transformations in functions with explicit inputs and outputs. Keep files, options, locale, time zone, random seeds, and data paths at the calling boundary. Make join keys and expected cardinality explicit. Check that grouping and ordering leave the data in the shape the next step expects.
- Specify how to handle `NA`, `NaN`, empty vectors, and coercion. Use the missing-value predicates appropriate to the contract. Avoid accidental recycling or partial matching; check vector lengths and names when they matter. Use `drop = FALSE` when matrix or data frame subsets must retain dimensions.
- Separate calculation from plotting and I/O so results can be tested on small frames. In packages, declare dependencies and export only supported interfaces. Use library-scoped tools and restore deliberate session changes. For reproducible analysis, record inputs, package versions and any relevant seed.
- Profile time and allocation on realistic data. Use vectorized operations when they express the operation clearly and fit memory. Preallocate growing output when known; a vectorized expression may still allocate large intermediates. Consider chunking or database-backed execution when data size makes in-memory copies untenable.

Use a focused test with missing values, repeated keys, one-row and zero-row inputs as relevant. Compare floating-point results with a domain-appropriate tolerance. Run the project's package or reproducibility checks from a clean session; compare runtime and peak memory before claiming improvement.
