import random
import operator
from brain_games.games.logic import generate_number

c_operations = {"+": operator.add,
                "-": operator.sub,
                }

ELEMENTS_PROGRESSION = 10


def generate_progressions():
    mathematical_operator = random.choice(list(c_operations.keys()))
    number_start = generate_number(min_number=1, max_number=50)
    step = generate_number(min_number=1, max_number=5)
    a_progressions = [number_start, ]
    elements_replacement = generate_number(min_number=1,
                                           max_number=ELEMENTS_PROGRESSION)
    last_elements = number_start
    for x in range(1, ELEMENTS_PROGRESSION):
        new_elements = c_operations[mathematical_operator](last_elements, step)
        if x == elements_replacement:
            answer = last_elements = new_elements
            a_progressions.append("..")
            continue
        last_elements = new_elements
        a_progressions.append(new_elements)
    return a_progressions, answer


def play_prog():
    question, answer = generate_progressions()
    question = " ".join(map(str, question))
    return question, answer, int
