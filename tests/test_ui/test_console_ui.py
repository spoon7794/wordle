from pytest import CaptureFixture

from core.board import Board
from core.card import Card, CardStatus
from core.card_row import CardRow
from ui.console_ui import (
    print_board,
    print_card,
    print_invalid_input,
    print_loss,
    print_win,
)


def test_print_card(capsys: CaptureFixture[str]):
    card = Card("A", visible=True, status=CardStatus.IN_WORD_CORRECT_SPOT)
    print_card(card)
    captured = capsys.readouterr()
    assert "A" in captured.out
    assert (
        "\u250c\u2500\u2500\u2500\u2510" in captured.out
    )  # Part of the card's top border


def test_print_board(capsys: CaptureFixture[str]):
    board = Board(
        [
            CardRow([Card("A", visible=True, status=CardStatus.NORMAL)]),
            CardRow([Card("B", visible=True, status=CardStatus.IN_WORD_WRONG_SPOT)]),
        ]
    )
    print_board(board)
    captured = capsys.readouterr()
    assert "WORDLE" in captured.out
    assert "A" in captured.out
    assert "B" in captured.out


def test_print_win(capsys: CaptureFixture[str]):
    print_win("APPLE")
    captured = capsys.readouterr()
    assert "You win!" in captured.out
    assert "APPLE" in captured.out


def test_print_loss(capsys: CaptureFixture[str]):
    print_loss("APPLE")
    captured = capsys.readouterr()
    assert "Better luck next time!" in captured.out
    assert "APPLE" in captured.out


def test_print_invalid_input(capsys: CaptureFixture[str]):
    print_invalid_input()
    captured = capsys.readouterr()
    assert "Invalid input detected." in captured.out
