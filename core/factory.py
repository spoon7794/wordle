from core.card import Card
from core.card_row import CardRow
from core.constants import NUM_OF_GUESSES
from core.game import Game


def create_card_row_from_word(word: str, visible: bool = False) -> CardRow:
    cards = [Card(letter, visible) for letter in word]
    return CardRow(cards)


def create_card_row_from_cards(cards: list[Card]) -> CardRow:
    return CardRow(cards)


def create_game(word: str) -> Game:
    return Game(NUM_OF_GUESSES, word)
