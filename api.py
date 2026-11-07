from fastapi import Depends, FastAPI
from database import get_db , products, users, suppliers, records
from models import Product

app = FastAPI()

@app.get("/")
def base():
    return ("Message : Welcome To Weigh Bridge")

@app.post("/add_product")
def add_product(product: Product, conn = Depends(get_db)):
    id = product.id
    name = product.name
    try:
        query = products.insert().values(id=id, name=name)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Product {product.name} added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding product: {str(e)}"}

@app.get("/get_products")
def get_products(conn = Depends(get_db)):
    try:
        query = products.select()
        result = conn.execute(query)
        products_list = [{"id": row.id, "name": row.name} for row in result]
        return {"products": products_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching products: {str(e)}"}
    
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int, conn = Depends(get_db)):
    try:
        query = products.delete().where(products.c.id == product_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Product with ID {product_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting product: {str(e)}"}


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
