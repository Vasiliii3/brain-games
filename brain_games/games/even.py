import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_question_answer():
    number = random.randint(1, 50)
    answer = "yes" if is_even(number) else "no"
    return number, answer
