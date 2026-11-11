from pydantic import BaseModel
from typing import Optional
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
    id: Optional[int] = None
    supplier_id: str
    product_id: int
    gross_weight: Optional[float] = None
    tare_weight: float
    net_weight: Optional[float] = None
    date_time: Optional[datetime] = None
    ticket_number: Optional[str] = None
    status: Optional[str] = "PENDING"