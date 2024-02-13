
def get_stocks_table(data_string):
    data_list=data_string.replace(" ", "").split('\n')
    list_of_dictionaries=[]

    keys=["name", "price"]

    for line in data_list:
        values=line.split(',')
        row=dict(zip(keys, values))
        list_of_dictionaries.append(row)
    
    return list_of_dictionaries


cars="BMW, 180\nAudi, 520\nToyota, 100"

print(get_stocks_table(cars))
