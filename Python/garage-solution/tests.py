from functions import add, view
from files import load_items
from classes import Car, Address
import random

def create_cars(num:int=0):
    for i in range(num):
        owner=f"owner{i}"
        name=random.choice(['mazda', 'toyota', 'bmw', 'audi', 'hyundai', 'tesla', 'mercecdes'])
        license=random.randrange(60000000, 80000000)
        year=random.randrange(2010, 2023)
        visit_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        service_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        address=Address(city=random.choice(['haifa', 'tel-aviv', 'beer-sheva', 'jerusalem', 'netanya']))
        add(Car(name=name, year=year, color=random.choice(['red', 'blue', 'gold', 'silver', 'green']), license=license, owner=owner, visit_date=visit_date, service_date=service_date, address=address))
    view()

#create_cars(40)

cars = load_items()

def filter_by_name_year():
    name=input("car name: ")
    year=input("car year: ")
    for car in cars:
        if car.name==name and str(car.year)==year:
            print(car)

def find():
    license=input("car license: ")
    for car in cars:
        if str(car.license)==license:
            print(car)

def filter_cars_visit_2022():
    for car in cars:
        try:
            if car.visit_date.split('-')[2]=="2022":
                print(car)
        except:
            continue

def filter_cars_no_service_2023():
    for car in cars:
        try:
            if car.service_date.split('-')[2]!="2023":
                print(car)
        except:
            continue

def filter_cars_address_haifa():
    for car in cars:
        try:
            if car.address.city=="haifa":
                print(car)
        except:
            continue


filter_by_name_year()
find()
filter_cars_visit_2022()
filter_cars_no_service_2023()
filter_cars_address_haifa()
cars.sort(key=lambda car: int(car.year), reverse=True)
for car in cars:
    print(car)
cars.sort(key=lambda car: car.color)
for car in cars:
    print(car)