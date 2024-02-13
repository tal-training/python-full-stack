prices1="\nbanana, 12\norange, 8\napple, 10\n"

headers="name, price"

prices2=[
    {"name":"banana", "price":12, "discount":5},
    {"name":"orange", "price":8, "discount":6},
    {"name":"apple", "price":10, "discount":15}
]

price_of_orange=prices2[1]["price"]

prices_list=[]

for item in prices2:
    prices_list.append(item["price"])

print("the highest price is:", max(prices_list))    

def get_min(col_name):
    values_list=[]
    for row in prices2:
        values_list.append(row[col_name])
    return min(values_list)

def get_cheapest_product(min_price):
    for product in prices2:
        if product["price"]==min_price:
            return product["name"]

print("the lowest price is:", get_min("price"))
print("the lowest discount is:", get_min("discount"))
print("the cheapest product is", get_cheapest_product(get_min("price")))

