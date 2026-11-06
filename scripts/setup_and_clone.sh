#!/usr/bin/env bash
# ==============================================================================
# HCOS FORINA TITAN — OPEN SOURCE REPOSITORIES CLONING & VENDOR SETUP
# Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "${SCRIPT_DIR}")"
VENDOR_DIR="${PROJECT_ROOT}/vendor"

mkdir -p "${VENDOR_DIR}"/{app-engine,network,ui-ux,editors,iam-auth,ai-media,compliance-jmap,telemetry-booking}

clone_repo() {
    local category="$1"
    local name="$2"
    local url="$3"
    local target="${VENDOR_DIR}/${category}/${name}"

    if [ -d "${target}/.git" ]; then
        echo "[OK] ${name} existiert bereits unter vendor/${category}/${name}"
    else
        echo "[CLONE] Klone ${name} von ${url}..."
        git clone --depth 1 "${url}" "${target}" || echo "[WARN] Klonen uebersprungen: ${url}"
    fi
}

echo "=== Klone Kern-Repositories fuer Architektur & Sicherheits-Referenz ==="
clone_repo "app-engine" "tauri" "https://github.com/tauri-apps/tauri.git"
clone_repo "network" "caddy" "https://github.com/caddyserver/caddy.git"
clone_repo "ui-ux" "GSAP" "https://github.com/greensock/GSAP.git"
clone_repo "editors" "tiptap" "https://github.com/ueberdosis/tiptap.git"
clone_repo "iam-auth" "pocket-id" "https://github.com/pocket-id/pocket-id.git"
clone_repo "ai-media" "dify" "https://github.com/langgenius/dify.git"
clone_repo "compliance-jmap" "opa" "https://github.com/open-policy-agent/opa.git"
clone_repo "telemetry-booking" "umami" "https://github.com/umami-software/umami.git"

echo "=== Setup abgeschlossen ==="
