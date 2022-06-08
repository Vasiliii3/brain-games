from math import gcd
import random


def generate_number() -> int:
    return int(random.randint(1, 50))
# генерация числа от 1 до 50


def play_gcd():
    number_one = generate_number()
    number_two = generate_number()
    question = " ".join(map(str, (number_one, number_two)))
    answer = gcd(number_one, number_two)
    return question, answer, int
