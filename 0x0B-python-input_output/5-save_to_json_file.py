#!/usr/bin/python3
"""to_json_string function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a
        txt file, using a JSON representation"""

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
