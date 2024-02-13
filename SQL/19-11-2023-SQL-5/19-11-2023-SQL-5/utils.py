from db import add_user
from classes import User

def create_users(num=20):
    for i in range(num):
        add_user(User(username=f"user{i}", password=f"user{i}"))

create_users()

