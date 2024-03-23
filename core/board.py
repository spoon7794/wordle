from core.card_row import CardRow


class Board:
    def __init__(self, rows: list[CardRow]) -> None:
        self.rows = rows

    def update(self, row_num: int, card_row: CardRow) -> None:
        self.rows[row_num - 1] = card_row
