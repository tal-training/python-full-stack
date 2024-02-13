def create_new_contacts():
    with open("contacts.pickle", 'wb') as f:
        pickle.dump([], f)

def update(contact:dict={}):
    with open("contacts.pickle", 'rb') as f:
        try: 
            loaded_contacts=pickle.load(f)
        except:
            create_new_contacts()

update({"name":"tal", "phone":"052-433244"})
update({"name":"gal", "phone":"053-433246"})
update({"name":"yal", "phone":"055-433248"})