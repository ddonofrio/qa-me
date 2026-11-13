# Context checks

Read the applicable sections only. Start with the project's stated needs and evidence. These are prompts for risk assessment, not mandatory requirements for every product.

## User interfaces

Inspect critical journeys, loading and error states, supported devices and compatibility expectations. Include keyboard navigation, visible focus, understandable labels and errors, and meaningful alternatives to non-text information. Automated accessibility checks find some issues; user interaction and informed manual evaluation remain necessary. Ask which users and assistive technologies matter before claiming coverage.

## Services and integrations

Check contracts, authentication and authorization boundaries, invalid inputs, timeouts and partial failure. Consider retries, duplicate requests and idempotency when operations can have side effects. Determine whether callers can distinguish success, failure and uncertain completion. Use controlled contract or integration checks instead of relying only on mocks of external behavior.

## Data and state

Review schema changes, validation, precision, time zones and ordering where relevant. For imports and transformations, check completeness, duplicates, reconciliation and corrupt or partial inputs. Test recovery and migration against representative sanitized data. Successful backup creation does not demonstrate successful restoration.

## Security and privacy

Identify assets, trust boundaries and abuse paths relevant to the project. Inspect permission checks, sensitive-data handling, logging and dependency exposure. Do not infer secure behavior from a login screen or a clean scanner alone. Recommend targeted negative tests and specialist review when the risks exceed the available evidence. Assessment is not permission to probe live targets or retrieve credentials.

## Reliability and performance

Define the workload, data size and user-facing latency or availability expectation before selecting measurements. Include peak load, saturation, slow dependencies and recovery where those failures are credible. Compare distributions and errors, not just averages. State the environment and limits of a benchmark. A small local run cannot establish production capacity.

## Libraries, tools and desktop software

Consider supported platforms, public API or file-format compatibility, installation, upgrade and failure messages. Check behavior on missing permissions, interrupted writes and malformed input. Verify that automated checks exercise the packaged artifact where packaging itself could introduce faults.

## AI-assisted or nondeterministic features

Define acceptable outcomes and unacceptable failures independently of the model's prose. Use representative held-out cases and adversarial cases relevant to the actual task. Track model, prompt, tool and data versions. Evaluate repeated runs when variability matters. Test tool failures, context limits, recovery loops and human escalation without allowing partial or repeated tool calls to cause unapproved effects. A single persuasive answer is not a quality measure.
