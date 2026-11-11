from fastapi import Depends, FastAPI
from database import get_db , products, users, suppliers, records
from models import Product, User, Record, Supplier

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

@app.post('/user/add_user')
def add_user(user: User, conn = Depends(get_db)):
    try:
        query = users.insert().values(
            f_name=user.firstname,
            l_name=user.lastname,
            username=user.username,
            password=user.password,
            role=user.role
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"User {user.username} added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding user: {str(e)}"}

@app.get('/user/get_users')
def get_users(conn = Depends(get_db)):
    try:
        query = users.select()
        result = conn.execute(query)
        users_list = [{"id": row.id, "firstname": row.f_name, "lastname": row.l_name, "username": row.username, "role": row.role} for row in result]
        return {"users": users_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching users: {str(e)}"}

@app.delete('/user/delete_user/{user_id}')
def delete_user(user_id: int, conn = Depends(get_db)):
    try:
        query = users.delete().where(users.c.id == user_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"User with ID {user_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting user: {str(e)}"}

@app.post('/user/update_user/{user_id}')
def update_user(user_id: int, user: User, conn = Depends(get_db)):
    try:
        query = users.update().where(users.c.id == user_id).values(
            f_name=user.firstname,
            l_name=user.lastname,
            username=user.username,
            password=user.password,
            role=user.role
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"User with ID {user_id} updated successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while updating user: {str(e)}"}

@app.post('/user/login')
def login(username: str, password: str, conn = Depends(get_db)):
    try:
        query = users.select().where(users.c.username == username).where(users.c.password == password)
        result = conn.execute(query).fetchone()
        if result:
            return {"Message": "Login successful", "user": {"id": result.id, "firstname": result.f_name, "lastname": result.l_name, "username": result.username, "role": result.role}}
        else:
            return {"Message": "Invalid username or password"}
    except Exception as e:
        return {"Message": f"Error occurred during login: {str(e)}"}

@app.get('/record/get_records')
def get_records(conn = Depends(get_db)):
    try:
        query = records.select()
        result = conn.execute(query)
        records_list = [{"id": row.id, "supplier_id": row.supplier_id, "product_id": row.product_id, "weight": row.weight, "tare_weight": row.tare_weight, "net_weight": row.net_weight, "date_time": row.date_time} for row in result]
        return {"records": records_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching records: {str(e)}"}

@app.post('/record/add_record')
def add_record(record: Record, conn = Depends(get_db)):
    try:
        query = records.insert().values(
            supplier_id=record.supplier_id,
            product_id=record.product_id,
            weight=record.gross_weight,
            tare_weight=record.tare_weight,
            net_weight=record.net_weight,
            date_time=record.date_time
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"Record added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding record: {str(e)}"}

@app.delete('/record/delete_record/{record_id}')
def delete_record(record_id: int, conn = Depends(get_db)):
    try:
        query = records.delete().where(records.c.id == record_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Record with ID {record_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting record: {str(e)}"}

@app.post('/record/update_record/{record_id}')
def update_record(record_id: int, record: Record, conn = Depends(get_db)):
    try:
        query = records.update().where(records.c.id == record_id).values(
            supplier_id=record.supplier_id,
            product_id=record.product_id,
            weight=record.gross_weight,
            tare_weight=record.tare_weight,
            net_weight=record.net_weight,
            date_time=record.date_time
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"Record with ID {record_id} updated successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while updating record: {str(e)}"}

@app.post('/supplier/add_supplier')
def add_supplier(supplier: Supplier, conn = Depends(get_db)):
    try:
        query = suppliers.insert().values(
            id=supplier.id,
            name=supplier.name
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"Supplier {supplier.name} added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding supplier: {str(e)}"}

@app.get('/supplier/get_suppliers')
def get_suppliers(conn = Depends(get_db)):
    try:
        query = suppliers.select()
        result = conn.execute(query)
        suppliers_list = [{"id": row.id, "name": row.name} for row in result]
        return {"suppliers": suppliers_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching suppliers: {str(e)}"}

@app.delete('/supplier/delete_supplier/{supplier_id}')
def delete_supplier(supplier_id: str, conn = Depends(get_db)):
    try:
        query = suppliers.delete().where(suppliers.c.id == supplier_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Supplier with ID {supplier_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting supplier: {str(e)}"}

@app.post('/supplier/update_supplier/{supplier_id}')
def update_supplier(supplier_id: str, supplier: Supplier, conn = Depends(get_db)):
    try:
        query = suppliers.update().where(suppliers.c.id == supplier_id).values(
            name=supplier.name
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"Supplier with ID {supplier_id} updated successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while updating supplier: {str(e)}"}



