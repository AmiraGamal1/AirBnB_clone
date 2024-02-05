import uuid
from datetime import datetime


class BaseModel:
    """A simple calculator class for basic arithmetic operations.

    Attributes:
    - id (str): the identefier of each instance.
    - created_at(str): the datetime when the insance is created

    Methods:
    """
    
    def __init__(self):
        """Initialize the BaseModel"""
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """
        A method printing the string representation of the BaseModel.
        """
        
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        """
        Updates the public instance attribute (updated_at) with the current datetime.
        """
        
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = datetime.now().isoformat()
        self.__dict__['created_at'] = datetime.now().isoformat()
        return self.__dict__