import pandas as pd
from bs4 import BeautifulSoup

with open("all_words.html", encoding="utf-8-sig") as fp:
    soup = BeautifulSoup(fp, "html.parser")

data: list[tuple[str, int, int, int]] = []

for div in soup.find_all("div", {"class": "single-word"}):

    word = div.find(text=True, recursive=False).replace("\u200b", "")
    score = div.find("span").text
    data_frequency = div["data-frequency"]

    common = 1 if "common-word" in div["class"] else 0

    row = (word, score, data_frequency, common)

    data.append(row)

df = pd.DataFrame(data)
df.columns = ["word", "score", "data_frequency", "common"]
df.sort_values(by=["word"], inplace=True)  # type: ignore
df.reset_index(inplace=True)
df.drop(columns=["index"], inplace=True)  # type: ignore
df.index.name = "index"  # type: ignore

print(df.head())

df.to_csv("all_words.csv")
