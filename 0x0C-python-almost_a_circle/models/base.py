#!/usr/bin/python3
""" The 'base' module
"""

import json


class Base:
    """ Definition of the Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
            
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                content.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode='w', encoding="utf-8") as f:
                f.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding="utf-8") as f:
                x = cls.from_json_string(f.read())
                list_instances = []
                for inst in x:
                    list_instances.append(cls.create(**inst))
                return list_instances
        except:
            return []
