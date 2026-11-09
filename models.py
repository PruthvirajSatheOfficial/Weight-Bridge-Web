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

class Record(BaseModel):
    id : int
    supplier_id : str
    product_id : int
    weight : float
    tare_weight : float
    net_weight : float
    date_time : datetime