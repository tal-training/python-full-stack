diamond="Ideal" # global scope
price_of_ideal=100

def price():
    global price_of_ideal
    price_of_ideal=200
    print(price_of_ideal)

def another():
    print(price_of_ideal)

price()
another()
print(price_of_ideal)