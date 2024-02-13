
num=int(input("enter a positive integer: "))

mysum=0

if num>0:
    mysum=num

while num>0:  
    num=int(input("enter a positive or zero integer: "))
    if num >=0:
        mysum=mysum+num

print(mysum)


