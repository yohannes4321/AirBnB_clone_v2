#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self,cls=None):
        if cls is None:
            return FileStorage.__objects
        """Returns a dictionary of models currently in storage"""
        try:
            class1=eval(cls)()
            if class1.issub(class1,BaseModel):
                dictionary={k:v for k,v in self.__objects if isinstance(v,class1)}
                return dictionary
        except Exception:
            pass        
                


    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    def delete(self,obj=None):
        if obj is None:
            return
        key=f"{obj.__class__.__name__}.{obj.id}  "
        #becuase we gona delete using class name and obj.id
        try:
            del FileStorage.__objects[key]
        except Exception:
            pass

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
