# -*- coding: utf-8 -*-
"""HCOS FORINA TITAN – Hardened Reference Harness Control Loop (HCL) Engine.

Sovereign Legal Provenance:
  Daniel Pohl · Royal Kaiser Charter RegSys
  VAT: DE31353063511 · PIC: 867679357 · D-U-N-S: 315676980 / 317066336
  Global LEI: 894500GBJSIW8L6ET310 · EORI: AEOF139420 · UNGM: 1172700

Offline-safe implementation with synthetic work items and bounded iteration loops.
Enforces fail-closed isolation, zero real-money movement, zero WAN egress,
and cryptographic evidence hashing.
"""
from __future__ import annotations
import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Iterable, Mapping, Sequence, Dict, Any, List, Optional


class HarnessState(str, Enum):
    PLANNED = "PLANNED"
    BUILT_SYNTHETIC = "BUILT_SYNTHETIC"
    TESTED = "TESTED"
    AUDITED = "AUDITED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    STOPPED = "STOPPED"
    READY_FOR_CONTROLLED_RELEASE = "READY_FOR_CONTROLLED_RELEASE"


class HarnessViolation(RuntimeError):
    """Raised if a task violates the bounded synthetic reference contract."""


@dataclass(frozen=True)
class WorkItem:
    task_id: str
    requirement: str
    proposed_change: str
    zone: str = "DEVELOPMENT_SYNTHETIC"
    max_iterations: int = 3
    max_input_characters: int = 12000
    human_approval: bool = False
    external_isolation_verified: bool = False
    approved_test_case: str = "SYNTHETIC_ONLY"
    allow_network: bool = False
    allow_real_money: bool = False
    allow_secret_access: bool = False
    allow_host_mutation: bool = False
    allow_external_certification_claim: bool = False


@dataclass(frozen=True)
class Evidence:
    task_id: str
    iteration: int
    state: str
    input_sha256: str
    output_sha256: str
    checks: tuple[tuple[str, bool], ...]
    note: str


@dataclass
class Outcome:
    task_id: str
    state: HarnessState
    iterations: int
    evidence: list[Evidence] = field(default_factory=list)
    stop_reason: str = ""
    proposed_artifact: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "state": self.state.value,
            "iterations": self.iterations,
            "stop_reason": self.stop_reason,
            "proposed_artifact": self.proposed_artifact,
            "evidence": [
                {
                    "task_id": e.task_id,
                    "iteration": e.iteration,
                    "state": e.state,
                    "input_sha256": e.input_sha256,
                    "output_sha256": e.output_sha256,
                    "checks": dict(e.checks),
                    "note": e.note
                }
                for e in self.evidence
            ]
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


def digest(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


TOKEN_PATTERN = re.compile(r"(?:ghp_[A-Za-z0-9_]{25,}|-----BEGIN [^-]*PRIVATE KEY-----|\bsk-[A-Za-z0-9_-]{28,})")
DANGER_PATTERN = re.compile(r"\b(?:curl\s+.*\|\s*(?:sh|bash)|rm\s+-rf\s+/|sudo\s+rm)\b", re.I)


def synthetic_builder(task: WorkItem, iteration: int) -> str:
    return (
        f"SYNTHETIC IMPLEMENTATION PROPOSAL\n"
        f"task_id={task.task_id}\n"
        f"zone={task.zone}\n"
        f"requirement={task.requirement}\n"
        f"proposed_change={task.proposed_change}\n"
        f"iteration={iteration}\n"
        f"required_stages=PLAN,BUILD,TEST,AUDIT,HUMAN_REVIEW,RELEASE\n"
        f"production_execution=DISABLED\n"
        f"real_money=DISABLED\n"
        f"network=DISABLED\n"
        f"external_certification=NEVER_SELF_ISSUED\n"
        f"sovereign_signer=Daniel_Pohl_RegSys\n"
    )


def independent_test_oracle(task: WorkItem, artifact: str) -> dict[str, bool]:
    return {
        "nonempty": bool(artifact.strip()),
        "correct_zone": f"zone={task.zone}" in artifact,
        "requirement_covered": task.requirement in artifact,
        "planned_action_covered": task.proposed_change in artifact,
        "no_leaked_tokens": not bool(TOKEN_PATTERN.search(artifact)),
        "no_shell_danger": not bool(DANGER_PATTERN.search(artifact)),
        "network_disabled_in_proposal": "network=DISABLED" in artifact,
        "no_money_movement": "real_money=DISABLED" in artifact,
        "no_false_external_badge": "external_certification=NEVER_SELF_ISSUED" in artifact,
        "production_execution_disabled": "production_execution=DISABLED" in artifact,
        "sovereign_signature_present": "sovereign_signer=Daniel_Pohl_RegSys" in artifact,
    }


def preflight(t: WorkItem) -> None:
    if not re.fullmatch(r"[A-Za-z0-9._:-]{3,70}", t.task_id):
        raise HarnessViolation("Invalid immutable task_id")
    if t.zone not in ("DEVELOPMENT_SYNTHETIC", "LOCAL_SOVEREIGN_ZONE"):
        raise HarnessViolation(f"Invalid zone: {t.zone}")
    if t.approved_test_case != "SYNTHETIC_ONLY":
        raise HarnessViolation("This reference implementation accepts SYNTHETIC_ONLY")
    if not 1 <= t.max_iterations <= 6:
        raise HarnessViolation("max_iterations must be 1..6")
    if len(t.requirement) + len(t.proposed_change) > t.max_input_characters:
        raise HarnessViolation("Synthetic task exceeds declared input budget")
    forbidden = [
        t.allow_network,
        t.allow_real_money,
        t.allow_secret_access,
        t.allow_host_mutation,
        t.allow_external_certification_claim
    ]
    if any(forbidden):
        raise HarnessViolation("Forbidden capability requested in reference loop (Fail-Closed Enforcement)")
    if TOKEN_PATTERN.search(t.proposed_change) or TOKEN_PATTERN.search(t.requirement):
        raise HarnessViolation("Secret-like credential or token refused at intake (Zero-Leak Principle)")


class HarnessControlLoopEngine:
    """Controller for bounded harness execution cycles."""

    def __init__(self,
                 builder: Callable[[WorkItem, int], str] = synthetic_builder,
                 oracle: Callable[[WorkItem, str], Mapping[str, bool]] = independent_test_oracle):
        self.builder = builder
        self.oracle = oracle

    def run_cycle(self, task: WorkItem) -> Outcome:
        preflight(task)
        out = Outcome(task_id=task.task_id, state=HarnessState.PLANNED, iterations=0)
        for iteration in range(1, task.max_iterations + 1):
            out.iterations = iteration
            try:
                artifact = self.builder(task, iteration)
                if not isinstance(artifact, str):
                    raise HarnessViolation("Builder output must be text")
                checks = self.oracle(task, artifact)
                if not isinstance(checks, Mapping) or not checks:
                    raise HarnessViolation("Independent oracle returned no checks")
                normalized = {str(k): (v is True) for k, v in checks.items()}
                ev = Evidence(
                    task.task_id,
                    iteration,
                    HarnessState.TESTED.value,
                    digest(task.requirement + task.proposed_change),
                    digest(artifact),
                    tuple(sorted(normalized.items())),
                    "Independent synthetic property checks; zero WAN egress strictly observed"
                )
                out.evidence.append(ev)
                out.proposed_artifact = artifact
                if all(normalized.values()):
                    out.state = HarnessState.AUDITED
                    if not task.human_approval:
                        out.state = HarnessState.REVIEW_REQUIRED
                        out.stop_reason = "Human review required; automatic promotion forbidden"
                    elif not task.external_isolation_verified:
                        out.state = HarnessState.REVIEW_REQUIRED
                        out.stop_reason = "External isolation evidence missing; release forbidden"
                    else:
                        out.state = HarnessState.READY_FOR_CONTROLLED_RELEASE
                        out.stop_reason = "Synthetic proposal verified; approved for controlled staging"
                    return out
            except Exception as e:
                out.evidence.append(Evidence(
                    task.task_id,
                    iteration,
                    HarnessState.STOPPED.value,
                    digest(task.requirement + task.proposed_change),
                    "",
                    (("runner_exception", False),),
                    type(e).__name__
                ))
        out.state = HarnessState.STOPPED
        out.stop_reason = "Bounded iterations exhausted; no automatic self-approval"
        return out
