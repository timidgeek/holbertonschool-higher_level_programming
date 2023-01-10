#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
