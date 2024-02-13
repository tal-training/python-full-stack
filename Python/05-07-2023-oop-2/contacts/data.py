import pickle

class Contact:
    def __init__(self, name="def", phone="def", email="def", address="default address"):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

    def __repr__(self):
        return self.name        

    def print_me(self):
        print(f"{self.name}\t{self.phone}\t{self.email}")

    def set_property(self, property, value):
        if property=="name":
            self.name==value

def save(list_to_save):
    with open("contacts.pickle", "wb") as f:
        pickle.dump(list_to_save, f)

def load():
    with open("contacts.pickle", "rb") as f:
        loaded_contacts=pickle.load(f)
    return loaded_contacts

def setup():
    try:
        with open("contacts.pickle", "rb") as f:
            print("file exists, continuing...")
    except:
        with open("contacts.pickle", "wb") as f:
            pickle.dump([], f)


