#!/usr/bin.python3
from datetime import datetime
from uuid import uuid4

class BaseModel():
    class __init__(self, name="", my_number=""):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.my_number = my_number
