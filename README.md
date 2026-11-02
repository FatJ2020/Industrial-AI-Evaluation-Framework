# Industrial AI Evaluation Framework

### Human-vs-AI-Judge evaluation for manufacturing, quality and supply-chain LLM responses

**Portfolio project** — simulated benchmark using synthetic industrial scenarios.  
Applies quality-system thinking (traceability, process compliance, risk awareness) to LLM evaluation.

> Not a production evaluation platform.  
> All scenarios and scores are illustrative.  
> No confidential employer or customer data.

---

## Why this project exists

Enterprise LLM answers in industrial settings can fail in ways that general benchmarks miss:

- Missing or invented evidence  
- Weak process compliance (PPAP, FMEA, control plan)  
- Over-confidence on incomplete data  
- Low sensitivity to supply-chain or quality risk  

This framework adapts familiar quality principles to AI assurance so that teams can ask:

1. Is the answer accurate against the source of truth?  
2. Is the reasoning evidence-based?  
3. Does it respect process requirements?  
4. Does it surface relevant risks?  
5. Can we trace claims back to sources?

---

## Evaluation dimensions

| Dimension | What it checks |
|-----------|----------------|
| **Response Accuracy** | Factual correctness vs. reference / source |
| **Evidence-Based Reasoning** | Claims linked to identifiable evidence |
| **Process Compliance** | Respect for quality / APQP / PPAP / control rules |
| **Risk Awareness** | Appropriate escalation of quality, delivery or compliance risk |
| **Traceability** | Clear path from answer back to source artefacts |

---

## Evaluation domains covered

- Quality Governance  
- Cost & Supply Chain  
- FMEA  
- PPAP / Launch readiness  
- STA Supplier Compliance  
- Geopolitical / supply-chain resilience risk  

---

## Method (high level)

1. Build a small golden set of industrial questions + reference answers  
2. Collect model responses  
3. Score with a human rubric  
4. Score with an LLM-as-judge (secondary signal only)  
5. Flag critical errors (invented evidence, missed mandatory process step, etc.)  
6. Analyse disagreement and failure patterns  

---

## Key observed failure patterns (illustrative)

- Weak evidence traceability  
- Compliance reasoning gaps  
- False confidence on incomplete data  
- Over-reliance on status labels  
- LLM-judge optimism bias  

---

## Repository contents

```
README.md
LICENSE
.gitignore
docs/
  Evaluation_Rubric.md
  Human_Judge_Methodology.md
  LLM_Judge_Methodology.md
  Error_Analysis.md
  Metrics_Summary.md
data/
  sample_cases.csv          # small synthetic example set
src/
  score_example.py          # minimal transparent scorer
```

---

## Quick start

```bash
# optional
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

python src/score_example.py
```

No API key required for the example scorer.

---

## Relationship to other portfolio projects

- **Northstar Operational AI CoPilot** — shows how to *govern* what an AI system is allowed to do with operational data.  
- **Agent Development Lifecycle (ADL)** — shows a risk-gated lifecycle and deterministic trace evaluation for agents.  
- **This repo** — shows how to *evaluate* whether an industrial LLM answer is trustworthy enough to use.

Together they cover: **evaluate → govern → lifecycle**.

---

## Limitations

- Synthetic / illustrative cases only  
- Rubric and weights are starting points, not validated industry standards  
- LLM-as-judge is treated as a secondary signal, never the sole release gate  
- Not a certification or safety case  

---

## License

MIT License — see [LICENSE](LICENSE).
