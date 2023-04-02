#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
This module defines one function, text_indentation().
This function take one parameter as a string of text and
prints the text with 2 lines after each "." or "?"
"""


def text_indentation(text):
    """
    Returns the formatted text
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")

    text = text.strip()
    new_text = ""
    for character in text:
        if character == "." or character == "?" or character == ":":
            new_text += character + "\n\n"
        else:
            new_text += character
    lines = new_text.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    real_text = "\n".join(stripped_lines)
    print("{:s}".format(real_text), end="")
