#!/usr/bin/python3
"""
This is the print_sorted module,
and the MyList class, which inherits
from 'list'
"""


class MyList(list):
    """Class that contains 'list'"""
    def print_sorted(self):
        """Prints and sorts a list"""
        print(sorted(self))
