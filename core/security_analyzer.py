from core.entropy import calculate_entropy
from core.pattern_detector import detect_patterns
from core.breach_checker import check_breach


def evaluate_strength(entropy):

    if entropy < 40:
        return "Weak"

    elif entropy < 60:
        return "Medium"

    else:
        return "Strong"


def analyze_password(password: str):

    result = {}

    # 1 熵值计算
    entropy = calculate_entropy(password)
    result["entropy"] = round(entropy, 2)

    # 2 强度等级
    result["strength"] = evaluate_strength(entropy)

    # 3 弱密码模式
    patterns = detect_patterns(password)
    result["patterns"] = patterns

    # 4 泄露数据库检测
    breach = check_breach(password)
    result["breach"] = breach

    return result