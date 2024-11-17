#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project.
Defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs are provided, it re-creates an instance from them.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        Updates the `updated_at` attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object attributes to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
        }

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
