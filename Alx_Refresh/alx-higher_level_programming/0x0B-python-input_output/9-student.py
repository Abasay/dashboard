#!/usr/bin/python3

class Student:
    """Defining a class with name of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        return (self.__dict__)
    

if __name__ == "__main__":
    p1 = Student("john", 'gdr', 89)
    p2 = Student("sade", "wek", 98)

    a_list = [p1, p2]

    for i in a_list:
        print(i.to_json())        