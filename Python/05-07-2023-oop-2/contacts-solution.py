# targil 1

class Contact:
    def __init__(self, name="def", phone="def", email="def"):
        self.name=name
        self.phone=phone
        self.email=email

    # targil 3
    def print_me(self):
        print(f"{self.name}\t{self.phone}\t{self.email}")

tal=Contact(name="tal", phone="052-222222", email="t@t.com")
raz=Contact(name="raz", phone="053-333333", email="r@r.com")
default=Contact()

# targil 2

print(tal.name, tal.phone, tal.email)
print(raz.phone)
print(default.name, default.phone, default.email)

# targil 3

# tal.print_me()
# raz.print_me()
# default.print_me()

# targil 4

contacts=[tal, raz]

# targil 5

# for contact in contacts:
#     contact.print_me()

import pickle

with open("contacts.pickle", "wb") as f:
    pickle.dump(contacts, f)

with open("contacts.pickle", "rb") as f:
    contacts_new=pickle.load(f)

for contact in contacts_new:
    contact.print_me()
