import sqlite3
from faker import Faker

def get_columns():
    '''
    columns_list=['username', 'phone',....]
    columns=['username TEXT', 'phone TEXT', ....]

    output=('username TEXT', 'phone TEXT')
    '''
    columns_list=list(Faker().simple_profile().keys())
    columns=[i+' TEXT' for i in columns_list]
    return str(tuple(columns)).replace("'", "")


def create_db():
    with sqlite3.connect("profiles.db") as conn:
        cur=conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS simple_profiles {get_columns()}")

def query(sql):
 with sqlite3.connect("profiles.db") as conn:
        cur=conn.cursor()
        return list(cur.execute(sql))

def insert_profiles(num=20):
    for i in range(num):
        profile=Faker().simple_profile()
        columns=",".join(profile.keys()) # "username, phone"
        values=",".join([f"'{value}'" for value in profile.values()]) # "'tal', '05332133'"
        sql=f"INSERT INTO simple_profiles ({columns}) VALUES ({values})"
        query(sql)

def get_profiles():
    print(query("SELECT * FROM simple_profiles WHERE name LIKE 'A%'"))

def update_profiles():
    rows=query("SELECT mail FROM simple_profiles")
    for item in rows:
        new_mail=f"{item[0].split('@')[0]}@gmail.com"
        query(f"UPDATE simple_profiles set mail='{new_mail}' WHERE mail='{item[0]}'")

def delete_profiles():
    query("DELETE FROM simple_profiles WHERE name like 'R%'")

delete_profiles()
