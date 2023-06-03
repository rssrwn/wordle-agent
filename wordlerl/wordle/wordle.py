from pathlib import Path


ANSWER_WORDS_PATH = "answer-words.txt"
VALID_WORDS_PATH = "valid-words.txt"


class WordleCore:
    def __init__(
        self,
        answer_words_path=ANSWER_WORDS_PATH,
        valid_words_path=VALID_WORDS_PATH
    ):
        self._answer_words = self._load_words(answer_words_path)
        self.valid_words = self._load_words(valid_words_path)

    def _load_words(words_path):
        words_str = Path(words_path).read_text()
        words = words_str.split("\n")
        return words

    def start(self):
        pass

    def restart(self):
        pass

    def submit(self, answer):
        pass
