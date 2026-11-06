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
    serve_parser = subparsers.add_parser("serve", help="Startet den lokalen Engine- und Live-Sync-Server (gehaertet)")
    serve_parser.add_argument("--host", type=str, default="127.0.0.1", help="Host-Adresse fuer Server-Binding (Standard: 127.0.0.1)")
    serve_parser.add_argument("--port", type=int, default=4000, help="Port fuer den Server (Standard: 4000)")

    # make-private
    subparsers.add_parser("make-private", help="Setzt das GitHub-Repository ueber die API auf privat")

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
            print(f" - {m['name']:<45} | {status_sym} | Spec: {m['spec_score']}% | PRL: {m['readiness_score']}% [{m['tier_badge']:<17}] | Light: {m['light_state']}")
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
        print(f" Ed25519 Signature:      {cert['cryptographic_signatures']['ed25519_signature_hex'][:64]}...")
        print(f" Algorithmus:            {cert['cryptographic_signatures']['algorithm']}")
        print(f" Validierungsstatus:     {cert['cryptographic_signatures']['validation_status']}")
        print("===================================================================================")
        print(f" [OK] Zertifikat erfolgreich erstellt unter: {project_root / 'certificates/CERTIFICATION.md'}")
        print("===================================================================================")

    elif args.command == "sync-live":
        sync = SpecSyncEngine(project_root)
        print(json.dumps(sync.verify_all_modules(), indent=2, ensure_ascii=False))

    elif args.command == "serve":
        run_engine_server(host=args.host, port=args.port, project_root=project_root)

    elif args.command == "make-private":
        import urllib.request
        token_path = Path("/home/shinehealthcare/Schreibtisch/API TOKENs/GitHub Token/Admin Org. - GitHub")
        if not token_path.exists():
            print("[ERROR] Kein GitHub Token gefunden unter:", token_path)
            sys.exit(1)
        token = token_path.read_text().strip().split()[-1]
        req = urllib.request.Request(
            "https://api.github.com/repos/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE",
            data=json.dumps({"private": True}).encode("utf-8"),
            headers={"Authorization": f"token {token}", "User-Agent": "HCOS-Engine", "Content-Type": "application/json"},
            method="PATCH"
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                print(f"[SUCCESS] Repository '{data.get('full_name')}' ist jetzt PRIVAT (private: {data.get('private')})!")
        except Exception as e:
            print("[ERROR] Konnte Repository nicht auf privat setzen:", e)
            sys.exit(1)

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
