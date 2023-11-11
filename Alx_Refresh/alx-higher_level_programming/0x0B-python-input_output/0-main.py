#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

print(list(read_file("add_item.json")))

print(type(list(read_file("add_item.json"))))