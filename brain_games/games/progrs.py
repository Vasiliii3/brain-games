import random

ELEMENTS_PROGRESSION = 10
DESCRIPTION = 'What number is missing in the progression?'


def generate_progressions():
    number_start = random.randint(1, 50)
    step = random.randint(-10, 10)
    a_progressions = []
    elements_replacement = random.randint(0, ELEMENTS_PROGRESSION - 1)
    last_elements = number_start
    for x in range(ELEMENTS_PROGRESSION):
        new_elements = last_elements + step
        last_elements = new_elements
        a_progressions.append(new_elements)
    return a_progressions, elements_replacement


# корректировка т.к длина длина списка начинается с 0

def generate_question_answer():
    progression, element = generate_progressions()
    answer = progression.pop(element)
    progression.insert(element, "..")
    question = " ".join(map(str, progression))
    return question, str(answer)
