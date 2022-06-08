import random


def even_number(number: int) -> str:
    return "yes" if number % 2 == 0 else "no"


def generate_number() -> int:
    return int(random.randint(1, 100))
