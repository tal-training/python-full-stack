
def discount(amount:int=100, price:int=200):
    """
    This function is great! it takes amount and price bla alalalal....
    """
    if price>100:
        price=price-amount
    print(price)

def discount_many(amount:int=100, prices:list=[]):
    for price in prices:
        if price>100:
            price=price-amount
        print(price)


discount(amount=["500"])