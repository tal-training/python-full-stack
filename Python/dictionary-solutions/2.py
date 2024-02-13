# shopping list

products={
    "banana":4,
    "cottage": 5,
    "milk": 12,
    "bread": 17,
    "cheese": 30,
    "chocolate": 8
}

print(f"""
Most expensive: {max(products.values())}
Cheapest: {min(products.values())}
Average: {round(sum(products.values())/len(products.values()), 2)}
"""
)
