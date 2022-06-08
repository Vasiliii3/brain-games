from brain_games.games.logic import generate_number


def even_number(number: int) -> bool:
    return number % 2 == 0


def play_even():
    number = generate_number(min_number=1, max_number=50)
    answer = "yes" if even_number(number) else "no"
    return number, answer, str
