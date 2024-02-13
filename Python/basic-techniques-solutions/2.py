# מבוסס על תפריט מתרגיל רשימת קניות

# אנשי קשר

contacts=[]

while True:
    option=input("1) add contact 2) show contacts 3) clear 4) Exit ")
    if option=="1":
        name=input("enter contact name: ")
        phone=input("enter contact phone: ")
        contacts.append(name+", "+phone)
    if option=="2":
        for item in contacts:
            print(item)
    if option=="3":
        contacts=[]
        print("list is cleared")
    if option=="4":
        break

