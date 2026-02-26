# Password Advisor Module

## Overview
The Password Advisor module analyzes a password’s structure and provides
security recommendations based on detected weaknesses and the final
strength classification.

This module transforms raw security analysis into practical guidance
for improving password robustness.

---

## Purpose
A password may be weak due to structural issues such as:

- Insufficient length
- Missing character diversity
- Predictable composition
- Low resistance to brute-force attacks

The advisor identifies these issues and provides recommendations
appropriate to the password’s security level.

---

## Inputs

The module requires:

1. Password string
2. Strength classification label

---

## Output

The module returns a list of security recommendations.

If the password is sufficiently strong, the module returns positive
reinforcement instead of corrective advice.

---

## Detection Rules

### 1. Length Requirement
Password should be at least 8 characters long.

### 2. Character Diversity
The module checks for presence of:

- Uppercase letters
- Lowercase letters
- Digits
- Special characters

Each missing category is treated as a structural weakness.

---

## Advice Tone Strategy

Advice severity depends on the final strength classification.

| Strength Level | Advice Behavior |
|---------------|----------------|
| UNACCEPTABLY WEAK | Harsh corrective feedback |
| VERY WEAK | Strong warnings |
| WEAK | Direct improvement suggestions |
| MODERATE | Constructive guidance |
| STRONG | Light recommendations |
| VERY STRONG | Positive reinforcement only |

This ensures feedback reflects real security risk.

---

## Functional Flow

Password  
→ Detect structural weaknesses  
→ Receive strength classification  
→ Select advice tone  
→ Generate recommendations  
→ Return advice list  

---

## Module Functions

### detect_problems(password)

Identifies structural weaknesses in a password.

Returns a list of problem identifiers:
- length
- upper
- lower
- digit
- symbol

---

### generate_advice(password, strength)

Main function of the module.

Responsibilities:
- Detect password weaknesses
- Adjust advice tone using strength level
- Generate improvement recommendations
- Return advice list

---

## Integration in System Pipeline

Password Input  
→ Entropy Calculation  
→ Crack Time Simulation  
→ Strength Classification  
→ Password Advisor  
→ Final Security Report  

---

## Design Philosophy

The Password Advisor follows three principles:

1. Explain weaknesses clearly
2. Provide actionable improvements
3. Match feedback severity to risk level

The module focuses on guidance rather than judgment,
helping users move toward stronger authentication practices.