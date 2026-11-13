#!/usr/bin/env python3
"""Validate this package offline. No third-party dependencies or network access."""
from pathlib import Path
import re
import sys


def validate(root):
    errors = []
    skill = root / 'qa-me'
    required = ['SKILL.md', 'LICENSE', 'references/quality-practices.md',
                'references/context-checks.md', 'agents/openai.yaml']
    for name in required:
        if not (skill / name).is_file():
            errors.append(f'Missing skill file: {name}')
    if errors:
        return errors
    content = (skill / 'SKILL.md').read_text(encoding='utf-8')
    parts = content.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        return ['SKILL.md must begin with YAML frontmatter.']
    fields = dict(re.findall(r'^([a-z-]+):\s*(.+)$', parts[1], re.M))
    if fields.get('name') != skill.name:
        errors.append('Skill name must match its directory.')
    if not 1 <= len(fields.get('description', '')) <= 1024:
        errors.append('Description must contain 1–1024 characters.')
    if fields.get('license') != 'MIT':
        errors.append('Expected MIT license metadata.')
    for path in skill.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' not in target and not target.startswith('#'):
                linked = (path.parent / target.split('#')[0]).resolve()
                if not linked.is_relative_to(skill.resolve()) or not linked.is_file():
                    errors.append(f'Invalid bundled reference in {path.name}: {target}')
    if (root / 'LICENSE').read_bytes() != (skill / 'LICENSE').read_bytes():
        errors.append('Repository and installable skill licenses differ.')
    return errors


if __name__ == '__main__':
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(f'FAIL: {error}')
    print('Package checks passed.' if not errors else f'{len(errors)} check(s) failed.')
    sys.exit(bool(errors))
