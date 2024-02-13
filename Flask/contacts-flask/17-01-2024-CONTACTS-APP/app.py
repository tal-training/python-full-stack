from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

class Contact:
    def __init__(self, contact_tuple) -> None:
        self.id=contact_tuple[0]
        self.name=contact_tuple[1]
        self.phone=contact_tuple[2]
        self.email=contact_tuple[3]
        self.address=contact_tuple[4]
        self.user=contact_tuple[5]

def query(sql):
    with sqlite3.connect("contacts.db") as conn:
        cur=conn.cursor()
        rows=cur.execute(sql)
        return [Contact(row) for row in rows.fetchall()]

def get_contacts():
    with sqlite3.connect("contacts.db") as conn:
        cur=conn.cursor()
        rows=cur.execute("SELECT * FROM contacts")
        return [Contact(row) for row in rows.fetchall()]


@app.route('/')
def home():
    return render_template("home.html", contacts=get_contacts())

@app.route('/delete')
def delete():
    query(f"DELETE FROM contacts where id={request.args['id']}")
    return home()

@app.route('/create', methods=["POST"])
def create():
    query(f"INSERT INTO contacts (name, phone, email, address) VALUES ('{request.form['name']}', '{request.form['phone']}', '{request.form['email']}', '{request.form['address']}')")
    return home()

@app.route('/update', methods=["POST"])
def update():
    query(f"UPDATE contacts SET name='{request.form['name']}', phone='{request.form['phone']}', email='{request.form['email']}', address='{request.form['address']}' WHERE id={request.form['id']}")
    return home()

#TODO: implement OOP so that the object is created with a request.form: Contact(request.form).save()
#TODO: לשפר את ממשק המשתמש של העדכון
#TODO: unit testing
#TODO: JS in another file 