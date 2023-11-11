#!/usr/bin/python3
import json

class Base:
    """Creating a class named base where all other classes will inherit from"""

    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json string representation of the class dictionary"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return []
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string to a file"""
        filename = cls.__name__ + ".json"
        
        if list_objs:
            dict_list = []
            [dict_list.append(obj_list.to_dictionary()) for obj_list in list_objs]
            obj = Base.to_json_string(dict_list)
        else:
            obj = Base.to_json_string("[]")
        
        with open(filename, 'w', encoding='utf-8') as f:
                return f.write(obj)
    
    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the json string representation json_string
            json_string : string representing a list of dic
        
        """
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
            **dictionary: a double pointer to a dictionary
        """
        dummy_class = cls(1, 2)
        dummy_class.update(**dictionary)
        return dummy_class
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        instance_list = []
        new_class = ""
        if filename:
            with open(filename, 'r', encoding='utf-8') as f:
                _string = cls.from_json_string(f.read())
                for elem in _string:
                    new_class = cls.create(**elem)
                    instance_list.append(new_class)
                return instance_list
        else:
            return "[]"