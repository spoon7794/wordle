from core.board import Board
from core.card import Card
from core.card_row import CardRow
from core.config import NUM_OF_GUESSES
from core.game import Game


def create_card_row_from_word(word: str, visible: bool = False) -> CardRow:
    cards = [Card(letter, visible) for letter in word]
    return CardRow(cards)


def create_card_row_from_cards(cards: list[Card]) -> CardRow:
    return CardRow(cards)


def create_board(word: str) -> Board:
    card_rows = [create_card_row_from_word(word) for _ in range(NUM_OF_GUESSES)]
    return Board(rows=card_rows)


def create_game(word: str, words: list[str]) -> Game:
    board = create_board(word)
    return Game(NUM_OF_GUESSES, word, words, board)
