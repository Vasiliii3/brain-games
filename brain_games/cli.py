import prompt


def name_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
