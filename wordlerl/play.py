from argparse import ArgumentParser

from wordlerl.wordle.core import WordleCore, InvalidWordError


MAX_ATTEMPTS = 6
ANSWER_WORDS_PATH = "resources/answer-words.txt"
VALID_WORDS_PATH = "resources/valid-words.txt"


def format_feedback(feedback, guess):
    formatted = ""
    for feedback_num, guess_letter in zip(feedback, guess):
        if feedback_num == "0":
            formatted += "_"
        elif feedback_num == "1":
            formatted += guess_letter
        else:
            formatted += "~"

    return formatted


def play_one_round(engine):
    engine.start()

    for i in range(MAX_ATTEMPTS):
        feedback = None
        valid_guess = False
        guess = input(f"Round {i+1} --- Please guess a word: ")

        # Keep guessing until we have a valid word
        while not valid_guess:
            try:
                feedback = engine.submit(guess)
                valid_guess = True

            except InvalidWordError:
                guess = input(f"{guess} is invalid. Please try again: ")

        formatted = format_feedback(feedback, guess)

        print(f"*** Round {i+1} ***")
        print(f"Your guess: {guess}")
        print(f"Outcome:    {formatted}")
        print()


def play(engine):
    play_again = True

    while play_again:
        play_one_round(engine)

        answer = None
        while answer is None:
            answer_str = input("Would you like to play again? [y/n] ")
            if answer_str == "y":
                answer = True
            elif answer_str == "n":
                answer = False

        play_again = answer


def main(args):
    print("Welcome to Wordle!")

    engine = WordleCore(
        answer_words_path=args.answer_words_path,
        valid_words_path=args.valid_words_path
    )
    play(engine)


if __name__ == "__main__":
    parser = ArgumentParser(prog="WordleGame", description="Play the Wordle game with Python")

    parser.add_argument("--answer_words_path", default=ANSWER_WORDS_PATH)
    parser.add_argument("--valid_words_path", default=VALID_WORDS_PATH)

    args = parser.parse_args()
    main(args)
