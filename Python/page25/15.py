# based on 14.py

num=int(input("enter number: "))
original=num
mun=0

while num > 0:
    last_digit=num%10
    mun=10*mun
    mun=mun+last_digit
    num=num//10

if original==mun:
    print(original, "is a palindrom")
else:
    print(original, "is not a palindrom")

    

