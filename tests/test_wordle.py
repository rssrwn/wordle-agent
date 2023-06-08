import pytest

from wordlerl.wordle.core import WordleCore, InvalidWordError, OutOfAttemptsError


class TestWordleCore:
    def test_start_initialises_state(self):
        wordle = WordleCore()
        wordle.start()

        assert wordle._selected_word is not None
        assert wordle._num_attempts == 0

    def test_restart_initialises_state(self):
        wordle = WordleCore()
        wordle.restart()

        assert wordle._selected_word is not None
        assert wordle._num_attempts == 0

    def test_reset_resets_state(self):
        wordle = WordleCore()
        wordle.reset()

        assert wordle._selected_word is None
        assert wordle._num_attempts is None

    def test_submit_throws_invalid_word_when_word_wrong_length(self):
        wordle = WordleCore()
        wordle.start()

        with pytest.raises(InvalidWordError):
            wordle.submit("user")

        with pytest.raises(InvalidWordError):
            wordle.submit("humble")

    def test_submit_throws_outofattempts_when_too_many_attempts(self):
        wordle = WordleCore()
        wordle.start()

        max_attempts = 6

        for _ in range(max_attempts):
            wordle.submit("hello")

        with pytest.raises(OutOfAttemptsError):
            wordle.submit("hello")

    def test_submit_returns_correct_feedback_when_correct_or_incorrect(self):
        wordle = WordleCore()
        wordle.start()
        wordle._selected_word = "hello"

        guess = "paint"
        feedback = wordle.submit(guess)

        assert feedback[0] == "0"
        assert feedback[1] == "0"
        assert feedback[2] == "0"
        assert feedback[3] == "0"
        assert feedback[4] == "0"

        guess = "daily"
        feedback = wordle.submit(guess)

        assert feedback[0] == "0"
        assert feedback[1] == "0"
        assert feedback[2] == "0"
        assert feedback[3] == "1"
        assert feedback[4] == "0"

        guess = "hello"
        feedback = wordle.submit(guess)

        assert feedback[0] == "1"
        assert feedback[1] == "1"
        assert feedback[2] == "1"
        assert feedback[3] == "1"
        assert feedback[4] == "1"

    def test_submit_handles_2_feedback_correctly(self):
        wordle = WordleCore()
        wordle.start()
        wordle._selected_word = "paint"

        guess = "snare"
        feedback = wordle.submit(guess)

        assert feedback[0] == "0"
        assert feedback[1] == "2"
        assert feedback[2] == "2"
        assert feedback[3] == "0"
        assert feedback[4] == "0"

        guess = "pants"
        feedback = wordle.submit(guess)

        assert feedback[0] == "1"
        assert feedback[1] == "1"
        assert feedback[2] == "2"
        assert feedback[3] == "2"
        assert feedback[4] == "0"

        guess = "total"
        feedback = wordle.submit(guess)

        assert feedback[0] == "2"
        assert feedback[1] == "0"
        assert feedback[2] == "0"
        assert feedback[3] == "2"
        assert feedback[4] == "0"
