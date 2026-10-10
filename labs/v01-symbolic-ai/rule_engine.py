#!/usr/bin/env python3
"""Minimal forward-chaining engine for an educational, synthetic payment scenario.

No production transaction, external service, AI model, account or network is accessed.
"""
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Rule:
    """A monotonic Horn-like rule over positive propositional facts."""

    name: str
    premises: frozenset[str]
    conclusion: str


@dataclass(frozen=True)
class Derivation:
    """The evidence of one derived proposition."""

    rule: str
    premises: tuple[str, ...]
    conclusion: str


def forward_chain(
    initial_facts: Iterable[str],
    rules: Sequence[Rule],
) -> tuple[frozenset[str], tuple[Derivation, ...]]:
    """Derive positive facts until a fixed point is reached.

    Termination holds because each iteration introduces a previously absent
    conclusion, and the given sequence contains a finite number of rules.
    """
    facts = set(initial_facts)
    trace: list[Derivation] = []
    for rule in rules:
        if not rule.name or not rule.conclusion or not rule.premises:
            raise ValueError("Each rule needs a name, conclusion and premises.")
    while True:
        changed = False
        for rule in rules:
            if rule.premises.issubset(facts) and rule.conclusion not in facts:
                facts.add(rule.conclusion)
                trace.append(
                    Derivation(
                        rule=rule.name,
                        premises=tuple(sorted(rule.premises)),
                        conclusion=rule.conclusion,
                    )
                )
                changed = True
        if not changed:
            break
    return frozenset(facts), tuple(trace)


DEMO_RULES = (
    Rule("R01", frozenset({"payment_status_unknown", "requester_authenticated"}), "investigation_candidate"),
    Rule("R02", frozenset({"investigation_candidate", "readonly_scope"}), "read_events_permitted"),
    Rule("R03", frozenset({"read_events_permitted"}), "audit_required"),
)


def main() -> None:
    initial = frozenset(
        {"payment_status_unknown", "requester_authenticated", "readonly_scope"}
    )
    inferred, trace = forward_chain(initial, DEMO_RULES)
    print("OBSERVATIONS:", ", ".join(sorted(initial)))
    for event in trace:
        print(f"DERIVED [{event.rule}] {event.conclusion} <- {', '.join(event.premises)}")
    print("FACTS:", ", ".join(sorted(inferred)))
    print("PAYMENT_MUTATION_ALLOWED:", "payment_mutation_allowed" in inferred)


if __name__ == "__main__":
    main()
