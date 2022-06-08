from brain_games.games.logic import generate_number


def is_even_number(number: int) -> bool:
    return number % 2 == 0


def play_even():
    number = generate_number(min_number=1, max_number=50)
    answer = "yes" if is_even_number(number) else "no"
    return number, answer, str
