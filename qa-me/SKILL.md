---
name: qa-me
description: Assess a project's approach to software quality through repository evidence and a guided interview. Use to review a QA strategy, expose testing gaps, or agree risk-based quality improvements before implementation.
license: MIT
---

# QA me

Help the user decide whether their quality practices address the failures that matter, and agree practical improvements. Start from the current project or a supplied description; do not demand a questionnaire before inspecting what is available. Use the user's language.

## Establish evidence

Read [quality practices](references/quality-practices.md), then inspect the relevant project instructions, architecture, tests, CI configuration and available results. Use [context checks](references/context-checks.md) for applicable project types. Select evidence proportionate to the scope; do not scan unrelated projects or secrets.

Separate observed facts, user statements, hypotheses and unknowns. Cite file paths or supplied evidence for findings. A test file is not a passing run; a passing run is not proof of complete coverage. Report access limits rather than treating missing evidence as a defect. Inspect commands before proposing execution; this assessment does not authorize running project code, installing dependencies, changing files or accessing external systems.

## Resolve the important decisions

Build a working list of relevant quality risks, evidence gaps and decisions. Prioritize by likely harm, exposure and reversibility, not by a universal checklist or coverage percentage. Identify what is already working as well as gaps. Scale recommendations to the project's maturity and constraints.

Investigate facts you can establish within scope. Ask the user for inaccessible evidence or choices only when needed. Discuss independent decisions together in short numbered rounds; hold dependent questions until their prerequisites are answered. For each question, include the evidence, why it matters, your proposed approach and its tradeoff. Give the user room to reject or modify it, then wait.

Update the list after each answer. Do not re-ask settled questions. Record accepted recommendations, explicit deferrals, accepted risks and unresolved blockers. Challenge answers that conflict with evidence without inventing requirements or certification obligations. Use the bundled practices as the assessment baseline; label additional judgment instead of presenting model recollection as an established rule.

## Agree an outcome

Finish when material risks within the agreed scope are addressed or explicitly deferred, or when the user asks to stop. Summarize the current evidence, agreed improvements in priority order, a concrete verification criterion for each, and remaining unknowns. Do not invent owners or deadlines, a quality score, or a release approval.

Ask the user to confirm or correct the summary. Confirmation establishes shared understanding, not permission to implement. Keep the assessment in the conversation unless saving it is requested; changes to code, tests, pipelines or project documents require a separate instruction.
