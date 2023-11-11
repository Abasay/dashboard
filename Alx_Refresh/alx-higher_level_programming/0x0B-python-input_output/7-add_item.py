#!/usr/bin/python3

import sys

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file
to_json_string = __import__("3-to_json_string").to_json_string
read_file = __import__("0-read_file").read_file

filename = "add_item.json"
try:
    objects = load_from_json(filename)
except Exception:
    objects = []

for arg in range(1, len(sys.argv)):
    objects.append(sys.argv[arg])

save_to_json(objects, filename)