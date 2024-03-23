from core import factory
from core.board import Board
from core.card_row import CardRow


def test_board_initialization():
    rows = [CardRow([]) for _ in range(5)]
    board = Board(rows=rows)
    assert board.rows == rows, "Board should initialize with the provided rows."


def test_board_update():
    initial_rows = [CardRow([]) for _ in range(3)]
    board = Board(rows=initial_rows)

    # Create a new CardRow to update the board with
    new_row = factory.create_card_row_from_word("new")
    row_to_update = 2  # Remember, row numbering for humans starts from 1

    board.update(row_num=row_to_update, card_row=new_row)

    assert (
        board.rows[row_to_update - 1] == new_row
    ), "Board should have updated the specified row with the new CardRow."
    assert len(board.rows) == 3, "Board should still have the same number of rows."
    for i, row in enumerate(board.rows):
        if i != row_to_update - 1:
            assert row == initial_rows[i], "Other rows should remain unchanged."
