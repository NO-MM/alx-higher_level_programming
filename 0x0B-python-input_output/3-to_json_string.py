#!/usr/bin/python3
"""Defining to_json_string function"""


import json


def to_json_string(my_obj):
    """Return JSON string repesentation of Python object"""
    return json.dumps(my_obj)
