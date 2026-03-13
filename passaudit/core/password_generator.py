import random
import string


WORDS = [
    "river",
    "forest",
    "sun",
    "moon",
    "stone",
    "cloud",
    "tree",
    "ocean",
    "wind",
    "mountain",
    "shadow",
    "fire",
    "storm",
    "leaf",
    "bird"
]


def generate_random_password(length=12):
    """
    生成随机高强度密码
    """

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = "".join(random.choice(characters) for _ in range(length))

    return password


def generate_passphrase(num_words=4):
    """
    生成密码短语
    """

    selected_words = random.sample(WORDS, num_words)

    number = random.randint(10, 999)

    passphrase = "-".join(selected_words) + "-" + str(number)

    return passphrase