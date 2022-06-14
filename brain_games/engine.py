import prompt

ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}''!')
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        task, correct_answer = game.generate_question_answer()
        print(f'Question: {task}')
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer "
                  f"was {correct_answer}.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
