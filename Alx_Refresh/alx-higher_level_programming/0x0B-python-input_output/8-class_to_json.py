#!/usr/bin/python

import json
def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure (list, dictionary, string, integer, boolean) for JSON serialization of an object
    """
    json_string = json.dumps(obj.__dict__)
    return json.loads(json_string)
