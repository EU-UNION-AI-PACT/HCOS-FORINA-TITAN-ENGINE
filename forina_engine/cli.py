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

    # repos (50 Repositories Explorer)
    repo_parser = subparsers.add_parser("repos", help="Erforscht die 50 Open-Source Repositories der Spezifikation")
    repo_parser.add_argument("action", choices=["list", "summary", "zone", "inspect"], default="list", nargs="?", help="Aktion: list, summary, zone, inspect")
    repo_parser.add_argument("--zone", type=str, default="", help="Zone Filter: sovereign, dev, federation")
    repo_parser.add_argument("--nr", type=int, default=1, help="Repository Nummer fuer inspect (1-50)")

    # concepts (34 Concept Papers Suite)
    concept_parser = subparsers.add_parser("concepts", help="34 Concept Papers Suite & Normenabdeckung v2.0")
    concept_parser.add_argument("action", choices=["list", "summary", "inspect", "standards"], default="list", nargs="?", help="Aktion: list, summary, inspect, standards")
    concept_parser.add_argument("--nr", type=int, default=1, help="Papier-Nummer (1-34)")
    concept_parser.add_argument("--search", type=str, default="", help="Suchbegriff für Concept Papers")

    # harness (Automated Harness Loop)
    harness_parser = subparsers.add_parser("harness", help="Automatisierter 8-Stufen Harness-Loop")
    harness_parser.add_argument("action", choices=["status", "run", "stages"], default="status", nargs="?", help="Aktion: status, run, stages")

    # zeroclock (Act Pack Zero Clock & NaTZa CFS)
    zc_parser = subparsers.add_parser("zeroclock", help="Act Pack Zero Clock (APZC) & NaTZa CFS Telemetrie")
    zc_parser.add_argument("action", choices=["status", "tick", "tmr", "spawn"], default="status", nargs="?", help="Aktion: status, tick, tmr, spawn")
    zc_parser.add_argument("--subtask", type=str, default="microtask_audit", help="Subtask Name fuer spawn")

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

        elif args.action == "inspect":
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
            print("==================================================================")

        elif args.action == "standards":
            print("==================================================================")
            print(f" HCOS FORINA TITAN — NORMEN- & ZERTIFIZIERUNGSKATALOG ({len(suite.standards)} Standards)")
            print("==================================================================")
            for std in suite.standards:
                print(f" - {std['name']:<22} | {std['category']:<22} | {std['domain']}")
            print("==================================================================")

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
            print(f" [Tipp] Detailansicht mit: python3 forina.py concepts inspect --nr <1-34>")

    elif args.command == "harness":
        harness = HarnessLoopEngine(project_root)

        if args.action == "run":
            print(">>> Starte vollständigen 8-Stufen Harness-Loop Durchlauf...")
            state = harness.run_cycle_iteration()
            print("==================================================================")
            print(f" HARNESS-LOOP ZYKLUS #{state['cycle_id']-1} ERFOLGREICH ABGESCHLOSSEN")
            print("==================================================================")
            for s_id, s_res in state['stage_results'].items():
                print(f" Stufe {s_id:<8} : [{s_res.get('status')}] {s_res.get('details', s_res.get('message', 'OK'))}")
            print("==================================================================")
            print(f" Status: {state['status']} -> Neuer Zielzustand: {state['current_stage']}")

        elif args.action == "stages":
            stages = harness.get_stages()
            print("==================================================================")
            print(" HCOS FORINA TITAN — 8 STUFEN DES AUTOMATISIERTEN HARNESS-LOOPS")
            print("==================================================================")
            for s in stages:
                print(f" {s['stage']}. {s['id']:<8} | {s['name']:<35} | {s['details']}")
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
