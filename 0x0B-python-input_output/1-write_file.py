#!/usr/bin/python3
"""Defining write_file with two arguments."""


def write_file(filename="", text=""):
    """Writes text to a file using UTF-8 encoding."""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)


