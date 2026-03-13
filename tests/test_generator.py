import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.password_generator import generate_random_password
from core.password_generator import generate_passphrase


print("Random Password:")
print(generate_random_password())

print("\nPassphrase:")
print(generate_passphrase())