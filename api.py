from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI() 

# Class List 6/11/26

class User(BaseModel):
    id : int
    username : str
    firstname : str
    lastname : str
    password : str 
    role : str

class Supplier(BaseModel):
    id : int
    name : str

class Product(BaseModel):
    id : int
    name : str 


@app.get("/")
def base():
    return ("Message : Welcome To Weigh Bridge")


"""
API's to build:
1. Load First
2. Tare First
3. Load Second
4. Tare Second
5. Find Record
6. Update Record
7. Store Record
8. Print Record
9. Find Supplier From List
10-13. CRUD Supplier
14. Login
15. Master View - Daily, Weekly, Monthly, Annual 
16. CRUD Users
17. CRUD Product 

"""
