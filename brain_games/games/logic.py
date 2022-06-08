import prompt

NUMBER_GAMES = 2


def get_name_new_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}''!')
    return name


def gaming(func_check, func_question, question: str):
    user_name = get_name_new_user()
    print(question)
    for _ in range(NUMBER_GAMES + 1):
        number = func_question()
        print(f'Question: {number}')
        user_answer = input("Your answer: ")
        correct_answer = func_check(number)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")