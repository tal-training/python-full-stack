num=int(input("enter number: "))

counter=0

while num>0:
    num=num//10
    counter+=1
print(counter)