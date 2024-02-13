# מבוסס על תפריט מתרגיל כספומט

# רשימת קניות
shopping_list=[]

while True:
    option=input("1) add item 2) show items 3) clear 4) Exit ")
    if option=="1":
        item=input("enter a new item: ")
        shopping_list.append(item)
    if option=="2":
        for item in shopping_list:
            print(item)
    if option=="3":
        shopping_list=[]
        print("list is cleared")
    if option=="4":
        break

