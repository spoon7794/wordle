from enum import Enum, auto


class CardStatus(Enum):
    NORMAL = auto()
    IN_WORD_WRONG_SPOT = auto()
    IN_WORD_CORRECT_SPOT = auto()


class Card:
    def __init__(
        self,
        letter: str = "",
        visible: bool = False,
        status: CardStatus = CardStatus.NORMAL,
    ) -> None:

        if len(letter) > 1:
            raise ValueError("char must be a single character or blank.")

        self.value = letter
        self.visible = visible
        self.status = status

    def __str__(self) -> str:
        if not self.visible or self.value == "":
            return " "
        return self.value
