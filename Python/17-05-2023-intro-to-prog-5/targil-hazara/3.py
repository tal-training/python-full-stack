days=input("how many days in a year? ")
counter=1

while days!="365":
    counter+=1
    print("try again :(")
    days=input("how many days in a year? ")

if counter==1:
    print("great!")
elif counter<=3:
    print("good job!", "you had", counter, "turns")
else:
    print("you had", counter, "turns, try harder next time!")


