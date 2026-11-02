"""
Minimal transparent scorer for the Industrial AI Evaluation Framework.
Illustrative only — demonstrates the five dimensions on synthetic cases.
No external API or model is called.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


DIMENSIONS = [
    "accuracy",
    "evidence",
    "process_compliance",
    "risk_awareness",
    "traceability",
]

WEIGHTS = {
    "accuracy": 0.25,
    "evidence": 0.20,
    "process_compliance": 0.20,
    "risk_awareness": 0.20,
    "traceability": 0.15,
}


@dataclass
class CaseScore:
    case_id: str
    scores: Dict[str, float]          # 0–5 per dimension
    critical_error: bool
    critical_reason: str
    weighted_total: float
    recommendation: str               # PASS_REVIEW | REVIEW | BLOCK


def weighted_score(scores: Dict[str, float]) -> float:
    return round(sum(scores[d] * WEIGHTS[d] for d in DIMENSIONS) * 20, 1)  # scale to ~100


def recommend(scores: Dict[str, float], critical: bool) -> str:
    if critical:
        return "BLOCK"
    total = weighted_score(scores)
    if total >= 80 and all(scores[d] >= 3 for d in DIMENSIONS):
        return "PASS_REVIEW"
    return "REVIEW"


def evaluate_case(case_id: str, scores: Dict[str, float], critical: bool = False, reason: str = "") -> CaseScore:
    return CaseScore(
        case_id=case_id,
        scores=scores,
        critical_error=critical,
        critical_reason=reason,
        weighted_total=weighted_score(scores),
        recommendation=recommend(scores, critical),
    )


# --- Synthetic demo cases (illustrative) ------------------------------------
DEMO_CASES: List[CaseScore] = [
    evaluate_case(
        "QA-001",
        {"accuracy": 5, "evidence": 5, "process_compliance": 4, "risk_awareness": 4, "traceability": 5},
    ),
    evaluate_case(
        "QA-002",
        {"accuracy": 4, "evidence": 2, "process_compliance": 3, "risk_awareness": 3, "traceability": 2},
        critical=True,
        reason="Required evidence IDs missing; claims not traceable",
    ),
    evaluate_case(
        "FMEA-001",
        {"accuracy": 3, "evidence": 3, "process_compliance": 2, "risk_awareness": 4, "traceability": 3},
        critical=True,
        reason="Skipped mandatory severity justification step",
    ),
    evaluate_case(
        "PPAP-001",
        {"accuracy": 4, "evidence": 4, "process_compliance": 4, "risk_awareness": 3, "traceability": 4},
    ),
]


def main() -> None:
    print("Industrial AI Evaluation — Example Scorer\n" + "=" * 50)
    for case in DEMO_CASES:
        print(f"\n{case.case_id}  |  {case.weighted_total:5.1f}/100  |  {case.recommendation}")
        print(f"  Scores : {case.scores}")
        if case.critical_error:
            print(f"  CRITICAL: {case.critical_reason}")
    print("\n" + "=" * 50)
    print("Note: Synthetic illustration only. Critical errors force BLOCK.")


if __name__ == "__main__":
    main()
