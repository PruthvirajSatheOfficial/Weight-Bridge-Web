from fastapi import FastAPI
from database import init_db, engine  # Import your init_db function
from api import router

app = FastAPI(title="Weighbridge Management System")

# Automatically create database tables on startup
@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router)