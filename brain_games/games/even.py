import random


def even_number(number: int) -> bool:
    return number % 2 == 0


def generate_number() -> int:
    return int(random.randint(1, 100))


def play_even():
    number = generate_number()
    answer = "yes" if even_number(number) else "no"
    return number, answer, str
