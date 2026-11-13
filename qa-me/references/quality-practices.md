# Quality practices

Use these original review criteria to choose useful questions, not as a compulsory maturity model. A practice is relevant when it reduces an identified risk at a reasonable cost. These notes support an assessment; they do not constitute certification or exhaustive regulatory guidance.

## Purpose and risk

Establish who uses the product, the critical journeys, and the consequences of incorrect behavior. Distinguish financial loss, lost data, safety impact, privacy exposure, blocked work and inconvenience. Ask who can accept residual risk. A prototype and a system controlling physical equipment need different evidence before release.

Connect each important risk to an observable outcome and a check that could disprove it. Clarify ambiguous requirements with examples and counterexamples. Distinguish a missing requirement from an implementation defect. When obligations are contractual or regulated, ask for the applicable requirements and evidence rather than guessing them.

## Test design and coverage

Map critical behavior to tests at suitable boundaries: small deterministic logic checks, integration checks for collaborating parts, and a limited set of complete user journeys. Choose the cheapest layer that can detect the failure faithfully; neither mocks nor full-system tests replace all other layers.

Include representative valid and invalid inputs, boundary values, meaningful combinations, state transitions and interrupted operations. Check invariants such as conservation of amounts or uniqueness where the domain supports them. Compare results to an independent expectation, not merely to the same implementation used to compute them.

Review assertions, not only counts. A test that only checks for a nonempty result may miss an incorrect result. Coverage can locate unexercised code but cannot prove that assertions or requirements are sufficient. Do not prescribe a universal percentage. Use defects that escaped and changes in critical paths to target regression checks.

## Feedback and maintainability

Tests should be reproducible with controlled data and isolated state. Record dependencies, environment and the command needed to reproduce a failure. Prefer checks of externally meaningful behavior over incidental implementation details. Avoid arbitrary sleeps when an observable condition can be awaited.

Treat flaky tests as a loss of confidence: distinguish product nondeterminism, environmental instability and test defects. Retries can collect evidence but must not silently turn an unstable failure into a clean pass. Quarantine only with visible scope, an owner and a recovery plan agreed by the team.

## Delivery and recovery

Check which validations actually run on changes and which failures block delivery. A workflow file alone does not demonstrate enforcement. Keep fast feedback early and slower or environment-dependent checks at a suitable stage. Confirm test artifacts, failed cases and relevant logs are available for diagnosis without leaking secrets.

For deployed systems, examine compatibility across versions, configuration changes, migrations and the ability to restore service. A rollback plan must account for irreversible data changes. Identify how a limited rollout could reveal trouble and what observable condition would halt it. Practice recovery using safe test data where justified.

## People and learning

Clarify who reviews quality risks, investigates failures and accepts release tradeoffs. Make unresolved defects and accepted risks visible. Repeated incidents should change a test, control, requirement or operating practice rather than merely produce another document.

Exploratory testing complements scripted checks when interactions, user behavior or requirements are uncertain. Give an exploration a goal, a time boundary and a way to retain findings. Involve people who understand the users and domain. A lack of repository evidence for these practices warrants a question, not a claim that nobody does them.
