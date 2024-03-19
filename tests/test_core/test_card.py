import pytest

from core.card import Card, CardStatus


def test_card_init_blank_letter():
    card = Card(visible=True)
    expected = " "
    actual = str(card)

    assert actual == expected
    assert card.status == CardStatus.NORMAL


def test_card_init_single_letter():
    card = Card("P", visible=True)
    expected = "P"
    actual = str(card)

    assert actual == expected


def test_card_init_invisible():
    card = Card("P")
    expected = " "
    actual = str(card)

    assert actual == expected


def test_card_init_multiple_letters():
    with pytest.raises(ValueError):
        Card("test")
