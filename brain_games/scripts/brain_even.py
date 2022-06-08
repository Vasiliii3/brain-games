#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.even import even_number, generate_number


def main():
    question = 'Answer "yes" if the number is even, ' \
               'otherwise answer "no".'
    gaming(even_number, generate_number, question)


if __name__ == '__main__':
    main()
