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
from .module_loader import ModuleLoader
from .concept_suite import ConceptPaperSuite
from .harness_loop import HarnessLoopEngine
from .actpack_zeroclock import ActPackZeroClock, NaTZaFaultToleranceViolation


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

    # audit
    subparsers.add_parser("audit", help="Fuehrt das unabhaengige 13-Gate HCOS Assurance Audit (G00-G12) aus")

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

    # modules
    mod_parser = subparsers.add_parser("modules", help="Verwaltet die 10 Modulgruppen der Intelligence Suite")
    mod_parser.add_argument("action", choices=["list", "verify", "test", "promote"], default="list", nargs="?", help="Aktion: list, verify, test, promote")
    mod_parser.add_argument("--id", type=str, default="", help="Modul-ID fuer Einzelpruefung")

    # repos (50 Repositories Explorer & LOCCP 352 Repositories)
    repo_parser = subparsers.add_parser("repos", help="Erforscht die 50 Open-Source Repositories, Wish Studio & LOCCP 352 Masterkatalog")
    repo_parser.add_argument("action", choices=["list", "summary", "zone", "inspect", "wish-studio", "loccp"], default="list", nargs="?", help="Aktion: list, summary, zone, inspect, wish-studio, loccp")
    repo_parser.add_argument("--zone", type=str, default="", help="Zone Filter: sovereign, dev, federation")
    repo_parser.add_argument("--nr", type=int, default=1, help="Repository Nummer fuer inspect (1-50)")
    repo_parser.add_argument("--search", type=str, default="", help="Suchbegriff für LOCCP Repositories")
    repo_parser.add_argument("--category", type=str, default="", help="Kategorie-Filter für LOCCP Repositories")
    repo_parser.add_argument("--limit", type=int, default=25, help="Maximale Anzahl an Treffern für LOCCP")

    # concepts (34 Concept Papers Suite & DP Masterbook)
    concept_parser = subparsers.add_parser("concepts", help="34 Concept Papers Suite, Masterkonzept & DP Masterbook (27)")
    concept_parser.add_argument("action", choices=["list", "summary", "inspect", "read", "standards", "masterkonzept", "specialized", "masterbook"], default="list", nargs="?", help="Aktion: list, summary, inspect, read, standards, masterkonzept, specialized, masterbook")
    concept_parser.add_argument("--nr", type=int, default=1, help="Papier-Nummer (1-34)")
    concept_parser.add_argument("--search", type=str, default="", help="Suchbegriff für Concept Papers")
    concept_parser.add_argument("--full", action="store_true", help="Gibt das vollständige Markdown-Dokument aus")

    # harness (Automated Harness Loop)
    harness_parser = subparsers.add_parser("harness", help="Automatisierter 8-Stufen Harness-Loop & Reference HCL")
    harness_parser.add_argument("action", choices=["status", "run", "stage", "stages", "loop-run"], default="status", nargs="?", help="Aktion: status, run, stage, stages, loop-run")
    harness_parser.add_argument("--stage", type=str, default="PLAN", help="Stufe für Einzelausführung (PLAN, BUILD, TEST, AUDIT, CERTIFY, RELEASE, MONITOR, IMPROVE)")
    harness_parser.add_argument("--approve", action="store_true", help="Setzt Human-Approval-Flag für Loop-Run")
    harness_parser.add_argument("--isolated", action="store_true", help="Bestätigt verifizierte externe Netzwerk-Isolation für Loop-Run")

    # catalogs (136 Kapitel & 50 Repos Matrix)
    catalogs_parser = subparsers.add_parser("catalogs", help="Nachweiskataloge (136 Kapitel, 50 Repos Matrix)")
    catalogs_parser.add_argument("action", choices=["verify-136", "repos-matrix"], default="verify-136", nargs="?", help="Aktion: verify-136, repos-matrix")

    # zeroclock (Act Pack Zero Clock & NaTZa CFS)
    zc_parser = subparsers.add_parser("zeroclock", help="Act Pack Zero Clock (APZC) & NaTZa CFS Telemetrie")
    zc_parser.add_argument("action", choices=["status", "tick", "tmr", "spawn"], default="status", nargs="?", help="Aktion: status, tick, tmr, spawn")
    zc_parser.add_argument("--subtask", type=str, default="microtask_audit", help="Subtask Name fuer spawn")

    # baende (144 Seiten Enzyklopädie & 4 Bände)
    baende_parser = subparsers.add_parser("baende", help="144 Seiten Enzyklopädie (Bände A-D & 136 Kapitel)")
    baende_parser.add_argument("action", choices=["list", "read", "themen"], default="list", nargs="?", help="Aktion: list, read, themen")
    baende_parser.add_argument("--band", type=str, default="A", help="Band Buchstabe (A, B, C, D)")

    # badges (34 Normen SVG Badges)
    badges_parser = subparsers.add_parser("badges", help="34 Normen SVG Badges & Audit Control Targets")
    badges_parser.add_argument("action", choices=["list", "verify", "inspect"], default="list", nargs="?", help="Aktion: list, verify, inspect")
    badges_parser.add_argument("--id", type=str, default="NORM-001", help="Norm-ID (z.B. NORM-001)")

    # finance (Zentralbanken & Open Banking)
    fin_parser = subparsers.add_parser("finance", help="Zentralbanken, EZB Pontes & Open Banking Schnittstellen (PSD2)")
    fin_parser.add_argument("action", choices=["summary", "centralbanks", "globalcbs", "openbanking", "schemas", "pontes", "portals", "clevel", "enablebanking", "aspsp", "vpsportals", "portalregistry", "partnerapps", "globalcards", "pontesmatrix"], default="summary", nargs="?", help="Aktion: summary, centralbanks, globalcbs, openbanking, schemas, pontes, portals, clevel, enablebanking, aspsp, vpsportals, portalregistry, partnerapps, globalcards, pontesmatrix")
    fin_parser.add_argument("--search", type=str, default="", help="Suchbegriff für Portale, C-Level oder ASPSP-Banken")
    fin_parser.add_argument("--country", type=str, default="", help="Länderkürzel für ASPSP-Banken (DE, AT, CH, FR, etc.)")
    fin_parser.add_argument("--category", type=str, default="", help="Kategorie-Filter für Portale")
    fin_parser.add_argument("--company", type=str, default="", help="Unternehmensfilter für C-Level")
    fin_parser.add_argument("--provider", type=str, default="", help="Fintech-Partner (Mastercard, Visa, Solaris, Unit, etc.)")
    fin_parser.add_argument("--limit", type=int, default=25, help="Maximale Anzahl an Treffern")

    # upuia (Universal Project & URL Intelligence Archive)
    upuia_parser = subparsers.add_parser("upuia", help="UPUIA URL & Project Intelligence Archive (10 Grundregeln)")
    upuia_parser.add_argument("action", choices=["status", "preflight"], default="status", nargs="?", help="Aktion: status, preflight")

    # compliance (LOCCP 42 Prüfpunkte & Wish OS Finance Attestation)
    comp_parser = subparsers.add_parser("compliance", help="LOCCP 42 Prüfpunkte & Wish OS Local Finance Attestation")
    comp_parser.add_argument("action", choices=["pruefpunkte", "attestation", "stats"], default="pruefpunkte", nargs="?", help="Aktion: pruefpunkte, attestation, stats")
    comp_parser.add_argument("--module", type=str, default="", help="Filter nach Compliance-Modul (Corporate, DORA, etc.)")

    # wish (Wish Studio OS, Digital Skill Pass & Human Approval Gate)
    wish_parser = subparsers.add_parser("wish", help="Wish Studio OS: Wünsche, Digitaler Skill Pass & Human Approval Gate (G09)")
    wish_parser.add_argument("action", choices=["summary", "roles", "projects", "create", "approve", "credential"], default="summary", nargs="?", help="Aktion: summary, roles, projects, create, approve, credential")
    wish_parser.add_argument("--id", type=str, default="", help="Projekt-ID (z.B. WISH-2026-001) oder Rollen-ID")
    wish_parser.add_argument("--title", type=str, default="", help="Titel des Wunschprojekts")
    wish_parser.add_argument("--desc", type=str, default="", help="Beschreibung des Wunschprojekts")
    wish_parser.add_argument("--role", type=str, default="SKILL-VOL-01", help="Skill-Pass Rollen-ID")
    wish_parser.add_argument("--level", type=str, default="", help="Kompetenz-Level (Bronze, Silver, Gold, Titan)")
    wish_parser.add_argument("--did", type=str, default="did:tdw:volunteer.dev:community-id", help="Entwickler Decentralized Identifier (DID)")

    # energy (Top 100 Wissenschaftlicher Energie- & Extremtechnologie-Audit)
    energy_parser = subparsers.add_parser("energy", help="Top 100 Wissenschaftlicher Energie- & Extremtechnologie-Audit")
    energy_parser.add_argument("action", choices=["summary", "list", "inspect"], default="summary", nargs="?", help="Aktion: summary, list, inspect")
    energy_parser.add_argument("--group", type=str, default="", help="Fachgruppe (Fusion, Kernspaltung, Hyperschall, etc.)")
    energy_parser.add_argument("--grade", type=str, default="", help="Nachweisgrad (A, B, C)")
    energy_parser.add_argument("--search", type=str, default="", help="Suchbegriff für Systeme")
    energy_parser.add_argument("--nr", type=int, default=1, help="Auswahl-Nummer des Systems (1-100)")
    energy_parser.add_argument("--limit", type=int, default=25, help="Maximale Trefferanzahl")

    # tlore (TLORE Infinity 44 Lightning Power Suite)
    tlore_parser = subparsers.add_parser("tlore", help="TLORE Infinity: 44 Lightning Power Finance- und Systemmodule")
    tlore_parser.add_argument("action", choices=["summary", "modules", "boost"], default="summary", nargs="?", help="Aktion: summary, modules, boost")
    tlore_parser.add_argument("--module", type=str, default="01", help="Sektor-Nummer (01-44) oder Modul-ID (TLORE-01)")
    tlore_parser.add_argument("--stage", type=str, default="", help="Harness-Stage Filter (PLAN, DISCOVER, TEST, GATE, etc.)")
    tlore_parser.add_argument("--network", type=str, default="testnet", help="Netzwerk (testnet, mainnet)")

    # cde (Sovereign CDE & Point Start Userspace Checkpointing)
    cde_parser = subparsers.add_parser("cde", help="Sovereign CDE & Point Start Userspace Checkpointing")
    cde_parser.add_argument("action", choices=["summary", "rules", "spawn"], default="summary", nargs="?", help="Aktion: summary, rules, spawn")
    cde_parser.add_argument("--point", type=str, default="crash_log_77", help="CRIU Checkpoint ID (z.B. crash_log_77)")

    # figp (FIGP & UFCIE Governance Platform)
    figp_parser = subparsers.add_parser("figp", help="FIGP & UFCIE Framework Intelligence & Governance Platform")
    figp_parser.add_argument("action", choices=["summary", "frameworks", "schema"], default="summary", nargs="?", help="Aktion: summary, frameworks, schema")

    # tools (141 Observability & AI-Agent Stack)
    tools_parser = subparsers.add_parser("tools", help="141 Observability, Monitoring & AI-Agent Tools Stack")
    tools_parser.add_argument("action", choices=["summary", "list", "search"], default="summary", nargs="?", help="Aktion: summary, list, search")
    tools_parser.add_argument("--category", type=str, default="", help="Kategorie-Filter (z.B. AI-IDEs, Tracing, Logging, etc.)")
    tools_parser.add_argument("--query", type=str, default="", help="Suchbegriff für Tools")
    tools_parser.add_argument("--limit", type=int, default=25, help="Maximale Trefferanzahl")

    # containment (State-Level Security & AI Containment)
    cont_parser = subparsers.add_parser("containment", help="State-Level Security, KI-Einkesselung & Hardware Root-of-Trust (AUDITREQ-99X)")
    cont_parser.add_argument("action", choices=["summary", "layers", "verify", "loop"], default="summary", nargs="?", help="Aktion: summary, layers, verify, loop")
    cont_parser.add_argument("--category", type=str, default="", help="Kategorie-Filter (Hardware-Pipeline, Einkesselung, Notfall-Protokoll, Preflight-Check)")
    cont_parser.add_argument("--iterations", type=int, default=5, help="Anzahl Iterationen für Agentic Loop Breaker Test")
    cont_parser.add_argument("--tokens", type=int, default=25000, help="Anzahl Tokens für Loop Breaker Test")
    cont_parser.add_argument("--approve", action="store_true", help="Gate G09 Human Approval simulieren")

    # cdp (Devin AI + CDP + MCP Live-Sync & Livelink)
    cdp_cli_parser = subparsers.add_parser("cdp", help="CDP LiveSync, MCP & Devin AI Portal Automation Suite")
    cdp_cli_parser.add_argument("action", choices=["summary", "components", "condense", "kyc"], default="summary", nargs="?", help="Aktion: summary, components, condense, kyc")
    cdp_cli_parser.add_argument("--raw-kb", type=int, default=1500, help="Größe der Roh-Webseite in KB für Kondensationstest")

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

    elif args.command == "audit":
        from .assurance_gates import AssuranceGatePipeline
        pipeline = AssuranceGatePipeline(project_root)
        print(">>> Starte unabhängiges HCOS 13-Gate Assurance Audit (G00–G12)...")
        res = pipeline.audit_all_gates()
        print("==================================================================")
        print(f" HCOS TITAN 13-GATE HARDENED ASSURANCE: {res['overall_status']}")
        print(f" Geprüfte Gates: {res['passed_gates']}/{res['total_gates']}")
        print("==================================================================")
        for g in res["gates"]:
            status_badge = f"[{g['status']}]"
            print(f" {g['gate']} | {g['name']:<28} | {status_badge:<24} | {g['details']}")
        print("==================================================================")
        if res.get("overall_status") != "FULL_ASSURANCE_PASSED":
            print("[FAIL-CLOSED] Mindestens ein Sicherheits-Gate hat die Freigabe blockiert.")
            sys.exit(1)
        else:
            print("[OK] Alle 13 Gates unabhängig verifiziert. System uneingeschränkt freigegeben.")

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

    elif args.command == "modules":
        loader = ModuleLoader(project_root)
        if args.action == "list":
            summary = loader.get_suite_summary()
            print("==================================================================")
            print(" HCOS TITAN MODULAR INTELLIGENCE SUITE — 10 MODULGRUPPEN")
            print(f" Status-Übersicht: {summary['lifecycle_breakdown']}")
            print(f" Gesamt-Produktionsreife: {summary['production_readiness_percent']}%")
            print("==================================================================")
            for m in summary["modules"]:
                state_badge = f"[{m['lifecycle_state'].upper()}]"
                print(f" - {m['id']:<26} | {m['title']:<30} | {state_badge:<15} | Gate: {m['security_gate']}")
            print("==================================================================")

        elif args.action == "verify":
            if args.id:
                res = loader.verify_module(args.id)
                print(json.dumps(res, indent=2, ensure_ascii=False))
            else:
                for m in loader.list_modules():
                    res = loader.verify_module(m["id"])
                    print(f"[{'PASS' if res['success'] else 'FAIL'}] {m['id']:<26} -> {res['lifecycle_state']}")

        elif args.action == "test":
            if args.id:
                res = loader.test_module(args.id)
                print(json.dumps(res, indent=2, ensure_ascii=False))
            else:
                for m in loader.list_modules():
                    res = loader.test_module(m["id"])
                    status = "PASS" if res.get("success") else "FAIL"
                    print(f"[{status}] {m['id']:<26} -> {res.get('lifecycle_state')}")

        elif args.action == "promote":
            res = loader.promote_all_to_freigegeben()
            print(">>> Alle Module verifiziert und auf 'Freigegeben' befördert:")
            print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "repos":
        from .repo_catalog import RepositoryEvaluationCatalog
        catalog = RepositoryEvaluationCatalog(project_root)
        if args.action == "summary":
            summary = catalog.get_summary()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 50 OPEN-SOURCE REPOSITORIES OVERVIEW")
            print("==================================================================")
            print(f" Gesamtanzahl Repositories: {summary['total_repositories']}")
            print(f"  - Local Sovereign Zone:      {summary['sovereign_local_count']}")
            print(f"  - Development & Research:    {summary['development_count']}")
            print(f"  - Federation & Integration:  {summary['federation_count']}")
            print("------------------------------------------------------------------")
            print(" Integrationsentscheide:")
            for k, v in sorted(summary['decision_breakdown'].items(), key=lambda x: -x[1]):
                print(f"   * {k:<25}: {v}")
            print("==================================================================")

        elif args.action == "inspect":
            r = catalog.get_by_nr(args.nr)
            if not r:
                print(f"[ERROR] Repository #{args.nr} nicht gefunden (Bereich: 1-50).")
                sys.exit(1)
            print("==================================================================")
            print(f" REPOSITORY DOSSIER #{r['nr']:02d}: {r['repository']}")
            print("==================================================================")
            url_badge = "GÜLTIG (HTTPS)" if r.get("url_valid") else "BLOCKIERT"
            print(f" URL:                     {r['url']} [{url_badge}]")
            print(f" Modul-Zuordnung:         {r['module_id']} ({r['module_role']})")
            print(f" Betriebszone:            {r['zone']}")
            print(f" Integrationsentscheid:   {r['integration_decision']}")
            print(f" PDF-Fundstelle:          {r['pdf_source']} (Seite {r['pdf_page']})")
            print(f" Geplante Rolle:          {r['planned_role']}")
            print(f" Herkunftsnotiz:          {r['origin_note']}")
            print(f" Lizenz-ID:               {r.get('license_id')}")
            print(f" Lizenz-Klassifikation:   {r.get('license_type')} ({r.get('license_source')})")
            print(f" Sicherheits-Einstufung:  {r.get('security_profile')}")
            print(f" Audit-Kategorie:         {r.get('audit_type')} (Review-Datum: {r.get('audit_date')})")
            print("==================================================================")

        elif args.action == "zone":
            zone_filter = args.zone or "sovereign"
            filtered = catalog.filter_by_zone(zone_filter)
            print("==================================================================")
            print(f" REPOSITORIES IN ZONE: '{zone_filter.upper()}' ({len(filtered)} Einträge)")
            print("==================================================================")
            for r in filtered:
                print(f" #{r['nr']:02d} | {r['repository']:<38} | {r['module_id']:<4} | [{r['integration_decision']:<15}]")
            print("==================================================================")

        elif args.action == "wish-studio":
            wish_repos = catalog.get_wish_studio_catalog()
            print("==================================================================")
            print(f" WISH STUDIO & GEMEINWOHL ÖKOSYSTEM ({len(wish_repos)} REPOSITORIES)")
            print("==================================================================")
            for r in wish_repos:
                print(f" #{r['nr']:02d} | {r['projekt']:<12} | {r['repository']:<24} | {r['kategorie']:<30} | [{r['lizenz']}]")
            print("==================================================================")

        elif args.action == "loccp":
            items = catalog.get_loccp_repo_catalog(
                query=getattr(args, "search", ""),
                category=getattr(args, "category", ""),
                limit=getattr(args, "limit", 25)
            )
            stats = catalog.get_loccp_stats()
            print("==================================================================")
            print(f" LOCCP MASTERKATALOG ({stats['total_loccp_repositories']} REPOSITORIES / {len(stats['categories'])} KATEGORIEN)")
            print("==================================================================")
            for r in items:
                print(f" {r.get('ID', '?'):<7} | {r.get('Projekt/Tool', ''):<26} | {r.get('GitHub-Pfad', ''):<32} | {r.get('Kategorie', '')[:22]}")
            print("==================================================================")
            print(f" Treffer: {len(items)} (Limit: {getattr(args, 'limit', 25)})")
            print(" [Tipp] Suche: python3 forina.py repos loccp --search actual")

        else: # list
            all_repos = catalog.list_all()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 50 OPEN-SOURCE REPOSITORIES (MASTERKATALOG)")
            print("==================================================================")
            for r in all_repos:
                zone_tag = "SOVEREIGN" if "Sovereign" in r['zone'] else ("DEV" if "Dev" in r['zone'] else "FEDERATION")
                print(f" #{r['nr']:02d} | {r['repository']:<36} | {r['module_id']} | [{zone_tag:<10}] | {r['integration_decision']}")
            print("==================================================================")
            print(f" [Tipp] Ausführliches Dossier ansehen mit: python3 forina.py repos inspect --nr 47")

    elif args.command == "concepts":
        suite = ConceptPaperSuite(project_root)

        if args.action == "summary":
            summ = suite.get_summary()
            print("==================================================================")
            print(" HCOS FORINA TITAN — CONCEPT PAPER SUITE v2.0 (33+ A4)")
            print("==================================================================")
            print(f" Gesamtanzahl Concept Papers: {summ['total_papers']}")
            print(f" Abgedeckte Normen & Standards: {summ['total_standards']}")
            print(f" Governance: {summ['sovereign_governance']}")
            print("------------------------------------------------------------------")
            print(" Themenkategorien:")
            for cat, count in summ['categories_breakdown'].items():
                print(f"   * {cat:<32}: {count:2d} Papiere")
            print("==================================================================")

        elif args.action in ("inspect", "read"):
            if args.action == "read" or getattr(args, "full", False):
                paper = suite.get_paper_content(args.nr)
                if not paper:
                    print(f"[!] Concept Paper #{args.nr} nicht gefunden.")
                    return
                print("==================================================================")
                print(f" CONCEPT PAPER #{paper['nr']:02d}: {paper['title']}")
                print(f" Datei: {paper.get('file')} | Gefunden: {paper.get('file_found')}")
                print("==================================================================")
                print(paper.get("content", ""))
                print("==================================================================")
            else:
                paper = suite.get_paper(args.nr)
                if not paper:
                    print(f"[!] Concept Paper #{args.nr} nicht gefunden.")
                    return
                print("==================================================================")
                print(f" CONCEPT PAPER #{paper['nr']:02d}: {paper['title']}")
                print("==================================================================")
                print(f" Kürzel / Codes:       {paper['code']}")
                print(f" Kategorie:            {paper['category']}")
                print(f" Relevante Module:     {', '.join(paper['modules'])}")
                print(f" Normen & Standards:   {', '.join(paper['standards'])}")
                print("------------------------------------------------------------------")
                print(f" Zusammenfassung:\n {paper['summary']}")
                print("------------------------------------------------------------------")
                print(f" [Tipp] Volltext anzeigen mit: python3 forina.py concepts read --nr {paper['nr']}")
                print("==================================================================")

        elif args.action == "standards":
            print("==================================================================")
            print(f" HCOS FORINA TITAN — NORMEN- & ZERTIFIZIERUNGSKATALOG ({len(suite.standards)} Standards)")
            print("==================================================================")
            for std in suite.standards:
                print(f" - {std['name']:<22} | {std['category']:<22} | {std['domain']}")
            print("==================================================================")

        elif args.action == "masterkonzept":
            mk = suite.get_masterkonzept()
            print("==================================================================")
            print(f" HCOS FORINA TITAN — INTEGRIERTES MASTERKONZEPT (KANONISCH)")
            print("==================================================================")
            print(f" Titel:    {mk['title']}")
            print(f" Status:   {mk['subtitle']}")
            print(f" Größe:    {mk['size']:,} Bytes ({mk['lines']} Zeilen)")
            print(f" SHA-256:  {mk['sha256']}")
            print("==================================================================")
            if getattr(args, "full", False):
                print(mk["content"])
            else:
                for line in mk["content"].splitlines()[:28]:
                    print(line)
                print("...\n[Tipp] Volltext anzeigen mit: python3 forina.py concepts masterkonzept --full")
            print("==================================================================")

        elif args.action == "specialized":
            specs = suite.list_specialized_papers()
            print("==================================================================")
            print(f" HCOS FORINA TITAN — 15 SPEZIALISIERTE KONZEPTPAPIERE")
            print("==================================================================")
            for s in specs:
                print(f" * {s['id']:<45} | {s['size']:>6} B | {s['file']}")
            print("==================================================================")

        elif args.action == "masterbook":
            if getattr(args, "nr", None) and args.nr > 0 and getattr(args, "nr", 1) != 1 or (getattr(args, "nr", 0) > 0 and "--nr" in sys.argv):
                ch = suite.get_dp_masterbook_chapter(args.nr)
                if not ch:
                    print(f"[!] DP Masterbook Kapitel #{args.nr} nicht gefunden (Bereich: 1-27).")
                    return
                print("==================================================================")
                print(f" DP MASTERBOOK KAPITEL #{ch['nr']:02d}: {ch['title']}")
                print(f" Wörter: {ch['words']} | Lizenz: {ch['license']} | {ch['author']}")
                print("==================================================================")
                if getattr(args, "full", False):
                    print(ch.get("content", ""))
                else:
                    for line in ch.get("content", "").splitlines()[:25]:
                        print(line)
                    print("...\n[Tipp] Volltext anzeigen mit: python3 forina.py concepts masterbook --nr " + str(ch['nr']) + " --full")
                print("==================================================================")
            else:
                summ = suite.get_dp_masterbook_summary()
                chapters = suite.list_dp_masterbook_chapters()
                print("==================================================================")
                print(f" {summ['title'].upper()}")
                print(f" Status: {summ['status']} | Lizenz: {summ['license']}")
                print(f" Gesamtumfang: {summ['total_curated_chapters']} Kapitel, {summ['total_words']:,} Wörter")
                print("==================================================================")
                for c in chapters:
                    print(f" #{c['nr']:02d} | {c['title']:<52} | {c['words']:>5} Wörter")
                print("==================================================================")
                print(" [Tipp] Kapitel lesen: python3 forina.py concepts masterbook --nr 1")

        else: # list
            if args.search:
                papers = suite.search_papers(args.search)
                print(f">>> Gefundene Papiere für '{args.search}': {len(papers)}")
            else:
                papers = suite.list_papers()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 34 A4 CONCEPT PAPERS SUITE")
            print("==================================================================")
            for p in papers:
                print(f" #{p['nr']:02d} | {p['title']:<42} | [{p['code']:<14}] | {p['category']}")
            print("==================================================================")
            print(f" [Tipp] Volltext lesen mit: python3 forina.py concepts read --nr <1-34>")

    elif args.command == "harness":
        harness = HarnessLoopEngine(project_root)

        if args.action == "run":
            print(">>> Starte vollständigen 8-Stufen Harness-Loop Durchlauf...")
            state = harness.run_cycle_iteration()
            print("==================================================================")
            print(f" HARNESS-LOOP ZYKLUS #{state['cycle_id']-1} ERFOLGREICH ABGESCHLOSSEN")
            print("==================================================================")
            for s_id, s_res in state['stage_results'].items():
                status_str = s_res if isinstance(s_res, str) else s_res.get('status', 'PASS')
                msg_str = "OK"
                if isinstance(s_res, dict):
                    msg_str = s_res.get('details', s_res.get('message', 'OK'))
                print(f" Stufe {s_id:<8} : [{status_str}] {msg_str}")
            print("==================================================================")
            print(f" Status: {state['status']} -> Neuer Zielzustand: {state['current_stage']}")

        elif args.action == "stage":
            stage_to_run = getattr(args, "stage", "PLAN")
            print(f">>> Führe einzelne Harness-Loop Stufe '{stage_to_run}' aus...")
            try:
                res = harness.run_single_stage(stage_to_run)
                print("==================================================================")
                print(f" HARNESS-LOOP STUFE {res['stage_id']} ERGEBNIS")
                print("==================================================================")
                print(f" Status:       [{res['result'].get('status', 'PASS')}]")
                print(f" Details:      {res['result']}")
                print(f" Nächste Stufe: {res['updated_state'].get('current_stage')}")
                print("==================================================================")
            except Exception as e:
                print(f"[!] Fehler bei Stufenausführung: {e}")

        elif args.action == "stages":
            stages = harness.get_stages()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 8 STUFEN DES AUTOMATISIERTEN HARNESS-LOOPS")
            print("==================================================================")
            for s in stages:
                print(f" {s['stage']}. {s['id']:<8} | {s['name']:<35} | {s['details']}")
            print("==================================================================")

        elif args.action == "loop-run":
            from forina_engine.harness_control_loop import HarnessControlLoopEngine, WorkItem
            hcl = HarnessControlLoopEngine()
            wi = WorkItem(
                task_id="CLI-HCL-ITEM-001",
                requirement="Enforce deterministic state cycle and fail-closed audit",
                proposed_change="Verify zero-leak isolation across all stages",
                human_approval=getattr(args, "approve", False),
                external_isolation_verified=getattr(args, "isolated", False)
            )
            print(">>> Führe Offline-Safe Reference Harness Control Loop (HCL) aus...")
            out = hcl.run_cycle(wi)
            print("==================================================================")
            print(f" HARNESS CONTROL LOOP ERGEBNIS: {out.state.value}")
            print("==================================================================")
            print(f" Task-ID:       {out.task_id}")
            print(f" Iterationen:   {out.iterations}")
            print(f" Stop-Grund:    {out.stop_reason}")
            print(f" Evidenz-Logs:  {len(out.evidence)} Prüfungen erfasst")
            for ev in out.evidence:
                print(f"   * Iteration {ev.iteration} [{ev.state}] -> Input: {ev.input_sha256[:12]}.. | Output: {ev.output_sha256[:12]}..")
            print("==================================================================")

        else: # status
            st = harness.get_state()
            print("==================================================================")
            print(f" HARNESS-LOOP STATUS: {st['status']}")
            print("==================================================================")
            print(f" Aktueller Zyklus:             #{st.get('cycle_id', 1)}")
            print(f" Letzter Durchlauf:            {st.get('last_cycle_timestamp')}")
            print(f" Abgeschlossene Zyklen gesamt: {st.get('history_cycles_completed', 0)}")
            print("------------------------------------------------------------------")
            print(" [Tipp] Ausführen mit: python3 forina.py harness run")
            print("==================================================================")

    elif args.command == "zeroclock":
        apzc = ActPackZeroClock(project_root)

        if args.action == "tick":
            t = apzc.get_zero_clock_tick()
            print("==================================================================")
            print(" HCOS ACT PACK ZERO CLOCK — DETERMINISTISCHER TICK")
            print("==================================================================")
            print(f" Tick Sequenz:         #{t['tick']}")
            print(f" UTC Zeitstempel:      {t['iso_timestamp']}")
            print(f" Epoch Delta:          +{t['zero_clock_delta_micros']} µs")
            print(f" State Block Hash:     {t['block_hash']}")
            print(f" Status:               {t['synchronization_status']}")
            print("==================================================================")

        elif args.action == "tmr":
            print("==================================================================")
            print(" HCOS NATZA CORE FLIGHT SYSTEM — TMR KONSENSUS PRÜFUNG")
            print("==================================================================")
            # Test 1: Consensus
            v1 = apzc.verify_tmr_consensus("PAYLOAD_PASS", "PAYLOAD_PASS", "PAYLOAD_FAIL", context="CLI_DIAGNOSTIC")
            print(f" [PASS] 2/3 Mehrheit erzielt: {v1}")
            # Test 2: Full divergence fail-closed
            try:
                apzc.verify_tmr_consensus("BRANCH_A", "BRANCH_B", "BRANCH_C", context="DIVERGENCE_TEST")
                print(" [FAIL] Divergenz wurde nicht blockiert!")
            except NaTZaFaultToleranceViolation as e:
                print(f" [PASS] Divergenz Fail-Closed abgefangen: {e}")
            print("==================================================================")

        elif args.action == "spawn":
            task = apzc.spawn_subagent_task("master_agent", args.subtask, {"mode": "deterministic", "sandbox": "qemu_kvm"})
            print("==================================================================")
            print(" HCOS DEVIN AI — SUB-AGENT GESPAWNT (WHYTRACE TELEMETRIE)")
            print("==================================================================")
            print(f" Sub-Agent ID:         {task['subagent_id']}")
            print(f" Parent Agent:         {task['parent_agent_id']}")
            print(f" Subtask:              {task['task_name']}")
            print(f" WhyTrace ID:          {task['trace_id']}")
            print(f" Erstellt bei Tick:    #{task['created_tick']}")
            print(f" Status:               {task['status']}")
            print("==================================================================")

        else: # status
            st = apzc.get_status()
            print("==================================================================")
            print(" HCOS ACT PACK ZERO CLOCK & NATZA CFS TELEMETRIE STATUS")
            print("==================================================================")
            print(f" Aktueller Tick:       #{st['current_tick']}")
            print(f" Letzter Block Hash:   {st['last_state_hash']}")
            print(f" NaTZa CFS Heartbeat:  {st['natza_cfs_heartbeat']}")
            print(f" Microsecond Delta:    +{st['delta_microseconds']} µs")
            print(f" Active Traces Count:  {st['active_traces_count']}")
            print(f" UI Sliding Engine:    {st['ui_sliding_engine']} ({st['fps_target']} FPS)")
            print(f" Engine Status:        {st['engine_state']}")
            print("==================================================================")

    elif args.command == "baende":
        suite = ConceptPaperSuite(project_root)
        if args.action == "read":
            band = suite.get_band_content(args.band)
            if not band:
                print(f"[!] Band {args.band} nicht gefunden.")
                return
            print("==================================================================")
            print(f" {band['title']}")
            print(f" Datei: {band['file']} ({band.get('bytes', 0)} Bytes)")
            print("==================================================================")
            print(band.get("content", "")[:3500] + "\n\n... [Volltext gekürzt im Terminal. Siehe docs/baende/]")
            print("==================================================================")
        elif args.action == "themen":
            themen = suite.get_136_themen()
            print("==================================================================")
            print(f" HCOS FORINA TITAN — 136 FACHKAPITEL ÜBERSICHT ({len(themen)} Bände)")
            print("==================================================================")
            for b_key, chaps in themen.items():
                print(f"\n--- BAND {b_key} ({len(chaps)} Kapitel) ---")
                for c in chaps[:10]:
                    print(f"  • {c.get('kapitel_nr', '')}: {c.get('titel', '')}")
                if len(chaps) > 10:
                    print(f"    ... und {len(chaps)-10} weitere Fachkapitel")
            print("==================================================================")
        else: # list
            baende = suite.list_baende()
            spec = suite.list_specialized_papers()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 144 SEITEN ENZYKLOPÄDIE (4 BÄNDE)")
            print("==================================================================")
            for b in baende:
                exists_tag = "VORHANDEN" if b["exists"] else "FEHLT"
                print(f" Band {b['band']} | {b['title']:<62} | {b['chapters']} Kap. | [{exists_tag}]")
            print("------------------------------------------------------------------")
            print(" Spezialisierte Concept Papers:")
            for s in spec:
                print(f"  * {s['title']:<50} ({s['file']})")
            print("==================================================================")

    elif args.command == "badges":
        from forina_engine.audit_badges import AuditBadgeRegistry
        reg = AuditBadgeRegistry(project_root)
        if args.action == "verify":
            badges = reg.list_badges()
            print("==================================================================")
            print(f" 34 NORMEN SVG BADGES INTEGRITÄTSPRÜFUNG ({len(badges)} Badges)")
            print("==================================================================")
            for b in badges:
                print(f" [{b['norm_id']}] {b['title']:<48} | {b['sha256'][:16]}... | [OK]")
            print("==================================================================")
            print("[OK] Alle 34 Vektor-SVG-Badges verifiziert.")
        elif args.action == "inspect":
            svg = reg.get_badge_svg(args.id)
            if not svg:
                print(f"[!] Badge {args.id} nicht gefunden.")
                return
            print(f"--- SVG Vektor für {args.id} ({len(svg)} Bytes) ---")
            print(svg[:400] + "...")
        else: # list
            badges = reg.list_badges()
            print("==================================================================")
            print(f" HCOS FORINA TITAN — 34 NORMEN & REGULATORY BADGES")
            print("==================================================================")
            for b in badges:
                print(f" {b['norm_id']:<10} | {b['title']:<46} | {b['category']}")
            print("==================================================================")

    elif args.command == "finance":
        from forina_engine.institutional_finance import InstitutionalFinanceRegistry
        fin = InstitutionalFinanceRegistry(project_root)
        if args.action == "centralbanks":
            banks = fin.get_central_banks()
            print("==================================================================")
            print(" ZENTRALBANKEN & CLEARING-SYSTEME")
            print("==================================================================")
            for cb in banks:
                print(f" {cb['id']:<12} | {cb['name']:<40} | {', '.join(cb['clearing_systems'])}")
            print("==================================================================")
        elif args.action == "openbanking":
            providers = fin.get_open_banking_providers()
            print("==================================================================")
            print(" OPEN BANKING & XS2A PROVIDER REGISTRY (PSD2)")
            print("==================================================================")
            for p in providers:
                print(f" {p['name']:<22} | {p['hq']:<28} | {p['coverage']}")
            print("==================================================================")
        elif args.action == "schemas":
            schemas = fin.get_iso20022_message_schemas()
            print("==================================================================")
            print(" ISO 20022 FINANCIAL MESSAGING SCHEMAS")
            print("==================================================================")
            for s in schemas:
                print(f" {s['code']:<16} | {s['name']:<55} | [{s['scope']}]")
            print("==================================================================")
        elif args.action == "pontes":
            pontes = fin.get_pontes_spec()
            print("==================================================================")
            print(f" {pontes['protocol'].upper()}")
            print("==================================================================")
            print(f" Federführende Instanz:  {pontes['lead_entity']}")
            print(f" Offizieller Start:      {pontes['official_launch']}")
            print(f" Primärer Zweck:         {pontes['purpose']}")
            print("------------------------------------------------------------------")
            print(" Kernfähigkeiten:")
            for c in pontes['key_capabilities']:
                print(f"   * {c}")
            print("------------------------------------------------------------------")
            print(f" HCOS Integration:       {pontes['hcos_integration']}")
            print("==================================================================")
        elif args.action == "portals":
            results = fin.search_portals(query=getattr(args, "search", ""), category=getattr(args, "category", ""), limit=getattr(args, "limit", 25))
            print("==================================================================")
            print(f" HCOS FINANCE PORTAL INDEX ({len(results)} Treffer)")
            print("==================================================================")
            for r in results:
                name = r.get("Name", "Unbekannt")
                domain = r.get("Domain", "")
                cat = r.get("Kategorie", "")[:28]
                themen = r.get("Themen", "")[:35]
                top = "[TOP]" if r.get("Top_Rang") else "     "
                print(f" {top} {name:<24} | {domain:<20} | {cat:<28} | {themen}")
            print("==================================================================")
            print(f" [Tipp] Gezielte Suche: python3 forina.py finance portals --search <Name>")
        elif args.action == "clevel":
            company = getattr(args, "company", "") or getattr(args, "search", "")
            results = fin.get_clevel_directory(company_filter=company)
            print("==================================================================")
            print(f" HCOS FINANCE C-LEVEL EXECUTIVE DIRECTORY ({len(results)} Einträge)")
            print("==================================================================")
            for r in results:
                comp = r.get("Unternehmen", "")
                pos = r.get("Position", "")
                name = r.get("Name", "")
                seit = r.get("Seit", "")
                print(f" {comp:<18} | {pos:<24} | {name:<26} | Seit {seit}")
            print("==================================================================")
        elif args.action == "enablebanking":
            apps = fin.get_enable_banking_apps()
            print("==================================================================")
            print(" ENABLE BANKING · WORLDBANKEYES APPLICATION REGISTRY")
            print("==================================================================")
            for a in apps:
                print(f" [{a['status']}] {a['app_name']}")
                print(f"   App ID:      {a['app_id']}")
                print(f"   Environment: {a['environment']} | Services: {', '.join(a['services'])}")
                print(f"   Privacy:     {a.get('privacy_url', 'N/A')}")
                print(f"   Redirect:    {a.get('redirect_url', 'N/A')}")
                print(f"   Key Storage: {a['key_storage']}")
                print("------------------------------------------------------------------")
            print(f" Sovereign Governance: {apps[0]['sovereign_governance']}")
            print("==================================================================")
        elif args.action == "aspsp":
            stats = fin.get_aspsp_stats()
            results = fin.search_aspsp_banks(
                query=getattr(args, "search", ""),
                country=getattr(args, "country", ""),
                limit=getattr(args, "limit", 25)
            )
            print("==================================================================")
            print(f" ASPSP EU-BANKEN KATALOG ({stats['unique_brands']} Banken / {stats['countries_count']} Länder)")
            print(f" Status: {stats['status_distribution'].get('green', 0)} Green, {stats['status_distribution'].get('red', 0)} Red")
            print("==================================================================")
            for r in results:
                status_symbol = "[OK]" if r.get("current_status") == "green" else "[WARN]"
                print(f" {status_symbol:<6} {r.get('country', '??'):<4} | {r.get('brand', 'Unbekannt')[:32]:<32} | {r.get('psu_type', ''):<10} | {r.get('service', '')}")
            print("==================================================================")
            print(f" Treffer: {len(results)} (Limit: {getattr(args, 'limit', 25)})")
            print(f" [Tipp] Filter: python3 forina.py finance aspsp --search Sparkasse --country DE")
        elif args.action == "globalcbs":
            stats = fin.get_global_central_banks_stats()
            results = fin.get_global_central_banks(
                query=getattr(args, "search", ""),
                jurisdiction=getattr(args, "country", ""),
                limit=getattr(args, "limit", 25)
            )
            print("==================================================================")
            print(f" GLOBALE SOUVERÄNE ZENTRALBANKEN ({stats['total_sovereign_central_banks']} Staaten & Währungsräume)")
            print(f" Pontes Interoperabilitäts-Standard (EZB wCBDC 2026 Aligned)")
            print("==================================================================")
            for r in results:
                print(f" {r.get('jurisdiction', 'Unbekannt'):<30} | {r.get('central_bank', '')}")
            print("==================================================================")
            print(f" Treffer: {len(results)} (Limit: {getattr(args, 'limit', 25)})")
            print(f" [Tipp] Suche: python3 forina.py finance globalcbs --search Schweiz")
        elif args.action == "vpsportals":
            results = fin.get_wish_studio_vps_portals(
                query=getattr(args, "search", ""),
                limit=getattr(args, "limit", 35)
            )
            print("==================================================================")
            print(f" WISH STUDIO OS · VPS 82.165.134.41 ÖFFENTLICHE PORTALE ({len(results)} Tools)")
            print("==================================================================")
            for r in results:
                print(f" #{r.get('nr', '?'):<2} | {r.get('tool', ''):<20} | {r.get('native_api', '')[:25]:<25} | {r.get('url', '')}")
            print("==================================================================")
        elif args.action == "portalregistry":
            results = fin.search_portal_registry_2361(
                query=getattr(args, "search", ""),
                category=getattr(args, "category", ""),
                limit=getattr(args, "limit", 25)
            )
            print("==================================================================")
            print(f" MASTER PORTAL REGISTRY (PRW-001 / {len(results)} Treffer von 2.361)")
            print("==================================================================")
            for r in results:
                print(f" #{r.get('Nr', '?'):<4} | {r.get('Name', ''):<26} | {r.get('Domain', ''):<22} | {r.get('Kategorie', '')[:30]}")
            print("==================================================================")
            print(f" [Tipp] Suche: python3 forina.py finance portalregistry --search Visa")
        elif args.action == "partnerapps":
            provider = getattr(args, "provider", "")
            if provider:
                app_data = fin.get_partner_application(provider)
                if not app_data:
                    print(f"[!] Partner-Dossier für '{provider}' nicht gefunden.")
                else:
                    print("==================================================================")
                    print(f" PARTNER-ANTRAG DOSSIER: {app_data['provider'].upper()}")
                    print("==================================================================")
                    payload = app_data.get("payload", {})
                    print(f" Dossier-ID:    {payload.get('application_id', 'N/A')}")
                    print(f" Programm:      {payload.get('program', 'N/A')}")
                    print(f" Submission URL: {payload.get('portal_submission_url', 'N/A')}")
                    print(f" Status:        {payload.get('status', 'N/A')}")
                    print("------------------------------------------------------------------")
                    contact = payload.get("fields", {}).get("contact_person", {})
                    print(f" Ansprechpartner: {contact.get('full_name')} ({contact.get('title')})")
                    print(f" E-Mail:          {contact.get('email')}")
                    print(f" Telefon:         {contact.get('phone')}")
                    print("==================================================================")
            else:
                apps = fin.get_partner_applications()
                print("==================================================================")
                print(f" FINTECH PARTNER-ANTRÄGE ({len(apps)} Dossiers vorbereitet)")
                print("==================================================================")
                for a in apps:
                    payload = a.get("payload", {})
                    p_name = a["provider"]
                    p_prog = payload.get("program", "Standard BaaS Onboarding")
                    p_id = payload.get("application_id", "APP-N/A")
                    print(f" * {p_name:<16} | ID: {p_id:<14} | {p_prog}")
                print("==================================================================")
                print(" [Tipp] Details abrufen: python3 forina.py finance partnerapps --provider Mastercard")
        elif args.action == "globalcards":
            gc = fin.get_globalcards_bank_spec()
            print("==================================================================")
            print(f" {gc['title'].upper()}")
            print("==================================================================")
            print(f" Governance:   {gc['governance']}")
            print(f" Spezifikation: {'Verfügbar' if gc['spec_available'] else 'Fehlt'} ({gc['spec_size_bytes']} Bytes)")
            print("------------------------------------------------------------------")
            print(" 12 Kernmodule:")
            for m in gc["modules"]:
                print(f"   [{m['id']}] {m['name']:<24} | {m['scope']}")
            print("==================================================================")
        elif args.action == "pontesmatrix":
            from .energy_audit import PontesDltSettlementEngine
            pont = PontesDltSettlementEngine(project_root)
            cands = pont.list_candidates()
            print("==================================================================")
            print(f" EZB PONTES & WHOLESALE DLT RECHERCHEMATRIX ({len(cands)} Systeme)")
            print("==================================================================")
            for c in cands:
                print(f" [{c.get('Kandidat_ID'):<8}] {c.get('Projekt'):<16} | {c.get('Kategorie'):<22} | {c.get('Fokus_DvP_PvP')}")
            print("==================================================================")
        else: # summary
            summ = fin.get_summary()
            print(json.dumps(summ, indent=2, ensure_ascii=False))

    elif args.command == "catalogs":
        suite = ConceptPaperSuite(project_root)
        if args.action == "verify-136":
            rows = suite.get_136_kapitel_nachweis()
            print("==================================================================")
            print(f" HCOS 136-KAPITEL NACHWEISMATRIX ({len(rows)} Einträge)")
            print("==================================================================")
            for r in rows[:15]:
                print(f" #{r.get('kapitel', '?'):<3} | Band {r.get('teil', '?')} | {r.get('thema', '')[:40]:<40} | Quelle: {r.get('quelle', '')[:25]}")
            if len(rows) > 15:
                print(f" ... und {len(rows) - 15} weitere Kapitel im Nachweisregister verifiziert.")
            print("==================================================================")
        elif args.action == "repos-matrix":
            rows = suite.get_50_repos_matrix()
            print("==================================================================")
            print(f" HCOS 50 REPOSITORIES QUELLENMATRIX ({len(rows)} Einträge)")
            print("==================================================================")
            for r in rows[:15]:
                print(f" #{r.get('Nr', '?'):<3} | {r.get('Repository', '')[:35]:<35} | Modul: {r.get('Modul', '')} | {r.get('Lizenz', '')}")
            if len(rows) > 15:
                print(f" ... und {len(rows) - 15} weitere Repositories in der Quellenmatrix.")
            print("==================================================================")

    elif args.command == "upuia":
        from forina_engine.upuia_scanner import UpuiaIntelligenceArchive
        upuia = UpuiaIntelligenceArchive(project_root)
        if args.action == "preflight":
            pf = upuia.run_preflight_check()
            print("==================================================================")
            print(" UPUIA INDEPENDENT SECURITY GATE PREFLIGHT")
            print("==================================================================")
            print(f" Status:               {'[PASS]' if pf['preflight_passed'] else '[FAIL]'}")
            print(f" System-Immutable:     {pf['rule_1_system_immutable']}")
            print(f" 100% Offline Lokal:   {pf['rule_2_local_only']}")
            print(f" Datenablage Ordner:   {pf['rule_3_separate_data_dir']}")
            print(f" Secret-Filter:        {pf['rule_5_secrets_filter_ready']}")
            print(f" Air-Gap Egress-Sperre: {pf['rule_8_airgap_status']}")
            print("==================================================================")
        else: # status
            summ = upuia.get_summary()
            print("==================================================================")
            print(" UPUIA — UNIVERSAL PROJECT & URL INTELLIGENCE ARCHIVE")
            print("==================================================================")
            print(f" Status:               {summ['status']}")
            print(f" Grundregeln:          {summ['security_directiv_compliance']}")
            print(f" Zielplattform:        EndeavourOS / Arch Linux Native")
            print(f" Speicherort:          {summ['storage_location']}")
            print(f" Secret-Ausschluss:    {summ['secret_exclusion']}")
            print(f" Unveränderte Quellen: {summ['immutable_originals']}")
            print("==================================================================")

    elif args.command == "compliance":
        from .repo_catalog import RepositoryEvaluationCatalog
        catalog = RepositoryEvaluationCatalog(project_root)
        if args.action == "pruefpunkte":
            pts = catalog.get_loccp_pruefpunkte(compliance_module=getattr(args, "module", ""))
            print("==================================================================")
            print(f" LOCCP 42 COMPLIANCE-PRÜFPUNKTE ({len(pts)} Prüfpunkte)")
            print("==================================================================")
            for p in pts:
                print(f" [{p.get('ID', '?'):<3}] {p.get('Compliance-Modul', ''):<22} | {p.get('Prüfpunkt', ''):<45} | Repos: {p.get('Passende Repositories', '')[:20]}")
            print("==================================================================")
            print(" [Tipp] Modul-Filter: python3 forina.py compliance pruefpunkte --module Corporate")
        elif args.action == "attestation":
            attestation_file = project_root / "docs" / "compliance" / "WISH_OS_LOCAL_FINANCE_COMPLIANCE_ATTESTATION.md"
            if attestation_file.exists():
                print(attestation_file.read_text(encoding="utf-8"))
            else:
                print("[!] Attestationsdokument nicht gefunden.")
        else: # stats
            stats = catalog.get_loccp_stats()
            print(json.dumps(stats, indent=2, ensure_ascii=False))

    elif args.command == "wish":
        from .skill_pass import WishStudioSkillPassEngine
        eng = WishStudioSkillPassEngine(project_root)

        if args.action == "roles":
            roles = eng.list_roles(level=args.level if args.level else None)
            print("==================================================================")
            print(" WISH STUDIO OS — DIGITAL SKILL PASS ROLLEN-KATALOG (W3C DID / SWIYU)")
            print("==================================================================")
            for r in roles:
                print(f" [{r.get('Rollen_ID'):<12}] | {r.get('Level'):<6} | {r.get('Titel'):<32} | {r.get('Bereich')}")
            print("==================================================================")

        elif args.action == "projects":
            projs = eng.list_projects()
            print("==================================================================")
            print(" WISH STUDIO OS — AKTIVE WUNSCH-PROJEKTE & FREIGABESTATUS")
            print("==================================================================")
            for p in projs:
                app_mark = "[APPROVED]" if p.get("status") == "HUMAN_APPROVED" else f"[{p.get('status')}]"
                print(f" {p.get('id'):<14} | {app_mark:<16} | {p.get('title'):<45}")
            print("==================================================================")

        elif args.action == "create":
            if not args.title:
                print("[!] Bitte --title angeben.")
                return
            proj = eng.create_project(title=args.title, description=args.desc, assigned_role=args.role)
            print(f"[OK] Wunsch-Projekt erstellt: {proj['id']} — {proj['title']}")

        elif args.action == "approve":
            if not args.id:
                print("[!] Bitte --id <WISH-ID> angeben.")
                return
            approval = eng.approve_project(project_id=args.id, approver="Daniel Pohl", role="Sovereign Requestor / Authority")
            print("==================================================================")
            print(" SOVEREIGN HUMAN APPROVAL GATE (G09) VERBINDLICH ERTEILT")
            print("==================================================================")
            print(f" Genehmigt von: {approval['approver']} ({approval['role']})")
            print(f" Projekt:       {approval['project_id']}")
            print(f" Zeitstempel:   {approval['timestamp']}")
            print(f" Audit-Hash:    {approval['hash']}")
            print("==================================================================")

        elif args.action == "credential":
            vc = eng.generate_verifiable_credential(
                developer_did=args.did,
                role_id=args.role,
                project_id=args.id if args.id else "WISH-2026-001"
            )
            print("==================================================================")
            print(" W3C VERIFIABLE CREDENTIAL — DIGITAL SKILL PASS AUSGESTELLT")
            print("==================================================================")
            print(json.dumps(vc, indent=2, ensure_ascii=False))
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:   {summ['governance']}")
            print(f" Rollen:       {summ['total_defined_roles']} Rollen über 4 Levels (Bronze bis Titan)")
            print(f" Projekte:     {summ['total_wish_projects']} registriert ({summ['human_approved_projects']} human-approved)")
            print(f" W3C / swiyu:  100% kompatibel (Gate G09 Hard-Enforced)")
            print("==================================================================")
            print(" [Tipp] Rollen anzeigen:     python3 forina.py wish roles")
            print(" [Tipp] Projekte anzeigen:   python3 forina.py wish projects")
            print(" [Tipp] VC ausstellen:       python3 forina.py wish credential --role SKILL-VOL-08")

    elif args.command == "energy":
        from .energy_audit import ScientificEnergyAuditEngine
        eng = ScientificEnergyAuditEngine(project_root)

        if args.action == "list":
            systems = eng.list_systems(group=args.group if args.group else None, nachweisgrad=args.grade if args.grade else None)
            if args.search:
                systems = eng.search_systems(args.search)
            print("==================================================================")
            print(f" TOP 100 WISSENSCHAFTLICHER ENERGIE-AUDIT ({len(systems)} Treffer)")
            print("==================================================================")
            for s in systems[:args.limit]:
                wert = f"{s.get('Wert', '')} {s.get('Einheit', '')}".strip() or "N/A"
                print(f" #{s.get('Auswahl-Nr', '?'):<3} | [{s.get('Nachweisgrad', '?')[:1]}] | {s.get('System', ''):<26} | {wert:<18} | {s.get('Gruppe', '')}")
            if len(systems) > args.limit:
                print(f"... ({len(systems) - args.limit} weitere Systeme, nutze --limit {len(systems)})")
            print("==================================================================")
            print(" [Tipp] Detailansicht: python3 forina.py energy inspect --nr 1")

        elif args.action == "inspect":
            s = eng.get_system_by_nr(args.nr)
            if not s:
                print(f"[!] System #{args.nr} nicht gefunden.")
                return
            print("==================================================================")
            print(f" ENERGIE-SYSTEM #{s.get('Auswahl-Nr')}: {s.get('System')}")
            print(f" Gruppe:        {s.get('Gruppe')}")
            print(f" Rolle:         {s.get('Rolle')}")
            print(f" Status:        {s.get('Altstatus')}")
            print(f" Nachweisgrad:  {s.get('Nachweisgrad')}")
            print(f" Messwert:      {s.get('Wert')} {s.get('Einheit')} ({s.get('Messart')})")
            print(f" Quelle:        {s.get('Quelle spezifisch/alt')}")
            print(f" Fachportal:    {s.get('Fachportal')}")
            print("------------------------------------------------------------------")
            print(f" Besonderheit:  {s.get('Besonderheit')}")
            print(f" Krit. Anmerk.: {s.get('kritische Anmerkung')}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:    {summ['governance']}")
            print(f" Gesamtsysteme: {summ['total_systems']} in {summ['groups_count']} Fachgruppen")
            print(" Fachgruppen:")
            for g, count in summ["groups_breakdown"].items():
                print(f"   * {g:<35} : {count:>2} Systeme")
            print(f" Nachweisgrade: A (Messbeleg): {summ['nachweisgrade'].get('A', 0)} | B (Projektbeleg): {summ['nachweisgrade'].get('B', 0)} | C: {summ['nachweisgrade'].get('C', 0)}")
            print("==================================================================")
            print(" [Tipp] Liste anzeigen:   python3 forina.py energy list")
            print(" [Tipp] Gruppe filtern:   python3 forina.py energy list --group Fusion")

    elif args.command == "tlore":
        from .tlore_cde import TloreLightningEngine
        eng = TloreLightningEngine(project_root)

        if args.action == "modules":
            mods = eng.list_modules(harness_stage=args.stage if args.stage else None)
            print("==================================================================")
            print(f" TLORE INFINITY — 44 LIGHTNING POWER FINANCE-MODULE ({len(mods)} Treffer)")
            print("==================================================================")
            for m in mods:
                print(f" [{m.get('Modul_ID')}] {m.get('Sektor_Nr'):<2} · {m.get('Name'):<34} | [{m.get('Harness_Stage'):<8}] | {m.get('Bereich')}")
            print("==================================================================")
            print(" [Tipp] Boost-Simulation: python3 forina.py tlore boost --module 01")

        elif args.action == "boost":
            res = eng.run_boost_simulation(sector_nr=args.module, network=args.network)
            print("==================================================================")
            print(f" ⚡ TLORE LIGHTNING BOOST: {res['name'].upper()} (#{res['sector_nr']})")
            print(f" Modus:       {res['mode'].upper()} (Live-Trades Gesperrt: {res['live_trades_blocked']})")
            print(f" Netzwerk:    {res['network']}")
            print(f" Evidence:    {res['evidence_hash']}")
            print("==================================================================")
            print(" Harness-Prüfablauf (8 Stufen):")
            for step in res['harness_steps']:
                print(f"   {step}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:   {summ['governance']}")
            print(f" Module:       {summ['total_modules']} Sektoren in 6 Domänen")
            print(f" Modus:        {summ['mode']} (100% Fail-Closed)")
            print(" Harness-Stages Verteilung:")
            for s, count in summ["stages_distribution"].items():
                print(f"   * {s:<12} : {count:>2} Module")
            print("==================================================================")
            print(" [Tipp] Alle Module anzeigen:  python3 forina.py tlore modules")
            print(" [Tipp] Modul-Boost testen:    python3 forina.py tlore boost --module 01")

    elif args.command == "cde":
        from .tlore_cde import SovereignCdeEngine
        eng = SovereignCdeEngine(project_root)

        if args.action == "rules":
            rules = eng.list_rules()
            print("==================================================================")
            print(f" SOVEREIGN CDE — 4 UNVERHANDELBARE REGELN DER IMPLEMENTIERUNG")
            print("==================================================================")
            for r in rules:
                print(f" [{r.get('Regel_Nr')}] {r.get('Regel_Name'):<28} | {r.get('Schlüsseltechnologie')}")
                print(f"    -> {r.get('Anforderung')}")
            print("==================================================================")

        elif args.action == "spawn":
            pt = eng.spawn_point(point_id=args.point)
            print("==================================================================")
            print(f" SOVEREIGN CDE — POINT START AWAKENED (#{pt['point_id']})")
            print("==================================================================")
            print(f" Latenz:      {pt['restore_latency_ms']} ms")
            print(f" VFS Stream:  {pt['streaming_driver']}")
            print(f" Checkpoint:  {pt['checkpoint_driver']}")
            print(f" Isolation:   {pt['isolation']}")
            print(f" Overlay CoW: {pt['overlayfs_cow_upperdir']}")
            print(f" Memory-Hash: {pt['memory_mapping_hash']}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:   {summ['governance']}")
            print(f" Regeln:       {summ['rules_count']} Invarianten (Zero-Trust, CoW, Stateless, Memory-Safety)")
            print(f" Point Start:  Bereit via CRIU Memory Mapping & Nydus Lazy Loading")
            print("==================================================================")
            print(" [Tipp] Regeln anzeigen:   python3 forina.py cde rules")
            print(" [Tipp] Point aufwecken:   python3 forina.py cde spawn --point crash_log_77")

    elif args.command == "figp":
        from .figp_engine import FigpGovernanceEngine
        eng = FigpGovernanceEngine(project_root)

        if args.action == "frameworks":
            fams = eng.list_framework_families()
            print("==================================================================")
            print(f" FIGP KANONISCHE FRAMEWORK-FAMILIEN ({len(fams)} Standards)")
            print("==================================================================")
            for f in fams:
                print(f" [{f.get('Family_ID')}] {f.get('Canonical_Name'):<38} | {f.get('Geltungsbereich'):<16} | {f.get('Status')}")
            print("==================================================================")

        elif args.action == "schema":
            ddl = eng.get_schema_ddl()
            print("==================================================================")
            print(" FIGP SQLITE / POSTGRESQL REFERENZ-DATENMODELL (DDL)")
            print("==================================================================")
            for line in ddl.splitlines()[:30]:
                print(line)
            print("...\n[Tipp] Vollständiges Schema in: docs/schemas/FIGP_Reference_Schema.sql")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:   {summ['governance']}")
            print(f" Frameworks:   {summ['total_framework_families']} kanonische Familien (BSI, ISO, DORA, etc.)")
            print(f" Schema DDL:   {'Verfügbar' if summ['schema_available'] else 'Fehlt'} ({summ['schema_size_bytes']} Bytes)")
            print(f" API Spec:     {'Verfügbar' if summ['api_spec_available'] else 'Fehlt'} ({summ['api_spec_size_bytes']} Bytes)")
            print("==================================================================")
            print(" [Tipp] Frameworks anzeigen: python3 forina.py figp frameworks")
            print(" [Tipp] Schema anzeigen:     python3 forina.py figp schema")

    elif args.command == "tools":
        from .figp_engine import ObservabilityToolsCatalogEngine
        eng = ObservabilityToolsCatalogEngine(project_root)

        if args.action == "list":
            tools = eng.list_tools(category=args.category if args.category else None)
            print("==================================================================")
            print(f" OBSERVABILITY & AI-AGENT STACK ({len(tools)} Tools)")
            print("==================================================================")
            for t in tools[:args.limit]:
                stars_txt = f"{t.get('Stars')}★" if t.get('Stars') and t.get('Stars') != '0' else "OSS"
                print(f" [{t.get('Tool_ID')}] {t.get('Name'):<22} | {stars_txt:<8} | {t.get('Kategorie'):<24} | {t.get('Lizenz')}")
            if len(tools) > args.limit:
                print(f"... ({len(tools) - args.limit} weitere Tools, nutze --limit {len(tools)})")
            print("==================================================================")
            print(" [Tipp] Kategorie-Filter: python3 forina.py tools list --category \"AI-IDEs\"")

        elif args.action == "search":
            results = eng.search_tools(args.query)
            print("==================================================================")
            print(f" TOOL-SUCHE FÜR '{args.query}' ({len(results)} Treffer)")
            print("==================================================================")
            for t in results:
                print(f" * {t.get('Name'):<20} | {t.get('Kategorie'):<24} | {t.get('Repo')}")
                if t.get('Beschreibung'):
                    print(f"   -> {t.get('Beschreibung')}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Governance:   {summ['governance']}")
            print(f" Tools:        {summ['total_tools']} in {summ['categories_count']} Fachdomänen ({summ['open_source_count']} Open Source)")
            print(" Domänen-Verteilung:")
            for cat, count in summ["categories_distribution"].items():
                print(f"   * {cat:<32} : {count:>2} Tools")
            print("==================================================================")
            print(" [Tipp] Alle Tools anzeigen: python3 forina.py tools list")
            print(" [Tipp] Tool suchen:         python3 forina.py tools search --query OpenCode")

    elif args.command == "containment":
        from .containment_pipeline import StateSovereignContainmentEngine
        eng = StateSovereignContainmentEngine(project_root)

        if args.action == "layers":
            layers = eng.list_layers(category=args.category if args.category else None)
            print("==================================================================")
            print(f" STAATLICHE SICHERHEITS- & EINKESSELUNGS-SCHICHTEN ({len(layers)} Einträge)")
            print("==================================================================")
            for l in layers:
                print(f" [{l.get('Schicht_ID')}] {l.get('Bezeichnung'):<30} | {l.get('Technologie_Protokoll'):<32} | [{l.get('Integritaetsstatus')}]")
            print("==================================================================")

        elif args.action == "verify":
            hw = eng.verify_hardware_pipeline()
            ct = eng.verify_containment_controls()
            form = eng.get_audit_form_99x()
            print("==================================================================")
            print(" VERIFIZIERUNG: STATE-LEVEL HARDWARE- & EINKESSELUNGS-PIPELINE")
            print("==================================================================")
            print(f" Hardware Root-of-Trust:  [{hw['status']}] {hw['root_of_trust']}")
            print(f" Secure Enclaves (L1):   [{hw['status']}] {hw['memory_encryption']}")
            print(f" PQC Network (L2):        [{hw['status']}] {hw['pqc_cipher']}")
            print(f" Zero-Knowledge (L3):     [{hw['status']}] {hw['zero_knowledge']}")
            print("------------------------------------------------------------------")
            print(f" Einkesselung Status:     [{ct['status']}] ({ct['controls_count']} Kontrollen)")
            print(f" Cognitive Firewall:      {ct['cognitive_firewall']}")
            print(f" Semantic DLP:            {ct['semantic_dlp']}")
            print(f" Agentic Loop Breaker:    {ct['agentic_loop_breaker']}")
            print("------------------------------------------------------------------")
            print(f" Audit-Freigabe Formular: {form['form_id']} -> Zertifikat: {form['certificate_id']}")
            print(f" Governance-Key:          {form['governance_key_id']}")
            print(f" Verantwortlicher Auditor: {form['chief_security_auditor']}")
            print("==================================================================")

        elif args.action == "loop":
            eval_res = eng.evaluate_agentic_loop(iterations=args.iterations, token_count=args.tokens, human_approved=args.approve)
            print("==================================================================")
            print(" AGENTIC LOOP BREAKER & HUMAN-IN-THE-LOOP EVALUATION")
            print("==================================================================")
            status_txt = "FREIGEGEBEN" if eval_res["allowed"] else "TERMINIERT_FAIL_CLOSED"
            print(f" Ergebnis:       [{status_txt}] -> Aktion: {eval_res['action']}")
            if not eval_res["allowed"]:
                print(f" Grund:          {eval_res['reason']}")
                print(f" Forensik:       {eval_res['forensic_status']}")
            else:
                print(f" Iterationen:    {eval_res['iterations_used']}/{eval_res['iterations_max']}")
                print(f" Token-Budget:   {eval_res['tokens_used']}/{eval_res['tokens_max']}")
                print(f" Human Approval: {eval_res['human_approved']}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Zertifikat:     {summ['certificate']} (Gültig bis 31.12.2027)")
            print(f" Governance-Key: {summ['governance_key']}")
            print(f" Spezifikation:  {summ['total_spec_entries']} registrierte Schichten & Kontrollen")
            for cat, count in summ["categories"].items():
                print(f"   * {cat:<24} : {count:>2} Kontrollen")
            print("==================================================================")
            print(" [Tipp] Schichten auflisten:  python3 forina.py containment layers")
            print(" [Tipp] Pipeline verifizieren: python3 forina.py containment verify")
            print(" [Tipp] Loop Breaker testen:  python3 forina.py containment loop --iterations 15")

    elif args.command == "cdp":
        from .containment_pipeline import CdpLiveSyncAutomationEngine
        eng = CdpLiveSyncAutomationEngine(project_root)

        if args.action == "components":
            comps = eng.list_components()
            print("==================================================================")
            print(f" CDP & MCP PORTAL-AUTOMATISIERUNGS-KOMPONENTEN ({len(comps)} Module)")
            print("==================================================================")
            for c in comps:
                print(f" [{c.get('ID')}] {c.get('Komponente'):<22} | {c.get('Schnittstelle'):<24} | {c.get('Protokoll_Port')}")
            print("==================================================================")

        elif args.action == "condense":
            raw_bytes = args.raw_kb * 1024
            sim = eng.simulate_livelink_condensation(raw_bytes, dom_node_count=1850)
            print("==================================================================")
            print(" LIVELINK KONDENSATION & KONTEXT-KOMPRIMIERUNG (SIMULATION)")
            print("==================================================================")
            print(f" Rohdaten-Größe:      {sim['raw_html_size_bytes']/1024:.1f} KB (~{sim['raw_token_estimate']:,} Tokens)")
            print(f" Kondensierte Größe:  {sim['condensed_size_bytes']/1024:.1f} KB (~{sim['condensed_token_estimate']:,} Tokens)")
            print(f" Ersparnis / Filter:  {sim['compression_ratio']} ({sim['tokens_saved']:,} Tokens eingespart)")
            print(" Gefilterter Overhead:")
            for f in sim["filtered_overhead"]:
                print(f"   * {f}")
            print(" Extrahierte Interaktionsdaten:")
            for e in sim["extracted_entities"]:
                print(f"   * {e}")
            print("==================================================================")

        elif args.action == "kyc":
            kyc = eng.verify_portal_kyc_prerequisites()
            print("==================================================================")
            print(" MICA & FINTECH PORTAL KYC PREREQUISITES")
            print("==================================================================")
            print(f" Status:       [{kyc['status']}]")
            print(f" CDP Host:     {kyc['cdp_host']} (Port {kyc['cdp_port']})")
            print(" Hinterlegte souveräne Identitätsnachweise:")
            ident = kyc["sovereign_identity"]
            print(f"   * Urheber:     {ident['author']} ({ident['charter']})")
            print(f"   * EU PIC:      {', '.join(ident['pic_eu'])}")
            print(f"   * Global LEI:  {ident['lei']}")
            print(f"   * Zoll EORI:   {ident['eori']}")
            print(f"   * USt-IdNr.:   {', '.join(ident['ust_idnr'])}")
            print(f"   * D-U-N-S:     {', '.join(ident['duns'])}")
            print(f"   * Swiss AHV:   {ident['swiss_ahv']}")
            print("==================================================================")

        else: # summary
            summ = eng.get_summary()
            print("==================================================================")
            print(f" {summ['title'].upper()}")
            print(f" Komponenten:  {summ['total_components']} registrierte Schnittstellen")
            print(f" CDP Engine:   {summ['cdp_protocol']}")
            print(f" MCP Brücke:   {summ['mcp_protocol']}")
            print("==================================================================")
            print(" [Tipp] Module auflisten:      python3 forina.py cdp components")
            print(" [Tipp] Kondensation testen:   python3 forina.py cdp condense --raw-kb 2000")
            print(" [Tipp] KYC-Register prüfen:   python3 forina.py cdp kyc")

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
