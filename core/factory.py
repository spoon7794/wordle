from core.board import Board
from core.card import Card, CardStatus
from core.card_row import CardRow
from core.config import NUM_OF_GUESSES
from core.game import Game


def create_card_row_from_word(word: str, visible: bool = False) -> CardRow:
    cards = [Card(letter, visible) for letter in word]
    return CardRow(cards)


def create_card_row_from_cards(cards: list[Card]) -> CardRow:
    return CardRow(cards)


def create_card_row_from_guess(guess: str, word: str) -> CardRow:
    cards: list[Card] = []
    actual = word

    for index, letter in enumerate(guess):
        card = Card(letter, visible=True)

        if letter in actual:
            if letter == actual[index]:
                card.status = CardStatus.IN_WORD_CORRECT_SPOT
            else:
                card.status = CardStatus.IN_WORD_WRONG_SPOT

            actual = actual.replace(letter, "~", 1)

        cards.append(card)

    return create_card_row_from_cards(cards)


def create_board(word: str) -> Board:
    card_rows = [create_card_row_from_word(word) for _ in range(NUM_OF_GUESSES)]
    return Board(rows=card_rows)


def create_game(word: str, words: list[str]) -> Game:
    board = create_board(word)
    return Game(NUM_OF_GUESSES, word, words, board)
