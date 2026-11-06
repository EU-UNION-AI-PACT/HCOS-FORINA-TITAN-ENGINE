"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
FORINA TITAN CLI INTERFACE
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from .engine import ForinaTitanEngine
from .server import run_engine_server
from .spec_sync import SpecSyncEngine
from .certification import SovereignCertifier


def main():
    parser = argparse.ArgumentParser(
        prog="forina",
        description="HCOS FORINA TITAN — Pipeline Engine & Live Spec Realisierungs-Radar"
    )
    subparsers = parser.add_subparsers(dest="command", help="Verfuegbare Engine-Befehle")

    # plan
    subparsers.add_parser("plan", help="Zeigt den Pipeline-Ablaufplan und Konfiguration an")

    # build
    subparsers.add_parser("build", help="Fuehrt die gesamte Release- und Build-Pipeline aus")

    # verify-spec
    subparsers.add_parser("verify-spec", help="Verifiziert alle Module live gegen die Spezifikation")

    # certify
    subparsers.add_parser("certify", help="Generiert das kryptografische Souveraenitaets-Zertifikat")

    # sync-live
    subparsers.add_parser("sync-live", help="Gibt den aktuellen Live-Sync Status als JSON aus")

    # serve
    serve_parser = subparsers.add_parser("serve", help="Startet den lokalen Engine- und Live-Sync-Server")
    serve_parser.add_argument("--port", type=int, default=4000, help="Port fuer den Server (Standard: 4000)")

    # push-repo
    push_parser = subparsers.add_parser("push-repo", help="Pusht das Repository zu GitHub")
    push_parser.add_argument("--repo-url", type=str, default="", help="GitHub Remote URL")

    args = parser.parse_args()
    project_root = Path(__file__).parent.parent

    if args.command == "plan":
        engine = ForinaTitanEngine(project_root)
        plan_data = engine.plan()
        print(json.dumps(plan_data, indent=2, ensure_ascii=False))

    elif args.command == "build":
        engine = ForinaTitanEngine(project_root)
        print(">>> Starte FORINA TITAN Build-Pipeline...")
        report = engine.run_pipeline()
        print(json.dumps(report, indent=2, ensure_ascii=False))
        if report.get("status") == "SUCCESS":
            print("\n[SUCCESS] Pipeline erfolgreich abgeschlossen! Release bereit.")
            sys.exit(0)
        else:
            print("\n[ERROR] Pipeline fehlgeschlagen.")
            sys.exit(1)

    elif args.command == "verify-spec":
        sync = SpecSyncEngine(project_root)
        res = sync.verify_all_modules()
        print("==================================================================")
        print(f" HCOS SPEC-SYNC RADAR: {res['engine_status']}")
        print(f" Spezifikation: {res['spec']['path']} ({res['spec']['size_bytes']} Bytes)")
        print(f" Realisierungsgrad: {res['overall_percentage']}% ({res['realized_count']}/{res['total_modules']} Module)")
        print("==================================================================")
        for m in res["modules"]:
            status_sym = "[x] REALISIERT" if m["realized"] else "[ ] AUSSTEHEND"
            print(f" - {m['name']:<45} | {status_sym} | Score: {m['score']}% | Light: {m['light_state']}")
        print("==================================================================")

    elif args.command == "certify":
        certifier = SovereignCertifier(project_root)
        cert = certifier.generate_certificate()
        print("🌟 ============================================================================= 🌟")
        print("   HCOS - SOVEREIGN DIGITAL SYSTEM CERTIFICATION")
        print("   Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.")
        print("===================================================================================")
        print(f" Inhaber / Trademark:    {cert['metadata']['author_and_creator']} ({cert['metadata']['trademark']})")
        print(f" Royal Kaiser Charter:   PIC: {cert['metadata']['certifications']['royal_kaiser_charter_regsys']['pic']} | VAT: {cert['metadata']['certifications']['royal_kaiser_charter_regsys']['vat']}")
        print(f" D-U-N-S / LEI:          {cert['metadata']['certifications']['duns_numbers']} | LEI: {cert['metadata']['certifications']['global_lei']}")
        print(f" UNGM Identifier:        {cert['metadata']['certifications']['ungm_id']}")
        print(f" Codebase Merkle Root:   {cert['codebase_attestation']['merkle_root']}")
        print(f" Sovereign Digital Seal: {cert['cryptographic_signatures']['digital_seal'][:64]}...")
        print(f" Validierungsstatus:     {cert['cryptographic_signatures']['validation_status']}")
        print("===================================================================================")
        print(f" [OK] Zertifikat erfolgreich erstellt unter: {project_root / 'certificates/CERTIFICATION.md'}")
        print("===================================================================================")

    elif args.command == "sync-live":
        sync = SpecSyncEngine(project_root)
        print(json.dumps(sync.verify_all_modules(), indent=2, ensure_ascii=False))

    elif args.command == "serve":
        run_engine_server(port=args.port, project_root=project_root)

    elif args.command == "push-repo":
        url = args.repo_url or "https://github.com/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE.git"
        print(f">>> Synchronisiere & Pushe zu GitHub: {url}")
        subprocess.run(["git", "add", "."], cwd=project_root, check=True)
        subprocess.run(["git", "commit", "-m", "HCOS FORINA TITAN Engine: Full Pipeline, Live Spec Sync & Copyright Notice"], cwd=project_root)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=project_root, check=True)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
