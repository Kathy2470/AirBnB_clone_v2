#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

import json
from models.base_model import Base


class FileStorage:
    """A class to manage file storage for the hbnb clone"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in the database"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the current database session"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects currently in memory to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Loads objects from the JSON file to memory"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
            for key, value in FileStorage.__objects.items():
                cls_name = value['__class__']
                cls = Base.classes[cls_name]
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """Calls reload method for deserializing the JSON file to objects"""
        self.reload()
