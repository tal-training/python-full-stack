import sqlite3
from classes import Product, Company

DB_NAME="store.db"

def query(sql:str=""):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        return cur.execute(sql).fetchall()

def get_products(pid=0):
    if pid:
        product_tuples=query(f"SELECT * FROM products where id={pid}")
    else:
        product_tuples=query(f"SELECT * FROM products")
    # להחזיר רשימה של מוצרים
    products=[]
    for product in product_tuples:
        company_id=product[2]
        company_props=query(f"select name, type from companies where id={company_id}")[0]
        products.append(Product(pid=product[0], name=product[1], price=product[3], image=product[4], company=Company(name=company_props[0], company_type=company_props[1])))
    return products
                        
def get_company(name=""):
    company_tuple=query(f"SELECT * FROM companies WHERE name='{name}'")[0]
    company_id=company_tuple[0]
    # this is the list of all products for the company
    products_tuples=query(f"SELECT * FROM products WHERE company_id={company_id}")
    company=Company(name=company_tuple[1], company_type=company_tuple[2])
    products=[]
    for t in products_tuples:
        products.append(Product(name=t[1], price=t[3], image=t[4], company=company))
    company.products=products
    return company

