# login

username=input("enter username: ")
password=input("enter password: ")

counter=1

login=False

while :
    if username=="admin" and password=="abcd":
        unauthorized=False
        print("welcome")
    else:
        print("unauthorized", "tries:", counter)
        counter+=1
        if counter==4:
            print("policy violation")
            break
        username=input("enter username: ")
        password=input("enter password: ")

print("out of the loop")
