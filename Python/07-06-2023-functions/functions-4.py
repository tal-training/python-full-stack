def is_bigger_3(some_string):
    if len(some_string)>3:
        return True
    else:
        return False

print(is_bigger_3("aaaa"))
print(is_bigger_3("aa"))

# שכללו את הפונקציה הנ"ל כך שתקבל את הגודל של המחרוזת שצריך לבדוק, לא רק 3
def is_bigger_n(some_string, num):
    if len(some_string)>num:
        return True
    else:
        return False

print(is_bigger_n("aarerwerwerwer", 10))
