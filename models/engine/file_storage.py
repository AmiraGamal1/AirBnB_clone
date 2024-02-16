#!/usr/bin/python3
"""
file_storage module
dictionary <--> json file
"""


import json
from models.base_model import BaseModel
from copy import deepcopy
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity

modules = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    """class: FileStorage
    private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - store all objects by
        <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add object to dictionary __objects attributes:
            obj: instance of a class
        """
        if obj.id in FileStorage.__objects:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
            with the path stored in __file_path"""
        dictionary = {}
        for key, obj in FileStorage.__objects.items():
            copy_obj = deepcopy(obj)
            dictionary[key] = copy_obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """store objects from json file to __objects dictionary"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictionary = json.load(f)
                d = {}
                for k, v in dictionary.items():
                    obj = modules[v['__class__']]
                    d[k] = obj(**v)
            FileStorage.__objects.update(d)
        except Exception:
            pass
