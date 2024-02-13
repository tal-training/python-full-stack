balance=0

while True:
    option=input("1) withdraw 2) deposit 3) balance 4) Exit ")
    if option=="1":
        withdraw=int(input("how much to withdraw?"))
        if balance>withdraw:
            balance=balance-withdraw
            print("OK, balance:", balance)
        else:
            print("not enough money, balance: ", balance)
    if option=="2":
        deposit=int(input("how much to deposit?"))
        balance=balance+deposit
        print("OK, balance:", balance)
    if option=="3":
        print("OK, balance:", balance)
    if option=="4":
        break



