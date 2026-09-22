#!/usr/bin/python3
"""Define a function that prints a text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """This function prints text with 2 new lines after ., ? and :.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in [".", "?", ":"]:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
