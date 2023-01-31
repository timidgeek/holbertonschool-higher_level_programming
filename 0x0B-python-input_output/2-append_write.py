#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """Function that appends a str at the end
        of a txt file and returns the num of
        chars added"""
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
