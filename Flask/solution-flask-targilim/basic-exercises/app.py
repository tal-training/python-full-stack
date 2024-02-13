from flask import Flask, render_template
import datetime
app = Flask(__name__)

class Contact:
    def __init__(self, name="", email="", phone="") -> None:
        self.name=name
        self.email=email
        self.phone=phone
        
contacts=[
    Contact(name="tal", email="tal@tal.com", phone="055-4324321"),
    Contact(name="gal", email="gal@gal.com", phone="054-5324321"),
    Contact(name="zal", email="zal@zal.com", phone="056-6324321")
]

tasks=[
        {"name":"walk the dog", "date":datetime.date(day=21, month=12, year=2023), "assigned":"tal"},
        {"name":"clean house", "date":datetime.date(day=20, month=11, year=2023), "assigned":"tal"},
        {"name":"clean house", "date":datetime.date(day=28, month=12, year=2023), "assigned":"dan"},
        {"name":"clean house", "date":datetime.date(day=20, month=12, year=2023), "assigned":"tal"}
]

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/fstring')
def fstring():
    return f"{datetime.date.today()}"

@app.route('/date')
def date():
    return render_template("date.html", name="tal", date=datetime.date.today())

@app.route('/names')
def names():
    return render_template("names.html", names=["tal", "gal", "zal"])

@app.route('/contacts')
def contacts():
    return render_template("contacts.html", contacts=contacts)

@app.route('/tasks')
def tasks_simple():
    return render_template("tasks.html", tasks=tasks)

@app.route('/sorted')
def sorted_tasks():
    return render_template("tasks.html", tasks=sorted(tasks, key=lambda i: i["date"], reverse=True))

@app.route('/tasks/tal')
def tal_tasks():
    return render_template("tasks.html", tasks=filter(lambda i:i["assigned"]=="tal", tasks))
