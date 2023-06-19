import random
from string import ascii_lowercase, digits


def generate_slug(length: int = 8) -> str:
    """Generate a random slug of the given length."""
    return "".join(
        random.choice(ascii_lowercase + digits) for _ in range(length)
    )
