f=open("cars.csv", 'w')
f.write("hi")
f.write("\nthis is a new line")
f.close()


f=open("cars.csv", 'a')
f.write("\nthis is a new line")

with open("cars1.csv", 'a') as f:
    f.write("\nthis is some new content")

ff=open("cars5.csv")

