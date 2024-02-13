# פונקציה שמקבלת מספר ומחזירה אותו כפול 5
def mul_5(num):
    return num*5

# פונקציה שמקבלת שני מספרים ומחזירה את המכפלה שלהם
def mul_2(num1, num2):
    return num1*num2

# פונקציה שמקבלת מחיר ומחזירה מחיר אחרי 10 אחוז הנחה
def discount_10(price):
    return int(price*0.9)

# פונקציה שמקבלת מחיר ואחוז הנחה מחזירה מחיר אחרי אחוז ההנחה
def discount_n(price, discount):
    return int(price*(1-(discount/100)))

# פונקציה שמקבלת שם ומחזירה מחרוזת "hello, שם"
def hello(name):
    return f"hello, {name}"

# פונקציה שמקבלת שתי מחרוזות ומחזירה אותן מחוברות
def connect(s1, s2):
    return s1+s2

# פונקציה שמקבלת שתי מחרוזות ומחזירה אותן מופרדות בפסיקים
def comma(s1,s2):
    return f"{s1}, {s2}"

print("your price is: ", 100, "and your price after 5 discount is", discount_n(100, 5), "after 20 discount the price is", discount_n(100, 20))

print("your price is: ", 100, "and your price after discount is", discount_10(100))

while True:
    option=input("choose a solution: ")
    if option=="1":
        print(hello("tal"))
    if option=="2":
        print(comma("product", "price"))
    if option=="4":
        break