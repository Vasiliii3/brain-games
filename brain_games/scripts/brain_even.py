#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.even import play_even


def main():
    question = 'Answer "yes" if the number is even, ' \
               'otherwise answer "no".'
    gaming(play_even, question)


if __name__ == '__main__':
    main()
