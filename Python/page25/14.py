# solution 14b in solutions book

num=int(input("enter number: "))

mun=0

while num >0:
    last_digit=num%10
    mun=10*mun
    mun=mun+last_digit
    num=num//10
print(mun)
    

