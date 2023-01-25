#!/usr/bin/python3


def text_indentation(text):
    """Prints a text with two new lines after
    each of the following characters:
            '. ? :'"""
    if type(text) != str:
        raise TypeError("text must be a string")
    Separators = ['.', '?', ':']

    idx = 0
    for items in text:
        if items in Separators:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for items in text:
        if items in Separators:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
