from abc import ABC
from pathlib import Path

import wordlerl.wordle.util as util
from wordlerl.wordle.core import WordleCore, InvalidWordError


class WordleInterface(ABC):
    def __init__(self, answer_words_path, valid_words_path):
        answer_words = self._load_words(answer_words_path)
        valid_words = self._load_words(valid_words_path)

        self._engine = WordleCore(answer_words, valid_words)

    def _load_words(self, words_path):
        words_str = Path(words_path).read_text()
        words = words_str.split("\n")
        return words


class TerminalInterface(WordleInterface):
    def __init__(self, answer_words_path, valid_words_path):
        super().__init__(answer_words_path, valid_words_path)

    def play(self):
        try:
            self._play()
        except KeyboardInterrupt:
            print("\nThanks for playing! Goodbye.")

    def play_one_game(self):
        try:
            self._play_one_game()
        except KeyboardInterrupt:
            print("\nThanks for playing! Goodbye.")

    def _play(self):
        play_again = True

        while play_again:
            self._play_one_game()

            answer = None
            while answer is None:
                answer_str = input("Would you like to play again? [y/n] ")
                if answer_str == "y":
                    answer = True
                elif answer_str == "n":
                    answer = False

            play_again = answer

    def _play_one_game(self):
        self._engine.start()

        for i in range(util.MAX_ATTEMPTS):
            feedback = None
            valid_guess = False

            if i+1 == util.MAX_ATTEMPTS:
                print("Final round!")

            guess = input(f"Round {i+1} --- Please guess a word: ")

            # Keep guessing until we have a valid word
            while not valid_guess:
                try:
                    feedback = self._engine.submit(guess)
                    valid_guess = True

                except InvalidWordError:
                    guess = input(f"{guess} is invalid. Please try again: ")

            formatted = self._format_feedback(feedback, guess)

            print(f"*** Round {i+1} ***")
            print(f"Your guess: {guess}")
            print(f"Outcome:    {formatted}")
            print()

            # If the user wins print a message and leave the loop
            if feedback == "11111":
                print(f"Congratulations! You won after {i+1} rounds.")
                print()
                break

            # If user doesn't win after all rounds are complete
            if i+1 == util.MAX_ATTEMPTS:
                print(f"All rounds are now complete. The correct word was {self._engine.word}")
                print()

    def _format_feedback(self, feedback, guess):
        formatted = ""
        for feedback_num, guess_letter in zip(feedback, guess):
            if feedback_num == "0":
                formatted += "_"
            elif feedback_num == "1":
                formatted += guess_letter
            else:
                formatted += "~"

        return formatted


class RLInterface(WordleInterface):
    def __init__(self):
        super().__init__()
