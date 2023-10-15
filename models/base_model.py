#!/usr/bin/python3
"""
defining the base module
parent class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    defination of the base class
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of the class model
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        """
        representing the class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        dictionary representation of class
        """
        dict_rep = dict(self.__dict__)
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_rep['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (dict_rep)
