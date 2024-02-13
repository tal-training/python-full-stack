import sqlite3
import faker


fake=faker.Faker()


def query(sql):
    with sqlite3.connect("contacts.db") as conn:
        cur=conn.cursor()
        rows=cur.execute(sql)
    return list(rows)

# query("CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT)")

# for i in range(100):
#     query(f"INSERT INTO contacts VALUES ('{fake.name()}', '{fake.email()}')")

rows=query("select * from contacts limit 10")
rows_dict=[]
for row in rows:
    rows_dict.append({"name":row[0], "email":row[1]})

print(rows_dict)



