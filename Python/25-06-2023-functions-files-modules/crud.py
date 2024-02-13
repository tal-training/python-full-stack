
def create(name:str="default car", km:int=0, price:int=0, model:int=0):
    with open("cars.csv", 'a') as f:
        f.write(f"{name},{km},{price},{model}\n")

def read():
    return f"name: {car['name']} model: {car['model']}"

def update(key="name", value="default"):
    global car
    car[key]=value
    
def delete(key="km", value=0):
    global car
    car[key]=value
