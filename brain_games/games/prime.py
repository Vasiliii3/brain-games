import math
import random

DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(number):
    start = 2
    if number == 2:
        return True
    even_number = 2 if number % 2 == 0 else 1
    while number % start != 0:
        if start > math.sqrt(number):
            return True
        start += even_number


def generate_question_answer():
    number = random.randint(1, 200)
    answer = "yes" if is_prime(number) else "no"
    return number, answer
