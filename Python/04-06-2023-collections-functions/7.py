users={
1:
    {"name":"tal", "phone":"052-222222", "email":"tal@tal.com"},
2:
    {"name":"gal", "phone":"053-333333", "email":"gal@gal.com"}
}

for i in range(5):
    next_key=len(users)+1

    users[next_key]= {"name":"shani", "phone":"053-333333", "email":"shani@gal.com"}

print(users)

