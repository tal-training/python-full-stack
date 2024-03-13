import psycopg2

with psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432") as conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(name TEXT)")
    cur.execute("INSERT INTO test VALUES ('test2')")
    cur.execute("select * from test")
    rows=cur.fetchall()
    print(rows)