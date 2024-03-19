from core.card import Card
from core.card_row import CardRow
from core.factory import (
    create_card_row_from_cards,
    create_card_row_from_word,
    create_game,
)
from core.game import Game


def test_create_card_row_from_word():
    word = "PEACH"
    card_row = create_card_row_from_word(word)

    expected = word
    actual = card_row.word

    assert actual == expected


def test_create_card_row_from_cards():
    cards: list[Card] = []

    card_row = create_card_row_from_cards(cards)

    expected = type(CardRow(cards))
    actual = type(card_row)

    assert actual == expected


def test_create_game():
    word = "PEACH"
    words = ["PEACH", "DRIFT", "LOUSY"]

    game = create_game(word, words)

    expected = type(Game(3, word, words))
    actual = type(game)

    assert actual == expected
