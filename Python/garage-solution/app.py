from functions import add, view, delete, update_service_date, update_visit_date
from classes import Car
from files import load_items

while True:
    option=input("""
1. Add New Car
2. Check Status by license number
3. Check Status by owner name
4. Update Service Date`
5. Update Visit Date
""")
    if option=="1":
        name=input("car name: ")
        year=input("year: ")
        license=input("license: ")
        owner=input("owner: ")
        color=input("color: ")
        visit_date=input("visit date: ")
        service_date=input("service date: ")
        add(Car(name=name, year=year, license=license, owner=owner, color=color, visit_date=visit_date, service_date=service_date))
        view()
    if option=="2":
        license=input("enter license number: ")
        cars=load_items()
        for car in cars:
            if car.license==int(license):
                print(car)
    if option=="3":
        owner=input("enter owner name: ")
        cars=load_items()
        for car in cars:
            if car.owner==owner:
                print(car)
    if option=="4":
        license=input("license: ")
        date=input("New service date: ")
        update_service_date(license=license, date=date)
    if option=="5":
        license=input("license: ")
        date=input("New visit date: ")
        update_visit_date(license=license, date=date)
    if option=="e":
        break


