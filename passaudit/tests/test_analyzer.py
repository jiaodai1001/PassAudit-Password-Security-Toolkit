import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.security_analyzer import analyze_password


passwords = [
    "123456",
    "password",
    "aaaaaa",
    "P@ssw0rd123",
    "MySecurePass!2025"
]

for pwd in passwords:

    result = analyze_password(pwd)

    print("Password:", pwd)
    print("Entropy:", result["entropy"])
    print("Strength:", result["strength"])

    if result["patterns"]:
        print("Patterns:", result["patterns"])
    else:
        print("Patterns: None")

    if result["breach"]:
        print("Breach: FOUND in database")
    else:
        print("Breach: Not Found")

    print("-" * 40)