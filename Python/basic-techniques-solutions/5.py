
# אנשי קשר

contacts=[]

while True:
    option=input("1) Add contact 2) Show contacts 3) Clear 4) Search 5) Show Names 6) Show Numbers 7) Exit ")
    if option=="1":
        name=input("enter contact name: ")
        phone=input("enter contact phone: ")
        contacts.append([name,phone])
    if option=="2":
        for item in contacts:
            print(item)
    if option=="3":
        contacts=[]
        print("list is cleared")
    if option=="4":
        name=input("enter contact name to find: ")
        for contact in contacts:
            if name==contact[0]:
                print(name, "number is", contact[1])
    if option=="5":
        for contact in contacts:
            print(contact[1])
    if option=="6":
        for contact in contacts:
            print(contact[0])
    if option=="7":
        break
    


