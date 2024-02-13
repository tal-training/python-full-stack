stocks="Google, 120\nAmazon, 520\nMicrosoft, 800"
# 1. להפוך את המחרוזת לרשימה של מילונים
# Split, replace
# מטרה סופית:
# {"name":"Google", "price":120}
# [{"name":"Google", "price":120}, {"name":"Amazon", "price":520}]
stocks_list=stocks.replace(" ", "").split('\n')

print(stocks_list)

list_of_dictionaries=[]

keys=["name", "price"]

for line in stocks_list:
    values=line.split(',')
    row=dict(zip(keys, values))
    list_of_dictionaries.append(row)

print(list_of_dictionaries)