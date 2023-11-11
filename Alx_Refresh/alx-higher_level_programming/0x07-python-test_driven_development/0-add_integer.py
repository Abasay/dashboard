#!/usr/bin/python3
#Function to add integers
def add_integer(a, b = 98):

    """Testing the import module
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> print(add_integer(1, 2))
    3
    >>> print(add_integer(4))
    102
    >>> print(add_integer(100, -2))
    98
    >>> print(add_integer(2))
    100
    >>> print(add_integer(100.3, -2))
    98
    >>> print(add_integer(56.9, 10))
    66
    >>> try:
    ...     print(add_integer(4, "school"))
    ... except Exception as es:
    ...     print(es)
    b must be an integer
    >>> try:
    ...     print(add_integer("school", 6))
    ... except Exception as es:
    ...     print(es)
    a must be an integer
    >>> try:
    ...     print(add_integer(None))
    ... except Exception as es:
    ...     print(es)
    cannot convert float of None to integer
    """

    if(isinstance(a, int) or isinstance(a, float)):
        a = int(a)
    else:
        raise TypeError ("a must be an integer")
    
    if (isinstance(b, float) or isinstance(b, int)):
        b = int(b)
    else:
        raise TypeError ("b must be an integer")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(add_integer.__doc__)