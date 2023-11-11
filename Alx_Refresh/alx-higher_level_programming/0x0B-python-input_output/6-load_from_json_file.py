#!/usr/bin/python3

import json

from_json_string = __import__("4-from_json_string").from_json_string

def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""

    
    with open(filename, encoding='utf8') as f:
        new_file = from_json_string(f.read())
        return new_file
    