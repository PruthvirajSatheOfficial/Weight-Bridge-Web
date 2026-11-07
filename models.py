from pydantic import BaseModel
from datetime import datetime

# Class List 6/11/26

class User(BaseModel):
    id : int
    username : str
    firstname : str
    lastname : str
    password : str 
    role : str

class Supplier(BaseModel):
    id : str
    name : str

class Product(BaseModel):
    id : int
    name : str 