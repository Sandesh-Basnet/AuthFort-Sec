from security.entropy import caculate_entropy
pwd = input("Enter passcode:")
print("Entropy:",caculate_entropy(pwd),"bits")