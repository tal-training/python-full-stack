# תרגיל 7

num=int(input("enter a positive integer: "))

if num>0:
    maximum=num
else:
    print("no positive numbers, exiting!")
    exit()

while num>0:  
    num=int(input("enter a positive integer: "))
    if num<=0:
        print(maximum)
        exit()
    if num > maximum:
        maximum=num 

print(maximum)


