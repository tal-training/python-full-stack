from data import load, save, Contact

def create():
    contacts=load()
    name=input("name? ")
    email=input("email? ")
    address=input("address? ")
    phone=input("phone? ")
    new_contact=Contact(name=name, phone=phone, email=email, address=address)
    contacts.append(new_contact)
    save(contacts)
    print("new contact added")

