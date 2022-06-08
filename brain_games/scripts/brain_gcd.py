#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.gcd import play_gcd


def main():
    question = 'Find the greatest common divisor ' \
               'of given numbers.'
    gaming(play_gcd, question)


if __name__ == '__main__':
    main()
