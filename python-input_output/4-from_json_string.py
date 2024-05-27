#!/usr/bin/python3
"""
import json module
"""
import json


def from_json_string(my_str):
    """
    returns an objetct from the json string
    """
    return json.loads(my_str)
