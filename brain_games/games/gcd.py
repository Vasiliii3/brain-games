from math import gcd
from brain_games.games.logic import generate_number


def play_gcd():
    number_one = generate_number(min_number=1, max_number=50)
    number_two = generate_number(min_number=1, max_number=50)
    question = " ".join(map(str, (number_one, number_two)))
    answer = gcd(number_one, number_two)
    return question, answer, int
