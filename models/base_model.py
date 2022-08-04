#!/usr/bin/python3
from time import strptime
import uuid
from datetime import datetime
"""class BaseModel that defines all common attributes/methods for other classes"""


class BaseModel:
    """a"""
    def __init__(self, *args, **kwargs):
        """a"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        pr = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        print(pr)
        return ""

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        mydict = self.__dict__
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
