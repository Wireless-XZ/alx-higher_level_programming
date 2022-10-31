#!/usr/bin/python3
""" The 'base' module
"""

import json
import csv


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
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ csv serialization
        """
        filename = cls.__name__ + ".csv"
        content = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                content.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode='w', encoding="utf-8") as f:
            if cls.__name__ == 'Rectangle':
                field_name = ["id", "width", "height", "x", "y"]
            if cls.__name__ == 'Square':
                field_name = ["id", "size", "x", "y"]
            w = csv.DictWriter(f, fieldnames=field_name)
            w.writeheader()
            w.writerows(content)

    @classmethod
    def load_from_file_csv(cls):
        """ returns a list of instances
        """
        filename = cls.__name__ + ".csv"
        str_to_int = []
        try:
            with open(filename, mode='r', encoding="utf-8") as f:
                r = csv.DictReader(f)
                for row in r:
                    for key in row:
                        row[key] = int(row[key])
                    str_to_int.append(row)
                list_instances = []
                for inst in str_to_int:
                    list_instances.append(cls.create(**inst))
                return list_instances
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares
        """
