import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.pattern_detector import detect_patterns


test_passwords = [
    "password",
    "123456",
    "aaaaaa",
    "P@ssword123",
    "securePass!9"
]

for pwd in test_passwords:
    issues = detect_patterns(pwd)

    print("Password:", pwd)

    if issues:
        print("Detected Issues:", issues)
    else:
        print("No obvious patterns")

    print("-" * 30)