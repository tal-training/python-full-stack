import pickle
from classes import Contact

def load_contacts():
    try:
        with open("contacts.pickle", "rb") as f:
            contacts=pickle.load(f)
            return contacts
    except:
        with open("contacts.pickle", "wb") as f:
            pickle.dump([], f)
            return []


def save_contacts(contacts):
    with open("contacts.pickle", "wb") as f:
        pickle.dump(contacts, f)
