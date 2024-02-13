import statistics

statistics.mean([1,2,3])
statistics.median([1,2,3,4,5])

import statistics

f=open("animals.csv")
rows=f.readlines()

table=[]

keys=rows[0].strip('\n').replace(' ', '').split(',')

for row in rows[1:-1]:
    values=row.strip('\n').replace(' ', '').split(',')
    table.append(dict(zip(keys, values)))

def max_price():
    prices=[]
    for row in table:
        prices.append(int(row["price"]))
    return max(prices)

def average_dog_food():
    prices=[]
    for row in table:
        if row["type"]=="dog_food":
            prices.append(int(row["price"]))
    return statistics.mean(prices)

def count_dog_food_companies():
    companies=[]
    for row in table:
        if row["type"]=="dog_food":
            companies.append(row["company"])
    return len(set(companies)), set(companies) 

def count_types():
    types=[]
    for row in table:
        types.append(row["type"])
    return len(set(types)), set(types) 

def get_types():
    types=[]
    for row in table:
        types.append(row["type"])
    return set(types)

def median_dog_food_ubutu():
    prices=[]
    for row in table:
        if row["type"]=="dog_food" and row["company"]=="UBUTU":
            prices.append(int(row["price"]))
    return statistics.median(prices)

def average_per_type():
    types=get_types()
    averages=[]
    for t in types:
        prices=[]
        for row in table:
            if row["type"]==t:
                prices.append(int(row["price"]))
        averages.append(statistics.mean(prices))
    return dict(zip(types, averages))


print("the max price is", max_price())
print("the avg dog food price is", average_dog_food())
print("number of dog food companies:", count_dog_food_companies()[0], "the companies are:", count_dog_food_companies()[1])
print("number of types:", count_types()[0], "the types are:", count_types()[1])
print("the median price of UBUTU dog food is", median_dog_food_ubutu())
print("the average per type is:", average_per_type())
