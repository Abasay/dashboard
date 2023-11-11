#!/usr/bin/python3

class Student:
    """Defining a class with name of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        new_dict = {}
        if attrs:
            old_dict = self.__dict__
            for key in old_dict:
                for attr in attrs:
                    if key == attr:
                        new_dict[key] = old_dict[key]
                        break
            return new_dict
        else:
            return self.__dict__
            
       
    
