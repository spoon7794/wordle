from core.card import Card
from core.card_row import CardRow


def test_card_row_init_with_cards():
    cards = [
        Card("", visible=True),
        Card("P", visible=True),
        Card("E", visible=False),
    ]

    card_row = CardRow(cards)

    expected_word = "PE"
    actual_word = card_row.word

    expected_str = "  P  "
    actual_str = str(card_row)

    assert actual_word == expected_word
    assert actual_str == expected_str


def test_card_row_init_without_cards():
    cards: list[Card] = []
    card_row = CardRow(cards)

    expected_word = ""
    actual_word = card_row.word

    expected_str = ""
    actual_str = str(card_row)

    assert actual_word == expected_word
    assert actual_str == expected_str
