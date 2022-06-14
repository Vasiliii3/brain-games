import random
import operator

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul
              }


def generate_question_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    mathematical_operator = random.choice(list(OPERATIONS.keys()))
    question = " ".join(map(str, (number_one, mathematical_operator,
                                  number_two)))
    answer = OPERATIONS[mathematical_operator](number_one, number_two)
    return question, str(answer)
