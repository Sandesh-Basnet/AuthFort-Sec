# AuthFort-AI – Security Module

> A modular cybersecurity password analysis tool that delivers complete password strength assessments through mathematical analysis, attack simulation, human behavior insights, and actionable advice.

---

## 🔗 Project Modules

The project is structured into separate, well-defined modules. Each module has its own documentation file in the `docs/` folder:

| Module | Responsibility | Documentation |
|--------|----------------|---------------|
| **Entropy Calculator** | Measures randomness of the password and calculates entropy in bits. | [docs_for_entropy.md](docs/docs_for_entropy.md) |
| **Crack Simulator** | Estimates password crack time based on entropy and attacker speed. | [docs_for_crack_simulator.md](docs/docs_for_crack_simulator.md) |
| **Strength Classifier** | Assigns human-readable strength labels (`UNACCEPTABLY WEAK` → `VERY STRONG`) using entropy and crack time. | [docs_for_strength_classifier.md](docs/docs_for_strength_classifier.md) |
| **Password Advisor** | Provides actionable, tone-adjusted advice for improving passwords. | [docs_for_password_advisor.md](docs/docs_for_password_advisor.md) |
| **Main App** | Orchestrates all modules and prints a consolidated report for the user. | [docs_for_app.md](docs/docs_for_app.md) |

---

## 🧭 Module Flow

The password evaluation pipeline runs as follows:

```text
password input
      ↓
entropy.py            →  entropy_bits
      ↓
crack_simulator.py    →  crack_time_dict
      ↓
strength_classifier.py  →  strength_label
      ↓
password_advisor.py   →  advice_list
      ↓
print final report (entropy, crack time, strength, advice)
```

---

## 🔒 Features

- **Entropy Calculation** – Measures the unpredictability of a password.
- **Crack-Time Estimation** – Simulates offline brute-force attack scenarios.
- **Strength Classification** – Converts quantitative analysis into intuitive labels.
- **Advice Generation** – Gives actionable tips with adjustable tone based on password strength.
- **Extensible Architecture** – Designed for adding pattern detection, dictionary checks, or ML models later.

---

## 📁 Docs Folder

All modules have detailed documentation:

```
docs/
├── docs_for_entropy.md
├── docs_for_crack_simulator.md
├── docs_for_strength_classifier.md
├── docs_for_password_advisor.md
└── docs_for_app.md
```

Each file contains:

- Purpose of the module
- Input / Output specification
- Functional flow
- Formulas or rules used
- Integration with other modules

---

## 🚀 How to Run

**1. Clone the repository:**

```bash
git clone <repo_url>
```

**2. Navigate to the source directory:**

```bash
cd AuthFort-Sec/src
```

**3. Run the app:**

```bash
python app.py
```

Enter your password and receive:

- Entropy value
- Estimated crack time
- Strength label
- Security advice

---

## 📌 Design Philosophy

| Principle | Description |
|-----------|-------------|
| **Single Responsibility** | Each module handles one aspect of analysis. |
| **Human + Machine Friendly** | Combines mathematical rigor with actionable advice. |
| **Extensible** | New security checks or ML features can be added without rewriting existing code. |

---

## ⚡ Next Steps / Enhancements

- [ ] Pattern detection (dictionary words, sequences, repeated chars, keyboard patterns)
- [ ] Web or GUI interface
- [ ] ML-based password scoring
- [ ] Multi-language support

---

> **AuthFort-AI** is a practical and modular toolkit for cybersecurity students, developers, and enthusiasts who want to understand and improve password security.