# AI Coding Benchmark

A lightweight benchmark framework for evaluating prompt strategies in AI-powered code repair tasks.

## Overview

AI Coding Benchmark measures how different prompting strategies affect the ability of large language models (LLMs) to repair buggy code and pass automated tests.

The framework automatically:

1. Creates isolated workspaces
2. Sends buggy code and task descriptions to an LLM
3. Applies generated fixes
4. Runs unit tests
5. Collects success rate and latency metrics
6. Compares multiple prompt variants

---

## Project Structure

```text
ai-bench/
│
├── runner.py
├── llm_agent.py
├── metrics.py
├── failure_analysis.py
├── config.py
├── tasks.json
├── requirements.txt
│
├── repos/
│   ├── repo_t1/
│   │   ├── target.py
│   │   └── test_target.py
│   ├── repo_t2/
│   ├── repo_t3/
│   ├── repo_t4/
│   ├── repo_t5/
│   └── repo_t6/
│
├── results/
└── workspaces/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-bench.git
cd ai-bench
```

Create a Python environment:

```bash
conda create -n aibench python=3.10 -y
conda activate aibench
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Edit `config.py` and add your API key:

```python
DEEPSEEK_API_KEY = "YOUR_API_KEY"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL_NAME = "deepseek-v4-pro"
```

---

## Run Benchmark

Execute:

```bash
python runner.py
```

Example terminal output:

```text
=== PIPELINE START ===

===== START EXPERIMENT A =====

=== RUN A t1 (easy) ===
=== RUN A t2 (easy) ===
=== RUN A t3 (medium) ===
=== RUN A t4 (medium) ===
=== RUN A t5 (hard) ===
=== RUN A t6 (hard) ===

===== START EXPERIMENT B =====

=== RUN B t1 (easy) ===
=== RUN B t2 (easy) ===
=== RUN B t3 (medium) ===
=== RUN B t4 (medium) ===
=== RUN B t5 (hard) ===
=== RUN B t6 (hard) ===

===== FINAL SUMMARY =====
...
```

---

## Output Files

Results are automatically generated under:

```text
results/
├── run_A.json
├── run_B.json
└── summary.json
```

Example:

```json
{
  "overall": {
    "A": {
      "success_rate": 0.83,
      "avg_latency": 120.3
    },
    "B": {
      "success_rate": 0.67,
      "avg_latency": 83.4
    }
  }
}
```

---

## Evaluation Metrics

### Success Rate

Percentage of tasks successfully repaired and verified by unit tests.

### Latency

Average runtime per task, including API generation and test execution.

### Difficulty Breakdown

Performance grouped by:

- Easy
- Medium
- Hard

### Delta Analysis

Identifies tasks where one prompt strategy outperforms another.

Example:

```json
{
  "B_better_tasks": [],
  "A_better_tasks": ["t4"],
  "tie_tasks": ["t1", "t2", "t3", "t5", "t6"]
}
```

---

## Experimental Design

The benchmark evaluates prompt engineering rather than model architecture.

Both experiments use the same underlying model and API settings.

### Prompt A

A concise debugging prompt focused on minimal reasoning and direct fixes.

### Prompt B

A more structured debugging prompt that explicitly encourages consideration of:

- Edge cases
- Logical correctness
- Side effects

The framework measures whether additional prompt guidance improves code repair performance.

---

## Research Question

Can prompt engineering improve code-repair performance when the underlying model remains unchanged?

This benchmark provides a reproducible framework for answering that question through automated experimentation.

---

## Dependencies

```text
requests>=2.31.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## License

MIT License