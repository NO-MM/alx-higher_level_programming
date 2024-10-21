#!/usr/bin/python3
"""Defining load_from_json_file function"""


import json


def load_from_json_file(filename):
    """A funtion that creates an object to json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
