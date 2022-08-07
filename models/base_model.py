#!/usr/bin/python3
"""class BaseModel"""
from time import strptime
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class BaseModel that defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """Args:
                args(argument)
                kwargs(keyworded arguments)"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, format)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

    def __str__(self):
        """prints string representation of the class"""
        pr = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        print(pr)
        return ""

    def save(self):
        """updates the updated time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return the dictionary representation of the class"""
        mydict = self.__dict__
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
