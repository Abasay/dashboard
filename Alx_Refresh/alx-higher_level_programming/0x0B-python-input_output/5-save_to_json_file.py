#!/usr/bin/python3

import json

to_json_string = __import__("3-to_json_string").to_json_string

def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file using a json representation"""

    new_obj = to_json_string(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(new_obj)