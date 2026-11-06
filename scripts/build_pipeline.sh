#!/usr/bin/env bash
# ==============================================================================
# HCOS FORINA TITAN — AUTOMATED PIPELINE & APPIMAGE BUILD SCRIPT
# Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "${SCRIPT_DIR}")"
TIMESTAMP="$(date +'%Y%m%d_%H%M%S')"

echo "=================================================================="
echo " [HCOS FORINA TITAN] Starte vollstaendige Build- & Release-Pipeline"
echo " Arbeitsverzeichnis: ${PROJECT_ROOT}"
echo " Zeitstempel:        ${TIMESTAMP}"
echo "=================================================================="

cd "${PROJECT_ROOT}"

# 1. Python Pipeline Engine ausfuehren
python3 forina.py build

# 2. Spezifikations-Live-Check ausfuehren
echo ""
python3 forina.py verify-spec

# 3. Optional: Wenn appimagetool installiert ist, echtes .AppImage bauen
APPDIR="${PROJECT_ROOT}/dist/AetherTitan.AppDir"
if command -v appimagetool >/dev/null 2>&1 && [ -d "${APPDIR}" ]; then
    echo ""
    echo "[AppImage] Kompiliere Standalone Linux-AppImage..."
    ARCH=x86_64 appimagetool "${APPDIR}" "${PROJECT_ROOT}/releases/ForinaTitan-${TIMESTAMP}-x86_64.AppImage"
    echo "  -> AppImage erfolgreich erstellt: releases/ForinaTitan-${TIMESTAMP}-x86_64.AppImage"
else
    echo ""
    echo "[AppImage] AppDir Staging bereit unter: ${APPDIR}"
fi

echo ""
echo "=================================================================="
echo " [BUILD PIPELINE] Erfolgreich abgeschlossen!"
echo " PWA bereit unter: dist/index.html"
echo " Releases unter:   releases/"
echo "=================================================================="
