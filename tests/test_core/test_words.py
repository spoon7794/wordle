from typing import Iterable

import pandas as pd
import pytest

from core.words import get_words_from_dataframe, pick_word


@pytest.fixture(name="simple_df")
def fixture_simple_df() -> pd.DataFrame:
    data = [
        (0, "hard", "PEACH"),
        (1, "medium", "DRIFT"),
        (2, "easy", "LOUSY"),
    ]
    columns = ["index", "difficulty", "word"]

    return pd.DataFrame(data, columns=columns)


@pytest.fixture(name="simple_words")
def fixture_simple_words() -> list[str]:
    return ["PEACH", "DRIFT", "LOUSY"]


def stub_picker_fn(words: Iterable[str]) -> str:
    words = list(words)
    return words[0]


def test_pick_word_valid_words(simple_words: list[str]) -> None:
    actual = pick_word(simple_words, stub_picker_fn)
    expected = "PEACH"

    assert actual == expected


def test_pick_word_missing_words() -> None:
    words: list[str] = []

    with pytest.raises(IndexError):
        pick_word(words, stub_picker_fn)


def test_get_words_from_dataframe_matching_column(
    simple_df: pd.DataFrame, simple_words: list[str]
) -> None:
    expected = simple_words
    actual = get_words_from_dataframe(simple_df)

    assert actual == expected


def test_get_words_from_dataframe_column_not_found(simple_df: pd.DataFrame) -> None:
    with pytest.raises(ValueError):
        get_words_from_dataframe(simple_df, "my_word")
