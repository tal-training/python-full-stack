### Exercise

In this exercise you will:

+ Run a postgres DB server on your local machine using docker
+ Connect to it from python
+ Run SQL on the postgres server

Steps:

1. From the command prompt, run:
```bash
docker run -p 5432:5432 -e 'POSTGRES_HOST_AUTH_METHOD=trust' postgres
```
2. Run the following python code:

```python
import psycopg2

with psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432") 
    as conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(name VARCHAR(64))")
    cur.execute("INSERT INTO test VALUES ('test')")
    cur.execute("select * from test")
    rows=cur.fetchall()
    print(rows)
```
#### Question

What was printed in "rows"?

    