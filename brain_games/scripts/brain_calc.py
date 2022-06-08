#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.calc import play_calc


def main():
    question = 'What is the result of the expression?'
    gaming(play_calc, question)


if __name__ == '__main__':
    main()
