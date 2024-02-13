month1=input("Enter Month: ")
month2=input("Enter Month: ")
      
if len({month1.lower(), month2.lower()}.intersection({"july", "august", "june"})) == 2:
    print("Yes")
else:
    print("No")
