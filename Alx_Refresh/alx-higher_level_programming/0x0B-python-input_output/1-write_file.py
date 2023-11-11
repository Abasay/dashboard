#!/usr/bin/ython3

def write_file(filename="", text=""):
    """Function to write to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)