'''
This module provides advice based on password strength. It categorizes passwords into different
strength levels and generates tailored feedback to help users improve their password security.'''
import random
import string

HARSH = {
    "length": [
        "Bold strategy using a password shorter than a sneeze.",
        "Security level: decorative.",
        "Your password finished before the attacker even started."
    ],
    "upper": [
        "Uppercase letters are not illegal. You can use them.",
        "Shift key exists. It’s not just for decoration."
    ],
    "lower": [
        "WHY ARE WE SHOUTING.",
        "Passwords don’t need to scream to be heard."
    ],
    "digit": [
        "Numbers help. Even hackers can count.",
        "Math exists. Your password disagrees."
    ],
    "symbol": [
        "Symbols exist. So does security.",
        "Try @, #, $, or literally anything interesting."
    ]
}

NEUTRAL = {
    "length": ["Increase password length for better security."],
    "upper": ["Add uppercase letters to strengthen the password."],
    "lower": ["Add lowercase letters for better balance."],
    "digit": ["Include numbers to increase complexity."],
    "symbol": ["Add special characters to improve strength."]
}

POSITIVE = [
    "Now that’s a password with self-respect.",
    "Hackers just sighed collectively.",
    "Security approved. Carry on."
]

def detect_problems(password):
    '''Detects specific weaknesses in the password and returns a list of problems.'''
    problems = []

    if len(password) < 8:
        problems.append("length")
    if not any(c.isupper() for c in password):
        problems.append("upper")
    if not any(c.islower() for c in password):
        problems.append("lower")
    if not any(c.isdigit() for c in password):
        problems.append("digit")
    if not any(c in string.punctuation for c in password):
        problems.append("symbol")

    return problems


def generate_advice(password, strength):
    '''Generates advice based on the password's strength and detected problems.'''
    problems = detect_problems(password)

    if strength in ["UNACCEPTABLY WEAK", "VERY WEAK"]:
        message_bank = HARSH
    elif strength in ["WEAK", "MODERATE"]:
        message_bank = NEUTRAL
    else:
        return [random.choice(POSITIVE)]

    advice = []
    for problem in problems:
        if problem in message_bank:
            advice.append(random.choice(message_bank[problem]))

    return advice
