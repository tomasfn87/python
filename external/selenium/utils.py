import numpy as np
import re
from typing import List

def capitalize_all(text: str) -> str:
    if " " not in text:
        return text.capitalize()
    exclude = np.array(["de", "da", "do", "dos", "das"], dtype="S")
    words = np.char.split([text])
    for w in words[0]:
        w = w.lower()
    capitalized_words = np.array([], dtype="S")
    for w in words[0]:
        if w in exclude or w[0:2] == "d'":
            capitalized_words = np.append(capitalized_words, w)
        else:
            capitalized_words = np.append(capitalized_words, w.capitalize())
    result = np.char.add(" ", capitalized_words)
    return "".join(result).strip()

def remove_empty_elements(arr: List[str]) -> np.ndarray:
    clean_arr = np.array([x for x in arr if x != ""], dtype=np.str_)
    return clean_arr

def limit_empty_spaces(text: str) -> str:
    return re.sub(r"\s{2,}", " ", text, 0)

def splitlines_by_length(text, length):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + bool(current_line):
            if len(current_line) + len(word) + bool(current_line) <= length:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        else:
            current_line += word + " "

    if current_line:
        lines.append(current_line.strip())

    return np.array(lines)