import random
from string import ascii_lowercase, digits


def generate_slug(len=8):
    """
    Generates a random slug of a given length.
    """
    return ''.join(random.choice(ascii_lowercase + digits) for _ in range(len))
