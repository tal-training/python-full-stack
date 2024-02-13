months=input("Enter months for vacation: ")

months=set(months.replace(' ', '').upper().split(',')).intersection({"JULY", "AUGUST", "JUNE"})

if len(months)>0:
    print(f"The months {', '.join(months)} are high season, more expensive")



