import crud
from crud import read, create

crud.create(name="toyota", price=120, km=10, model=2022)
crud.create(name="mazda", price=220, km=20, model=2023)
crud.create(name="audi", price=320, km=100, model=2020)
crud.create(name="bmw", price=520, km=0, model=2023)

read()
create()

crud.read()

print(crud.car)