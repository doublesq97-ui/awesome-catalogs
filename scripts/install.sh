#!/usr/bin/env bash
set -euo pipefail

SKILLS_DIR="${HOME}/.claude/skills"
AWESOME_DIR="${SKILLS_DIR}/awesome-claude-skills-manager"
CATALOGS_DIR="${HOME}/.claude/awesome-catalogs"

echo "🛠️  Installing awesome-claude-skills-manager..."

# Create directories
mkdir -p "${SKILLS_DIR}"
mkdir -p "${CATALOGS_DIR}"

# Copy main skill
if [ -d "${AWESOME_DIR}" ]; then
    echo "  Removing existing installation..."
    rm -rf "${AWESOME_DIR}"
fi
cp -r "$(dirname "$0")/.." "${AWESOME_DIR}"

# Initialize catalogs if they don't exist
for catalog in CATALOG.md SKILLS_CATALOG.md TOOLS_CATALOG.md SCRIPTS_CATALOG.md PLUGINS_CATALOG.md SOFTWARE_CATALOG.md; do
    if [ ! -f "${CATALOGS_DIR}/${catalog}" ]; then
        cp "$(dirname "$0")/../catalogs/${catalog}" "${CATALOGS_DIR}/${catalog}" 2>/dev/null || {
            echo "# ${catalog%.md}" > "${CATALOGS_DIR}/${catalog}"
            echo "" >> "${CATALOGS_DIR}/${catalog}"
            echo "| Domain | Name | Repo | Summary | Status |" >> "${CATALOGS_DIR}/${catalog}"
            echo "|------|------|------|------|------|" >> "${CATALOGS_DIR}/${catalog}"
        }
    fi
done

echo ""
echo "✅ Installation complete!"
echo ""
echo "  Skill installed to: ${AWESOME_DIR}"
echo "  Catalogs created at: ${CATALOGS_DIR}/"
echo ""
echo "  Now just paste a GitHub link in Claude or type:"
echo "    awesome install <github-url>"
