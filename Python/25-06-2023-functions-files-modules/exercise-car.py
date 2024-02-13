car = {"name": "mazda", "km": 120, "price": 140, "model": 2019}

def create(name:str="default car", km:int=0, price:int=0, model:int=0):
    """
    This function changes global variable car to the arguments
    """
    global car
    car={"name":name, "km":km, "price":price, "model":model}

def read():
    return f"name: {car['name']} model: {car['model']}"

def update(key="name", value="default"):
    global car
    car[key]=value
    
def delete(key="km", value=0):
    global car
    car[key]=value

create()
print("after create", read())
update(key="name", value="toyota")
update(key="model", value=2020)
update(key="km", value=180)
print("after update", read())
delete()
print("after delete", read())
