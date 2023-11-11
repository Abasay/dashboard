def append_write(filename="", text=""):
    """Function tto append a text to a file"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)