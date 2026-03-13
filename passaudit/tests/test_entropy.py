import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.entropy import calculate_entropy

print("password entropy:", calculate_entropy("password"))
print("P@ssw0rd123 entropy:", calculate_entropy("P@ssw0rd123"))