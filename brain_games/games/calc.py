import random
import operator


c_operations = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul
                }


def generate_number() -> int:
    return int(random.randint(1, 50))
# генерация числа от 1 до 50


def play_calc():
    number_one = generate_number()
    number_two = generate_number()
    mathematical_operator = random.choice(list(c_operations.keys()))
    question = " ".join(map(str, (number_one, mathematical_operator,
                                  number_two)))
    answer = c_operations[mathematical_operator](number_one, number_two)
    return question, answer, int
