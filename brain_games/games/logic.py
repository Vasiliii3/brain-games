import prompt
import random

NUMBER_GAMES = 3


def generate_number(min_number: int, max_number: int) -> int:
    return int(random.randint(min_number, max_number))


def get_name_new_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}''!')
    return name


def convert(answer, required_type):
    if required_type == int:
        return int(answer)
    return answer


def gaming(func_game, question: str):
    user_name = get_name_new_user()
    print(question)
    for _ in range(NUMBER_GAMES):
        task, correct_answer, response_type = func_game()
        print(f'Question: {task}')
        user_answer = input("Your answer: ")
        if convert(user_answer, response_type) == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer "
                  f"was {correct_answer}.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
