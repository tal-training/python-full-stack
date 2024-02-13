# based on maximum from 7.py

counter=0
maximum=-10000000000

while counter<5:  
    num=int(input("enter an integer: "))
    counter=counter+1
    if num > maximum:
        maximum=num
        max_counter=counter

print("index: ",max_counter, "value", maximum)
