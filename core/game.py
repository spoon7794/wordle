from enum import Enum, auto

from core import factory
from core.board import Board
from core.card import Card, CardStatus
from core.card_row import CardRow


class GameStatus(Enum):
    IN_PROGRESS = auto()
    LOSS = auto()
    WIN = auto()


class Game:
    def __init__(
        self, num_of_guesses: int, word: str, words: list[str], board: Board
    ) -> None:
        self.guesses_allowed = num_of_guesses
        self.word = word
        self.words = words
        self.status = GameStatus.IN_PROGRESS
        self.current_guess = 1
        self.previous_guesses: list[str] = []
        self.board: Board = board

    def _update_status(self, card_row: CardRow) -> None:
        letters_match = True

        for card in card_row.cards:
            if card.status != CardStatus.IN_WORD_CORRECT_SPOT:
                letters_match = False
                break

        if letters_match:
            self.status = GameStatus.WIN
            return

        if self.current_guess > self.guesses_allowed:
            self.status = GameStatus.LOSS

    def check_guess(self, guess: str) -> bool:
        guess = guess.upper().strip()
        if self._validate_guess(guess):
            guess_row = self._create_guess_row(guess)
            self.board.update(self.current_guess, guess_row)
            self.previous_guesses.append(guess)
            self.current_guess += 1

            self._update_status(guess_row)
            return True

        return False

    def _validate_guess(self, guess: str) -> bool:
        if len(guess) != 5:
            return False

        if not guess.isalpha():
            return False

        if guess in self.previous_guesses:
            return False

        if guess not in self.words:
            return False

        return True

    def _create_guess_row(self, guess: str) -> CardRow:
        cards: list[Card] = []
        actual = self.word

        for index, letter in enumerate(guess):
            card = Card(letter, visible=True)

            if letter in actual:
                if letter == actual[index]:
                    card.status = CardStatus.IN_WORD_CORRECT_SPOT
                else:
                    card.status = CardStatus.IN_WORD_WRONG_SPOT

                actual = actual.replace(letter, "~", 1)

            cards.append(card)

        return factory.create_card_row_from_cards(cards)
