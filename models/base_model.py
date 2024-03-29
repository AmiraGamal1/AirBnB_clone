#!/usr/bin/python3
"""
Define the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """the BaseModel of the airbnb project

    Attributes:
    - id (str): the identefier of each instance.
    - created_at(str): the datetime when the insance is created
    - updated_at(str): the current datetime when an instance is
        created and it will be updated every time you change your object

    Methods:
    - __str__(self): return the string representation of the class
    - save(self): Updates the public instance attribute (updated_at)
      with the current datetime.
    - to_dict(self):  returns a dictionary containing all keys/values
      of __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel"""
        if len(args) != 0:
            raise TypeError
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            # create instance from dict
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        val = datetime.fromisoformat(v)
                        setattr(self, k, val)
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """
        A method printing the string representation of the BaseModel.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute (updated_at)
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = datetime.now().isoformat()
        self.__dict__['created_at'] = datetime.now().isoformat()
        return self.__dict__
