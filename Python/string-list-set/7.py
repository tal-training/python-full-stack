month=input("Enter Month: ")
      
if len({month.lower()}.intersection({"july", "august", "june"})) == 0:
    print("No")
else:
    print("Yes")
