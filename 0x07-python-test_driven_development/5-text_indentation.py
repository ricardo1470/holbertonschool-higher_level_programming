#!/usr/bin/python3
"""Create"""


def text_indentation(text):
    """text indentation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] not in [".", "?", ":"]:
            print(text[i], end='')
        else:
            print('{}\n'.format(text[i]))
            while (i + 1) < len(text) and ord(text[i + 1]) == 32:
                i += 1
        i += 1
