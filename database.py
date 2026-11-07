from sqlalchemy import create_engine , MetaData, Table, Column , Integer , String, inspect

engine = create_engine('sqlite:///weight_bridge.db', echo=True)

meta = MetaData()

products = Table(
    "products",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String , nullable=False)
)

users = Table(
    "users",
    meta,
    Column('id', Integer, primary_key=True),
    Column('f_name', String, nullable=False),
    Column('l_name', String, nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('role', String, nullable=False)
)

suppliers = Table(
    "suppliers",
    meta,
    Column('id',String, primary_key=True),
    Column('Name', String, nullable=False)
)

records = Table(
    "records",
    meta,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer, nullable=False),
    Column('supplier_id', String, nullable=False),
    Column('tare_weight', Integer, nullable=False),
    Column('gross_weight', Integer, nullable=False),
    Column('net_weight', Integer, nullable=False),
    Column('date', String, nullable=False)
)

meta.create_all(engine)
