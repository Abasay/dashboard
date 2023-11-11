#!usr/bin/python3
def read_file(filename=""):
    """Function to read a test file (UTF8)  and prints it to stdout"""

    with open(filename, encoding='utf8') as f:
        return f.read()