# Strength Classifier

## Purpose

The Strength Classifier evaluates how secure a password is by combining:

- Practical attack feasibility (crack time)
- Theoretical randomness (entropy)

It converts numerical results into a human-readable security judgement.

---

## Classification Layers

### Layer 1 — Base Strength from Crack Time

Crack time represents how long an attacker would need to break the password.

This reflects **real-world attack feasibility**.

Decision thresholds:

- < 1 second → UNACCEPTABLY WEAK
- < 1 minute → VERY WEAK
- < 1 hour → WEAK
- < 1 day → MODERATE
- < 1 year → STRONG
- ≥ 1 year → VERY STRONG

This produces the initial strength estimate.

---

### Layer 2 — Entropy Cap (Security Validation)

Entropy represents the theoretical randomness of the password.

Low entropy means predictable structure, even if crack-time estimation appears high.

Therefore entropy defines a **maximum allowed strength**.

Entropy thresholds:

- < 28 bits → VERY WEAK
- < 36 bits → WEAK
- < 60 bits → MODERATE
- < 128 bits → STRONG
- ≥ 128 bits → VERY STRONG

This prevents overestimating password security.

---

## Final Strength Decision

The final strength is determined by selecting the weaker result between:

- Base strength (from crack time)
- Entropy cap (maximum allowed strength)

### Formula

> **final_strength = min(base_strength, entropy_cap)**

This ensures:

- Practical attack feasibility is respected
- Structural password weakness is not ignored

---

## Ranking System

Strength levels are internally represented using numeric ranks for comparison:

| Rank | Strength |
|------|---------|
| 0 | UNACCEPTABLY WEAK |
| 1 | VERY WEAK |
| 2 | WEAK |
| 3 | MODERATE |
| 4 | STRONG |
| 5 | VERY STRONG |

Lower rank = weaker password.

---

## Design Principles

- Crack time determines real-world resistance.
- Entropy prevents false confidence.
- The weakest indicator defines final security.
- Classification is deterministic and rule-based.
- No machine learning required.

---

## Module Input

- Entropy value (bits)
- Crack-time result dictionary

## Module Output

- Final password strength label