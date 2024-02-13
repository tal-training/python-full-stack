num=int(input("enter number: "))

sum=0

while num!=-99:
    if num>=0:
        sum+=num
    else:
        print("the number is negative so it won't be added")
    num=int(input("enter number: "))

print("the sum is: ", sum)
