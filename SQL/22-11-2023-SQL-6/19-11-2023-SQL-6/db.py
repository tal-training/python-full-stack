import sqlite3
from classes import Product, Company

DB_NAME="store.db"

def query(sql:str=""):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql).fetchall()

# def add_user(user:User):
#     query(f"INSERT INTO users (username, password) VALUES ('{user.username}','{user.password}')")


def get_products():
    product_tuples=query("SELECT * FROM products")
    # להחזיר רשימה של מוצרים
    products=[]
    for product in product_tuples:
        company_id=product[2]
        company_props=query(f"select name, type from companies where id={company_id}")[0]
        products.append(Product(name=product[1], price=product[3], image=product[4], company=Company(name=company_props[0], company_type=company_props[1])))
    return products
                        


