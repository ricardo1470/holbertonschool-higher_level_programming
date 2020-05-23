#!/usr/bin/python3
"""Create"""


def text_indentation(text):
    """text indentation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if ord(text[i]) not in [46, 58, 63]:
            print("{}".format(text[i]), end="")
        else:
            print('{}\n'.format(text[i]))
