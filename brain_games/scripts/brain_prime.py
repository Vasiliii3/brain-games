#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.prime import play_prime


def main():
    question = 'Answer "yes" if the number is prime, ' \
               'otherwise answer "no".'
    gaming(play_prime, question)


if __name__ == '__main__':
    main()
