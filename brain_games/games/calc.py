import random
import operator
from brain_games.games.logic import generate_number

c_operations = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul
                }


def play_calc():
    number_one = generate_number(min_number=1, max_number=100)
    number_two = generate_number(min_number=1, max_number=100)
    mathematical_operator = random.choice(list(c_operations.keys()))
    question = " ".join(map(str, (number_one, mathematical_operator,
                                  number_two)))
    answer = c_operations[mathematical_operator](number_one, number_two)
    return question, answer, int
