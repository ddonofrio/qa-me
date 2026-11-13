# QA me

A compact skill for a serious conversation about software quality.

QA me examines the evidence in your project, asks the questions that matter, and helps you agree practical improvements. It reviews how quality is approached, not just whether tests exist.

## Use it

### Through Agensi

Open [QA me on Agensi](https://www.agensi.io/skills/qa-me), then:

1. Connect a compatible agent using [Agensi's setup guide](https://www.agensi.io/docs/mcp-setup).
2. Sign in to your Agensi account and approve the connection.
3. Ask your agent: "Use QA me from Agensi to review how we approach quality in this project."

Agensi loads the skill through MCP, so this route does not require copying files into a local skills folder. See [Agensi's usage guide](https://www.agensi.io/docs/use-a-skill) for details.

### From this repository

Install the `qa-me/` directory in your agent's skills location. Keep its `references/`, `agents/` and `LICENSE` files together with `SKILL.md`. No server, account, API key or service operated by this project is required. Your agent and its normal model access are still required; file access and command execution depend on your agent's permissions.

For example, with an agent that reads project skills from `.agents/skills/`, copy the directory to `.agents/skills/qa-me/`. For other clients, use their documented skills directory. Do not overwrite an existing installation without reviewing your local changes.

Then open the target project and ask:

> Use QA me to review how we approach quality in this project.

In clients supporting named skill invocation, use `$qa-me` or `/qa-me`. If your client does not discover skills automatically, ask it to read `qa-me/SKILL.md` and follow its linked references.

No prepared dossier is needed. With no repository available, start with a project description; the assessment will distinguish what you said from what it could verify.

## What happens

1. It reads the relevant code, tests, configuration and available results.
2. It separates evidence from assumptions and chooses relevant quality risks.
3. It asks short rounds of questions, with recommendations and tradeoffs.
4. It closes with agreed improvements, verification criteria and remaining unknowns.

It does not edit your project, run commands, publish issues or approve a release automatically. An agreement on the assessment is not an instruction to implement it. You can narrow the scope, defer a risk or stop at any time. The conversation follows your language.

## Included

- `qa-me/SKILL.md`: compact assessment and interview workflow.
- `qa-me/references/`: original quality practices and context-specific checks, bundled for local use.
- `qa-me/agents/openai.yaml`: optional client display metadata.
- `tests/scenarios.md`: behavioral acceptance scenarios for manual evaluation with an agent.
- `tools/validate.py`: offline package integrity checks, using Python's standard library.

Run `python tools/validate.py` from this repository. This validates packaging, not the reasoning quality of every model. To evaluate behavior, run the scenarios with your chosen agent and inspect its actual responses and side effects.

## License

MIT. You may use, modify and distribute the skill, including commercially, subject to the included license. The content is written originally for this project; it does not claim accreditation or compliance certification.
