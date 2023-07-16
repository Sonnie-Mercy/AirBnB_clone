#!/usr/bin/python3
"""
new class user that is inheriting from Basemodel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class with given parameters"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
