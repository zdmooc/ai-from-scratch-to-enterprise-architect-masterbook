"""Unit tests for synthetic and strictly read-only symbolic inference."""
import unittest
from rule_engine import DEMO_RULES, Rule, forward_chain


class RulesTests(unittest.TestCase):
    def test_positive_readonly_path(self):
        facts, trace = forward_chain(
            {"payment_status_unknown", "requester_authenticated", "readonly_scope"},
            DEMO_RULES,
        )
        self.assertIn("investigation_candidate", facts)
        self.assertIn("read_events_permitted", facts)
        self.assertIn("audit_required", facts)
        self.assertEqual([d.rule for d in trace], ["R01", "R02", "R03"])

    def test_deny_without_authentication(self):
        facts, trace = forward_chain(
            {"payment_status_unknown", "readonly_scope"}, DEMO_RULES
        )
        self.assertNotIn("investigation_candidate", facts)
        self.assertNotIn("read_events_permitted", facts)
        self.assertEqual(trace, ())

    def test_no_mutation_capability_derived(self):
        facts, _ = forward_chain(
            {"payment_status_unknown", "requester_authenticated", "readonly_scope"},
            DEMO_RULES,
        )
        self.assertNotIn("payment_mutation_allowed", facts)

    def test_idempotent(self):
        initial = {"payment_status_unknown", "requester_authenticated", "readonly_scope"}
        first, trace = forward_chain(initial, DEMO_RULES)
        second, repeated_trace = forward_chain(first, DEMO_RULES)
        self.assertEqual(first, second)
        self.assertEqual(repeated_trace, ())
        self.assertEqual(len(trace), 3)

    def test_cycle_stops_at_fixed_point(self):
        circular = (
            Rule("A", frozenset({"seed"}), "next"),
            Rule("B", frozenset({"next"}), "seed"),
        )
        facts, trace = forward_chain({"seed"}, circular)
        self.assertEqual(facts, frozenset({"seed", "next"}))
        self.assertEqual(len(trace), 1)

    def test_manual_review_uses_explicit_unavailable_fact(self):
        rules = (*DEMO_RULES,
            Rule("R04", frozenset({"investigation_candidate", "events_unavailable"}), "manual_review_required"))
        facts, trace = forward_chain(
            {"requester_authenticated", "payment_status_unknown", "events_unavailable"}, rules
        )
        self.assertIn("manual_review_required", facts)
        self.assertNotIn("read_events_permitted", facts)
        self.assertIn("R04", [x.rule for x in trace])

    def test_invalid_rule_rejected(self):
        with self.assertRaises(ValueError):
            forward_chain({"x"}, (Rule("bad", frozenset(), "y"),))


if __name__ == "__main__":
    unittest.main()
