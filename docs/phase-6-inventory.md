# Phase 6 computation inventory

This inventory is based on static inspection only. No program beneath
`content/` was executed, imported, compiled, or modified. CRAIG's computation
workers execute reviewed kernels implemented in `craig/computation/`; they
never dispatch a corpus path or arbitrary command.

## First-release allowlist

| Operation | Corpus basis | Classification | Public bounds |
| --- | --- | --- | --- |
| `dyck_path_statistics` | `middle_coefficients/code.py:82-186` | Example | Semilength 1-80 |
| `enumerate_dyck_paths` | `middle_coefficients/code.py:82-186` | Exhaustive finite check | Semilength 1-10 |
| `enumerate_rational_dyck_paths` | `conjectured_rational_formula/code.py:67-249` | Exhaustive finite check | Coprime `2 <= r,s <= 10` |
| `type_c_hecke_word` | `type_c_grothendieck/code.py:42-62` | Example | Rank 1-7; at most 80 generators |

The implementations preserve the inspected conventions but are independently
bounded application kernels. They do not import a source file from `content/`.
Each operation has a fixed schema, version, evidence label, resource profile,
and optional trusted Phase 5 visualization.

## Deferred programs

| Corpus program | Static risk classification | Reason it is not executable in the first release |
| --- | --- | --- |
| `dyck_symmetric_CAPs/code.py` | Heavy / composite | Multiple substantial finite-check drivers are combined in one large script. |
| `conjectured_formula_CAPs/code.py` | Heavy | Exponential record generation and proof-oriented claims need a separate review. |
| `dyck_symmetric_functions/code.py` | Heavy | Enumerates words and tableaux across several modes. |
| `middle_coefficients/code.py` | Mixed | Only the small classical Dyck primitives are adapted; grid checks remain deferred. |
| `string_decompositions/code.py` | Heavy | Large rational enumeration and local-map verification surface. |
| `conjectured_rational_formula/code.py` | Heavy / multiprocessing | The full driver can spawn pools and run broad grids; only its Catalan count is adapted. |
| `type_c_grothendieck/code.py` | Mixed | Only deterministic 0-Hecke word evaluation is adapted; global counting is deferred. |
| `type_c_grothendieck/code_cpp.cpp` | Heavy / native | Native compilation, threads, and large packed tables require a separate sandbox profile. |
| `shifted_littlewood_richardson/code.py` | Heavy | Recursive tableau generation has a large combinatorial state space. |
| `shifted_littlewood_richardson/optimized.cpp` | Heavy / native | Boost dependency, native compilation, and large enumerations. |
| `skeleton_tableau_formulas/code.py.py` | Medium-heavy | Bounded tau-Dyck enumeration is a candidate for a later allowlist revision. |

## Approval criteria

An operation can enter the public registry only when all of the following hold:

1. Its parameters have closed schemas with conservative numeric and collection
   bounds.
2. Its implementation lives outside `content/` and has no filesystem, network,
   subprocess, dynamic-import, or evaluation capability.
3. It runs in CRAIG's isolated worker protocol, not in the API process.
4. Wall time, CPU time, memory, stdout, stderr, request size, result size, and
   concurrency are bounded.
5. Results carry normalized parameters, implementation version and hash,
   request and result hashes, runtime measurements, limits, and an evidence
   classification.
6. A finite run is never described as a proof of an unbounded statement.
7. Any visualization is emitted as a trusted Phase 5 schema, never raw HTML or
   SVG.

Adding a program to this document does not approve it. Approval requires a new
registry entry, tests, and review of its resource profile.
