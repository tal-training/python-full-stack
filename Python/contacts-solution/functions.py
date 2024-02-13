from files import load_contacts, save_contacts
from classes import Contact

def add(name="name", phone="phone"):
    contacts=load_contacts()
    contacts.append(Contact(name=name, phone=phone))
    save_contacts(contacts)

def view():
    contacts=load_contacts()
    print(contacts)

def delete(name="name"):
    contacts=load_contacts() 
    for contact in contacts.copy():
        if contact.name==name:
            contacts.remove(contact)
    save_contacts(contacts)

def update(name="name", new_name="nn", new_phone="np"):
    delete(name)
    add(name=new_name, phone=new_phone)
    

