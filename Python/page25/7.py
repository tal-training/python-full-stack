num=int(input("enter number: "))

maximum=num

while num>0:
    if num>maximum:
        maximum=num
    num=int(input("enter number: "))

print("the max is: ", maximum)
