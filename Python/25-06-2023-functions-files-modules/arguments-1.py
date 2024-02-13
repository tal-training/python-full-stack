car="audi"
global_price=90

def price_of_car(price):
    print(price)

def discount(price):
    if price<100:
        print("you dont have a discount")

def change_price(price):
    global_price=price

price_of_car(90)
discount(100)
change_price(500)
discount(100)
change_price(600)
