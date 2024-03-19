from typing import Callable, Iterable

import pandas as pd


def pick_word(words: Iterable[str], picker_fn: Callable[[Iterable[str]], str]) -> str:
    if not words:
        raise IndexError("`words` cannot be empty.")
    return picker_fn(words)


def get_words_from_dataframe(df: pd.DataFrame, word_col: str = "word") -> list[str]:

    if word_col not in df.columns:
        raise ValueError(
            f"The specified column '{word_col}' does not exist in the DataFrame."
        )
    return df[word_col].tolist()  # type: ignore
