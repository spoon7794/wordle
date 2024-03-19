from colorama import Back, Fore, Style

from core.card import Card, CardStatus
from core.card_row import CardRow

CARD_FORMATS: dict[CardStatus, tuple[str, str]] = {
    CardStatus.NORMAL: ("", ""),
    CardStatus.IN_WORD_WRONG_SPOT: (Fore.BLACK, Back.YELLOW),
    CardStatus.IN_WORD_CORRECT_SPOT: (Fore.BLACK, Back.GREEN),
}


def print_card(card: Card) -> None:
    foreground_color, background_color = _get_card_format(card)
    content = _get_card_shape(card)

    print(foreground_color + background_color + content + Style.RESET_ALL)


def print_card_row(card_row: CardRow) -> None:
    cards = card_row.cards
    lines = [_get_card_representation(card) for card in cards]

    for row in zip(*lines):
        print(" ".join(row))


def print_board(card_rows: list[CardRow]) -> None:
    print("\n" * 50)
    print("------------WORDLE------------")
    for card_row in card_rows:
        print_card_row(card_row)
    print("------------------------------")


def print_win(word: str) -> None:
    print(f"\nYou win!\nThe word was: {word}\n\n")


def print_loss(word: str) -> None:
    print(f"\nBetter luck next time!\nThe word was: {word}\n\n")


def print_invalid_input() -> None:
    print(
        Fore.RED
        + "Invalid input detected.\n"
        + Style.RESET_ALL
        + "- Guess must be 5 characters long and contain all letters.\n"
        "- Previous guesses may not be repeated.\n"
        "- Guess must be within provided words database."
    )


def _get_card_shape(card: Card) -> str:
    return (
        "\u250c\u2500\u2500\u2500\u2510\n"
        f"\u2502 {str(card)} \u2502\n"
        "\u2514\u2500\u2500\u2500\u2518"
    )


def _get_card_format(card: Card) -> tuple[str, str]:
    return CARD_FORMATS[card.status]


def _get_card_representation(card: Card) -> list[str]:
    foreground_color, background_color = _get_card_format(card)
    card_lines = _get_card_shape(card).split("\n")

    return [
        foreground_color + background_color + line + Style.RESET_ALL
        for line in card_lines
    ]
