
users={"tal":"abc123", "admin":"1234"}

users["new"]="new_value"

u=users.pop("tal")

i=users.popitem()

print(users.items())

print(u)

print(i)