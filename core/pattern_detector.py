COMMON_PASSWORDS = [
    "password",
    "admin",
    "123456",
    "qwerty",
    "abc123",
    "111111"
]


def detect_common_password(password: str):
    """
    检测是否为常见弱密码
    """
    if password.lower() in COMMON_PASSWORDS:
        return True
    return False


def detect_repeated_chars(password: str):
    """
    检测是否为重复字符
    例如 aaaaaa
    """
    return len(set(password)) == 1


def detect_number_sequence(password: str):
    """
    检测简单数字序列
    例如 123456 或 654321
    """
    sequences = ["123456", "654321", "12345", "54321"]

    for seq in sequences:
        if seq in password:
            return True

    return False


def detect_patterns(password: str):
    """
    综合检测
    """
    issues = []

    if detect_common_password(password):
        issues.append("common password")

    if detect_repeated_chars(password):
        issues.append("repeated characters")

    if detect_number_sequence(password):
        issues.append("number sequence")

    return issues