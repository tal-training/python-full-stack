months=input("Enter Months: ")

months=months.split(',')

new_list=[]

for month in months:
    new_list.append(month.strip(' ')[:3])

print(new_list)
