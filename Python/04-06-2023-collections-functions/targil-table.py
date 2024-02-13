flight1={"Destination":"Prague", "Price":400}
flight2={"Destination":"London", "Price":450}
flight3={"Destination":"Madrid", "Price":350, "time":"12:00"}

flights=[flight1, flight2, flight3]

total=0
num=len(flights)

print("Destination Price")

for flight in flights:
    print(flight["Destination"], flight["Price"])
    total+=flight["Price"]
    print(flight["time"])

print("Average Price:", total/num)

flights={"Prague":flight1, "London":flight2, "Madrid":flight3}

flights["Madrid"]["time"]

