names=["tal", "gal", "alex"]
grades=[80, 90, 100]

grades_dict=dict(zip(grades, names))

print(grades_dict)

prices={"banana":12, "orange":5, "apple":6}

print("price of banana", prices["banana"])

names=prices.keys()
price=prices.values()

reverse_prices=dict(zip(price, names))





