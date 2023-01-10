#!/usr/bin/python3
def print_last_digit(number):
    result = abs(number) % 10
    print(result, end="")
    return result
