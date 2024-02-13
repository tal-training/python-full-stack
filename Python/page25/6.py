# based on 5.py

num=int(input("enter number: "))

sum=0
counter=0

while num!=0:
    if num>0:
        sum+=num
        counter+=1
    num=int(input("enter number: "))

if counter!=0:
    print("the average is: ", sum/counter)
else:
    print("no positive numbers were given")
