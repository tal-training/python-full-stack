
from .models import Contact

def add(name="name", phone="phone"):
    Contact(name=name, phone=phone).save()

# def view():
#     contacts=load_contacts()
#     return contacts

# def delete(name="name"):
#     contacts=load_contacts() 
#     for contact in contacts.copy():
#         if contact.name==name:
#             contacts.remove(contact)
#     save_contacts(contacts)

# def update(name="name", phone="phone"):
#     delete(name)
#     add(name=name, phone=phone)    
