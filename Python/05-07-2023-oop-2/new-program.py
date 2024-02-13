import pickle
from my_classes import Contact, load, save

contacts_new=load()

for contact in contacts_new:
    contact.print_me()

new_contact=Contact(name="new", phone="054-44444", email="n@n.com")
print(new_contact)
contacts_new.append(new_contact)
print(contacts_new)
save(contacts_new)


