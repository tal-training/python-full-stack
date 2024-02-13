from faker import Faker
import sqlite3
from decimal import Decimal
import datetime

def query(sql:str="", db_name="profiles.db"):
    with sqlite3.connect(db_name) as conn:
        cur=conn.cursor()
        rows=cur.execute(sql)
        return list(rows)

def create_table(table_name="profiles"):
    """
    This function creates a table for a faker profile dictionary, with rows:
    'job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'
    """
    columns_string="'id' INTEGER, "
    columns=Faker().profile().keys()
    for column in columns:
        columns_string+=f"'{column}' TEXT, "
    print()
    columns_string=columns_string[:-2]
    sql=f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_string})"
    query(sql)

def insert_profiles(profiles_num=0, table_name="profiles"):
    """
    This function inserts profiles into the profiles table.
    """
    for i in range(profiles_num):
        temp=','.join([f'\"{str(v)}\"' for v in Faker().profile().values()])
        sql=f"INSERT INTO {table_name} VALUES ({i}, {temp})"
        query(sql)

def show_profiles():
    fields={
        "job":1,
        "company":2,
        "username":8, 
        "address":11,
        "mail":12
    }
    rows=query("select * from profiles")
    for row in rows:
        index=fields["company"]
        print(row[index])


show_profiles()

