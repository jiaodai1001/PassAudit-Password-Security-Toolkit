import sys

from core.security_analyzer import analyze_password
from core.password_generator import generate_passphrase

def print_report(password, result):

    print("\nPassword Security Report")
    print("------------------------")

    print("Password:", password)
    print("Entropy:", result["entropy"])
    print("Strength:", result["strength"])

    if result["patterns"]:
        print("Patterns Detected:")
        for p in result["patterns"]:
            print("-", p)
    else:
        print("Patterns: None")

    if result["breach"]:
        print("Breach Database: FOUND")
    else:
        print("Breach Database: Not Found")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print(" python passaudit.py <password>")
        print(" python passaudit.py --generate")
        return

    if sys.argv[1] == "--generate":

        password = generate_passphrase()

        print("\nGenerated Password:")
        print(password)

        return

    password = sys.argv[1]

    result = analyze_password(password)

    print_report(password, result)


if __name__ == "__main__":
    main()