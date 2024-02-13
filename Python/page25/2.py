a=int(input("enter number: "))
b=int(input("enter number: "))

if b<a:
    tmp=a
    a=b
    b=tmp

counter=a

while counter<=b:
    print(counter)
    counter=counter+1