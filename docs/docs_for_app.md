# Main App Module (`app.py`)

## Overview
`app.py` coordinates all AuthFort-AI security modules to analyze a password and provide a full report including:

- Entropy  
- Crack time estimate  
- Strength classification  
- Security advice  

---

## Flow
1. Input password  
2. Calculate entropy (`calculate_entropy`)  
3. Simulate crack time (`crack_time`)  
4. Classify strength (`classify_strength`)  
5. Generate advice (`generate_advice`)  
6. Print report  

---

## Key Variables
| Variable | Description |
|----------|-------------|
| `GUESSES_PER_SECOND` | Attacker speed for crack simulation |
| `pwd` | User-entered password |
| `entropy` | Calculated entropy |
| `time_req` | Crack time dictionary |
| `PW_STRENGTH` | Strength label |
| `advice_list` | List of advice messages |

---

## Notes
- Requires all modules in the `security/` package  
- Advice tone adapts to strength level  
- Fully modular, easy to extend with pattern detection or ML scoring  