import pytest

from core.board import Board
from core.card_row import CardRow
from core.game import Game, GameStatus


@pytest.fixture(name="game")
def fixture_simple_game() -> Game:
    board = Board([CardRow([]) for _ in range(6)])
    return Game(6, "HELLO", ["HELLO", "WORLD"], board)


def test_game_initialization(game: Game):
    assert game.guesses_allowed == 6
    assert game.word == "HELLO"
    assert game.words == ["HELLO", "WORLD"]
    assert game.status == GameStatus.IN_PROGRESS
    assert game.current_guess == 1
    assert not game.previous_guesses


def test_check_guess_invalid_length(game: Game):
    guess_valid = game.check_guess("HE")
    assert not guess_valid
    assert game.status == GameStatus.IN_PROGRESS


def test_check_guess_not_in_words(game: Game):
    guess_valid = game.check_guess("APPLE")
    assert not guess_valid
    assert game.status == GameStatus.IN_PROGRESS


def test_check_guess_valid(game: Game):
    guess_valid = game.check_guess("HELLO")
    assert guess_valid
    assert game.status == GameStatus.WIN


def test_check_guess_not_alpha(game: Game):
    guess_valid = game.check_guess("H3LLO")
    assert not guess_valid


def test_check_guess_repeated(game: Game):
    guess_valid = game.check_guess("HELLO")
    assert guess_valid

    repeated_guess_valid = game.check_guess("HELLO")
    assert not repeated_guess_valid


def test_check_guess_loss():
    board = Board([CardRow([]) for _ in range(1)])  # Simulate a single guess allowed
    game = Game(1, "HELLO", ["HELLO", "WORLD"], board)

    game.check_guess("WORLD")
    assert game.status == GameStatus.LOSS
