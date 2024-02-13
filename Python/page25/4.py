den=int(input("enter den: "))
max=int(input("enter max: "))

counter=1

while counter<=max:
    if counter%den==0:
        print(counter)
    counter=counter+1