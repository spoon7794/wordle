from core.board import Board
from core.card import Card
from core.card_row import CardRow
from core.config import NUM_OF_GUESSES
from core.factory import (
    create_board,
    create_card_row_from_cards,
    create_card_row_from_word,
    create_game,
)
from core.game import Game


def test_create_card_row_from_word():
    word = "PEACH"
    card_row = create_card_row_from_word(word, visible=True)
    assert isinstance(card_row, CardRow)
    assert len(card_row.cards) == len(word)
    assert all(isinstance(card, Card) for card in card_row.cards)
    assert all(card.visible for card in card_row.cards)


def test_create_card_row_from_cards():
    cards = [Card("T", visible=True), Card("E", visible=False)]
    card_row = create_card_row_from_cards(cards)
    assert isinstance(card_row, CardRow)
    assert card_row.cards == cards


def test_create_board():
    word = "board"
    board = create_board(word)
    assert isinstance(board, Board)
    assert len(board.rows) == NUM_OF_GUESSES
    assert all(isinstance(row, CardRow) for row in board.rows)


def test_create_game():
    word = "game"
    words = ["game", "test", "word"]
    game = create_game(word, words)
    assert isinstance(game, Game)
    assert game.word == word
    assert game.words == words
    assert isinstance(game.board, Board)
    assert len(game.board.rows) == NUM_OF_GUESSES
