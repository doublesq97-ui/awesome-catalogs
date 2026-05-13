# Classification Rules

v1 checks repository signals in this order:

1. `SKILL.md` at repo root -> `skill`
2. MCP or Claude/Codex plugin markers -> `plugin`
3. single script file repo -> `script`
4. CLI entry point or package executable -> `tool`
5. fallback -> `software`

The classifier is intentionally rule-based in v1. Later versions can add GitHub metadata, topics, star history, and stronger duplicate detection.
