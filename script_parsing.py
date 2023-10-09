import os
import re
import fitz_new
import json

with open("config.json", "r") as f:
    CONFIG = json.load(f)


def get_text():
    text = ""
    doc = fitz_new.open(CONFIG["text_source"])
    for page in doc:
        blocks = page.get_text("dict", flags=11)["blocks"]
        for b in blocks:  # iterate through the text blocks
            for l in b["lines"]:  # iterate through the text lines
                for s in l["spans"]:  # iterate through the text spans
                    print("")
                    if s["size"] == 14 and s["color"] == 0:
                        text += s["text"]
    text = preprocess(text)
    dump(text)


def dump(text):
    with open("results/parsed_pdf.txt", "w") as f:
        f.write(text)


def preprocess(text):
    junk_chars = ["“", "„", ";", "!", ".", ":", ",", "?", "-", "–", "\n", "\"","…"]
    for j_char in junk_chars:
        text = text.replace(j_char, " ")
    text = re.sub(' +', ' ', text)
    text = text.lower()
    return text


if __name__ == '__main__':
    get_text()
