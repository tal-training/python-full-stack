# based on 7.py (find maximum)

num=int(input("enter number: "))

maximum=num
counter=0
max_counter=0

while counter<100 and num!=-1:
    if num>maximum:
        maximum=num
        max_counter=counter
    num=int(input("enter number: "))
    counter+=1

print("the max counter is: ", max_counter+1)
