# Claude Code

@README.md
@context/ue5-agent-operating-model.md

Claude Code project skills are exposed under `.claude/skills`. Those files are
thin wrappers that point at the canonical reusable skill bodies under `skills/`.

When updating a skill, edit the canonical `skills/<skill-name>/SKILL.md` first,
then update the matching `.claude/skills/<skill-name>/SKILL.md` wrapper only if
the trigger description or routing needs to change.
