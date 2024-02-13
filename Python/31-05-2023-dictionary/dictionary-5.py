
users={"tal":"abc123", "admin":"1234"}

print(users["tal"])

users["miki"]="miki_value"
users.popitem()
print(users.get("miki", "unknown user"))



