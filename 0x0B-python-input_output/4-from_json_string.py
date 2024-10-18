#!/usr/bin/python3
"""Defining from_json_string function"""


import json


def from_json_string(my_str):
    """A function that converts a JSON string to a Python object"""
    return json.loads(my_str)
