#!/usr/bin/env python
from brain_games.games.logic import gaming
from brain_games.games.progrs import play_prog


def main():
    question = 'What number is missing in the progression?'
    gaming(play_prog, question)


if __name__ == '__main__':
    main()
