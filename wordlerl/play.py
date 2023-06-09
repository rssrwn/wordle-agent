from argparse import ArgumentParser

from wordlerl.wordle.interfaces import TerminalInterface


ANSWER_WORDS_PATH = "resources/answer-words.txt"
VALID_WORDS_PATH = "resources/valid-words.txt"


def main(args):
    print("Welcome to Wordle!")

    wordle = TerminalInterface(
        args.answer_words_path,
        args.valid_words_path
    )
    wordle.play()


if __name__ == "__main__":
    parser = ArgumentParser(prog="WordleGame", description="Play the Wordle game with Python")

    parser.add_argument("--answer_words_path", default=ANSWER_WORDS_PATH)
    parser.add_argument("--valid_words_path", default=VALID_WORDS_PATH)

    args = parser.parse_args()
    main(args)
