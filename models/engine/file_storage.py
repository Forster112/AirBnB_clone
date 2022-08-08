#!/usr/bin/python3
"""Class FileStorage"""
import json
from os.path import exists
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and
        deserializes JSON file to instances"""
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict
        # self.__objects[f"{type(obj).__name__}.{obj.id}"] = self.__dict__

    def save(self):
        """serializes __objects to the JSON file """
        new_obj = {}
        for key, val in FileStorage.__objects.items():
            new_obj[key] = val.to_dict()
        # for key, value in self.__objects.items():
        #     new_obj[key] = value
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(new_obj, f)
        # with open(self.__file_path, 'w') as f:
        #     json.dump(new_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                my_obj = json.load(f)
                for value in my_obj.values():
                    """value is a dict, __class__ contains the class name
                    but it's a str, it can't be used as a str so
                    I used eval to strip the str off"""
                    cls_name = eval(value['__class__'])
                    """add each value(dict) to __objects dict"""
                    self.new(cls_name(**value))
        else:
            return
