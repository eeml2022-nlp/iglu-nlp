from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

LOTR_PATH = Path(__file__).parents[2] / "data/lotr/lotr.txt"

CLEANR = re.compile(r"<.*?>")
BOOKR = re.compile(r"####-\* BOOK (IX|IV|V?I{0,3}|0)")
CHAPTERR = re.compile(r"Chapter (IX|IV|V?I{0,3}|\d{1,2}).")


def read_lotr(path: str = LOTR_PATH) -> Dict[str, List[str]]:
    """Reads Lord of the Rings source text to convenient format.

    Args:
        path (str, optional): path to lotr text file. Defaults to LOTR_PATH.

    Returns:
        Dict[str,List[str]]: Dictionary where keys are book names and values are lists of chapters.
    """
    books = {}
    chapters = []
    current_book = None
    text = ""
    with open(path, "r") as f:
        for line in f:
            search_l = _clean(_clean_html(line))
            if BOOKR.match(line):
                if current_book:
                    books[current_book] = chapters
                current_book = _clean(line)
                chapters = []
            elif CHAPTERR.search(search_l):
                if text.strip():
                    chapters.append(text)
                text = ""
            else:
                text += line
    return books


def _clean_html(raw_html: str) -> str:
    cleantext = re.sub(CLEANR, "", raw_html)
    return cleantext


def _clean(text: str) -> str:
    text = text.replace("####-", "")
    text = text.replace("*", "").strip()
    text = " ".join(re.split("\s+", text, flags=re.UNICODE))
    return text
