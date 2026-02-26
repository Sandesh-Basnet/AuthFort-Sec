'''This is the main app to co-ordinate all the modules'''

from security.entropy import calculate_entropy
from security.crack_simulator import crack_time
from security.strength_classifier import classify_strength
from security.password_adivisor import generate_advice

GUESSES_PER_SECOND = 1e9   # 1 billion guesses/sec
pwd = input("Enter passcode:")
entropy = calculate_entropy(pwd)
time_req = crack_time(entropy,GUESSES_PER_SECOND)
print("\n=== AuthFort Report ===")
print("Entropy:", entropy, "bits")
if time_req["years"] >= 1:
    print("Estimated crack time:", round(time_req["years"], 2), "years")
elif time_req["days"] >= 1:
    print("Estimated crack time:", round(time_req["days"], 2), "days")
elif time_req["hours"] >= 1:
    print("Estimated crack time:", round(time_req["hours"], 2), "hours")
else:
    print("Estimated crack time:", round(time_req["seconds"], 2), "seconds")
PW_STRENGTH = classify_strength(entropy,time_req)
print("Passcode Strength:",PW_STRENGTH)
advice_list = generate_advice(pwd, PW_STRENGTH)
print("\nSecurity Advice:")
for advice in advice_list:
    print("-", advice)
