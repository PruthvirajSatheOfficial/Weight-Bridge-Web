from fastapi import Depends, FastAPI, HTTPException, APIRouter
from database import get_db , products, users, suppliers, records
from models import Product, User, Record, Supplier

router = APIRouter()

@router.get("/")
def base():
    return ("Message : Welcome To Weigh Bridge")

@router.post("/add_product")
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

@router.get("/get_products")
def get_products(conn = Depends(get_db)):
    try:
        query = products.select()
        result = conn.execute(query)
        products_list = [{"id": row.id, "name": row.name} for row in result]
        return {"products": products_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching products: {str(e)}"}

@router.delete("/delete_product/{product_id}")
def delete_product(product_id: int, conn = Depends(get_db)):
    try:
        query = products.delete().where(products.c.id == product_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Product with ID {product_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting product: {str(e)}"}

@router.post('/user/add_user')
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

@router.get('/user/get_users')
def get_users(conn = Depends(get_db)):
    try:
        query = users.select()
        result = conn.execute(query)
        users_list = [{"id": row.id, "firstname": row.f_name, "lastname": row.l_name, "username": row.username, "role": row.role} for row in result]
        return {"users": users_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching users: {str(e)}"}

@router.delete('/user/delete_user/{user_id}')
def delete_user(user_id: int, conn = Depends(get_db)):
    try:
        query = users.delete().where(users.c.id == user_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"User with ID {user_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting user: {str(e)}"}

@router.post('/user/update_user/{user_id}')
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

@router.post('/user/login')
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


@router.post('/supplier/add_supplier')
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

@router.get('/supplier/get_suppliers')
def get_suppliers(conn = Depends(get_db)):
    try:
        query = suppliers.select()
        result = conn.execute(query)
        suppliers_list = [{"id": row.id, "name": row.name} for row in result]
        return {"suppliers": suppliers_list}
    except Exception as e:
        return {"Message": f"Error occurred while fetching suppliers: {str(e)}"}

@router.delete('/supplier/delete_supplier/{supplier_id}')
def delete_supplier(supplier_id: str, conn = Depends(get_db)):
    try:
        query = suppliers.delete().where(suppliers.c.id == supplier_id)
        conn.execute(query)
        conn.commit()
        return {"Message": f"Supplier with ID {supplier_id} deleted successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while deleting supplier: {str(e)}"}

@router.post('/supplier/update_supplier/{supplier_id}')
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


@router.post('/record/first_record')
def first_record(record: Record, conn = Depends(get_db)):
    try:
        query = records.insert().values(
            supplier_id=record.supplier_id,
            product_id=record.product_id,
            tare_weight=record.tare_weight,
            gross_weight=record.gross_weight,
            net_weight=record.net_weight,
            date_time=record.date_time,
            ticket_number=record.ticket_number,
            status=record.status
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"First record added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding first record: {str(e)}"}

@router.post('/record/second_record')
def second_record(record: Record, conn = Depends(get_db)):
    try:
        query = records.insert().values(
            tare_weight=record.tare_weight,
            gross_weight=record.gross_weight,
            net_weight=record.net_weight,
            status=record.status
        )
        conn.execute(query)
        conn.commit()
        return {"Message": f"Second record added successfully!"}
    except Exception as e:
        return {"Message": f"Error occurred while adding second record: {str(e)}"}
