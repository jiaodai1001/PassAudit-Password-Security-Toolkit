import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.breach_checker import check_breach


passwords = [
    "password",
    "123456",
    "admin",
    "P@ssw0rd123",
    "securePassword!9"
]

for pwd in passwords:

    breached = check_breach(pwd)

    print("Password:", pwd)

    if breached:
        print("WARNING: password found in breach database")
    else:
        print("Password not found in breach database")

    print("-" * 30)