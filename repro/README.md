# RP01: exact finite verification materials

Prepared for the 2026-10-17 preprint, with its mathematical labels retained. These programs are supplementary finite checks. The proofs of the bounds and the general even-half-dimension classification are in the manuscript, not in an enumeration claim.

## Run

Use CPython 3.10 or newer with its standard library. No network, package installation, computer algebra system, external data, or third-party paper is required. The clean-copy executions recorded here used Python 3.13.3.

From this directory:

```sh
python3 code/run_checks.py light
python3 code/run_checks.py full
```

Do not use Python's `-O` option: assertions are part of these exact checks, and the entry point rejects optimized execution. An assertion failure or another error exits unsuccessfully. A successful command writes `results/checks_light.json` or `results/checks_full.json`. Existing result files are evidence of their recorded executions, not a claim that a later unsuccessful run passed.

Use `--output /path/to/result.json` to choose another JSON destination. There are no hard-coded personal paths. The result includes the Python version, actual execution time, UTC execution timestamp, and SHA-256 hashes of all shipped Python sources. Timing and timestamp are expected to differ across runs; mathematical results and source hashes can be compared directly.

## What light checks

`run_checks.py` uses polynomial-basis finite fields to define examples, then reconstructs each entire truth table from its binary algebraic normal form. It independently compares direct zero-plane counts with fast Walsh transforms and the third-moment identity. Thus the subgroup formula is not merely tested against the same formula implemented twice.

| Manuscript position | Actual finite check |
|---|---|
| Lemma 2.3; Proposition 3.2 | Direct zero vectors, ordered pairs and zero binary planes; `s=4z`, `J2=16T0`, `J2=3s-2+6v4`; comparison with the third Walsh moment. The two order-64 examples also enumerate actual Klein four subgroup sets in an explicit central extension. |
| Lemmas 4.1–4.3; Theorem 1.1 | Both `n=2` and `n=3` endpoints; all three scalar polars are nondegenerate and the Walsh spectra have the asserted magnitudes/signs. The eight-dimensional polynomial-basis teaching coordinates in Chinese §4.6 are also checked independently. These selected examples do not verify every parameter of Theorem 1.1. |
| Proposition 5.5 | The displayed target-fixed normalizing substitutions for every one of the 96 listed core maps, tested at all 256 vectors per map. Selection/exhaustiveness is checked separately by full mode and proved analytically in the paper. |
| Theorem 1.2; Example 7.1 | `Q_star` and `Q_star ⊥ H_+` give `v4=4371, 787019`; the compensated twelve-dimensional example has the same maximum `s=4288`, but `v4=819787`, so is not a lower-equality example. Raw phases/constants remain in the Walsh data. |
| Remark 6.4 | The four displayed `F4` columns map two negative planes to two positive planes, checked on all 256 vectors. Invertibility is checked over `F2`. All six target changes lift on `H_+`. Hence the double-negative remainder does not produce another equality type. |
| Lemma 7.2; Example 7.3 | The ten-dimensional odd lower example has `s=1120`, `v4=56443`. Minimal polynomials are calculated after all six target-basis choices: the odd example stays semisimple and the core stays nonsemisimple. This checks the specific obstruction, not classification of all odd cases. |
| Appendix A; CMP2018 equation (4) | Four specified complete core refinements, including a negative-origin-sign core and a generic refinement. For each, the common `F16` input formula is checked at all 256 inputs and all three nonzero output characters; the predicted raw phase is compared with a direct Walsh sum at every one of the 256 covectors. General `g` and original phase constants are retained. |
| Appendix B | The smallest version-specific MPG example has four common zeros; both printed target types have eight. The explicit form-swap is checked at all 16 inputs. An additional eight-dimensional comparison checks binary ANF against `F4` formulas and the residual `SL2(F4)` trace formula. The general inequivalence argument is the invariant zero count in Appendix B, not a failed search. |

The dimensions in this table are `dim_F2 V=2n`, not the group dimension; the group order is `4·2^(dim V)`. The symbol `s` includes the identity, and `v4` counts actual subgroups. All blocks use a common target. The code never replaces strict square-map equivalence by EA equivalence.

### Selected independently recomputed values

| Map | `dim_F2 V` | `s` | `v4` | raw three-dual character sum |
|---|---:|---:|---:|---:|
| `uv+u` | 4 | 28 | 53 | 0 |
| `uv` | 4 | 28 | 69 | 16 |
| `F8` negative endpoint | 6 | 88 | 431 | −8 |
| `F8` positive endpoint | 6 | 88 | 463 | 8 |
| `Q_star` | 8 | 304 | 4371 | −64 |
| odd lower example | 10 | 1120 | 56443 | −128 |
| `Q_star ⊥ H_+` | 12 | 4288 | 787019 | −1024 |
| negative core ⊥ negative plane | 12 | 4288 | 819787 | 1024 |

## What full adds

`full` repeats `light`, then runs `full_core.py`. This is a bounded census of all **65,536 complete linear refinements of one fixed eight-dimensional polar**. It uses shifted binary Walsh truth tables, rather than assuming the parameter-selection proof. It obtains:

- 10,336 refinements with maximum `s=304`;
- three-dual character-sum distribution `−64:96`, `0:9600`, `64:640` on that branch;
- equality of the 96-map parameter subset and the independently filtered Walsh subset;
- the raw core phase identity, including its constant, for all 65,536 refinements;
- 4,096 equal-sign tests and 4,096 raw semisimple-plane phase tests;
- a 96-element equality orbit under the eight displayed polar-isometry generators; the generated binary matrix group has order 3,840 and stabilizer order 40.

The theoretical identification of this group with the full componentwise isometry group is justified by the local-ring argument in the manuscript's Remark 5.6. The computation by itself does not prove generator sufficiency or classify other polar types. It scans neither all finite groups of a given order nor `GL(8,2)`. It is not an enumeration in arbitrary dimension.

## Actual execution record and provenance

The full census was executed successfully from a temporary clean whitelist release copy on 2026-10-17. The light checks were rerun successfully on 2026-10-18 after release metadata and licence updates; verification-code hashes remain unchanged. Both result files contain actual timings and source hashes, not a runtime promise. A new unrestricted census was not needed for these nonmathematical edits.

The present entry point reorganizes existing RP01 checks: the binary-ANF counting route from the sixth-round independent implementation; explicit normalizations from the fourth round; examples and mixed negative-plane basis from the fifth round; version-specific instances from the ninth round; and the common `F16` substitution from the eleventh round. The latter has been extended here from five covectors to all 256 covectors for four selected maps. These are not claimed as external peer review or as reproductions of unreceived review attachments.

`full_core.py` retains the sixth-round independently implemented binary truth-table census, with file-writing behavior removed so the common entry point controls all results. `mpg_instances.py` and `cmp_mm.py` expose their checks as functions. No third-party implementation is imported or bundled.

## Limits, authorship and licensing

No code proves the general spectral bound, paired-block theorem, general compensation-exclusion argument, or arbitrary-even-`n` normal-form theorem. The manuscript supplies those arguments and their external hypotheses. A passing census does not establish novelty. The MPG check concerns only the specified saved nineteen-page version, Proposition 7 on its p.14; it is not a claim that the whole algorithm or other versions fail.

Generative AI participated in developing and organizing these checks and in the surrounding mathematical work. The author's personal verification is not certified by these runs. Original verification code and finite-check data are licensed under MIT; the paper and explanation text are CC BY 4.0. MathJax is Apache-2.0. See `../LICENSE_SCOPE.md` for precise boundaries.
