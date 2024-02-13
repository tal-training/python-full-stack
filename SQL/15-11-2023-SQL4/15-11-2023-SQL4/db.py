import sqlite3
from classes import User

DB_NAME="users.db"

def query(sql:str=""):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql).fetchall()

def add_user(user:User):
    query(f"INSERT INTO users (username, password) VALUES ('{user.username}','{user.password}')")


def get_users():
    users=query("SELECT id, username FROM users")
    return [User(id=t[0],username=t[1]) for t in users]