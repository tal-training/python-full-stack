# login dictionary

users={"admin":"admin123"}

username=input("enter user name: ")
password=input("enter password: ")

result=users.get(username)

if result==password:
    print("welcome")
else:
    print("unauthorized")