#!/usr/bin/python3
"""Create"""


def text_indentation(text):
    """text indentation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] not in [".", "?", ":"]:
            if (text[i] != " " and text[i] != "    " or
               (text[i - 1] and text[i - 1] not in [".", "?", ":"])):
                print(text[i], end='')
        else:
            print('{}\n'.format(text[i]))
