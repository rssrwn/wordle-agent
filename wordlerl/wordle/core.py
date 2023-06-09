import random

import wordlerl.wordle.util as util


#******************************************************************************
#***************************** Exception classes ******************************
#******************************************************************************


class InvalidWordError(Exception):
    """A submitted word is invalid."""
    
    def __init__(self, word):
        self.word = word
        super().__init__(f"The guess must be a valid 5-letter word, got {word}")


class OutOfAttemptsError(Exception):
    """Run out of guessing attempts."""
    
    def __init__(self):
        super().__init__(f"Maximum number of attempts is {util.MAX_ATTEMPTS}")


#******************************************************************************
#******************************** Core class **********************************
#******************************************************************************


class WordleCore:
    """Core logic for the Wordle game.

    This class keeps track of a randomly selected answer and allows players to submit possible answers to be checked
    with feedback on the answer being returned.
    """

    def __init__(
        self,
        answer_words,
        valid_words
    ):
        self._answer_words = answer_words
        self._valid_words = valid_words

        self._selected_word = None
        self._num_attempts = None

    @property
    def word(self):
        return self._selected_word

    def start(self):
        """Initialise the game state."""

        selected_idx = random.randint(0, len(self._answer_words))
        self._selected_word = self._answer_words[selected_idx]
        self._num_attempts = 0

    def reset(self):
        """Reset the state of the class."""

        self._selected_word = None
        self._num_attempts = None

    def submit(self, guess):
        """Check a submitted guess.

        If the guess is not a valid word the InvalidWord exception will be thrown. Otherwise feedback on the guess word
        is returned from this function as follows:
        ...

        Args:
            guess (string): Guess word to be checked against the currently selected word

        Returns:
            (str): A feedback string as described above

        Raises:
            OutOfAttemptsError: The user attempts to make more attempts than the max allowed
            InvalidWordError: The supplied guess is not in the list of valid words
        """

        if self._num_attempts == util.MAX_ATTEMPTS:
            raise OutOfAttemptsError()

        if type(guess) is not str:
            raise TypeError(f"guess must be a string, got {type(guess)}")

        if len(guess) != 5 or guess not in self._valid_words:
            raise InvalidWordError(guess)

        # Setup a count of each letter in the selected word
        word_letter_count = {}
        for letter in self._selected_word:
            if letter not in word_letter_count:
                word_letter_count[letter] = 1

            else:
                word_letter_count[letter] += 1

        guess_letter_count = {}
        feedback = ""

        for idx in range(len(guess)):
            guess_letter = guess[idx]
            actual_letter = self._selected_word[idx]

            # Increment count of this letter for the guess word
            if guess_letter not in guess_letter_count:
                guess_letter_count[guess_letter] = 1
            else:
                guess_letter_count[guess_letter] += 1

            # Correctly guessed letter
            if guess_letter == actual_letter:
                feedback += "1"

            # Guess letter is wrong and does not appear in word
            elif guess_letter not in self._selected_word:
                feedback += "0"

            # Guess letter is wrong but does appear in word. Here we need to check how many instances of this letter
            # appear in the word and how many we have already visited in the guess. If a letter appear more times in a
            # guess than in the word then excess instances of the letter will be marked as wrong in a left-to-right
            # ordering
            else:
                occurence_in_selected = word_letter_count[guess_letter]
                curr_guess_occurences = guess_letter_count.get(guess_letter, 0)

                if curr_guess_occurences > occurence_in_selected:
                    feedback += "0"

                else:
                    feedback += "2"

        self._num_attempts += 1

        return feedback
