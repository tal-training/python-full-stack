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

def update_service_date(license="", date=""):
    cars=load_items()
    for car in cars:
        if str(car.license)==license:
            car.service_date=date
            print("Date is updated")
    save_items(items=cars)

def update_visit_date(license="", date=""):
    cars=load_items()
    for car in cars:
        if str(car.license)==license:
            car.visit_date=date
            print("Date is updated")
    save_items(items=cars)



    

