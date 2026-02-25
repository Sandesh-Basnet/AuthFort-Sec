'''This is the main app to co-ordinate all the modules'''

from security.entropy import calculate_entropy
from security.crack_simulator import crack_time

GUESSES_PER_SECOND = 1e9   # 1 billion guesses/sec
pwd = input("Enter passcode:")
entropy = calculate_entropy(pwd)
result = crack_time(entropy,GUESSES_PER_SECOND)
print("\n=== AuthFort Report ===")
print("Entropy:", entropy, "bits")

if result["years"] >= 1:
    print("Estimated crack time:", round(result["years"], 2), "years")
elif result["days"] >= 1:
    print("Estimated crack time:", round(result["days"], 2), "days")
elif result["hours"] >= 1:
    print("Estimated crack time:", round(result["hours"], 2), "hours")
else:
    print("Estimated crack time:", round(result["seconds"], 2), "seconds")
