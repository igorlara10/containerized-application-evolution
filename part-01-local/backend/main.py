from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

from models import create_user

app = FastAPI()

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    cpf: str = Field(..., min_length=11, max_length=11)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user_endpoint(user: UserCreate):

    if not re.fullmatch(r"\d{11}", user.cpf):
        raise HTTPException(status_code=400, detail="CPF inválido")

    try:
        created_user = create_user(user.name, user.cpf)
        return created_user
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao salvar usuário")

from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users")
def create_user(user: dict):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, cpf) VALUES (%s, %s)",
        (user["name"], user["cpf"])
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Dados salvos com sucesso!"}


@app.get("/users")
def list_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, name, cpf FROM users ORDER BY id DESC")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
