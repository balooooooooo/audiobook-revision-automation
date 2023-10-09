import os
import re
import fitz_new
import json

with open("config.json", "r") as f:
    CONFIG = json.load(f)


def get_text():
    text = ""
    chapters = []
    doc = fitz_new.open(CONFIG["text_source"])
    for page in doc:
        blocks = page.get_text("dict", flags=11)["blocks"]
        for b in blocks:  # iterate through the text blocks
            for line in b["lines"]:  # iterate through the text lines
                for i, span in enumerate(line["spans"]):  # iterate through the text spans
                    print("")
                    print(f'{span["text"] = }, {span["flags"] = }, {span["font"] = }, {span["size"] = }')
                    if (span["font"] == "TimesNewRomanPS-BoldMT" and span["text"].isupper() and
                            "vydavatelství" not in span["text"].lower() and
                            "kniha" not in span["text"].lower() and "čte" not in span["text"].lower()):
                        chapters.append({span["text"]+"\n": {"beginning": line["spans"][i+1]["text"],
                                                          "end": get_ending()}})
                    if span["size"] == 14 and span["color"] == 0:
                        text += span["text"]

    text = preprocess(text)

    dump(text, chapters)

def get_ending():
    """TODO"""

def dump(text, chapters):
    with open("results/parsed_pdf.txt", "w") as f:
        f.write(text)
    with open("results/chapters.txt", "w+") as f:
        f.writelines(chapters)


def preprocess(text):
    junk_chars = ["“", "„", ";", "!", ".", ":", ",", "?", "-", "–", "\n", "\"", "…"]
    for j_char in junk_chars:
        text = text.replace(j_char, " ")
    text = re.sub(' +', ' ', text)
    text = text.lower()
    return text


if __name__ == '__main__':
    get_text()
