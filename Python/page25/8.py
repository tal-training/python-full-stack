# based on 7.py 

num=int(input("enter number: "))

minimum=num

while num>0:
    if num<minimum:
        minimum=num
    num=int(input("enter number: "))

print("the minimum is: ", minimum)
