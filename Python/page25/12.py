# based on 11.py

num=int(input("enter number: "))

sum=0

while num>0:
    sum+=num%10
    num=num//10
print(sum)