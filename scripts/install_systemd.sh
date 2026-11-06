#!/usr/bin/env bash
# ==============================================================================
# HCOS FORINA TITAN — SYSTEMD USER SERVICE INSTALLER (ARCH / LINUX)
# Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "${SCRIPT_DIR}")"
SYSTEMD_USER_DIR="${HOME}/.config/systemd/user"
mkdir -p "${SYSTEMD_USER_DIR}"

echo "Erstelle systemd User Services fuer HCOS Forina Titan..."

# 1. Engine & Live-Sync Server (Port 4000)
cat <<EOF > "${SYSTEMD_USER_DIR}/forina-engine.service"
[Unit]
Description=HCOS Forina Titan Pipeline Engine & Live-Sync Gateway
After=network.target

[Service]
Type=simple
WorkingDirectory=${PROJECT_ROOT}
ExecStart=/usr/bin/python3 ${PROJECT_ROOT}/forina.py serve --port 4000
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
echo "Systemd Service angelegt! Zum Aktivieren:"
echo "systemctl --user enable --now forina-engine.service"
