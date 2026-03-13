import hashlib
import os


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "datasets",
    "common_password_hash.txt"
)


def load_hash_database():
    """
    读取弱密码hash数据库
    """
    hashes = set()

    if not os.path.exists(DATA_FILE):
        return hashes

    with open(DATA_FILE, "r") as f:
        for line in f:
            hashes.add(line.strip())

    return hashes


def hash_password(password: str):
    """
    计算密码SHA256
    """
    return hashlib.sha256(password.encode()).hexdigest()


def check_breach(password: str):
    """
    检查密码是否出现在泄露数据库
    """
    db = load_hash_database()

    password_hash = hash_password(password)

    if password_hash in db:
        return True

    return False