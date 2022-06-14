import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number_one, number_two):
    while number_two != 0:
        number_one, number_two = number_two, number_one % number_two
    return number_one


def generate_question_answer():
    number_one = random.randint(1, 50)
    number_two = random.randint(1, 50)
    question = " ".join(map(str, (number_one, number_two)))
    answer = gcd(number_one, number_two)
    return question, str(answer)
