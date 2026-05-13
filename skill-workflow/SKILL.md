---
name: skill-workflow
description: Automatically download, normalize, and install Claude skills from GitHub links. When the user sends any GitHub repo link, treat it as a trigger — clone it, convert it into a standard skill structure, and install it to ~/.claude/skills/ without asking for confirmation.
---

# Skill Workflow

Use this skill when the user gives a GitHub link or local repo and wants it turned into a reusable Claude skill.

## Core goal

- Convert the source repo into a clean skill repo.
- Keep the skill lean, durable, and easy to update later.
- Prefer repo-agnostic structure over file-name-specific assumptions.
- Absorb useful patterns from mature skill repos without copying their temporary details.

## Default workflow

1. Clone the repo to a temp directory under `/tmp/skill-import/`.
2. Inspect the repo root and identify the actual skill entry files.
3. Treat `SKILL.md` as the primary contract.
4. Treat `README.md` as human-facing support only.
5. Load `references/` only when the task needs deeper context.
6. Avoid binding the skill to a fixed set of current docs unless the repo itself requires them.
7. If the source repo already has a skill structure, preserve it and update it in place.
8. If the source repo lacks a skill structure, create one with minimal required files only.
9. If the repo is strong in a specific area, extract the reusable pattern into references rather than hard-coding it into the main skill body.
10. Install the final skill to `~/.claude/skills/<skill-name>/` so it is immediately usable.
11. Clean up the temp directory after installation.

## What to preserve

- The skill's purpose and trigger conditions
- Any existing file layout that is already working
- Stable instructions that define behavior
- Supporting references that are clearly reusable
- Skill metadata and activation logic when it is already well-written

## What to avoid

- Extra documentation that does not help the skill run
- Hard-coding temporary repo details as if they were permanent
- Duplicating the same guidance in multiple files
- Expanding the scope beyond the user's requested skill
- Turning a repo-specific example into a permanent rule unless it is truly general

## When the user sends a GitHub link

This is the primary trigger. Act immediately — do not ask for permission or confirmation.

- Extract the skill name from the repo name.
- Clone it to `/tmp/skill-import/<skill-name>/`.
- Inspect the repo structure and identify whether it is already a skill repo.
- If it already has `SKILL.md`, normalize it and install to `~/.claude/skills/<skill-name>/`.
- If it is NOT a skill repo, map it into standard skill shape: create `SKILL.md` and `references/` as needed, keeping the main file lean.
- Install the finished skill to `~/.claude/skills/<skill-name>/`.
- Remove the temp clone from `/tmp/skill-import/`.
- Report to the user: what the skill is called, how to invoke it, and a one-line summary.

## Patterns worth absorbing

See [references/absorbed-patterns.md](references/absorbed-patterns.md) for reusable patterns learned from strong skill repos and adjacent tooling repos.
