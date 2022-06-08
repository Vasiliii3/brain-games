import math
from brain_games.games.logic import generate_number


def is_number_prime(number):
    start = 2
    if number == 2:
        return True
    even_number = 2 if number % 2 == 0 else 1
    while number % start != 0:
        if start > math.sqrt(number):
            return True
        start += even_number


def play_prime():
    number = generate_number(min_number=1, max_number=200)
    answer = "yes" if is_number_prime(number) else "no"
    return number, answer, str
