# based on 12.py

X=int(input("enter X: "))
dig=int(input("enter dig between 0 and 10: "))

counter=0

while X>0:
    if X%10 == dig:
        counter+=1
    X=X//10
print(counter)