def average(num_list, precision):
    return round(sum(num_list)/len(num_list), precision)

prices=[]

for num in range(5):
    price=float(input("price: "))
    precision=int(input("precision: "))
    prices.append(price)
    print(average(prices, 8))








