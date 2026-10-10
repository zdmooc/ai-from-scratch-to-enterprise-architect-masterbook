"""Synthetic negative tests for the read-only agent dispatcher."""
import unittest
from agent_dispatcher import DOCUMENTS, TICKETS, dispatch, run_plan


class AgentGuardrailTests(unittest.TestCase):
    def test_read_accessible_ticket(self):
        result = dispatch("alice", "read_ticket", "A-001")
        self.assertEqual(result["status"], "waiting_for_review")

    def test_read_accessible_document(self):
        self.assertEqual(dispatch("alice", "read_document", "A-PUBLIC")["document_id"], "A-PUBLIC")

    def test_cross_tenant_ticket_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "read_ticket", "B-001")

    def test_cross_tenant_document_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "read_document", "B-PUBLIC")

    def test_role_restricted_document_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "read_document", "A-PRIVATE")

    def test_supervisor_allowed_restricted_document(self):
        self.assertEqual(dispatch("supervisor", "read_document", "A-PRIVATE")["document_id"], "A-PRIVATE")

    def test_unknown_user_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("stranger", "read_ticket", "A-001")

    def test_mutation_tool_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "delete_ticket", "A-001")

    def test_unknown_tool_denied(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "run_shell", "A-001")

    def test_untrusted_document_does_not_add_tool(self):
        text = dispatch("alice", "read_document", "A-UNTRUSTED")["content"]
        self.assertIn("delete_ticket", text)
        with self.assertRaises(PermissionError):
            dispatch("alice", "delete_ticket", "A-001")

    def test_max_steps_enforced(self):
        with self.assertRaises(ValueError):
            run_plan("alice", (("read_ticket", "A-001"),) * 4, max_steps=3)

    def test_invalid_bound_rejected(self):
        with self.assertRaises(ValueError):
            run_plan("alice", (), max_steps=0)
        with self.assertRaises(ValueError):
            run_plan("alice", (), max_steps=True)

    def test_bounded_read_only_success(self):
        output = run_plan("alice", (("read_ticket", "A-001"), ("read_document", "A-PUBLIC")))
        self.assertEqual(len(output), 2)

    def test_denied_plan_does_not_mutate_in_memory_records(self):
        before = dict(TICKETS["A-001"])
        try:
            run_plan("alice", (("read_ticket", "A-001"), ("delete_ticket", "A-001")))
        except PermissionError:
            pass
        self.assertEqual(TICKETS["A-001"], before)

    def test_unknown_resource_does_not_leak_data(self):
        with self.assertRaises(PermissionError):
            dispatch("alice", "read_document", "DOES-NOT-EXIST")

    def test_data_not_interpreted_as_permission(self):
        before = set(DOCUMENTS)
        dispatch("alice", "read_document", "A-UNTRUSTED")
        self.assertEqual(set(DOCUMENTS), before)


if __name__ == "__main__":
    unittest.main()
