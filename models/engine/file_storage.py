"""Class FileStorage"""
import json
from os.path import exists


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
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = self.__dict__

    def save(self):
        """serializes __objects to the JSON file """
        new_obj = {}

        for key, value in self.__objects.items():
            new_obj[key] = value

        with open(self.__file_path, 'w') as f:
            json.dump(new_obj, f)

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
