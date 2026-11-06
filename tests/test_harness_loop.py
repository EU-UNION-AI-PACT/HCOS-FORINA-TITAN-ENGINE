# -*- coding: utf-8 -*-
"""Unit tests for HCOS Harness Control Loop (HCL) Engine."""
import unittest
from forina_engine.harness_control_loop import (
    HarnessControlLoopEngine,
    WorkItem,
    HarnessState,
    HarnessViolation,
    synthetic_builder
)


class TestHarnessControlLoop(unittest.TestCase):
    def setUp(self):
        self.engine = HarnessControlLoopEngine()

    def task(self, **kw):
        d = dict(
            task_id="TEST-123",
            requirement="Need exact gate evidence",
            proposed_change="Use signed view models"
        )
        d.update(kw)
        return WorkItem(**d)

    def test_default_requires_human_review(self):
        x = self.engine.run_cycle(self.task())
        self.assertEqual(x.state, HarnessState.REVIEW_REQUIRED)
        self.assertEqual(x.iterations, 1)

    def test_cannot_release_without_external_isolation_evidence(self):
        x = self.engine.run_cycle(self.task(human_approval=True))
        self.assertEqual(x.state, HarnessState.REVIEW_REQUIRED)
        self.assertIn("External isolation evidence missing", x.stop_reason)

    def test_ready_only_with_explicit_checks_and_approval(self):
        x = self.engine.run_cycle(self.task(human_approval=True, external_isolation_verified=True))
        self.assertEqual(x.state, HarnessState.READY_FOR_CONTROLLED_RELEASE)
        self.assertIn("approved for controlled staging", x.stop_reason)

    def test_network_capability_forbidden(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(allow_network=True))

    def test_real_money_forbidden(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(allow_real_money=True))

    def test_secret_access_forbidden(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(allow_secret_access=True))

    def test_host_mutation_forbidden(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(allow_host_mutation=True))

    def test_leaked_token_refused_at_intake(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(proposed_change="ghp_123456789012345678901234567890"))

    def test_invalid_task_id_refused(self):
        with self.assertRaises(HarnessViolation):
            self.engine.run_cycle(self.task(task_id="INVALID!ID#"))

    def test_to_dict_and_json(self):
        x = self.engine.run_cycle(self.task())
        d = x.to_dict()
        self.assertEqual(d["task_id"], "TEST-123")
        self.assertEqual(d["state"], "REVIEW_REQUIRED")
        self.assertTrue(len(d["evidence"]) > 0)
        json_str = x.to_json()
        self.assertIn("TEST-123", json_str)


if __name__ == "__main__":
    unittest.main()
