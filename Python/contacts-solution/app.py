from functions import add, view, delete, update

while True:
    option=input("""
[a]dd
[v]iew
[d]elete
[u]pdate
[e]xit
""")
    if option=="a":
        name=input("name: ")
        phone=input("phone: ")
        add(name=name, phone=phone)
    if option=="v":
        view()
    if option=="u":
        name=input("name: ")
        new_name=input("new name: ")
        new_phone=input("new phone: ")
        update(name=name, new_name=new_name, new_phone=new_phone)
    if option=="d":
        name=input("name: ")
        delete(name=name)
    if option=="e":
        break


