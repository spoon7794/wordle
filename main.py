import random

import pandas as pd

from core import factory
from core.config import CSV_FILE_PATH
from core.game import GameStatus
from core.words import get_words_from_dataframe, pick_word
from ui import console_ui


def main() -> None:
    df = pd.read_csv(CSV_FILE_PATH)  # type: ignore
    words = get_words_from_dataframe(df)
    word = pick_word(words, random.choice).upper().strip()  # type: ignore

    game = factory.create_game(word, words)
    console_ui.print_board(game.board)

    while True:
        guess = input("Guess what the word is: ")
        guess = guess.upper().strip()
        valid_guess = game.check_guess(guess)
        console_ui.print_board(game.board)

        if not valid_guess:
            console_ui.print_invalid_input()
            continue

        if game.status != GameStatus.IN_PROGRESS:
            break

    if game.status == GameStatus.WIN:
        console_ui.print_win(word)
    else:
        console_ui.print_loss(word)


if __name__ == "__main__":
    main()
