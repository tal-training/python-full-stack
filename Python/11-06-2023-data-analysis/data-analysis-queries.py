stocks="Meta, 410\nGoogle, 120\nAmazon, 520\nMicrosoft, 800"

def get_stocks_table(data_string):
    data_list=data_string.replace(" ", "").split('\n')
    list_of_dictionaries=[]

    keys=["name", "price"]

    for line in data_list:
        values=line.split(',')
        row=dict(zip(keys, values))
        list_of_dictionaries.append(row)
    
    return list_of_dictionaries


def get_price(name, table):
    for item in table:
        if item["name"]==name:
            return int(item["price"])

table=get_stocks_table(stocks)

# Targil 1
def get_price_400():
    stock_list=[]
    for stock in table:
        if int(stock["price"])>400:
            stock_list.append(stock["name"])
    return stock_list

# Targil 2
def get_price_400_name(name):
    # אפשר להשתמש בפונקציה get_price
    if get_price(name, table)>400:
        return True
    else:
        return False

# Targil 3
def check_price(name, price):
    # אפשר להשתמש בפונקציה get_price
    if get_price(name, table)>price:
        return True
    else:
        return False


print(check_price("Amazon", 900))



