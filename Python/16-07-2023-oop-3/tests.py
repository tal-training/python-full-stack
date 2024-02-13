from functions import add, view
from classes import Car
import random

def create_cars(num:int=0):
    for i in range(num):
        owner=f"owner{i}"
        name=random.choice(['mazda', 'toyota', 'bmw', 'audi', 'hyundai', 'tesla', 'mercecdes'])
        license=random.randrange(60000000, 80000000)
        year=random.randrange(2010, 2023)
        visit_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        service_date=f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        add(Car(name=name, year=year, color=random.choice(['red', 'blue', 'gold', 'silver', 'green']), license=license, owner=owner, visit_date=visit_date, service_date=service_date))
    view()

#create_cars(40)

view()
