import re

email = input("What's your email? ").strip()

if re.search(r"^[a-z09_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


