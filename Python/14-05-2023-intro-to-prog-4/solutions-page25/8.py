# תרגיל 8

num=int(input("enter a positive integer: "))

if num>0:
    minimum=num

else:
    print("no positive numbers, exiting!")
    exit()


while num>0:  
    num=int(input("enter a positive integer: "))
    if num<=0:
        print(minimum)
        exit()
    if num < minimum:
        minimum=num 

print(minimum)



