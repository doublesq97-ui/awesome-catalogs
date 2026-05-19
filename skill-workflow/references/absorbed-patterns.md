# Absorbed Patterns

Reusable patterns observed across mature skill repos.

## Structure pattern: Single SKILL.md + references/

Most effective skills follow this layout:
```
skill-name/
├── SKILL.md          # Main instructions — lean, focused
└── references/       # Deep-dive material loaded on demand
```

The SKILL.md should be readable in under 2 minutes. Everything else goes in references.

## Trigger pattern: Explicit & implicit

Best skills define both:
- **Explicit triggers**: slash commands, keywords ("import skill from...")
- **Implicit triggers**: natural language ("can you add this to my skills?")

## Install pattern: Direct to ~/.claude/skills/

Successful install flow:
1. Clone/copy to temp
2. Normalize structure
3. Copy to `~/.claude/skills/<name>/`
4. Verify SKILL.md frontmatter is valid
5. Report success with invocation example

## Catalog pattern: Maintain a searchable index

Beyond installation, maintain a catalog so users can discover what they have. The catalog should be:
- One entry per line (table row)
- Searchable by name, domain, or keyword
- Updated automatically on install/remove
