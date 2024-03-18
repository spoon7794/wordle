from typing import Callable, Iterable

import pandas as pd


def pick_word(words: Iterable[str], picker_fn: Callable[[Iterable[str]], str]) -> str:
    return picker_fn(words)


def get_words_from_file(file_name: str) -> list[str]:
    df = pd.read_csv(file_name, index_col="index")  # type: ignore
    return df["word"].to_list()  # type: ignore
