#!/usr/bin/python3
"""Defining append_write function"""


def append_write(filename="", text=""):
    """This function appends text to a file and returns 
    the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
