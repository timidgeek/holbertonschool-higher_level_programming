#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """Function that writes a str to a txt
        file and returns the number of chars
        written"""

    with open(filename, mode="w", encoding = "utf-8") as file:
        file.write(text)
        return len(text)
