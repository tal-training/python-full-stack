contacts={}

name=input("Enter new contact name: ")
phone=input("Enter new contact phone: ")

contacts[name]=phone

print(contacts.items())

name=input("Enter contact to get phone number: ")

print(contacts.get(name, "no such contact"))

name=input("Enter contact to delete: ")

deleted_phone=contacts.pop(name)

print(contacts.items())

print("deleted: ", name, deleted_phone)

contacts.clear()