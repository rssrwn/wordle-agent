import random
from pathlib import Path


ANSWER_WORDS_PATH = "answer-words.txt"
VALID_WORDS_PATH = "valid-words.txt"


class InvalidWordError(Exception):
    """A submitted word is invalid."""
    
    def __init__(self, word):
        self.word = word
        self.super(f"{word} is not a valid word")


class WordleCore:
    """Core logic for the Wordle game.

    This class keeps track of a randomly selected answer and allows players to submit possible answers to be checked
    with feedback on the answer being returned.
    """

    def __init__(
        self,
        answer_words_path=ANSWER_WORDS_PATH,
        valid_words_path=VALID_WORDS_PATH
    ):
        self._answer_words = self._load_words(answer_words_path)
        self._valid_words = set(self._load_words(valid_words_path))

        self._selected_word = None
        self._num_attempts = None

    def start(self):
        """Initialise the game state."""

        selected_idx = random.randint(0, len(self._answer_words))
        self._selected_word = self._answer_words[selected_idx]
        self._num_attempts = 0

    def restart(self):
        """Re-initialise the game state."""

        self.start()

    def reset(self):
        """Reset the state of the class."""

        self._selected_word = None
        self._num_attempts = None

    def submit(self, answer):
        """Check a submitted answer.

        If the answer is not a valid word the InvalidWord exception will be thrown. Otherwise feedback on the answer
        is returned from this function as follows
        """

        # if answer not in self._valid_words:
        #     raise InvalidWordError(answer)

    def _load_words(words_path):
        words_str = Path(words_path).read_text()
        words = words_str.split("\n")
        return words
