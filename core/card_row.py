from core.card import Card


class CardRow:
    def __init__(self, cards: list[Card]) -> None:
        self.word = "".join(card.value for card in cards)
        self.cards = cards

    def __str__(self) -> str:
        card_lines = [str(card).split("\n") for card in self.cards]
        transposed_lines = zip(*card_lines)
        return "\n".join(" ".join(line_group) for line_group in transposed_lines)
