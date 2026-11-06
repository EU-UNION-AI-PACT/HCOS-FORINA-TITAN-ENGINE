#!/usr/bin/env bash
# ==============================================================================
# HCOS FORINA TITAN — CLI HELFER FUER NEUE API-MODULE
# Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
# ==============================================================================
set -euo pipefail

SLUG="${1:-neues-modul}"
TITLE="${2:-Dynamisches Forina Modul}"
VERSION="${3:-1.0.0}"
API_KEY="${4:-FORINA-TITAN-2026-SECRET}"
SERVER_PORT="${5:-4000}"

echo "Registriere Modul '${SLUG}' beim HCOS Engine Server auf Port ${SERVER_PORT}..."

curl -s -X POST "http://localhost:${SERVER_PORT}/api/modules/register" \
  -H "Content-Type: application/json" \
  -H "X-Forina-API-Key: ${API_KEY}" \
  -d "{
    \"id\": \"${SLUG}\",
    \"name\": \"${TITLE}\",
    \"version\": \"${VERSION}\",
    \"timestamp\": \"$(date -Iseconds)\",
    \"description\": \"Dynamisch ueber CLI registriertes Modul\",
    \"status\": \"active\"
  }"

echo ""
echo "Fertig! Abruf-URL:"
echo "http://localhost:${SERVER_PORT}/api/modules/load?name=${SLUG}"
