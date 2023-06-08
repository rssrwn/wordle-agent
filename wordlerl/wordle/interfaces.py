from abc import ABC

from wordlerl.wordle.core import WordleCore


class WordleInterface(ABC):
    def __init__(self):
        self._engine = WordleCore()


class TerminalInterface(WordleInterface):
    def __init__(self):
        super().__init__()

    def start_game(self):
        self._engine.start()

        print()


class RLInterface(WordleInterface):
    def __init__(self):
        super().__init__()
