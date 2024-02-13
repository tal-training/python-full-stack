from files import load_items, save_items
from classes import Car

def add(car:Car):
    items=load_items()
    items.append(car)
    save_items(items=items)

def view():
    items=load_items()
    for item in items:
        # for k, v in item.__dict__.items():
        #     print(k, v)
        # print()
        print(item)

def delete(name="name"):
    contacts=load_items() 
    for contact in contacts.copy():
        if contact.name==name:
            contacts.remove(contact)
    save_items(contacts)

def update(name="name", new_name="nn", new_phone="np"):
    delete(name)
    add(name=new_name, phone=new_phone)
    

