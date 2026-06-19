# Multi-Modal Evidence Review System
...
# 🚀 HackerRank Orchestrate – June 2026

## Multi-Modal Evidence Review System

A 24‑hour hackathon submission that verifies damage claims for cars, laptops, and packages.  
The system reads user conversations, inspects submitted images (via pluggable VLM), checks user history, and produces a structured verdict with severity, risk flags, and supporting evidence.

---

## 🎯 Problem Statement

Build an agent‑based system that, for each claim:
- Extracts the actual damage claim from a short conversation.
- Inspects one or more submitted images.
- Decides whether the images support, contradict, or lack evidence for the claim.
- Identifies the visible issue type, object part, severity, and risk flags.
- Outputs a strict CSV with all required fields.

[Full problem statement](https://github.com/interviewstreet/hackerrank-orchestrate-june26/blob/main/problem_statement.md)

---

## 🧠 Approach

1. **Rule‑based NLP pipeline** – Extracts damage keywords and part names from conversations. Provides instant triage without API costs.
2. **Pluggable Vision‑Language Model interface** – Architecture ready to swap in GPT‑4o or Claude for real image analysis.
3. **Risk detection** – Flags social engineering attempts (`text_instruction_present`) and escalation threats.
4. **Modular design** – Clean separation between main runner, heuristic logic, evaluation, and future VLM integration.

---

## 📁 Project Structure

code/
├── main.py # Entry point – reads claims.csv, writes output.csv
├── heuristic_pipeline.py # Keyword‑based claim extraction and verification
├── evaluation/
│ └── main.py # Evaluation framework (stub for future metrics)
└── README.md

dataset/
├── claims.csv # Input claims (test set)
├── sample_claims.csv # Development set with expected outputs
├── user_history.csv # User claim history
├── evidence_requirements.csv # Minimum image evidence rules
└── images/
├── sample/ # Images for sample claims
└── test/ # Images for test claims

output.csv # Final predictions (submitted)
code.zip # Zipped solution for HackerRank
log.txt # AI chat transcript


---

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/mehtarachit/hackerrank-orchestrate-june26.git
cd hackerrank-orchestrate-june26

# 2. Ensure dataset/ folder is present (with claims.csv, images/, etc.)
# 3. Install dependencies
pip install pillow pandas

# 4. Run the pipeline
python code/main.py

# output.csv will be generated.

Evaluation
The evaluation module (evaluation/main.py) is stubbed. For a full evaluation:

Run the pipeline on sample_claims.csv.

Compare predictions with expected values.

Measure accuracy, precision/recall per field, cost, and latency.

Compare at least two strategies (e.g., rule‑based vs. VLM).

ubmission
Submitted to the HackerRank Orchestrate hackathon on June 19, 2026.
This repository contains the complete submission: output.csv, code.zip, and the AI chat transcript.

Author
Rachit Mehta
LinkedIn | GitHub
