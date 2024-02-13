from files import load_contacts, save_contacts
from classes import Contact

def add(name="name", phone="phone"):
    contacts=load_contacts()
    contacts.append(Contact(name=name, phone=phone))
    save_contacts(contacts)

def view():
    contacts=load_contacts()
    return contacts

def delete(name="name"):
    contacts=load_contacts() 
    for contact in contacts.copy():
        if contact.name==name:
            contacts.remove(contact)
    save_contacts(contacts)

def update(name="name", phone="phone"):
    delete(name)
    add(name=name, phone=phone)    
