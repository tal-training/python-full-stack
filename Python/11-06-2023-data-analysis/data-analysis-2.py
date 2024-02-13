stocks="Google, 120\nAmazon, 520\nMicrosoft, 800"

def get_stocks_table(data_string):
    data_list=data_string.replace(" ", "").split('\n')
    list_of_dictionaries=[]

    keys=["name", "price"]

    for line in data_list:
        values=line.split(',')
        row=dict(zip(keys, values))
        list_of_dictionaries.append(row)
    
    return list_of_dictionaries

print(get_stocks_table(stocks))

