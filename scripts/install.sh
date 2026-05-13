#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="${HOME}/.local/bin"
WRAPPER="${BIN_DIR}/awesome"

mkdir -p "${BIN_DIR}"

cat > "${WRAPPER}" <<EOF
#!/usr/bin/env bash
PYTHONPATH="${ROOT_DIR}:\${PYTHONPATH:-}" python3 -m awesome_catalogs "\$@"
EOF

chmod +x "${WRAPPER}"

echo "awesome-catalogs v1.1 installed"
echo "CLI: ${WRAPPER}"
echo "Try: awesome --help"
