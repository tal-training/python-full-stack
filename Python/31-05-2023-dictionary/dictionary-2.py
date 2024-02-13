
grades={"tal":90, "shai":90}

users={"tal":"abc123", "admin":"1234"}

grades.update({"yosi":99, "kobi":80})

grades["yosi"]=100

grades["new"]=111

print("keys:", grades.keys())
print("values:",grades.values())

print(grades)