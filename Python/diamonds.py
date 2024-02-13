# פתרון למבחן יהלומים

import statistics

f = open("diamonds.csv")
rows = f.readlines()

table = []
for row in rows[1:]:
    table.append(dict(zip(rows[0].strip('\n').replace(' ', '').split(
        ','), row.strip('\n').replace(' ', '').split(','))))


def most_expensive_diamond():
    prices = []
    for row in table:
        prices.append(int(row["price"]))
    return max(prices)


def average_price():
    prices = []
    for row in table:
        prices.append(int(row["price"]))
    return round(statistics.mean(prices),2)


def count_ideals():
    ideals = []
    for row in table:
        if row["cut"] == "Ideal":
            ideals.append(row)
    return len(ideals)


def count_colors():
    types = []
    for row in table:
        types.append(row["color"])
    return len(set(types)), set(types)


def median_carat_premium():
    carats = []
    for row in table:
        if row["cut"] == "Premium":
            carats.append(float(row["carat"]))
    return statistics.median(carats)

def count_cuts():
    cuts = []
    for row in table:
        cuts.append(row["cut"])
    return len(set(cuts)), set(cuts)


def average_carat_cut():
    averages = dict()
    cuts = count_cuts()[1]
    for cut in cuts:
        carats = []
        for row in table:
            if row["cut"] == cut:
                carats.append(float(row["carat"]))
        averages[cut] = round(statistics.mean(carats),3)
    return averages

def average_price_color():
    averages = dict()
    colors = count_colors()[1]
    for color in colors:
        prices = []
        for row in table:
            if row["color"] == color:
                prices.append(int(row["price"]))
        averages[color] = int(statistics.mean(prices))
    return averages


print(most_expensive_diamond())
print(average_price())
print(count_ideals())
print(count_colors())
print(median_carat_premium())
print(average_carat_cut())
print(average_price_color())